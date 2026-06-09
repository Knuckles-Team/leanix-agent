# leanix-agent

LeanIX Enterprise Architecture Management **MCP Server + A2A Agent** for the
agent-utilities ecosystem — typed REST and GraphQL access to FactSheets, metrics,
discovery, and integrations, with confidence-gated graph routing.

!!! info "Official documentation"
    This site is the canonical reference for `leanix-agent`, maintained alongside
    every release.

[![PyPI](https://img.shields.io/pypi/v/leanix-agent)](https://pypi.org/project/leanix-agent/)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
[![License](https://img.shields.io/pypi/l/leanix-agent)](https://github.com/Knuckles-Team/leanix-agent/blob/main/LICENSE)
[![GitHub](https://img.shields.io/badge/source-GitHub-181717?logo=github)](https://github.com/Knuckles-Team/leanix-agent)

## Overview

`leanix-agent` wraps the SAP LeanIX (Enterprise Architecture Management) REST and
Pathfinder GraphQL surface with typed, deterministic MCP tools, and ships an
optional Pydantic-AI agent server for agent-to-agent (A2A) orchestration. It
provides:

- **`LeanixApi`** — a REST facade over the Pathfinder API for FactSheet operations,
  with `GraphQL` for flexible Pathfinder queries and `get_client()` to build a
  client straight from the environment.
- **30+ LeanIX service domains** exposed as action-routed MCP tools (Pathfinder,
  Metrics, MTM, Discovery, Integrations, Webhooks, and more), filtered dynamically
  to keep the agent context lean.
- **Dynamic meta-model introspection** for zero-hallucination GraphQL schema
  discovery, plus interactive OAuth, OIDC delegation, and technical-user
  authentication.

## Explore the documentation

<div class="grid cards" markdown>

- :material-rocket-launch: **[Installation](installation.md)** — pip, source, extras, and the prebuilt Docker image.
- :material-server-network: **[Deployment](deployment.md)** — run the MCP and agent servers, Docker Compose, Caddy + Technitium.
- :material-console: **[Usage](usage.md)** — the MCP tools, the `LeanixApi` client, and the CLI.
- :material-sitemap: **[Architecture](overview.md)** — the standardized agent-package pattern and concept registry.
- :material-shield-key: **[Introspection & Filtering](introspection_and_filtering.md)** — authentication modes and dynamic toolset filtering.
- :material-tag-multiple: **[Concepts](concepts.md)** — the `CONCEPT:LIX-*` registry.

</div>

## Quick start

```bash
pip install leanix-agent
leanix-mcp                       # stdio MCP server (default transport)
```

Connect it to a LeanIX workspace:

```bash
export LEANIX_WORKSPACE=https://your-workspace.leanix.net
export LEANIX_API_TOKEN=your_leanix_api_token
leanix-mcp --transport streamable-http --host 0.0.0.0 --port 8000
```

See **[Installation](installation.md)** and **[Deployment](deployment.md)** for the
full matrix (PyPI extras, Docker image, all transports, the agent server, reverse
proxy, and DNS).
