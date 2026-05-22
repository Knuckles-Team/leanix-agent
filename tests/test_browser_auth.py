"""
Tests for browser_auth.py - Browser-based OAuth PKCE login and token lifecycle.
"""

import json
import os
import time
from unittest.mock import MagicMock, Mock, patch

import pytest
import httpx

from leanix_agent.browser_auth import (
    generate_pkce,
    LeanixBrowserAuthManager,
)
from leanix_agent.auth import (
    get_client,
    is_browser_auth_enabled as auth_is_browser_enabled,
)
from leanix_agent.api.api_client_leanix import LeanixApi


@pytest.mark.unit
class TestBrowserAuthUtils:
    """Test PKCE generation and auth enabled helpers."""

    def test_generate_pkce(self):
        """Test that generate_pkce returns valid code_verifier and code_challenge."""
        verifier, challenge = generate_pkce()
        assert verifier is not None
        assert challenge is not None
        assert len(verifier) > 0
        assert len(challenge) > 0

    @patch.dict(os.environ, {"LEANIX_AUTH_METHOD": "browser"}, clear=True)
    def test_is_browser_auth_enabled_env(self):
        """Test is_browser_auth_enabled when LEANIX_AUTH_METHOD=browser."""
        assert auth_is_browser_enabled() is True

    @patch.dict(os.environ, {"LEANIX_BROWSER_LOGIN": "True"}, clear=True)
    def test_is_browser_auth_enabled_flag(self):
        """Test is_browser_auth_enabled when LEANIX_BROWSER_LOGIN=True."""
        assert auth_is_browser_enabled() is True

    @patch.dict(os.environ, {}, clear=True)
    def test_is_browser_auth_enabled_disabled(self):
        """Test is_browser_auth_enabled defaults to False."""
        assert auth_is_browser_enabled() is False


@pytest.mark.unit
class TestLeanixBrowserAuthManager:
    """Tests for LeanixBrowserAuthManager class."""

    def setup_method(self):
        self.mock_secrets = MagicMock()
        self.manager = LeanixBrowserAuthManager(
            workspace_base_url="https://test-workspace.leanix.net",
            secrets_client=self.mock_secrets,
        )

    def test_init_sets_correct_secret_key(self):
        """Test that the secret key is correctly scoped by workspace host."""
        assert (
            self.manager.secret_key == "leanix/oauth_tokens/test-workspace.leanix.net"
        )

    def test_get_cached_tokens_returns_none_if_missing(self):
        """Test that get_cached_tokens returns None when secrets client returns None."""
        self.mock_secrets.get.return_value = None
        assert self.manager.get_cached_tokens() is None

    def test_get_cached_tokens_returns_decoded_dict(self):
        """Test that get_cached_tokens parses JSON successfully."""
        tokens = {"access_token": "abc", "refresh_token": "def", "expires_at": 123.4}
        self.mock_secrets.get.return_value = json.dumps(tokens)
        assert self.manager.get_cached_tokens() == tokens

    def test_save_tokens_persists_tokens(self):
        """Test that save_tokens stores serialized JSON in secrets."""
        tokens = {"access_token": "abc"}
        self.manager.save_tokens(tokens)
        self.mock_secrets.set.assert_called_once_with(
            self.manager.secret_key, json.dumps(tokens)
        )

    @patch("httpx.post")
    def test_refresh_tokens_success(self, mock_post):
        """Test successful token refresh using httpx."""
        mock_response = MagicMock()
        mock_response.json.return_value = {
            "access_token": "new-access",
            "refresh_token": "new-refresh",
            "expires_in": 3600,
        }
        mock_post.return_value = mock_response

        old_tokens = {"refresh_token": "old-refresh"}
        new_tokens = self.manager.refresh_tokens(old_tokens)

        assert new_tokens["access_token"] == "new-access"
        assert new_tokens["refresh_token"] == "new-refresh"
        assert new_tokens["expires_at"] > time.time()
        self.mock_secrets.set.assert_called_once()

    def test_resolve_credentials_returns_none_no_cached_no_login(self):
        """Test resolve_credentials returns None when no cached tokens exist and auto_login=False."""
        self.mock_secrets.get.return_value = None
        assert self.manager.resolve_credentials(auto_login=False) is None

    def test_resolve_credentials_returns_cached_valid_token(self):
        """Test resolve_credentials returns access token if cached and valid."""
        tokens = {
            "access_token": "valid-token",
            "refresh_token": "refresh",
            "expires_at": time.time() + 1000,
        }
        self.mock_secrets.get.return_value = json.dumps(tokens)
        assert self.manager.resolve_credentials(auto_login=False) == "valid-token"

    @patch.object(LeanixBrowserAuthManager, "refresh_tokens")
    def test_resolve_credentials_proactive_refresh(self, mock_refresh):
        """Test resolve_credentials refreshes token if it is about to expire."""
        tokens = {
            "access_token": "expiring-token",
            "refresh_token": "refresh",
            "expires_at": time.time() + 10,  # expiring in 10s (skew window is 120s)
        }
        self.mock_secrets.get.return_value = json.dumps(tokens)

        refreshed = {
            "access_token": "refreshed-token",
            "refresh_token": "refresh",
            "expires_at": time.time() + 3600,
        }
        mock_refresh.return_value = refreshed

        token = self.manager.resolve_credentials(auto_login=False)
        assert token == "refreshed-token"
        mock_refresh.assert_called_once_with(tokens)


@pytest.mark.unit
class TestLeanixAuthIntegration:
    """Integration test verification for auth.py using browser auth."""

    def setup_method(self):
        import leanix_agent.auth

        leanix_agent.auth._client = None

    def teardown_method(self):
        import leanix_agent.auth

        leanix_agent.auth._client = None

    @patch.dict(
        os.environ,
        {
            "LEANIX_AUTH_METHOD": "browser",
            "LEANIX_WORKSPACE": "https://test.leanix.net",
        },
        clear=True,
    )
    @patch("leanix_agent.browser_auth.LeanixBrowserAuthManager.resolve_credentials")
    def test_get_client_browser_auth_enabled(self, mock_resolve):
        """Test that get_client uses browser auth and returns LeanixApi with is_oauth=True."""
        mock_resolve.return_value = "mocked-oauth-bearer-token"

        client = get_client()
        assert client is not None
        assert client.is_oauth is True
        assert client.access_token == "mocked-oauth-bearer-token"
        assert client.headers["Authorization"] == "Bearer mocked-oauth-bearer-token"

    @patch.dict(
        os.environ,
        {
            "LEANIX_AUTH_METHOD": "browser",
            "LEANIX_WORKSPACE": "https://test.leanix.net",
        },
        clear=True,
    )
    @patch("leanix_agent.browser_auth.LeanixBrowserAuthManager.resolve_credentials")
    def test_sub_api_header_prepopulation(self, mock_resolve):
        """Test that dynamic sub-API factory prepopulates authorization headers."""
        mock_resolve.return_value = "oauth-token"

        # Instantiate the main OAuth client
        main_client = get_client()

        # Mock sub-API module and Api class
        mock_api_class = MagicMock()
        mock_api_instance = MagicMock()
        mock_api_instance._session = MagicMock()
        mock_api_instance._session.headers = {}
        mock_api_class.Api.return_value = mock_api_instance

        import importlib

        original_import = importlib.import_module

        def mock_import_fn(name, package=None):
            if "api_client_mtm" in name:
                return mock_api_class
            return original_import(name, package)

        with patch("importlib.import_module", side_effect=mock_import_fn):
            # Trigger get_mtm_client dynamic attribute retrieval
            from leanix_agent.auth import get_mtm_client

            sub_api = get_mtm_client()

            # Verify that sub-API was constructed and headers prepopulated
            mock_api_class.Api.assert_called_once_with(
                base_url=main_client.base_url,
                token=main_client.api_token,
                verify=main_client.verify,
            )
            assert sub_api._session.headers["Authorization"] == "Bearer oauth-token"
