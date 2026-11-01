# CONN-LEANIX-AGENT — LeanIX connector tool surface

## Outcome

The connector must serve one typed MCP tool for each operation of the LeanIX API routers.
The served surface holds 746 router operations plus 12 base tools, which is 758 tools.

## Scope and owner

The `leanix-agent` repository owns this behavior. The shared connector SDK owns the tool-surface mechanism.
The shared pipelines repository owns quality gates and delivery rendering.

Component: Connector integration
References: [Connector SDK](https://github.com/Knuckles-Team/scion-sdk/blob/main/README.md)
Code: ../../leanix_agent/mcp_server.py:234 ../../leanix_agent/mcp ../../tests/test_per_operation_tools_cover_routers.py ../../pyproject.toml

## Non-goals

This specification grants no service access, credential creation, deployment, or approval exception.
The connector must not implement a graph engine, a policy authority, or a duplicate shared SDK runtime.

## Why a new spec

The search `git grep -n leanix -- specs` found no spec in this repository. The `specs/` tree holds only the template. No other repository owns the LeanIX tool surface.

## Requirements

See [requirements.md](requirements.md), [plan.md](plan.md), and [test-spec.md](test-spec.md).

## Scope and interfaces

In scope: the rows of [requirements.md](requirements.md). Out of scope: the SDK modules and the engine, which own the shared capabilities.

## User Scenarios & Testing

### User Story 1 - LeanIX connector tool surface (Priority: P1)

The connector must serve one typed MCP tool for each operation of the LeanIX API routers.

**Acceptance Scenarios**:

1. **Given** the connector is configured, **When** the behaviour of row `CONN-LEANIX-AGENT-R001` (per-operation tools) is exercised, **Then** `tests/test_per_operation_tools_cover_routers.py` rows R001.1 to R001.6 pass.
2. **Given** the connector is configured, **When** the behaviour of row `CONN-LEANIX-AGENT-R002` (shared graphql client) is exercised, **Then** `tests/test_leanix_gql.py::TestGraphQLDelegation` must pass.

### Edge Cases

- If `CONN-LEANIX-AGENT-R001` is not met, its proving test fails: per-operation tools.
- If `CONN-LEANIX-AGENT-R002` is not met, its proving test fails: shared graphql client.

## Requirements

- **FR-001**: Per-operation tools. Rows: `CONN-LEANIX-AGENT-R001`.
- **FR-002**: Shared GraphQL client. Rows: `CONN-LEANIX-AGENT-R002`.

## Success Criteria

- **SC-001**: `tests/test_per_operation_tools_cover_routers.py` rows R001.1 to R001.6 pass. Rows: `CONN-LEANIX-AGENT-R001`.
- **SC-002**: `tests/test_leanix_gql.py::TestGraphQLDelegation` must pass. Rows: `CONN-LEANIX-AGENT-R002`.

## Assumptions

- The external system is reachable with operator-supplied credentials.
- The SDK and engine contracts the rows cite are at the floors declared in `pyproject.toml`.

## Traceability

| Label | Rows | Design section | Test ID | Evidence |
|---|---|---|---|---|
| FR-001 | `CONN-LEANIX-AGENT-R001` | [plan.md](plan.md) | T-001 | [test-spec.md](test-spec.md) |
| FR-002 | `CONN-LEANIX-AGENT-R002` | [plan.md](plan.md) | T-002 | [test-spec.md](test-spec.md) |
