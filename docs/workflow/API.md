# Search Console multi-account MCP: executable interfaces

## Purpose

| Question | Answer |
| --- | --- |
| **Whom?** | SEO analyst investigating explicitly authorized Search Console properties. |
| **What?** | 17 tools: list_accounts, set_default_account, reauthenticate, list_properties, get_site_details, get_search_analytics, get_performance_overview, compare_periods, get_advanced_search_analytics, get_search_by_page, inspect_url, batch_inspect_urls, check_indexing_issues, list_sitemaps, get_sitemap, submit_sitemap, delete_sitemap. |
| **Where?** | gsc/server.py, tests/test_server.py. |
| **Why it exists?** | Search Console multi-account MCP needs this document to prevent unsupported parameters or misleading success results from guiding an action. |
| **Why this approach?** | 17 tools: list_accounts, set_default_account, reauthenticate, list_properties, get_site_details, get_search_analytics, get_performance_overview, compare_periods, get_advanced_search_analytics, get_search_by_page, inspect_url, batch_inspect_urls, check_indexing_issues, list_sitemaps, get_sitemap, submit_sitemap, delete_sitemap. |
| **Why it matters?** | Credential profile and site_url are distinct inputs. |

## Exact current interface

17 tools: list_accounts, set_default_account, reauthenticate, list_properties, get_site_details, get_search_analytics, get_performance_overview, compare_periods, get_advanced_search_analytics, get_search_by_page, inspect_url, batch_inspect_urls, check_indexing_issues, list_sitemaps, get_sitemap, submit_sitemap, delete_sitemap. Analytics require site_url,start_date,end_date; default dimensions=[query], row_limit=25. Basic/advanced/page tools clamp rows to 1..1000 and send dataState=all. compare_periods requests both periods, joins dimension keys, calculates click/impression deltas and sorts by absolute click change; its row_limit is not clamped like the other handlers. Single inspection sends inspectionUrl and siteUrl. Batch and issue summaries allow at most ten URLs per call, a local contract rather than independently verified provider-wide limit. Sitemap writes take site_url,sitemap_url,account?. Most errors are {error: message}; batch errors remain per URL. HTTP 429/500/502/503/504 retry up to five attempts; 401 suggests reauthentication, 403 property access, 404 exact property syntax. stdio is default; optional SSE defaults 127.0.0.1:3001.

## Complete registered signatures

These signatures are transcribed from the current Python handler definitions. Optional defaults are source behavior; effect labels distinguish configuration/authentication changes from reporting.

| Handler signature | Effect |
| --- | --- |
| `list_accounts()` | provider read or local discovery |
| `set_default_account(account: str)` | persistent configuration write |
| `reauthenticate(account: Optional[str]=None)` | token invalidation/authentication |
| `list_properties(account: Optional[str]=None)` | provider read or local discovery |
| `get_site_details(site_url: str, account: Optional[str]=None)` | provider read or local discovery |
| `get_search_analytics(site_url: str, start_date: str, end_date: str, dimensions: Optional[list[str]]=None, row_limit: int=25, account: Optional[str]=None)` | provider read or local discovery |
| `get_performance_overview(site_url: str, start_date: str, end_date: str, account: Optional[str]=None)` | provider read or local discovery |
| `compare_periods(site_url: str, period1_start: str, period1_end: str, period2_start: str, period2_end: str, dimensions: Optional[list[str]]=None, row_limit: int=25, account: Optional[str]=None)` | provider read or local discovery |
| `get_advanced_search_analytics(site_url: str, start_date: str, end_date: str, dimensions: Optional[list[str]]=None, filters: Optional[list[dict]]=None, row_limit: int=25, account: Optional[str]=None)` | provider read or local discovery |
| `get_search_by_page(site_url: str, page_url: str, start_date: str, end_date: str, row_limit: int=25, account: Optional[str]=None)` | provider read or local discovery |
| `inspect_url(site_url: str, page_url: str, account: Optional[str]=None)` | provider read or local discovery |
| `batch_inspect_urls(site_url: str, page_urls: list[str], account: Optional[str]=None)` | provider read or local discovery |
| `check_indexing_issues(site_url: str, page_urls: list[str], account: Optional[str]=None)` | provider read or local discovery |
| `list_sitemaps(site_url: str, account: Optional[str]=None)` | provider read or local discovery |
| `get_sitemap(site_url: str, sitemap_url: str, account: Optional[str]=None)` | provider read or local discovery |
| `submit_sitemap(site_url: str, sitemap_url: str, account: Optional[str]=None)` | external write |
| `delete_sitemap(site_url: str, sitemap_url: str, account: Optional[str]=None)` | external write |

## Authorization and error limits

GSC_ALLOW_DESTRUCTIVE is checked for nonempty presence, not parsed as the literal true: a value such as false still enables the code path. Treat this as a known implementation gap; actual operator approval is separate. Reauthenticate may delete a token and rebuild authentication; deletion occurs only for an explicit type="oauth" profile with an existing token_file. An omitted type still builds an OAuth client but does not trigger that unlink branch, so fresh consent is not guaranteed. set_default_account writes configuration. SSE has no separately implemented application authentication in this source. Read-only reports still expose private site data.

## Contract gaps

1. Strict destructive-flag parsing is absent. 2. compare_periods does not clamp row_limit or prove complete pagination; results are bounded comparisons. 3. Current tests cover guards and registration rather than provider response semantics. 4. Cached authenticated status is weaker than live access. Proposed first work is contract/guard regression coverage for the exact requested operation; no current operator-ranked backlog was recovered.

5. Reauthentication has inconsistent default-type handling: building a profile with omitted type uses OAuth, but invalidation only unlinks an explicit OAuth profile token. Inspect the selected profile metadata within authorized recovery scope and test explicit/implicit OAuth plus service-account branches before promising a forced new login. Do not inspect or delete token values just to validate documentation.

## Supporting sources

- [gsc/server.py](../../gsc/server.py)
- [tests/test_server.py](../../tests/test_server.py)

## Continue

Return to [INDEX.md](../../INDEX.md) and finish all routes relevant to the latest task before acting. After verification, update affected owning facts, REPORT and HANDOFFS.
