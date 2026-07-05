# Start Here — mcp-search-console

## What this repo ships

- One Python package: `mcp-search-console-multi`
- One MCP server entry point: `gsc.server:main`
- One account-manager layer that lets a single MCP server address many Search Console accounts

## First run

1. Install the package:

```bash
python -m pip install mcp-search-console-multi
```

2. Create the accounts config:

```bash
mkdir -p ~/.config/mcp-search-console
cp accounts.example.json ~/.config/mcp-search-console/accounts.json
```

3. Export the config path and start your MCP client:

```bash
export GSC_ACCOUNTS_CONFIG="$HOME/.config/mcp-search-console/accounts.json"
```

## Required environment

| Variable | Required | Notes |
|---|---|---|
| `GSC_ACCOUNTS_CONFIG` | yes | Path to the multi-account config file |
| `GSC_ALLOW_DESTRUCTIVE` | optional | Required for sitemap submit/delete |
| `MCP_TRANSPORT` | optional | `stdio` by default; `sse` for remote hosting |
| `MCP_HOST` / `MCP_PORT` | optional | SSE bind address when remote transport is enabled |

## Validation commands

```bash
python -m compileall gsc
python -m build
```

## Common failures

| Symptom | Likely cause | Fix |
|---|---|---|
| Account not found | Config alias mismatch | Check the `default` key and account names in `accounts.json` |
| OAuth prompt never completes | Local OAuth credentials missing | Recreate the desktop OAuth client and token files |
| Search Console auth error | Wrong property access or bad credentials | Re-verify property access and credential file paths |
| Destructive sitemap tool refuses to run | Safety flag missing | Set `GSC_ALLOW_DESTRUCTIVE=true` intentionally |
