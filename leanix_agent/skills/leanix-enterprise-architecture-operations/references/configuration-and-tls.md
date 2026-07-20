# Configuration and TLS

Treat AgentConfig as the runtime authority. Keep connection values and credentials
outside the package, and store sensitive values behind secret references.

## Connection and authentication

Configure the following keys at runtime:

| Key | Purpose |
|---|---|
| `LEANIX_WORKSPACE` | LeanIX workspace base URL |
| `LEANIX_AUTH_METHOD` | Select technical-user, token, browser, or delegated authentication |
| `LEANIX_TECHNICAL_USER` / `LEANIX_TECHNICAL_USER_PASSWORD` | Technical-user client credentials |
| `LEANIX_TOKEN` / `LEANIX_API_TOKEN` | API-token alternative |
| `LEANIX_OAUTH_CLIENT_ID` | Browser OAuth client identifier |
| `AUDIENCE` / `DELEGATED_SCOPES` | RFC 8693 delegated-token target and scopes |

Provide one authentication path. Do not copy a credential value into a skill,
manifest, command history, trace attribute, or knowledge-graph property.

## TLS profile

Keep certificate verification mandatory. Select trust and client-certificate
policy with one of these AgentConfig interfaces:

- Set `TLS_PROFILE` and resolve its catalog through `TLS_PROFILES_REF`.
- Set `TLS_PROFILE_REF` to a direct secret reference containing the profile.

Use the profile for private CA bundles, mTLS material, proxy policy, and timeouts.
Do not add connector-specific verification booleans, hardcoded CA paths, warning
suppression, or any fallback that disables certificate verification.

## Readiness check

1. Run the AgentConfig/GraphOS doctor without echoing resolved secret values.
2. Confirm that the workspace URL has an HTTPS scheme and an allowed host.
3. Confirm that the selected TLS profile resolves and verification remains enabled.
4. Confirm that exactly one intended authentication path succeeds.
5. Discover the live MCP tool schema before executing a workflow.

## Optional hosted MCP federation

GraphOS can mount a hosted MCP child only from an explicitly selected generic
`AgentConfig.provider_configs` profile. The package supplies no profile,
endpoint, credential, helper, trust path, or default. The `leanix-official`
child policy requires a verified TLS profile, an integrity-pinned preinstalled
helper, and read-only live tool annotations; unresolved or incomplete profiles
fail before spawn.
