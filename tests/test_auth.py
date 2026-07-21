"""
Tests for leanix_agent/auth.py, validating all authentication paths, factories, and exception pathways.

CONCEPT:AU-OS.config.secrets-authentication
CONCEPT:AU-KG.query.object-graph-mapper
"""

import os
from unittest.mock import MagicMock, patch

import pytest
from agent_utilities.core.exceptions import AuthError

import leanix_agent.auth as auth
from leanix_agent.api.api_client_leanix import LeanixApi


@pytest.fixture(autouse=True)
def reset_client_singleton():
    """Reset the auth module's global _client singleton before/after each test."""
    auth._client = None
    yield
    auth._client = None


def test_get_client_singleton():
    """Test that get_client returns the cached singleton client if it already exists."""
    mock_client = MagicMock(spec=LeanixApi)
    auth._client = mock_client

    # Enable browser auth, but check that it doesn't trigger refresh if it doesn't have browser_auth_manager
    with patch("leanix_agent.auth.is_browser_auth_enabled", return_value=True):
        res = auth.get_client()
        assert res is mock_client


def test_get_client_singleton_browser_refresh():
    """Test get_client singleton checking browser auth proactively."""
    mock_client = MagicMock(spec=LeanixApi)
    mock_client.access_token = "old-token"
    mock_client.headers = {"Authorization": "Bearer old-token"}
    mock_auth_manager = MagicMock()
    mock_auth_manager.resolve_credentials.return_value = "new-token"
    mock_client.browser_auth_manager = mock_auth_manager

    auth._client = mock_client

    with patch("leanix_agent.auth.is_browser_auth_enabled", return_value=True):
        res = auth.get_client()
        assert res is mock_client
        assert mock_client.access_token == "new-token"
        assert mock_client.headers["Authorization"] == "Bearer new-token"


def test_get_client_singleton_browser_refresh_exception():
    """Test get_client singleton browser auth refresh logging a warning on error."""
    mock_client = MagicMock(spec=LeanixApi)
    mock_client.access_token = "old-token"
    mock_auth_manager = MagicMock()
    mock_auth_manager.resolve_credentials.side_effect = Exception("Auth Server Down")
    mock_client.browser_auth_manager = mock_auth_manager

    auth._client = mock_client

    with (
        patch("leanix_agent.auth.is_browser_auth_enabled", return_value=True),
        patch("leanix_agent.auth.logger.warning") as mock_warning,
    ):
        res = auth.get_client()
        assert res is mock_client
        assert mock_client.access_token == "old-token"
        mock_warning.assert_called_once_with("Browser OAuth token refresh unavailable")


@patch.dict(
    os.environ,
    {"LEANIX_AUTH_METHOD": "browser", "LEANIX_WORKSPACE": "https://test.leanix.net"},
    clear=True,
)
@patch("agent_utilities.security.browser_auth.BaseBrowserAuthManager")
def test_get_client_browser_auth_success(mock_manager_type):
    """Test successful PKCE browser oauth instantiation path."""
    mock_manager = MagicMock()
    mock_manager.resolve_credentials.return_value = "oauth-access-token"
    mock_manager_type.return_value = mock_manager

    client = auth.get_client()
    assert client.is_oauth is True
    assert client.access_token == "oauth-access-token"
    assert client.headers["Authorization"] == "Bearer oauth-access-token"
    assert client.browser_auth_manager is mock_manager


@patch.dict(
    os.environ,
    {"LEANIX_AUTH_METHOD": "browser", "LEANIX_WORKSPACE": "https://test.leanix.net"},
    clear=True,
)
@patch("agent_utilities.security.browser_auth.BaseBrowserAuthManager")
def test_get_client_browser_auth_failure(mock_manager_type):
    """Test that PKCE browser oauth raises a RuntimeError upon failure."""
    mock_manager = MagicMock()
    mock_manager.resolve_credentials.side_effect = Exception("Failed connection")
    mock_manager_type.return_value = mock_manager

    with pytest.raises(
        RuntimeError,
        match="AUTHENTICATION ERROR: Interactive browser OAuth login failed",
    ):
        auth.get_client()


@patch.dict(os.environ, {"LEANIX_WORKSPACE": "https://test.leanix.net"}, clear=True)
@patch("agent_utilities.mcp.delegated_auth.is_delegation_enabled", return_value=True)
@patch(
    "agent_utilities.mcp.delegated_auth.get_delegated_token",
    return_value="delegated-access-token",
)
@patch("agent_utilities.mcp.delegated_auth.get_user_identity")
def test_get_client_oidc_delegation_success(mock_identity, mock_token, mock_enabled):
    """Test successful OIDC delegation path (RFC 8693 token exchange)."""
    _ = (mock_token, mock_enabled)
    client = auth.get_client()
    assert client.api_token == "delegated-access-token"
    assert client.base_url == "https://test.leanix.net"
    mock_identity.assert_not_called()


@patch.dict(
    os.environ,
    {"LEANIX_WORKSPACE": "https://test.leanix.net", "LEANIX_TOKEN": "fallback-token"},
    clear=True,
)
@patch("agent_utilities.mcp.delegated_auth.is_delegation_enabled", return_value=True)
@patch(
    "agent_utilities.mcp.delegated_auth.get_delegated_token",
    side_effect=Exception("Token exchange failed"),
)
@patch("leanix_agent.auth.logger.warning")
def test_get_client_oidc_delegation_fallback(mock_warn, mock_token, mock_enabled):
    """Test that get_client gracefully falls back to API token if OIDC delegation fails."""
    _ = (mock_token, mock_enabled)
    client = auth.get_client()
    assert client.api_token == "fallback-token"
    mock_warn.assert_called_once_with(
        "OIDC delegation unavailable; using configured API credentials"
    )


@patch.dict(
    os.environ,
    {
        "LEANIX_WORKSPACE": "https://test.leanix.net",
        "LEANIX_TOKEN": "fixture-token",
    },
    clear=True,
)
@patch("leanix_agent.auth.LeanixApi")
@patch("leanix_agent.auth.resolve_configured_tls_profile")
def test_get_client_uses_shared_current_tls_profile(resolve_tls, api_class):
    """Auth resolves one strict AgentConfig transport profile for LeanIX."""
    tls_profile = MagicMock()
    resolve_tls.return_value = tls_profile

    client = auth.get_client()

    assert client is api_class.return_value
    resolve_tls.assert_called_once_with("leanix")
    api_class.assert_called_once_with(
        base_url="https://test.leanix.net",
        token="fixture-token",
        client_id=None,
        client_secret=None,
        tls_profile=tls_profile,
    )


@patch.dict(
    os.environ,
    {
        "LEANIX_WORKSPACE": "https://test.leanix.net",
        "LEANIX_TECHNICAL_USER": "tech_user",
        "LEANIX_TECHNICAL_USER_PASSWORD": "tech_password",
    },
    clear=True,
)
def test_technical_user_credentials():
    """Test using Technical User ID and Password."""
    client = auth.get_client()
    assert client.client_id == "tech_user"
    assert client.client_secret == "tech_password"


@patch.dict(
    os.environ,
    {"LEANIX_WORKSPACE": "https://test.leanix.net", "LEANIX_TOKEN": "invalid-token"},
    clear=True,
)
@patch(
    "leanix_agent.api.api_client_leanix.LeanixApi.__init__",
    side_effect=AuthError("Invalid LeanIX API Token"),
)
def test_client_init_auth_error(mock_init):
    """Test that get_client wraps AuthError into RuntimeError."""
    _ = mock_init
    with pytest.raises(
        RuntimeError,
        match="AUTHENTICATION ERROR: The LeanIX credentials provided are not valid",
    ):
        auth.get_client()


def test_get_graphql_client(tls_profile_factory):
    """Test creating GraphQL client factory under different authentication states."""
    mock_client = MagicMock(spec=LeanixApi)
    mock_client.base_url = "https://mock.leanix.net"
    mock_client.access_token = None
    mock_client.tls_profile = tls_profile_factory()

    def mock_auth():
        mock_client.access_token = "mock-graphql-token"

    mock_client._authenticate.side_effect = mock_auth

    with patch("leanix_agent.auth.get_client", return_value=mock_client):
        gql_client = auth.get_graphql_client()
        mock_client._authenticate.assert_called_once()
        assert (
            gql_client.url == "https://mock.leanix.net/services/pathfinder/v1/graphql"
        )
        assert gql_client.token == "mock-graphql-token"
        assert gql_client.tls_profile is mock_client.tls_profile


def test_dynamic_client_factories():
    """Test resolving sub-API clients via module-level __getattr__."""
    mock_client = MagicMock(spec=LeanixApi)
    mock_client.base_url = "https://mock.leanix.net"
    mock_client.api_token = "mock-api-token"
    mock_client.access_token = "mock-exchanged-access-token"
    mock_client.tls_profile = MagicMock()
    mock_client.is_oauth = False

    with patch("leanix_agent.auth.get_client", return_value=mock_client):
        # Trigger get_mtm_client dynamic attribute retrieval
        factory = auth.get_mtm_client
        assert callable(factory)

        mock_api_instance = MagicMock()
        mock_api_instance._session = MagicMock()
        mock_api_instance._session.headers = {}

        with patch("importlib.import_module") as mock_import:
            mock_mod = MagicMock()
            mock_mod.Api.return_value = mock_api_instance
            mock_import.return_value = mock_mod

            sub_client = factory()
            assert sub_client is mock_api_instance
            mock_mod.Api.assert_called_once_with(
                base_url="https://mock.leanix.net/services/mtm/v1",
                token="mock-exchanged-access-token",
                tls_profile=mock_client.tls_profile,
            )
            mock_client.tls_profile.configure_requests_session.assert_called_once_with(
                mock_api_instance._session
            )


def test_dynamic_client_factories_oauth():
    """Test resolving sub-API clients via module-level __getattr__ with OAuth headers."""
    mock_client = MagicMock(spec=LeanixApi)
    mock_client.base_url = "https://mock.leanix.net"
    mock_client.api_token = "mock-api-token"
    mock_client.access_token = "mock-oauth-access-token"
    mock_client.tls_profile = MagicMock()
    mock_client.is_oauth = True

    with patch("leanix_agent.auth.get_client", return_value=mock_client):
        factory = auth.get_mtm_client
        mock_api_instance = MagicMock()
        mock_api_instance._session = MagicMock()
        mock_api_instance._session.headers = {}

        with patch("importlib.import_module") as mock_import:
            mock_mod = MagicMock()
            mock_mod.Api.return_value = mock_api_instance
            mock_import.return_value = mock_mod

            sub_client = factory()
            assert sub_client is mock_api_instance
            assert (
                sub_client._session.headers["Authorization"]
                == "Bearer mock-oauth-access-token"
            )


def test_dynamic_client_factories_import_error():
    """Test importing non-existent API client modules via __getattr__."""
    mock_client = MagicMock(spec=LeanixApi)
    with patch("leanix_agent.auth.get_client", return_value=mock_client):
        factory = auth.get_non_existent_client
        with pytest.raises(
            AttributeError,
            match="Module leanix_agent.api.api_client_non_existent not found",
        ):
            factory()


def test_invalid_module_getattr():
    """Test accessing non-factory attributes on the auth module raises AttributeError."""
    with pytest.raises(
        AttributeError,
        match="module 'leanix_agent.auth' has no attribute 'invalid_attr'",
    ):
        _ = auth.invalid_attr


def test_generated_service_locations_are_current_and_exact():
    assert auth._service_base_url(
        "https://tenant.example.test", "discovery_linking_v2"
    ) == ("https://tenant.example.test/services/discovery-linking/v2")
    assert auth._service_base_url(
        "https://tenant.example.test", "reference_data_catalog"
    ) == ("https://tenant.example.test/services/reference-data-catalog/v1")
