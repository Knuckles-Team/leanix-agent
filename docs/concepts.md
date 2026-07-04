# Concept Registry — leanix-agent

> **Prefix**: `CONCEPT:LIX-*`
> **Version**: 0.14.0
> **Bridge**: [`CONCEPT:AU-ECO.messaging.native-backend-abstraction`](https://knuckles-team.github.io/agent-utilities/) (Unified Toolkit Ingestion)

---

## Project-Specific Concepts

| Concept ID | Name | Description |
|------------|------|-------------|
| `CONCEPT:LX-OS.governance.lix` | Graphql Operations | MCP tool domain `graphql` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-2` | Leanix Ai Inventory Builder Operations | MCP tool domain `leanix_ai_inventory_builder` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-3` | Leanix Apptio Connector Operations | MCP tool domain `leanix_apptio_connector` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-4` | Leanix Automations Operations | MCP tool domain `leanix_automations` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-5` | Leanix Discovery Ai Agents Operations | MCP tool domain `leanix_discovery_ai_agents` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-6` | Leanix Discovery Linking V1 Operations | MCP tool domain `leanix_discovery_linking_v1` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-7` | Leanix Discovery Linking V2 Operations | MCP tool domain `leanix_discovery_linking_v2` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-8` | Leanix Discovery Saas Operations | MCP tool domain `leanix_discovery_saas` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-9` | Leanix Discovery Sap Operations | MCP tool domain `leanix_discovery_sap` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-10` | Leanix Discovery Sap Extension Operations | MCP tool domain `leanix_discovery_sap_extension` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-11` | Leanix Documents Operations | MCP tool domain `leanix_documents` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-12` | Leanix Impacts Operations | MCP tool domain `leanix_impacts` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-13` | Leanix Integration Api Operations | MCP tool domain `leanix_integration_api` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-14` | Leanix Integration Collibra Operations | MCP tool domain `leanix_integration_collibra` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-15` | Leanix Integration Servicenow Operations | MCP tool domain `leanix_integration_servicenow` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-16` | Leanix Integration Signavio Operations | MCP tool domain `leanix_integration_signavio` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-17` | Leanix Inventory Data Quality Operations | MCP tool domain `leanix_inventory_data_quality` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-18` | Leanix Managed Code Execution Operations | MCP tool domain `leanix_managed_code_execution` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-19` | Leanix Metrics Operations | MCP tool domain `leanix_metrics` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-20` | Leanix Mtm Operations | MCP tool domain `leanix_mtm` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-21` | Leanix Navigation Operations | MCP tool domain `leanix_navigation` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-22` | Leanix Pathfinder Operations | MCP tool domain `leanix_pathfinder` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-23` | Leanix Poll Operations | MCP tool domain `leanix_poll` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-24` | Leanix Reference Data Operations | MCP tool domain `leanix_reference_data` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-25` | Leanix Reference Data Catalog Operations | MCP tool domain `leanix_reference_data_catalog` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-26` | Leanix Storage Operations | MCP tool domain `leanix_storage` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-27` | Leanix Survey Operations | MCP tool domain `leanix_survey` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-28` | Leanix Synclog Operations | MCP tool domain `leanix_synclog` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-29` | Leanix Technology Discovery Operations | MCP tool domain `leanix_technology_discovery` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-30` | Leanix Todo Operations | MCP tool domain `leanix_todo` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-31` | Leanix Transformations Operations | MCP tool domain `leanix_transformations` — Action-routed dynamic tool registration |
| `CONCEPT:LX-OS.governance.lix-32` | Leanix Webhooks Operations | MCP tool domain `leanix_webhooks` — Action-routed dynamic tool registration |

## Cross-Project References (from agent-utilities)

| Concept ID | Name | Origin |
|------------|------|--------|
| `CONCEPT:AU-ECO.messaging.native-backend-abstraction` | Unified Toolkit Ingestion | agent-utilities |
| `CONCEPT:AU-ORCH.adapter.hot-cache-invalidation` | Confidence-Gated Router | agent-utilities |
| `CONCEPT:AU-OS.config.secrets-authentication` | Prompt Injection Defense | agent-utilities |
| `CONCEPT:AU-OS.state.cognitive-scheduler-preemption` | Cognitive Scheduler | agent-utilities |
| `CONCEPT:AU-OS.governance.reactive-multi-axis-budget` | Guardrail Engine | agent-utilities |
| `CONCEPT:AU-OS.governance.wasm-micro-agent-sandbox` | Audit Logging | agent-utilities |
| `CONCEPT:AU-KG.query.object-graph-mapper` | Knowledge Graph Core | agent-utilities |

## Synergy with agent-utilities

This project integrates with `agent-utilities` via `CONCEPT:AU-ECO.messaging.native-backend-abstraction` (Unified Toolkit Ingestion). The `leanix_agent` MCP server registers its tools with the agent-utilities FastMCP middleware, enabling automatic discovery, telemetry, and Knowledge Graph ingestion of all LIX-* concepts.
