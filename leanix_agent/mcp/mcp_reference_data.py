from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_reference_data_client,
)

_REFERENCE_DATA_ACTIONS = frozenset(
    {
        "gettbmtaxonomy",
        "getfactsheetsbysourcename",
        "getlatestrecommendationrun",
        "putusedtechnolotrecommendationcontroller",
        "getusedtechnolotrecommendationcontroller",
        "get_source_name_fact_sheets_id",
        "getlinksbysourcename",
        "putlinksbysourcename",
        "putsourcehierarchylinkcontroller",
        "putbulklinksbysourcename",
        "putbulksourcehierarchylinkscontroller",
        "getlinksbyfactsheettype",
        "getlinkbysourcename",
        "deletelinkbysourcename",
        "getrequests",
        "putrequests",
        "getrequestscount",
        "getrefresh",
        "getrefreshes",
        "postrefresh",
        "refreshltlslinks",
        "batchlinks",
        "clonelinks",
        "getlink",
        "getconfigurationmodels",
        "getconfiguration",
        "putconfiguration",
        "getsaasconfiguration",
        "putsaasconfiguration",
        "gettechcategoryconfiguration",
        "puttechcategoryconfiguration",
        "getbuscapconfiguration",
        "putbuscapconfiguration",
        "getprovisioning",
        "putprovisioning",
        "getlinks",
        "clearduplicatelinks",
        "validatelink",
        "gettbmmigrationstatus",
        "tbmmigrationstatusupdate",
        "startmappingexport",
        "getexportstatus",
        "getexportfile",
        "putimporttbm",
        "precomputedrecommendations",
        "getbusinesscapability",
        "postbusinesscapability",
        "filteredfactsheetscount",
        "post_jobs",
        "get_jobs",
        "fetchbusinesscapabilitymetrics",
        "post_managedsnapshotrequests",
        "post_managedrestorationrequests",
    }
)


def _dispatch_reference_data_action(client, action: str, kwargs: dict):
    """Call client.<action>(**kwargs) for a whitelisted action name.

    Behavior-preserving replacement for the original 53-branch
    if/elif chain: action name always equals the target client method
    name in this generated module, so a single whitelist-gated
    getattr() call is exactly equivalent to the original dispatch.
    """
    if action not in _REFERENCE_DATA_ACTIONS:
        raise ValueError(f"Unknown action: {action}")
    return getattr(client, action)(**kwargs)


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
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return _dispatch_reference_data_action(client, action, kwargs)
