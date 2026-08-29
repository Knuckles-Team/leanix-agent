from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_navigation_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_NAVIGATION_ACTIONS = frozenset(
    {
        "getallcollectiongroups",
        "createcollectiongroup",
        "batchputcollectiongroups",
        "getcollectiongroupbyid",
        "putcollectiongroupbyid",
        "deletecollectiongroupbyid",
        "postcollection",
        "getcollections",
        "putcollection",
        "deletecollection",
        "putcollectionnavigationitem",
        "postcollectionnavigationitem",
        "deletecollectionnavigationitem",
        "getcollectionfolders",
        "postfoldercontroller",
        "updatefoldercontroller",
        "executebatchmove",
        "executebatchdelete",
        "searchnavigationitem",
        "getnavigationitemfavorite",
        "postnavigationitemfavorite",
        "deletenavigationitemfavorite",
        "createslide",
        "putslidebyid",
        "deleteslidebyid",
        "searchpresentation",
        "createpresentation",
        "getpresentationbyid",
        "putpresentationbyid",
        "deletepresentationbyid",
        "getpresentationsharesbyid",
        "sharepresentation",
        "deletepresentationsharebyid",
    }
)


def register_leanix_navigation_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-navigation"})
    async def leanix_leanix_navigation(
        action: str = Field(
            description="Action to perform. Must be one of: 'getallcollectiongroups', 'createcollectiongroup', 'batchputcollectiongroups', 'getcollectiongroupbyid', 'putcollectiongroupbyid', 'deletecollectiongroupbyid', 'postcollection', 'getcollections', 'putcollection', 'deletecollection', 'putcollectionnavigationitem', 'postcollectionnavigationitem', 'deletecollectionnavigationitem', 'getcollectionfolders', 'postfoldercontroller', 'updatefoldercontroller', 'executebatchmove', 'executebatchdelete', 'searchnavigationitem', 'getnavigationitemfavorite', 'postnavigationitemfavorite', 'deletenavigationitemfavorite', 'createslide', 'putslidebyid', 'deleteslidebyid', 'searchpresentation', 'createpresentation', 'getpresentationbyid', 'putpresentationbyid', 'deletepresentationbyid', 'getpresentationsharesbyid', 'sharepresentation', 'deletepresentationsharebyid'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_navigation_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix navigation operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(
            client, action, kwargs, allowed=_NAVIGATION_ACTIONS
        )
