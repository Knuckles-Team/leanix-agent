"""Governed LeanIX GraphQL MCP tools."""

from __future__ import annotations

import json
import re
from typing import Any

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from graphql import OperationType, parse
from pydantic import Field

from leanix_agent.auth import get_graphql_client
from leanix_agent.mcp.mcp_universal_api import _decode_uploads

_MAX_QUERY_BYTES = 128 * 1024
_MAX_VARIABLE_BYTES = 4 * 1024 * 1024
_MAX_MAP_ENTRIES = 32
_UPLOAD_PATH = re.compile(
    r"^variables(?:\.[_A-Za-z][_0-9A-Za-z]{0,127}|\.[0-9]{1,6}){1,20}$"
)


def _is_mutation(query: str) -> bool:
    if len(query.encode("utf-8")) > _MAX_QUERY_BYTES:
        raise ValueError("GraphQL document exceeds the query size limit")
    document = parse(query)
    return any(
        getattr(definition, "operation", None) == OperationType.MUTATION
        for definition in document.definitions
    )


def _mutation_blocked(query: str, allow_mutation: bool) -> bool:
    return _is_mutation(query) and not allow_mutation


def register_graphql_tools(mcp: FastMCP) -> None:
    """Register query, schema discovery, and multipart tools."""

    @mcp.tool(tags={"graphql"})
    async def leanix_graphql(
        query: str = Field(description="GraphQL query or mutation document."),
        variables: str = Field(
            default="{}", description="JSON object of GraphQL variables."
        ),
        operation_name: str | None = Field(
            default=None, description="Optional operation name."
        ),
        allow_mutation: bool = Field(
            default=False,
            description="Must be true for this individual mutation request.",
        ),
        client=Depends(get_graphql_client),
        ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Execute a bounded GraphQL document with mutation consent."""
        try:
            if len(variables.encode("utf-8")) > _MAX_VARIABLE_BYTES:
                raise ValueError("variables exceeds the size limit")
            parsed_variables = json.loads(variables) if variables else {}
            if not isinstance(parsed_variables, dict):
                raise ValueError("variables must be a JSON object")
            if _mutation_blocked(query, allow_mutation):
                return {
                    "error": "LeanIX mutation is blocked by default",
                    "errorType": "MutationApprovalRequired",
                }
        except Exception as exc:  # noqa: BLE001 - parse boundary
            return {
                "error": "GraphQL request validation failed",
                "errorType": type(exc).__name__,
            }
        if ctx:
            await ctx.info("Executing a configured LeanIX GraphQL operation")
        try:
            return client.execute_gql(
                query_str=query,
                variables=parsed_variables or None,
                operation_name=operation_name,
            )
        except Exception as exc:  # noqa: BLE001 - bounded MCP error
            return {
                "error": "GraphQL execution failed",
                "errorType": type(exc).__name__,
            }

    @mcp.tool(tags={"graphql", "schema", "coverage"})
    async def leanix_graphql_schema(
        max_types: int | None = Field(
            default=None,
            ge=1,
            le=10_000,
            description="Optional maximum returned type count.",
        ),
        include_sdl: bool = Field(
            default=False, description="Include the printable schema document."
        ),
        client=Depends(get_graphql_client),
        ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Introspect and fingerprint the current workspace schema."""
        if ctx:
            await ctx.info("Discovering the configured LeanIX GraphQL schema")
        try:
            return client.schema_snapshot(max_types=max_types, include_sdl=include_sdl)
        except Exception as exc:  # noqa: BLE001 - bounded MCP error
            return {
                "error": "GraphQL schema discovery failed",
                "errorType": type(exc).__name__,
            }

    @mcp.tool(tags={"graphql", "upload"})
    async def leanix_graphql_upload(
        operations_json: str = Field(
            description="GraphQL multipart operations JSON object."
        ),
        file_map_json: str = Field(description="GraphQL multipart map JSON object."),
        files_json: str = Field(
            description="Bounded multipart file map with base64 content."
        ),
        allow_mutation: bool = Field(
            default=False,
            description="Must be true for this individual mutation request.",
        ),
        client=Depends(get_graphql_client),
        ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Execute a bounded GraphQL multipart upload through configured TLS."""
        try:
            if (
                len(operations_json.encode("utf-8")) > _MAX_VARIABLE_BYTES
                or len(file_map_json.encode("utf-8")) > _MAX_VARIABLE_BYTES
            ):
                raise ValueError("multipart metadata exceeds the size limit")
            operations = json.loads(operations_json)
            file_map = json.loads(file_map_json)
            files = _decode_uploads(files_json)
            if not isinstance(operations, dict) or not isinstance(file_map, dict):
                raise ValueError("multipart metadata must be objects")
            if not files or not 1 <= len(file_map) <= _MAX_MAP_ENTRIES:
                raise ValueError("multipart file map is invalid")
            query = operations.get("query")
            if not isinstance(query, str):
                raise ValueError("operations query is required")
            if _mutation_blocked(query, allow_mutation):
                return {
                    "error": "LeanIX mutation is blocked by default",
                    "errorType": "MutationApprovalRequired",
                }
            normalized_map: dict[str, list[str]] = {}
            for key, paths in file_map.items():
                if (
                    str(key) not in files
                    or not isinstance(paths, list)
                    or not paths
                    or not all(
                        isinstance(path, str) and _UPLOAD_PATH.fullmatch(path)
                        for path in paths
                    )
                ):
                    raise ValueError("multipart map entry is invalid")
                normalized_map[str(key)] = paths
            if set(normalized_map) != set(files):
                raise ValueError("multipart map and files must match exactly")
        except Exception as exc:  # noqa: BLE001 - parse boundary
            return {
                "error": "GraphQL multipart validation failed",
                "errorType": type(exc).__name__,
            }
        if ctx:
            await ctx.info("Uploading to the configured LeanIX GraphQL endpoint")
        try:
            return client.execute_multipart(operations, normalized_map, files)
        except Exception as exc:  # noqa: BLE001 - bounded MCP error
            return {
                "error": "GraphQL multipart request failed",
                "errorType": type(exc).__name__,
            }
