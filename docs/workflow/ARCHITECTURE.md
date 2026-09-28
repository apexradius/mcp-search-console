# Search Console multi-account MCP: components and decisions

## Purpose

| Question | Answer |
| --- | --- |
| **Whom?** | SEO analyst investigating explicitly authorized Search Console properties. |
| **What?** | FastMCP server -> lazy AccountManager -> cached Google webmasters v3 client -> endpoint request.execute through with_retry -> tool result. |
| **Where?** | gsc/server.py, tests/test_server.py. |
| **Why it exists?** | Search Console multi-account MCP needs this document to locate the component that owns the requested behavior. |
| **Why this approach?** | FastMCP server -> lazy AccountManager -> cached Google webmasters v3 client -> endpoint request.execute through with_retry -> tool result. |
| **Why it matters?** | Credential profile and site_url are distinct inputs. |

## Components, flow and rationale

FastMCP server -> lazy AccountManager -> cached Google webmasters v3 client -> endpoint request.execute through with_retry -> tool result. AccountManager validates profile names and refreshes expired clients. OAuth/service-account adapters share the webmasters scope. Source separates profile lifecycle, provider retry and tool mapping; no original alternatives analysis was found, so reuse is an implementation-based choice, not a claimed historical ADR.

## State boundary

There is no local business database. Accounts JSON holds default plus profile configurations and file references; set_default_account persists that default. Client cache membership is reported as authenticated, but it does not prove a current successful provider request. OAuth token JSON persists locally and may refresh on access. Reauthenticate always invalidates the cached client. It deletes an existing token file only when the profile explicitly sets type="oauth" and token_file; _build_client separately defaults an omitted type to OAuth. An implicit-OAuth profile can therefore reuse its saved token instead of forcing consent. It then rebuilds the client, which may refresh credentials or open the OAuth flow depending on actual credential state. Analytics and inspection results are transient; source snippets and property identifiers should not enter public validation receipts.

## Evolution and current mismatch

Current main candidate 7b77d88 is the 2026-09-16 CI-gate merge. July 5 added hermetic tests; July 19 removed an empty tools directory. Existing history shows a compact connector, not an approved current SEO campaign or a pending sitemap deployment.

1. Strict destructive-flag parsing is absent. 2. compare_periods does not clamp row_limit or prove complete pagination; results are bounded comparisons. 3. Current tests cover guards and registration rather than provider response semantics. 4. Cached authenticated status is weaker than live access. Proposed first work is contract/guard regression coverage for the exact requested operation; no current operator-ranked backlog was recovered.

## Supporting sources

- [gsc/server.py](../../gsc/server.py)
- [tests/test_server.py](../../tests/test_server.py)

## Continue

Return to [INDEX.md](../../INDEX.md) and finish all routes relevant to the latest task before acting. After verification, update affected owning facts, REPORT and HANDOFFS.
