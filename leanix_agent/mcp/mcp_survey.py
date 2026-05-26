from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_survey_client,
)


def register_leanix_survey_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-survey"})
    async def leanix_leanix_survey(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_poll', 'update_poll', 'delete_poll_by_id', 'get_poll_run_by_id', 'update_poll_run', 'delete_poll_run', 'update_poll_run_status', 'get_poll_result', 'update_poll_result', 'get_polls', 'create_poll', 'get_poll_runs', 'create_poll_run', 'create_poll_reminder', 'check_for_new_fact_sheets', 'replay_all_workspaces', 'replay_workspace_by_id', 'get_polls_for_fact_sheet', 'get_recipients_and_fact_sheets_for_poll', 'get_poll_runs_by_poll', 'get_poll_count', 'get_all_templates', 'get_templates_by_id', 'get_poll_results_for_user', 'get_all_reminders_for_poll_run', 'get_recipients_and_fact_sheets_for_poll_run', 'getpollrunresultsasexcel', 'get_poll_results_by_poll_run_id', 'get_added_recipients_for_poll_run'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_survey_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix survey operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "get_poll":
            return client.get_poll(**kwargs)
        if action == "update_poll":
            return client.update_poll(**kwargs)
        if action == "delete_poll_by_id":
            return client.delete_poll_by_id(**kwargs)
        if action == "get_poll_run_by_id":
            return client.get_poll_run_by_id(**kwargs)
        if action == "update_poll_run":
            return client.update_poll_run(**kwargs)
        if action == "delete_poll_run":
            return client.delete_poll_run(**kwargs)
        if action == "update_poll_run_status":
            return client.update_poll_run_status(**kwargs)
        if action == "get_poll_result":
            return client.get_poll_result(**kwargs)
        if action == "update_poll_result":
            return client.update_poll_result(**kwargs)
        if action == "get_polls":
            return client.get_polls(**kwargs)
        if action == "create_poll":
            return client.create_poll(**kwargs)
        if action == "get_poll_runs":
            return client.get_poll_runs(**kwargs)
        if action == "create_poll_run":
            return client.create_poll_run(**kwargs)
        if action == "create_poll_reminder":
            return client.create_poll_reminder(**kwargs)
        if action == "check_for_new_fact_sheets":
            return client.check_for_new_fact_sheets(**kwargs)
        if action == "replay_all_workspaces":
            return client.replay_all_workspaces(**kwargs)
        if action == "replay_workspace_by_id":
            return client.replay_workspace_by_id(**kwargs)
        if action == "get_polls_for_fact_sheet":
            return client.get_polls_for_fact_sheet(**kwargs)
        if action == "get_recipients_and_fact_sheets_for_poll":
            return client.get_recipients_and_fact_sheets_for_poll(**kwargs)
        if action == "get_poll_runs_by_poll":
            return client.get_poll_runs_by_poll(**kwargs)
        if action == "get_poll_count":
            return client.get_poll_count(**kwargs)
        if action == "get_all_templates":
            return client.get_all_templates(**kwargs)
        if action == "get_templates_by_id":
            return client.get_templates_by_id(**kwargs)
        if action == "get_poll_results_for_user":
            return client.get_poll_results_for_user(**kwargs)
        if action == "get_all_reminders_for_poll_run":
            return client.get_all_reminders_for_poll_run(**kwargs)
        if action == "get_recipients_and_fact_sheets_for_poll_run":
            return client.get_recipients_and_fact_sheets_for_poll_run(**kwargs)
        if action == "getpollrunresultsasexcel":
            return client.getpollrunresultsasexcel(**kwargs)
        if action == "get_poll_results_by_poll_run_id":
            return client.get_poll_results_by_poll_run_id(**kwargs)
        if action == "get_added_recipients_for_poll_run":
            return client.get_added_recipients_for_poll_run(**kwargs)
        raise ValueError(f"Unknown action: {action}")
