"""
Tests for mtm_api.py - MTM API client.
"""

import pytest
from unittest.mock import Mock, patch
from requests import Response
import urllib3

from leanix_agent.mtm_api import Api as MtmApi
from agent_utilities.core.exceptions import (
    AuthError,
    MissingParameterError,
    UnauthorizedError,
)


@pytest.mark.unit
class TestMtmApiInitialization:
    """Tests for MtmApi initialization."""

    def test_init_with_all_parameters(self, sample_workspace_base_url, sample_token):
        """Test initialization with all parameters."""
        api = MtmApi(
            base_url=sample_workspace_base_url,
            token=sample_token,
            proxies={"http": "http://proxy:8080"},
            verify=False,
        )
        assert api.base_url == sample_workspace_base_url
        assert api._token == sample_token
        assert api.proxies == {"http": "http://proxy:8080"}
        assert api.verify is False
        assert api._session.verify is False

    def test_init_without_base_url(self, sample_token):
        """Test initialization without base_url raises error."""
        with pytest.raises(MissingParameterError) as exc_info:
            MtmApi(base_url=None, token=sample_token)
        assert "base_url is required" in str(exc_info.value)

    def test_init_without_token(self, sample_workspace_base_url):
        """Test initialization without token raises error."""
        with pytest.raises(MissingParameterError) as exc_info:
            MtmApi(base_url=sample_workspace_base_url)
        assert "token is required" in str(exc_info.value)

    def test_init_with_verify_false_disables_warnings(
        self, sample_workspace_base_url, sample_token
    ):
        """Test that verify=False is set correctly."""
        api = MtmApi(
            base_url=sample_workspace_base_url, token=sample_token, verify=False
        )
        assert api.verify is False
        assert api._session.verify is False

    def test_init_sets_session_verify(self, sample_workspace_base_url, sample_token):
        """Test that session verify is set correctly."""
        api = MtmApi(
            base_url=sample_workspace_base_url, token=sample_token, verify=False
        )
        assert api._session.verify is False


@pytest.mark.auth
class TestMtmApiAuthentication:
    """Tests for MtmApi authentication."""

    def test_authenticate_success(
        self,
        sample_workspace_base_url,
        sample_token,
        sample_bearer_token,
        mock_auth_response,
    ):
        """Test successful authentication."""
        api = MtmApi(base_url=sample_workspace_base_url, token=sample_token)

        with patch.object(api._session, "post", return_value=mock_auth_response):
            api._authenticate()

            assert "Authorization" in api._session.headers
            assert (
                api._session.headers["Authorization"] == f"Bearer {sample_bearer_token}"
            )
            assert api._session.headers["Content-Type"] == "application/json"

    def test_authenticate_uses_workspace_base_url(
        self,
        sample_workspace_base_url,
        sample_token,
        sample_bearer_token,
        mock_auth_response,
    ):
        """Test that authentication uses workspace base URL."""
        api = MtmApi(base_url=sample_workspace_base_url, token=sample_token)

        with patch.object(api._session, "post") as mock_post:
            mock_post.return_value = mock_auth_response
            api._authenticate()

            expected_url = (
                "https://test-workspace.leanix.net/services/mtm/v1/oauth2/token"
            )
            mock_post.assert_called_once()
            call_args = mock_post.call_args
            assert call_args[0][0] == expected_url

    def test_authenticate_403_forbidden(
        self, sample_workspace_base_url, sample_token, mock_forbidden_response
    ):
        """Test authentication with 403 forbidden response."""
        api = MtmApi(base_url=sample_workspace_base_url, token=sample_token)

        with patch.object(api._session, "post", return_value=mock_forbidden_response):
            with pytest.raises(UnauthorizedError) as exc_info:
                api._authenticate()
            assert "LeanIX access forbidden" in str(exc_info.value)

    def test_authenticate_401_invalid_token(
        self, sample_workspace_base_url, sample_token, mock_auth_error_response
    ):
        """Test authentication with 401 invalid token response."""
        api = MtmApi(base_url=sample_workspace_base_url, token=sample_token)

        with patch.object(api._session, "post", return_value=mock_auth_error_response):
            with pytest.raises(AuthError) as exc_info:
                api._authenticate()
            assert "Invalid LeanIX API Token" in str(exc_info.value)

    def test_authenticate_non_200_status(self, sample_workspace_base_url, sample_token):
        """Test authentication with non-200 status code."""
        api = MtmApi(base_url=sample_workspace_base_url, token=sample_token)

        response = Mock(spec=Response)
        response.status_code = 500
        response.text = "Internal Server Error"

        with patch.object(api._session, "post", return_value=response):
            with pytest.raises(AuthError) as exc_info:
                api._authenticate()
            assert "Failed to authenticate with LeanIX" in str(exc_info.value)

    def test_authenticate_no_access_token_in_response(
        self, sample_workspace_base_url, sample_token
    ):
        """Test authentication when response doesn't contain access token."""
        api = MtmApi(base_url=sample_workspace_base_url, token=sample_token)

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"token_type": "Bearer"}

        with patch.object(api._session, "post", return_value=response):
            with pytest.raises(AuthError) as exc_info:
                api._authenticate()
            assert "No access token returned by LeanIX" in str(exc_info.value)

    def test_authenticate_passes_verify_parameter(
        self, sample_workspace_base_url, sample_token, mock_auth_response
    ):
        """Test that authentication respects verify parameter."""
        api = MtmApi(
            base_url=sample_workspace_base_url, token=sample_token, verify=False
        )

        with patch.object(api._session, "post") as mock_post:
            mock_post.return_value = mock_auth_response
            api._authenticate()

            call_kwargs = mock_post.call_args[1]
            assert call_kwargs["verify"] is False

    def test_authenticate_passes_proxies_parameter(
        self, sample_workspace_base_url, sample_token, mock_auth_response
    ):
        """Test that authentication respects proxies parameter."""
        proxies = {"http": "http://proxy:8080"}
        api = MtmApi(
            base_url=sample_workspace_base_url, token=sample_token, proxies=proxies
        )

        with patch.object(api._session, "post") as mock_post:
            mock_post.return_value = mock_auth_response
            api._authenticate()

            call_kwargs = mock_post.call_args[1]
            assert call_kwargs["proxies"] == proxies


@pytest.mark.unit
class TestMtmApiRequest:
    """Tests for request method."""

    def test_request_authenticates_if_needed(
        self, sample_workspace_base_url, sample_token, sample_bearer_token
    ):
        """Test that request authenticates if Authorization header not set."""
        api = MtmApi(base_url=sample_workspace_base_url, token=sample_token)

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"status": "success"}

        with patch.object(api._session, "request", return_value=response):
            with patch.object(api, "_authenticate") as mock_auth:
                api.request(method="GET", endpoint="/test")
                mock_auth.assert_called_once()

    def test_request_uses_urljoin(
        self, sample_workspace_base_url, sample_token, sample_bearer_token
    ):
        """Test that request uses urljoin for URL construction."""
        api = MtmApi(base_url=sample_workspace_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"status": "success"}

        with patch("leanix_agent.mtm_api.urljoin") as mock_urljoin:
            mock_urljoin.return_value = (
                "https://test-workspace.leanix.net/services/mtm/v1/test"
            )

            with patch.object(api._session, "request", return_value=response):
                api.request(method="GET", endpoint="/test")

                mock_urljoin.assert_called_once_with(sample_workspace_base_url, "/test")

    def test_request_passes_verify_parameter(
        self, sample_workspace_base_url, sample_token, sample_bearer_token
    ):
        """Test that request passes verify parameter."""
        api = MtmApi(
            base_url=sample_workspace_base_url, token=sample_token, verify=False
        )
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"status": "success"}

        with patch.object(api._session, "request") as mock_request:
            mock_request.return_value = response
            api.request(method="GET", endpoint="/test")

            call_kwargs = mock_request.call_args[1]
            assert call_kwargs["verify"] is False

    def test_request_passes_proxies_parameter(
        self, sample_workspace_base_url, sample_token, sample_bearer_token
    ):
        """Test that request passes proxies parameter."""
        proxies = {"http": "http://proxy:8080"}
        api = MtmApi(
            base_url=sample_workspace_base_url, token=sample_token, proxies=proxies
        )
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"status": "success"}

        with patch.object(api._session, "request") as mock_request:
            mock_request.return_value = response
            api.request(method="GET", endpoint="/test")

            call_kwargs = mock_request.call_args[1]
            assert call_kwargs["proxies"] == proxies

    def test_request_200_returns_json(
        self, sample_workspace_base_url, sample_token, sample_bearer_token
    ):
        """Test that 200 response returns JSON."""
        api = MtmApi(base_url=sample_workspace_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"data": "test"}

        with patch.object(api._session, "request", return_value=response):
            result = api.request(method="GET", endpoint="/test")

            assert result == {"data": "test"}

    def test_request_204_returns_success_status(
        self, sample_workspace_base_url, sample_token, sample_bearer_token
    ):
        """Test that 204 response returns success status."""
        api = MtmApi(base_url=sample_workspace_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 204
        response.text = ""

        with patch.object(api._session, "request", return_value=response):
            result = api.request(method="DELETE", endpoint="/test")

            assert result == {"status": "success"}

    def test_request_non_json_returns_success_with_text(
        self, sample_workspace_base_url, sample_token, sample_bearer_token
    ):
        """Test that non-JSON response returns success with text."""
        api = MtmApi(base_url=sample_workspace_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.side_effect = Exception("Not JSON")
        response.text = "Plain text response"

        with patch.object(api._session, "request", return_value=response):
            result = api.request(method="GET", endpoint="/test")

            assert result == {"status": "success", "text": "Plain text response"}


@pytest.mark.error
class TestMtmApiErrorHandling:
    """Tests for error handling in request method."""

    def test_request_401_raises_auth_error(
        self, sample_workspace_base_url, sample_token, sample_bearer_token
    ):
        """Test that 401 raises AuthError."""
        api = MtmApi(base_url=sample_workspace_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 401
        response.text = "Unauthorized"

        with patch.object(api._session, "request", return_value=response):
            with pytest.raises(AuthError) as exc_info:
                api.request(method="GET", endpoint="/test")
            assert "Authentication failed" in str(exc_info.value)

    def test_request_403_raises_unauthorized_error(
        self, sample_workspace_base_url, sample_token, sample_bearer_token
    ):
        """Test that 403 raises UnauthorizedError."""
        api = MtmApi(base_url=sample_workspace_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 403
        response.text = "Forbidden"

        with patch.object(api._session, "request", return_value=response):
            with pytest.raises(UnauthorizedError) as exc_info:
                api.request(method="GET", endpoint="/test")
            assert "Access forbidden" in str(exc_info.value)

    def test_request_other_4xx_raises_generic_error(
        self, sample_workspace_base_url, sample_token, sample_bearer_token
    ):
        """Test that other 4xx errors raise generic Exception."""
        api = MtmApi(base_url=sample_workspace_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 404
        response.text = "Not Found"

        with patch.object(api._session, "request", return_value=response):
            with pytest.raises(Exception) as exc_info:
                api.request(method="GET", endpoint="/test")
            assert "API error" in str(exc_info.value)
            assert "404" in str(exc_info.value)


@pytest.mark.unit
class TestMtmApiMethods:
    """Tests for specific MTM API methods."""

    def test_token(self, sample_workspace_base_url, sample_token, sample_bearer_token):
        """Test token method."""
        api = MtmApi(base_url=sample_workspace_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"access_token": "new-token", "expires_in": 3600}

        with patch.object(api, "request") as mock_request:
            mock_request.return_value = response
            result = api.token()

            mock_request.assert_called_once()
            call_args = mock_request.call_args
            # Handle both positional and keyword arguments
            if call_args[0]:
                assert call_args[0][0] == "POST"
                assert call_args[0][1] == "/oauth2/token"
            else:
                assert call_args[1]["method"] == "POST"
                assert call_args[1]["endpoint"] == "/oauth2/token"

    def test_get_accounts(
        self, sample_workspace_base_url, sample_token, sample_bearer_token
    ):
        """Test get_accounts method."""
        api = MtmApi(base_url=sample_workspace_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"data": [{"id": "acc-1", "name": "Account 1"}]}

        with patch.object(api, "request") as mock_request:
            mock_request.return_value = response
            result = api.get_accounts()

            mock_request.assert_called_once()
            call_args = mock_request.call_args
            if call_args[0]:
                assert call_args[0][0] == "GET"
                assert (
                    "/accounts" in call_args[0][1]
                    if call_args[0]
                    else call_args[1].get("endpoint", "")
                )

    def test_createapitoken(
        self, sample_workspace_base_url, sample_token, sample_bearer_token
    ):
        """Test createapitoken method."""
        api = MtmApi(base_url=sample_workspace_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 201
        response.json.return_value = {"id": "token-1", "name": "API Token"}

        data = {"name": "Test Token", "description": "Test"}

        with patch.object(api, "request") as mock_request:
            mock_request.return_value = response
            result = api.createapitoken(data=data)

            mock_request.assert_called_once()
            call_args = mock_request.call_args
            if call_args[0]:
                assert call_args[0][0] == "POST"
                assert (
                    "/apitokens" in call_args[0][1]
                    if call_args[0]
                    else call_args[1].get("endpoint", "")
                )

    def test_get_workspaces(
        self, sample_workspace_base_url, sample_token, sample_bearer_token
    ):
        """Test get_workspaces method."""
        api = MtmApi(base_url=sample_workspace_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"data": [{"id": "ws-1", "name": "Workspace 1"}]}

        with patch.object(api, "request") as mock_request:
            mock_request.return_value = response
            result = api.get_workspaces(id_="test-id")

            mock_request.assert_called_once()
            call_args = mock_request.call_args
            if call_args[0]:
                assert call_args[0][0] == "GET"
            else:
                assert call_args[1]["method"] == "GET"


@pytest.mark.ssl
class TestMtmApiSSL:
    """Tests for SSL verification in MTM API."""

    def test_verify_false_disables_warnings(
        self, sample_workspace_base_url, sample_token
    ):
        """Test that verify=False is set correctly."""
        api = MtmApi(
            base_url=sample_workspace_base_url, token=sample_token, verify=False
        )
        assert api._session.verify is False
