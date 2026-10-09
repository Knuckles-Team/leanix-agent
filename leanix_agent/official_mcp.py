"""Fail-closed contract for federating a hosted LeanIX MCP service.

The package deliberately carries no hosted endpoint, toolset, executable, auth
material, certificate material, or deployment profile.  Those values are
resolved from one explicitly selected :class:`AgentConfig` provider profile at
the process boundary.  This module validates the ephemeral result and returns a
redacted plan for GraphOS wiring; it never downloads or launches a helper.
"""

from __future__ import annotations

import hashlib
import hmac
import json
import os
import re
import stat
from collections.abc import Mapping, Sequence
from dataclasses import dataclass, field
from pathlib import Path
from typing import TYPE_CHECKING, Any
from urllib.parse import urlsplit

from agent_utilities.core.provider_runtime import (
    PreparedProviderChildRuntime,
    ProviderRuntimeError,
    ResolvedProviderRuntime,
    get_provider_runtime_profile,
    prepare_resolved_provider_runtime_child_environment,
    resolve_provider_runtime_profile,
)

if TYPE_CHECKING:
    from agent_connector_sdk.tls.profile import ResolvedTLSProfile

    # SDK gap: no AgentConfig equivalent in agent_connector_sdk yet.
    from agent_utilities.core import config as config_module

__all__ = [
    "AUTH_PROFILE_SELECTOR",
    "HELPER_COMMAND_SELECTOR",
    "HELPER_SHA256_SELECTOR",
    "READ_ONLY_TOOLS_SELECTOR",
    "TOOLSETS_SELECTOR",
    "OfficialMCPFederationError",
    "OfficialMCPChildPolicy",
    "OfficialMCPFederationPlan",
    "create_official_mcp_child_policy",
    "fingerprint_read_only_catalog",
    "resolve_official_mcp_federation",
]

TOOLSETS_SELECTOR = "HOSTED_MCP_TOOLSETS"
HELPER_COMMAND_SELECTOR = "HOSTED_MCP_HELPER_COMMAND"
HELPER_SHA256_SELECTOR = "HOSTED_MCP_HELPER_SHA256"
AUTH_PROFILE_SELECTOR = "HOSTED_MCP_AUTH_PROFILE"
READ_ONLY_TOOLS_SELECTOR = "HOSTED_MCP_READ_ONLY_TOOLS"

_REQUIRED_SELECTORS = frozenset(
    {
        TOOLSETS_SELECTOR,
        HELPER_COMMAND_SELECTOR,
        HELPER_SHA256_SELECTOR,
        AUTH_PROFILE_SELECTOR,
    }
)
_ALLOWED_SELECTORS = _REQUIRED_SELECTORS | {READ_ONLY_TOOLS_SELECTOR}
_SELECTOR_VALUE_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_.:-]{0,127}$")
_TOOLSET_VALUE_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_.:-]{0,49}$")
_TOOL_VALUE_RE = re.compile(r"^[A-Za-z][A-Za-z0-9_.:-]{0,255}$")
_SHA256_RE = re.compile(r"^[0-9a-f]{64}$")
_MAX_HELPER_BYTES = 256 * 1024 * 1024
_MAX_TOOLSETS = 10
_MAX_READ_ONLY_TOOLS = 4_096
_MAX_CATALOG_TOOLS = 4_096
_MAX_CATALOG_BYTES = 16 * 1024 * 1024


class OfficialMCPFederationError(RuntimeError):
    """Stable federation failure that never includes deployment-owned values."""


def _error(code: str) -> OfficialMCPFederationError:
    return OfficialMCPFederationError(code)


def _valid_string_list_shape(
    parsed: Any, *, maximum_items: int, allow_empty: bool
) -> bool:
    """Return whether a decoded JSON value is an in-bounds, non-empty-unless-allowed list."""
    return (
        isinstance(parsed, list)
        and len(parsed) <= maximum_items
        and (bool(parsed) or allow_empty)
    )


def _valid_string_list_item(
    item: Any, *, item_pattern: re.Pattern[str], observed: set[str]
) -> bool:
    """Return whether one list entry is an untrimmed-safe, pattern-matching, unique string."""
    return (
        isinstance(item, str)
        and item == item.strip()
        and item_pattern.fullmatch(item) is not None
        and item not in observed
    )


def _parse_string_list(
    value: str,
    *,
    field_name: str,
    maximum_items: int,
    item_pattern: re.Pattern[str],
    allow_empty: bool = False,
) -> tuple[str, ...]:
    try:
        parsed = json.loads(value)
    except (TypeError, ValueError):
        raise _error(f"{field_name}_invalid") from None
    if not _valid_string_list_shape(
        parsed, maximum_items=maximum_items, allow_empty=allow_empty
    ):
        raise _error(f"{field_name}_invalid")
    result: list[str] = []
    observed: set[str] = set()
    for item in parsed:
        if not _valid_string_list_item(
            item, item_pattern=item_pattern, observed=observed
        ):
            raise _error(f"{field_name}_invalid")
        observed.add(item)
        result.append(item)
    return tuple(result)


def _endpoint_shape_invalid(rendered: str, parsed: Any) -> bool:
    """Return whether the rendered URL or its scheme/host is structurally unsafe."""
    return (
        not rendered
        or len(rendered.encode("utf-8")) > 8_192
        or parsed.scheme.casefold() != "https"
        or not parsed.netloc
        or not parsed.hostname
    )


def _endpoint_identity_invalid(parsed: Any, port: int | None) -> bool:
    """Return whether the URL carries embedded credentials, query, or a bad port."""
    return (
        parsed.username is not None
        or parsed.password is not None
        or parsed.query
        or parsed.fragment
        or (port is not None and not 1 <= port <= 65_535)
    )


def _secure_hosted_endpoint(value: str | None) -> str:
    rendered = str(value or "").strip().rstrip("/")
    try:
        parsed = urlsplit(rendered)
        port = parsed.port
    except ValueError:
        raise _error("hosted_mcp_endpoint_invalid") from None
    if _endpoint_shape_invalid(rendered, parsed) or _endpoint_identity_invalid(
        parsed, port
    ):
        raise _error("hosted_mcp_endpoint_invalid")
    return rendered


def _helper_value_malformed(value: str) -> bool:
    """Return whether a helper path string carries unsafe characters or shape."""
    return (
        not isinstance(value, str)
        or not value
        or value != value.strip()
        or "\x00" in value
        or "\r" in value
        or "\n" in value
        or len(value.encode("utf-8")) > 4_096
    )


def _helper_path(value: str) -> Path:
    if _helper_value_malformed(value):
        raise _error("hosted_mcp_helper_invalid")
    candidate = Path(value)
    if not candidate.is_absolute() or ".." in candidate.parts:
        raise _error("hosted_mcp_helper_invalid")
    try:
        if candidate.resolve(strict=True) != candidate:
            raise _error("hosted_mcp_helper_invalid")
    except OfficialMCPFederationError:
        raise
    except OSError:
        raise _error("hosted_mcp_helper_unavailable") from None
    return candidate


def _helper_metadata_invalid(metadata: os.stat_result) -> bool:
    """Return whether an opened helper's file metadata fails the integrity shape."""
    return (
        not stat.S_ISREG(metadata.st_mode)
        or not 1 <= metadata.st_size <= _MAX_HELPER_BYTES
        or (os.name == "posix" and metadata.st_mode & 0o111 == 0)
        or (os.name == "posix" and metadata.st_mode & 0o022 != 0)
    )


def _digest_open_file(descriptor: int) -> Any:
    """Return the SHA-256 digest object for an already-open file descriptor."""
    digest = hashlib.sha256()
    while True:
        chunk = os.read(descriptor, 1024 * 1024)
        if not chunk:
            break
        digest.update(chunk)
    return digest


def _verify_helper(command: Path, expected_sha256: str) -> None:
    if _SHA256_RE.fullmatch(expected_sha256) is None:
        raise _error("hosted_mcp_helper_integrity_invalid")
    flags = os.O_RDONLY | getattr(os, "O_CLOEXEC", 0)
    nofollow = getattr(os, "O_NOFOLLOW", 0)
    if not nofollow and command.is_symlink():
        raise _error("hosted_mcp_helper_invalid")
    try:
        descriptor = os.open(command, flags | nofollow)
    except OSError:
        raise _error("hosted_mcp_helper_unavailable") from None
    try:
        metadata = os.fstat(descriptor)
        if _helper_metadata_invalid(metadata):
            raise _error("hosted_mcp_helper_invalid")
        digest = _digest_open_file(descriptor)
    finally:
        os.close(descriptor)
    if not hmac.compare_digest(digest.hexdigest(), expected_sha256):
        raise _error("hosted_mcp_helper_integrity_mismatch")


@dataclass(slots=True, repr=False)
class OfficialMCPFederationPlan:
    """Ephemeral, read-only hosted-MCP launch plan with deterministic cleanup."""

    endpoint: str = field(repr=False)
    toolsets: tuple[str, ...] = field(repr=False)
    helper_command: Path = field(repr=False)
    helper_sha256: str = field(repr=False)
    auth_profile: str = field(repr=False)
    read_only_tools: frozenset[str] = field(repr=False)
    tls: ResolvedTLSProfile | None = field(repr=False)
    _runtime: ResolvedProviderRuntime = field(repr=False)
    _closed: bool = field(default=False, init=False, repr=False)

    @property
    def read_only(self) -> bool:
        """The federation cannot be promoted to a write-capable mode."""
        return True

    def __repr__(self) -> str:
        return "<OfficialMCPFederationPlan redacted>"

    def verify_helper(self) -> None:
        """Recheck the preinstalled helper immediately before process spawn."""
        if self._closed:
            raise _error("hosted_mcp_plan_closed")
        _verify_helper(self.helper_command, self.helper_sha256)

    def allows_tool(self, name: str, annotations: object) -> bool:
        """Admit only explicitly read-only tools, optionally narrowed by name."""
        if self._closed or _TOOL_VALUE_RE.fullmatch(str(name or "")) is None:
            return False
        if self.read_only_tools and name not in self.read_only_tools:
            return False
        if isinstance(annotations, Mapping):
            return annotations.get("readOnlyHint") is True
        return getattr(annotations, "readOnlyHint", None) is True

    def close(self) -> None:
        """Erase resolved provider material and release TLS resources."""
        if self._closed:
            return
        self._closed = True
        self.endpoint = ""
        self.toolsets = ()
        self.helper_command = Path()
        self.helper_sha256 = ""
        self.auth_profile = ""
        self.read_only_tools = frozenset()
        self.tls = None
        self._runtime.close()

    def __enter__(self) -> OfficialMCPFederationPlan:
        return self

    def __exit__(self, *_exc: object) -> None:
        self.close()


@dataclass(slots=True, repr=False)
class OfficialMCPChildPolicy:
    """GraphOS child policy for one ephemeral official-MCP plan."""

    plan: OfficialMCPFederationPlan = field(repr=False)
    profile_name: str = field(repr=False)
    prepared: PreparedProviderChildRuntime = field(repr=False)
    _closed: bool = field(default=False, init=False, repr=False)

    def __repr__(self) -> str:
        return "<OfficialMCPChildPolicy redacted>"

    def transport_config(self) -> dict[str, object]:
        """Return the preinstalled helper's shell-free stdio declaration."""
        if self._closed:
            raise _error("hosted_mcp_policy_closed")
        return {"args": [], "command": str(self.plan.helper_command)}

    def child_environment(self) -> Mapping[str, str]:
        """Return the isolated generic provider projection for the helper."""
        if self._closed:
            raise _error("hosted_mcp_policy_closed")
        return self.prepared.environment

    def verify_before_spawn(self) -> None:
        """Revalidate helper integrity at the multiplexer spawn boundary."""
        if self._closed:
            raise _error("hosted_mcp_policy_closed")
        self.plan.verify_helper()

    def allows_tool(self, name: str, annotations: object) -> bool:
        """Apply the permanent read-only live-catalog admission rule."""
        return not self._closed and self.plan.allows_tool(name, annotations)

    def fingerprint_catalog(self, tools: Sequence[Mapping[str, Any]]) -> str:
        """Fingerprint only tools admitted by the same plan."""
        if self._closed:
            raise _error("hosted_mcp_policy_closed")
        return fingerprint_read_only_catalog(self.plan, tools)

    def close(self) -> None:
        """Erase the child projection and close the resolved plan once."""
        if self._closed:
            return
        self._closed = True
        self.profile_name = ""
        try:
            self.prepared.close()
        finally:
            self.plan.close()


def _declaration_invalid(declaration: Any) -> bool:
    """Return whether a resolved profile declaration is missing required wiring."""
    return (
        declaration.endpoint_ref is None
        or not (declaration.tls_profile or declaration.tls_profile_ref)
        or declaration.credential_refs
        or not _REQUIRED_SELECTORS.issubset(declaration.selector_refs)
        or not set(declaration.selector_refs).issubset(_ALLOWED_SELECTORS)
    )


def _federation_selectors(
    runtime: ResolvedProviderRuntime,
) -> tuple[str, tuple[str, ...], frozenset[str], Path, str, str]:
    """Validate and extract every selector-derived field for one federation plan."""
    endpoint = _secure_hosted_endpoint(runtime.endpoint)
    if (
        runtime.credentials
        or runtime.tls is None
        or runtime.tls.verify_enabled is not True
    ):
        raise _error("hosted_mcp_tls_unavailable")
    selectors = runtime.selectors
    if not _REQUIRED_SELECTORS.issubset(selectors):
        raise _error("hosted_mcp_selectors_unavailable")
    toolsets = _parse_string_list(
        selectors[TOOLSETS_SELECTOR],
        field_name="hosted_mcp_toolsets",
        maximum_items=_MAX_TOOLSETS,
        item_pattern=_TOOLSET_VALUE_RE,
    )
    read_only_tools = frozenset(
        _parse_string_list(
            selectors.get(READ_ONLY_TOOLS_SELECTOR, "[]"),
            field_name="hosted_mcp_read_only_tools",
            maximum_items=_MAX_READ_ONLY_TOOLS,
            item_pattern=_TOOL_VALUE_RE,
            allow_empty=True,
        )
    )
    helper_command = _helper_path(selectors[HELPER_COMMAND_SELECTOR])
    helper_sha256 = selectors[HELPER_SHA256_SELECTOR]
    auth_profile = selectors[AUTH_PROFILE_SELECTOR]
    if _SELECTOR_VALUE_RE.fullmatch(auth_profile) is None:
        raise _error("hosted_mcp_auth_profile_invalid")
    _verify_helper(helper_command, helper_sha256)
    return (
        endpoint,
        toolsets,
        read_only_tools,
        helper_command,
        helper_sha256,
        auth_profile,
    )


def _resolved_federation_plan(
    runtime: ResolvedProviderRuntime,
) -> OfficialMCPFederationPlan:
    """Validate a resolved runtime and build its read-only plan, closing it on failure."""
    try:
        (
            endpoint,
            toolsets,
            read_only_tools,
            helper_command,
            helper_sha256,
            auth_profile,
        ) = _federation_selectors(runtime)
    except OfficialMCPFederationError:
        runtime.close()
        raise
    except Exception:
        runtime.close()
        raise _error("hosted_mcp_runtime_invalid") from None

    return OfficialMCPFederationPlan(
        endpoint=endpoint,
        toolsets=toolsets,
        helper_command=helper_command,
        helper_sha256=helper_sha256,
        auth_profile=auth_profile,
        read_only_tools=read_only_tools,
        tls=runtime.tls,
        _runtime=runtime,
    )


def resolve_official_mcp_federation(
    *, config: config_module.AgentConfig, profile_name: str
) -> OfficialMCPFederationPlan:
    """Resolve one enabled generic provider profile into a read-only plan.

    The selected profile is the enable switch.  Missing, disabled, incomplete,
    or ambiguous profiles fail before any helper is launched or network
    connection is attempted.
    """
    try:
        declaration = get_provider_runtime_profile(
            profile_name,
            config=config,
            require_enabled=False,
        )
    except ProviderRuntimeError:
        raise _error("hosted_mcp_profile_unavailable") from None
    if not declaration.enabled:
        raise _error("hosted_mcp_profile_disabled")
    if _declaration_invalid(declaration):
        raise _error("hosted_mcp_profile_invalid")

    try:
        runtime = resolve_provider_runtime_profile(profile_name, config=config)
    except ProviderRuntimeError:
        raise _error("hosted_mcp_runtime_unavailable") from None

    return _resolved_federation_plan(runtime)


def create_official_mcp_child_policy(
    *,
    profile_name: str,
    config: config_module.AgentConfig,
) -> OfficialMCPChildPolicy:
    """Resolve one configured profile into the GraphOS child-policy seam."""

    plan = resolve_official_mcp_federation(
        config=config,
        profile_name=profile_name,
    )
    try:
        prepared = prepare_resolved_provider_runtime_child_environment(
            profile_name,
            plan._runtime,
        )
    except Exception:
        plan.close()
        raise _error("hosted_mcp_child_projection_unavailable") from None
    return OfficialMCPChildPolicy(
        plan=plan,
        profile_name=profile_name,
        prepared=prepared,
    )


def _validated_catalog_tool(
    tool: Any, names: set[str]
) -> tuple[str, Mapping[str, Any], Any]:
    """Return the name/schema/annotations of one catalog tool, or fail closed."""
    if not isinstance(tool, Mapping):
        raise _error("hosted_mcp_catalog_invalid")
    name = tool.get("name")
    schema = tool.get("inputSchema")
    annotations = tool.get("annotations")
    if (
        not isinstance(name, str)
        or _TOOL_VALUE_RE.fullmatch(name) is None
        or name in names
        or not isinstance(schema, Mapping)
    ):
        raise _error("hosted_mcp_catalog_invalid")
    names.add(name)
    return name, schema, annotations


def _admitted_catalog_tools(
    plan: OfficialMCPFederationPlan, tools: Sequence[Mapping[str, Any]]
) -> list[dict[str, Any]]:
    """Validate every tool entry and return only those the plan admits, sorted."""
    admitted: list[dict[str, Any]] = []
    names: set[str] = set()
    for tool in tools:
        name, schema, annotations = _validated_catalog_tool(tool, names)
        if plan.allows_tool(name, annotations):
            admitted.append({"inputSchema": dict(schema), "name": name})
    admitted.sort(key=lambda item: item["name"])
    return admitted


def fingerprint_read_only_catalog(
    plan: OfficialMCPFederationPlan,
    tools: Sequence[Mapping[str, Any]],
) -> str:
    """Return a deterministic fingerprint of the admitted live tool schemas."""
    if plan._closed or len(tools) > _MAX_CATALOG_TOOLS:
        raise _error("hosted_mcp_catalog_invalid")
    admitted = _admitted_catalog_tools(plan, tools)
    try:
        payload = json.dumps(
            admitted,
            ensure_ascii=True,
            separators=(",", ":"),
            sort_keys=True,
        ).encode("utf-8")
    except (TypeError, ValueError):
        raise _error("hosted_mcp_catalog_invalid") from None
    if len(payload) > _MAX_CATALOG_BYTES:
        raise _error("hosted_mcp_catalog_invalid")
    return hashlib.sha256(payload).hexdigest()
