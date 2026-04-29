"""
Tests for auth.py - Authentication and client initialization.
"""

import pytest
from unittest.mock import Mock, patch
import os

# We need to import the module after mocking urllib3 to avoid the module-level disable_warnings call
import sys
from unittest.mock import MagicMock

# Mock urllib3 before importing auth
mock_urllib3 = MagicMock()
sys.modules["urllib3"] = mock_urllib3
mock_urllib3.disable_warnings = MagicMock()

from leanix_agent.auth import get_client
from agent_utilities.exceptions import AuthError, UnauthorizedError

# Restore original urllib3
del sys.modules["urllib3"]


@pytest.mark.unit
class TestGetClient:
    """Tests for get_client function."""

    def setup_method(self):
        """Reset the global _client before each test."""
        import leanix_agent.auth

        leanix_agent.auth._client = None

    def teardown_method(self):
        """Reset the global _client after each test."""
        import leanix_agent.auth

        leanix_agent.auth._client = None

    @patch.dict(
        os.environ,
        {"LEANIX_WORKSPACE": "https://test.leanix.net", "LEANIX_TOKEN": "test-token"},
        clear=True,
    )
    def test_get_client_creates_instance(self):
        """Test that get_client creates a new instance."""
        with patch("leanix_agent.auth.LeanixApi") as mock_api:
            mock_api.return_value = Mock()
            client = get_client()

            mock_api.assert_called_once_with(
                base_url="https://test.leanix.net", token="test-token", verify=True
            )
            assert client is not None

    @patch.dict(
        os.environ,
        {
            "LEANIX_WORKSPACE": "https://test.leanix.net",
            "LEANIX_API_TOKEN": "api-token",
        },
        clear=True,
    )
    def test_get_client_uses_leanix_api_token(self):
        """Test that get_client uses LEANIX_API_TOKEN when LEANIX_TOKEN is not set."""
        with patch("leanix_agent.auth.LeanixApi") as mock_api:
            mock_api.return_value = Mock()
            client = get_client()

            mock_api.assert_called_once_with(
                base_url="https://test.leanix.net", token="api-token", verify=True
            )

    @patch.dict(
        os.environ,
        {
            "LEANIX_WORKSPACE": "https://test.leanix.net",
            "LEANIX_TOKEN": "token",
            "LEANIX_API_TOKEN": "api-token",
        },
        clear=True,
    )
    def test_get_client_prioritizes_leanix_token(self):
        """Test that get_client prioritizes LEANIX_TOKEN over LEANIX_API_TOKEN."""
        with patch("leanix_agent.auth.LeanixApi") as mock_api:
            mock_api.return_value = Mock()
            client = get_client()

            mock_api.assert_called_once_with(
                base_url="https://test.leanix.net", token="token", verify=True
            )

    @patch.dict(
        os.environ,
        {"LEANIX_WORKSPACE": "https://test.leanix.net", "LEANIX_TOKEN": "test-token"},
        clear=True,
    )
    def test_get_client_singleton(self):
        """Test that get_client returns the same instance on subsequent calls."""
        with patch("leanix_agent.auth.LeanixApi") as mock_api:
            mock_api.return_value = Mock()
            client1 = get_client()
            client2 = get_client()

            mock_api.assert_called_once()
            assert client1 is client2

    @patch.dict(os.environ, {}, clear=True)
    def test_get_client_default_workspace(self):
        """Test that get_client uses default workspace when not set."""
        with patch("leanix_agent.auth.LeanixApi") as mock_api:
            mock_api.return_value = Mock()
            client = get_client()

            mock_api.assert_called_once_with(
                base_url="https://app.leanix.net", token="", verify=True
            )

    @patch.dict(
        os.environ,
        {"LEANIX_WORKSPACE": "https://test.leanix.net", "LEANIX_TOKEN": "test-token"},
        clear=True,
    )
    def test_get_client_ssl_verify_default(self):
        """Test that SSL verification defaults to True."""
        with patch("leanix_agent.auth.LeanixApi") as mock_api:
            mock_api.return_value = Mock()
            client = get_client()

            call_kwargs = mock_api.call_args[1]
            assert call_kwargs["verify"] is True

    @patch.dict(
        os.environ,
        {
            "LEANIX_WORKSPACE": "https://test.leanix.net",
            "LEANIX_TOKEN": "test-token",
            "SSL_VERIFY": "False",
        },
        clear=True,
    )
    def test_get_client_ssl_verify_false(self):
        """Test that SSL_VERIFY=False disables verification."""
        with patch("leanix_agent.auth.LeanixApi") as mock_api:
            mock_api.return_value = Mock()
            client = get_client()

            call_kwargs = mock_api.call_args[1]
            assert call_kwargs["verify"] is False

    @patch.dict(
        os.environ,
        {
            "LEANIX_WORKSPACE": "https://test.leanix.net",
            "LEANIX_TOKEN": "test-token",
            "SSL_VERIFY": "True",
        },
        clear=True,
    )
    def test_get_client_ssl_verify_true(self):
        """Test that SSL_VERIFY=True enables verification."""
        with patch("leanix_agent.auth.LeanixApi") as mock_api:
            mock_api.return_value = Mock()
            client = get_client()

            call_kwargs = mock_api.call_args[1]
            assert call_kwargs["verify"] is True

    @patch.dict(
        os.environ,
        {
            "LEANIX_WORKSPACE": "https://test.leanix.net",
            "LEANIX_TOKEN": "test-token",
            "SSL_VERIFY": "0",
        },
        clear=True,
    )
    def test_get_client_ssl_verify_zero(self):
        """Test that SSL_VERIFY=0 disables verification."""
        with patch("leanix_agent.auth.LeanixApi") as mock_api:
            mock_api.return_value = Mock()
            client = get_client()

            call_kwargs = mock_api.call_args[1]
            assert call_kwargs["verify"] is False

    @patch.dict(
        os.environ,
        {
            "LEANIX_WORKSPACE": "https://test.leanix.net",
            "LEANIX_TOKEN": "test-token",
            "SSL_VERIFY": "1",
        },
        clear=True,
    )
    def test_get_client_ssl_verify_one(self):
        """Test that SSL_VERIFY=1 enables verification."""
        with patch("leanix_agent.auth.LeanixApi") as mock_api:
            mock_api.return_value = Mock()
            client = get_client()

            call_kwargs = mock_api.call_args[1]
            assert call_kwargs["verify"] is True

    @patch.dict(
        os.environ,
        {
            "LEANIX_WORKSPACE": "https://test.leanix.net",
            "LEANIX_TOKEN": "test-token",
            "SSL_VERIFY": "no",
        },
        clear=True,
    )
    def test_get_client_ssl_verify_no(self):
        """Test that SSL_VERIFY=no disables verification."""
        with patch("leanix_agent.auth.LeanixApi") as mock_api:
            mock_api.return_value = Mock()
            client = get_client()

            call_kwargs = mock_api.call_args[1]
            assert call_kwargs["verify"] is False

    @patch.dict(
        os.environ,
        {
            "LEANIX_WORKSPACE": "https://test.leanix.net",
            "LEANIX_TOKEN": "test-token",
            "SSL_VERIFY": "yes",
        },
        clear=True,
    )
    def test_get_client_ssl_verify_yes(self):
        """Test that SSL_VERIFY=yes enables verification."""
        with patch("leanix_agent.auth.LeanixApi") as mock_api:
            mock_api.return_value = Mock()
            client = get_client()

            call_kwargs = mock_api.call_args[1]
            assert call_kwargs["verify"] is True

    @patch.dict(
        os.environ,
        {
            "LEANIX_WORKSPACE": "https://test.leanix.net",
            "LEANIX_TOKEN": "test-token",
            "LEANIX_AGENT_VERIFY": "True",
        },
        clear=True,
    )
    def test_get_client_leanix_agent_verify_true(self):
        """Test that LEANIX_AGENT_VERIFY=True enables verification."""
        with patch("leanix_agent.auth.LeanixApi") as mock_api:
            mock_api.return_value = Mock()
            client = get_client()

            call_kwargs = mock_api.call_args[1]
            assert call_kwargs["verify"] is True

    @patch.dict(
        os.environ,
        {
            "LEANIX_WORKSPACE": "https://test.leanix.net",
            "LEANIX_TOKEN": "test-token",
            "LEANIX_AGENT_VERIFY": "False",
        },
        clear=True,
    )
    def test_get_client_leanix_agent_verify_false(self):
        """Test that LEANIX_AGENT_VERIFY=False disables verification."""
        with patch("leanix_agent.auth.LeanixApi") as mock_api:
            mock_api.return_value = Mock()
            client = get_client()

            call_kwargs = mock_api.call_args[1]
            assert call_kwargs["verify"] is False

    @patch.dict(
        os.environ,
        {
            "LEANIX_WORKSPACE": "https://test.leanix.net",
            "LEANIX_TOKEN": "test-token",
            "SSL_VERIFY": "False",
            "LEANIX_AGENT_VERIFY": "True",
        },
        clear=True,
    )
    def test_get_client_ssl_verify_takes_precedence(self):
        """Test that SSL_VERIFY takes precedence over LEANIX_AGENT_VERIFY."""
        with patch("leanix_agent.auth.LeanixApi") as mock_api:
            mock_api.return_value = Mock()
            client = get_client()

            call_kwargs = mock_api.call_args[1]
            assert call_kwargs["verify"] is False

    @patch.dict(
        os.environ,
        {"LEANIX_WORKSPACE": "https://test.leanix.net", "LEANIX_TOKEN": "test-token"},
        clear=True,
    )
    def test_get_client_auth_error_raises_runtime_error(self):
        """Test that AuthError raises RuntimeError with helpful message."""
        with patch("leanix_agent.auth.LeanixApi") as mock_api:
            mock_api.side_effect = AuthError("Invalid token")

            with pytest.raises(RuntimeError) as exc_info:
                get_client()

            error_msg = str(exc_info.value)
            assert "AUTHENTICATION ERROR" in error_msg
            assert "https://test.leanix.net" in error_msg
            assert "Invalid token" in error_msg

    @patch.dict(
        os.environ,
        {"LEANIX_WORKSPACE": "https://test.leanix.net", "LEANIX_TOKEN": "test-token"},
        clear=True,
    )
    def test_get_client_unauthorized_error_raises_runtime_error(self):
        """Test that UnauthorizedError raises RuntimeError with helpful message."""
        with patch("leanix_agent.auth.LeanixApi") as mock_api:
            mock_api.side_effect = UnauthorizedError("Access forbidden")

            with pytest.raises(RuntimeError) as exc_info:
                get_client()

            error_msg = str(exc_info.value)
            assert "AUTHENTICATION ERROR" in error_msg
            assert "https://test.leanix.net" in error_msg
            assert "Access forbidden" in error_msg

    @patch.dict(
        os.environ,
        {"LEANIX_WORKSPACE": "https://test.leanix.net", "LEANIX_TOKEN": "test-token"},
        clear=True,
    )
    def test_get_client_case_insensitive_ssl_verify(self):
        """Test that SSL_VERIFY is case-insensitive."""
        with patch("leanix_agent.auth.LeanixApi") as mock_api:
            mock_api.return_value = Mock()

            # Test lowercase "false"
            with patch.dict(os.environ, {"SSL_VERIFY": "false"}):
                import leanix_agent.auth

                leanix_agent.auth._client = None
                client = get_client()
                assert mock_api.call_args[1]["verify"] is False

            # Test uppercase "FALSE"
            global _client
            _client = None
            with patch.dict(os.environ, {"SSL_VERIFY": "FALSE"}):
                import leanix_agent.auth

                leanix_agent.auth._client = None
                client = get_client()
                assert mock_api.call_args[1]["verify"] is False

            # Test mixed case "FaLsE"
            _client = None
            with patch.dict(os.environ, {"SSL_VERIFY": "FaLsE"}):
                import leanix_agent.auth

                leanix_agent.auth._client = None
                client = get_client()
                assert mock_api.call_args[1]["verify"] is False
