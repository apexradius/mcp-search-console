# Search Console multi-account MCP: available capability boundaries

## Purpose

| Question | Answer |
| --- | --- |
| **Whom?** | SEO analyst investigating explicitly authorized Search Console properties. |
| **What?** | 17 tools: list_accounts, set_default_account, reauthenticate, list_properties, get_site_details, get_search_analytics, get_performance_overview, compare_periods, get_advanced_search_analytics, get_search_by_page, inspect_url, batch_inspect_urls, check_indexing_issues, list_sitemaps, get_sitemap, submit_sitemap, delete_sitemap. |
| **Where?** | README.md, pyproject.toml, gsc/server.py. |
| **Why it exists?** | Search Console multi-account MCP needs this document to distinguish available implementation from authorized operation. |
| **Why this approach?** | Credential profile and site_url are distinct inputs. |
| **Why it matters?** | Credential profile and site_url are distinct inputs. |

## Implemented surface

17 tools: list_accounts, set_default_account, reauthenticate, list_properties, get_site_details, get_search_analytics, get_performance_overview, compare_periods, get_advanced_search_analytics, get_search_by_page, inspect_url, batch_inspect_urls, check_indexing_issues, list_sitemaps, get_sitemap, submit_sitemap, delete_sitemap. Analytics require site_url,start_date,end_date; default dimensions=[query], row_limit=25. Basic/advanced/page tools clamp rows to 1..1000 and send dataState=all. compare_periods requests both periods, joins dimension keys, calculates click/impression deltas and sorts by absolute click change; its row_limit is not clamped like the other handlers. Single inspection sends inspectionUrl and siteUrl. Batch and issue summaries allow at most ten URLs per call, a local contract rather than independently verified provider-wide limit. Sitemap writes take site_url,sitemap_url,account?. Most errors are {error: message}; batch errors remain per URL. HTTP 429/500/502/503/504 retry up to five attempts; 401 suggests reauthentication, 403 property access, 404 exact property syntax. stdio is default; optional SSE defaults 127.0.0.1:3001.

## Capability does not imply authorization

Credential profile and site_url are distinct inputs. A domain property retains its sc-domain: prefix. Analytics, current indexing inspection and sitemap submission are different evidence classes. Submission does not prove indexing or rankings.

GSC_ALLOW_DESTRUCTIVE is checked for nonempty presence, not parsed as the literal true: a value such as false still enables the code path. Treat this as a known implementation gap; actual operator approval is separate. Reauthenticate may delete a token and rebuild authentication; deletion occurs only for an explicit type="oauth" profile with an existing token_file. An omitted type still builds an OAuth client but does not trigger that unlink branch, so fresh consent is not guaranteed. set_default_account writes configuration. SSE has no separately implemented application authentication in this source. Read-only reports still expose private site data.

Route the current task through [the conductor selector](../../prompt.md#select-the-conductor). No native runtime, MCP connection, paid model, hook or third-party account is activated by this inventory. Verify availability in the actual invocation instead of inferring it from installed source.

## Supporting sources

- [README.md](../../README.md)
- [pyproject.toml](../../pyproject.toml)
- [gsc/server.py](../../gsc/server.py)

## Continue

Return to [INDEX.md](../../INDEX.md) and finish all routes relevant to the latest task before acting. After verification, update affected owning facts, REPORT and HANDOFFS.
