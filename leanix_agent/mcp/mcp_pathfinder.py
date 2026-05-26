from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_pathfinder_client,
)


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
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "download_asset":
            return client.download_asset(**kwargs)
        if action == "upsert_asset":
            return client.upsert_asset(**kwargs)
        if action == "delete_asset":
            return client.delete_asset(**kwargs)
        if action == "get_bookmark_shares":
            return client.get_bookmark_shares(**kwargs)
        if action == "create_bookmark_shares":
            return client.create_bookmark_shares(**kwargs)
        if action == "delete_bookmark_shares":
            return client.delete_bookmark_shares(**kwargs)
        if action == "get_bookmark":
            return client.get_bookmark(**kwargs)
        if action == "update_bookmark":
            return client.update_bookmark(**kwargs)
        if action == "delete_bookmark":
            return client.delete_bookmark(**kwargs)
        if action == "change_bookmark_owner":
            return client.change_bookmark_owner(**kwargs)
        if action == "get_bookmarks":
            return client.get_bookmarks(**kwargs)
        if action == "create_bookmark":
            return client.create_bookmark(**kwargs)
        if action == "get_all_versions_for_bookmark":
            return client.get_all_versions_for_bookmark(**kwargs)
        if action == "get_data_model":
            return client.get_data_model(**kwargs)
        if action == "update_data_model":
            return client.update_data_model(**kwargs)
        if action == "get_enriched_data_model":
            return client.get_enriched_data_model(**kwargs)
        if action == "create_full_export":
            return client.create_full_export(**kwargs)
        if action == "download_export_file":
            return client.download_export_file(**kwargs)
        if action == "get_exports":
            return client.get_exports(**kwargs)
        if action == "get_fact_sheet":
            return client.get_fact_sheet(**kwargs)
        if action == "update_fact_sheet":
            return client.update_fact_sheet(**kwargs)
        if action == "archive_fact_sheet":
            return client.archive_fact_sheet(**kwargs)
        if action == "get_fact_sheets":
            return client.get_fact_sheets(**kwargs)
        if action == "create_fact_sheet":
            return client.create_fact_sheet(**kwargs)
        if action == "get_fact_sheet_relations":
            return client.get_fact_sheet_relations(**kwargs)
        if action == "create_fact_sheet_relation":
            return client.create_fact_sheet_relation(**kwargs)
        if action == "update_fact_sheet_relation":
            return client.update_fact_sheet_relation(**kwargs)
        if action == "delete_fact_sheet_relation":
            return client.delete_fact_sheet_relation(**kwargs)
        if action == "get_fact_sheet_hierarchy":
            return client.get_fact_sheet_hierarchy(**kwargs)
        if action == "get_feature":
            return client.get_feature(**kwargs)
        if action == "update_feature":
            return client.update_feature(**kwargs)
        if action == "get_features":
            return client.get_features(**kwargs)
        if action == "process_graph_ql":
            return client.process_graph_ql(**kwargs)
        if action == "process_graph_ql_multipart":
            return client.process_graph_ql_multipart(**kwargs)
        if action == "get_access_control_entities":
            return client.get_access_control_entities(**kwargs)
        if action == "create_access_control_entity":
            return client.create_access_control_entity(**kwargs)
        if action == "get_access_control_entity":
            return client.get_access_control_entity(**kwargs)
        if action == "update_access_control_entity":
            return client.update_access_control_entity(**kwargs)
        if action == "delete_access_control_entity":
            return client.delete_access_control_entity(**kwargs)
        if action == "get_authorization":
            return client.get_authorization(**kwargs)
        if action == "update_authorization":
            return client.update_authorization(**kwargs)
        if action == "get_fact_sheet_resource_model":
            return client.get_fact_sheet_resource_model(**kwargs)
        if action == "update_fact_sheet_resource_model":
            return client.update_fact_sheet_resource_model(**kwargs)
        if action == "get_language":
            return client.get_language(**kwargs)
        if action == "update_language":
            return client.update_language(**kwargs)
        if action == "get_reporting_model":
            return client.get_reporting_model(**kwargs)
        if action == "update_reporting_model":
            return client.update_reporting_model(**kwargs)
        if action == "get_view_model":
            return client.get_view_model(**kwargs)
        if action == "update_view_model":
            return client.update_view_model(**kwargs)
        if action == "get_model_customization":
            return client.get_model_customization(**kwargs)
        if action == "update_models_with_customization":
            return client.update_models_with_customization(**kwargs)
        if action == "get_settings":
            return client.get_settings(**kwargs)
        if action == "update_settings":
            return client.update_settings(**kwargs)
        if action == "get_suggestions":
            return client.get_suggestions(**kwargs)
        if action == "get_meta_model":
            return client.get_meta_model(**kwargs)
        if action == "get_meta_model_actions":
            return client.get_meta_model_actions(**kwargs)
        if action == "post_meta_model_actions":
            return client.post_meta_model_actions(**kwargs)
        if action == "get_meta_model_actions_audit_log":
            return client.get_meta_model_actions_audit_log(**kwargs)
        if action == "get_meta_model_job":
            return client.get_meta_model_job(**kwargs)
        if action == "get_meta_model_permission_roles":
            return client.get_meta_model_permission_roles(**kwargs)
        if action == "get_meta_model_actions_for_node":
            return client.get_meta_model_actions_for_node(**kwargs)
        if action == "get_action_batch":
            return client.get_action_batch(**kwargs)
        if action == "get_action_batches":
            return client.get_action_batches(**kwargs)
        if action == "post_action_batches":
            return client.post_action_batches(**kwargs)
        if action == "get_meta_model_authorization":
            return client.get_meta_model_authorization(**kwargs)
        if action == "get_meta_model_root":
            return client.get_meta_model_root(**kwargs)
        if action == "get_meta_model_for_type":
            return client.get_meta_model_for_type(**kwargs)
        if action == "get_preview_of_affected_data":
            return client.get_preview_of_affected_data(**kwargs)
        raise ValueError(f"Unknown action: {action}")

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
            return {"error": f"Failed to retrieve dynamic meta-model: {str(e)}"}
