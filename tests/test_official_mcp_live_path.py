"""The official hosted federation executes through GraphOS's live child path."""

from __future__ import annotations

import contextlib
import hashlib
import json
from types import SimpleNamespace

import pytest
from agent_utilities.core.provider_runtime import ResolvedProviderRuntime
from agent_utilities.mcp import multiplexer as multiplexer_module
from agent_utilities.mcp.multiplexer import MCPMultiplexer

from leanix_agent import official_mcp


class _Session:
    async def initialize(self):
        return None

    async def list_tools(self):
        return SimpleNamespace(
            tools=[
                SimpleNamespace(
                    name="read_inventory",
                    description="read",
                    inputSchema={"type": "object"},
                    annotations={"readOnlyHint": True},
                    meta=None,
                ),
                SimpleNamespace(
                    name="write_inventory",
                    description="write",
                    inputSchema={"type": "object"},
                    annotations={"readOnlyHint": False},
                    meta=None,
                ),
            ]
        )


class _SessionContext:
    async def __aenter__(self):
        return _Session()

    async def __aexit__(self, *_exc):
        return False


@pytest.mark.asyncio
async def test_official_policy_runs_through_multiplexer_and_closes(
    monkeypatch, tmp_path
):
    helper = tmp_path / "hosted-helper"
    helper.write_bytes(b"#!/bin/sh\nexit 0\n")
    helper.chmod(0o700)
    digest = hashlib.sha256(helper.read_bytes()).hexdigest()
    cleaned: list[str] = []
    tls = SimpleNamespace(
        verify_enabled=True,
        cleanup=lambda: cleaned.append("tls"),
        system_trust=True,
        trust_env=False,
        ca_bundle_path=None,
        ca_directory=None,
        client_cert_path=None,
        client_key_path=None,
        client_key_password=None,
        proxy_url=None,
        no_proxy=None,
    )
    runtime = ResolvedProviderRuntime(
        endpoint="https://provider.example.invalid/mcp",
        selectors={
            official_mcp.TOOLSETS_SELECTOR: json.dumps(["inventory_read"]),
            official_mcp.HELPER_COMMAND_SELECTOR: str(helper),
            official_mcp.HELPER_SHA256_SELECTOR: digest,
            official_mcp.AUTH_PROFILE_SELECTOR: "interactive-auth",
            official_mcp.READ_ONLY_TOOLS_SELECTOR: json.dumps(["read_inventory"]),
        },
        tls=tls,
    )
    plan = official_mcp.OfficialMCPFederationPlan(
        endpoint=runtime.endpoint or "",
        toolsets=("inventory_read",),
        helper_command=helper,
        helper_sha256=digest,
        auth_profile="interactive-auth",
        read_only_tools=frozenset({"read_inventory"}),
        tls=tls,
        _runtime=runtime,
    )
    monkeypatch.setattr(
        official_mcp,
        "resolve_official_mcp_federation",
        lambda **_kwargs: plan,
    )
    monkeypatch.setattr(
        multiplexer_module,
        "_load_runtime_child_policy_factory",
        lambda name: (
            official_mcp.create_official_mcp_child_policy
            if name == "leanix-official"
            else None
        ),
    )

    events: list[str] = []
    original_verify = official_mcp.OfficialMCPFederationPlan.verify_helper

    def verify(self):
        events.append("verify")
        original_verify(self)

    monkeypatch.setattr(
        official_mcp.OfficialMCPFederationPlan,
        "verify_helper",
        verify,
    )

    @contextlib.asynccontextmanager
    async def stdio_client(params, *, errlog=None):
        assert errlog is not None
        assert params.command == str(helper)
        assert params.args == []
        assert (
            params.env["AGENT_PROVIDER_RUNTIME_ENDPOINT"]
            == "https://provider.example.invalid/mcp"
        )
        child_config = json.loads(params.env["PROVIDER_CONFIGS"])
        child_profile = child_config["deployment-profile"]
        assert child_profile["credential_refs"] == {}
        assert set(child_profile["selector_refs"]) == set(runtime.selectors)
        assert child_profile["tls_profile_ref"].startswith("env://")
        events.append("spawn")
        try:
            yield ("read", "write")
        finally:
            events.append("child-close")

    monkeypatch.setattr(multiplexer_module, "stdio_client", stdio_client)
    monkeypatch.setattr(
        multiplexer_module,
        "ClientSession",
        lambda *_args, **_kwargs: _SessionContext(),
    )

    mux = MCPMultiplexer(tmp_path / "mcp_config.json")
    result = await mux._start_child(
        "enterprise-architecture-hosted",
        {
            "runtime_policy": "leanix-official",
            "provider_profile": "deployment-profile",
        },
    )

    assert result is not None
    server_name, child, tools, config = result
    assert [tool.name for tool in tools] == ["read_inventory"]
    assert events[:2] == ["verify", "spawn"]
    mux._register_child_result(server_name, child, tools, config)
    fingerprint = mux.status_snapshot()["children"][server_name]["catalog_fingerprint"]
    assert len(fingerprint) == 64

    await mux.aclose()
    assert events.index("child-close") < len(events)
    assert cleaned == ["tls"]
    assert plan.allows_tool("read_inventory", {"readOnlyHint": True}) is False
