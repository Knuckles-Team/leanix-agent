# Installation

`leanix-agent` is a standard Python package and a prebuilt container image. Pick the
path that matches how you want to run it.

## Requirements

- **Python 3.11 – 3.14**.
- A reachable **SAP LeanIX workspace** and credentials (API token, technical user,
  or interactive OAuth) — see [Deployment](deployment.md#backing-service) for the
  connection details.

## From PyPI (recommended)

```bash
pip install leanix-agent
```

### Optional extras

The base install ships the MCP server runtime. Install the extra for what you need:

| Extra | Install | Pulls in |
|---|---|---|
| (base) | `pip install leanix-agent` | FastMCP MCP-server runtime (`agent-utilities[mcp]`) |
| `agent` | `pip install "leanix-agent[agent]"` | Pydantic-AI agent server + Logfire tracing |
| `gql` | `pip install "leanix-agent[gql]"` | `gql` for the Pathfinder GraphQL client |
| `all` | `pip install "leanix-agent[all]"` | Everything above |

```bash
# Typical: run the MCP server with the GraphQL client
pip install "leanix-agent[gql]"
```

## From source

```bash
git clone https://github.com/Knuckles-Team/leanix-agent.git
cd leanix-agent
pip install -e ".[all]"          # editable install with every extra
```

With [`uv`](https://docs.astral.sh/uv/):

```bash
uv pip install -e ".[all]"
uv run leanix-mcp
```

## Prebuilt Docker image

A multi-stage, slim image is published on every release (entrypoint `leanix-mcp`):

```bash
docker pull knucklessg1/leanix-agent:latest

docker run --rm -i \
  -e LEANIX_WORKSPACE=https://your-workspace.leanix.net \
  -e LEANIX_API_TOKEN=your_leanix_api_token \
  knucklessg1/leanix-agent:latest        # stdio transport (default)
```

For an HTTP server with a published port and the agent server, see
[Deployment](deployment.md).

## Verify the install

```bash
leanix-mcp --help
python -c "import leanix_agent; print(leanix_agent.__version__)"
```

## Next steps

- **[Deployment](deployment.md)** — run it as a long-lived MCP server behind Caddy + DNS.
- **[Usage](usage.md)** — call the tools, the API, and the CLI.
- **[Configuration](deployment.md#configuration-environment)** — every environment variable.
