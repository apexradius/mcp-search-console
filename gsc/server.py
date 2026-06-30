import functools
import inspect
import os
from typing import Optional

from fastmcp import FastMCP

from gsc.accounts import AccountManager, AccountError
from gsc.retry import with_retry

mcp = FastMCP("mcp-search-console")
manager = AccountManager()


def _safe(fn):
    """Return structured error dicts instead of raising — keeps MCP responses clean.
    Preserves the original function signature so fastmcp can build the tool schema."""
    @functools.wraps(fn)
    def wrapper(*args, **kwargs):
        try:
            return fn(*args, **kwargs)
        except AccountError as e:
            return {"error": str(e)}
        except RuntimeError as e:
            return {"error": str(e)}
        except Exception as e:
            return {"error": f"Unexpected error: {type(e).__name__}: {str(e)}"}
    wrapper.__signature__ = inspect.signature(fn)
    return wrapper


# ---------------------------------------------------------------------------
# Account management tools
# ---------------------------------------------------------------------------

@mcp.tool()
@_safe
def list_accounts() -> list[dict]:
    """List all configured GSC accounts and which is the current default."""
    return manager.list_accounts()


@mcp.tool()
@_safe
def set_default_account(account: str) -> dict:
    """Set the default account used when no account is specified in other tools."""
    manager.set_default(account)
    return {"success": True, "default": account}


@mcp.tool()
@_safe
def reauthenticate(account: Optional[str] = None) -> dict:
    """
    Force re-authentication for an account. Clears the cached token and re-runs
    the OAuth flow (or reloads service account credentials). Useful when a token
    has been revoked or you need to switch Google accounts.
    """
    manager.invalidate(account)
    manager.get_client(account)
    return {"success": True, "account": account or manager._config.get("default")}


# ---------------------------------------------------------------------------
# GSC property tools
# ---------------------------------------------------------------------------

@mcp.tool()
@_safe
def list_properties(account: Optional[str] = None) -> list[dict]:
    """List all Google Search Console properties for the specified account."""
    service = manager.get_client(account)
    response = with_retry(service.sites().list().execute)
    sites = response.get("siteEntry", [])
    return [{"url": s["siteUrl"], "permission_level": s.get("permissionLevel")} for s in sites]


@mcp.tool()
@_safe
def get_site_details(site_url: str, account: Optional[str] = None) -> dict:
    """Get verification and permission details for a specific GSC property."""
    service = manager.get_client(account)
    return with_retry(service.sites().get(siteUrl=site_url).execute)


# ---------------------------------------------------------------------------
# Search analytics tools
# ---------------------------------------------------------------------------

@mcp.tool()
@_safe
def get_search_analytics(
    site_url: str,
    start_date: str,
    end_date: str,
    dimensions: Optional[list[str]] = None,
    row_limit: int = 25,
    account: Optional[str] = None,
) -> dict:
    """
    Fetch search analytics data (clicks, impressions, CTR, position).

    Args:
        site_url: GSC property URL (e.g. 'https://example.com' or 'sc-domain:example.com')
        start_date: Start date in YYYY-MM-DD format
        end_date: End date in YYYY-MM-DD format
        dimensions: List of dimensions — any of ['query', 'page', 'country', 'device', 'date']
        row_limit: Number of rows to return (default 25, max 1000)
        account: Account name from config (uses default if omitted)
    """
    service = manager.get_client(account)
    body = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": dimensions or ["query"],
        "rowLimit": min(max(1, row_limit), 1000),
        "dataState": "all",
    }
    return with_retry(service.searchanalytics().query(siteUrl=site_url, body=body).execute)


@mcp.tool()
@_safe
def get_performance_overview(
    site_url: str,
    start_date: str,
    end_date: str,
    account: Optional[str] = None,
) -> dict:
    """
    Get a high-level performance summary: total clicks, impressions, CTR, average position.
    No dimension breakdown — use get_search_analytics for that.
    """
    service = manager.get_client(account)
    body = {"startDate": start_date, "endDate": end_date, "dataState": "all"}
    response = with_retry(service.searchanalytics().query(siteUrl=site_url, body=body).execute)
    rows = response.get("rows", [])
    if rows:
        r = rows[0]
        totals = {
            "clicks": r.get("clicks", 0),
            "impressions": r.get("impressions", 0),
            "ctr": round(r.get("ctr", 0) * 100, 2),
            "position": round(r.get("position", 0), 1),
        }
    else:
        totals = {"clicks": 0, "impressions": 0, "ctr": 0.0, "position": 0.0}
    return {"site_url": site_url, "period": f"{start_date} to {end_date}", **totals}


@mcp.tool()
@_safe
def compare_periods(
    site_url: str,
    period1_start: str,
    period1_end: str,
    period2_start: str,
    period2_end: str,
    dimensions: Optional[list[str]] = None,
    row_limit: int = 25,
    account: Optional[str] = None,
) -> dict:
    """
    Compare search performance between two date ranges.
    Returns rows for both periods side-by-side with delta calculations.
    """
    service = manager.get_client(account)
    dims = dimensions or ["query"]

    def fetch(start, end):
        body = {
            "startDate": start,
            "endDate": end,
            "dimensions": dims,
            "rowLimit": row_limit,
            "dataState": "all",
        }
        return with_retry(service.searchanalytics().query(siteUrl=site_url, body=body).execute)

    p1 = fetch(period1_start, period1_end)
    p2 = fetch(period2_start, period2_end)

    def key(row):
        return tuple(row.get("keys", []))

    p1_index = {key(r): r for r in p1.get("rows", [])}
    p2_index = {key(r): r for r in p2.get("rows", [])}

    comparison = []
    for k in set(p1_index) | set(p2_index):
        r1 = p1_index.get(k, {})
        r2 = p2_index.get(k, {})
        comparison.append({
            "keys": list(k),
            "period1": {m: r1.get(m, 0) for m in ["clicks", "impressions", "ctr", "position"]},
            "period2": {m: r2.get(m, 0) for m in ["clicks", "impressions", "ctr", "position"]},
            "delta_clicks": r2.get("clicks", 0) - r1.get("clicks", 0),
            "delta_impressions": r2.get("impressions", 0) - r1.get("impressions", 0),
        })

    comparison.sort(key=lambda x: abs(x["delta_clicks"]), reverse=True)
    return {"dimensions": dims, "rows": comparison[:row_limit]}


@mcp.tool()
@_safe
def get_advanced_search_analytics(
    site_url: str,
    start_date: str,
    end_date: str,
    dimensions: Optional[list[str]] = None,
    filters: Optional[list[dict]] = None,
    row_limit: int = 25,
    account: Optional[str] = None,
) -> dict:
    """
    Advanced search analytics with dimension filters.

    filters format: [{"dimension": "country", "operator": "equals", "expression": "usa"}]
    operators: equals, notEquals, contains, notContains, includingRegex, excludingRegex
    """
    service = manager.get_client(account)
    body = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": dimensions or ["query"],
        "rowLimit": min(max(1, row_limit), 1000),
        "dataState": "all",
    }
    if filters:
        body["dimensionFilterGroups"] = [{"filters": filters}]
    return with_retry(service.searchanalytics().query(siteUrl=site_url, body=body).execute)


@mcp.tool()
@_safe
def get_search_by_page(
    site_url: str,
    page_url: str,
    start_date: str,
    end_date: str,
    row_limit: int = 25,
    account: Optional[str] = None,
) -> dict:
    """Get search queries driving traffic to a specific page URL."""
    service = manager.get_client(account)
    body = {
        "startDate": start_date,
        "endDate": end_date,
        "dimensions": ["query"],
        "rowLimit": min(max(1, row_limit), 1000),
        "dataState": "all",
        "dimensionFilterGroups": [
            {"filters": [{"dimension": "page", "operator": "equals", "expression": page_url}]}
        ],
    }
    return with_retry(service.searchanalytics().query(siteUrl=site_url, body=body).execute)


# ---------------------------------------------------------------------------
# URL inspection tools
# ---------------------------------------------------------------------------

@mcp.tool()
@_safe
def inspect_url(
    site_url: str,
    page_url: str,
    account: Optional[str] = None,
) -> dict:
    """
    Inspect a URL's indexing status, last crawl date, mobile usability,
    and rich result eligibility.
    """
    service = manager.get_client(account)
    body = {"inspectionUrl": page_url, "siteUrl": site_url}
    return with_retry(service.urlInspection().index().inspect(body=body).execute)


@mcp.tool()
@_safe
def batch_inspect_urls(
    site_url: str,
    page_urls: list[str],
    account: Optional[str] = None,
) -> list[dict]:
    """
    Inspect multiple URLs at once. Returns one result per URL.
    Maximum 10 URLs per call (GSC API limit).
    """
    if len(page_urls) > 10:
        return [{"error": "Maximum 10 URLs per batch. Split into multiple calls."}]

    service = manager.get_client(account)
    results = []
    for url in page_urls:
        try:
            body = {"inspectionUrl": url, "siteUrl": site_url}
            result = with_retry(service.urlInspection().index().inspect(body=body).execute)
            results.append({"url": url, "result": result})
        except (RuntimeError, Exception) as e:
            results.append({"url": url, "error": str(e)})
    return results


@mcp.tool()
@_safe
def check_indexing_issues(
    site_url: str,
    page_urls: list[str],
    account: Optional[str] = None,
) -> list[dict]:
    """
    Check a list of URLs for indexing problems. Returns a prioritised summary
    of issues — more actionable than raw inspect_url output.
    """
    if len(page_urls) > 10:
        return [{"error": "Maximum 10 URLs per call."}]

    service = manager.get_client(account)
    results = []
    for url in page_urls:
        try:
            body = {"inspectionUrl": url, "siteUrl": site_url}
            raw = with_retry(service.urlInspection().index().inspect(body=body).execute)
            ir = raw.get("inspectionResult", {})
            index_status = ir.get("indexStatusResult", {})
            verdict = index_status.get("verdict", "UNKNOWN")
            results.append({
                "url": url,
                "verdict": verdict,
                "coverage_state": index_status.get("coverageState", ""),
                "last_crawled": index_status.get("lastCrawlTime", "never"),
                "indexing_allowed": index_status.get("indexingAllowed"),
                "robots_txt_state": index_status.get("robotsTxtState"),
                "has_issues": verdict != "PASS",
            })
        except (RuntimeError, Exception) as e:
            results.append({"url": url, "error": str(e)})

    results.sort(key=lambda x: (0 if x.get("has_issues") else 1))
    return results


# ---------------------------------------------------------------------------
# Sitemap tools
# ---------------------------------------------------------------------------

@mcp.tool()
@_safe
def list_sitemaps(site_url: str, account: Optional[str] = None) -> list[dict]:
    """List all sitemaps submitted to GSC for this property."""
    service = manager.get_client(account)
    response = with_retry(service.sitemaps().list(siteUrl=site_url).execute)
    result = []
    for s in response.get("sitemap", []):
        errors = int(s.get("errors", 0))
        warnings = int(s.get("warnings", 0))
        result.append({
            "path": s.get("path"),
            "last_submitted": s.get("lastSubmitted"),
            "last_downloaded": s.get("lastDownloaded"),
            "is_pending": s.get("isPending"),
            "is_sitemaps_index": s.get("isSitemapsIndex"),
            "type": s.get("type"),
            "warnings": warnings,
            "errors": errors,
            "status": "Error" if errors > 0 else ("Has warnings" if warnings > 0 else "OK"),
        })
    return result


@mcp.tool()
@_safe
def get_sitemap(site_url: str, sitemap_url: str, account: Optional[str] = None) -> dict:
    """Get details and status of a specific sitemap."""
    service = manager.get_client(account)
    return with_retry(service.sitemaps().get(siteUrl=site_url, feedpath=sitemap_url).execute)


@mcp.tool()
@_safe
def submit_sitemap(
    site_url: str,
    sitemap_url: str,
    account: Optional[str] = None,
) -> dict:
    """Submit a sitemap to Google Search Console. Requires GSC_ALLOW_DESTRUCTIVE=true."""
    if not os.environ.get("GSC_ALLOW_DESTRUCTIVE"):
        return {
            "error": "Sitemap submission is disabled by default. "
            "Set GSC_ALLOW_DESTRUCTIVE=true to enable."
        }
    service = manager.get_client(account)
    with_retry(service.sitemaps().submit(siteUrl=site_url, feedpath=sitemap_url).execute)
    return {"success": True, "submitted": sitemap_url}


@mcp.tool()
@_safe
def delete_sitemap(
    site_url: str,
    sitemap_url: str,
    account: Optional[str] = None,
) -> dict:
    """Delete a sitemap from Google Search Console. Requires GSC_ALLOW_DESTRUCTIVE=true."""
    if not os.environ.get("GSC_ALLOW_DESTRUCTIVE"):
        return {
            "error": "Sitemap deletion is disabled by default. "
            "Set GSC_ALLOW_DESTRUCTIVE=true to enable."
        }
    service = manager.get_client(account)
    with_retry(service.sitemaps().delete(siteUrl=site_url, feedpath=sitemap_url).execute)
    return {"success": True, "deleted": sitemap_url}


# ---------------------------------------------------------------------------
# Entry point
# ---------------------------------------------------------------------------

def main():
    transport = os.environ.get("MCP_TRANSPORT", "stdio")
    if transport == "sse":
        host = os.environ.get("MCP_HOST", "127.0.0.1")
        port = int(os.environ.get("MCP_PORT", "3001"))
        mcp.run(transport="sse", host=host, port=port)
    else:
        mcp.run(transport="stdio")


if __name__ == "__main__":
    main()
