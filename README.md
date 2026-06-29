# mcp-search-console

Multi-account Google Search Console MCP server. Connect any number of GSC accounts to Claude, Cursor, Codex, or any MCP-compatible AI assistant — and query them by name in the same session.

```
# Ask your AI:
"Show me the top queries for my-site last month"
"Compare client-acme's performance between Q1 and Q2"
"Check indexing issues on client-beta's 5 product pages"
```

---

## Why this one?

Most GSC MCP servers support one account per server process. This one lets you configure multiple accounts (your own sites + client sites) and switch between them per tool call — no restart needed.

| Feature | This server | Others |
|---|---|---|
| Multiple accounts | Yes — named, switchable | No — one per process |
| OAuth + service account | Both, mixed per account | Usually one type |
| Auto token refresh | Yes | Sometimes |
| Rate limit retry | Yes — exponential backoff | No |
| Destructive op guard | Yes — env flag required | Sometimes |
| SSE transport (remote) | Yes | Varies |

---

## Quickstart (uvx — no clone needed)

**1. Create your accounts config:**

```bash
mkdir -p ~/.config/mcp-search-console
cp accounts.example.json ~/.config/mcp-search-console/accounts.json
# Edit it — add your accounts
```

**2. Add to your MCP client config:**

```json
{
  "mcpServers": {
    "search-console": {
      "command": "uvx",
      "args": ["mcp-search-console"],
      "env": {
        "GSC_ACCOUNTS_CONFIG": "/Users/you/.config/mcp-search-console/accounts.json"
      }
    }
  }
}
```

**3. Restart your AI client. Done.**

---

## Accounts config

Copy `accounts.example.json` and edit it:

```json
{
  "default": "my-site",
  "accounts": {
    "my-site": {
      "type": "oauth",
      "client_secrets_file": "~/.config/mcp-search-console/client_secrets.json",
      "token_file": "~/.config/mcp-search-console/my-site.token"
    },
    "client-acme": {
      "type": "service_account",
      "credentials_file": "~/.config/mcp-search-console/acme.json"
    }
  }
}
```

Set `GSC_ACCOUNTS_CONFIG` to its path, or put it at `~/.config/mcp-search-console/accounts.json` (default).

### OAuth setup

1. [Google Cloud Console](https://console.cloud.google.com/) → create project
2. Enable the [Search Console API](https://console.cloud.google.com/apis/library/searchconsole.googleapis.com)
3. Credentials → Create → OAuth client ID → Desktop app
4. Download as `client_secrets.json`
5. On first use, a browser window opens for you to authorise — token is saved automatically

### Service account setup

1. Google Cloud Console → Credentials → Create → Service Account
2. Keys tab → Add Key → JSON → download
3. In GSC, add the service account email as a user on each property

---

## Using multiple accounts

Every tool accepts an optional `account` parameter. Omit it to use your default.

```
"Show top queries for my-site"                    # uses default
"Show top queries for client-acme"                # uses named account
"Compare client-beta performance Jan vs Feb"      # named account
```

Or set the default mid-session:

```
"Switch to client-acme as my default account"
```

---

## Available tools

### Account management
| Tool | What it does |
|---|---|
| `list_accounts` | Show all configured accounts and which is default |
| `set_default_account` | Change the default account |
| `reauthenticate` | Re-run OAuth flow or reload credentials for an account |

### Properties
| Tool | What it does |
|---|---|
| `list_properties` | List all GSC properties |
| `get_site_details` | Verification + permission details for a property |

### Search analytics
| Tool | What it does |
|---|---|
| `get_search_analytics` | Queries, pages, clicks, impressions, CTR, position |
| `get_performance_overview` | Site-level totals for a period |
| `compare_periods` | Side-by-side comparison of two date ranges |
| `get_advanced_search_analytics` | Analytics with dimension filters (country, device, etc.) |
| `get_search_by_page` | Queries driving traffic to a specific page |

### URL inspection
| Tool | What it does |
|---|---|
| `inspect_url` | Indexing status, crawl date, mobile usability, rich results |
| `batch_inspect_urls` | Inspect up to 10 URLs at once |
| `check_indexing_issues` | Prioritised issue summary across multiple URLs |

### Sitemaps
| Tool | What it does |
|---|---|
| `list_sitemaps` | All submitted sitemaps with status |
| `get_sitemap` | Details for a specific sitemap |
| `submit_sitemap` | Submit a new sitemap *(requires `GSC_ALLOW_DESTRUCTIVE=true`)* |
| `delete_sitemap` | Remove a sitemap *(requires `GSC_ALLOW_DESTRUCTIVE=true`)* |

---

## Environment variables

| Variable | Default | Description |
|---|---|---|
| `GSC_ACCOUNTS_CONFIG` | `~/.config/mcp-search-console/accounts.json` | Path to your accounts config |
| `GSC_ALLOW_DESTRUCTIVE` | unset | Set to `true` to enable sitemap submit/delete |
| `MCP_TRANSPORT` | `stdio` | Set to `sse` for remote/Docker deployment |
| `MCP_HOST` | `127.0.0.1` | SSE bind host (use `0.0.0.0` for all interfaces) |
| `MCP_PORT` | `3001` | SSE bind port |

---

## Remote deployment (Docker / VPS)

```bash
docker build -t mcp-search-console .

docker run \
  -e MCP_TRANSPORT=sse \
  -e MCP_HOST=0.0.0.0 \
  -e MCP_PORT=3001 \
  -e GSC_ACCOUNTS_CONFIG=/config/accounts.json \
  -v /path/to/config:/config \
  -p 3001:3001 \
  mcp-search-console
```

Your MCP client connects to `http://your-server:3001/sse`.

---

## License

MIT
