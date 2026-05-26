from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_automations_client,
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
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "templatescontroller_getalltemplates":
            return client.templatescontroller_getalltemplates(**kwargs)
        if action == "templatescontroller_createtemplate":
            return client.templatescontroller_createtemplate(**kwargs)
        if action == "templatescontroller_gettemplate":
            return client.templatescontroller_gettemplate(**kwargs)
        if action == "templatescontroller_updatetemplate":
            return client.templatescontroller_updatetemplate(**kwargs)
        if action == "templatescontroller_patchtemplate":
            return client.templatescontroller_patchtemplate(**kwargs)
        if action == "templatescontroller_deletetemplate":
            return client.templatescontroller_deletetemplate(**kwargs)
        if action == "instancescontroller_findall":
            return client.instancescontroller_findall(**kwargs)
        if action == "instancescontroller_quota":
            return client.instancescontroller_quota(**kwargs)
        if action == "statisticscontroller_getstatistics":
            return client.statisticscontroller_getstatistics(**kwargs)
        if action == "snapshotscontroller_managesnapshotrequests":
            return client.snapshotscontroller_managesnapshotrequests(**kwargs)
        if action == "snapshotscontroller_managedrestorationrequests":
            return client.snapshotscontroller_managedrestorationrequests(**kwargs)
        if action == "scriptscontroller_createmcescript":
            return client.scriptscontroller_createmcescript(**kwargs)
        if action == "scriptscontroller_updatemcescript":
            return client.scriptscontroller_updatemcescript(**kwargs)
        raise ValueError(f"Unknown action: {action}")
