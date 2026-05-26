from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_reference_data_client,
)


def register_leanix_reference_data_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-reference-data"})
    async def leanix_leanix_reference_data(
        action: str = Field(
            description="Action to perform. Must be one of: 'gettbmtaxonomy', 'getfactsheetsbysourcename', 'getlatestrecommendationrun', 'putusedtechnolotrecommendationcontroller', 'getusedtechnolotrecommendationcontroller', 'get_source_name_fact_sheets_id', 'getlinksbysourcename', 'putlinksbysourcename', 'putsourcehierarchylinkcontroller', 'putbulklinksbysourcename', 'putbulksourcehierarchylinkscontroller', 'getlinksbyfactsheettype', 'getlinkbysourcename', 'deletelinkbysourcename', 'getrequests', 'putrequests', 'getrequestscount', 'getrefresh', 'getrefreshes', 'postrefresh', 'refreshltlslinks', 'batchlinks', 'clonelinks', 'getlink', 'getconfigurationmodels', 'getconfiguration', 'putconfiguration', 'getsaasconfiguration', 'putsaasconfiguration', 'gettechcategoryconfiguration', 'puttechcategoryconfiguration', 'getbuscapconfiguration', 'putbuscapconfiguration', 'getprovisioning', 'putprovisioning', 'getlinks', 'clearduplicatelinks', 'validatelink', 'gettbmmigrationstatus', 'tbmmigrationstatusupdate', 'startmappingexport', 'getexportstatus', 'getexportfile', 'putimporttbm', 'precomputedrecommendations', 'getbusinesscapability', 'postbusinesscapability', 'filteredfactsheetscount', 'post_jobs', 'get_jobs', 'fetchbusinesscapabilitymetrics', 'post_managedsnapshotrequests', 'post_managedrestorationrequests'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_reference_data_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix reference data operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "gettbmtaxonomy":
            return client.gettbmtaxonomy(**kwargs)
        if action == "getfactsheetsbysourcename":
            return client.getfactsheetsbysourcename(**kwargs)
        if action == "getlatestrecommendationrun":
            return client.getlatestrecommendationrun(**kwargs)
        if action == "putusedtechnolotrecommendationcontroller":
            return client.putusedtechnolotrecommendationcontroller(**kwargs)
        if action == "getusedtechnolotrecommendationcontroller":
            return client.getusedtechnolotrecommendationcontroller(**kwargs)
        if action == "get_source_name_fact_sheets_id":
            return client.get_source_name_fact_sheets_id(**kwargs)
        if action == "getlinksbysourcename":
            return client.getlinksbysourcename(**kwargs)
        if action == "putlinksbysourcename":
            return client.putlinksbysourcename(**kwargs)
        if action == "putsourcehierarchylinkcontroller":
            return client.putsourcehierarchylinkcontroller(**kwargs)
        if action == "putbulklinksbysourcename":
            return client.putbulklinksbysourcename(**kwargs)
        if action == "putbulksourcehierarchylinkscontroller":
            return client.putbulksourcehierarchylinkscontroller(**kwargs)
        if action == "getlinksbyfactsheettype":
            return client.getlinksbyfactsheettype(**kwargs)
        if action == "getlinkbysourcename":
            return client.getlinkbysourcename(**kwargs)
        if action == "deletelinkbysourcename":
            return client.deletelinkbysourcename(**kwargs)
        if action == "getrequests":
            return client.getrequests(**kwargs)
        if action == "putrequests":
            return client.putrequests(**kwargs)
        if action == "getrequestscount":
            return client.getrequestscount(**kwargs)
        if action == "getrefresh":
            return client.getrefresh(**kwargs)
        if action == "getrefreshes":
            return client.getrefreshes(**kwargs)
        if action == "postrefresh":
            return client.postrefresh(**kwargs)
        if action == "refreshltlslinks":
            return client.refreshltlslinks(**kwargs)
        if action == "batchlinks":
            return client.batchlinks(**kwargs)
        if action == "clonelinks":
            return client.clonelinks(**kwargs)
        if action == "getlink":
            return client.getlink(**kwargs)
        if action == "getconfigurationmodels":
            return client.getconfigurationmodels(**kwargs)
        if action == "getconfiguration":
            return client.getconfiguration(**kwargs)
        if action == "putconfiguration":
            return client.putconfiguration(**kwargs)
        if action == "getsaasconfiguration":
            return client.getsaasconfiguration(**kwargs)
        if action == "putsaasconfiguration":
            return client.putsaasconfiguration(**kwargs)
        if action == "gettechcategoryconfiguration":
            return client.gettechcategoryconfiguration(**kwargs)
        if action == "puttechcategoryconfiguration":
            return client.puttechcategoryconfiguration(**kwargs)
        if action == "getbuscapconfiguration":
            return client.getbuscapconfiguration(**kwargs)
        if action == "putbuscapconfiguration":
            return client.putbuscapconfiguration(**kwargs)
        if action == "getprovisioning":
            return client.getprovisioning(**kwargs)
        if action == "putprovisioning":
            return client.putprovisioning(**kwargs)
        if action == "getlinks":
            return client.getlinks(**kwargs)
        if action == "clearduplicatelinks":
            return client.clearduplicatelinks(**kwargs)
        if action == "validatelink":
            return client.validatelink(**kwargs)
        if action == "gettbmmigrationstatus":
            return client.gettbmmigrationstatus(**kwargs)
        if action == "tbmmigrationstatusupdate":
            return client.tbmmigrationstatusupdate(**kwargs)
        if action == "startmappingexport":
            return client.startmappingexport(**kwargs)
        if action == "getexportstatus":
            return client.getexportstatus(**kwargs)
        if action == "getexportfile":
            return client.getexportfile(**kwargs)
        if action == "putimporttbm":
            return client.putimporttbm(**kwargs)
        if action == "precomputedrecommendations":
            return client.precomputedrecommendations(**kwargs)
        if action == "getbusinesscapability":
            return client.getbusinesscapability(**kwargs)
        if action == "postbusinesscapability":
            return client.postbusinesscapability(**kwargs)
        if action == "filteredfactsheetscount":
            return client.filteredfactsheetscount(**kwargs)
        if action == "post_jobs":
            return client.post_jobs(**kwargs)
        if action == "get_jobs":
            return client.get_jobs(**kwargs)
        if action == "fetchbusinesscapabilitymetrics":
            return client.fetchbusinesscapabilitymetrics(**kwargs)
        if action == "post_managedsnapshotrequests":
            return client.post_managedsnapshotrequests(**kwargs)
        if action == "post_managedrestorationrequests":
            return client.post_managedrestorationrequests(**kwargs)
        raise ValueError(f"Unknown action: {action}")
