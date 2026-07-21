"""Declarative hosted-MCP preset remains environment-neutral and fail closed."""

from __future__ import annotations

import json
from importlib.resources import files


def test_official_mcp_preset_is_reference_only_and_read_only():
    path = files("leanix_agent.connectors").joinpath("official_mcp_federation.json")
    preset = json.loads(path.read_text(encoding="utf-8"))
    configuration = preset["configuration"]

    assert configuration["source"] == "AgentConfig.provider_configs"
    assert configuration["default_enabled"] is False
    assert configuration["credential_fields_allowed"] == []
    assert preset["execution"]["downloads_allowed"] is False
    assert preset["execution"]["shell_allowed"] is False
    assert preset["policy"]["access_mode"] == "read_only"
    assert preset["policy"]["tool_annotation_required_value"] is True

    serialized = json.dumps(preset, sort_keys=True).casefold()
    assert "http://" not in serialized
    assert "https://" not in serialized
    assert "npx" not in serialized
    assert "node_extra_ca_certs" not in serialized
    assert "workspace" not in serialized
