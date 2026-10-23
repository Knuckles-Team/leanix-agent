# CONN-LEANIX-AGENT-CONNECTOR-CONTENT — Design and implementation plan

Governing spec: [spec.md](spec.md).

## Architecture

`pyproject.toml` declares `leanix-mcp` as the connector identity. `create_mcp_server` resolves the packaged content of `leanix_agent` from it.
