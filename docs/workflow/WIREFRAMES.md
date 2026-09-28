# Search Console multi-account MCP: task journeys

## Purpose

| Question | Answer |
| --- | --- |
| **Whom?** | SEO analyst investigating explicitly authorized Search Console properties. |
| **What?** | Identify the requested site and account -> list permitted properties -> choose search-performance or URL-inspection evidence -> request the smallest bounded window -> explain result freshness and metric units -> propose a sitemap change only if needed -> separately approve exact submission/deletion -> observe provider state. |
| **Where?** | README.md, gsc/server.py, tests/test_server.py. |
| **Why it exists?** | Search Console multi-account MCP needs this document to show the order of observations and actions required for a real task. |
| **Why this approach?** | Identify the requested site and account -> list permitted properties -> choose search-performance or URL-inspection evidence -> request the smallest bounded window -> explain result freshness and metric units -> propose a sitemap change only if needed -> separately approve exact submission/deletion -> observe provider state. |
| **Why it matters?** | Credential profile and site_url are distinct inputs. |

## Concrete interaction flow

Identify the requested site and account -> list permitted properties -> choose search-performance or URL-inspection evidence -> request the smallest bounded window -> explain result freshness and metric units -> propose a sitemap change only if needed -> separately approve exact submission/deletion -> observe provider state. A 401 is an authentication recovery task, not permission to silently delete an existing token.

## Entry, result and failure states

This is a conversational analytics interface. Report property, profile, date range, dimensions and dataState before metrics. Overview converts CTR to percent and rounds position; raw analytics and compare_periods retain provider CTR scale. Do not mix those representations in one chart without conversion. check_indexing_issues derives has_issues from verdict != PASS and orders issue rows first; an UNKNOWN verdict is not a diagnosed cause.

GSC_ALLOW_DESTRUCTIVE is checked for nonempty presence, not parsed as the literal true: a value such as false still enables the code path. Treat this as a known implementation gap; actual operator approval is separate. Reauthenticate may delete a token and rebuild authentication; deletion occurs only for an explicit type="oauth" profile with an existing token_file. An omitted type still builds an OAuth client but does not trigger that unlink branch, so fresh consent is not guaranteed. set_default_account writes configuration. SSE has no separately implemented application authentication in this source. Read-only reports still expose private site data.

This is a sequence specification for the current interface. It does not introduce an unimplemented graphical application. Use the source tool/CLI contract for exact input fields.

## Supporting sources

- [README.md](../../README.md)
- [gsc/server.py](../../gsc/server.py)
- [tests/test_server.py](../../tests/test_server.py)

## Continue

Return to [INDEX.md](../../INDEX.md) and finish all routes relevant to the latest task before acting. After verification, update affected owning facts, REPORT and HANDOFFS.
