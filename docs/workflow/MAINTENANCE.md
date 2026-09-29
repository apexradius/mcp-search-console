# Search Console multi-account MCP: operation and recovery

## Purpose

| Question | Answer |
| --- | --- |
| **Whom?** | SEO analyst investigating explicitly authorized Search Console properties. |
| **What?** | Start through gsc.server:main only for an authorized runtime task. |
| **Where?** | README.md. |
| **Why it exists?** | Search Console multi-account MCP needs this document to recover safely from the actual failure modes rather than repeat old operations. |
| **Why this approach?** | Start through gsc.server:main only for an authorized runtime task. |
| **Why it matters?** | Credential profile and site_url are distinct inputs. |

## Runtime and recovery

Start through gsc.server:main only for an authorized runtime task. Validate exact property syntax before diagnosing missing access. Reauthentication may open a browser and replace a private token. Do not replay old sitemap submissions after a restart; inspect the exact provider target and durable state first. Record date range/dimensions for analytics and observation time for inspections without storing sensitive output.

## Prioritized uncertainty

1. Strict destructive-flag parsing is absent. 2. compare_periods does not clamp row_limit or prove complete pagination; results are bounded comparisons. 3. Current tests cover guards and registration rather than provider response semantics. 4. Cached authenticated status is weaker than live access. Proposed first work is contract/guard regression coverage for the exact requested operation; no current operator-ranked backlog was recovered.

## Closeout

Verify the requested result at the correct layer, reconcile the owning manual/interface and update [HANDOFFS](HANDOFFS.md). Record a [knowledge event](REFERENCES.md) for material source/decision/freshness changes. Do not run package publishing, provider writes, private index sync or browser automation just to refresh a document.

## Supporting sources

- [README.md](../../README.md)

## Continue

Return to [INDEX.md](../../INDEX.md) and finish all routes relevant to the latest task before acting. After verification, update affected owning facts, REPORT and HANDOFFS.
