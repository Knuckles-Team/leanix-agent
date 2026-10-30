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
