# Search Console multi-account MCP: operator experience

## Purpose

| Question | Answer |
| --- | --- |
| **Whom?** | SEO analyst investigating explicitly authorized Search Console properties. |
| **What?** | This is a conversational analytics interface. |
| **Where?** | gsc/server.py, tests/test_server.py. |
| **Why it exists?** | Search Console multi-account MCP needs this document to make the human-facing contract explicit even when the interface is a CLI or MCP tool. |
| **Why this approach?** | This is a conversational analytics interface. |
| **Why it matters?** | Credential profile and site_url are distinct inputs. |

## Operator experience

This is a conversational analytics interface. Report property, profile, date range, dimensions and dataState before metrics. Overview converts CTR to percent and rounds position; raw analytics and compare_periods retain provider CTR scale. Do not mix those representations in one chart without conversion. check_indexing_issues derives has_issues from verdict != PASS and orders issue rows first; an UNKNOWN verdict is not a diagnosed cause.

## State and error presentation

Identify the requested site and account -> list permitted properties -> choose search-performance or URL-inspection evidence -> request the smallest bounded window -> explain result freshness and metric units -> propose a sitemap change only if needed -> separately approve exact submission/deletion -> observe provider state. A 401 is an authentication recovery task, not permission to silently delete an existing token.

## Review standard

Review the actual interface changed: schema/error/citation output for tools, and visible rendered pages where this product creates a document or browser experience. Do not invent screen designs, visual tokens or customer flows that the product does not contain. User-facing success must name what succeeded and what remains unverified.

## Supporting sources

- [gsc/server.py](../../gsc/server.py)
- [tests/test_server.py](../../tests/test_server.py)

## Continue

Return to [INDEX.md](../../INDEX.md) and finish all routes relevant to the latest task before acting. After verification, update affected owning facts, REPORT and HANDOFFS.
