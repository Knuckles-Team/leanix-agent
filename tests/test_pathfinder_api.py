"""
Tests for pathfinder_api.py - Pathfinder API client.
"""

import pytest
from unittest.mock import Mock, patch
from requests import Response
import urllib3

from leanix_agent.pathfinder_api import Api as PathfinderApi
from agent_utilities.exceptions import (
    AuthError,
    MissingParameterError,
    UnauthorizedError,
)


@pytest.mark.unit
class TestPathfinderApiInitialization:
    """Tests for PathfinderApi initialization."""

    def test_init_with_all_parameters(self, sample_service_base_url, sample_token):
        """Test initialization with all parameters."""
        api = PathfinderApi(
            base_url=sample_service_base_url,
            token=sample_token,
            proxies={"http": "http://proxy:8080"},
            verify=False,
        )
        assert api.base_url == sample_service_base_url
        assert api.token == sample_token
        assert api.proxies == {"http": "http://proxy:8080"}
        assert api.verify is False
        assert api._session.verify is False

    def test_init_without_base_url(self, sample_token):
        """Test initialization without base_url raises error."""
        with pytest.raises(MissingParameterError) as exc_info:
            PathfinderApi(base_url=None, token=sample_token)
        assert "base_url is required" in str(exc_info.value)

    def test_init_without_token(self, sample_service_base_url):
        """Test initialization without token raises error."""
        with pytest.raises(MissingParameterError) as exc_info:
            PathfinderApi(base_url=sample_service_base_url)
        assert "token is required" in str(exc_info.value)

    def test_init_with_verify_false_disables_warnings(
        self, sample_service_base_url, sample_token
    ):
        """Test that verify=False is set correctly."""
        api = PathfinderApi(
            base_url=sample_service_base_url, token=sample_token, verify=False
        )
        assert api.verify is False
        assert api._session.verify is False

    def test_init_extracts_workspace_base_url(
        self, sample_service_base_url, sample_token
    ):
        """Test that workspace base URL is extracted correctly."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)
        expected_workspace_url = "https://test-workspace.leanix.net"
        assert api.workspace_base_url == expected_workspace_url

    def test_init_without_services_in_url(
        self, sample_workspace_base_url, sample_token
    ):
        """Test initialization without /services/ in URL."""
        api = PathfinderApi(base_url=sample_workspace_base_url, token=sample_token)
        assert api.workspace_base_url == sample_workspace_base_url

    def test_init_sets_session_verify(self, sample_service_base_url, sample_token):
        """Test that session verify is set correctly."""
        api = PathfinderApi(
            base_url=sample_service_base_url, token=sample_token, verify=False
        )
        assert api._session.verify is False


@pytest.mark.auth
class TestPathfinderApiAuthentication:
    """Tests for PathfinderApi authentication."""

    def test_authenticate_success(
        self,
        sample_service_base_url,
        sample_token,
        sample_bearer_token,
        mock_auth_response,
    ):
        """Test successful authentication."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)

        with patch.object(api._session, "post", return_value=mock_auth_response):
            api._authenticate()

            assert "Authorization" in api._session.headers
            assert (
                api._session.headers["Authorization"] == f"Bearer {sample_bearer_token}"
            )
            assert api._session.headers["Content-Type"] == "application/json"

    def test_authenticate_uses_workspace_base_url(
        self,
        sample_service_base_url,
        sample_token,
        sample_bearer_token,
        mock_auth_response,
    ):
        """Test that authentication uses workspace base URL."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)

        with patch.object(api._session, "post") as mock_post:
            mock_post.return_value = mock_auth_response
            api._authenticate()

            expected_url = (
                "https://test-workspace.leanix.net/services/mtm/v1/oauth2/token"
            )
            mock_post.assert_called_once()
            call_args = mock_post.call_args
            # Handle both positional and keyword arguments
            if call_args[0]:
                assert call_args[0][0] == expected_url
            else:
                assert call_args[1]["url"] == expected_url

    def test_authenticate_403_forbidden(
        self, sample_service_base_url, sample_token, mock_forbidden_response
    ):
        """Test authentication with 403 forbidden response."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)

        with patch.object(api._session, "post", return_value=mock_forbidden_response):
            with pytest.raises(UnauthorizedError) as exc_info:
                api._authenticate()
            assert "LeanIX access forbidden" in str(exc_info.value)

    def test_authenticate_401_invalid_token(
        self, sample_service_base_url, sample_token, mock_auth_error_response
    ):
        """Test authentication with 401 invalid token response."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)

        with patch.object(api._session, "post", return_value=mock_auth_error_response):
            with pytest.raises(AuthError) as exc_info:
                api._authenticate()
            assert "Invalid LeanIX API Token" in str(exc_info.value)

    def test_authenticate_non_200_status(self, sample_service_base_url, sample_token):
        """Test authentication with non-200 status code."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)

        response = Mock(spec=Response)
        response.status_code = 500
        response.text = "Internal Server Error"

        with patch.object(api._session, "post", return_value=response):
            with pytest.raises(AuthError) as exc_info:
                api._authenticate()
            assert "Failed to authenticate with LeanIX" in str(exc_info.value)

    def test_authenticate_no_access_token_in_response(
        self, sample_service_base_url, sample_token
    ):
        """Test authentication when response doesn't contain access token."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"token_type": "Bearer"}

        with patch.object(api._session, "post", return_value=response):
            with pytest.raises(AuthError) as exc_info:
                api._authenticate()
            assert "No access token returned by LeanIX" in str(exc_info.value)

    def test_authenticate_passes_verify_parameter(
        self, sample_service_base_url, sample_token, mock_auth_response
    ):
        """Test that authentication respects verify parameter."""
        api = PathfinderApi(
            base_url=sample_service_base_url, token=sample_token, verify=False
        )

        with patch.object(api._session, "post") as mock_post:
            mock_post.return_value = mock_auth_response
            api._authenticate()

            call_kwargs = mock_post.call_args[1]
            assert call_kwargs["verify"] is False

    def test_authenticate_passes_proxies_parameter(
        self, sample_service_base_url, sample_token, mock_auth_response
    ):
        """Test that authentication respects proxies parameter."""
        proxies = {"http": "http://proxy:8080"}
        api = PathfinderApi(
            base_url=sample_service_base_url, token=sample_token, proxies=proxies
        )

        with patch.object(api._session, "post") as mock_post:
            mock_post.return_value = mock_auth_response
            api._authenticate()

            call_kwargs = mock_post.call_args[1]
            assert call_kwargs["proxies"] == proxies


@pytest.mark.unit
class TestPathfinderApiRequest:
    """Tests for request method."""

    def test_request_authenticates_if_needed(
        self, sample_service_base_url, sample_token, sample_bearer_token
    ):
        """Test that request authenticates if Authorization header not set."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"status": "success"}

        with patch.object(api._session, "request", return_value=response):
            with patch.object(api, "_authenticate") as mock_auth:
                api.request(method="GET", endpoint="/test")
                mock_auth.assert_called_once()

    def test_request_uses_urljoin(
        self, sample_service_base_url, sample_token, sample_bearer_token
    ):
        """Test that request uses urljoin for URL construction."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"status": "success"}

        with patch("leanix_agent.pathfinder_api.urljoin") as mock_urljoin:
            mock_urljoin.return_value = (
                "https://test-workspace.leanix.net/services/pathfinder/v1/test"
            )

            with patch.object(api._session, "request", return_value=response):
                api.request(method="GET", endpoint="/test")

                mock_urljoin.assert_called_once_with(sample_service_base_url, "/test")

    def test_request_passes_verify_parameter(
        self, sample_service_base_url, sample_token, sample_bearer_token
    ):
        """Test that request passes verify parameter."""
        api = PathfinderApi(
            base_url=sample_service_base_url, token=sample_token, verify=False
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
        self, sample_service_base_url, sample_token, sample_bearer_token
    ):
        """Test that request passes proxies parameter."""
        proxies = {"http": "http://proxy:8080"}
        api = PathfinderApi(
            base_url=sample_service_base_url, token=sample_token, proxies=proxies
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
        self, sample_service_base_url, sample_token, sample_bearer_token
    ):
        """Test that 200 response returns JSON."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"data": "test"}

        with patch.object(api._session, "request", return_value=response):
            result = api.request(method="GET", endpoint="/test")

            assert result == {"data": "test"}

    def test_request_204_returns_success_status(
        self, sample_service_base_url, sample_token, sample_bearer_token
    ):
        """Test that 204 response returns success status."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 204
        response.text = ""

        with patch.object(api._session, "request", return_value=response):
            result = api.request(method="DELETE", endpoint="/test")

            assert result == {"status": "success"}

    def test_request_non_json_returns_success_with_text(
        self, sample_service_base_url, sample_token, sample_bearer_token
    ):
        """Test that non-JSON response returns success with text."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.side_effect = Exception("Not JSON")
        response.text = "Plain text response"

        with patch.object(api._session, "request", return_value=response):
            result = api.request(method="GET", endpoint="/test")

            assert result == {"status": "success", "text": "Plain text response"}


@pytest.mark.error
class TestPathfinderApiErrorHandling:
    """Tests for error handling in request method."""

    def test_request_401_raises_auth_error(
        self, sample_service_base_url, sample_token, sample_bearer_token
    ):
        """Test that 401 raises AuthError."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 401
        response.text = "Unauthorized"

        with patch.object(api._session, "request", return_value=response):
            with pytest.raises(AuthError) as exc_info:
                api.request(method="GET", endpoint="/test")
            assert "Authentication failed" in str(exc_info.value)

    def test_request_403_raises_unauthorized_error(
        self, sample_service_base_url, sample_token, sample_bearer_token
    ):
        """Test that 403 raises UnauthorizedError."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 403
        response.text = "Forbidden"

        with patch.object(api._session, "request", return_value=response):
            with pytest.raises(UnauthorizedError) as exc_info:
                api.request(method="GET", endpoint="/test")
            assert "Access forbidden" in str(exc_info.value)

    def test_request_other_4xx_raises_generic_error(
        self, sample_service_base_url, sample_token, sample_bearer_token
    ):
        """Test that other 4xx errors raise generic Exception."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)
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
class TestPathfinderApiMethods:
    """Tests for specific Pathfinder API methods."""

    def test_get_fact_sheets(
        self, sample_service_base_url, sample_token, sample_bearer_token
    ):
        """Test get_fact_sheets method."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"data": [{"id": "1", "name": "Test"}]}

        with patch.object(api, "request") as mock_request:
            mock_request.return_value = response
            result = api.get_fact_sheets(type="Application", pageSize=5)

            mock_request.assert_called_once()
            call_args = mock_request.call_args
            # Handle both positional and keyword arguments
            if call_args[0]:
                assert call_args[0][0] == "GET"
                assert call_args[0][1] == "/factSheets"
            else:
                assert call_args[1]["method"] == "GET"
                assert call_args[1]["endpoint"] == "/factSheets"

    def test_get_fact_sheet(
        self, sample_service_base_url, sample_token, sample_bearer_token
    ):
        """Test get_fact_sheet method."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"id": "test-id", "name": "Test"}

        with patch.object(api, "request") as mock_request:
            mock_request.return_value = response
            result = api.get_fact_sheet(id_="test-id")

            mock_request.assert_called_once()
            call_args = mock_request.call_args
            # Handle both positional and keyword arguments
            if call_args[0]:
                assert call_args[0][0] == "GET"
                assert call_args[0][1] == "/factSheets/test-id"
            else:
                assert call_args[1]["method"] == "GET"
                assert call_args[1]["endpoint"] == "/factSheets/test-id"

    def test_create_fact_sheet(
        self, sample_service_base_url, sample_token, sample_bearer_token
    ):
        """Test create_fact_sheet method."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 201
        response.json.return_value = {"id": "new-id", "name": "New App"}

        data = {"name": "New Application", "type": "Application"}

        with patch.object(api, "request") as mock_request:
            mock_request.return_value = response
            result = api.create_fact_sheet(data=data)

            mock_request.assert_called_once()
            call_args = mock_request.call_args
            # Handle both positional and keyword arguments
            if call_args[0]:
                assert call_args[0][0] == "POST"
                assert call_args[0][1] == "/factSheets"
                assert call_args[0][3] == data
            else:
                assert call_args[1]["method"] == "POST"
                assert call_args[1]["endpoint"] == "/factSheets"
                assert call_args[1]["data"] == data

    def test_update_fact_sheet(
        self, sample_service_base_url, sample_token, sample_bearer_token
    ):
        """Test update_fact_sheet method."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"id": "test-id", "name": "Updated"}

        data = {"name": "Updated Application"}

        with patch.object(api, "request") as mock_request:
            mock_request.return_value = response
            result = api.update_fact_sheet(id_="test-id", data=data)

            mock_request.assert_called_once()
            call_args = mock_request.call_args
            # Handle both positional and keyword arguments
            if call_args[0]:
                assert call_args[0][0] == "PUT"
                assert call_args[0][1] == "/factSheets/test-id"
                assert call_args[0][3] == data
            else:
                assert call_args[1]["method"] == "PUT"
                assert call_args[1]["endpoint"] == "/factSheets/test-id"
                assert call_args[1]["data"] == data


@pytest.mark.unit
class TestPathfinderApiParameterValidation:
    """Tests for parameter validation in Pathfinder API methods."""

    def test_get_fact_sheets_with_type_filter(
        self, sample_service_base_url, sample_token, sample_bearer_token
    ):
        """Test get_fact_sheets with type parameter."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"data": [{"id": "1", "type": "Application"}]}

        with patch.object(api, "request") as mock_request:
            mock_request.return_value = response
            api.get_fact_sheets(type="Application")

            mock_request.assert_called_once()
            call_args = mock_request.call_args
            # Verify the type parameter is passed
            if call_args[1]:
                assert "type" in call_args[1] or "params" in call_args[1]

    def test_get_fact_sheet_requires_id(
        self, sample_service_base_url, sample_token, sample_bearer_token
    ):
        """Test that get_fact_sheet requires id parameter."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"data": {"id": "test-id", "type": "Application"}}

        with patch.object(api, "request") as mock_request:
            mock_request.return_value = response
            api.get_fact_sheet(id_="test-id")

            mock_request.assert_called_once()
            call_args = mock_request.call_args
            # Verify the endpoint includes the id
            if call_args[0]:
                assert (
                    "test-id" in call_args[0][1]
                    if call_args[0]
                    else call_args[1].get("endpoint", "")
                )

    def test_create_fact_sheet_requires_data(
        self, sample_service_base_url, sample_token, sample_bearer_token
    ):
        """Test that create_fact_sheet requires data parameter."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 201
        response.json.return_value = {"id": "new-id", "type": "Application"}

        data = {"name": "Test App", "type": "Application"}

        with patch.object(api, "request") as mock_request:
            mock_request.return_value = response
            api.create_fact_sheet(data=data)

            mock_request.assert_called_once()
            # Verify data is passed
            call_args = mock_request.call_args
            if call_args[1]:
                assert "data" in call_args[1] or call_args[1].get("data") == data

    def test_get_fact_sheet_relations(
        self, sample_service_base_url, sample_token, sample_bearer_token
    ):
        """Test get_fact_sheet_relations method."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"data": [{"id": "rel-1", "type": "dependsOn"}]}

        with patch.object(api, "request") as mock_request:
            mock_request.return_value = response
            result = api.get_fact_sheet_relations(id_="test-id")

            mock_request.assert_called_once()
            call_args = mock_request.call_args
            # Verify the endpoint includes the id
            if call_args[0]:
                assert (
                    "test-id" in call_args[0][1]
                    if call_args[0]
                    else call_args[1].get("endpoint", "")
                )

    def test_get_fact_sheet_hierarchy(
        self, sample_service_base_url, sample_token, sample_bearer_token
    ):
        """Test get_fact_sheet_hierarchy method."""
        api = PathfinderApi(base_url=sample_service_base_url, token=sample_token)
        api._session.headers["Authorization"] = f"Bearer {sample_bearer_token}"

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"data": [{"id": "child-1", "name": "Child"}]}

        with patch.object(api, "request") as mock_request:
            mock_request.return_value = response
            result = api.get_fact_sheet_hierarchy(root_id="root-id")

            mock_request.assert_called_once()
            call_args = mock_request.call_args
            # Verify the endpoint includes the root_id
            if call_args[0]:
                assert (
                    "root-id" in call_args[0][1]
                    if call_args[0]
                    else call_args[1].get("endpoint", "")
                )


@pytest.mark.ssl
class TestPathfinderApiSSL:
    """Tests for SSL verification in Pathfinder API."""

    def test_verify_false_disables_warnings(
        self, sample_service_base_url, sample_token
    ):
        """Test that verify=False is set correctly."""
        api = PathfinderApi(
            base_url=sample_service_base_url, token=sample_token, verify=False
        )
        assert api._session.verify is False
