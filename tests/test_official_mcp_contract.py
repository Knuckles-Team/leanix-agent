"""Focused contract tests for the optional hosted MCP federation."""

from __future__ import annotations

import hashlib
import json
from types import SimpleNamespace

import pytest
from agent_utilities.core.config import AgentConfig

from leanix_agent import official_mcp


class _Runtime:
    def __init__(self, *, endpoint, selectors, tls):
        self.endpoint = endpoint
        self.selectors = selectors
        self.credentials = {}
        self.tls = tls
        self.closed = False

    def close(self):
        self.closed = True


def _executable(tmp_path):
    path = tmp_path / "hosted-mcp-helper"
    path.write_bytes(b"#!/bin/sh\nexit 0\n")
    path.chmod(0o700)
    return path, hashlib.sha256(path.read_bytes()).hexdigest()


def _profile(*, enabled=True, selectors=None, credentials=None):
    selector_refs = {
        alias: f"secret://hosted-mcp/{index}"
        for index, alias in enumerate(
            (
                official_mcp.TOOLSETS_SELECTOR,
                official_mcp.HELPER_COMMAND_SELECTOR,
                official_mcp.HELPER_SHA256_SELECTOR,
                official_mcp.AUTH_PROFILE_SELECTOR,
            )
        )
    }
    selector_refs.update(selectors or {})
    return SimpleNamespace(
        enabled=enabled,
        endpoint_ref="secret://hosted-mcp/endpoint",
        tls_profile="runtime-trust",
        tls_profile_ref=None,
        credential_refs=credentials or {},
        selector_refs=selector_refs,
    )


def _selectors(command, digest):
    return {
        official_mcp.TOOLSETS_SELECTOR: json.dumps(["inventory_read"]),
        official_mcp.HELPER_COMMAND_SELECTOR: str(command),
        official_mcp.HELPER_SHA256_SELECTOR: digest,
        official_mcp.AUTH_PROFILE_SELECTOR: "interactive-auth",
    }


def test_agent_config_profile_uses_runtime_references_only():
    config = AgentConfig(
        PROVIDER_CONFIGS={
            "runtime-selected": {
                "enabled": False,
                "endpoint_ref": "secret://federation/endpoint",
                "selector_refs": {
                    official_mcp.TOOLSETS_SELECTOR: "secret://federation/toolsets",
                    official_mcp.HELPER_COMMAND_SELECTOR: (
                        "secret://federation/helper-command"
                    ),
                    official_mcp.HELPER_SHA256_SELECTOR: (
                        "secret://federation/helper-sha256"
                    ),
                    official_mcp.AUTH_PROFILE_SELECTOR: (
                        "secret://federation/auth-profile"
                    ),
                },
                "tls_profile_ref": "secret://federation/tls",
            }
        }
    )

    profile = config.provider_configs["runtime-selected"]
    assert profile.enabled is False
    assert profile.endpoint_ref.startswith("secret://")
    assert profile.credential_refs == {}


def test_resolve_returns_redacted_read_only_plan(monkeypatch, tmp_path):
    command, digest = _executable(tmp_path)
    runtime = _Runtime(
        endpoint="https://hosted-mcp.example.invalid/mcp",
        selectors=_selectors(command, digest),
        tls=SimpleNamespace(verify_enabled=True),
    )
    monkeypatch.setattr(
        official_mcp,
        "get_provider_runtime_profile",
        lambda *_args, **_kwargs: _profile(),
    )
    monkeypatch.setattr(
        official_mcp,
        "resolve_provider_runtime_profile",
        lambda *_args, **_kwargs: runtime,
    )

    plan = official_mcp.resolve_official_mcp_federation(
        config=object(), profile_name="runtime-selected"
    )

    assert plan.read_only is True
    assert repr(plan) == "<OfficialMCPFederationPlan redacted>"
    assert plan.allows_tool("read_inventory", {"readOnlyHint": True}) is True
    assert plan.allows_tool("write_inventory", {"readOnlyHint": False}) is False
    assert plan.allows_tool("unannotated", {}) is False
    plan.verify_helper()
    plan.close()
    assert runtime.closed is True
    assert plan.tls is None
    assert plan.allows_tool("read_inventory", {"readOnlyHint": True}) is False


def test_disabled_profile_fails_before_runtime_resolution(monkeypatch):
    monkeypatch.setattr(
        official_mcp,
        "get_provider_runtime_profile",
        lambda *_args, **_kwargs: _profile(enabled=False),
    )
    called = False

    def resolve(*_args, **_kwargs):
        nonlocal called
        called = True

    monkeypatch.setattr(official_mcp, "resolve_provider_runtime_profile", resolve)

    with pytest.raises(
        official_mcp.OfficialMCPFederationError,
        match="^hosted_mcp_profile_disabled$",
    ):
        official_mcp.resolve_official_mcp_federation(
            config=object(), profile_name="runtime-selected"
        )
    assert called is False


@pytest.mark.parametrize(
    "profile",
    [
        _profile(credentials={"TOKEN": "secret://hosted-mcp/token"}),
        _profile(selectors={"UNDECLARED_SELECTOR": "secret://hosted-mcp/value"}),
    ],
)
def test_profile_rejects_secret_projection_and_unknown_selectors(monkeypatch, profile):
    monkeypatch.setattr(
        official_mcp,
        "get_provider_runtime_profile",
        lambda *_args, **_kwargs: profile,
    )

    with pytest.raises(
        official_mcp.OfficialMCPFederationError,
        match="^hosted_mcp_profile_invalid$",
    ):
        official_mcp.resolve_official_mcp_federation(
            config=object(), profile_name="runtime-selected"
        )


def test_helper_integrity_mismatch_closes_resolved_runtime(monkeypatch, tmp_path):
    command, _digest = _executable(tmp_path)
    runtime = _Runtime(
        endpoint="https://hosted-mcp.example.invalid/mcp",
        selectors=_selectors(command, "0" * 64),
        tls=SimpleNamespace(verify_enabled=True),
    )
    monkeypatch.setattr(
        official_mcp,
        "get_provider_runtime_profile",
        lambda *_args, **_kwargs: _profile(),
    )
    monkeypatch.setattr(
        official_mcp,
        "resolve_provider_runtime_profile",
        lambda *_args, **_kwargs: runtime,
    )

    with pytest.raises(
        official_mcp.OfficialMCPFederationError,
        match="^hosted_mcp_helper_integrity_mismatch$",
    ):
        official_mcp.resolve_official_mcp_federation(
            config=object(), profile_name="runtime-selected"
        )
    assert runtime.closed is True


def test_unexpected_runtime_failure_is_redacted_and_closes(monkeypatch, tmp_path):
    command, digest = _executable(tmp_path)
    runtime = _Runtime(
        endpoint="https://hosted-mcp.example.invalid/mcp",
        selectors=_selectors(command, digest),
        tls=SimpleNamespace(verify_enabled=True),
    )
    monkeypatch.setattr(
        official_mcp,
        "get_provider_runtime_profile",
        lambda *_args, **_kwargs: _profile(),
    )
    monkeypatch.setattr(
        official_mcp,
        "resolve_provider_runtime_profile",
        lambda *_args, **_kwargs: runtime,
    )
    monkeypatch.setattr(
        official_mcp,
        "_secure_hosted_endpoint",
        lambda _value: (_ for _ in ()).throw(ValueError("private detail")),
    )

    with pytest.raises(
        official_mcp.OfficialMCPFederationError,
        match="^hosted_mcp_runtime_invalid$",
    ) as exc:
        official_mcp.resolve_official_mcp_federation(
            config=object(), profile_name="runtime-selected"
        )

    assert "private detail" not in str(exc.value)
    assert runtime.closed is True


def test_catalog_fingerprint_includes_only_admitted_tools(monkeypatch, tmp_path):
    command, digest = _executable(tmp_path)
    runtime = _Runtime(
        endpoint="https://hosted-mcp.example.invalid/mcp",
        selectors={
            **_selectors(command, digest),
            official_mcp.READ_ONLY_TOOLS_SELECTOR: json.dumps(["read_inventory"]),
        },
        tls=SimpleNamespace(verify_enabled=True),
    )
    monkeypatch.setattr(
        official_mcp,
        "get_provider_runtime_profile",
        lambda *_args, **_kwargs: _profile(
            selectors={
                official_mcp.READ_ONLY_TOOLS_SELECTOR: (
                    "secret://hosted-mcp/read-only-tools"
                )
            }
        ),
    )
    monkeypatch.setattr(
        official_mcp,
        "resolve_provider_runtime_profile",
        lambda *_args, **_kwargs: runtime,
    )
    plan = official_mcp.resolve_official_mcp_federation(
        config=object(), profile_name="runtime-selected"
    )
    tools = [
        {
            "name": "read_inventory",
            "inputSchema": {"type": "object"},
            "annotations": {"readOnlyHint": True},
        },
        {
            "name": "write_inventory",
            "inputSchema": {"type": "object"},
            "annotations": {"readOnlyHint": False},
        },
    ]

    first = official_mcp.fingerprint_read_only_catalog(plan, tools)
    second = official_mcp.fingerprint_read_only_catalog(plan, list(reversed(tools)))

    assert first == second
    assert len(first) == 64
    plan.close()


def test_toolsets_enforce_hosted_service_bounds(monkeypatch, tmp_path):
    command, digest = _executable(tmp_path)
    selectors = _selectors(command, digest)
    selectors[official_mcp.TOOLSETS_SELECTOR] = json.dumps(
        [f"inventory_{index}" for index in range(11)]
    )
    runtime = _Runtime(
        endpoint="https://hosted-mcp.example.invalid/mcp",
        selectors=selectors,
        tls=SimpleNamespace(verify_enabled=True),
    )
    monkeypatch.setattr(
        official_mcp,
        "get_provider_runtime_profile",
        lambda *_args, **_kwargs: _profile(),
    )
    monkeypatch.setattr(
        official_mcp,
        "resolve_provider_runtime_profile",
        lambda *_args, **_kwargs: runtime,
    )

    with pytest.raises(
        official_mcp.OfficialMCPFederationError,
        match="^hosted_mcp_toolsets_invalid$",
    ):
        official_mcp.resolve_official_mcp_federation(
            config=object(), profile_name="runtime-selected"
        )
    assert runtime.closed is True
