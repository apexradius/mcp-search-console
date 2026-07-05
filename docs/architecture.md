# Architecture — mcp-search-console

## Component map

| Component | File | Role |
|---|---|---|
| MCP server | [`../gsc/server.py`](../gsc/server.py) | Declares the tool surface and normalizes responses |
| Account manager | [`../gsc/accounts.py`](../gsc/accounts.py) | Resolves named accounts and builds authenticated clients |
| Auth backends | [`../gsc/auth/`](../gsc/auth/) | OAuth desktop flow and service-account loading |
| Retry wrapper | [`../gsc/retry.py`](../gsc/retry.py) | Retries transient Search Console API failures |
| Package metadata | [`../pyproject.toml`](../pyproject.toml) | Version, dependency set, script entry point |

## Runtime lifecycle

1. The MCP client launches `mcp-search-console-multi`.
2. `FastMCP` registers the account, property, analytics, inspection, and sitemap tools.
3. The selected tool resolves the named or default account through `AccountManager`.
4. The authenticated Search Console client calls the API through `with_retry()`.
5. Results return as plain dictionaries and lists for the MCP client.
