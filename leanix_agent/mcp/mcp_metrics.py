from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_metrics_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_METRICS_ACTIONS = frozenset(
    {
        "all_schemas_schemas_get",
        "new_schema_schemas_post",
        "find_schemas_schemas_find_get",
        "one_schema_schemas__uuid__get",
        "delete_schema_schemas__uuid__delete",
        "all_points_schemas__uuid__points_get",
        "new_point_schemas__uuid__points_post",
        "delete_points_range_schemas__uuid__points_delete",
        "get_aggregation_schemas__uuid__points_aggregation_post",
        "one_point_schemas__uuid__points__timestamp__get",
        "delete_one_point_schemas__uuid__points__timestamp__delete",
        "trend_schemas__uuid__trends_get",
        "all_kpis_kpis_get",
        "put_kpi_kpis_put",
        "new_kpi_kpis_post",
        "patch_kpi_kpis_patch",
        "all_kpis_simple_kpis_simple_get",
        "one_kpi_kpis__uuid__get",
        "delete_one_kpi_kpis__uuid__delete",
        "validate_kpis_validate_post",
        "healthcheck_healthcheck__get",
        "ws_job_jobs_post",
        "kpi_job_jobs_kpi__kpi_uuid__post",
        "all_charts_charts_get",
        "new_chart_charts_post",
        "one_chart_charts__uuid__get",
        "update_put_chart_charts__uuid__put",
        "delete_chart_charts__uuid__delete",
        "update_patch_chart_charts__uuid__patch",
    }
)


def register_leanix_metrics_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-metrics"})
    async def leanix_leanix_metrics(
        action: str = Field(
            description="Action to perform. Must be one of: 'all_schemas_schemas_get', 'new_schema_schemas_post', 'find_schemas_schemas_find_get', 'one_schema_schemas__uuid__get', 'delete_schema_schemas__uuid__delete', 'all_points_schemas__uuid__points_get', 'new_point_schemas__uuid__points_post', 'delete_points_range_schemas__uuid__points_delete', 'get_aggregation_schemas__uuid__points_aggregation_post', 'one_point_schemas__uuid__points__timestamp__get', 'delete_one_point_schemas__uuid__points__timestamp__delete', 'trend_schemas__uuid__trends_get', 'all_kpis_kpis_get', 'put_kpi_kpis_put', 'new_kpi_kpis_post', 'patch_kpi_kpis_patch', 'all_kpis_simple_kpis_simple_get', 'one_kpi_kpis__uuid__get', 'delete_one_kpi_kpis__uuid__delete', 'validate_kpis_validate_post', 'healthcheck_healthcheck__get', 'ws_job_jobs_post', 'kpi_job_jobs_kpi__kpi_uuid__post', 'all_charts_charts_get', 'new_chart_charts_post', 'one_chart_charts__uuid__get', 'update_put_chart_charts__uuid__put', 'delete_chart_charts__uuid__delete', 'update_patch_chart_charts__uuid__patch'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_metrics_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix metrics operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(client, action, kwargs, allowed=_METRICS_ACTIONS)
