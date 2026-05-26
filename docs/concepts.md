# Concept Registry — leanix-agent

> **Prefix**: `CONCEPT:LIX-*`
> **Version**: 0.14.0
> **Bridge**: [`CONCEPT:ECO-4.0`](../../agent-utilities/docs/concepts.md) (Unified Toolkit Ingestion)

---

## Project-Specific Concepts

| Concept ID | Name | Description |
|------------|------|-------------|
| `CONCEPT:LIX-001` | Graphql Operations | MCP tool domain `graphql` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-002` | Leanix Ai Inventory Builder Operations | MCP tool domain `leanix_ai_inventory_builder` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-003` | Leanix Apptio Connector Operations | MCP tool domain `leanix_apptio_connector` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-004` | Leanix Automations Operations | MCP tool domain `leanix_automations` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-005` | Leanix Discovery Ai Agents Operations | MCP tool domain `leanix_discovery_ai_agents` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-006` | Leanix Discovery Linking V1 Operations | MCP tool domain `leanix_discovery_linking_v1` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-007` | Leanix Discovery Linking V2 Operations | MCP tool domain `leanix_discovery_linking_v2` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-008` | Leanix Discovery Saas Operations | MCP tool domain `leanix_discovery_saas` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-009` | Leanix Discovery Sap Operations | MCP tool domain `leanix_discovery_sap` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-010` | Leanix Discovery Sap Extension Operations | MCP tool domain `leanix_discovery_sap_extension` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-011` | Leanix Documents Operations | MCP tool domain `leanix_documents` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-012` | Leanix Impacts Operations | MCP tool domain `leanix_impacts` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-013` | Leanix Integration Api Operations | MCP tool domain `leanix_integration_api` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-014` | Leanix Integration Collibra Operations | MCP tool domain `leanix_integration_collibra` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-015` | Leanix Integration Servicenow Operations | MCP tool domain `leanix_integration_servicenow` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-016` | Leanix Integration Signavio Operations | MCP tool domain `leanix_integration_signavio` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-017` | Leanix Inventory Data Quality Operations | MCP tool domain `leanix_inventory_data_quality` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-018` | Leanix Managed Code Execution Operations | MCP tool domain `leanix_managed_code_execution` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-019` | Leanix Metrics Operations | MCP tool domain `leanix_metrics` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-020` | Leanix Mtm Operations | MCP tool domain `leanix_mtm` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-021` | Leanix Navigation Operations | MCP tool domain `leanix_navigation` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-022` | Leanix Pathfinder Operations | MCP tool domain `leanix_pathfinder` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-023` | Leanix Poll Operations | MCP tool domain `leanix_poll` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-024` | Leanix Reference Data Operations | MCP tool domain `leanix_reference_data` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-025` | Leanix Reference Data Catalog Operations | MCP tool domain `leanix_reference_data_catalog` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-026` | Leanix Storage Operations | MCP tool domain `leanix_storage` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-027` | Leanix Survey Operations | MCP tool domain `leanix_survey` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-028` | Leanix Synclog Operations | MCP tool domain `leanix_synclog` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-029` | Leanix Technology Discovery Operations | MCP tool domain `leanix_technology_discovery` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-030` | Leanix Todo Operations | MCP tool domain `leanix_todo` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-031` | Leanix Transformations Operations | MCP tool domain `leanix_transformations` — Action-routed dynamic tool registration |
| `CONCEPT:LIX-032` | Leanix Webhooks Operations | MCP tool domain `leanix_webhooks` — Action-routed dynamic tool registration |

## Cross-Project References (from agent-utilities)

| Concept ID | Name | Origin |
|------------|------|--------|
| `CONCEPT:ECO-4.0` | Unified Toolkit Ingestion | agent-utilities |
| `CONCEPT:ORCH-1.2` | Confidence-Gated Router | agent-utilities |
| `CONCEPT:OS-5.1` | Prompt Injection Defense | agent-utilities |
| `CONCEPT:OS-5.2` | Cognitive Scheduler | agent-utilities |
| `CONCEPT:OS-5.3` | Guardrail Engine | agent-utilities |
| `CONCEPT:OS-5.4` | Audit Logging | agent-utilities |
| `CONCEPT:KG-2.0` | Knowledge Graph Core | agent-utilities |

## Synergy with agent-utilities

This project integrates with `agent-utilities` via `CONCEPT:ECO-4.0` (Unified Toolkit Ingestion). The `leanix_agent` MCP server registers its tools with the agent-utilities FastMCP middleware, enabling automatic discovery, telemetry, and Knowledge Graph ingestion of all LIX-* concepts.
