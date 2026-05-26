from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_poll_client,
)


def register_leanix_poll_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-poll"})
    async def leanix_leanix_poll(
        action: str = Field(
            description="Action to perform. Must be one of: 'replay', 'replay_1', 'get_polls_for_factsheet', 'get_polls', 'create_poll', 'get_poll', 'update_poll', 'delete_poll', 'get_poll_count', 'get_poll_recipient_details', 'get_poll_poll_runs', 'get_poll_result', 'update_poll_result', 'check_for_new_fact_sheets', 'create_poll_reminder', 'get_poll_runs', 'create_poll_run', 'get_poll_run', 'update_poll_run', 'delete_poll_run', 'get_added_recipients_for_run', 'get_poll_results_for_user', 'get_poll_run_results', 'get_poll_runs_kpi_counts', 'get_recipients_for_poll_run', 'get_reminders', 'get_results_for_poll_run', 'set_status', 'get_all', 'create_poll_template', 'get_by_id', 'delete_by_id'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_poll_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix poll operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "replay":
            return client.replay(**kwargs)
        if action == "replay_1":
            return client.replay_1(**kwargs)
        if action == "get_polls_for_factsheet":
            return client.get_polls_for_factsheet(**kwargs)
        if action == "get_polls":
            return client.get_polls(**kwargs)
        if action == "create_poll":
            return client.create_poll(**kwargs)
        if action == "get_poll":
            return client.get_poll(**kwargs)
        if action == "update_poll":
            return client.update_poll(**kwargs)
        if action == "delete_poll":
            return client.delete_poll(**kwargs)
        if action == "get_poll_count":
            return client.get_poll_count(**kwargs)
        if action == "get_poll_recipient_details":
            return client.get_poll_recipient_details(**kwargs)
        if action == "get_poll_poll_runs":
            return client.get_poll_poll_runs(**kwargs)
        if action == "get_poll_result":
            return client.get_poll_result(**kwargs)
        if action == "update_poll_result":
            return client.update_poll_result(**kwargs)
        if action == "check_for_new_fact_sheets":
            return client.check_for_new_fact_sheets(**kwargs)
        if action == "create_poll_reminder":
            return client.create_poll_reminder(**kwargs)
        if action == "get_poll_runs":
            return client.get_poll_runs(**kwargs)
        if action == "create_poll_run":
            return client.create_poll_run(**kwargs)
        if action == "get_poll_run":
            return client.get_poll_run(**kwargs)
        if action == "update_poll_run":
            return client.update_poll_run(**kwargs)
        if action == "delete_poll_run":
            return client.delete_poll_run(**kwargs)
        if action == "get_added_recipients_for_run":
            return client.get_added_recipients_for_run(**kwargs)
        if action == "get_poll_results_for_user":
            return client.get_poll_results_for_user(**kwargs)
        if action == "get_poll_run_results":
            return client.get_poll_run_results(**kwargs)
        if action == "get_poll_runs_kpi_counts":
            return client.get_poll_runs_kpi_counts(**kwargs)
        if action == "get_recipients_for_poll_run":
            return client.get_recipients_for_poll_run(**kwargs)
        if action == "get_reminders":
            return client.get_reminders(**kwargs)
        if action == "get_results_for_poll_run":
            return client.get_results_for_poll_run(**kwargs)
        if action == "set_status":
            return client.set_status(**kwargs)
        if action == "get_all":
            return client.get_all(**kwargs)
        if action == "create_poll_template":
            return client.create_poll_template(**kwargs)
        if action == "get_by_id":
            return client.get_by_id(**kwargs)
        if action == "delete_by_id":
            return client.delete_by_id(**kwargs)
        raise ValueError(f"Unknown action: {action}")
