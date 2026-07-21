# Hosted MCP federation

The hosted LeanIX MCP surface is an optional GraphOS child, not a checked-in
connection. The package contains only the validation contract. Endpoint,
toolsets, helper selection, authentication selection, and TLS trust remain in a
single runtime-selected `AgentConfig.provider_configs` profile.

The profile itself is the enable switch and defaults to disabled. No profile is
selected by this package. GraphOS wiring must pass the selected profile name to
`resolve_official_mcp_federation`; an absent, disabled, incomplete, or
unresolvable profile fails before a process is started or a network connection
is attempted.

## Provider-profile contract

The current contract uses only the generic provider fields below. There are no
provider-specific environment-variable aliases and no legacy field names.

| Generic profile field | Contract |
|---|---|
| `enabled` | Must be explicitly true. False is the default. |
| `endpoint_ref` | Required runtime reference resolving to a credential-free HTTPS endpoint. |
| `tls_profile` or `tls_profile_ref` | Exactly one verified runtime trust profile is required. |
| `credential_refs` | Must remain empty; credentials are not copied into helper environment variables. |
| `selector_refs` | Contains only the bounded selectors listed below. |

The selector references resolve at the trusted runtime boundary:

| Selector | Resolved shape |
|---|---|
| `HOSTED_MCP_TOOLSETS` | Non-empty JSON array of at most 10 unique identifiers, each at most 50 characters. |
| `HOSTED_MCP_HELPER_COMMAND` | Canonical absolute path to a preinstalled executable. |
| `HOSTED_MCP_HELPER_SHA256` | Lowercase SHA-256 digest for that executable. |
| `HOSTED_MCP_AUTH_PROFILE` | Identifier for the helper's externally managed authentication profile. |
| `HOSTED_MCP_READ_ONLY_TOOLS` | Optional JSON array that narrows the live read-only catalog. |

The helper is never fetched on demand and no shell command is constructed. Its
file must be executable, immutable to group and other users on POSIX, and match
the configured digest. Wiring must call `plan.verify_helper()` immediately
before spawn so an integrity failure remains fail closed.

The preinstalled helper consumes the standard isolated provider-child
projection (`AGENT_PROVIDER_PROFILE` plus reference-only `PROVIDER_CONFIGS`).
That projection carries the resolved endpoint, toolset/auth selectors, and TLS
profile only for the child lifetime. This provider contract rejects credential
references, so no credential is projected to the helper.

## Read-only admission and schema drift

The federation has no write-capable mode. A live tool is admitted only when its
MCP annotation sets `readOnlyHint` to the boolean value `true`; an absent,
malformed, or false annotation is denied. The optional read-only tool list can
further narrow that set but cannot promote an unannotated tool.

`fingerprint_read_only_catalog` produces a bounded canonical SHA-256 fingerprint
from the admitted live tool names and input schemas. Record that digest in
deployment evidence to detect permission-, license-, or rollout-driven schema
changes without storing tenant content or connection details in this package.

## Wiring boundary

The server integration owns profile selection, helper process lifecycle, and
transport construction. It consumes the returned plan only in memory, applies
the plan's TLS object to the hosted connection, rechecks helper integrity at the
spawn boundary, filters the live catalog through `plan.allows_tool`, and closes
the plan during teardown. Logging or tracing the plan fields is prohibited; its
representation is intentionally redacted.

In a deployment-owned GraphOS fleet catalog, select the installed policy and
the deployment's profile explicitly:

```json
{
  "mcpServers": {
    "enterprise-architecture-hosted": {
      "runtime_policy": "leanix-official",
      "provider_profile": "<deployment-profile>"
    }
  }
}
```

The package ships no such fleet entry and provides no profile or endpoint
default. GraphOS resolves the policy at mount/probe time, re-verifies the helper
as the next operation before stdio spawn, applies read-only admission after
every live `tools/list`, fingerprints the admitted schemas, rechecks admission
on every delegated call, and closes the child before erasing the plan during
reload or shutdown.
