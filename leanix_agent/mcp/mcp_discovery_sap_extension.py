from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from pydantic import Field

#!/usr/bin/env python3
from leanix_agent.auth import (
    get_discovery_sap_extension_client,
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
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "get_cloud_foundry_domains":
            return client.get_cloud_foundry_domains(**kwargs)
        if action == "get_cloud_foundry_subject_pattern":
            return client.get_cloud_foundry_subject_pattern(**kwargs)
        if action == "put_integrations_id_credentials_cloud_foundry":
            return client.put_integrations_id_credentials_cloud_foundry(**kwargs)
        if action == "post_cloud_foundry_infer_certificate_domain":
            return client.post_cloud_foundry_infer_certificate_domain(**kwargs)
        if action == "get_credentials_type":
            return client.get_credentials_type(**kwargs)
        if action == "post_credentials_verify_cms":
            return client.post_credentials_verify_cms(**kwargs)
        if action == "get_health":
            return client.get_health(**kwargs)
        if action == "post_integrations":
            return client.post_integrations(**kwargs)
        if action == "get_integrations":
            return client.get_integrations(**kwargs)
        if action == "put_integrations_id_credentials_cms":
            return client.put_integrations_id_credentials_cms(**kwargs)
        if action == "patch_integrations_id":
            return client.patch_integrations_id(**kwargs)
        if action == "delete_integrations_id_":
            return client.delete_integrations_id_(**kwargs)
        if action == "post_integrations_credentials_verify":
            return client.post_integrations_credentials_verify(**kwargs)
        if action == "post_integrations_id_sync":
            return client.post_integrations_id_sync(**kwargs)
        if action == "get_kyma_spec_suggestions":
            return client.get_kyma_spec_suggestions(**kwargs)
        if action == "post_kyma_verify_api_url":
            return client.post_kyma_verify_api_url(**kwargs)
        if action == "put_integrations_id_credentials_kyma":
            return client.put_integrations_id_credentials_kyma(**kwargs)
        if action == "put_integrations_id_credentials_build":
            return client.put_integrations_id_credentials_build(**kwargs)
        if action == "get_checkdatamodel":
            return client.get_checkdatamodel(**kwargs)
        if action == "get_check_data_model":
            return client.get_check_data_model(**kwargs)
        raise ValueError(f"Unknown action: {action}")
