from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_technology_discovery_client,
)


def register_leanix_technology_discovery_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-technology-discovery"})
    async def leanix_leanix_technology_discovery(
        action: str = Field(
            description="Action to perform. Must be one of: 'leanix_v1_microservice_discovery_yaml_manifest_register', 'leanix_v1_factsheets_sboms_ingest', 'leanix_v1_factsheets_sboms_ingest_1', 'getcomponentsbyapplication', 'searchcomponentsbypurl', 'getalltechstacks', 'updatetechstackbyqueryparam', 'createtechstack', 'deletetechstackbyqueryparam', 'previewmatches', 'gettechstackdetailsbyqueryparam', 'getaggregatedcounts', 'getfactsheetsbylibrary', 'getlibraryusagedetails', 'getversionsbylibrary', 'getlibraries'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_technology_discovery_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix technology discovery operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "leanix_v1_microservice_discovery_yaml_manifest_register":
            return client.leanix_v1_microservice_discovery_yaml_manifest_register(
                **kwargs
            )
        if action == "leanix_v1_factsheets_sboms_ingest":
            return client.leanix_v1_factsheets_sboms_ingest(**kwargs)
        if action == "leanix_v1_factsheets_sboms_ingest_1":
            return client.leanix_v1_factsheets_sboms_ingest_1(**kwargs)
        if action == "getcomponentsbyapplication":
            return client.getcomponentsbyapplication(**kwargs)
        if action == "searchcomponentsbypurl":
            return client.searchcomponentsbypurl(**kwargs)
        if action == "getalltechstacks":
            return client.getalltechstacks(**kwargs)
        if action == "updatetechstackbyqueryparam":
            return client.updatetechstackbyqueryparam(**kwargs)
        if action == "createtechstack":
            return client.createtechstack(**kwargs)
        if action == "deletetechstackbyqueryparam":
            return client.deletetechstackbyqueryparam(**kwargs)
        if action == "previewmatches":
            return client.previewmatches(**kwargs)
        if action == "gettechstackdetailsbyqueryparam":
            return client.gettechstackdetailsbyqueryparam(**kwargs)
        if action == "getaggregatedcounts":
            return client.getaggregatedcounts(**kwargs)
        if action == "getfactsheetsbylibrary":
            return client.getfactsheetsbylibrary(**kwargs)
        if action == "getlibraryusagedetails":
            return client.getlibraryusagedetails(**kwargs)
        if action == "getversionsbylibrary":
            return client.getversionsbylibrary(**kwargs)
        if action == "getlibraries":
            return client.getlibraries(**kwargs)
        raise ValueError(f"Unknown action: {action}")
