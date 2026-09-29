# Search Console multi-account MCP: orientation

## Purpose

| Question | Answer |
| --- | --- |
| **Whom?** | SEO analyst investigating explicitly authorized Search Console properties. |
| **What?** | Provide property discovery, search analytics, URL inspection and controlled sitemap operations across multiple Google Search Console accounts through one local MCP server. |
| **Where?** | README.md, pyproject.toml, gsc/server.py. |
| **Why it exists?** | Search Console multi-account MCP needs this document to recover the purpose and correct owning implementation before acting. |
| **Why this approach?** | FastMCP server -> lazy AccountManager -> cached Google webmasters v3 client -> endpoint request.execute through with_retry -> tool result. |
| **Why it matters?** | Credential profile and site_url are distinct inputs. |

## Product and scope

Provide property discovery, search analytics, URL inspection and controlled sitemap operations across multiple Google Search Console accounts through one local MCP server.

Credential profile and site_url are distinct inputs. A domain property retains its sc-domain: prefix. Analytics, current indexing inspection and sitemap submission are different evidence classes. Submission does not prove indexing or rankings.

## Find the owning behavior

FastMCP server -> lazy AccountManager -> cached Google webmasters v3 client -> endpoint request.execute through with_retry -> tool result. AccountManager validates profile names and refreshes expired clients. OAuth/service-account adapters share the webmasters scope. Source separates profile lifecycle, provider retry and tool mapping; no original alternatives analysis was found, so reuse is an implementation-based choice, not a claimed historical ADR.

Use [API](API.md) for the exact interface, [DATABASE](DATABASE.md) for state, [TESTING](TESTING.md) for proof and [HANDOFFS](HANDOFFS.md) for current uncertainty. [The root README](../../README.md) remains the original manual; known stale statements are preserved and explained here, not silently adopted.

## Current baseline

Current main candidate 7b77d88 is the 2026-09-16 CI-gate merge. July 5 added hermetic tests; July 19 removed an empty tools directory. Existing history shows a compact connector, not an approved current SEO campaign or a pending sitemap deployment.

## Supporting sources

- [README.md](../../README.md)
- [pyproject.toml](../../pyproject.toml)
- [gsc/server.py](../../gsc/server.py)

## Continue

Return to [INDEX.md](../../INDEX.md) and finish all routes relevant to the latest task before acting. After verification, update affected owning facts, REPORT and HANDOFFS.
