from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_discovery_sap_extension_client,
)


from leanix_agent.mcp._action_dispatch import dispatch_client_action

_DISCOVERY_SAP_EXTENSION_ACTIONS = frozenset(
    {
        "get_cloud_foundry_domains",
        "get_cloud_foundry_subject_pattern",
        "put_integrations_id_credentials_cloud_foundry",
        "post_cloud_foundry_infer_certificate_domain",
        "get_credentials_type",
        "post_credentials_verify_cms",
        "get_health",
        "post_integrations",
        "get_integrations",
        "put_integrations_id_credentials_cms",
        "patch_integrations_id",
        "delete_integrations_id_",
        "post_integrations_credentials_verify",
        "post_integrations_id_sync",
        "get_kyma_spec_suggestions",
        "post_kyma_verify_api_url",
        "put_integrations_id_credentials_kyma",
        "put_integrations_id_credentials_build",
        "get_checkdatamodel",
        "get_check_data_model",
    }
)


def register_leanix_discovery_sap_extension_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-discovery-sap-extension"})
    async def leanix_leanix_discovery_sap_extension(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_cloud_foundry_domains', 'get_cloud_foundry_subject_pattern', 'put_integrations_id_credentials_cloud_foundry', 'post_cloud_foundry_infer_certificate_domain', 'get_credentials_type', 'post_credentials_verify_cms', 'get_health', 'post_integrations', 'get_integrations', 'put_integrations_id_credentials_cms', 'patch_integrations_id', 'delete_integrations_id_', 'post_integrations_credentials_verify', 'post_integrations_id_sync', 'get_kyma_spec_suggestions', 'post_kyma_verify_api_url', 'put_integrations_id_credentials_kyma', 'put_integrations_id_credentials_build', 'get_checkdatamodel', 'get_check_data_model'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_discovery_sap_extension_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix discovery sap extension operations."""
        if ctx:
            await ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception:
            return {"error": "Operation failed"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        return dispatch_client_action(
            client, action, kwargs, allowed=_DISCOVERY_SAP_EXTENSION_ACTIONS
        )
