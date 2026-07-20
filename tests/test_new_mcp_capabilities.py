"""Direct execution coverage for the newly integrated MCP capability clusters."""

from __future__ import annotations

from types import SimpleNamespace
from unittest.mock import MagicMock, patch

import pytest
from fastmcp import FastMCP

from leanix_agent.mcp.mcp_graphql import register_graphql_tools
from leanix_agent.mcp.mcp_instance_graph import register_instance_graph_tools
from leanix_agent.mcp.mcp_universal_api import register_universal_api_tools


async def _tool(mcp: FastMCP, name: str):
    return next(tool for tool in await mcp.list_tools() if tool.name == name)


@pytest.mark.asyncio
async def test_universal_rest_tool_executes_reads_and_blocks_mutations():
    mcp = FastMCP("universal-fixture")
    register_universal_api_tools(mcp)
    tool = await _tool(mcp, "leanix_rest_api")
    client = MagicMock()
    client.request_api.return_value = {"status": 200, "data": {"ok": True}}

    read = await tool.fn(
        method="GET",
        service="pathfinder",
        endpoint="factSheets",
        version="v1",
        params_json="{}",
        body_json="{}",
        files_json="{}",
        accept="application/json",
        allow_mutation=False,
        client=client,
        ctx=None,
    )
    blocked = await tool.fn(
        method="DELETE",
        service="pathfinder",
        endpoint="factSheets/opaque-id",
        version="v1",
        params_json="{}",
        body_json="{}",
        files_json="{}",
        accept="application/json",
        allow_mutation=False,
        client=client,
        ctx=None,
    )

    assert read["data"] == {"ok": True}
    assert blocked["errorType"] == "MutationApprovalRequired"
    client.request_api.assert_called_once()


@pytest.mark.asyncio
async def test_graphql_tools_execute_query_schema_and_block_mutation():
    mcp = FastMCP("graphql-fixture")
    register_graphql_tools(mcp)
    client = MagicMock()
    client.execute_gql.return_value = {"viewer": {"id": "opaque"}}
    client.schema_snapshot.return_value = {"schemaDigest": "a" * 64}

    query_tool = await _tool(mcp, "leanix_graphql")
    query = await query_tool.fn(
        query="query Viewer { viewer { id } }",
        variables="{}",
        operation_name="Viewer",
        allow_mutation=False,
        client=client,
        ctx=None,
    )
    blocked = await query_tool.fn(
        query="mutation Update { updateThing { id } }",
        variables="{}",
        operation_name="Update",
        allow_mutation=False,
        client=client,
        ctx=None,
    )
    schema_tool = await _tool(mcp, "leanix_graphql_schema")
    schema = await schema_tool.fn(
        max_types=100, include_sdl=False, client=client, ctx=None
    )

    assert query["viewer"]["id"] == "opaque"
    assert blocked["errorType"] == "MutationApprovalRequired"
    assert schema["schemaDigest"] == "a" * 64
    client.execute_gql.assert_called_once()


@pytest.mark.asyncio
async def test_instance_ontology_and_sync_tools_execute_current_paths():
    mcp = FastMCP("instance-fixture")
    register_instance_graph_tools(mcp)
    client = MagicMock()
    graphql_client = MagicMock()
    artifact = SimpleNamespace(
        model_dump=lambda **_kwargs: {
            "schema_digest": "b" * 64,
            "class_count": 1,
            "turtle": "@prefix : <urn:fixture:> .",
        }
    )
    ontology_tool = await _tool(mcp, "leanix_generate_instance_ontology")
    with (
        patch(
            "leanix_agent.metamodel.discover_meta_model",
            return_value={"factSheets": {"Application": {}}},
        ),
        patch(
            "leanix_agent.metamodel.compile_instance_ontology",
            return_value=artifact,
        ),
    ):
        ontology = await ontology_tool.fn(include_turtle=False, client=client, ctx=None)

    report = SimpleNamespace(
        model_dump=lambda: {
            "status": "ok",
            "native_atomic": True,
            "complete": True,
        }
    )
    sync_tool = await _tool(mcp, "leanix_sync_instance_to_graph")
    with patch("leanix_agent.instance_sync.sync_instance", return_value=report):
        sync = await sync_tool.fn(
            mode="delta",
            ids_json='["opaque-id"]',
            page_size=250,
            client=client,
            graphql_client=graphql_client,
            ctx=None,
        )

    assert ontology["schema_digest"] == "b" * 64
    assert "turtle" not in ontology
    assert sync == {"status": "ok", "native_atomic": True, "complete": True}
