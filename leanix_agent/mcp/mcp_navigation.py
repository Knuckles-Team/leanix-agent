from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_navigation_client,
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
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "getallcollectiongroups":
            return client.getallcollectiongroups(**kwargs)
        if action == "createcollectiongroup":
            return client.createcollectiongroup(**kwargs)
        if action == "batchputcollectiongroups":
            return client.batchputcollectiongroups(**kwargs)
        if action == "getcollectiongroupbyid":
            return client.getcollectiongroupbyid(**kwargs)
        if action == "putcollectiongroupbyid":
            return client.putcollectiongroupbyid(**kwargs)
        if action == "deletecollectiongroupbyid":
            return client.deletecollectiongroupbyid(**kwargs)
        if action == "postcollection":
            return client.postcollection(**kwargs)
        if action == "getcollections":
            return client.getcollections(**kwargs)
        if action == "putcollection":
            return client.putcollection(**kwargs)
        if action == "deletecollection":
            return client.deletecollection(**kwargs)
        if action == "putcollectionnavigationitem":
            return client.putcollectionnavigationitem(**kwargs)
        if action == "postcollectionnavigationitem":
            return client.postcollectionnavigationitem(**kwargs)
        if action == "deletecollectionnavigationitem":
            return client.deletecollectionnavigationitem(**kwargs)
        if action == "getcollectionfolders":
            return client.getcollectionfolders(**kwargs)
        if action == "postfoldercontroller":
            return client.postfoldercontroller(**kwargs)
        if action == "updatefoldercontroller":
            return client.updatefoldercontroller(**kwargs)
        if action == "executebatchmove":
            return client.executebatchmove(**kwargs)
        if action == "executebatchdelete":
            return client.executebatchdelete(**kwargs)
        if action == "searchnavigationitem":
            return client.searchnavigationitem(**kwargs)
        if action == "getnavigationitemfavorite":
            return client.getnavigationitemfavorite(**kwargs)
        if action == "postnavigationitemfavorite":
            return client.postnavigationitemfavorite(**kwargs)
        if action == "deletenavigationitemfavorite":
            return client.deletenavigationitemfavorite(**kwargs)
        if action == "createslide":
            return client.createslide(**kwargs)
        if action == "putslidebyid":
            return client.putslidebyid(**kwargs)
        if action == "deleteslidebyid":
            return client.deleteslidebyid(**kwargs)
        if action == "searchpresentation":
            return client.searchpresentation(**kwargs)
        if action == "createpresentation":
            return client.createpresentation(**kwargs)
        if action == "getpresentationbyid":
            return client.getpresentationbyid(**kwargs)
        if action == "putpresentationbyid":
            return client.putpresentationbyid(**kwargs)
        if action == "deletepresentationbyid":
            return client.deletepresentationbyid(**kwargs)
        if action == "getpresentationsharesbyid":
            return client.getpresentationsharesbyid(**kwargs)
        if action == "sharepresentation":
            return client.sharepresentation(**kwargs)
        if action == "deletepresentationsharebyid":
            return client.deletepresentationsharebyid(**kwargs)
        raise ValueError(f"Unknown action: {action}")
