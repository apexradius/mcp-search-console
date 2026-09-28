# Search Console multi-account MCP: implementation conventions

## Purpose

| Question | Answer |
| --- | --- |
| **Whom?** | SEO analyst investigating explicitly authorized Search Console properties. |
| **What?** | Python 3.11+, snake_case FastMCP handlers, Ruff py311/100 columns. |
| **Where?** | pyproject.toml. |
| **Why it exists?** | Search Console multi-account MCP needs this document to preserve the implementation’s existing conventions at the change boundary. |
| **Why this approach?** | Python 3.11+, snake_case FastMCP handlers, Ruff py311/100 columns. |
| **Why it matters?** | Small compatible changes remain easier to review and recover. |

## Existing conventions

Python 3.11+, snake_case FastMCP handlers, Ruff py311/100 columns. Keep account/auth/retry modules separate. Preserve per-URL error isolation in batch tools. Use explicit response mappings rather than claiming annotations guarantee error types; tests should cover raw versus percentage CTR and bounded comparison behavior.

## Change boundary

FastMCP server -> lazy AccountManager -> cached Google webmasters v3 client -> endpoint request.execute through with_retry -> tool result. AccountManager validates profile names and refreshes expired clients. OAuth/service-account adapters share the webmasters scope. Source separates profile lifecycle, provider retry and tool mapping; no original alternatives analysis was found, so reuse is an implementation-based choice, not a claimed historical ADR.

Prefer the smallest change in the component that already owns the behavior. Preserve generated artifacts and original requirements. Test a changed contract at its actual boundary; do not add scaffolding, services or broad refactors only to satisfy a documentation layout.

## Supporting sources

- [pyproject.toml](../../pyproject.toml)

## Continue

Return to [INDEX.md](../../INDEX.md) and finish all routes relevant to the latest task before acting. After verification, update affected owning facts, REPORT and HANDOFFS.
