# Start Here

This server exposes Google Search Console search analytics, URL inspection, sitemap, and property
tools through MCP. It is designed for multi-account SEO work across owned and client properties.

## First Run

```bash
uvx mcp-search-console-multi
```

Then configure an MCP client with `GSC_ACCOUNTS_CONFIG` pointing to an account map based on
`accounts.example.json`.

## Account Setup

1. Choose OAuth for interactive user-owned properties or service accounts for managed client
   access.
2. Add one named account per property group.
3. Set the `default` account in `accounts.json`.
4. Start the MCP client and call `list_accounts`.
5. Confirm property access with `list_properties`.

## Development Loop

```bash
uv sync
uv run ruff check .
uv run python -m gsc.server
```

Tool registration lives in `gsc/server.py`; account resolution lives in `gsc/accounts.py`; auth
strategies live under `gsc/auth/`.
