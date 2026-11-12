"""
Tests for programmatically verifying all registered MCP tools in mcp_server.py.
"""

import sys

# Set dummy sys.argv before importing anything to prevent create_mcp_server parsing issues
sys.argv = ["mcp_server.py"]

import base64
import json
from unittest.mock import MagicMock

import pytest
from scion_sdk.connector import build_server

_DISCOVERED_TOOLS = {}


class MockClient:
    """A highly flexible mock client that returns serializable results for any API call."""

    def __getattr__(self, name):
        def method(*args, **kwargs):
            return {
                "status": "success",
                "method": name,
                "args": [str(a) for a in args],
                "kwargs": {k: str(v) for k, v in kwargs.items()},
            }

        return method


@pytest.fixture
def mock_client():
    """Fixture to provide a flexible MockClient instance."""
    return MockClient()


@pytest.mark.asyncio
async def test_graphql_tool(mock_client):
    """Test the leanix_graphql tool directly."""
    _, mcp = build_server("leanix_agent", command_args=[])
    tools = await mcp.list_tools()

    graphql_tool = next((t for t in tools if t.name == "leanix_graphql"), None)
    assert graphql_tool is not None, "leanix_graphql tool not found"

    # Call t.fn directly with mock dependencies
    res = await graphql_tool.fn(
        query="{ me { id } }",
        variables="{}",
        operation_name=None,
        client=mock_client,
        ctx=None,
    )
    assert res.get("status") == "success"


@pytest.mark.asyncio
async def test_discover_meta_model_tool(mock_client):
    """Test the leanix_discover_meta_model tool directly."""
    _, mcp = build_server("leanix_agent", command_args=[])
    tools = await mcp.list_tools()

    meta_tool = next((t for t in tools if t.name == "leanix_discover_meta_model"), None)
    assert meta_tool is not None, "leanix_discover_meta_model tool not found"

    res = await meta_tool.fn(
        fact_sheet_type="Application",
        client=mock_client,
        ctx=None,
    )

    assert res is not None


@pytest.mark.asyncio
async def test_source_factsheets_tool(mock_client):
    """The provider-owned source preset resolves to a read-only MCP tool."""
    _, mcp = build_server("leanix_agent", command_args=[])
    tools = await mcp.list_tools()

    source_tool = next(
        (tool for tool in tools if tool.name == "leanix_source_factsheets"), None
    )
    assert source_tool is not None

    result = await source_tool.fn(params_json="{}", client=mock_client, ctx=None)

    assert result["count"] == 1
    assert result["data"]["data"][0]["status"] == "success"


async def _graphql_upload_tool():
    _, mcp = build_server("leanix_agent", command_args=[])
    tools = await mcp.list_tools()
    upload_tool = next((t for t in tools if t.name == "leanix_graphql_upload"), None)
    assert upload_tool is not None, "leanix_graphql_upload tool not found"
    return upload_tool


def _single_file_upload_json() -> str:
    return json.dumps(
        {
            "file0": {
                "filename": "a.txt",
                "content_type": "text/plain",
                "content_base64": base64.b64encode(b"content").decode(),
            }
        }
    )


@pytest.mark.asyncio
async def test_graphql_upload_tool_rejects_mismatched_multipart_map(mock_client):
    """A file-map entry referencing an undeclared file must be rejected (FAIL)."""
    upload_tool = await _graphql_upload_tool()

    res = await upload_tool.fn(
        operations_json='{"query": "query { noop }"}',
        file_map_json='{"file0": ["variables.file"]}',
        files_json="{}",
        allow_mutation=False,
        client=mock_client,
        ctx=None,
    )

    assert res["error"] == "GraphQL multipart validation failed"
    assert res["errorType"] == "ValueError"


@pytest.mark.asyncio
async def test_graphql_upload_tool_rejects_unsafe_variable_path(mock_client):
    """A file-map path outside the bounded ``variables.*`` shape must be rejected (FAIL)."""
    upload_tool = await _graphql_upload_tool()

    res = await upload_tool.fn(
        operations_json='{"query": "query { noop }"}',
        file_map_json='{"file0": ["../../etc/passwd"]}',
        files_json=_single_file_upload_json(),
        allow_mutation=False,
        client=mock_client,
        ctx=None,
    )

    assert res["error"] == "GraphQL multipart validation failed"
    assert res["errorType"] == "ValueError"


@pytest.mark.asyncio
async def test_graphql_upload_tool_blocks_unapproved_mutation(mock_client):
    """A mutation document without allow_mutation=True must be blocked, not executed."""
    upload_tool = await _graphql_upload_tool()

    res = await upload_tool.fn(
        operations_json='{"query": "mutation { noop }"}',
        file_map_json='{"file0": ["variables.file"]}',
        files_json=_single_file_upload_json(),
        allow_mutation=False,
        client=mock_client,
        ctx=None,
    )

    assert res == {
        "error": "LeanIX mutation is blocked by default",
        "errorType": "MutationApprovalRequired",
    }


@pytest.mark.asyncio
async def test_graphql_upload_tool_executes_approved_query(mock_client):
    """A well-formed, allowlisted multipart request reaches execute_multipart (PASS)."""
    upload_tool = await _graphql_upload_tool()

    res = await upload_tool.fn(
        operations_json='{"query": "query { factSheets }"}',
        file_map_json='{"file0": ["variables.file"]}',
        files_json=_single_file_upload_json(),
        allow_mutation=False,
        client=mock_client,
        ctx=None,
    )

    assert res.get("status") == "success"
    assert res.get("method") == "execute_multipart"


@pytest.mark.asyncio
async def test_no_served_tool_routes_an_action():
    """Every operation is its own tool; none takes an ``action`` argument."""
    _, mcp = build_server("leanix_agent", command_args=[])
    tools = await mcp.list_tools()
    assert len(tools) == 758
    routed = [
        tool.name for tool in tools if "action" in tool.parameters.get("properties", {})
    ]
    assert routed == []


@pytest.mark.asyncio
async def test_mcp_server_custom_routes():
    """Test custom HTTP endpoints like /health registered on the MCP server."""
    # Temporarily bypass requests dependency check
    from scion_sdk.connector import build_server

    _, mcp = build_server("leanix_agent", command_args=[])

    # Find the health custom route
    health_route = next(
        (route for route in mcp._additional_http_routes if route.path == "/health"),
        None,
    )
    assert health_route is not None, "Health route not found on MCP server"

    # Mock Starlette Request
    mock_request = MagicMock()
    response = await health_route.endpoint(mock_request)
    import json

    assert json.loads(response.body) == {"status": "ok"}
