#!/usr/bin/python

"""GraphQL API Wrapper for LeanIX Agent.

Provides a GraphQL interface using the `gql` library that mirrors
REST API methods with GraphQL queries and mutations.

Requires: pip install gql[requests]
"""

import hashlib
import json
import logging
from typing import Any

import requests
from agent_utilities.core.decorators import require_auth
from agent_utilities.core.exceptions import (
    MissingParameterError,
    ParameterError,
)
from agent_utilities.core.transport_security import (
    ResolvedTLSProfile,
    resolve_configured_tls_profile,
)
from gql import Client, gql
from gql.transport.requests import RequestsHTTPTransport

logger = logging.getLogger(__name__)


class _ProfiledRequestsHTTPTransport(RequestsHTTPTransport):
    """Apply one mandatory-verification profile to every GraphQL request."""

    def __init__(self, *, tls_profile: ResolvedTLSProfile, **kwargs: Any) -> None:
        request_kwargs = tls_profile.requests_kwargs()
        verify = request_kwargs.pop("verify")
        super().__init__(verify=verify, **request_kwargs, **kwargs)
        self.tls_profile = tls_profile

    def connect(self) -> None:
        super().connect()
        if self.session is not None:
            self.tls_profile.configure_requests_session(self.session)


class GraphQL:
    """A class to interact with LeanIX Agent's GraphQL API."""

    def __init__(
        self,
        url: str | None = None,
        token: str | None = None,
        tls_profile: ResolvedTLSProfile | None = None,
        debug: bool = False,
    ):
        if not url:
            raise MissingParameterError("URL is required")
        if not token:
            raise MissingParameterError("Token is required")

        self.url = f"{url.rstrip('/')}/services/pathfinder/v1/graphql"
        self.token = token
        self.tls_profile = tls_profile or resolve_configured_tls_profile("leanix")
        self.debug = debug
        self.headers = {
            "Authorization": f"Bearer {token}"
        }  # Add headers for @require_auth decorator

        if debug:
            logger.setLevel(logging.DEBUG)

        headers = {"Authorization": f"Bearer {token}"}
        self.transport = _ProfiledRequestsHTTPTransport(
            url=self.url,
            headers=headers,
            tls_profile=self.tls_profile,
        )
        self.client = Client(transport=self.transport, fetch_schema_from_transport=True)

    @require_auth
    def execute_gql(
        self,
        query_str: str,
        variables: dict[str, Any] | None = None,
        operation_name: str | None = None,
        *,
        allow_partial: bool = False,
    ) -> dict[str, Any]:
        """Execute a GraphQL query or mutation.

        Args:
            query_str: The GraphQL query or mutation string.
            variables: Optional dictionary of variables for the query.
            operation_name: Optional name of the operation.
            allow_partial: Return usable ``data`` when the server also reports
                field-level errors. Error content is never returned or logged.

        Returns:
            Dict[str, Any]: The raw GraphQL response dictionary.
        """
        try:
            query = gql(query_str)
            if allow_partial:
                execution_result = self.client.execute(
                    query,
                    variable_values=variables,
                    operation_name=operation_name,
                    get_execution_result=True,
                )
                data = getattr(execution_result, "data", None)
                errors = getattr(execution_result, "errors", None) or []
                self.last_partial_error_count = len(errors)
                if errors:
                    logger.warning(
                        "GraphQL returned %d field-level error(s); using bounded partial data",
                        len(errors),
                    )
                if not isinstance(data, dict):
                    raise ParameterError("GraphQL returned no usable data")
                return data
            self.last_partial_error_count = 0
            result = self.client.execute(
                query, variable_values=variables, operation_name=operation_name
            )
            if "errors" in result:
                raise ParameterError(f"GraphQL errors: {result['errors']}")
            return result
        except Exception:
            logger.error("GraphQL execution failed")
            raise ParameterError("Query execution failed") from None

    @require_auth
    def query(
        self, query_str: str, variables: dict[str, Any] | None = None
    ) -> dict[str, Any]:
        """Execute a generic GraphQL query for LeanIX.

        Args:
            query_str: The GraphQL query string.
            variables: Optional dictionary of variables for the query.

        Returns:
            Dict[str, Any]: The raw GraphQL response dictionary.
        """
        return self.execute_gql(query_str, variables=variables)

    def ensure_schema(self) -> Any:
        """Fetch and retain the live schema before generated selections."""
        schema = getattr(self.client, "schema", None)
        if schema is None:
            self.execute_gql("query LeanixSchemaWarmup { __typename }")
            schema = getattr(self.client, "schema", None)
        if schema is None:
            raise ParameterError("GraphQL schema introspection is unavailable")
        return schema

    def schema_snapshot(
        self, *, max_types: int | None = None, include_sdl: bool = False
    ) -> dict[str, Any]:
        """Fingerprint the complete current workspace GraphQL schema."""
        if max_types is not None and not 1 <= max_types <= 10_000:
            raise ParameterError("max_types must be between 1 and 10000")
        from graphql import build_client_schema, get_introspection_query, print_schema

        introspection = self.execute_gql(
            get_introspection_query(
                descriptions=False,
                specified_by_url=True,
                directive_is_repeatable=True,
                schema_description=False,
                input_value_deprecation=True,
            )
        )
        if "data" in introspection and isinstance(introspection["data"], dict):
            introspection = introspection["data"]
        schema_data = introspection.get("__schema")
        if not isinstance(schema_data, dict):
            raise ParameterError("GraphQL introspection returned no schema")
        canonical = json.dumps(
            introspection, sort_keys=True, separators=(",", ":"), ensure_ascii=False
        )
        if len(canonical.encode("utf-8")) > 16 * 1024 * 1024:
            raise ParameterError("GraphQL schema exceeds the size limit")
        all_types = sorted(
            (item for item in schema_data.get("types") or [] if isinstance(item, dict)),
            key=lambda item: str(item.get("name") or ""),
        )
        if len(all_types) > 10_000:
            raise ParameterError("GraphQL schema type count exceeds the limit")
        selected_types = all_types if max_types is None else all_types[:max_types]
        roots = {
            key: value.get("name") if isinstance(value, dict) else None
            for key in ("queryType", "mutationType", "subscriptionType")
            if (value := schema_data.get(key)) is not None
        }
        result: dict[str, Any] = {
            "schemaDigest": hashlib.sha256(canonical.encode("utf-8")).hexdigest(),
            "typeCount": len(all_types),
            "returnedTypeCount": len(selected_types),
            "truncated": len(selected_types) < len(all_types),
            "roots": roots,
            "directives": schema_data.get("directives") or [],
            "types": selected_types,
        }
        if include_sdl:
            sdl = print_schema(build_client_schema(introspection))
            if len(sdl.encode("utf-8")) > 16 * 1024 * 1024:
                raise ParameterError("GraphQL SDL exceeds the size limit")
            result["sdl"] = sdl
        return result

    def execute_multipart(
        self,
        operations: dict[str, Any],
        file_map: dict[str, list[str]],
        files: dict[str, tuple[str, bytes, str]],
    ) -> dict[str, Any]:
        """Execute a bounded multipart request through the configured TLS profile."""
        from leanix_agent.api.api_client_leanix import LeanixApi

        session = requests.Session()
        self.tls_profile.configure_requests_session(session)
        response = session.post(
            f"{self.url}/upload",
            headers={"Authorization": f"Bearer {self.token}"},
            data={
                "operations": json.dumps(operations, separators=(",", ":")),
                "map": json.dumps(file_map, separators=(",", ":")),
            },
            files=files,
            stream=True,
            timeout=(10.0, 120.0),
        )
        try:
            response.raise_for_status()
            body = LeanixApi._bounded_content(response)
        finally:
            response.close()
            session.close()
        try:
            result = json.loads(body.decode("utf-8"))
        except (UnicodeDecodeError, json.JSONDecodeError) as exc:
            raise ParameterError("GraphQL multipart response is invalid") from exc
        if not isinstance(result, dict) or result.get("errors"):
            raise ParameterError("GraphQL multipart request returned errors")
        return result
