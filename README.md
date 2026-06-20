# Leanix Agent
## CLI or API | MCP | Agent

![PyPI - Version](https://img.shields.io/pypi/v/leanix-agent)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
![PyPI - Downloads](https://img.shields.io/pypi/dd/leanix-agent)
![GitHub Repo stars](https://img.shields.io/github/stars/Knuckles-Team/leanix-agent)
![GitHub forks](https://img.shields.io/github/forks/Knuckles-Team/leanix-agent)
![GitHub contributors](https://img.shields.io/github/contributors/Knuckles-Team/leanix-agent)
![PyPI - License](https://img.shields.io/pypi/l/leanix-agent)
![GitHub](https://img.shields.io/github/license/Knuckles-Team/leanix-agent)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Knuckles-Team/leanix-agent)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Knuckles-Team/leanix-agent)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/Knuckles-Team/leanix-agent)
![GitHub issues](https://img.shields.io/github/issues/Knuckles-Team/leanix-agent)
![GitHub top language](https://img.shields.io/github/languages/top/Knuckles-Team/leanix-agent)
![GitHub language count](https://img.shields.io/github/languages/count/Knuckles-Team/leanix-agent)
![GitHub repo size](https://img.shields.io/github/repo-size/Knuckles-Team/leanix-agent)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/Knuckles-Team/leanix-agent)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/leanix-agent)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/leanix-agent)

*Version: 0.33.0*

> **Documentation** — Installation, deployment, usage across the API, CLI, and MCP
> interfaces, and the authentication and dynamic-filtering guides are maintained in
> the [official documentation](https://knuckles-team.github.io/leanix-agent/).

---

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [CLI or API](#cli-or-api)
- [MCP](#mcp)
  - [Available MCP Tools](#available-mcp-tools)
  - [MCP Configuration Examples](#mcp-configuration-examples)
  - [Dynamic Tool Selection & Visibility](#dynamic-tool-selection--visibility)
- [Agent](#agent)
  - [Running the Agent CLI](#running-the-agent-cli)
  - [Docker Compose Orchestration](#docker-compose-orchestration)
- [Security & Governance](#security--governance)
- [Installation](#installation)
- [Documentation](#documentation)
- [Contribute](#contribute)

---

## Overview

**Leanix Agent** is a production-grade Agent and Model Context Protocol (MCP) server designed to interface directly with Agent package for communicating with LeanIX Enterprise Architecture Management via REST APIs and GraphQL..

---

## Key Features

- **Consolidated Action-Routed MCP Tools:** Minimizes token overhead and eliminates tool bloat in LLM contexts by grouping methods into optimized, togglable tool modules.
- **Enterprise-Grade Security:** Comprehensive support for Eunomia policies, OIDC token delegation, and granular execution context tracking.
- **Integrated Graph Agent:** Built-in Pydantic AI agent supporting the Agent Control Protocol (ACP) and standard Web interfaces (AG-UI).
- **Native Telemetry & Tracing:** Out-of-the-box OpenTelemetry exports and native Langfuse tracing.

---

## CLI or API

This agent wraps the Agent package for communicating with LeanIX Enterprise Architecture Management via REST APIs and GraphQL. API. You can interact with it programmatically or via its integrated execution entrypoints.

Detailed instructions on how to use the underlying API wrappers, extended schema bindings, and developer SDK references are maintained in [docs/index.md](docs/index.md).

---

## MCP

This server utilizes dynamic Action-Routed tools to optimize token overhead and maximize IDE compatibility.

### Available MCP Tools
Auto-generated — do not edit between the markers below.
<!-- MCP-TOOLS-TABLE:START -->

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `leanix_discover_meta_model` | `LEANIX-PATHFINDERTOOL` | Discover the custom LeanIX meta-model/data-model schema including custom attributes and fields in real-time. |
| `leanix_graphql` | `GRAPHQLTOOL` | Execute raw GraphQL queries and mutations natively on LeanIX Pathfinder API. |
| `leanix_leanix_ai_inventory_builder` | `LEANIX-AI-INVENTORY-BUILDERTOOL` | Manage leanix leanix ai inventory builder operations. |
| `leanix_leanix_apptio_connector` | `LEANIX-APPTIO-CONNECTORTOOL` | Manage leanix leanix apptio connector operations. |
| `leanix_leanix_automations` | `LEANIX-AUTOMATIONSTOOL` | Manage leanix leanix automations operations. |
| `leanix_leanix_discovery_ai_agents` | `LEANIX-DISCOVERY-AI-AGENTSTOOL` | Manage leanix leanix discovery ai agents operations. |
| `leanix_leanix_discovery_linking_v1` | `LEANIX-DISCOVERY-LINKING-V1TOOL` | Manage leanix leanix discovery linking v1 operations. |
| `leanix_leanix_discovery_linking_v2` | `LEANIX-DISCOVERY-LINKING-V2TOOL` | Manage leanix leanix discovery linking v2 operations. |
| `leanix_leanix_discovery_saas` | `LEANIX-DISCOVERY-SAASTOOL` | Manage leanix leanix discovery saas operations. |
| `leanix_leanix_discovery_sap` | `LEANIX-DISCOVERY-SAPTOOL` | Manage leanix leanix discovery sap operations. |
| `leanix_leanix_discovery_sap_extension` | `LEANIX-DISCOVERY-SAP-EXTENSIONTOOL` | Manage leanix leanix discovery sap extension operations. |
| `leanix_leanix_documents` | `LEANIX-DOCUMENTSTOOL` | Manage leanix leanix documents operations. |
| `leanix_leanix_impacts` | `LEANIX-IMPACTSTOOL` | Manage leanix leanix impacts operations. |
| `leanix_leanix_integration_api` | `LEANIX-INTEGRATION-APITOOL` | Manage leanix leanix integration api operations. |
| `leanix_leanix_integration_collibra` | `LEANIX-INTEGRATION-COLLIBRATOOL` | Manage leanix leanix integration collibra operations. |
| `leanix_leanix_integration_servicenow` | `LEANIX-INTEGRATION-SERVICENOWTOOL` | Manage leanix leanix integration servicenow operations. |
| `leanix_leanix_integration_signavio` | `LEANIX-INTEGRATION-SIGNAVIOTOOL` | Manage leanix leanix integration signavio operations. |
| `leanix_leanix_inventory_data_quality` | `LEANIX-INVENTORY-DATA-QUALITYTOOL` | Manage leanix leanix inventory data quality operations. |
| `leanix_leanix_managed_code_execution` | `LEANIX-MANAGED-CODE-EXECUTIONTOOL` | Manage leanix leanix managed code execution operations. |
| `leanix_leanix_metrics` | `LEANIX-METRICSTOOL` | Manage leanix leanix metrics operations. |
| `leanix_leanix_mtm` | `LEANIX-MTMTOOL` | Manage leanix leanix mtm operations. |
| `leanix_leanix_navigation` | `LEANIX-NAVIGATIONTOOL` | Manage leanix leanix navigation operations. |
| `leanix_leanix_pathfinder` | `LEANIX-PATHFINDERTOOL` | Manage leanix leanix pathfinder operations. |
| `leanix_leanix_poll` | `LEANIX-POLLTOOL` | Manage leanix leanix poll operations. |
| `leanix_leanix_reference_data` | `LEANIX-REFERENCE-DATATOOL` | Manage leanix leanix reference data operations. |
| `leanix_leanix_reference_data_catalog` | `LEANIX-REFERENCE-DATA-CATALOGTOOL` | Manage leanix leanix reference data catalog operations. |
| `leanix_leanix_storage` | `LEANIX-STORAGETOOL` | Manage leanix leanix storage operations. |
| `leanix_leanix_survey` | `LEANIX-SURVEYTOOL` | Manage leanix leanix survey operations. |
| `leanix_leanix_synclog` | `LEANIX-SYNCLOGTOOL` | Manage leanix leanix synclog operations. |
| `leanix_leanix_technology_discovery` | `LEANIX-TECHNOLOGY-DISCOVERYTOOL` | Manage leanix leanix technology discovery operations. |
| `leanix_leanix_todo` | `LEANIX-TODOTOOL` | Manage leanix leanix todo operations. |
| `leanix_leanix_transformations` | `LEANIX-TRANSFORMATIONSTOOL` | Manage leanix leanix transformations operations. |
| `leanix_leanix_webhooks` | `LEANIX-WEBHOOKSTOOL` | Manage leanix leanix webhooks operations. |

_33 action-routed tools (default `MCP_TOOL_MODE=condensed`). Each is enabled unless its toggle is set false; set `MCP_TOOL_MODE=verbose` (or `both`) for the 1:1 per-operation surface. Auto-generated — do not edit._
<!-- MCP-TOOLS-TABLE:END -->

Detailed tool schemas, parameter shapes, and validation constraints are preserved in [docs/mcp.md](docs/mcp.md).

### Dynamic Tool Selection & Visibility

This MCP server supports dynamic toolset selection and visibility filtering at runtime. This allows you to restrict the set of exposed tools in order to prevent blowing up the LLM's context window.

You can configure tool filtering via multiple input channels:

- **CLI Arguments:** Pass `--tools` or `--toolsets` (or their disabled counterparts `--disabled-tools` and `--disabled-toolsets`) during startup.
- **Environment Variables:** Define standard environment variables:
  - `MCP_ENABLED_TOOLS` / `MCP_DISABLED_TOOLS`
  - `MCP_ENABLED_TAGS` / `MCP_DISABLED_TAGS`
- **HTTP SSE Request Headers:** Pass custom headers during transport initialization:
  - `x-mcp-enabled-tools` / `x-mcp-disabled-tools`
  - `x-mcp-enabled-tags` / `x-mcp-disabled-tags`
- **HTTP SSE Request Query Parameters:** Append query parameters directly to your transport connection URL:
  - `?tools=tool1,tool2`
  - `?tags=tag1`

When query strings or parameters are supplied, an LLM-free **Knowledge Graph resolution layer** (using `DynamicToolOrchestrator`) matches query intents against known tool tags, names, or descriptions, with safe fallback and automated 24-hour background cache refreshing.

---

### MCP Configuration Examples

#### stdio Transport (Recommended for local IDEs e.g., Cursor, Claude Desktop)
Configure your IDE's `mcp.json` to launch the MCP server via `uvx`:

```json
{
  "mcpServers": {
    "leanix-agent": {
      "command": "uvx",
      "args": [
        "--from",
        "leanix-agent",
        "leanix-mcp"
      ],
      "env": {
        "LEANIX_WORKSPACE": "your_leanix_workspace_here",
        "LEANIX_API_TOKEN": "your_leanix_api_token_here",
        "SSL_VERIFY": "your_ssl_verify_here",
        "DEBUG": "your_debug_here",
        "PYTHONUNBUFFERED": "your_pythonunbuffered_here",
        "LEANIX_TOKEN": "your_leanix_token_here"
      }
    }
  }
}
```

#### Streamable-HTTP Transport (Recommended for production deployments)
Configure your client's `mcp.json` to launch the Streamable-HTTP server via `uvx` with explicit host and port definition:

```json
{
  "mcpServers": {
    "leanix-agent": {
      "command": "uvx",
      "args": [
        "--from",
        "leanix-agent",
        "leanix-mcp"
      ],
      "env": {
        "TRANSPORT": "streamable-http",
        "HOST": "0.0.0.0",
        "PORT": "8000",
        "LEANIX_WORKSPACE": "your_leanix_workspace_here",
        "LEANIX_API_TOKEN": "your_leanix_api_token_here",
        "SSL_VERIFY": "your_ssl_verify_here",
        "DEBUG": "your_debug_here",
        "PYTHONUNBUFFERED": "your_pythonunbuffered_here",
        "LEANIX_TOKEN": "your_leanix_token_here"
      }
    }
  }
}
```

Alternatively, connect to a pre-deployed remote or local Streamable-HTTP instance:

```json
{
  "mcpServers": {
    "leanix-agent": {
      "url": "http://localhost:8000/leanix-agent/mcp"
    }
  }
}
```

Deploying the Streamable-HTTP server via Docker:

```bash
docker run -d \
  --name leanix-agent-mcp \
  -p 8000:8000 \
  -e TRANSPORT=streamable-http \
  -e PORT=8000 \
  -e LEANIX_WORKSPACE="your_value" \
  -e LEANIX_API_TOKEN="your_value" \
  -e SSL_VERIFY="your_value" \
  -e DEBUG="your_value" \
  -e PYTHONUNBUFFERED="your_value" \
  -e LEANIX_TOKEN="your_value" \
  knucklessg1/leanix-agent:latest
```

---

<!-- BEGIN GENERATED: additional-deployment-options -->
### Additional Deployment Options

`leanix-agent` can also run as a **local container** (Docker / Podman / `uv`) or be
consumed from a **remote deployment**. The
[Deployment guide](https://knuckles-team.github.io/leanix-agent/deployment/) has full, copy-paste
`mcp_config.json` for all four transports — **stdio**, **streamable-http**,
**local container / uv**, and **remote URL**:

- **Local container / uv** — launch the server from `mcp_config.json` via `uvx`,
  `docker run`, or `podman run`, or point at a local streamable-http container by `url`.
- **Remote URL** — connect to a server deployed behind Caddy at
  `http://leanix-mcp.arpa/mcp` using the `"url"` key.
<!-- END GENERATED: additional-deployment-options -->

## Agent

This repository features a fully integrated Pydantic AI Graph Agent. It communicates over the **Agent Control Protocol (ACP)** and interacts seamlessly with the **Agent Web UI (AG-UI)** and Terminal interface.

### Running the Agent CLI
To start the interactive command-line agent:

```bash
# Set credentials
export LEANIX_WORKSPACE="your_value"
export LEANIX_API_TOKEN="your_value"
export SSL_VERIFY="your_value"
export DEBUG="your_value"
export PYTHONUNBUFFERED="your_value"
export LEANIX_TOKEN="your_value"

# Run the agent server
leanix-agent --provider openai --model-id gpt-4o
```

### Docker Compose Orchestration
The following `docker/agent.compose.yml` configures the Agent, Web UI, and Terminal Interface together:

```yaml
version: '3.8'

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
      start_period: 10s
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

  leanix-agent-agent:
    image: knucklessg1/leanix-agent:latest
    container_name: leanix-agent-agent
    hostname: leanix-agent-agent
    restart: always
    depends_on:
      - leanix-agent-mcp
    env_file:
      - ../.env
    command: [ "leanix-agent" ]
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=9004
      - MCP_URL=http://leanix-agent-mcp:8000/mcp
      - PROVIDER=${PROVIDER:-openai}
      - MODEL_ID=${MODEL_ID:-gpt-4o}
      - ENABLE_WEB_UI=True
      - ENABLE_OTEL=True
    ports:
      - "9004:9004"
    healthcheck:
      test: ["CMD", "python3", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:9004/health')"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

```

Detailed graph node architecture explanations, custom skill configurations, and agentic trace guides are available in [docs/agent.md](docs/agent.md).

---

## Security & Governance

Built directly upon the enterprise-ready [`agent-utilities`](https://github.com/Knuckles-Team/agent-utilities) core, standard security parameters are fully supported:

### Access Control & Policy Enforcement
- **Eunomia Policies:** Fine-grained, policy-driven tool authorization. Supports `none`, local `embedded` (`mcp_policies.json`), or centralized `remote` modes.
- **OIDC Token Delegation:** Compliant with RFC 8693 token exchange for flowing authenticating user credentials from Web UI / ACP → Agent → MCP.
- **Scoped Credentials:** Execution context runs restricted to the specific caller identity.

### Runtime Security Grid
| Feature | Functionality | Enablement |
|---------|---------------|------------|
| **Tool Guard** | Sensitivity inspection with human-in-the-loop validation | Enabled by default |
| **Prompt Injection Defense** | Input scanning, repetition monitoring, and recursive loop blocks | Enabled by default |
| **Context Safety Guard** | Stuck-loop detectors and contextual overflow preemptive alerts | Enabled by default |

---

## Installation

Install the Python package locally:

```bash
# Using uv (highly recommended)
uv pip install leanix-agent[all]

# Using standard pip
python -m pip install leanix-agent[all]
```

---

## Documentation

The complete documentation is published as the
[official documentation site](https://knuckles-team.github.io/leanix-agent/) and is
the recommended reference for installation, deployment, and day-to-day operation.

| Page | Contents |
|---|---|
| [Installation](https://knuckles-team.github.io/leanix-agent/installation/) | pip, source, extras, prebuilt Docker image |
| [Deployment](https://knuckles-team.github.io/leanix-agent/deployment/) | run the MCP and agent servers, Compose, Caddy + Technitium, env config |
| [Usage](https://knuckles-team.github.io/leanix-agent/usage/) | the MCP tools, the `LeanixApi` and `GraphQL` clients, the CLI |
| [Overview](https://knuckles-team.github.io/leanix-agent/overview/) | the standardized agent-package pattern and concept registry |
| [Introspection & Filtering](https://knuckles-team.github.io/leanix-agent/introspection_and_filtering/) | authentication modes and dynamic toolset filtering |
| [Concepts](https://knuckles-team.github.io/leanix-agent/concepts/) | concept registry (`CONCEPT:LIX-*`) |

---

## Repository Owners

<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=Knucklessg1&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/Knucklessg1)
![GitHub User's stars](https://img.shields.io/github/stars/Knucklessg1)

---

## Contribute

Contributions are welcome! Please ensure code quality by executing local checks before submitting pull requests:
- Format code using `ruff format .`
- Lint code using `ruff check .`
- Validate type-safety with `mypy .`
- Execute test suites using `pytest`


<!-- BEGIN agent-os-genesis-deploy (generated; do not edit between markers) -->

## Deploy with `agent-os-genesis`

This package can be provisioned for you — skill-guided — by the **`agent-os-genesis`**
universal skill (its *single-package deploy mode*): it picks your install method, seeds
secrets to OpenBao/Vault (or `.env`), trusts your enterprise CA, registers the MCP
server, and verifies it — the same machinery that stands up the whole Agent OS, narrowed
to just this package. Ask your agent to **"deploy `leanix-agent` with agent-os-genesis"**.

| Install mode | Command |
|------|---------|
| Bare-metal, prod (PyPI) | `uvx leanix-mcp` · or `uv tool install leanix-agent` |
| Bare-metal, dev (editable) | `uv pip install -e ".[all]"` · or `pip install -e ".[all]"` |
| Container, prod | deploy `knucklessg1/leanix-agent:latest` via docker-compose / swarm / podman / podman-compose / kubernetes |
| Container, dev (editable) | deploy `docker/compose.dev.yml` (source-mounted at `/src`; edits live on restart) |

Secrets are read-existing + seeded via `vault_sync` — you are only prompted for what's missing.

<!-- END agent-os-genesis-deploy -->
