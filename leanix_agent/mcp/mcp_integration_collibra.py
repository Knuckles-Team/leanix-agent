from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_integration_collibra_client,
)


def register_leanix_integration_collibra_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-integration-collibra"})
    async def leanix_leanix_integration_collibra(
        action: str = Field(
            description="Action to perform. Must be one of: 'createsynchronizationrun', 'getconfigurations', 'createconfiguration', 'getconfigurationbyid', 'updateconfiguration', 'deleteconfiguration', 'getoverview', 'getstatus', 'getfeaturetoggles', 'getfields', 'getrelationfields', 'getrelations', 'getsubscriptionroles', 'getcredentials', 'createcollibracredentials', 'getcollibracredentialsbyid', 'updatecollibracredentials', 'validatecollibracredentialsbyid', 'getattributetypesforassettype', 'getattributetypesforassettypebyscope', 'getassetstatuses', 'getassettypes', 'getattributetypes', 'getcommunities', 'getcomplexrelationtypes', 'getdomains', 'getrelationtypes', 'getresourceroles', 'getresponsibilityroles'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_integration_collibra_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix integration collibra operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "createsynchronizationrun":
            return client.createsynchronizationrun(**kwargs)
        if action == "getconfigurations":
            return client.getconfigurations(**kwargs)
        if action == "createconfiguration":
            return client.createconfiguration(**kwargs)
        if action == "getconfigurationbyid":
            return client.getconfigurationbyid(**kwargs)
        if action == "updateconfiguration":
            return client.updateconfiguration(**kwargs)
        if action == "deleteconfiguration":
            return client.deleteconfiguration(**kwargs)
        if action == "getoverview":
            return client.getoverview(**kwargs)
        if action == "getstatus":
            return client.getstatus(**kwargs)
        if action == "getfeaturetoggles":
            return client.getfeaturetoggles(**kwargs)
        if action == "getfields":
            return client.getfields(**kwargs)
        if action == "getrelationfields":
            return client.getrelationfields(**kwargs)
        if action == "getrelations":
            return client.getrelations(**kwargs)
        if action == "getsubscriptionroles":
            return client.getsubscriptionroles(**kwargs)
        if action == "getcredentials":
            return client.getcredentials(**kwargs)
        if action == "createcollibracredentials":
            return client.createcollibracredentials(**kwargs)
        if action == "getcollibracredentialsbyid":
            return client.getcollibracredentialsbyid(**kwargs)
        if action == "updatecollibracredentials":
            return client.updatecollibracredentials(**kwargs)
        if action == "validatecollibracredentialsbyid":
            return client.validatecollibracredentialsbyid(**kwargs)
        if action == "getattributetypesforassettype":
            return client.getattributetypesforassettype(**kwargs)
        if action == "getattributetypesforassettypebyscope":
            return client.getattributetypesforassettypebyscope(**kwargs)
        if action == "getassetstatuses":
            return client.getassetstatuses(**kwargs)
        if action == "getassettypes":
            return client.getassettypes(**kwargs)
        if action == "getattributetypes":
            return client.getattributetypes(**kwargs)
        if action == "getcommunities":
            return client.getcommunities(**kwargs)
        if action == "getcomplexrelationtypes":
            return client.getcomplexrelationtypes(**kwargs)
        if action == "getdomains":
            return client.getdomains(**kwargs)
        if action == "getrelationtypes":
            return client.getrelationtypes(**kwargs)
        if action == "getresourceroles":
            return client.getresourceroles(**kwargs)
        if action == "getresponsibilityroles":
            return client.getresponsibilityroles(**kwargs)
        raise ValueError(f"Unknown action: {action}")
