"""GraphQL schema fingerprinting and TLS-profiled multipart coverage."""

from __future__ import annotations

import json
from unittest.mock import MagicMock, patch

from leanix_agent.leanix_gql import GraphQL


def test_schema_snapshot_is_deterministic_and_bounded(tls_profile_factory):
    client = GraphQL(
        url="https://tenant.example.test",
        token="opaque-token",
        tls_profile=tls_profile_factory(),
    )
    schema = {
        "__schema": {
            "queryType": {"name": "Query"},
            "mutationType": None,
            "subscriptionType": None,
            "types": [
                {"kind": "OBJECT", "name": "Query", "fields": []},
                {"kind": "SCALAR", "name": "String"},
            ],
            "directives": [],
        }
    }
    client.execute_gql = MagicMock(return_value=schema)

    first = client.schema_snapshot(max_types=1)
    second = client.schema_snapshot(max_types=1)

    assert first["schemaDigest"] == second["schemaDigest"]
    assert first["typeCount"] == 2
    assert first["returnedTypeCount"] == 1
    assert first["truncated"] is True


def test_execute_gql_returns_usable_partial_data_without_error_content(
    tls_profile_factory,
):
    client = GraphQL(
        url="https://tenant.example.test",
        token="opaque-token",
        tls_profile=tls_profile_factory(),
    )
    execution = MagicMock()
    execution.data = {"allFactSheets": {"edges": []}}
    execution.errors = [RuntimeError("field-specific source detail")]
    client.client.execute = MagicMock(return_value=execution)

    result = client.execute_gql(
        "query Inventory { allFactSheets(first: 1) { edges { node { id } } } }",
        allow_partial=True,
    )

    assert result == {"allFactSheets": {"edges": []}}
    assert client.last_partial_error_count == 1
    assert "errors" not in result


def test_multipart_uses_profiled_session_timeout_and_bounded_reader(
    tls_profile_factory,
):
    tls_profile = tls_profile_factory()
    client = GraphQL(
        url="https://tenant.example.test",
        token="opaque-token",
        tls_profile=tls_profile,
    )
    session = MagicMock()
    response = MagicMock()
    response.status_code = 200
    response.headers = {"Content-Type": "application/json"}
    response.iter_content.return_value = [json.dumps({"data": {"ok": True}}).encode()]
    session.post.return_value = response

    with patch("leanix_agent.leanix_gql.requests.Session", return_value=session):
        result = client.execute_multipart(
            {"query": "query Upload { viewer { id } }", "variables": {"file": None}},
            {"0": ["variables.file"]},
            {"0": ("document.txt", b"content", "text/plain")},
        )

    assert result == {"data": {"ok": True}}
    tls_profile.configure_requests_session.assert_called_with(session)
    kwargs = session.post.call_args.kwargs
    assert kwargs["stream"] is True
    assert kwargs["timeout"] == (10.0, 120.0)
    assert "verify" not in kwargs
    session.close.assert_called_once()
