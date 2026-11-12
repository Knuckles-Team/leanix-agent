from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

from leanix_agent.auth import get_pathfinder_client


def register_leanix_pathfinder_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-pathfinder"})
    async def leanix_discover_meta_model(
        fact_sheet_type: str | None = Field(
            default=None,
            description="Optional specific Fact Sheet type to discover (e.g. 'Application', 'ITComponent'). If omitted, retrieves the root meta model.",
        ),
        client=Depends(get_pathfinder_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Discover the custom LeanIX meta-model/data-model schema including custom attributes and fields in real-time."""
        if ctx:
            await ctx.info("Retrieving dynamic LeanIX meta-model...")
        try:
            if fact_sheet_type:
                return client.get_meta_model_for_type(fact_sheet_type=fact_sheet_type)
            return client.get_meta_model_root()
        except Exception as e:
            return {
                "error": f"Failed to retrieve dynamic meta-model: {type(e).__name__}"
            }
