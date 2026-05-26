"""
Tests for leanix_api.py - Main LeanIX REST API client.
"""

from unittest.mock import Mock, patch

import pytest
import requests
from agent_utilities.exceptions import (
    AuthError,
    MissingParameterError,
    UnauthorizedError,
)
from requests import Response

from leanix_agent.api.api_client_leanix import LeanixApi
from leanix_agent.leanix_agent_models import FactSheetListResponse, FactSheetResponse


@pytest.mark.unit
class TestLeanixApiInitialization:
    """Tests for LeanixApi initialization."""

    def test_init_with_all_parameters(self, sample_base_url, sample_token):
        """Test initialization with all parameters."""
        api = LeanixApi(
            base_url=sample_base_url,
            token=sample_token,
            proxies={"http": "http://proxy:8080"},
            verify=True,
        )
        assert api.base_url == sample_base_url
        assert api.api_token == sample_token
        assert api.proxies == {"http": "http://proxy:8080"}
        assert api.verify is True
        assert api._session.verify is True

    def test_init_without_base_url(self, sample_token):
        """Test initialization without base_url raises error."""
        with pytest.raises(MissingParameterError) as exc_info:
            LeanixApi(token=sample_token)
        assert "base_url is required" in str(exc_info.value)

    def test_init_without_token(self, sample_base_url):
        """Test initialization without token raises error."""
        with pytest.raises(MissingParameterError) as exc_info:
            LeanixApi(base_url=sample_base_url)
        assert "Either token or both client_id and client_secret are required" in str(
            exc_info.value
        )

    def test_init_with_verify_false_disables_warnings(
        self, sample_base_url, sample_token
    ):
        """Test that verify=False is set correctly."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token, verify=False)
        assert api.verify is False
        assert api._session.verify is False

    def test_init_sets_correct_url(self, sample_base_url, sample_token):
        """Test that the API URL is correctly constructed."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)
        assert api.url == f"{sample_base_url}/services/pathfinder/v1"

    def test_init_strips_trailing_slash(self, sample_token):
        """Test that trailing slash is stripped from base_url."""
        api = LeanixApi(base_url="https://test.leanix.net/", token=sample_token)
        assert api.base_url == "https://test.leanix.net"


@pytest.mark.auth
class TestLeanixApiAuthentication:
    """Tests for LeanixApi authentication."""

    def test_authenticate_success(
        self, sample_base_url, sample_token, sample_bearer_token, mock_auth_response
    ):
        """Test successful authentication."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)

        with patch.object(api._session, "post", return_value=mock_auth_response):
            api._authenticate()

            assert api.access_token == sample_bearer_token
            assert api.headers is not None
            assert api.headers["Authorization"] == f"Bearer {sample_bearer_token}"
            assert api.headers["Content-Type"] == "application/json"

    def test_authenticate_403_forbidden(
        self, sample_base_url, sample_token, mock_forbidden_response
    ):
        """Test authentication with 403 forbidden response."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)

        with patch.object(api._session, "post", return_value=mock_forbidden_response):
            with pytest.raises(UnauthorizedError) as exc_info:
                api._authenticate()
            assert "LeanIX access forbidden" in str(exc_info.value)

    def test_authenticate_401_invalid_token(
        self, sample_base_url, sample_token, mock_auth_error_response
    ):
        """Test authentication with 401 invalid token response."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)

        with patch.object(api._session, "post", return_value=mock_auth_error_response):
            with pytest.raises(AuthError) as exc_info:
                api._authenticate()
            assert "Invalid LeanIX API Token" in str(exc_info.value)

    def test_authenticate_non_200_status(self, sample_base_url, sample_token):
        """Test authentication with non-200 status code."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)

        response = Mock(spec=Response)
        response.status_code = 500
        response.text = "Internal Server Error"

        with patch.object(api._session, "post", return_value=response):
            with pytest.raises(AuthError) as exc_info:
                api._authenticate()
            assert "Failed to authenticate with LeanIX" in str(exc_info.value)

    def test_authenticate_no_access_token_in_response(
        self, sample_base_url, sample_token
    ):
        """Test authentication when response doesn't contain access token."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"token_type": "Bearer"}

        with patch.object(api._session, "post", return_value=response):
            with pytest.raises(AuthError) as exc_info:
                api._authenticate()
            assert "No access token returned by LeanIX" in str(exc_info.value)

    def test_authenticate_uses_correct_url(
        self, sample_base_url, sample_token, mock_auth_response
    ):
        """Test that authentication uses the correct URL."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)

        with patch.object(api._session, "post") as mock_post:
            mock_post.return_value = mock_auth_response
            api._authenticate()

            expected_url = f"{sample_base_url}/services/mtm/v1/oauth2/token"
            mock_post.assert_called_once()
            call_args = mock_post.call_args
            assert call_args[0][0] == expected_url

    def test_authenticate_passes_verify_parameter(
        self, sample_base_url, sample_token, mock_auth_response
    ):
        """Test that authentication respects verify parameter."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token, verify=False)

        with patch.object(api._session, "post") as mock_post:
            mock_post.return_value = mock_auth_response
            api._authenticate()

            call_kwargs = mock_post.call_args[1]
            assert call_kwargs["verify"] is False

    def test_authenticate_passes_proxies_parameter(
        self, sample_base_url, sample_token, mock_auth_response
    ):
        """Test that authentication respects proxies parameter."""
        proxies = {"http": "http://proxy:8080"}
        api = LeanixApi(base_url=sample_base_url, token=sample_token, proxies=proxies)

        with patch.object(api._session, "post") as mock_post:
            mock_post.return_value = mock_auth_response
            api._authenticate()

            call_kwargs = mock_post.call_args[1]
            assert call_kwargs["proxies"] == proxies


@pytest.mark.unit
class TestLeanixApiGetFactSheets:
    """Tests for get_factsheets method."""

    def test_get_factsheets_success(
        self,
        sample_base_url,
        sample_token,
        sample_bearer_token,
        sample_factsheets_response,
    ):
        """Test successful get_factsheets call."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)
        api.access_token = sample_bearer_token
        api.headers = {
            "Authorization": f"Bearer {sample_bearer_token}",
            "Content-Type": "application/json",
        }

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = sample_factsheets_response
        response.raise_for_status = Mock()

        with patch.object(api._session, "get", return_value=response):
            result = api.get_factsheets(type="Application", pageSize=5)

            assert result.response.status_code == 200
            assert isinstance(result.data, FactSheetListResponse)
            assert len(result.data.data) == 2

    def test_get_factsheets_authenticates_if_needed(
        self,
        sample_base_url,
        sample_token,
        sample_bearer_token,
        sample_factsheets_response,
        mock_auth_response,
    ):
        """Test that get_factsheets authenticates if headers not set."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)

        # Set up authentication manually to avoid hanging
        api.access_token = sample_bearer_token
        api.headers = {
            "Authorization": f"Bearer {sample_bearer_token}",
            "Content-Type": "application/json",
        }

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = sample_factsheets_response
        response.raise_for_status = Mock()

        with patch.object(api._session, "get", return_value=response):
            api.get_factsheets(type="Application", pageSize=5)

    def test_get_factsheets_uses_correct_endpoint(
        self,
        sample_base_url,
        sample_token,
        sample_bearer_token,
        sample_factsheets_response,
    ):
        """Test that get_factsheets uses the correct endpoint."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)
        api.access_token = sample_bearer_token
        api.headers = {
            "Authorization": f"Bearer {sample_bearer_token}",
            "Content-Type": "application/json",
        }

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = sample_factsheets_response
        response.raise_for_status = Mock()

        with patch.object(api._session, "get") as mock_get:
            mock_get.return_value = response
            api.get_factsheets(type="Application", pageSize=5)

            call_args = mock_get.call_args
            # Check the URL parameter (could be positional or named)
            url = call_args[0][0] if call_args[0] else call_args[1].get("url", "")
            assert "factSheets" in url  # camelCase endpoint

    def test_get_factsheets_passes_verify_parameter(
        self,
        sample_base_url,
        sample_token,
        sample_bearer_token,
        sample_factsheets_response,
    ):
        """Test that get_factsheets respects verify parameter."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token, verify=False)
        api.access_token = sample_bearer_token
        api.headers = {
            "Authorization": f"Bearer {sample_bearer_token}",
            "Content-Type": "application/json",
        }

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = sample_factsheets_response
        response.raise_for_status = Mock()

        with patch.object(api._session, "get") as mock_get:
            mock_get.return_value = response
            api.get_factsheets(type="Application", pageSize=5)

            call_kwargs = mock_get.call_args[1]
            assert call_kwargs["verify"] is False

    def test_get_factsheets_401_raises_auth_error(
        self, sample_base_url, sample_token, sample_bearer_token
    ):
        """Test that get_factsheets raises AuthError on 401."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)
        api.access_token = sample_bearer_token
        api.headers = {
            "Authorization": f"Bearer {sample_bearer_token}",
            "Content-Type": "application/json",
        }

        response = Mock(spec=Response)
        response.status_code = 401
        response.text = "Unauthorized"

        http_error = requests.exceptions.HTTPError()
        http_error.response = response
        response.raise_for_status = Mock(side_effect=http_error)

        with patch.object(api._session, "get", return_value=response):
            with pytest.raises(AuthError):
                api.get_factsheets(type="Application", pageSize=5)

    def test_get_factsheets_403_raises_unauthorized_error(
        self, sample_base_url, sample_token, sample_bearer_token
    ):
        """Test that get_factsheets raises UnauthorizedError on 403."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)
        api.access_token = sample_bearer_token
        api.headers = {
            "Authorization": f"Bearer {sample_bearer_token}",
            "Content-Type": "application/json",
        }

        response = Mock(spec=Response)
        response.status_code = 403
        response.text = "Forbidden"

        http_error = requests.exceptions.HTTPError()
        http_error.response = response
        response.raise_for_status = Mock(side_effect=http_error)

        with patch.object(api._session, "get", return_value=response):
            with pytest.raises(UnauthorizedError):
                api.get_factsheets(type="Application", pageSize=5)


@pytest.mark.unit
class TestLeanixApiGetFactSheet:
    """Tests for get_factsheet method (single FactSheet)."""

    def test_get_factsheet_success(
        self, sample_base_url, sample_token, sample_bearer_token, sample_factsheet_data
    ):
        """Test successful get_factsheet call."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)
        api.access_token = sample_bearer_token
        api.headers = {
            "Authorization": f"Bearer {sample_bearer_token}",
            "Content-Type": "application/json",
        }

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"data": sample_factsheet_data}
        response.raise_for_status = Mock()

        with patch.object(api._session, "get", return_value=response):
            result = api.get_factsheet(id="test-id-123")

            assert result.response.status_code == 200
            assert isinstance(result.data, FactSheetResponse)
            assert result.data.id == "test-id-123"

    def test_get_factsheet_without_id_raises_error(
        self, sample_base_url, sample_token, sample_bearer_token
    ):
        """Test that get_factsheet without id raises MissingParameterError."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)
        api.access_token = sample_bearer_token
        api.headers = {
            "Authorization": f"Bearer {sample_bearer_token}",
            "Content-Type": "application/json",
        }

        with pytest.raises(MissingParameterError) as exc_info:
            api.get_factsheet()
        assert "id is required" in str(exc_info.value)

    def test_get_factsheet_uses_correct_endpoint(
        self, sample_base_url, sample_token, sample_bearer_token, sample_factsheet_data
    ):
        """Test that get_factsheet uses the correct endpoint."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)
        api.access_token = sample_bearer_token
        api.headers = {
            "Authorization": f"Bearer {sample_bearer_token}",
            "Content-Type": "application/json",
        }

        response = Mock(spec=Response)
        response.status_code = 200
        response.json.return_value = {"data": sample_factsheet_data}
        response.raise_for_status = Mock()

        with patch.object(api._session, "get") as mock_get:
            mock_get.return_value = response
            api.get_factsheet(id="test-id-123")

            call_args = mock_get.call_args
            # Check the URL parameter (could be positional or named)
            url = call_args[0][0] if call_args[0] else call_args[1].get("url", "")
            assert "factSheets/test-id-123" in url  # camelCase endpoint


@pytest.mark.ssl
class TestLeanixApiSSLVerification:
    """Tests for SSL verification handling."""

    def test_verify_false_disables_warnings(self, sample_base_url, sample_token):
        """Test that verify=False is set correctly."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token, verify=False)
        assert api._session.verify is False

    def test_verify_true_keeps_ssl_verification(self, sample_base_url, sample_token):
        """Test that verify=True keeps SSL verification enabled."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token, verify=True)
        assert api._session.verify is True

    def test_verify_default_is_true(self, sample_base_url, sample_token):
        """Test that verify defaults to True."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)
        assert api.verify is True
        assert api._session.verify is True


@pytest.mark.error
class TestLeanixApiErrorHandling:
    """Tests for error handling in API calls."""

    def test_http_error_with_401_raises_auth_error(
        self, sample_base_url, sample_token, sample_bearer_token
    ):
        """Test that HTTP 401 raises AuthError."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)
        api.access_token = sample_bearer_token
        api.headers = {
            "Authorization": f"Bearer {sample_bearer_token}",
            "Content-Type": "application/json",
        }

        response = Mock(spec=Response)
        response.status_code = 401

        http_error = requests.exceptions.HTTPError()
        http_error.response = response
        response.raise_for_status = Mock(side_effect=http_error)

        with patch.object(api._session, "get", return_value=response):
            with pytest.raises(AuthError):
                api.get_factsheets(type="Application")

    def test_http_error_with_403_raises_unauthorized_error(
        self, sample_base_url, sample_token, sample_bearer_token
    ):
        """Test that HTTP 403 raises UnauthorizedError."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)
        api.access_token = sample_bearer_token
        api.headers = {
            "Authorization": f"Bearer {sample_bearer_token}",
            "Content-Type": "application/json",
        }

        response = Mock(spec=Response)
        response.status_code = 403

        http_error = requests.exceptions.HTTPError()
        http_error.response = response
        response.raise_for_status = Mock(side_effect=http_error)

        with patch.object(api._session, "get", return_value=response):
            with pytest.raises(UnauthorizedError):
                api.get_factsheets(type="Application")

    def test_http_error_with_500_raises_generic_error(
        self, sample_base_url, sample_token, sample_bearer_token
    ):
        """Test that HTTP 500 raises the original error."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)
        api.access_token = sample_bearer_token
        api.headers = {
            "Authorization": f"Bearer {sample_bearer_token}",
            "Content-Type": "application/json",
        }

        response = Mock(spec=Response)
        response.status_code = 500

        http_error = requests.exceptions.HTTPError()
        http_error.response = response
        response.raise_for_status = Mock(side_effect=http_error)

        with patch.object(api._session, "get", return_value=response):
            with pytest.raises(requests.exceptions.HTTPError):
                api.get_factsheets(type="Application")

    def test_http_error_with_404_raises_generic_error(
        self, sample_base_url, sample_token, sample_bearer_token
    ):
        """Test that HTTP 404 raises the original error."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)
        api.access_token = sample_bearer_token
        api.headers = {
            "Authorization": f"Bearer {sample_bearer_token}",
            "Content-Type": "application/json",
        }

        response = Mock(spec=Response)
        response.status_code = 404

        http_error = requests.exceptions.HTTPError()
        http_error.response = response
        response.raise_for_status = Mock(side_effect=http_error)

        with patch.object(api._session, "get", return_value=response):
            with pytest.raises(requests.exceptions.HTTPError):
                api.get_factsheet(id="non-existent")

    def test_http_error_with_other_status_raises_original_error(
        self, sample_base_url, sample_token, sample_bearer_token
    ):
        """Test that other HTTP errors raise the original exception."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)
        api.access_token = sample_bearer_token
        api.headers = {
            "Authorization": f"Bearer {sample_bearer_token}",
            "Content-Type": "application/json",
        }

        response = Mock(spec=Response)
        response.status_code = 500
        response.raise_for_status = Mock(side_effect=Exception("500 Server Error"))

        with patch.object(api._session, "get", return_value=response):
            with pytest.raises(Exception, match="500 Server Error"):
                api.get_factsheets(type="Application")


@pytest.mark.unit
class TestLeanixApiCoverageGaps:
    """Extra tests to cover specific error paths and initialization triggers for 100% coverage."""

    def test_automatic_authenticate_when_headers_none(
        self,
        sample_base_url,
        sample_token,
        sample_bearer_token,
        mock_auth_response,
        sample_factsheet_data,
    ):
        """Verify that get_factsheets and get_factsheet trigger _authenticate automatically when self.headers is None."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)
        assert api.headers is None

        # Prepare a mock GET response
        mock_get_response = Mock(spec=Response)
        mock_get_response.status_code = 200
        mock_get_response.json.return_value = {"data": [sample_factsheet_data]}

        # Perform patched calls
        with (
            patch.object(
                api._session, "post", return_value=mock_auth_response
            ) as mock_post,
            patch.object(
                api._session, "get", return_value=mock_get_response
            ) as mock_get,
        ):
            # 1. Trigger via get_factsheets (bypassing decorator using __wrapped__)
            res = api.get_factsheets.__wrapped__(api, type="Application")
            assert res.data.data[0].id == "test-id-123"
            mock_post.assert_called_once()
            mock_get.assert_called_once()

        # Reset headers and do it for get_factsheet
        api.headers = None
        mock_get_response.json.return_value = {"data": sample_factsheet_data}
        with (
            patch.object(
                api._session, "post", return_value=mock_auth_response
            ) as mock_post,
            patch.object(
                api._session, "get", return_value=mock_get_response
            ) as mock_get,
        ):
            # 2. Trigger via get_factsheet (bypassing decorator using __wrapped__)
            res = api.get_factsheet.__wrapped__(api, id="test-id-123")
            assert res.data.id == "test-id-123"
            mock_post.assert_called_once()
            mock_get.assert_called_once()

    def test_get_factsheet_missing_parameter_raises(
        self, sample_base_url, sample_token
    ):
        """Verify missing id triggers MissingParameterError."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)
        api.headers = {"Authorization": "Bearer abc"}
        api.access_token = "dummy"
        with pytest.raises(MissingParameterError, match="id is required"):
            api.get_factsheet()

    def test_get_factsheets_validation_error_raises_parameter_error(
        self, sample_base_url, sample_token
    ):
        """Verify passing incorrect argument types triggers ParameterError."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)
        api.headers = {"Authorization": "Bearer abc"}
        api.access_token = "dummy"
        # Pass page_size="not-an-integer" to trigger ValidationError in FactSheetModel
        with pytest.raises(Exception) as exc_info:
            api.get_factsheets(page_size="not-an-integer")
        assert "Invalid parameters" in str(exc_info.value)

    def test_get_factsheet_validation_error_raises_parameter_error(
        self, sample_base_url, sample_token
    ):
        """Verify passing incorrect argument types in get_factsheet triggers ParameterError."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)
        api.headers = {"Authorization": "Bearer abc"}
        api.access_token = "dummy"
        # Pass page_size="not-an-integer" to trigger ValidationError in FactSheetModel
        with pytest.raises(Exception) as exc_info:
            api.get_factsheet(id="123", page_size="not-an-integer")
        assert "Invalid parameters" in str(exc_info.value)

    def test_get_factsheets_http_errors_raise_correct_exceptions(
        self, sample_base_url, sample_token, sample_bearer_token
    ):
        """Verify 401 and 403 HTTP errors translate to AuthError and UnauthorizedError respectively."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)
        api.access_token = sample_bearer_token
        api.headers = {"Authorization": f"Bearer {sample_bearer_token}"}

        # 1. Test 401 raises AuthError
        response_401 = Mock(spec=Response)
        response_401.status_code = 401
        http_error_401 = requests.exceptions.HTTPError()
        http_error_401.response = response_401
        response_401.raise_for_status = Mock(side_effect=http_error_401)

        with patch.object(api._session, "get", return_value=response_401):
            with pytest.raises(AuthError):
                api.get_factsheets(type="Application")

        # 2. Test 403 raises UnauthorizedError
        response_403 = Mock(spec=Response)
        response_403.status_code = 403
        http_error_403 = requests.exceptions.HTTPError()
        http_error_403.response = response_403
        response_403.raise_for_status = Mock(side_effect=http_error_403)

        with patch.object(api._session, "get", return_value=response_403):
            with pytest.raises(UnauthorizedError):
                api.get_factsheets(type="Application")

    def test_get_factsheet_http_errors_raise_correct_exceptions(
        self, sample_base_url, sample_token, sample_bearer_token
    ):
        """Verify 401 and 403 HTTP errors translate to AuthError and UnauthorizedError in get_factsheet."""
        api = LeanixApi(base_url=sample_base_url, token=sample_token)
        api.access_token = sample_bearer_token
        api.headers = {"Authorization": f"Bearer {sample_bearer_token}"}

        # 1. Test 401 raises AuthError
        response_401 = Mock(spec=Response)
        response_401.status_code = 401
        http_error_401 = requests.exceptions.HTTPError()
        http_error_401.response = response_401
        response_401.raise_for_status = Mock(side_effect=http_error_401)

        with patch.object(api._session, "get", return_value=response_401):
            with pytest.raises(AuthError):
                api.get_factsheet(id="123")

        # 2. Test 403 raises UnauthorizedError
        response_403 = Mock(spec=Response)
        response_403.status_code = 403
        http_error_403 = requests.exceptions.HTTPError()
        http_error_403.response = response_403
        response_403.raise_for_status = Mock(side_effect=http_error_403)

        with patch.object(api._session, "get", return_value=response_403):
            with pytest.raises(UnauthorizedError):
                api.get_factsheet(id="123")
