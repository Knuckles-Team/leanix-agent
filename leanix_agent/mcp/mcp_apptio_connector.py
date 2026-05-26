from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_apptio_connector_client,
)


def register_leanix_apptio_connector_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-apptio-connector"})
    async def leanix_leanix_apptio_connector(
        action: str = Field(
            description="Action to perform. Must be one of: 'getallconfigurations', 'upsertconfiguration', 'getconfigurations', 'deleteconfiguration', 'create', 'getresults', 'getresultsurl', 'getstats', 'getstatus', 'getwarnings'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_apptio_connector_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix apptio connector operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "getallconfigurations":
            return client.getallconfigurations(**kwargs)
        if action == "upsertconfiguration":
            return client.upsertconfiguration(**kwargs)
        if action == "getconfigurations":
            return client.getconfigurations(**kwargs)
        if action == "deleteconfiguration":
            return client.deleteconfiguration(**kwargs)
        if action == "create":
            return client.create(**kwargs)
        if action == "getresults":
            return client.getresults(**kwargs)
        if action == "getresultsurl":
            return client.getresultsurl(**kwargs)
        if action == "getstats":
            return client.getstats(**kwargs)
        if action == "getstatus":
            return client.getstatus(**kwargs)
        if action == "getwarnings":
            return client.getwarnings(**kwargs)
        raise ValueError(f"Unknown action: {action}")
