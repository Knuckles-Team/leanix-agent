# CONN-LEANIX-AGENT-CONNECTOR-CONTENT — Implementation plan

Governing spec: [spec.md](spec.md). Rows: [requirements.md](requirements.md).

## Summary

`pyproject.toml` declares `leanix-mcp` as the connector identity. `create_mcp_server` resolves the packaged content of `leanix_agent` from it.

## Technical Context

- **Language/Version**: Python 3.14 (floor 3.12)
- **Primary Dependencies**: scion-sdk, fastmcp
- **Storage**: N/A; the connector stores nothing
- **Testing**: pytest; the proof level each row names
- **Target Platform**: Linux containers
- **Project Type**: connector (MCP server)
- **Performance Goals**: N/A
- **Constraints**: one tool per API operation; shared capabilities come from the SDK
- **Scale/Scope**: 2 rows

## Constitution Check

- One owner per concept: pass. The connector owns one external system's calls, mappings and tools only.
- Connectors depend on the SDK and are called through arbora: pass.
- No ratchets: pass. The rows add no suppression.

## Project Structure

```text
pyproject.toml  existing
leanix_agent/connector_sources.py  existing
```

## Phase 0: Research

No unknowns. Each row names the code it touches.

## Phase 1: Design

The rows are delivered in place; the design is the caller chain below.

## Phase 2: Task approach

`tasks.md` holds one task line per row, producer first.

## Complexity Tracking

None. The constitution check passed.

## Build contract

The repository pre-commit hooks apply: `ruff-format`, `connector-standard`, `secrets`, `tests-fast`. Each row names its proving test. No suppression and no duplicate implementation.

## Production caller chain

1. `CONN-LEANIX-AGENT-CONNECTOR-CONTENT-R001`: the `leanix-mcp` console script (`scion_sdk.cli:serve`) loads the `scion_sdk.connector` entry point `leanix_agent:connector` (`leanix_agent/__init__.py:94`), which the SDK `build_server` turns into the served MCP server and its resources and prompts.
2. `CONN-LEANIX-AGENT-CONNECTOR-CONTENT-R002`: arbora calls `fleet.call` for the existing read tool `leanix_source_factsheets` (`leanix_agent/mcp_server.py:154`) -> the connector source in `leanix_agent/connector_sources.py` -> the packaged `leanix_agent/ontology/access_contracts.ttl` (planned, not yet present).

## Cross-repo seams

none. The cited owner rows are library capabilities the connector calls in process; spec.md names them.
