# Search Console multi-account MCP - begin here

## Purpose

| Question | Answer |
| --- | --- |
| **Whom?** | SEO analyst investigating explicitly authorized Search Console properties. |
| **What?** | Provide property discovery, search analytics, URL inspection and controlled sitemap operations across multiple Google Search Console accounts through one local MCP server. |
| **Where?** | README.md, pyproject.toml, gsc/server.py. |
| **Why it exists?** | Search Console multi-account MCP needs this document to start the next task with the product’s actual purpose. |
| **Why this approach?** | Credential profile and site_url are distinct inputs. |
| **Why it matters?** | Credential profile and site_url are distinct inputs. |

## Product goal

Provide property discovery, search analytics, URL inspection and controlled sitemap operations across multiple Google Search Console accounts through one local MCP server.

## Invariants

Credential profile and site_url are distinct inputs. A domain property retains its sc-domain: prefix. Analytics, current indexing inspection and sitemap submission are different evidence classes. Submission does not prove indexing or rankings.

## Recover the current task

Source reconstruction: 2026-09-26; candidate `7b77d888e71197486a67815d3462f66c80c2036f` on `main`; source version `0.1.3`. This is a dated source observation, not a live-service or installed-version claim.

Current main candidate 7b77d88 is the 2026-09-16 CI-gate merge. July 5 added hermetic tests; July 19 removed an empty tools directory. Existing history shows a compact connector, not an approved current SEO campaign or a pending sitemap deployment.

Use the latest user request as the task selector. This dossier is standing product context, not an instruction to repeat a completed documentation rollout. Recover applicable repository instructions, exact branch/candidate and dirty state, then bind the requested outcome and acceptance. If the only instruction is “read and begin,” finish this chain and perform a bounded read-only reconciliation of the current handoff and source; report the smallest next action, without inventing a product task or replaying historical external actions.

## Read chain

**Next: [INDEX.md](INDEX.md).** Follow every Continue link through all 17 role documents before returning here. Resolve relevant source contradictions before implementation; existing source documents remain canonical. Read deeper source when the selected task touches it.

## Select the conductor

- Bounded document maintenance uses doc-writer directly. Use init-studio’s relevant retrospective stages only when reconstructing requirements or reopening a real specification decision; finish with explicit project handoff and unresolved choices. Do not initialize another repository.
- A reproducible implementation defect routes to debug-studio with the actual failing contract. API/client/schema work routes to api-studio where applicable.
- Design-studio is for a real operator/document/interface design task. Web-studio requires an actual web-product task; CLI, native browser control, framework or library maintenance does not automatically become web development. Grow-studio applies only to an explicit growth task with evidence-backed claims.
- Load only the selected conductor and its relevant children. Reuse settled decisions, exact source constraints and current user authorization. Choose native platform/tool capabilities when no conductor matches; do not force a studio for bookkeeping.

## First unresolved work

1. Strict destructive-flag parsing is absent. 2. compare_periods does not clamp row_limit or prove complete pagination; results are bounded comparisons. 3. Current tests cover guards and registration rather than provider response semantics. 4. Cached authenticated status is weaker than live access. Proposed first work is contract/guard regression coverage for the exact requested operation; no current operator-ranked backlog was recovered.

Before implementation, state the requested outcome, smallest useful change, evidence required and stop condition. Verify the actual result, update canonical sources and HANDOFFS, and leave knowledge events honest about freshness.
