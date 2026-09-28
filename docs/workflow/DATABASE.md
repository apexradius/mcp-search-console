# Search Console multi-account MCP: state and persistence

## Purpose

| Question | Answer |
| --- | --- |
| **Whom?** | SEO analyst investigating explicitly authorized Search Console properties. |
| **What?** | There is no local business database. |
| **Where?** | gsc/accounts.py. |
| **Why it exists?** | Search Console multi-account MCP needs this document to identify what persists, what is transient and what requires recovery. |
| **Why this approach?** | There is no local business database. |
| **Why it matters?** | Credential profile and site_url are distinct inputs. |

## Actual state model

There is no local business database. Accounts JSON holds default plus profile configurations and file references; set_default_account persists that default. Client cache membership is reported as authenticated, but it does not prove a current successful provider request. OAuth token JSON persists locally and may refresh on access. Reauthenticate always invalidates the cached client. It deletes an existing token file only when the profile explicitly sets type="oauth" and token_file; _build_client separately defaults an omitted type to OAuth. An implicit-OAuth profile can therefore reuse its saved token instead of forcing consent. It then rebuilds the client, which may refresh credentials or open the OAuth flow depending on actual credential state. Analytics and inspection results are transient; source snippets and property identifiers should not enter public validation receipts.

## State transition and recovery

Start through gsc.server:main only for an authorized runtime task. Validate exact property syntax before diagnosing missing access. Reauthentication may open a browser and replace a private token. Do not replay old sitemap submissions after a restart; inspect the exact provider target and durable state first. Record date range/dimensions for analytics and observation time for inspections without storing sensitive output.

## Private-input boundary

GSC_ACCOUNTS_CONFIG selects accounts JSON, default ~/.config/mcp-search-console/accounts.json. OAuth uses client_secrets_file and token_file; service accounts use credentials_file. Both adapters request https://www.googleapis.com/auth/webmasters. The present docs do not inspect real files, accounts or access grants.

## Supporting sources

- [gsc/accounts.py](../../gsc/accounts.py)

## Continue

Return to [INDEX.md](../../INDEX.md) and finish all routes relevant to the latest task before acting. After verification, update affected owning facts, REPORT and HANDOFFS.
