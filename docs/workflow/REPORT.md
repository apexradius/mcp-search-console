# Search Console multi-account MCP: evidence and unresolved claims

## Purpose

| Question | Answer |
| --- | --- |
| **Whom?** | SEO analyst investigating explicitly authorized Search Console properties. |
| **What?** | Strict destructive-flag parsing is absent. |
| **Where?** | README.md, pyproject.toml, gsc/server.py. |
| **Why it exists?** | Search Console multi-account MCP needs this document to show what is observed, what remains unknown and what decision follows. |
| **Why this approach?** | Strict destructive-flag parsing is absent. |
| **Why it matters?** | These limits keep the next task honest and bounded. |

## Reconstruction finding

Source reconstruction: 2026-09-26; candidate `7b77d888e71197486a67815d3462f66c80c2036f` on `main`; source version `0.1.3`. This is a dated source observation, not a live-service or installed-version claim.

The earlier workflow-adoption completion has been superseded by the user’s request for substantive product reconstruction. The enduring product outcome is: Provide property discovery, search analytics, URL inspection and controlled sitemap operations across multiple Google Search Console accounts through one local MCP server.

## Established from sources

FastMCP server -> lazy AccountManager -> cached Google webmasters v3 client -> endpoint request.execute through with_retry -> tool result. AccountManager validates profile names and refreshes expired clients. OAuth/service-account adapters share the webmasters scope. Source separates profile lifecycle, provider retry and tool mapping; no original alternatives analysis was found, so reuse is an implementation-based choice, not a claimed historical ADR.

Current main candidate 7b77d88 is the 2026-09-16 CI-gate merge. July 5 added hermetic tests; July 19 removed an empty tools directory. Existing history shows a compact connector, not an approved current SEO campaign or a pending sitemap deployment.

## Unresolved product claims

1. Strict destructive-flag parsing is absent. 2. compare_periods does not clamp row_limit or prove complete pagination; results are bounded comparisons. 3. Current tests cover guards and registration rather than provider response semantics. 4. Cached authenticated status is weaker than live access. Proposed first work is contract/guard regression coverage for the exact requested operation; no current operator-ranked backlog was recovered.

## Evidence limits and value

This reconstruction makes the next task’s interfaces, boundaries and prior intent recoverable. It does not establish new customer value, provider success or a deployed fix. No current product build, account request, browser launch, private corpus read, publish or release was performed. Structural document validation and source-grounded scenario read-through are recorded separately from product acceptance. Live-product validation is required for every PR, and a docs-only exception is not accepted. Unavailable surface/access: read-only Google Search Console account and property access via the authorized API client; not provided in this delivery session. Live GSC validation was not performed and acceptance remains blocked pending that access. No simulated GSC data stands in for it. [TESTING](TESTING.md) identifies the additional proof a future implementation needs.

## Supporting sources

- [README.md](../../README.md)
- [pyproject.toml](../../pyproject.toml)
- [gsc/server.py](../../gsc/server.py)

## Continue

Return to [INDEX.md](../../INDEX.md) and finish all routes relevant to the latest task before acting. After verification, update affected owning facts, REPORT and HANDOFFS.
