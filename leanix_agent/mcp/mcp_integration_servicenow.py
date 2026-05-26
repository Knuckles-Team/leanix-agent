from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_integration_servicenow_client,
)


def register_leanix_integration_servicenow_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-integration-servicenow"})
    async def leanix_leanix_integration_servicenow(
        action: str = Field(
            description="Action to perform. Must be one of: 'getaggregatedfactsheetsummary', 'getaggregatedsoftwareinformation', 'getservicenowaggregatedsoftware', 'getfilterforfactsheet', 'getfilterforprovider', 'getfiltersforhardware', 'getservicenowaggregatedhardware', 'getstatusoverview', 'getallconfigurations', 'createconfiguration', 'getconfiguration', 'updateconfiguration', 'deleteconfiguration', 'synchronize', 'validateconfiguration', 'validateservicenowcredentials', 'getfilters', 'getservicenowsyncconstraintrules', 'getavailablerelcirelations', 'getinstalledservicenowpluginversion', 'getmappingtablerelations', 'getreferencefieldrelations', 'getservicenowmetadata', 'gettables', 'changes', 'hooks', 'sendprompt', 'sendpromptv2', 'abortallpendingandrunningsynchronizations', 'abortsynchronization', 'getcurrentlyrunningorlastcreatedrun', 'getversionbyid', 'getversions'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_integration_servicenow_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix integration servicenow operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "getaggregatedfactsheetsummary":
            return client.getaggregatedfactsheetsummary(**kwargs)
        if action == "getaggregatedsoftwareinformation":
            return client.getaggregatedsoftwareinformation(**kwargs)
        if action == "getservicenowaggregatedsoftware":
            return client.getservicenowaggregatedsoftware(**kwargs)
        if action == "getfilterforfactsheet":
            return client.getfilterforfactsheet(**kwargs)
        if action == "getfilterforprovider":
            return client.getfilterforprovider(**kwargs)
        if action == "getfiltersforhardware":
            return client.getfiltersforhardware(**kwargs)
        if action == "getservicenowaggregatedhardware":
            return client.getservicenowaggregatedhardware(**kwargs)
        if action == "getstatusoverview":
            return client.getstatusoverview(**kwargs)
        if action == "getallconfigurations":
            return client.getallconfigurations(**kwargs)
        if action == "createconfiguration":
            return client.createconfiguration(**kwargs)
        if action == "getconfiguration":
            return client.getconfiguration(**kwargs)
        if action == "updateconfiguration":
            return client.updateconfiguration(**kwargs)
        if action == "deleteconfiguration":
            return client.deleteconfiguration(**kwargs)
        if action == "synchronize":
            return client.synchronize(**kwargs)
        if action == "validateconfiguration":
            return client.validateconfiguration(**kwargs)
        if action == "validateservicenowcredentials":
            return client.validateservicenowcredentials(**kwargs)
        if action == "getfilters":
            return client.getfilters(**kwargs)
        if action == "getservicenowsyncconstraintrules":
            return client.getservicenowsyncconstraintrules(**kwargs)
        if action == "getavailablerelcirelations":
            return client.getavailablerelcirelations(**kwargs)
        if action == "getinstalledservicenowpluginversion":
            return client.getinstalledservicenowpluginversion(**kwargs)
        if action == "getmappingtablerelations":
            return client.getmappingtablerelations(**kwargs)
        if action == "getreferencefieldrelations":
            return client.getreferencefieldrelations(**kwargs)
        if action == "getservicenowmetadata":
            return client.getservicenowmetadata(**kwargs)
        if action == "gettables":
            return client.gettables(**kwargs)
        if action == "changes":
            return client.changes(**kwargs)
        if action == "hooks":
            return client.hooks(**kwargs)
        if action == "sendprompt":
            return client.sendprompt(**kwargs)
        if action == "sendpromptv2":
            return client.sendpromptv2(**kwargs)
        if action == "abortallpendingandrunningsynchronizations":
            return client.abortallpendingandrunningsynchronizations(**kwargs)
        if action == "abortsynchronization":
            return client.abortsynchronization(**kwargs)
        if action == "getcurrentlyrunningorlastcreatedrun":
            return client.getcurrentlyrunningorlastcreatedrun(**kwargs)
        if action == "getversionbyid":
            return client.getversionbyid(**kwargs)
        if action == "getversions":
            return client.getversions(**kwargs)
        raise ValueError(f"Unknown action: {action}")
