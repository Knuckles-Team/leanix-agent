"""
Tests for dynamically validating all generated API client modules under leanix_agent/api/.
"""

from typing import Any
import importlib
import inspect
import os
import pkgutil
import pytest
from unittest.mock import MagicMock, patch
import requests

import leanix_agent.api
from leanix_agent.api.api_client_leanix import LeanixApi


def get_all_api_modules():
    """Discover all api_client_* modules under leanix_agent.api."""
    modules = []
    package = leanix_agent.api
    for _, module_name, _ in pkgutil.walk_packages(
        package.__path__, package.__name__ + "."
    ):
        if "api_client_" in module_name:
            modules.append(module_name)
    return modules


@pytest.mark.parametrize("module_name", get_all_api_modules())
def test_api_client_methods(module_name):
    """Dynamically load each API client, mock requests, and execute every public method."""
    mod = importlib.import_module(module_name)

    # Identify Api class
    api_class = getattr(mod, "Api", None) or getattr(mod, "LeanixApi", None)
    assert api_class is not None, f"No Api class found in {module_name}"

    # Instantiate API client with mock/dummy args
    if api_class == LeanixApi:
        client = api_class(base_url="https://mock.leanix.net", token="mock-token")
        client.headers = {"Authorization": "Bearer mock-token"}
    else:
        client = api_class(
            base_url="https://mock.leanix.net/services/pathfinder/v1",
            token="mock-token",
        )
        client._session.headers["Authorization"] = "Bearer mock-token"

    # Mock request and _authenticate
    mock_request = MagicMock(return_value={"status": "success"})
    client.request = mock_request

    # Iterate through all methods of the client
    for name, method in inspect.getmembers(client, predicate=inspect.ismethod):
        # Skip special/private methods and base handlers
        if name.startswith("_") or name in (
            "request",
            "get_factsheets",
            "get_factsheet",
        ):
            continue

        # Inspect parameters to build mock inputs
        sig = inspect.signature(method)
        kwargs: dict[str, Any] = {}
        for param in sig.parameters.values():
            if param.name in ("self", "kwargs"):
                continue
            if param.default is not inspect.Parameter.empty:
                continue
            if param.annotation == dict or param.name == "data":
                kwargs[param.name] = {}
            else:
                kwargs[param.name] = "test-value"

        # Call method and check it runs without exceptions
        res = method(**kwargs)
        assert res == {"status": "success"}


def test_leanix_api_special_methods():
    """Specific tests for LeanixApi (get_factsheets and get_factsheet)."""
    client = LeanixApi(base_url="https://mock.leanix.net", token="mock-token")
    client.headers = {"Authorization": "Bearer mock-token"}

    # Use a real requests.Response object to pass Pydantic is_instance_of validation
    mock_response = requests.Response()
    mock_response.status_code = 200

    # 1. get_factsheets
    mock_response.json = MagicMock(return_value={"data": []})
    with patch.object(client._session, "get", return_value=mock_response):
        res = client.get_factsheets(workspaceId="mock-id")
        assert res.data.data == []

    # 2. get_factsheet
    mock_response.json = MagicMock(
        return_value={"data": {"id": "123", "name": "mock-fs"}}
    )
    with patch.object(client._session, "get", return_value=mock_response):
        res = client.get_factsheet(id="123")
        assert res.data.id == "123"


@pytest.mark.parametrize(
    "module_name", [m for m in get_all_api_modules() if "api_client_leanix" not in m]
)
def test_api_client_base_request_handling(module_name):
    """Test the base request method and _authenticate method in all standard generated Api clients."""
    import importlib

    mod = importlib.import_module(module_name)
    Api = getattr(mod, "Api")

    client = Api(
        base_url="https://mock.leanix.net/services/test/v1", token="mock-token"
    )

    # Mock post for _authenticate
    mock_auth_resp = MagicMock()
    mock_auth_resp.status_code = 200
    mock_auth_resp.json.return_value = {"access_token": "mocked-access"}

    # 1. Test successful authenticate + request
    mock_req_resp = MagicMock()
    mock_req_resp.status_code = 200
    mock_req_resp.json.return_value = {"status": "ok"}

    with (
        patch.object(client._session, "post", return_value=mock_auth_resp) as mock_post,
        patch.object(
            client._session, "request", return_value=mock_req_resp
        ) as mock_req,
    ):
        res = client.request("GET", "/test")
        assert res == {"status": "ok"}
        mock_post.assert_called_once()
        mock_req.assert_called_once()

    # 2. Test status code 204
    mock_req_resp.status_code = 204
    with patch.object(client._session, "request", return_value=mock_req_resp):
        res = client.request("GET", "/test-204")
        assert res == {"status": "success"}

    # 3. Test HTTP exception error handling
    mock_err_resp = MagicMock()
    mock_err_resp.status_code = 400
    mock_err_resp.text = "bad request detail"
    with patch.object(client._session, "request", return_value=mock_err_resp):
        with pytest.raises(Exception, match="API error: 400 - bad request detail"):
            client.request("GET", "/error")

    # 4. Test unauthorized error handling
    mock_unauth_resp = MagicMock()
    mock_unauth_resp.status_code = 401
    mock_unauth_resp.text = "unauthorized"
    with patch.object(client._session, "request", return_value=mock_unauth_resp):
        from agent_utilities.exceptions import AuthError

        try:
            client.request("GET", "/unauth")
            pytest.fail("Should have raised an error")
        except AuthError:
            pass
        except Exception as e:
            assert "API error: 401" in str(e)
