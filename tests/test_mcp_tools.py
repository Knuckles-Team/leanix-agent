"""
Tests for programmatically verifying all registered MCP tools in mcp_server.py.
"""

import sys

# Set dummy sys.argv before importing anything to prevent create_mcp_server parsing issues
sys.argv = ["mcp_server.py"]

import asyncio
import re
import pytest
from unittest.mock import MagicMock

from leanix_agent.mcp_server import get_mcp_instance


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
    mcp, _, _ = get_mcp_instance()
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
    mcp, _, _ = get_mcp_instance()
    tools = await mcp.list_tools()

    meta_tool = next((t for t in tools if t.name == "leanix_discover_meta_model"), None)
    assert meta_tool is not None, "leanix_discover_meta_model tool not found"

    res = await meta_tool.fn(
        fact_sheet_type="Application",
        client=mock_client,
        ctx=None,
    )

    assert res is not None


def get_all_mcp_tools_and_actions():
    """Discover all registered MCP tools and their corresponding actions."""
    # Run the async discovery in a synchronous wrapper for pytest parameterization
    loop = asyncio.get_event_loop()
    mcp, _, _ = get_mcp_instance()
    tools = loop.run_until_complete(mcp.list_tools())

    test_cases = []
    for tool in tools:
        if tool.name in ("leanix_graphql", "leanix_discover_meta_model"):
            continue

        desc = ""
        if "action" in tool.parameters.get("properties", {}):
            desc = tool.parameters["properties"]["action"].get("description", "")

        actions = re.findall(r"'([^']+)'", desc)
        if not actions:
            actions = ["healthcheck"]

        for action in actions:
            test_cases.append((tool.name, action))

    return test_cases


@pytest.mark.asyncio
@pytest.mark.parametrize("tool_name, action", get_all_mcp_tools_and_actions())
async def test_all_mcp_tools(tool_name, action, mock_client):
    """Dynamically test every registered MCP tool and action by invoking the underlying function."""
    mcp, _, _ = get_mcp_instance()
    tools = await mcp.list_tools()

    tool = next((t for t in tools if t.name == tool_name), None)
    assert tool is not None, f"Tool {tool_name} not found"

    # Invoke t.fn directly with the action, mock client, and mock ctx
    mock_ctx = MagicMock()
    try:
        res = await tool.fn(
            action=action, params_json="{}", client=mock_client, ctx=mock_ctx
        )
        assert isinstance(res, (dict, list, str, int, float, bool)) or res is None
        mock_ctx.info.assert_called_with("Executing tool...")
    except Exception as e:
        pytest.fail(f"Tool {tool_name} failed on action {action}: {e}")


@pytest.mark.asyncio
async def test_mcp_tools_exception_paths(mock_client):
    """Test standard error handling in MCP tools (invalid JSON, unknown actions)."""
    mcp, _, _ = get_mcp_instance()
    tools = await mcp.list_tools()

    # Get any tool other than leanix_graphql or leanix_discover_meta_model
    tool = next(
        (
            t
            for t in tools
            if t.name not in ("leanix_graphql", "leanix_discover_meta_model")
        ),
        None,
    )
    assert tool is not None

    # 1. Invalid JSON
    res = await tool.fn(
        action="healthcheck", params_json="{invalid_json}", client=mock_client, ctx=None
    )
    assert "error" in res
    assert "Invalid params_json" in res["error"]

    # 2. Unknown action
    with pytest.raises(ValueError, match="Unknown action: unknown_action_xyz"):
        await tool.fn(
            action="unknown_action_xyz", params_json="{}", client=mock_client, ctx=None
        )


@pytest.mark.asyncio
async def test_mcp_server_custom_routes():
    """Test custom HTTP endpoints like /health registered on the MCP server."""
    # Temporarily bypass requests dependency check
    from leanix_agent.mcp_server import get_mcp_instance

    mcp, _, _ = get_mcp_instance()

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

    assert json.loads(response.body) == {"status": "OK"}


def test_mcp_server_entrypoint():
    """Test the central mcp_server entrypoint launch block with stdio, streamable-http, sse, and invalid transports."""
    from leanix_agent.mcp_server import mcp_server
    from unittest.mock import patch, MagicMock

    mock_mcp = MagicMock()

    # Test stdio run
    mock_args = MagicMock()
    mock_args.transport = "stdio"
    mock_args.auth_type = "none"
    mock_args.host = "localhost"
    mock_args.port = 8000

    with (
        patch(
            "leanix_agent.mcp_server.get_mcp_instance",
            return_value=(mock_mcp, mock_args, []),
        ),
        patch("sys.exit") as mock_exit,
    ):
        mcp_server()
        mock_mcp.run.assert_called_with(transport="stdio")

    # Test streamable-http run
    mock_args.transport = "streamable-http"
    with patch(
        "leanix_agent.mcp_server.get_mcp_instance",
        return_value=(mock_mcp, mock_args, []),
    ):
        mcp_server()
        mock_mcp.run.assert_called_with(
            transport="streamable-http", host="localhost", port=8000
        )

    # Test sse run
    mock_args.transport = "sse"
    with patch(
        "leanix_agent.mcp_server.get_mcp_instance",
        return_value=(mock_mcp, mock_args, []),
    ):
        mcp_server()
        mock_mcp.run.assert_called_with(transport="sse", host="localhost", port=8000)

    # Test invalid transport exits
    mock_args.transport = "invalid-transport-xyz"
    with (
        patch(
            "leanix_agent.mcp_server.get_mcp_instance",
            return_value=(mock_mcp, mock_args, []),
        ),
        patch("sys.exit") as mock_exit,
    ):
        mcp_server()
        mock_exit.assert_called_once_with(1)
