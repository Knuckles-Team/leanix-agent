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

*Version: 2.0.0*

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

**LeanIX Agent** is a production-grade Agent and Model Context Protocol (MCP)
provider for SAP LeanIX Enterprise Architecture Management REST and GraphQL APIs.

---

## Key Features

- **Consolidated Action-Routed MCP Tools:** Minimizes token overhead and eliminates tool bloat in LLM contexts by grouping methods into optimized, togglable tool modules.
- **Enterprise-Grade Security:** Comprehensive support for Eunomia policies, OIDC token delegation, and granular execution context tracking.
- **Integrated Graph Agent:** Built-in Pydantic AI agent supporting the Agent Control Protocol (ACP) and standard Web interfaces (AG-UI).
- **Optional Telemetry:** OTLP and Logfire instrumentation activate only when their runtime configuration is present.
- **Live Instance Ontology:** Compiles the configured workspace data model into deterministic OWL, SHACL, and SKOS without checking in tenant schemas.
- **Governed Graph Sync:** Streams privacy-sanitized FactSheets through atomic ChangeEnvelope commits under the caller's verified graph session.

---

## CLI or API

The package exposes workspace-scoped LeanIX REST and GraphQL capabilities through
its Python API, MCP provider, and optional A2A agent entry point.

Detailed instructions on how to use the underlying API wrappers, extended schema bindings, and developer SDK references are maintained in [docs/index.md](docs/index.md).

---

## MCP

This server utilizes dynamic Action-Routed tools to optimize token overhead and maximize IDE compatibility.

The comprehensive surface includes bounded universal REST, GraphQL schema
fingerprinting and multipart upload, live metamodel compilation, and full,
delta, or reconcile graph synchronization. Every REST or GraphQL mutation
requires explicit consent on that individual tool call.

An optional `leanix-official` GraphOS child policy can federate a hosted MCP
service from a runtime-selected `AgentConfig.provider_configs` profile. The
package contains no endpoint, credentials, trust path, executable, or default
profile; the child remains read-only and verifies its preinstalled helper before
spawn. See [Hosted MCP federation](docs/hosted_mcp_federation.md).

### Available MCP Tools
Auto-generated — do not edit between the markers below.
<!-- MCP-TOOLS-TABLE:START -->

#### Condensed action-routed tools (`MCP_TOOL_MODE=condensed`)

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `leanix_discover_meta_model` | `LEANIX_PATHFINDERTOOL` | Discover the custom LeanIX meta-model/data-model schema including custom attributes and fields in real-time. |
| `leanix_generate_instance_ontology` | `INSTANCE_GRAPHTOOL` | Compile the current live data model to deterministic OWL, SHACL, and SKOS. |
| `leanix_graphql` | `GRAPHQLTOOL` | Execute a bounded GraphQL document with mutation consent. |
| `leanix_graphql_schema` | `GRAPHQLTOOL` | Introspect and fingerprint the current workspace schema. |
| `leanix_graphql_upload` | `GRAPHQLTOOL` | Execute a bounded GraphQL multipart upload through configured TLS. |
| `leanix_ingest_factsheets` | `LEANIX_KG_INGESTTOOL` | Natively ingest LeanIX FactSheets into epistemic-graph as typed nodes. |
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
| `leanix_rest_api` | `UNIVERSAL_APITOOL` | Invoke a workspace-scoped LeanIX operation with mutation consent. |
| `leanix_source_factsheets` | `LEANIX_KG_INGESTTOOL` | Return FactSheets for governed ChangeEnvelope materialization. |
| `leanix_sync_instance_to_graph` | `INSTANCE_GRAPHTOOL` | Load the generated ontology and stream records through ChangeEnvelope. |

#### Verbose 1:1 API-mapped tools (`MCP_TOOL_MODE=verbose` or `both`)

<details>
<summary>3 per-operation tools — one per public API method (click to expand)</summary>

| MCP Tool | Toggle Env Var | Description |
|----------|----------------|-------------|
| `leanix_get_factsheet` | `LEANIX_APITOOL` | Get a specific FactSheet by ID. |
| `leanix_get_factsheets` | `LEANIX_APITOOL` | Get a list of FactSheets. |
| `leanix_request_api` | `LEANIX_APITOOL` | Call a workspace API without permitting cross-host requests. |

</details>

_40 action-routed tool(s) · 3 verbose 1:1 tool(s). Each is enabled unless its `<DOMAIN>TOOL` toggle is set false; `MCP_TOOL_MODE` selects the surface (**`intent` default** — the six verb-tools, granular set loaded on demand · `condensed` action-routed · `verbose` 1:1 · `both`). Auto-generated — do not edit._
<!-- MCP-TOOLS-TABLE:END -->

Detailed tool schemas, parameter shapes, and validation constraints are documented in
[Usage](docs/usage.md).

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

> **Install the connector-focused `[mcp]` extra.** Examples use `leanix-agent[mcp]` to add
> FastMCP / FastAPI through `agent-utilities[mcp]`; the required Agent Utilities core
> still carries `epistemic-graph[full]`. The `[agent-runtime]` extra additionally
> enables model orchestration.

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
        "MCP_TOOL_MODE": "intent",
        "AUDIENCE": "https://app.leanix.net",
        "DELEGATED_SCOPES": "api",
        "GRAPHQLTOOL": "True",
        "INSTANCE_GRAPHTOOL": "True",
        "LEANIX_AI_INVENTORY_BUILDERTOOL": "True",
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
        "LEANIX_KG_INGESTTOOL": "True",
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
        "LEANIX_TECHNOLOGY_DISCOVERYTOOL": "True",
        "LEANIX_TODOTOOL": "True",
        "LEANIX_TRANSFORMATIONSTOOL": "True",
        "LEANIX_WEBHOOKSTOOL": "True",
        "LEANIX_WORKSPACE": "https://app.leanix.net",
        "TESTING_FALLBACK": "False",
        "UNIVERSAL_APITOOL": "True"
      }
    }
  }
}
```

Runtime references require an alias-aware launcher such as GraphOS. Other
launchers must omit those entries and inject the resolved values through their
own runtime secret boundary.

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
        "HOST": "127.0.0.1",
        "PORT": "8000",
        "MCP_TOOL_MODE": "intent",
        "AUDIENCE": "https://app.leanix.net",
        "DELEGATED_SCOPES": "api",
        "GRAPHQLTOOL": "True",
        "INSTANCE_GRAPHTOOL": "True",
        "LEANIX_AI_INVENTORY_BUILDERTOOL": "True",
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
        "LEANIX_KG_INGESTTOOL": "True",
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
        "LEANIX_TECHNOLOGY_DISCOVERYTOOL": "True",
        "LEANIX_TODOTOOL": "True",
        "LEANIX_TRANSFORMATIONSTOOL": "True",
        "LEANIX_WEBHOOKSTOOL": "True",
        "LEANIX_WORKSPACE": "https://app.leanix.net",
        "TESTING_FALLBACK": "False",
        "UNIVERSAL_APITOOL": "True"
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

Run a reviewed container image as a least-privilege stdio child (no
listener or published port):

```bash
docker run -i --rm \
  --read-only \
  --cap-drop=ALL \
  --security-opt=no-new-privileges \
  --pids-limit=256 \
  --tmpfs /tmp:rw,noexec,nosuid,nodev,size=64m \
  -e TRANSPORT=stdio \
  -e MCP_TOOL_MODE=intent \
  -e AUDIENCE=https://app.leanix.net \
  -e DELEGATED_SCOPES=api \
  -e GRAPHQLTOOL=True \
  -e INSTANCE_GRAPHTOOL=True \
  -e LEANIX_AI_INVENTORY_BUILDERTOOL=True \
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
  -e LEANIX_KG_INGESTTOOL=True \
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
  -e LEANIX_TECHNOLOGY_DISCOVERYTOOL=True \
  -e LEANIX_TODOTOOL=True \
  -e LEANIX_TRANSFORMATIONSTOOL=True \
  -e LEANIX_WEBHOOKSTOOL=True \
  -e LEANIX_WORKSPACE=https://app.leanix.net \
  -e TESTING_FALLBACK=False \
  -e UNIVERSAL_APITOOL=True \
  registry.example.invalid/leanix-agent@sha256:<digest> leanix-mcp
```

For containerized network HTTP, supply an authenticated TLS ingress (or
direct server TLS), exact `MCP_ALLOWED_HOSTS`, and an exact trusted-proxy
CIDR policy through the operator-owned deployment profile. The generator
does not emit an unauthenticated non-loopback listener.

_Auto-generated from the code-read env surface (`MCP_TOOL_MODE` + package vars) — do not edit._
<!-- MCP-CONFIG-EXAMPLES:END -->

<!-- BEGIN GENERATED: additional-deployment-options -->
### Additional Deployment Options

`leanix-agent` can run as a local stdio process or container, or behind a remote
network boundary. The
[Deployment guide](https://knuckles-team.github.io/leanix-agent/deployment/) carries
the detailed transport contract.

- **Local container** — launch a reviewed immutable image as a least-privilege
  stdio child with no listener or published port.
- **Remote URL** — connect through an operator-supplied authenticated HTTPS
  ingress. Keep its URL, outbound identity references, trust profile, and exact
  `MCP_ALLOWED_HOSTS` in `AgentConfig`.
<!-- END GENERATED: additional-deployment-options -->

## Agent

This repository features a fully integrated Pydantic AI Graph Agent. It communicates over the **Agent Control Protocol (ACP)** and interacts seamlessly with the **Agent Web UI (AG-UI)** and Terminal interface.

### Running the Agent CLI
To start the interactive command-line agent:

```bash
# Set credentials
export LEANIX_WORKSPACE="your_value"
export LEANIX_API_TOKEN="your_value"
export TLS_PROFILE_REF="secret://transport/leanix"
export DEBUG="your_value"
export PYTHONUNBUFFERED="your_value"
export LEANIX_TOKEN="your_value"

# Run the agent server
leanix-agent --provider openai --model-id gpt-4o
```

### Docker Compose Orchestration
The checked-in `docker/agent.compose.yml` starts the MCP and agent services with
fixed non-root identities, read-only root filesystems, dropped capabilities,
bounded resources, loopback-only published ports, and `no-new-privileges`. It
deliberately has no mutable image or model defaults. Supply immutable image
digests and the operator-selected model through the environment:

```bash
export LEANIX_AGENT_MCP_IMAGE='registry.example.invalid/leanix-agent@sha256:<digest>'
export LEANIX_AGENT_AGENT_IMAGE='registry.example.invalid/leanix-agent@sha256:<digest>'
export PROVIDER='<configured-provider>'
export MODEL_ID='<configured-model>'
docker compose -f docker/agent.compose.yml up -d
```

Agent, graph-sync, and deployment behavior is documented in
[Deployment](docs/deployment.md) and [Usage](docs/usage.md).

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
| `HOST` | `127.0.0.1` |  |
| `PORT` | `8000` |  |
| `TRANSPORT` | `stdio` | options: stdio, streamable-http, sse |
| `MCP_TOOL_MODE` | `intent` | options: intent, condensed, verbose, both |
| `PROVIDER` | `<configured-provider>` |  |
| `MODEL_ID` | `<configured-model>` |  |
| `ENABLE_OTEL` | `False` |  |
| `OTEL_EXPORTER_OTLP_ENDPOINT` | `https://otel.example.invalid` |  |
| `OTEL_EXPORTER_OTLP_PUBLIC_KEY_REF` | `secret://observability/otel-public-key` |  |
| `OTEL_EXPORTER_OTLP_SECRET_KEY_REF` | `secret://observability/otel-secret-key` |  |
| `OTEL_EXPORTER_OTLP_PROTOCOL` | `http/protobuf` |  |
| `EUNOMIA_TYPE` | `none` | options: none, embedded, remote |
| `EUNOMIA_POLICY_FILE` | `mcp_policies.json` |  |
| `EUNOMIA_REMOTE_URL` | `http://eunomia-server:8000` |  |
| `LEANIX_WORKSPACE` | `https://app.leanix.net` | Base URL or specific workspace URL |
| `LEANIX_AUTH_METHOD` | `technical` | Options: technical, browser, token, api_token |
| `LEANIX_TECHNICAL_USER` | — | Technical user client ID; inject at runtime |
| `LEANIX_TECHNICAL_USER_PASSWORD` | secret-injected | Technical user secret; inject at runtime |
| `LEANIX_API_TOKEN` | secret-injected | Alternative static API token; inject at runtime |
| `LEANIX_TOKEN` | secret-injected | Generic fallback token; inject at runtime |
| `LEANIX_BROWSER_LOGIN` | `False` | Force browser interactive OAuth SSO fallback |
| `LEANIX_OAUTH_CLIENT_ID` | `leanix-mcp` | OAuth Application Client ID |
| `LEANIX_OAUTH_SCOPE` | `openid offline_access` | Standard OAuth Scopes |
| `LEANIX_OAUTH_REDIRECT_PORT` | `56122` | Local port to receive auth code callback |
| `AUDIENCE` | `https://app.leanix.net` | Audience URI for delegation |
| `DELEGATED_SCOPES` | `api` | Requested scopes for token exchange |
| `TLS_PROFILE` | `leanix` | Named profile selected from the runtime catalog |
| `TLS_PROFILES_REF` | `secret://transport/tls-profiles` | Runtime profile catalog |
| `TLS_PROFILE_REF` | `secret://transport/leanix` | Direct profile reference; use instead of TLS_PROFILE |
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
| `LEANIX_KG_INGESTTOOL` | `True` |  |
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
| `INSTANCE_GRAPHTOOL` | `True` |  |
| `UNIVERSAL_APITOOL` | `True` |  |

#### Inherited agent-utilities variables (apply to every connector)

| Variable | Example | Description |
|----------|---------|-------------|
| `MCP_ENABLED_TOOLS` | — | Comma-separated tool allow-list |
| `MCP_DISABLED_TOOLS` | — | Comma-separated tool deny-list |
| `MCP_ENABLED_TAGS` | — | Comma-separated tag allow-list |
| `MCP_DISABLED_TAGS` | — | Comma-separated tag deny-list |
| `MCP_CLIENT_AUTH` | — | Outbound MCP child auth: `oidc-client-credentials` \| `basic` \| `none` |
| `OIDC_CLIENT_ID` | — | OIDC client id (service-account auth) |
| `OIDC_CLIENT_SECRET_REF` | `secret://identity/oidc-client-secret` | Runtime secret reference for the OIDC service account |
| `MCP_BASIC_AUTH_USERNAME` | — | HTTP Basic username (`MCP_CLIENT_AUTH=basic`) |
| `MCP_BASIC_AUTH_PASSWORD_REF` | `secret://identity/mcp-basic-password` | Runtime secret reference for HTTP Basic auth (`MCP_CLIENT_AUTH=basic`) |
| `DEBUG` | `False` | Verbose logging |
| `PYTHONUNBUFFERED` | `1` | Unbuffered stdout (recommended in containers) |
| `MCP_URL` | `http://localhost:8000/mcp` | URL of the MCP server the agent connects to |
| `ENABLE_WEB_UI` | `True` | Serve the AG-UI web interface |

_68 package + 13 inherited variable(s). Auto-generated from `.env.example` + the shared agent-utilities set — do not edit._
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
| `TLS_PROFILE` | Named runtime TLS profile selected through `AgentConfig` | — |
| `TLS_PROFILE_REF` | Direct secret reference containing a runtime TLS profile | — |
| `TLS_PROFILES_REF` | Secret reference containing the named profile catalog | — |

Certificate and hostname verification are mandatory. Runtime TLS profiles can add
private trust anchors, mTLS client material, proxy policy, and standard-environment
integration without storing certificate material or machine paths in this package.

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
| `HOST` | Bind host (HTTP transports) | `127.0.0.1` |
| `PORT` | Bind port (HTTP transports) | `8000` |
| `MCP_TOOL_MODE` | Tool surface: `intent`, `condensed`, `verbose`, or `both` | `intent` |
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
| `ENABLE_OTEL` | Enable OpenTelemetry export | `False` |
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
| `leanix-agent[mcp]` | MCP server stack (`agent-utilities[mcp,owl]`, including the shared `epistemic-graph[full]` core) | You run the **MCP server** without model orchestration |
| `leanix-agent[agent]` | Model orchestration and observability (`agent-utilities[agent-runtime,logfire]`) | You run the **integrated agent** |
| `leanix-agent[gql]` | GraphQL client dependency (`gql`) | You use the native GraphQL tool |
| `leanix-agent[all]` | MCP, model orchestration, observability, OWL, and GraphQL | Development / both surfaces |

```bash
# MCP server without model orchestration
uv pip install "leanix-agent[mcp]"

# Full agent runtime (Pydantic AI + epistemic-graph engine)
uv pip install "leanix-agent[agent]"

# Everything (development)
uv pip install "leanix-agent[all]"      # or: python -m pip install "leanix-agent[all]"
```

### Container image targets

One multi-stage `docker/Dockerfile` builds two runtime surfaces, selected by `--target`:

| Build target | Contents | Entrypoint |
|--------------|----------|------------|
| `mcp` | MCP runtime plus the shared Agent Utilities and `epistemic-graph[full]` core | `leanix-mcp` |
| `agent` (default) | MCP runtime plus model orchestration and observability | `leanix-agent` |

```bash
docker build --target mcp   -t leanix-agent:mcp-local   docker/
docker build --target agent -t leanix-agent:agent-local docker/
```

Promote and deploy only an operator-reviewed immutable image digest.

### Knowledge-graph database (`epistemic-graph`)

Every install carries the **`epistemic-graph[full]`** core through Agent Utilities. Select
an embedded or remote engine through `AgentConfig`; an MCP-only deployment can connect to
a shared GraphOS service without autostarting another local engine. Deployment recipes
(single-node + Raft HA), connection config, and the full database architecture are documented in the
[epistemic-graph deployment guide](https://knuckles-team.github.io/epistemic-graph/deployment/).

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

## Contribute

Contributions are welcome! Please ensure code quality by executing local checks before submitting pull requests:
- Format code using `ruff format .`
- Lint code using `ruff check .`
- Validate type-safety with `mypy .`
- Execute test suites using `pytest`


<!-- BEGIN agent-utilities-deployment (generated; do not edit between markers) -->

## Deploy with `agent-utilities-deployment`

Provision this package with the consolidated **`agent-utilities-deployment`**
workflow. It selects an installed-package, editable-source, or immutable-container
path; records only runtime secret and TLS-profile references in `AgentConfig`; and
runs doctor, registration, policy, observability, and rollback gates. Ask your agent
to **"deploy `leanix-agent` with agent-utilities-deployment"**.

| Install mode | Command |
|------|---------|
| Installed package | `uv tool install "leanix-agent[mcp]"`, then run `leanix-mcp` |
| Editable source | `uv pip install -e ".[agent]"`, then run `leanix-mcp` |
| Immutable container | deploy `registry.example.invalid/leanix-agent@sha256:<digest>` through the operator-selected orchestrator |

The repository embeds no deployment profile, credential value, certificate path, or
environment-specific endpoint. Supply those at runtime through `AgentConfig` and the
configured secret provider.

<!-- END agent-utilities-deployment -->

<!-- GOVERNED-CAPABILITY:START -->
## Governed capability contract

This package ships a compact canonical skill surface with specialist procedures
kept as referenced workflows. The current MCP tools, skill metadata,
`connector_manifest.yml`, ontology, mappings, shapes, fixtures, migrations,
tool-schema fingerprints, and certification metadata form one versioned
capability contract. Validate them together; do not rely on stale tool names or
historical per-task skill wrappers.

Runtime endpoints, credentials, certificate trust, tenant identity, retention,
and observability policy are deployment inputs and are never packaged values.
See [Configuration, trust, and privacy](docs/configuration.md) before enabling a
network transport, connector ingestion, GraphOS delegation, or trace export.
<!-- GOVERNED-CAPABILITY:END -->
