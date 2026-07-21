"""Governed universal LeanIX REST and multipart MCP tools."""

from __future__ import annotations

import base64
import json
import re
from typing import Any

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import BaseModel, Field, ValidationError, field_validator

from leanix_agent.auth import get_client

_MAX_UPLOAD_BYTES = 16 * 1024 * 1024
_MAX_ENCODED_UPLOAD_BYTES = ((_MAX_UPLOAD_BYTES + 2) // 3) * 4
_MAX_JSON_BYTES = 16 * 1024 * 1024
_MAX_FILES = 32
_FIELD_NAME = re.compile(r"^[A-Za-z][A-Za-z0-9_.-]{0,127}$")
_CONTENT_TYPE = re.compile(
    r"^[A-Za-z0-9][A-Za-z0-9!#$&^_.+-]{0,126}/"
    r"[A-Za-z0-9][A-Za-z0-9!#$&^_.+-]{0,126}$"
)
_MUTATING_METHODS = frozenset({"DELETE", "PATCH", "POST", "PUT"})


class UploadPart(BaseModel):
    """One bounded in-memory multipart upload part."""

    filename: str = Field(min_length=1, max_length=255)
    content_type: str = Field(default="application/octet-stream", min_length=1)
    content_base64: str = Field(min_length=1, max_length=_MAX_ENCODED_UPLOAD_BYTES)

    @field_validator("filename")
    @classmethod
    def validate_filename(cls, value: str) -> str:
        if (
            value in {".", ".."}
            or "/" in value
            or "\\" in value
            or any(ord(character) < 32 for character in value)
        ):
            raise ValueError("filename must be a plain leaf name")
        return value

    @field_validator("content_type")
    @classmethod
    def validate_content_type(cls, value: str) -> str:
        if not _CONTENT_TYPE.fullmatch(value):
            raise ValueError("content_type must be a media type")
        return value


def _load_json(value: str, label: str) -> Any:
    if len(value.encode("utf-8")) > _MAX_JSON_BYTES:
        raise ValueError(f"{label} exceeds the JSON size limit")
    try:
        return json.loads(value)
    except json.JSONDecodeError as exc:
        raise ValueError(f"{label} must be valid JSON") from exc


def _json_object(value: str, label: str) -> dict[str, Any]:
    parsed = _load_json(value or "{}", label)
    if not isinstance(parsed, dict):
        raise ValueError(f"{label} must be a JSON object")
    return parsed


def _json_value(value: str, label: str) -> Any:
    return _load_json(value, label)


def _decode_uploads(value: str) -> dict[str, tuple[str, bytes, str]] | None:
    raw = _json_object(value, "files_json")
    if not raw:
        return None
    if len(raw) > _MAX_FILES:
        raise ValueError("files_json exceeds the file-count limit")
    files: dict[str, tuple[str, bytes, str]] = {}
    total = 0
    for field_name, item in raw.items():
        if not _FIELD_NAME.fullmatch(str(field_name)):
            raise ValueError("multipart field name is invalid")
        part = UploadPart.model_validate(item)
        try:
            content = base64.b64decode(part.content_base64, validate=True)
        except (ValueError, TypeError) as exc:
            raise ValueError("multipart content is not valid base64") from exc
        total += len(content)
        if total > _MAX_UPLOAD_BYTES:
            raise ValueError("multipart upload exceeds the 16 MiB limit")
        files[str(field_name)] = (part.filename, content, part.content_type)
    return files


def register_universal_api_tools(mcp: FastMCP) -> None:
    """Register the workspace-scoped universal REST execution surface."""

    @mcp.tool(tags={"leanix-api", "openapi", "universal"})
    async def leanix_rest_api(
        method: str = Field(
            description="HTTP method: GET, POST, PUT, PATCH, DELETE, HEAD, or OPTIONS."
        ),
        service: str = Field(description="Configured LeanIX service slug."),
        endpoint: str = Field(
            description="Path relative to /services/<service>/<version>."
        ),
        version: str = Field(default="v1", description="Service API version."),
        params_json: str = Field(
            default="{}", description="JSON object of query parameters."
        ),
        body_json: str = Field(
            default="{}",
            description="JSON request body; multipart form fields must be an object.",
        ),
        files_json: str = Field(
            default="{}",
            description=(
                "Optional multipart map of field to filename, media type, and "
                "base64 content; aggregate payload is limited to 16 MiB."
            ),
        ),
        accept: str = Field(
            default="application/json", description="Requested response media type."
        ),
        allow_mutation: bool = Field(
            default=False,
            description="Must be true for this individual mutating request.",
        ),
        client=Depends(get_client),
        ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Invoke a workspace-scoped LeanIX operation with mutation consent."""
        verb = method.upper().strip()
        if verb in _MUTATING_METHODS and not allow_mutation:
            return {
                "error": "LeanIX mutation is blocked by default",
                "errorType": "MutationApprovalRequired",
            }
        try:
            params = _json_object(params_json, "params_json")
            body = _json_value(body_json, "body_json")
            files = _decode_uploads(files_json)
            if files and not isinstance(body, dict):
                raise ValueError("body_json must be an object for multipart requests")
        except (ValidationError, ValueError):
            return {
                "error": "LeanIX API request validation failed",
                "errorType": "ValidationError",
            }
        if ctx:
            await ctx.info("Calling the configured LeanIX workspace API")
        try:
            return client.request_api(
                verb,
                endpoint,
                service=service,
                version=version,
                params=params or None,
                data=body,
                files=files,
                accept=accept,
            )
        except Exception as exc:  # noqa: BLE001 - bounded MCP error boundary
            return {
                "error": "LeanIX API request failed",
                "errorType": type(exc).__name__,
            }
