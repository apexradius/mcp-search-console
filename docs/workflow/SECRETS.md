# Search Console multi-account MCP: configuration and private inputs

## Purpose

| Question | Answer |
| --- | --- |
| **Whom?** | SEO analyst investigating explicitly authorized Search Console properties. |
| **What?** | GSC_ACCOUNTS_CONFIG selects accounts JSON, default ~/.config/mcp-search-console/accounts.json. |
| **Where?** | gsc/server.py, gsc/accounts.py, gsc/auth/oauth.py. |
| **Why it exists?** | Search Console multi-account MCP needs this document to resolve configuration responsibility without exposing values. |
| **Why this approach?** | GSC_ACCOUNTS_CONFIG selects accounts JSON, default ~/.config/mcp-search-console/accounts.json. |
| **Why it matters?** | Private input access is not necessary to understand the product contract. |

## Metadata-only configuration map

GSC_ACCOUNTS_CONFIG selects accounts JSON, default ~/.config/mcp-search-console/accounts.json. OAuth uses client_secrets_file and token_file; service accounts use credentials_file. Both adapters request https://www.googleapis.com/auth/webmasters. The present docs do not inspect real files, accounts or access grants.

## Access discipline

This document carries configuration names, purpose and responsibility only. Never paste values, tokens, private prompts, unrestricted provider output or account exports. For a real credential failure, identify the approved storage/rotation path without printing its contents; verify the authorized replacement in the actual runtime and retain a redacted receipt. Secret presence, file readability and connector access are not approval to perform the task.

## Supporting sources

- [gsc/server.py](../../gsc/server.py)
- [gsc/accounts.py](../../gsc/accounts.py)
- [gsc/auth/oauth.py](../../gsc/auth/oauth.py)
- [gsc/auth/service_account.py](../../gsc/auth/service_account.py)
- [tests/test_server.py](../../tests/test_server.py)

## Continue

Return to [INDEX.md](../../INDEX.md) and finish all routes relevant to the latest task before acting. After verification, update affected owning facts, REPORT and HANDOFFS.
