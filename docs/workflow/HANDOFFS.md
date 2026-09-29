# Search Console multi-account MCP: product continuity

## Purpose

| Question | Answer |
| --- | --- |
| **Whom?** | SEO analyst investigating explicitly authorized Search Console properties. |
| **What?** | Strict destructive-flag parsing is absent. |
| **Where?** | README.md. |
| **Why it exists?** | Search Console multi-account MCP needs this document to separate finished historical work from an actual task that can resume. |
| **Why this approach?** | Current main candidate 7b77d88 is the 2026-09-16 CI-gate merge. |
| **Why it matters?** | The next agent must not repeat a dated delivery or convert a suggested fix into an approved operation. |

## Durable product state

Provide property discovery, search analytics, URL inspection and controlled sitemap operations across multiple Google Search Console accounts through one local MCP server.

Current main candidate 7b77d88 is the 2026-09-16 CI-gate merge. July 5 added hermetic tests; July 19 removed an empty tools directory. Existing history shows a compact connector, not an approved current SEO campaign or a pending sitemap deployment.

## Open work and blockers

1. Strict destructive-flag parsing is absent. 2. compare_periods does not clamp row_limit or prove complete pagination; results are bounded comparisons. 3. Current tests cover guards and registration rather than provider response semantics. 4. Cached authenticated status is weaker than live access. Proposed first work is contract/guard regression coverage for the exact requested operation; no current operator-ranked backlog was recovered.

The latest user request selects the actual task. These proposed maintenance priorities are not an approved feature roadmap, provider action or automatic queue. If the user only says “read and begin,” reconcile these findings against the current candidate and report the smallest useful next action; do not resume completed documentation adoption or replay an old submission.

5. Reauthentication has inconsistent default-type handling: building a profile with omitted type uses OAuth, but invalidation only unlinks an explicit OAuth profile token. Inspect the selected profile metadata within authorized recovery scope and test explicit/implicit OAuth plus service-account branches before promising a forced new login. Do not inspect or delete token values just to validate documentation.
6. Live-product acceptance remains blocked. Unavailable surface/access: read-only Google Search Console account and property access via the authorized API client; not provided in this delivery session. Live GSC validation was not performed and acceptance remains blocked pending that access.

## Next handoff contract

Record the concrete requested outcome, exact repository/candidate, selected conductor, touched source and task state, completed behavior with evidence level, unresolved blocker, next safe action, approvals and effects already performed. Include operation identity/duplicate-prevention state for any external effect. Preserve requirement/decision changes and pending knowledge events. A source/test inventory is not a release acceptance receipt.

## Supporting sources

- [README.md](../../README.md)

## Continue

Return to [INDEX.md](../../INDEX.md) and finish all routes relevant to the latest task before acting. After verification, update affected owning facts, REPORT and HANDOFFS.
