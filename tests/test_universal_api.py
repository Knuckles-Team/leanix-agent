"""Universal workspace-scoped REST transport and policy coverage."""

from __future__ import annotations

import base64
import json
from unittest.mock import MagicMock

import pytest
from agent_utilities.core.exceptions import ParameterError

from leanix_agent.api.api_client_leanix import LeanixApi
from leanix_agent.mcp.mcp_universal_api import _decode_uploads, _json_value


def _client(tls_profile_factory) -> LeanixApi:
    client = LeanixApi(
        base_url="https://tenant.example.test",
        token="bearer",
        is_oauth=True,
        tls_profile=tls_profile_factory(),
    )
    client._session = MagicMock()
    return client


def _response(body: bytes, content_type: str = "application/json", status: int = 200):
    response = MagicMock()
    response.status_code = status
    response.headers = {"Content-Type": content_type}
    response.iter_content.return_value = [body] if body else []
    return response


def test_request_api_routes_to_exact_service_version_path_and_timeout(
    tls_profile_factory,
):
    client = _client(tls_profile_factory)
    client._session.request.return_value = _response(b'{"ok":true}')

    result = client.request_api(
        "GET",
        "factSheets/abc",
        service="pathfinder",
        version="v1",
        params={"include": "relations"},
    )

    assert result["data"] == {"ok": True}
    kwargs = client._session.request.call_args.kwargs
    assert kwargs["url"] == (
        "https://tenant.example.test/services/pathfinder/v1/factSheets/abc"
    )
    assert kwargs["stream"] is True
    assert kwargs["timeout"] == (10.0, 120.0)
    assert "verify" not in kwargs


def test_request_api_supports_bounded_binary_responses(tls_profile_factory):
    client = _client(tls_profile_factory)
    client._session.request.return_value = _response(b"pdf", "application/pdf")

    result = client.request_api("GET", "exports/file", service="reports", version="v1")

    assert result["contentBase64"] == "cGRm"


def test_request_api_rejects_oversized_response(tls_profile_factory):
    client = _client(tls_profile_factory)
    response = _response(b"")
    response.headers["Content-Length"] = str(LeanixApi._MAX_RESPONSE_BYTES + 1)
    client._session.request.return_value = response

    with pytest.raises(ParameterError, match="size limit"):
        client.request_api("GET", "exports/file", service="reports", version="v1")


def test_request_api_authenticates_before_first_request(tls_profile_factory):
    client = LeanixApi(
        base_url="https://tenant.example.test",
        token="api-token",
        tls_profile=tls_profile_factory(),
    )
    client._session = MagicMock()
    client._session.request.return_value = _response(b"", status=204)
    authenticate = MagicMock(
        side_effect=lambda: setattr(
            client, "headers", {"Authorization": "Bearer exchanged"}
        )
    )
    client._authenticate = authenticate

    assert client.request_api("GET", "models/dataModel") == {
        "status": 204,
        "data": None,
    }
    authenticate.assert_called_once()


def test_universal_body_parser_preserves_json_patch_arrays():
    body = _json_value('[{"op":"replace","path":"/name","value":"New"}]', "body")

    assert body == [{"op": "replace", "path": "/name", "value": "New"}]


@pytest.mark.parametrize(
    ("service", "version", "endpoint"),
    [
        ("pathfinder", "v1", "https://example.test/secret"),
        ("pathfinder", "v1", "../mtm/token"),
        ("pathfinder", "v1", "%2e%2e/mtm/token"),
        ("pathfinder", "v1", "%252e%252e/mtm/token"),
        ("pathfinder", "v1", "factsheets%5ctoken"),
        ("pathfinder", "v1", "factsheets\nheader"),
        ("PathFinder", "v1", "factSheets"),
        ("pathfinder", "latest", "factSheets"),
    ],
)
def test_request_api_rejects_cross_host_or_unsafe_locations(
    tls_profile_factory, service: str, version: str, endpoint: str
):
    with pytest.raises(ParameterError):
        _client(tls_profile_factory).request_api(
            "GET", endpoint, service=service, version=version
        )


def test_upload_decoder_rejects_paths_and_caps_decoded_bytes():
    bad = json.dumps(
        {
            "file": {
                "filename": "../secret.txt",
                "content_type": "text/plain",
                "content_base64": base64.b64encode(b"content").decode(),
            }
        }
    )
    with pytest.raises(ValueError):
        _decode_uploads(bad)

    good = json.dumps(
        {
            "file": {
                "filename": "document.txt",
                "content_type": "text/plain",
                "content_base64": base64.b64encode(b"content").decode(),
            }
        }
    )
    assert _decode_uploads(good) == {"file": ("document.txt", b"content", "text/plain")}
