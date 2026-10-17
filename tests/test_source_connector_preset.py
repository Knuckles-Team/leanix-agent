"""SDK ``mcp_tool`` source-adapter coverage for LeanIX cursor pagination."""

from __future__ import annotations

import json
from importlib.resources import files

from agent_connector_sdk.adapters.mcp_tool import McpToolSourceAdapter
from agent_connector_sdk.manifest.presets import ToolPreset
from agent_connector_sdk.manifest.live_contract import validate_preset_tool_contract
from agent_connector_sdk.ports.session import TransportEndpoint
from agent_connector_sdk.transports.mcp import McpTransport
from fastmcp import FastMCP


async def test_leanix_source_preset_drains_every_cursor_page():
    mcp = FastMCP("leanix-source-fixture")
    calls: list[str | None] = []

    @mcp.tool()
    async def leanix_source_factsheets(params_json: str = "{}") -> dict:
        params = json.loads(params_json)
        cursor = params.get("cursor")
        calls.append(cursor)
        if cursor is None:
            return {
                "data": {
                    "data": [
                        {
                            "id": "one",
                            "name": "One",
                            "description": "First",
                            "updatedAt": "2026-07-01T00:00:00Z",
                        }
                    ],
                    "cursor": "page-two",
                    "total": 2,
                },
                "count": 1,
            }
        return {
            "data": {
                "data": [
                    {
                        "id": "two",
                        "name": "Two",
                        "description": "Second",
                        "updatedAt": "2026-07-02T00:00:00Z",
                    }
                ],
                "cursor": None,
                "total": 2,
            },
            "count": 1,
        }

    preset_path = files("leanix_agent.connectors").joinpath("mcp_source_presets.json")
    raw = json.loads(preset_path.read_text(encoding="utf-8"))["leanix-factsheets"]
    preset = ToolPreset(name="leanix-factsheets", **raw)

    async with McpTransport().session(TransportEndpoint(in_process=mcp)) as session:
        observed = validate_preset_tool_contract(
            await session.list_tools(), tool_name=preset.tool, presets=(preset,)
        )
        adapter = McpToolSourceAdapter(
            preset,
            connector="leanix-agent",
            tool_schema_sha256=observed.compatibility_sha256,
            mapping_reference="manifest:leanix-agent#schema_mappings/Document",
        )
        await adapter.discover(session)
        records = []
        checkpoint = None
        while True:
            page = await adapter.extract(session, checkpoint)
            records.extend(page.records)
            checkpoint = page.checkpoint
            if page.exhausted:
                break

    assert calls == [None, "page-two"]
    assert len(records) == 2
