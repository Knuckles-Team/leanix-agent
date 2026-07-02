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

*Version: 1.0.1*

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
- [Environment Variables](#environment-variables)
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

#### Condensed action-routed tools (default — `MCP_TOOL_MODE=condensed`)

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `leanix_discover_meta_model` | `LEANIX_PATHFINDERTOOL` | Discover the custom LeanIX meta-model/data-model schema including custom attributes and fields in real-time. |
| `leanix_graphql` | `GRAPHQLTOOL` | Execute raw GraphQL queries and mutations natively on LeanIX Pathfinder API. |
| `leanix_leanix_ai_inventory_builder` | `LEANIX_AI_INVENTORY_BUILDERTOOL` | Manage leanix leanix ai inventory builder operations. |
| `leanix_leanix_apptio_connector` | `LEANIX_APPTIO_CONNECTORTOOL` | Manage leanix leanix apptio connector operations. |
| `leanix_leanix_automations` | `LEANIX_AUTOMATIONSTOOL` | Manage leanix leanix automations operations. |
| `leanix_leanix_discovery_ai_agents` | `LEANIX_DISCOVERY_AI_AGENTSTOOL` | Manage leanix leanix discovery ai agents operations. |
| `leanix_leanix_discovery_linking_v1` | `LEANIX_DISCOVERY_LINKING_V1TOOL` | Manage leanix leanix discovery linking v1 operations. |
| `leanix_leanix_discovery_linking_v2` | `LEANIX_DISCOVERY_LINKING_V2TOOL` | Manage leanix leanix discovery linking v2 operations. |
| `leanix_leanix_discovery_saas` | `LEANIX_DISCOVERY_SAASTOOL` | Manage leanix leanix discovery saas operations. |
| `leanix_leanix_discovery_sap` | `LEANIX_DISCOVERY_SAPTOOL` | Manage leanix leanix discovery sap operations. |
| `leanix_leanix_discovery_sap_extension` | `LEANIX_DISCOVERY_SAP_EXTENSIONTOOL` | Manage leanix leanix discovery sap extension operations. |
| `leanix_leanix_documents` | `LEANIX_DOCUMENTSTOOL` | Manage leanix leanix documents operations. |
| `leanix_leanix_impacts` | `LEANIX_IMPACTSTOOL` | Manage leanix leanix impacts operations. |
| `leanix_leanix_integration_api` | `LEANIX_INTEGRATION_APITOOL` | Manage leanix leanix integration api operations. |
| `leanix_leanix_integration_collibra` | `LEANIX_INTEGRATION_COLLIBRATOOL` | Manage leanix leanix integration collibra operations. |
| `leanix_leanix_integration_servicenow` | `LEANIX_INTEGRATION_SERVICENOWTOOL` | Manage leanix leanix integration servicenow operations. |
| `leanix_leanix_integration_signavio` | `LEANIX_INTEGRATION_SIGNAVIOTOOL` | Manage leanix leanix integration signavio operations. |
| `leanix_leanix_inventory_data_quality` | `LEANIX_INVENTORY_DATA_QUALITYTOOL` | Manage leanix leanix inventory data quality operations. |
| `leanix_leanix_managed_code_execution` | `LEANIX_MANAGED_CODE_EXECUTIONTOOL` | Manage leanix leanix managed code execution operations. |
| `leanix_leanix_metrics` | `LEANIX_METRICSTOOL` | Manage leanix leanix metrics operations. |
| `leanix_leanix_mtm` | `LEANIX_MTMTOOL` | Manage leanix leanix mtm operations. |
| `leanix_leanix_navigation` | `LEANIX_NAVIGATIONTOOL` | Manage leanix leanix navigation operations. |
| `leanix_leanix_pathfinder` | `LEANIX_PATHFINDERTOOL` | Manage leanix leanix pathfinder operations. |
| `leanix_leanix_poll` | `LEANIX_POLLTOOL` | Manage leanix leanix poll operations. |
| `leanix_leanix_reference_data` | `LEANIX_REFERENCE_DATATOOL` | Manage leanix leanix reference data operations. |
| `leanix_leanix_reference_data_catalog` | `LEANIX_REFERENCE_DATA_CATALOGTOOL` | Manage leanix leanix reference data catalog operations. |
| `leanix_leanix_storage` | `LEANIX_STORAGETOOL` | Manage leanix leanix storage operations. |
| `leanix_leanix_survey` | `LEANIX_SURVEYTOOL` | Manage leanix leanix survey operations. |
| `leanix_leanix_synclog` | `LEANIX_SYNCLOGTOOL` | Manage leanix leanix synclog operations. |
| `leanix_leanix_technology_discovery` | `LEANIX_TECHNOLOGY_DISCOVERYTOOL` | Manage leanix leanix technology discovery operations. |
| `leanix_leanix_todo` | `LEANIX_TODOTOOL` | Manage leanix leanix todo operations. |
| `leanix_leanix_transformations` | `LEANIX_TRANSFORMATIONSTOOL` | Manage leanix leanix transformations operations. |
| `leanix_leanix_webhooks` | `LEANIX_WEBHOOKSTOOL` | Manage leanix leanix webhooks operations. |

#### Verbose 1:1 API-mapped tools (`MCP_TOOL_MODE=verbose` or `both`)

<details>
<summary>2 per-operation tools — one per public API method (click to expand)</summary>

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `leanix_get_factsheet` | `LEANIX_APITOOL` | Get a specific FactSheet by ID. |
| `leanix_get_factsheets` | `LEANIX_APITOOL` | Get a list of FactSheets. |

</details>

_33 action-routed tool(s) (default) · 2 verbose 1:1 tool(s). Each is enabled unless its `<DOMAIN>TOOL` toggle is set false; `MCP_TOOL_MODE` selects the surface (`condensed` default · `verbose` 1:1 · `both`). Auto-generated — do not edit._
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

<!-- MCP-CONFIG-EXAMPLES:START -->

> **Install the slim `[mcp]` extra.** All examples install `leanix-agent[mcp]` — the
> MCP-server extra that pulls only the FastMCP / FastAPI tooling (`agent-utilities[mcp]`).
> It deliberately **excludes** the heavy agent runtime (`pydantic-ai`, the epistemic-graph
> engine, `dspy`, `llama-index`), so `uvx` / container installs are far smaller. Use the
> full `[agent]` extra only when you need the integrated Pydantic AI agent.

#### stdio Transport (local IDEs — Cursor, Claude Desktop, VS Code)

```json
{
  "mcpServers": {
    "leanix-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "leanix-agent[mcp]",
        "leanix-mcp"
      ],
      "env": {
        "MCP_TOOL_MODE": "condensed",
        "AUDIENCE": "https://app.leanix.net",
        "DELEGATED_SCOPES": "api",
        "GRAPHQLTOOL": "True",
        "LEANIX_AGENT_VERIFY": "True",
        "LEANIX_AI_INVENTORY_BUILDERTOOL": "True",
        "LEANIX_API_TOKEN": "your_leanix_api_token_here",
        "LEANIX_APPTIO_CONNECTORTOOL": "True",
        "LEANIX_AUTH_METHOD": "technical",
        "LEANIX_AUTOMATIONSTOOL": "True",
        "LEANIX_BROWSER_LOGIN": "False",
        "LEANIX_DISCOVERY_AI_AGENTSTOOL": "True",
        "LEANIX_DISCOVERY_LINKING_V1TOOL": "True",
        "LEANIX_DISCOVERY_LINKING_V2TOOL": "True",
        "LEANIX_DISCOVERY_SAASTOOL": "True",
        "LEANIX_DISCOVERY_SAPTOOL": "True",
        "LEANIX_DISCOVERY_SAP_EXTENSIONTOOL": "True",
        "LEANIX_DOCUMENTSTOOL": "True",
        "LEANIX_IMPACTSTOOL": "True",
        "LEANIX_INTEGRATION_APITOOL": "True",
        "LEANIX_INTEGRATION_COLLIBRATOOL": "True",
        "LEANIX_INTEGRATION_SERVICENOWTOOL": "True",
        "LEANIX_INTEGRATION_SIGNAVIOTOOL": "True",
        "LEANIX_INVENTORY_DATA_QUALITYTOOL": "True",
        "LEANIX_MANAGED_CODE_EXECUTIONTOOL": "True",
        "LEANIX_METRICSTOOL": "True",
        "LEANIX_MTMTOOL": "True",
        "LEANIX_NAVIGATIONTOOL": "True",
        "LEANIX_OAUTH_CLIENT_ID": "leanix-mcp",
        "LEANIX_OAUTH_REDIRECT_PORT": "56122",
        "LEANIX_OAUTH_SCOPE": "openid offline_access",
        "LEANIX_PATHFINDERTOOL": "True",
        "LEANIX_POLLTOOL": "True",
        "LEANIX_REFERENCE_DATATOOL": "True",
        "LEANIX_REFERENCE_DATA_CATALOGTOOL": "True",
        "LEANIX_STORAGETOOL": "True",
        "LEANIX_SURVEYTOOL": "True",
        "LEANIX_SYNCLOGTOOL": "True",
        "LEANIX_TECHNICAL_USER": "your_leanix_technical_user_here",
        "LEANIX_TECHNICAL_USER_PASSWORD": "your_leanix_technical_user_password_here",
        "LEANIX_TECHNOLOGY_DISCOVERYTOOL": "True",
        "LEANIX_TODOTOOL": "True",
        "LEANIX_TOKEN": "your_alternative_token_here",
        "LEANIX_TRANSFORMATIONSTOOL": "True",
        "LEANIX_WEBHOOKSTOOL": "True",
        "LEANIX_WORKSPACE": "https://app.leanix.net",
        "SSL_VERIFY": "True",
        "TESTING_FALLBACK": "False"
      }
    }
  }
}
```

#### Streamable-HTTP Transport (networked / production)

```json
{
  "mcpServers": {
    "leanix-mcp": {
      "command": "uvx",
      "args": [
        "--from",
        "leanix-agent[mcp]",
        "leanix-mcp",
        "--transport",
        "streamable-http",
        "--port",
        "8000"
      ],
      "env": {
        "TRANSPORT": "streamable-http",
        "HOST": "0.0.0.0",
        "PORT": "8000",
        "MCP_TOOL_MODE": "condensed",
        "AUDIENCE": "https://app.leanix.net",
        "DELEGATED_SCOPES": "api",
        "GRAPHQLTOOL": "True",
        "LEANIX_AGENT_VERIFY": "True",
        "LEANIX_AI_INVENTORY_BUILDERTOOL": "True",
        "LEANIX_API_TOKEN": "your_leanix_api_token_here",
        "LEANIX_APPTIO_CONNECTORTOOL": "True",
        "LEANIX_AUTH_METHOD": "technical",
        "LEANIX_AUTOMATIONSTOOL": "True",
        "LEANIX_BROWSER_LOGIN": "False",
        "LEANIX_DISCOVERY_AI_AGENTSTOOL": "True",
        "LEANIX_DISCOVERY_LINKING_V1TOOL": "True",
        "LEANIX_DISCOVERY_LINKING_V2TOOL": "True",
        "LEANIX_DISCOVERY_SAASTOOL": "True",
        "LEANIX_DISCOVERY_SAPTOOL": "True",
        "LEANIX_DISCOVERY_SAP_EXTENSIONTOOL": "True",
        "LEANIX_DOCUMENTSTOOL": "True",
        "LEANIX_IMPACTSTOOL": "True",
        "LEANIX_INTEGRATION_APITOOL": "True",
        "LEANIX_INTEGRATION_COLLIBRATOOL": "True",
        "LEANIX_INTEGRATION_SERVICENOWTOOL": "True",
        "LEANIX_INTEGRATION_SIGNAVIOTOOL": "True",
        "LEANIX_INVENTORY_DATA_QUALITYTOOL": "True",
        "LEANIX_MANAGED_CODE_EXECUTIONTOOL": "True",
        "LEANIX_METRICSTOOL": "True",
        "LEANIX_MTMTOOL": "True",
        "LEANIX_NAVIGATIONTOOL": "True",
        "LEANIX_OAUTH_CLIENT_ID": "leanix-mcp",
        "LEANIX_OAUTH_REDIRECT_PORT": "56122",
        "LEANIX_OAUTH_SCOPE": "openid offline_access",
        "LEANIX_PATHFINDERTOOL": "True",
        "LEANIX_POLLTOOL": "True",
        "LEANIX_REFERENCE_DATATOOL": "True",
        "LEANIX_REFERENCE_DATA_CATALOGTOOL": "True",
        "LEANIX_STORAGETOOL": "True",
        "LEANIX_SURVEYTOOL": "True",
        "LEANIX_SYNCLOGTOOL": "True",
        "LEANIX_TECHNICAL_USER": "your_leanix_technical_user_here",
        "LEANIX_TECHNICAL_USER_PASSWORD": "your_leanix_technical_user_password_here",
        "LEANIX_TECHNOLOGY_DISCOVERYTOOL": "True",
        "LEANIX_TODOTOOL": "True",
        "LEANIX_TOKEN": "your_alternative_token_here",
        "LEANIX_TRANSFORMATIONSTOOL": "True",
        "LEANIX_WEBHOOKSTOOL": "True",
        "LEANIX_WORKSPACE": "https://app.leanix.net",
        "SSL_VERIFY": "True",
        "TESTING_FALLBACK": "False"
      }
    }
  }
}
```

Alternatively, connect to a pre-deployed Streamable-HTTP instance by `url`:

```json
{
  "mcpServers": {
    "leanix-mcp": {
      "url": "http://localhost:8000/leanix-mcp/mcp"
    }
  }
}
```

Deploying the Streamable-HTTP server via Docker:

```bash
docker run -d \
  --name leanix-mcp-mcp \
  -p 8000:8000 \
  -e TRANSPORT=streamable-http \
  -e HOST=0.0.0.0 \
  -e PORT=8000 \
  -e MCP_TOOL_MODE=condensed \
  -e AUDIENCE=https://app.leanix.net \
  -e DELEGATED_SCOPES=api \
  -e GRAPHQLTOOL=True \
  -e LEANIX_AGENT_VERIFY=True \
  -e LEANIX_AI_INVENTORY_BUILDERTOOL=True \
  -e LEANIX_API_TOKEN=your_leanix_api_token_here \
  -e LEANIX_APPTIO_CONNECTORTOOL=True \
  -e LEANIX_AUTH_METHOD=technical \
  -e LEANIX_AUTOMATIONSTOOL=True \
  -e LEANIX_BROWSER_LOGIN=False \
  -e LEANIX_DISCOVERY_AI_AGENTSTOOL=True \
  -e LEANIX_DISCOVERY_LINKING_V1TOOL=True \
  -e LEANIX_DISCOVERY_LINKING_V2TOOL=True \
  -e LEANIX_DISCOVERY_SAASTOOL=True \
  -e LEANIX_DISCOVERY_SAPTOOL=True \
  -e LEANIX_DISCOVERY_SAP_EXTENSIONTOOL=True \
  -e LEANIX_DOCUMENTSTOOL=True \
  -e LEANIX_IMPACTSTOOL=True \
  -e LEANIX_INTEGRATION_APITOOL=True \
  -e LEANIX_INTEGRATION_COLLIBRATOOL=True \
  -e LEANIX_INTEGRATION_SERVICENOWTOOL=True \
  -e LEANIX_INTEGRATION_SIGNAVIOTOOL=True \
  -e LEANIX_INVENTORY_DATA_QUALITYTOOL=True \
  -e LEANIX_MANAGED_CODE_EXECUTIONTOOL=True \
  -e LEANIX_METRICSTOOL=True \
  -e LEANIX_MTMTOOL=True \
  -e LEANIX_NAVIGATIONTOOL=True \
  -e LEANIX_OAUTH_CLIENT_ID=leanix-mcp \
  -e LEANIX_OAUTH_REDIRECT_PORT=56122 \
  -e LEANIX_OAUTH_SCOPE="openid offline_access" \
  -e LEANIX_PATHFINDERTOOL=True \
  -e LEANIX_POLLTOOL=True \
  -e LEANIX_REFERENCE_DATATOOL=True \
  -e LEANIX_REFERENCE_DATA_CATALOGTOOL=True \
  -e LEANIX_STORAGETOOL=True \
  -e LEANIX_SURVEYTOOL=True \
  -e LEANIX_SYNCLOGTOOL=True \
  -e LEANIX_TECHNICAL_USER=your_leanix_technical_user_here \
  -e LEANIX_TECHNICAL_USER_PASSWORD=your_leanix_technical_user_password_here \
  -e LEANIX_TECHNOLOGY_DISCOVERYTOOL=True \
  -e LEANIX_TODOTOOL=True \
  -e LEANIX_TOKEN=your_alternative_token_here \
  -e LEANIX_TRANSFORMATIONSTOOL=True \
  -e LEANIX_WEBHOOKSTOOL=True \
  -e LEANIX_WORKSPACE=https://app.leanix.net \
  -e SSL_VERIFY=True \
  -e TESTING_FALLBACK=False \
  knucklessg1/leanix-agent:mcp
```

_Auto-generated from the code-read env surface (`MCP_TOOL_MODE` + package vars) — do not edit._
<!-- MCP-CONFIG-EXAMPLES:END -->

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
    image: knucklessg1/leanix-agent:mcp
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

## Environment Variables

<!-- ENV-VARS-TABLE:START -->

#### Package environment variables

| Variable | Example | Description |
|----------|---------|-------------|
| `HOST` | `0.0.0.0` |  |
| `PORT` | `8000` |  |
| `TRANSPORT` | `stdio` | options: stdio, streamable-http, sse |
| `ENABLE_OTEL` | `True` |  |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `http://localhost:8080/api/public/otel` |  |
| `OTEL_EXPORTER_OTLP_PUBLIC_KEY` | `pk-...` |  |
| `OTEL_EXPORTER_OTLP_SECRET_KEY` | `sk-...` |  |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | `http/protobuf` |  |
| `EUNOMIA_TYPE` | `none` | options: none, embedded, remote |
| `EUNOMIA_POLICY_FILE` | `mcp_policies.json` |  |
| `EUNOMIA_REMOTE_URL` | `http://eunomia-server:8000` |  |
| `LEANIX_WORKSPACE` | `https://app.leanix.net` | Base URL or specific workspace URL |
| `LEANIX_AUTH_METHOD` | `technical` | Options: technical, browser, token, api_token |
| `LEANIX_TECHNICAL_USER` | `your_leanix_technical_user_here` | Technical user client ID |
| `LEANIX_TECHNICAL_USER_PASSWORD` | `your_leanix_technical_user_password_here` | Technical user password/secret |
| `LEANIX_API_TOKEN` | `your_leanix_api_token_here` | Alternative static API token |
| `LEANIX_TOKEN` | `your_alternative_token_here` | Generic fallback token |
| `LEANIX_BROWSER_LOGIN` | `False` | Force browser interactive OAuth SSO fallback |
| `LEANIX_OAUTH_CLIENT_ID` | `leanix-mcp` | OAuth Application Client ID |
| `LEANIX_OAUTH_SCOPE` | `openid offline_access` | Standard OAuth Scopes |
| `LEANIX_OAUTH_REDIRECT_PORT` | `56122` | Local port to receive auth code callback |
| `AUDIENCE` | `https://app.leanix.net` | Audience URI for delegation |
| `DELEGATED_SCOPES` | `api` | Requested scopes for token exchange |
| `SSL_VERIFY` | `True` | Toggle standard SSL certificate verification |
| `LEANIX_AGENT_VERIFY` | `True` | Strict alternate agent validation switch |
| `LEANIX_SSL_VERIFY` | `True` | LeanIX-specific SSL verification override |
| `DEFAULT_AGENT_NAME` | `LeanIX Agent` | Customized name for downstream LLMs |
| `AGENT_DESCRIPTION` | `Enterprise Architecture Agent` | Customized agent description |
| `AGENT_SYSTEM_PROMPT` | `Act as an EA expert...` | Customized agent prompt template |
| `TESTING_FALLBACK` | `False` | Fallback testing switch for browser authentication |
| `LEANIX_AI_INVENTORY_BUILDERTOOL` | `True` |  |
| `LEANIX_APPTIO_CONNECTORTOOL` | `True` |  |
| `LEANIX_AUTOMATIONSTOOL` | `True` |  |
| `LEANIX_REFERENCE_DATA_CATALOGTOOL` | `True` |  |
| `LEANIX_DISCOVERY_AI_AGENTSTOOL` | `True` |  |
| `LEANIX_DISCOVERY_LINKING_V1TOOL` | `True` |  |
| `LEANIX_DISCOVERY_LINKING_V2TOOL` | `True` |  |
| `LEANIX_DISCOVERY_SAP_EXTENSIONTOOL` | `True` |  |
| `LEANIX_DISCOVERY_SAASTOOL` | `True` |  |
| `LEANIX_DOCUMENTSTOOL` | `True` |  |
| `LEANIX_IMPACTSTOOL` | `True` |  |
| `LEANIX_INTEGRATION_APITOOL` | `True` |  |
| `LEANIX_INTEGRATION_COLLIBRATOOL` | `True` |  |
| `LEANIX_INTEGRATION_SERVICENOWTOOL` | `True` |  |
| `LEANIX_INTEGRATION_SIGNAVIOTOOL` | `True` |  |
| `LEANIX_INVENTORY_DATA_QUALITYTOOL` | `True` |  |
| `LEANIX_MTMTOOL` | `True` |  |
| `LEANIX_MANAGED_CODE_EXECUTIONTOOL` | `True` |  |
| `LEANIX_METRICSTOOL` | `True` |  |
| `LEANIX_NAVIGATIONTOOL` | `True` |  |
| `LEANIX_PATHFINDERTOOL` | `True` |  |
| `LEANIX_POLLTOOL` | `True` |  |
| `LEANIX_REFERENCE_DATATOOL` | `True` |  |
| `LEANIX_DISCOVERY_SAPTOOL` | `True` |  |
| `LEANIX_TECHNOLOGY_DISCOVERYTOOL` | `True` |  |
| `LEANIX_STORAGETOOL` | `True` |  |
| `LEANIX_SURVEYTOOL` | `True` |  |
| `LEANIX_SYNCLOGTOOL` | `True` |  |
| `LEANIX_TODOTOOL` | `True` |  |
| `LEANIX_TRANSFORMATIONSTOOL` | `True` |  |
| `LEANIX_WEBHOOKSTOOL` | `True` |  |
| `GRAPHQLTOOL` | `True` |  |

#### Inherited agent-utilities variables (apply to every connector)

| Variable | Example | Description |
|----------|---------|-------------|
| `MCP_TOOL_MODE` | `condensed` | Tool surface: `condensed` | `verbose` | `both` |
| `MCP_ENABLED_TOOLS` | — | Comma-separated tool allow-list |
| `MCP_DISABLED_TOOLS` | — | Comma-separated tool deny-list |
| `MCP_ENABLED_TAGS` | — | Comma-separated tag allow-list |
| `MCP_DISABLED_TAGS` | — | Comma-separated tag deny-list |
| `MCP_CLIENT_AUTH` | — | Outbound MCP auth (`oidc-client-credentials` for fleet calls) |
| `OIDC_CLIENT_ID` | — | OIDC client id (service-account auth) |
| `OIDC_CLIENT_SECRET` | — | OIDC client secret (service-account auth) |
| `DEBUG` | `False` | Verbose logging |
| `PYTHONUNBUFFERED` | `1` | Unbuffered stdout (recommended in containers) |
| `MCP_URL` | `http://localhost:8000/mcp` | URL of the MCP server the agent connects to |
| `PROVIDER` | `openai` | LLM provider for the agent |
| `MODEL_ID` | `gpt-4o` | Model id for the agent |
| `ENABLE_WEB_UI` | `True` | Serve the AG-UI web interface |

_62 package + 14 inherited variable(s). Auto-generated from `.env.example` + the shared agent-utilities set — do not edit._
<!-- ENV-VARS-TABLE:END -->


Every variable the server reads. Copy [`.env.example`](.env.example) to `.env` and populate
only what you use; blank connector credentials leave the corresponding surface inactive.

### Connection & credentials
| Variable | Description | Default |
|----------|-------------|---------|
| `LEANIX_WORKSPACE` | Base URL or specific workspace URL | `https://app.leanix.net` |
| `LEANIX_AUTH_METHOD` | Auth method: `technical`, `browser`, `token`, `api_token` | `technical` |
| `LEANIX_TECHNICAL_USER` | Technical user client id | — |
| `LEANIX_TECHNICAL_USER_PASSWORD` | Technical user password / secret | — |
| `LEANIX_API_TOKEN` | Static API token | — |
| `LEANIX_TOKEN` | Generic fallback token | — |
| `LEANIX_BROWSER_LOGIN` | Force browser interactive OAuth SSO fallback | `False` |
| `SSL_VERIFY` | Toggle standard SSL certificate verification | `True` |
| `LEANIX_AGENT_VERIFY` | Strict alternate agent validation switch | `True` |

### SSO / OAuth (SSO path)
| Variable | Description | Default |
|----------|-------------|---------|
| `LEANIX_OAUTH_CLIENT_ID` | OAuth application client id | `leanix-mcp` |
| `LEANIX_OAUTH_SCOPE` | Standard OAuth scopes | `openid offline_access` |
| `LEANIX_OAUTH_REDIRECT_PORT` | Local port to receive the auth-code callback | `56122` |

### OIDC token delegation (RFC 8693)
| Variable | Description | Default |
|----------|-------------|---------|
| `AUDIENCE` | Audience URI for delegation | `https://app.leanix.net` |
| `DELEGATED_SCOPES` | Requested scopes for token exchange | `api` |

### MCP server / transport
| Variable | Description | Default |
|----------|-------------|---------|
| `TRANSPORT` | `stdio`, `streamable-http`, or `sse` | `stdio` |
| `HOST` | Bind host (HTTP transports) | `0.0.0.0` |
| `PORT` | Bind port (HTTP transports) | `8000` |
| `MCP_TOOL_MODE` | Tool surface: `condensed`, `verbose`, or `both` | `condensed` |
| `DEBUG` | Verbose logging | `False` |
| `PYTHONUNBUFFERED` | Unbuffered stdout (recommended in containers) | `1` |

### Agent identity (full `[agent]` runtime only)
| Variable | Description | Default |
|----------|-------------|---------|
| `DEFAULT_AGENT_NAME` | Custom name for downstream LLMs | `LeanIX Agent` |
| `DEFAULT_AGENT_DESCRIPTION` | Custom agent description | `Enterprise Architecture Agent` |
| `DEFAULT_AGENT_SYSTEM_PROMPT` | Custom agent prompt template | — |

### Telemetry & governance
| Variable | Description | Default |
|----------|-------------|---------|
| `ENABLE_OTEL` | Enable OpenTelemetry export | `True` |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | OTLP collector endpoint | — |
| `OTEL_EXPORTER_OTLP_PUBLIC_KEY` / `OTEL_EXPORTER_OTLP_SECRET_KEY` | OTLP auth keys | — |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | OTLP protocol (e.g. `http/protobuf`) | — |
| `EUNOMIA_TYPE` | Authorization mode: `none`, `embedded`, `remote` | `none` |
| `EUNOMIA_POLICY_FILE` | Embedded policy file | `mcp_policies.json` |
| `EUNOMIA_REMOTE_URL` | Remote Eunomia server URL | — |

### Tool toggles
Each action-routed tool can be disabled individually via its toggle env var (set to `false`).
The full list is in the [Available MCP Tools](#available-mcp-tools) table above
(e.g. `LEANIX_DOCUMENTSTOOL`, `LEANIX_NAVIGATIONTOOL`, `GRAPHQLTOOL`).

---

## Installation

Pick the extra that matches what you want to run:

| Extra | Installs | Use when |
|-------|----------|----------|
| `leanix-agent[mcp]` | Slim MCP server only (`agent-utilities[mcp]` — FastMCP/FastAPI) | You only run the **MCP server** (smallest install / image) |
| `leanix-agent[agent]` | Full agent runtime (`agent-utilities[agent,logfire]` — Pydantic AI + the epistemic-graph engine) | You run the **integrated agent** |
| `leanix-agent[gql]` | GraphQL client dependency (`gql`) | You use the native GraphQL tool |
| `leanix-agent[all]` | Everything (`mcp` + `agent` + `gql` + `logfire`) | Development / both surfaces |

```bash
# MCP server only (recommended for tool hosting — slim deps)
uv pip install "leanix-agent[mcp]"

# Full agent runtime (Pydantic AI + epistemic-graph engine)
uv pip install "leanix-agent[agent]"

# Everything (development)
uv pip install "leanix-agent[all]"      # or: python -m pip install "leanix-agent[all]"
```

### Container images (`:mcp` vs `:agent`)

One multi-stage `docker/Dockerfile` builds two right-sized images, selected by `--target`:

| Image tag | Build target | Contents | Entrypoint |
|-----------|--------------|----------|------------|
| `knucklessg1/leanix-agent:mcp` | `--target mcp` | `leanix-agent[mcp]` — **slim**, no engine/`pydantic-ai`/`dspy`/`llama-index`/`tree-sitter` | `leanix-mcp` |
| `knucklessg1/leanix-agent:latest` | `--target agent` (default) | `leanix-agent[agent]` — **full** agent runtime + epistemic-graph engine | `leanix-agent` |

```bash
docker build --target mcp   -t knucklessg1/leanix-agent:mcp    docker/   # slim MCP server
docker build --target agent -t knucklessg1/leanix-agent:latest docker/   # full agent
```

### Knowledge-graph database (`epistemic-graph`)

The **full agent** (`[agent]` / `:latest`) embeds the **epistemic-graph** engine (pulled in
transitively via `agent-utilities[agent]`). For production — or to share one knowledge graph
across multiple agents — run **epistemic-graph as its own database container** and point the
agent at it instead of embedding it. Deployment recipes (single-node + Raft HA), connection
config, and the full database architecture (with diagrams) are documented in the
[epistemic-graph deployment guide](https://knuckles-team.github.io/epistemic-graph/deployment/).
The slim `[mcp]` server does **not** require the database.

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
