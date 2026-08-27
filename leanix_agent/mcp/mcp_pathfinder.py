from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_pathfinder_client,
)

_PATHFINDER_ACTIONS = frozenset(
    {
        "download_asset",
        "upsert_asset",
        "delete_asset",
        "get_bookmark_shares",
        "create_bookmark_shares",
        "delete_bookmark_shares",
        "get_bookmark",
        "update_bookmark",
        "delete_bookmark",
        "change_bookmark_owner",
        "get_bookmarks",
        "create_bookmark",
        "get_all_versions_for_bookmark",
        "get_data_model",
        "update_data_model",
        "get_enriched_data_model",
        "create_full_export",
        "download_export_file",
        "get_exports",
        "get_fact_sheet",
        "update_fact_sheet",
        "archive_fact_sheet",
        "get_fact_sheets",
        "create_fact_sheet",
        "get_fact_sheet_relations",
        "create_fact_sheet_relation",
        "update_fact_sheet_relation",
        "delete_fact_sheet_relation",
        "get_fact_sheet_hierarchy",
        "get_feature",
        "update_feature",
        "get_features",
        "process_graph_ql",
        "process_graph_ql_multipart",
        "get_access_control_entities",
        "create_access_control_entity",
        "get_access_control_entity",
        "update_access_control_entity",
        "delete_access_control_entity",
        "get_authorization",
        "update_authorization",
        "get_fact_sheet_resource_model",
        "update_fact_sheet_resource_model",
        "get_language",
        "update_language",
        "get_reporting_model",
        "update_reporting_model",
        "get_view_model",
        "update_view_model",
        "get_model_customization",
        "update_models_with_customization",
        "get_settings",
        "update_settings",
        "get_suggestions",
        "get_meta_model",
        "get_meta_model_actions",
        "post_meta_model_actions",
        "get_meta_model_actions_audit_log",
        "get_meta_model_job",
        "get_meta_model_permission_roles",
        "get_meta_model_actions_for_node",
        "get_action_batch",
        "get_action_batches",
        "post_action_batches",
        "get_meta_model_authorization",
        "get_meta_model_root",
        "get_meta_model_for_type",
        "get_preview_of_affected_data",
    }
)


def _dispatch_pathfinder_action(client, action: str, kwargs: dict):
    """Call client.<action>(**kwargs) for a whitelisted action name.

    Behavior-preserving replacement for the original 68-branch
    if/elif chain: action name always equals the target client method
    name in this generated module, so a single whitelist-gated
    getattr() call is exactly equivalent to the original dispatch.
    """
    if action not in _PATHFINDER_ACTIONS:
        raise ValueError(f"Unknown action: {action}")
    return getattr(client, action)(**kwargs)


def register_leanix_pathfinder_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-pathfinder"})
    async def leanix_leanix_pathfinder(
        action: str = Field(
            description="Action to perform. Must be one of: 'download_asset', 'upsert_asset', 'delete_asset', 'get_bookmark_shares', 'create_bookmark_shares', 'delete_bookmark_shares', 'get_bookmark', 'update_bookmark', 'delete_bookmark', 'change_bookmark_owner', 'get_bookmarks', 'create_bookmark', 'get_all_versions_for_bookmark', 'get_data_model', 'update_data_model', 'get_enriched_data_model', 'create_full_export', 'download_export_file', 'get_exports', 'get_fact_sheet', 'update_fact_sheet', 'archive_fact_sheet', 'get_fact_sheets', 'create_fact_sheet', 'get_fact_sheet_relations', 'create_fact_sheet_relation', 'update_fact_sheet_relation', 'delete_fact_sheet_relation', 'get_fact_sheet_hierarchy', 'get_feature', 'update_feature', 'get_features', 'process_graph_ql', 'process_graph_ql_multipart', 'get_access_control_entities', 'create_access_control_entity', 'get_access_control_entity', 'update_access_control_entity', 'delete_access_control_entity', 'get_authorization', 'update_authorization', 'get_fact_sheet_resource_model', 'update_fact_sheet_resource_model', 'get_language', 'update_language', 'get_reporting_model', 'update_reporting_model', 'get_view_model', 'update_view_model', 'get_model_customization', 'update_models_with_customization', 'get_settings', 'update_settings', 'get_suggestions', 'get_meta_model', 'get_meta_model_actions', 'post_meta_model_actions', 'get_meta_model_actions_audit_log', 'get_meta_model_job', 'get_meta_model_permission_roles', 'get_meta_model_actions_for_node', 'get_action_batch', 'get_action_batches', 'post_action_batches', 'get_meta_model_authorization', 'get_meta_model_root', 'get_meta_model_for_type', 'get_preview_of_affected_data'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_pathfinder_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix pathfinder operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return _dispatch_pathfinder_action(client, action, kwargs)

    @mcp.tool(tags={"leanix-pathfinder"})
    async def leanix_discover_meta_model(
        fact_sheet_type: str | None = Field(
            default=None,
            description="Optional specific Fact Sheet type to discover (e.g. 'Application', 'ITComponent'). If omitted, retrieves the root meta model.",
        ),
        client=Depends(get_pathfinder_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Discover the custom LeanIX meta-model/data-model schema including custom attributes and fields in real-time."""
        if ctx:
            await ctx.info("Retrieving dynamic LeanIX meta-model...")
        try:
            if fact_sheet_type:
                return client.get_meta_model_for_type(fact_sheet_type=fact_sheet_type)
            return client.get_meta_model_root()
        except Exception as e:
            return {
                "error": f"Failed to retrieve dynamic meta-model: {type(e).__name__}"
            }
