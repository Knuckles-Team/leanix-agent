"""MCP tools for current LeanIX ontology discovery and governed graph sync."""

from __future__ import annotations

import json
from typing import Any

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from leanix_agent.auth import get_client, get_graphql_client

_MAX_IDS_JSON_BYTES = 256 * 1024
_MAX_IDS = 1_000


def register_instance_graph_tools(mcp: FastMCP) -> None:
    """Register live metamodel and native ChangeEnvelope synchronization tools."""

    @mcp.tool(tags={"leanix-metamodel", "ontology", "discovery"})
    async def leanix_generate_instance_ontology(
        include_turtle: bool = Field(
            default=True,
            description="Return the privacy-sanitized generated Turtle ontology.",
        ),
        client=Depends(get_client),
        ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Compile the current live data model to deterministic OWL, SHACL, and SKOS."""
        from leanix_agent.metamodel import (
            compile_instance_ontology,
            discover_meta_model,
        )

        if ctx:
            await ctx.info("Compiling the configured LeanIX data model")
        try:
            artifact = compile_instance_ontology(discover_meta_model(client))
        except Exception as exc:  # noqa: BLE001 - bounded MCP error
            return {
                "error": "LeanIX ontology generation failed",
                "errorType": type(exc).__name__,
            }
        result = artifact.model_dump(exclude={"meta_model"})
        if not include_turtle:
            result.pop("turtle", None)
        return result

    @mcp.tool(tags={"leanix-kg", "ontology", "full-sync"})
    async def leanix_sync_instance_to_graph(
        mode: str = Field(
            default="full",
            description="Synchronization mode: full, delta, or reconcile.",
        ),
        ids_json: str = Field(
            default="[]",
            description="Optional bounded JSON array of FactSheet IDs for a delta.",
        ),
        page_size: int = Field(
            default=500,
            ge=1,
            le=1_000,
            description="FactSheets read per bounded upstream page.",
        ),
        client=Depends(get_client),
        graphql_client=Depends(get_graphql_client),
        ctx: Context | None = None,
    ) -> dict[str, Any]:
        """Load the generated ontology and stream records through ChangeEnvelope."""
        try:
            if len(ids_json.encode("utf-8")) > _MAX_IDS_JSON_BYTES:
                raise ValueError("ids_json exceeds the size limit")
            parsed_ids = json.loads(ids_json)
            if (
                not isinstance(parsed_ids, list)
                or len(parsed_ids) > _MAX_IDS
                or not all(isinstance(value, str) and value for value in parsed_ids)
            ):
                raise ValueError("ids_json must be a bounded array of strings")
        except (json.JSONDecodeError, ValueError):
            return {
                "error": "LeanIX sync request validation failed",
                "errorType": "ValidationError",
            }
        if ctx:
            await ctx.info("Starting governed LeanIX synchronization")
        try:
            from leanix_agent.instance_sync import sync_instance

            report = sync_instance(
                client,
                graphql_client,
                mode=mode,
                ids=parsed_ids or None,
                page_size=page_size,
            )
            return report.model_dump()
        except Exception as exc:  # noqa: BLE001 - bounded MCP error
            return {
                "error": "LeanIX graph synchronization failed",
                "errorType": type(exc).__name__,
            }
