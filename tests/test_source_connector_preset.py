"""Agent-utilities source connector coverage for LeanIX cursor pagination."""

from __future__ import annotations

import json
from importlib.resources import files

from agent_utilities.protocols.source_connectors.connectors.mcp_tool import (
    McpToolSourceConnector,
)
from fastmcp import FastMCP


def test_leanix_source_preset_drains_every_cursor_page():
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
    preset = json.loads(preset_path.read_text(encoding="utf-8"))["leanix-factsheets"]
    connector = McpToolSourceConnector(client=mcp, **preset)

    documents = list(connector.load())

    assert calls == [None, "page-two"]
    assert [document.id for document in documents] == ["one", "two"]
    assert [document.title for document in documents] == ["One", "Two"]
    assert [document.text for document in documents] == ["First", "Second"]
