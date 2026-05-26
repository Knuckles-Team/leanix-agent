# Dynamic Introspection, Filtering, & Authentication

This document details the advanced capabilities of the **LeanIX Agent**, focusing on dynamic meta-model introspection, real-time toolset filtering, and enterprise authentication methods.

---

## 🔐 Authentication Modes

The LeanIX Agent supports three tier-based enterprise authentication methods, prioritized automatically based on the environment configuration:

### 1. Interactive OAuth 2.0 Web Browser Login (with PKCE)
Perfect for local developer execution, desktop environments, and CLI usage. This flow mirrors the official SAP LeanIX MCP server's browser authentication.

*   **Activation**: Enabled by setting `LEANIX_AUTH_METHOD=browser` or `LEANIX_BROWSER_LOGIN=true`.
*   **Mechanism**:
    *   Initiates a lightweight loopback redirect server (default port `56122`).
    *   Launches your system's default browser pointing to the LeanIX authorize endpoint (`/services/mtm/v1/oauth2/authorize`).
    *   Uses **Proof Key for Code Exchange (PKCE)** to securely exchange the authorization code for access and refresh tokens.
    *   Persists the token bundle in local secure storage.
*   **Auto-Refresh**: Automatically checks expiration before any request and triggers a silent OAuth refresh flow using the stored refresh token with the `offline_access` scope—without prompting you again in the browser.
*   **Configuration**:
    *   `LEANIX_WORKSPACE`: Target workspace URL (e.g., `https://your-workspace.leanix.net`).
    *   `LEANIX_OAUTH_CLIENT_ID`: OAuth Client ID (defaults to `leanix-mcp`).
    *   `LEANIX_OAUTH_REDIRECT_PORT`: Local callback server port (defaults to `56122`).
    *   `LEANIX_OAUTH_SCOPE`: Requested scopes (defaults to `openid offline_access`).

### 2. OIDC Delegation (RFC 8693 Token Exchange)
Used in orchestrations where a parent identity provider issues tokens. The agent exchanges the user token for a downstream LeanIX access token automatically using `agent-utilities[auth]`.

*   **Activation**: Automatically active if `ENABLE_DELEGATION=true` is set.

### 3. API Token / Technical User Credentials
Standard backend authentication method using static credentials.

*   **Activation**: Set standard tokens or credentials via environment variables.
*   **Configuration**:
    *   `LEANIX_API_TOKEN` / `LEANIX_TOKEN`: Static API token.
    *   `LEANIX_TECHNICAL_USER` and `LEANIX_TECHNICAL_USER_PASSWORD`: Technical user credentials.

---

## 🔍 Dynamic Meta-Model Introspection

Custom fields, tags, and relations are a core part of enterprise LeanIX workspaces. Instead of utilizing rigid, hardcoded models, the LeanIX Agent supports **Dynamic Meta-Model Introspection**.

### How it Works
The agent exposes a first-class semantic tool called `leanix_discover_meta_model`:
*   **GraphQL Core**: Under the hood, this tool executes real-time schema and meta-model discovery queries against the Pathfinder GraphQL API.
*   **Real-time Capabilities**: It fetches all active FactSheet types, user-defined custom fields, custom field values, relationships, and tags.
*   **Zero Hallucination**: AI agents call this tool to introspect the schema of the workspace they are currently connected to *before* executing mutations or complex queries, completely eliminating field name hallucinations.

---

## 🛡️ Universal Dynamic Toolset Filtering

With over 30+ services and 500+ generated endpoints, exposing all available tools directly would overwhelm any LLM's context window and increase invocation costs.

The agent resolves this using **Universal Dynamic Toolset Filtering** powered by `DynamicVisibilityTransform` in the `agent-utilities` core.

### Architectural View
```
+-------------------------------------------------------------+
|                        MCP Server                           |
|  Exposes a curated subset of high-level semantic tools      |
+------------------------------+------------------------------+
                               |
                               v
               +-------------------------------+
               |   DynamicVisibilityTransform  |  <-- Configured by:
               |   Filters advanced tools based|      - Environment flags
               |   on active environments      |      - OAuth scopes
               +---------------+---------------+
                               |
                               v
+------------------------------+------------------------------+
|                  Curated Semantic Toolset                   |
|  - leanix_search_fact_sheets                                |
|  - leanix_create_fact_sheet                                 |
|  - leanix_update_fact_sheet                                 |
|  - leanix_get_fact_sheet_details                            |
|  - leanix_discover_meta_model (Dynamic Introspection)       |
+-------------------------------------------------------------+
```

### Benefits
*   **Minimal Context Bloat**: Keeps the number of active tools lean and context-optimized.
*   **Targeted Execution**: Advanced generated tools (like individual low-level REST API endpoints) are only exposed to the agent if explicitly configured or conditionally needed.
*   **Dynamic Enforcement**: Restricts tools dynamically if the active authentication token doesn't have the appropriate scope/privileges.
