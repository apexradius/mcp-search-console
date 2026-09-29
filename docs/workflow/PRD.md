# Search Console multi-account MCP: requirements and value

## Purpose

| Question | Answer |
| --- | --- |
| **Whom?** | SEO analyst investigating explicitly authorized Search Console properties. |
| **What?** | Resolve named OAuth/service-account profiles without restarting the server. |
| **Where?** | README.md. |
| **Why it exists?** | Search Console multi-account MCP needs this document to keep implementation choices tied to the promised outcome. |
| **Why this approach?** | Resolve named OAuth/service-account profiles without restarting the server. |
| **Why it matters?** | Credential profile and site_url are distinct inputs. |

## Vision and user value

Provide property discovery, search analytics, URL inspection and controlled sitemap operations across multiple Google Search Console accounts through one local MCP server.

## Requirements and acceptance meaning

Resolve named OAuth/service-account profiles without restarting the server. Expose the 17 current tools with explicit property scope and bounded URL inspection. Return understandable authorization/rate-limit errors. Sitemap submission and deletion must be treated as external writes even though they sit beside read tools. Never turn analytics absence into a guaranteed absence of traffic or a live-page diagnosis.

## Non-negotiable boundaries

Credential profile and site_url are distinct inputs. A domain property retains its sc-domain: prefix. Analytics, current indexing inspection and sitemap submission are different evidence classes. Submission does not prove indexing or rankings.

## Why this implementation

FastMCP server -> lazy AccountManager -> cached Google webmasters v3 client -> endpoint request.execute through with_retry -> tool result. AccountManager validates profile names and refreshes expired clients. OAuth/service-account adapters share the webmasters scope. Source separates profile lifecycle, provider retry and tool mapping; no original alternatives analysis was found, so reuse is an implementation-based choice, not a claimed historical ADR.

## Current requirement debt

1. Strict destructive-flag parsing is absent. 2. compare_periods does not clamp row_limit or prove complete pagination; results are bounded comparisons. 3. Current tests cover guards and registration rather than provider response semantics. 4. Cached authenticated status is weaker than live access. Proposed first work is contract/guard regression coverage for the exact requested operation; no current operator-ranked backlog was recovered.

Classify a future statement as original requirement, later amendment, observed implementation, inferred rationale or proposed change. Preserve the distinction: source behavior does not silently repeal an original promise, and a plausible rationale is not a recorded decision.

## Supporting sources

- [README.md](../../README.md)

## Continue

Return to [INDEX.md](../../INDEX.md) and finish all routes relevant to the latest task before acting. After verification, update affected owning facts, REPORT and HANDOFFS.
