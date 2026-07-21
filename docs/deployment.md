# Deployment

<!-- BEGIN GENERATED: deployment-options -->
## Deployment Options

`leanix-agent` supports local stdio, a loopback-only development listener, a
least-privilege stdio container, and a remote authenticated HTTPS boundary.
Provider endpoint, credential, selector, identity, and trust material are supplied
at runtime through `AgentConfig`; none is stored in this repository.

### Installed stdio process

```json
{
  "mcpServers": {
    "leanix": {
      "command": "leanix-mcp",
      "args": [],
      "env": {"MCP_TOOL_MODE": "intent"}
    }
  }
}
```

### Loopback development listener

```bash
leanix-mcp --transport streamable-http --host 127.0.0.1 --port 8000
```

Do not expose this listener beyond loopback. Network deployments require direct TLS
or an explicitly trusted TLS-terminating ingress, configured authentication, exact
`MCP_ALLOWED_HOSTS`, and an exact trusted-proxy CIDR policy.

### Least-privilege local container

```bash
docker run -i --rm \
  --read-only \
  --cap-drop=ALL \
  --security-opt=no-new-privileges \
  --pids-limit=256 \
  --tmpfs /tmp:rw,noexec,nosuid,nodev,size=64m \
  -e TRANSPORT=stdio \
  registry.example.invalid/leanix-agent@sha256:<digest> leanix-mcp
```

The operator projects the selected AgentConfig profile into the process at runtime;
the image remains immutable and contains no environment connection profile.

### Remote authenticated HTTPS endpoint

```json
{
  "mcpServers": {
    "leanix": {"url": "https://service.example.invalid/mcp"}
  }
}
```

Store the real remote URL, outbound identity reference, and TLS-profile reference in
`AgentConfig`, not in MCP client JSON or documentation.
<!-- END GENERATED: deployment-options -->

This page covers running `leanix-agent` as a long-lived service: the transports, a
Docker Compose stack, the optional A2A agent server, putting it behind a Caddy
reverse proxy, and giving it a DNS name with Technitium.

> `leanix-agent` ships an **MCP server** (console script `leanix-mcp`) and an
> **A2A agent server** (console script `leanix-agent`). The MCP server is the typed,
> deterministic tool surface; the agent server wraps it as a Pydantic-AI agent for
> agent-to-agent orchestration.

## Run the MCP server

The transport is selected with `--transport` (or the `TRANSPORT` env var):

=== "stdio (default)"

    ```bash
    leanix-mcp
    ```
    For IDE / desktop MCP clients that launch the server as a subprocess.

=== "streamable-http"

    ```bash
    leanix-mcp --transport streamable-http --host 127.0.0.1 --port 8000
    ```
    A network server with a `/health` endpoint and `/mcp` route.

=== "sse"

    ```bash
    leanix-mcp --transport sse --host 127.0.0.1 --port 8000
    ```

Health check (HTTP transports):

```bash
curl -s http://localhost:8000/health        # {"status":"ok"}
```

## Configuration (environment)

`leanix-agent` is configured through `AgentConfig`; a supervisor may project
runtime environment overrides into the provider child. The required connection
fields are:

| Var | Default | Meaning |
|---|---|---|
| `LEANIX_WORKSPACE` | `https://app.leanix.net` | Workspace base URL |
| `LEANIX_AUTH_METHOD` | `technical` | Auth mode: `technical`, `browser`, `token`, `api_token` |
| `LEANIX_API_TOKEN` | — | Static API token (token / api_token auth) |
| `LEANIX_TECHNICAL_USER` | — | Technical-user client id (technical auth) |
| `LEANIX_TECHNICAL_USER_PASSWORD` | — | Technical-user secret (technical auth) |
| `TLS_PROFILE_REF` | — | Optional secret reference for CA, mTLS, and proxy policy |
| `HOST` / `PORT` / `TRANSPORT` | `127.0.0.1` / `8000` / `stdio` | HTTP transport binding |

Certificate and hostname verification remain mandatory. Select a named profile with
`TLS_PROFILE` plus `TLS_PROFILES_REF`, or use `TLS_PROFILE_REF` directly. Profiles
are resolved through `AgentConfig`; certificate material and machine paths are not
stored in this package.

Each LeanIX service domain has its own `LEANIX_*TOOL` toggle (for example
`LEANIX_PATHFINDERTOOL`, `LEANIX_METRICSTOOL`, `GRAPHQLTOOL`) so you can register
only the tools you need. The full set, including the interactive OAuth and OIDC
delegation variables, is documented in
[`.env.example`](https://github.com/Knuckles-Team/leanix-agent/blob/main/.env.example).
Copy it to `.env` and fill in only what you use. The authentication modes are
detailed in [Introspection & Filtering](introspection_and_filtering.md).

## Backing service

SAP LeanIX is a **managed SaaS** Enterprise Architecture Management platform; there
is no local backing system to provision. `leanix-agent` connects to your hosted
workspace, so only connection configuration is required: point `LEANIX_WORKSPACE` at
your workspace URL and supply credentials via one of the supported authentication
modes. The connector remains inactive when credentials are absent.

## Docker Compose

The repo ships [`docker/mcp.compose.yml`](https://github.com/Knuckles-Team/leanix-agent/blob/main/docker/mcp.compose.yml).
It reads a sibling `.env`, requires an immutable image digest, and publishes the
HTTP server only on the loopback interface. The service runs as UID/GID 10001
with a read-only root filesystem, dropped capabilities, bounded resources, and
`no-new-privileges`.

```bash
export LEANIX_AGENT_MCP_IMAGE='registry.example.invalid/leanix-agent@sha256:<digest>'
docker compose -f docker/mcp.compose.yml up -d
docker compose -f docker/mcp.compose.yml logs -f
```

## Agent server (A2A)

For agent-to-agent orchestration, run the Pydantic-AI agent server (console script
`leanix-agent`). It connects to the MCP server over `MCP_URL` and exposes its own
HTTP surface on `:9004`. The repo ships
[`docker/agent.compose.yml`](https://github.com/Knuckles-Team/leanix-agent/blob/main/docker/agent.compose.yml),
which deploys both the MCP server and the agent server on one network:

```bash
# Local
leanix-agent --provider <configured-provider> --model-id <configured-model>
```

```bash
export LEANIX_AGENT_MCP_IMAGE='registry.example.invalid/leanix-agent@sha256:<digest>'
export LEANIX_AGENT_AGENT_IMAGE='registry.example.invalid/leanix-agent@sha256:<digest>'
export PROVIDER='<configured-provider>'
export MODEL_ID='<configured-model>'
docker compose -f docker/agent.compose.yml up -d
```

The compose definition applies the same least-privilege controls to both
services and publishes ports 8000 and 9004 on loopback only. A reverse proxy is
the explicit boundary for non-local access.

## Behind a Caddy reverse proxy

Expose the HTTP server on a hostname with automatic TLS. Add to your `Caddyfile`:

```caddy
# Operator-owned internal DNS zone
leanix-agent.example.com {
    tls internal
    reverse_proxy leanix-agent-mcp:8000
}
```

```caddy
# Public — automatic Let's Encrypt
leanix-agent.example.com {
    reverse_proxy leanix-agent-mcp:8000
}
```

Reload Caddy:

```bash
docker compose -f services/caddy/compose.yml exec caddy caddy reload --config /etc/caddy/Caddyfile
```

## DNS with Technitium

Point the hostname at the host running Caddy. Via the Technitium API:

```bash
curl -s "https://dns.example.invalid/api/zones/records/add" \
  --data-urlencode "token=$TECHNITIUM_DNS_TOKEN" \
  --data-urlencode "domain=leanix-agent.example.invalid" \
  --data-urlencode "zone=example.invalid" \
  --data-urlencode "type=A" \
  --data-urlencode "ipAddress=<caddy-host-ip>" \
  --data-urlencode "ttl=3600"
```

…or add an **A record** `leanix-agent.example.invalid → <caddy-host-ip>` in the Technitium web
console (`https://dns.example.invalid`). The ecosystem
[`technitium-dns-mcp`](https://knuckles-team.github.io/technitium-dns-mcp/) automates
this as a tool.

## Register with an MCP client

Add to your client's `mcp_config.json`:

```json
{
  "mcpServers": {
    "leanix-agent": {
      "command": "uv",
      "args": ["run", "leanix-mcp"],
      "env": {
        "LEANIX_WORKSPACE": "https://workspace.example.invalid"
      }
    }
  }
}
```

The supervisor injects the selected authentication material into the child. For a
remote server, use the operator-supplied authenticated HTTPS URL instead.
