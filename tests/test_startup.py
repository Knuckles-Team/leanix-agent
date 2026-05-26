"""
Tests for verifying agent initialization, dynamic imports, and CLI server startup wrappers.
"""

import sys
import pytest
from unittest.mock import patch, MagicMock

import leanix_agent


def test_init_module_dynamic_attributes():
    """Verify dynamic attributes on leanix_agent package imports."""
    # 1. Test availability flags
    assert isinstance(leanix_agent._MCP_AVAILABLE, bool)
    assert isinstance(leanix_agent._AGENT_AVAILABLE, bool)

    # 2. Test fetching non-existent attribute raises AttributeError
    with pytest.raises(
        AttributeError, match="has no attribute 'non_existent_attribute'"
    ):
        _ = leanix_agent.non_existent_attribute

    # 3. Test __dir__ returns expected dynamic lists
    d = dir(leanix_agent)
    assert "_expose_members" in d


def test_agent_server_bootstrap():
    """Test the agent_server entry point with custom command-line arguments."""
    from leanix_agent.agent_server import agent_server

    # Setup mock parser arguments
    mock_args = MagicMock()
    mock_args.debug = True
    mock_args.mcp_url = "http://localhost:8000"
    mock_args.mcp_config = "mcp_config.json"
    mock_args.host = "127.0.0.1"
    mock_args.port = 9000
    mock_args.provider = "openai"
    mock_args.model_id = "gpt-4o"
    mock_args.base_url = None
    mock_args.api_key = None
    mock_args.custom_skills_directory = None
    mock_args.web = True
    mock_args.otel = True
    mock_args.otel_endpoint = "http://localhost:4317"
    mock_args.otel_headers = None
    mock_args.otel_public_key = None
    mock_args.otel_secret_key = None
    mock_args.otel_protocol = "grpc"

    # Mock the parser and server creator
    mock_parser = MagicMock()
    mock_parser.parse_args.return_value = mock_args

    with (
        patch(
            "leanix_agent.agent_server.create_agent_parser", return_value=mock_parser
        ),
        patch("leanix_agent.agent_server.create_agent_server") as mock_create,
    ):
        agent_server()

        # Assert correct parser loading & server configuration dispatch
        mock_parser.parse_args.assert_called_once()
        mock_create.assert_called_once_with(
            mcp_url="http://localhost:8000",
            mcp_config="mcp_config.json",
            host="127.0.0.1",
            port=9000,
            provider="openai",
            model_id="gpt-4o",
            router_model="gpt-4o",
            agent_model="gpt-4o",
            base_url=None,
            api_key=None,
            custom_skills_directory=None,
            enable_web_ui=True,
            enable_otel=True,
            otel_endpoint="http://localhost:4317",
            otel_headers=None,
            otel_public_key=None,
            otel_secret_key=None,
            otel_protocol="grpc",
            debug=True,
        )
