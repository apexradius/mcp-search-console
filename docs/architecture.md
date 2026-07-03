# Architecture

`mcp-search-console` is a Python MCP server around Google Search Console. It resolves a named
account, authenticates through OAuth or service-account credentials, calls the Search Console API,
and returns structured MCP results.

## Components

```mermaid
flowchart TD
    Main[gsc/server.py] --> ToolRegistry[MCP tool registry]
    ToolRegistry --> Accounts[gsc/accounts.py]
    ToolRegistry --> Tools[gsc/tools]
    ToolRegistry --> Retry[gsc/retry.py]

    Accounts --> OAuth[gsc/auth/oauth.py]
    Accounts --> Service[gsc/auth/service_account.py]
    Tools --> Analytics[Search analytics]
    Tools --> Inspection[URL inspection]
    Tools --> Sitemaps[Sitemap tools]
    Analytics --> API[Google Search Console API]
    Inspection --> API
    Sitemaps --> API
```

## Request Sequence

```mermaid
sequenceDiagram
    actor User
    participant Client as MCP client
    participant Server as gsc/server.py
    participant Accounts as gsc/accounts.py
    participant Google as Search Console API

    User->>Client: Ask for SEO data
    Client->>Server: Call GSC tool
    Server->>Accounts: Resolve account
    Accounts-->>Server: Credentials and property context
    Server->>Google: Run analytics or inspection request
    Google-->>Server: API response
    Server-->>Client: Structured MCP result
    Client-->>User: SEO answer
```

## Data Boundaries

| Data | Source | Storage |
|---|---|---|
| Account map | `accounts.json` based on `accounts.example.json` | Local config path. |
| OAuth client secrets | Google Cloud OAuth app | Local file path only. |
| OAuth token files | Generated during OAuth flow | Local file path only. |
| Service-account JSON | Google Cloud service account | Local or mounted config. |
| GSC data | Search Console API | Returned through MCP; not persisted here. |

## Extension Points

| Change | File |
|---|---|
| Add a new MCP tool | `gsc/server.py` or `gsc/tools/` |
| Add account behavior | `gsc/accounts.py` |
| Change OAuth flow | `gsc/auth/oauth.py` |
| Change service-account flow | `gsc/auth/service_account.py` |
