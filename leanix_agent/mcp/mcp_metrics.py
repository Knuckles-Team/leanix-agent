from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_metrics_client,
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
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "all_schemas_schemas_get":
            return client.all_schemas_schemas_get(**kwargs)
        if action == "new_schema_schemas_post":
            return client.new_schema_schemas_post(**kwargs)
        if action == "find_schemas_schemas_find_get":
            return client.find_schemas_schemas_find_get(**kwargs)
        if action == "one_schema_schemas__uuid__get":
            return client.one_schema_schemas__uuid__get(**kwargs)
        if action == "delete_schema_schemas__uuid__delete":
            return client.delete_schema_schemas__uuid__delete(**kwargs)
        if action == "all_points_schemas__uuid__points_get":
            return client.all_points_schemas__uuid__points_get(**kwargs)
        if action == "new_point_schemas__uuid__points_post":
            return client.new_point_schemas__uuid__points_post(**kwargs)
        if action == "delete_points_range_schemas__uuid__points_delete":
            return client.delete_points_range_schemas__uuid__points_delete(**kwargs)
        if action == "get_aggregation_schemas__uuid__points_aggregation_post":
            return client.get_aggregation_schemas__uuid__points_aggregation_post(
                **kwargs
            )
        if action == "one_point_schemas__uuid__points__timestamp__get":
            return client.one_point_schemas__uuid__points__timestamp__get(**kwargs)
        if action == "delete_one_point_schemas__uuid__points__timestamp__delete":
            return client.delete_one_point_schemas__uuid__points__timestamp__delete(
                **kwargs
            )
        if action == "trend_schemas__uuid__trends_get":
            return client.trend_schemas__uuid__trends_get(**kwargs)
        if action == "all_kpis_kpis_get":
            return client.all_kpis_kpis_get(**kwargs)
        if action == "put_kpi_kpis_put":
            return client.put_kpi_kpis_put(**kwargs)
        if action == "new_kpi_kpis_post":
            return client.new_kpi_kpis_post(**kwargs)
        if action == "patch_kpi_kpis_patch":
            return client.patch_kpi_kpis_patch(**kwargs)
        if action == "all_kpis_simple_kpis_simple_get":
            return client.all_kpis_simple_kpis_simple_get(**kwargs)
        if action == "one_kpi_kpis__uuid__get":
            return client.one_kpi_kpis__uuid__get(**kwargs)
        if action == "delete_one_kpi_kpis__uuid__delete":
            return client.delete_one_kpi_kpis__uuid__delete(**kwargs)
        if action == "validate_kpis_validate_post":
            return client.validate_kpis_validate_post(**kwargs)
        if action == "healthcheck_healthcheck__get":
            return client.healthcheck_healthcheck__get(**kwargs)
        if action == "ws_job_jobs_post":
            return client.ws_job_jobs_post(**kwargs)
        if action == "kpi_job_jobs_kpi__kpi_uuid__post":
            return client.kpi_job_jobs_kpi__kpi_uuid__post(**kwargs)
        if action == "all_charts_charts_get":
            return client.all_charts_charts_get(**kwargs)
        if action == "new_chart_charts_post":
            return client.new_chart_charts_post(**kwargs)
        if action == "one_chart_charts__uuid__get":
            return client.one_chart_charts__uuid__get(**kwargs)
        if action == "update_put_chart_charts__uuid__put":
            return client.update_put_chart_charts__uuid__put(**kwargs)
        if action == "delete_chart_charts__uuid__delete":
            return client.delete_chart_charts__uuid__delete(**kwargs)
        if action == "update_patch_chart_charts__uuid__patch":
            return client.update_patch_chart_charts__uuid__patch(**kwargs)
        raise ValueError(f"Unknown action: {action}")
