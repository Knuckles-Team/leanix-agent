from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_automations_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_AUTOMATIONS_ACTIONS = frozenset(
    {
        "templatescontroller_getalltemplates",
        "templatescontroller_createtemplate",
        "templatescontroller_gettemplate",
        "templatescontroller_updatetemplate",
        "templatescontroller_patchtemplate",
        "templatescontroller_deletetemplate",
        "instancescontroller_findall",
        "instancescontroller_quota",
        "statisticscontroller_getstatistics",
        "snapshotscontroller_managesnapshotrequests",
        "snapshotscontroller_managedrestorationrequests",
        "scriptscontroller_createmcescript",
        "scriptscontroller_updatemcescript",
    }
)


def register_leanix_automations_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-automations"})
    async def leanix_leanix_automations(
        action: str = Field(
            description="Action to perform. Must be one of: 'templatescontroller_getalltemplates', 'templatescontroller_createtemplate', 'templatescontroller_gettemplate', 'templatescontroller_updatetemplate', 'templatescontroller_patchtemplate', 'templatescontroller_deletetemplate', 'instancescontroller_findall', 'instancescontroller_quota', 'statisticscontroller_getstatistics', 'snapshotscontroller_managesnapshotrequests', 'snapshotscontroller_managedrestorationrequests', 'scriptscontroller_createmcescript', 'scriptscontroller_updatemcescript'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_automations_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix automations operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(
            client, action, kwargs, allowed=_AUTOMATIONS_ACTIONS
        )
