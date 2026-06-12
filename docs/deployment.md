# Deployment

<!-- BEGIN GENERATED: deployment-options -->
## Deployment Options

`leanix-agent` exposes its MCP server (console script `leanix-mcp`) four ways. Pick the row that
matches where the server runs relative to your MCP client, then copy the matching
`mcp_config.json` below. Add the service-connection environment variables documented in the **Configuration** section.

| # | Option | Transport | Where it runs | `mcp_config.json` key |
|---|--------|-----------|---------------|------------------------|
| 1 | stdio | `stdio` | client launches a subprocess | `command` |
| 2 | Streamable-HTTP (local) | `streamable-http` | a local network port | `command` or `url` |
| 3 | Local container / uv | `stdio` or `streamable-http` | Docker / Podman / uv on this host | `command` or `url` |
| 4 | Remote URL | `streamable-http` | a remote host behind Caddy | `url` |

### 1. stdio (local subprocess)

The client launches the server over stdio via `uvx` — best for local IDEs
(Cursor, Claude Desktop, VS Code):

```json
{
  "mcpServers": {
    "leanix-mcp": {
      "command": "uvx",
      "args": ["--from", "leanix-agent", "leanix-mcp"]
    }
  }
}
```

### 2. Streamable-HTTP (local process)

Run the server as a long-lived HTTP process:

```bash
uvx --from leanix-agent leanix-mcp --transport streamable-http --host 0.0.0.0 --port 8000
curl -s http://localhost:8000/health        # {"status":"OK"}
```

Then either let the client launch it:

```json
{
  "mcpServers": {
    "leanix-mcp": {
      "command": "uvx",
      "args": ["--from", "leanix-agent", "leanix-mcp", "--transport", "streamable-http", "--port", "8000"],
      "env": {
        "TRANSPORT": "streamable-http",
        "HOST": "0.0.0.0",
        "PORT": "8000"
      }
    }
  }
}
```

…or connect to the already-running process by URL:

```json
{
  "mcpServers": {
    "leanix-mcp": { "url": "http://localhost:8000/mcp" }
  }
}
```

### 3. Local container / uv

**(a) Launch a container directly from `mcp_config.json`** (stdio over the container —
no ports to manage). Swap `docker` for `podman` for a daemonless runtime:

```json
{
  "mcpServers": {
    "leanix-mcp": {
      "command": "docker",
      "args": [
        "run", "-i", "--rm",
        "-e", "TRANSPORT=stdio",
        "knucklessg1/leanix-agent:latest"
      ]
    }
  }
}
```

**(b) Run a local streamable-http container, then connect by URL:**

```bash
docker run -d --name leanix-mcp -p 8000:8000 \
  -e TRANSPORT=streamable-http \
  -e PORT=8000 \
  knucklessg1/leanix-agent:latest
# or, from a clone of this repo:
docker compose -f docker/mcp.compose.yml up -d
```

```json
{
  "mcpServers": {
    "leanix-mcp": { "url": "http://localhost:8000/mcp" }
  }
}
```

**(c) From a local checkout with `uv`:**

```bash
uv run leanix-mcp --transport streamable-http --port 8000
```

### 4. Remote URL (deployed behind Caddy)

When the server is deployed remotely (e.g. as a Docker service) and published through
Caddy on the internal `*.arpa` zone, connect with the `"url"` key — no local process or
image required:

```json
{
  "mcpServers": {
    "leanix-mcp": { "url": "http://leanix-mcp.arpa/mcp" }
  }
}
```

Caddy reverse-proxies `http://leanix-mcp.arpa` to the container's `:8000`
streamable-http listener; `http://leanix-mcp.arpa/health` returns
`{"status":"OK"}` when the service is live.
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
    leanix-mcp --transport streamable-http --host 0.0.0.0 --port 8000
    ```
    A network server with a `/health` endpoint and `/mcp` route.

=== "sse"

    ```bash
    leanix-mcp --transport sse --host 0.0.0.0 --port 8000
    ```

Health check (HTTP transports):

```bash
curl -s http://localhost:8000/health        # {"status":"OK"}
```

## Configuration (environment)

`leanix-agent` is configured entirely from the environment. The **required** set for
a workspace connection:

| Var | Default | Meaning |
|---|---|---|
| `LEANIX_WORKSPACE` | `https://app.leanix.net` | Workspace base URL |
| `LEANIX_AUTH_METHOD` | `technical` | Auth mode: `technical`, `browser`, `token`, `api_token` |
| `LEANIX_API_TOKEN` | — | Static API token (token / api_token auth) |
| `LEANIX_TECHNICAL_USER` | — | Technical-user client id (technical auth) |
| `LEANIX_TECHNICAL_USER_PASSWORD` | — | Technical-user secret (technical auth) |
| `SSL_VERIFY` | `True` | Verify TLS certificates |
| `HOST` / `PORT` / `TRANSPORT` | `0.0.0.0` / `8000` / `stdio` | HTTP transport binding |

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
It reads a sibling `.env` and publishes the HTTP server on `:8000`:

```yaml
services:
  leanix-agent-mcp:
    image: knucklessg1/leanix-agent:latest
    container_name: leanix-agent-mcp
    hostname: leanix-agent-mcp
    restart: always
    env_file:
      - ../.env
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=streamable-http
    ports:
      - "8000:8000"
    healthcheck:
      test: ["CMD", "python3", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"]
      interval: 30s
      timeout: 10s
      retries: 3
```

```bash
cp .env.example .env          # then edit LEANIX_* values
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
leanix-agent --provider openai --model-id gpt-4o --api-key sk-...
```

```yaml
services:
  leanix-agent-mcp:
    image: knucklessg1/leanix-agent:latest
    hostname: leanix-agent-mcp
    env_file: [../.env]
    environment:
      - TRANSPORT=streamable-http
      - HOST=0.0.0.0
      - PORT=8000
    ports: ["8000:8000"]

  leanix-agent-agent:
    image: knucklessg1/leanix-agent:latest
    command: ["leanix-agent"]
    depends_on: [leanix-agent-mcp]
    env_file: [../.env]
    environment:
      - HOST=0.0.0.0
      - PORT=9004
      - MCP_URL=http://leanix-agent-mcp:8000/mcp
      - PROVIDER=${PROVIDER:-openai}
      - MODEL_ID=${MODEL_ID:-gpt-4o}
    ports: ["9004:9004"]
```

```bash
docker compose -f docker/agent.compose.yml up -d
```

## Behind a Caddy reverse proxy

Expose the HTTP server on a hostname with automatic TLS. Add to your `Caddyfile`:

```caddy
# Internal (self-signed) — homelab .arpa zone
leanix-agent.arpa {
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
curl -s "http://technitium.arpa:5380/api/zones/records/add" \
  --data-urlencode "token=$TECHNITIUM_DNS_TOKEN" \
  --data-urlencode "domain=leanix-agent.arpa" \
  --data-urlencode "zone=arpa" \
  --data-urlencode "type=A" \
  --data-urlencode "ipAddress=10.0.0.10" \
  --data-urlencode "ttl=3600"
```

…or add an **A record** `leanix-agent.arpa → <caddy-host-ip>` in the Technitium web
console (`http://technitium.arpa:5380`). The ecosystem
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
        "LEANIX_WORKSPACE": "https://your-workspace.leanix.net",
        "LEANIX_API_TOKEN": "your_leanix_api_token"
      }
    }
  }
}
```

For a remote HTTP server, point the client at `http://leanix-agent.arpa/mcp` instead.
