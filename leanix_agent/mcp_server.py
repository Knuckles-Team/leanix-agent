#!/usr/bin/python
import warnings

from fastmcp import Context, FastMCP
from fastmcp.dependencies import Depends
from fastmcp.utilities.logging import get_logger
from pydantic import Field

# Filter RequestsDependencyWarning early to prevent log spam
with warnings.catch_warnings():
    warnings.simplefilter("ignore")
    try:
        from requests.exceptions import RequestsDependencyWarning

        warnings.filterwarnings("ignore", category=RequestsDependencyWarning)
    except ImportError:
        pass

warnings.filterwarnings("ignore", message=".*urllib3.*or chardet.*")
warnings.filterwarnings("ignore", message=".*urllib3.*or charset_normalizer.*")

import logging
import os
import sys
from typing import Any

from agent_utilities.base_utilities import to_boolean
from agent_utilities.mcp_utilities import create_mcp_server
from dotenv import find_dotenv, load_dotenv
from starlette.requests import Request
from starlette.responses import JSONResponse

from leanix_agent.auth import (
    get_ai_inventory_builder_client,
    get_apptio_connector_client,
    get_automations_client,
    get_discovery_ai_agents_client,
    get_discovery_linking_v1_client,
    get_discovery_linking_v2_client,
    get_discovery_saas_client,
    get_discovery_sap_client,
    get_discovery_sap_extension_client,
    get_documents_client,
    get_impacts_client,
    get_integration_api_client,
    get_integration_collibra_client,
    get_integration_servicenow_client,
    get_integration_signavio_client,
    get_inventory_data_quality_client,
    get_managed_code_execution_client,
    get_metrics_client,
    get_mtm_client,
    get_navigation_client,
    get_pathfinder_client,
    get_poll_client,
    get_reference_data_catalog_client,
    get_reference_data_client,
    get_storage_client,
    get_survey_client,
    get_synclog_client,
    get_technology_discovery_client,
    get_todo_client,
    get_transformations_client,
    get_webhooks_client,
)

__version__ = "0.12.0"

logger = get_logger(name="leanix-agent")
logger.setLevel(logging.INFO)


def register_leanix_ai_inventory_builder_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-ai-inventory-builder"})
    async def leanix_leanix_ai_inventory_builder(
        action: str = Field(
            description="Action to perform. Must be one of: 'healthcheck', 'pipelines', 'getpipelines', 'sendpipelineaction', 'getpipelinesuggestions', 'getpipeline', 'deletepipeline', 'getpipelinefile', 'deletefailedpipelines', 'admindeletepipeline'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_ai_inventory_builder_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix ai inventory builder operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "healthcheck":
            return client.healthcheck(**kwargs)
        if action == "pipelines":
            return client.pipelines(**kwargs)
        if action == "getpipelines":
            return client.getpipelines(**kwargs)
        if action == "sendpipelineaction":
            return client.sendpipelineaction(**kwargs)
        if action == "getpipelinesuggestions":
            return client.getpipelinesuggestions(**kwargs)
        if action == "getpipeline":
            return client.getpipeline(**kwargs)
        if action == "deletepipeline":
            return client.deletepipeline(**kwargs)
        if action == "getpipelinefile":
            return client.getpipelinefile(**kwargs)
        if action == "deletefailedpipelines":
            return client.deletefailedpipelines(**kwargs)
        if action == "admindeletepipeline":
            return client.admindeletepipeline(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_apptio_connector_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-apptio-connector"})
    async def leanix_leanix_apptio_connector(
        action: str = Field(
            description="Action to perform. Must be one of: 'getallconfigurations', 'upsertconfiguration', 'getconfigurations', 'deleteconfiguration', 'create', 'getresults', 'getresultsurl', 'getstats', 'getstatus', 'getwarnings'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_apptio_connector_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix apptio connector operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "getallconfigurations":
            return client.getallconfigurations(**kwargs)
        if action == "upsertconfiguration":
            return client.upsertconfiguration(**kwargs)
        if action == "getconfigurations":
            return client.getconfigurations(**kwargs)
        if action == "deleteconfiguration":
            return client.deleteconfiguration(**kwargs)
        if action == "create":
            return client.create(**kwargs)
        if action == "getresults":
            return client.getresults(**kwargs)
        if action == "getresultsurl":
            return client.getresultsurl(**kwargs)
        if action == "getstats":
            return client.getstats(**kwargs)
        if action == "getstatus":
            return client.getstatus(**kwargs)
        if action == "getwarnings":
            return client.getwarnings(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_automations_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-automations"})
    async def leanix_leanix_automations(
        action: str = Field(
            description="Action to perform. Must be one of: 'templatescontroller_getalltemplates', 'templatescontroller_createtemplate', 'templatescontroller_gettemplate', 'templatescontroller_updatetemplate', 'templatescontroller_patchtemplate', 'templatescontroller_deletetemplate', 'instancescontroller_findall', 'instancescontroller_quota', 'statisticscontroller_getstatistics', 'snapshotscontroller_managesnapshotrequests', 'snapshotscontroller_managedrestorationrequests', 'scriptscontroller_createmcescript', 'scriptscontroller_updatemcescript'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_automations_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix automations operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "templatescontroller_getalltemplates":
            return client.templatescontroller_getalltemplates(**kwargs)
        if action == "templatescontroller_createtemplate":
            return client.templatescontroller_createtemplate(**kwargs)
        if action == "templatescontroller_gettemplate":
            return client.templatescontroller_gettemplate(**kwargs)
        if action == "templatescontroller_updatetemplate":
            return client.templatescontroller_updatetemplate(**kwargs)
        if action == "templatescontroller_patchtemplate":
            return client.templatescontroller_patchtemplate(**kwargs)
        if action == "templatescontroller_deletetemplate":
            return client.templatescontroller_deletetemplate(**kwargs)
        if action == "instancescontroller_findall":
            return client.instancescontroller_findall(**kwargs)
        if action == "instancescontroller_quota":
            return client.instancescontroller_quota(**kwargs)
        if action == "statisticscontroller_getstatistics":
            return client.statisticscontroller_getstatistics(**kwargs)
        if action == "snapshotscontroller_managesnapshotrequests":
            return client.snapshotscontroller_managesnapshotrequests(**kwargs)
        if action == "snapshotscontroller_managedrestorationrequests":
            return client.snapshotscontroller_managedrestorationrequests(**kwargs)
        if action == "scriptscontroller_createmcescript":
            return client.scriptscontroller_createmcescript(**kwargs)
        if action == "scriptscontroller_updatemcescript":
            return client.scriptscontroller_updatemcescript(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_reference_data_catalog_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-reference-data-catalog"})
    async def leanix_leanix_reference_data_catalog(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_recommendations', 'get_items', 'get_items_id', 'delete_links', 'post_links', 'post_requests', 'get_requests', 'post_requests_id_comments'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_reference_data_catalog_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix reference data catalog operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "get_recommendations":
            return client.get_recommendations(**kwargs)
        if action == "get_items":
            return client.get_items(**kwargs)
        if action == "get_items_id":
            return client.get_items_id(**kwargs)
        if action == "delete_links":
            return client.delete_links(**kwargs)
        if action == "post_links":
            return client.post_links(**kwargs)
        if action == "post_requests":
            return client.post_requests(**kwargs)
        if action == "get_requests":
            return client.get_requests(**kwargs)
        if action == "post_requests_id_comments":
            return client.post_requests_id_comments(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_discovery_ai_agents_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-discovery-ai-agents"})
    async def leanix_leanix_discovery_ai_agents(
        action: str = Field(
            description="Action to perform. Must be one of: 'post_agents_a2a_cards', 'post_integrations', 'get_integrations', 'get_integrations_id', 'put_integrations_id_name', 'put_integrations_id_status', 'put_integrations_id_capabilities', 'put_integrations_id_credentials'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_discovery_ai_agents_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix discovery ai agents operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "post_agents_a2a_cards":
            return client.post_agents_a2a_cards(**kwargs)
        if action == "post_integrations":
            return client.post_integrations(**kwargs)
        if action == "get_integrations":
            return client.get_integrations(**kwargs)
        if action == "get_integrations_id":
            return client.get_integrations_id(**kwargs)
        if action == "put_integrations_id_name":
            return client.put_integrations_id_name(**kwargs)
        if action == "put_integrations_id_status":
            return client.put_integrations_id_status(**kwargs)
        if action == "put_integrations_id_capabilities":
            return client.put_integrations_id_capabilities(**kwargs)
        if action == "put_integrations_id_credentials":
            return client.put_integrations_id_credentials(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_discovery_linking_v1_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-discovery-linking-v1"})
    async def leanix_leanix_discovery_linking_v1(
        action: str = Field(
            description="Action to perform. Must be one of: 'link', 'bulk_link', 'discovery_itemsid', 'discovery_items', 'discovery_itemsidpre_validate_linkfactsheetid', 'discovery_itemsfilter_options', 'reject', 'discovery_itemslinking_progress', 'discovery_itemslinking_progressid', 'discovery_itemskpi_values', 'factsheetsiddetails'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_discovery_linking_v1_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix discovery linking v1 operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "link":
            return client.link(**kwargs)
        if action == "bulk_link":
            return client.bulk_link(**kwargs)
        if action == "discovery_itemsid":
            return client.discovery_itemsid(**kwargs)
        if action == "discovery_items":
            return client.discovery_items(**kwargs)
        if action == "discovery_itemsidpre_validate_linkfactsheetid":
            return client.discovery_itemsidpre_validate_linkfactsheetid(**kwargs)
        if action == "discovery_itemsfilter_options":
            return client.discovery_itemsfilter_options(**kwargs)
        if action == "reject":
            return client.reject(**kwargs)
        if action == "discovery_itemslinking_progress":
            return client.discovery_itemslinking_progress(**kwargs)
        if action == "discovery_itemslinking_progressid":
            return client.discovery_itemslinking_progressid(**kwargs)
        if action == "discovery_itemskpi_values":
            return client.discovery_itemskpi_values(**kwargs)
        if action == "factsheetsiddetails":
            return client.factsheetsiddetails(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_discovery_linking_v2_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-discovery-linking-v2"})
    async def leanix_leanix_discovery_linking_v2(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_factsheets_id_links', 'get_origin_discoveryitems', 'get_origin_discoveryitems_export', 'put_origin_discoveryitems_link', 'get_origin_discoveryitems_linkingprogress', 'put_origin_discoveryitems_reject', 'get_origin_discoveryitems_sourceconfigs', 'get_origin_discoveryitems_id', 'get_origin_discoveryitems_id_changelogs', 'put_origin_discoveryitems_id_link', 'post_origin_discoveryitems_id_preview', 'get_origin_insights', 'get_origin_internal_events', 'get_origin_internal_events_compaction', 'post_origin_push', 'post_origin_push_id', 'get_origin_settings', 'get_origin_settings_autolinking', 'put_origin_settings_autolinking'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_discovery_linking_v2_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix discovery linking v2 operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "get_factsheets_id_links":
            return client.get_factsheets_id_links(**kwargs)
        if action == "get_origin_discoveryitems":
            return client.get_origin_discoveryitems(**kwargs)
        if action == "get_origin_discoveryitems_export":
            return client.get_origin_discoveryitems_export(**kwargs)
        if action == "put_origin_discoveryitems_link":
            return client.put_origin_discoveryitems_link(**kwargs)
        if action == "get_origin_discoveryitems_linkingprogress":
            return client.get_origin_discoveryitems_linkingprogress(**kwargs)
        if action == "put_origin_discoveryitems_reject":
            return client.put_origin_discoveryitems_reject(**kwargs)
        if action == "get_origin_discoveryitems_sourceconfigs":
            return client.get_origin_discoveryitems_sourceconfigs(**kwargs)
        if action == "get_origin_discoveryitems_id":
            return client.get_origin_discoveryitems_id(**kwargs)
        if action == "get_origin_discoveryitems_id_changelogs":
            return client.get_origin_discoveryitems_id_changelogs(**kwargs)
        if action == "put_origin_discoveryitems_id_link":
            return client.put_origin_discoveryitems_id_link(**kwargs)
        if action == "post_origin_discoveryitems_id_preview":
            return client.post_origin_discoveryitems_id_preview(**kwargs)
        if action == "get_origin_insights":
            return client.get_origin_insights(**kwargs)
        if action == "get_origin_internal_events":
            return client.get_origin_internal_events(**kwargs)
        if action == "get_origin_internal_events_compaction":
            return client.get_origin_internal_events_compaction(**kwargs)
        if action == "post_origin_push":
            return client.post_origin_push(**kwargs)
        if action == "post_origin_push_id":
            return client.post_origin_push_id(**kwargs)
        if action == "get_origin_settings":
            return client.get_origin_settings(**kwargs)
        if action == "get_origin_settings_autolinking":
            return client.get_origin_settings_autolinking(**kwargs)
        if action == "put_origin_settings_autolinking":
            return client.put_origin_settings_autolinking(**kwargs)
        raise ValueError(f"Unknown action: {action}")


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


def register_leanix_discovery_saas_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-discovery-saas"})
    async def leanix_leanix_discovery_saas(
        action: str = Field(
            description="Action to perform. Must be one of: 'getavailableintegrations', 'postintegration', 'getintegrations', 'getintegrationbyid', 'deleteintegrationbyid', 'putintegrationnamebyid', 'putintegrationcapabilitiesbyid', 'putintegrationcredentialsbyid', 'putintegrationstatusbyid', 'getdiscoveries', 'getdiscoveryprioritybyid'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_discovery_saas_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix discovery saas operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "getavailableintegrations":
            return client.getavailableintegrations(**kwargs)
        if action == "postintegration":
            return client.postintegration(**kwargs)
        if action == "getintegrations":
            return client.getintegrations(**kwargs)
        if action == "getintegrationbyid":
            return client.getintegrationbyid(**kwargs)
        if action == "deleteintegrationbyid":
            return client.deleteintegrationbyid(**kwargs)
        if action == "putintegrationnamebyid":
            return client.putintegrationnamebyid(**kwargs)
        if action == "putintegrationcapabilitiesbyid":
            return client.putintegrationcapabilitiesbyid(**kwargs)
        if action == "putintegrationcredentialsbyid":
            return client.putintegrationcredentialsbyid(**kwargs)
        if action == "putintegrationstatusbyid":
            return client.putintegrationstatusbyid(**kwargs)
        if action == "getdiscoveries":
            return client.getdiscoveries(**kwargs)
        if action == "getdiscoveryprioritybyid":
            return client.getdiscoveryprioritybyid(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_documents_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-documents"})
    async def leanix_leanix_documents(
        action: str = Field(
            description="Action to perform. Must be one of: 'gettemplatecomponents', 'updatecomponents', 'createtemplatecomponents', 'gettemplatebyid', 'updatetemplate', 'deletetemplate', 'getdocumentbyid', 'updatedocument', 'deletedocumentbyid', 'getdocumentcomponents', 'updatedocumentcomponents', 'gettemplatespaginated', 'createtemplates', 'getdocumentspaginated', 'createdocuments', 'getdocumentscount', 'deletetemplatecomponent'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_documents_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix documents operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "gettemplatecomponents":
            return client.gettemplatecomponents(**kwargs)
        if action == "updatecomponents":
            return client.updatecomponents(**kwargs)
        if action == "createtemplatecomponents":
            return client.createtemplatecomponents(**kwargs)
        if action == "gettemplatebyid":
            return client.gettemplatebyid(**kwargs)
        if action == "updatetemplate":
            return client.updatetemplate(**kwargs)
        if action == "deletetemplate":
            return client.deletetemplate(**kwargs)
        if action == "getdocumentbyid":
            return client.getdocumentbyid(**kwargs)
        if action == "updatedocument":
            return client.updatedocument(**kwargs)
        if action == "deletedocumentbyid":
            return client.deletedocumentbyid(**kwargs)
        if action == "getdocumentcomponents":
            return client.getdocumentcomponents(**kwargs)
        if action == "updatedocumentcomponents":
            return client.updatedocumentcomponents(**kwargs)
        if action == "gettemplatespaginated":
            return client.gettemplatespaginated(**kwargs)
        if action == "createtemplates":
            return client.createtemplates(**kwargs)
        if action == "getdocumentspaginated":
            return client.getdocumentspaginated(**kwargs)
        if action == "createdocuments":
            return client.createdocuments(**kwargs)
        if action == "getdocumentscount":
            return client.getdocumentscount(**kwargs)
        if action == "deletetemplatecomponent":
            return client.deletetemplatecomponent(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_impacts_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-impacts"})
    async def leanix_leanix_impacts(
        action: str = Field(
            description="Action to perform. Must be one of: 'get', 'update', 'compute', 'getprojection', 'getsinglefactsheetprojection'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_impacts_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix impacts operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "get":
            return client.get(**kwargs)
        if action == "update":
            return client.update(**kwargs)
        if action == "compute":
            return client.compute(**kwargs)
        if action == "getprojection":
            return client.getprojection(**kwargs)
        if action == "getsinglefactsheetprojection":
            return client.getsinglefactsheetprojection(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_integration_api_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-integration-api"})
    async def leanix_leanix_integration_api(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_examples_starterexample', 'get_examples_advancedexample', 'getprocessorconfigurations', 'upsertprocessorconfiguration', 'deleteprocessorconfiguration', 'getsynchronizationrunsstatuslist', 'createsynchronizationrun', 'startsynchronizationrun', 'getsynchronizationrunprogress', 'stopsynchronizationrun', 'getsynchronizationrunstatus', 'getsynchronizationrunstats', 'getsynchronizationrunresults', 'getsynchronizationrunresultsurl', 'getsynchronizationrunwarnings', 'createsynchronizationrunwithconfig', 'createsynchronizationrunwithurlinput', 'createsynchronizationrunwithexecutiongroupandurlinput', 'createsynchronizationrunwithexecutiongroup', 'getsynchronizationrundebuginformation', 'getsynchronizationrundebugvariables', 'createsynchronizationfastrun', 'createsynchronizationfastrunwithconfig', 'createinazure'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_integration_api_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix integration api operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "get_examples_starterexample":
            return client.get_examples_starterexample(**kwargs)
        if action == "get_examples_advancedexample":
            return client.get_examples_advancedexample(**kwargs)
        if action == "getprocessorconfigurations":
            return client.getprocessorconfigurations(**kwargs)
        if action == "upsertprocessorconfiguration":
            return client.upsertprocessorconfiguration(**kwargs)
        if action == "deleteprocessorconfiguration":
            return client.deleteprocessorconfiguration(**kwargs)
        if action == "getsynchronizationrunsstatuslist":
            return client.getsynchronizationrunsstatuslist(**kwargs)
        if action == "createsynchronizationrun":
            return client.createsynchronizationrun(**kwargs)
        if action == "startsynchronizationrun":
            return client.startsynchronizationrun(**kwargs)
        if action == "getsynchronizationrunprogress":
            return client.getsynchronizationrunprogress(**kwargs)
        if action == "stopsynchronizationrun":
            return client.stopsynchronizationrun(**kwargs)
        if action == "getsynchronizationrunstatus":
            return client.getsynchronizationrunstatus(**kwargs)
        if action == "getsynchronizationrunstats":
            return client.getsynchronizationrunstats(**kwargs)
        if action == "getsynchronizationrunresults":
            return client.getsynchronizationrunresults(**kwargs)
        if action == "getsynchronizationrunresultsurl":
            return client.getsynchronizationrunresultsurl(**kwargs)
        if action == "getsynchronizationrunwarnings":
            return client.getsynchronizationrunwarnings(**kwargs)
        if action == "createsynchronizationrunwithconfig":
            return client.createsynchronizationrunwithconfig(**kwargs)
        if action == "createsynchronizationrunwithurlinput":
            return client.createsynchronizationrunwithurlinput(**kwargs)
        if action == "createsynchronizationrunwithexecutiongroupandurlinput":
            return client.createsynchronizationrunwithexecutiongroupandurlinput(
                **kwargs
            )
        if action == "createsynchronizationrunwithexecutiongroup":
            return client.createsynchronizationrunwithexecutiongroup(**kwargs)
        if action == "getsynchronizationrundebuginformation":
            return client.getsynchronizationrundebuginformation(**kwargs)
        if action == "getsynchronizationrundebugvariables":
            return client.getsynchronizationrundebugvariables(**kwargs)
        if action == "createsynchronizationfastrun":
            return client.createsynchronizationfastrun(**kwargs)
        if action == "createsynchronizationfastrunwithconfig":
            return client.createsynchronizationfastrunwithconfig(**kwargs)
        if action == "createinazure":
            return client.createinazure(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_integration_collibra_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-integration-collibra"})
    async def leanix_leanix_integration_collibra(
        action: str = Field(
            description="Action to perform. Must be one of: 'createsynchronizationrun', 'getconfigurations', 'createconfiguration', 'getconfigurationbyid', 'updateconfiguration', 'deleteconfiguration', 'getoverview', 'getstatus', 'getfeaturetoggles', 'getfields', 'getrelationfields', 'getrelations', 'getsubscriptionroles', 'getcredentials', 'createcollibracredentials', 'getcollibracredentialsbyid', 'updatecollibracredentials', 'validatecollibracredentialsbyid', 'getattributetypesforassettype', 'getattributetypesforassettypebyscope', 'getassetstatuses', 'getassettypes', 'getattributetypes', 'getcommunities', 'getcomplexrelationtypes', 'getdomains', 'getrelationtypes', 'getresourceroles', 'getresponsibilityroles'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_integration_collibra_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix integration collibra operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "createsynchronizationrun":
            return client.createsynchronizationrun(**kwargs)
        if action == "getconfigurations":
            return client.getconfigurations(**kwargs)
        if action == "createconfiguration":
            return client.createconfiguration(**kwargs)
        if action == "getconfigurationbyid":
            return client.getconfigurationbyid(**kwargs)
        if action == "updateconfiguration":
            return client.updateconfiguration(**kwargs)
        if action == "deleteconfiguration":
            return client.deleteconfiguration(**kwargs)
        if action == "getoverview":
            return client.getoverview(**kwargs)
        if action == "getstatus":
            return client.getstatus(**kwargs)
        if action == "getfeaturetoggles":
            return client.getfeaturetoggles(**kwargs)
        if action == "getfields":
            return client.getfields(**kwargs)
        if action == "getrelationfields":
            return client.getrelationfields(**kwargs)
        if action == "getrelations":
            return client.getrelations(**kwargs)
        if action == "getsubscriptionroles":
            return client.getsubscriptionroles(**kwargs)
        if action == "getcredentials":
            return client.getcredentials(**kwargs)
        if action == "createcollibracredentials":
            return client.createcollibracredentials(**kwargs)
        if action == "getcollibracredentialsbyid":
            return client.getcollibracredentialsbyid(**kwargs)
        if action == "updatecollibracredentials":
            return client.updatecollibracredentials(**kwargs)
        if action == "validatecollibracredentialsbyid":
            return client.validatecollibracredentialsbyid(**kwargs)
        if action == "getattributetypesforassettype":
            return client.getattributetypesforassettype(**kwargs)
        if action == "getattributetypesforassettypebyscope":
            return client.getattributetypesforassettypebyscope(**kwargs)
        if action == "getassetstatuses":
            return client.getassetstatuses(**kwargs)
        if action == "getassettypes":
            return client.getassettypes(**kwargs)
        if action == "getattributetypes":
            return client.getattributetypes(**kwargs)
        if action == "getcommunities":
            return client.getcommunities(**kwargs)
        if action == "getcomplexrelationtypes":
            return client.getcomplexrelationtypes(**kwargs)
        if action == "getdomains":
            return client.getdomains(**kwargs)
        if action == "getrelationtypes":
            return client.getrelationtypes(**kwargs)
        if action == "getresourceroles":
            return client.getresourceroles(**kwargs)
        if action == "getresponsibilityroles":
            return client.getresponsibilityroles(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_integration_servicenow_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-integration-servicenow"})
    async def leanix_leanix_integration_servicenow(
        action: str = Field(
            description="Action to perform. Must be one of: 'getaggregatedfactsheetsummary', 'getaggregatedsoftwareinformation', 'getservicenowaggregatedsoftware', 'getfilterforfactsheet', 'getfilterforprovider', 'getfiltersforhardware', 'getservicenowaggregatedhardware', 'getstatusoverview', 'getallconfigurations', 'createconfiguration', 'getconfiguration', 'updateconfiguration', 'deleteconfiguration', 'synchronize', 'validateconfiguration', 'validateservicenowcredentials', 'getfilters', 'getservicenowsyncconstraintrules', 'getavailablerelcirelations', 'getinstalledservicenowpluginversion', 'getmappingtablerelations', 'getreferencefieldrelations', 'getservicenowmetadata', 'gettables', 'changes', 'hooks', 'sendprompt', 'sendpromptv2', 'abortallpendingandrunningsynchronizations', 'abortsynchronization', 'getcurrentlyrunningorlastcreatedrun', 'getversionbyid', 'getversions'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_integration_servicenow_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix integration servicenow operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "getaggregatedfactsheetsummary":
            return client.getaggregatedfactsheetsummary(**kwargs)
        if action == "getaggregatedsoftwareinformation":
            return client.getaggregatedsoftwareinformation(**kwargs)
        if action == "getservicenowaggregatedsoftware":
            return client.getservicenowaggregatedsoftware(**kwargs)
        if action == "getfilterforfactsheet":
            return client.getfilterforfactsheet(**kwargs)
        if action == "getfilterforprovider":
            return client.getfilterforprovider(**kwargs)
        if action == "getfiltersforhardware":
            return client.getfiltersforhardware(**kwargs)
        if action == "getservicenowaggregatedhardware":
            return client.getservicenowaggregatedhardware(**kwargs)
        if action == "getstatusoverview":
            return client.getstatusoverview(**kwargs)
        if action == "getallconfigurations":
            return client.getallconfigurations(**kwargs)
        if action == "createconfiguration":
            return client.createconfiguration(**kwargs)
        if action == "getconfiguration":
            return client.getconfiguration(**kwargs)
        if action == "updateconfiguration":
            return client.updateconfiguration(**kwargs)
        if action == "deleteconfiguration":
            return client.deleteconfiguration(**kwargs)
        if action == "synchronize":
            return client.synchronize(**kwargs)
        if action == "validateconfiguration":
            return client.validateconfiguration(**kwargs)
        if action == "validateservicenowcredentials":
            return client.validateservicenowcredentials(**kwargs)
        if action == "getfilters":
            return client.getfilters(**kwargs)
        if action == "getservicenowsyncconstraintrules":
            return client.getservicenowsyncconstraintrules(**kwargs)
        if action == "getavailablerelcirelations":
            return client.getavailablerelcirelations(**kwargs)
        if action == "getinstalledservicenowpluginversion":
            return client.getinstalledservicenowpluginversion(**kwargs)
        if action == "getmappingtablerelations":
            return client.getmappingtablerelations(**kwargs)
        if action == "getreferencefieldrelations":
            return client.getreferencefieldrelations(**kwargs)
        if action == "getservicenowmetadata":
            return client.getservicenowmetadata(**kwargs)
        if action == "gettables":
            return client.gettables(**kwargs)
        if action == "changes":
            return client.changes(**kwargs)
        if action == "hooks":
            return client.hooks(**kwargs)
        if action == "sendprompt":
            return client.sendprompt(**kwargs)
        if action == "sendpromptv2":
            return client.sendpromptv2(**kwargs)
        if action == "abortallpendingandrunningsynchronizations":
            return client.abortallpendingandrunningsynchronizations(**kwargs)
        if action == "abortsynchronization":
            return client.abortsynchronization(**kwargs)
        if action == "getcurrentlyrunningorlastcreatedrun":
            return client.getcurrentlyrunningorlastcreatedrun(**kwargs)
        if action == "getversionbyid":
            return client.getversionbyid(**kwargs)
        if action == "getversions":
            return client.getversions(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_integration_signavio_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-integration-signavio"})
    async def leanix_leanix_integration_signavio(
        action: str = Field(
            description="Action to perform. Must be one of: 'getconfigurations', 'createconfiguration', 'getconfiguration', 'updateconfiguration', 'deleteconfiguration', 'synchronizeconfiguration', 'unassignformation', 'getformations', 'getdirectories', 'createcategory', 'getfactsheetfields', 'getlabels', 'getsignavioglossaryitemfields', 'getsignavioprocessfields', 'getprocessfields', 'analyzelatestsynchronizationrun', 'analyzesynchronizationrun', 'cancelsynchronization', 'getlatestsynchronizationrunanalysis', 'getsynchronizationrunanalysis'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_integration_signavio_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix integration signavio operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "getconfigurations":
            return client.getconfigurations(**kwargs)
        if action == "createconfiguration":
            return client.createconfiguration(**kwargs)
        if action == "getconfiguration":
            return client.getconfiguration(**kwargs)
        if action == "updateconfiguration":
            return client.updateconfiguration(**kwargs)
        if action == "deleteconfiguration":
            return client.deleteconfiguration(**kwargs)
        if action == "synchronizeconfiguration":
            return client.synchronizeconfiguration(**kwargs)
        if action == "unassignformation":
            return client.unassignformation(**kwargs)
        if action == "getformations":
            return client.getformations(**kwargs)
        if action == "getdirectories":
            return client.getdirectories(**kwargs)
        if action == "createcategory":
            return client.createcategory(**kwargs)
        if action == "getfactsheetfields":
            return client.getfactsheetfields(**kwargs)
        if action == "getlabels":
            return client.getlabels(**kwargs)
        if action == "getsignavioglossaryitemfields":
            return client.getsignavioglossaryitemfields(**kwargs)
        if action == "getsignavioprocessfields":
            return client.getsignavioprocessfields(**kwargs)
        if action == "getprocessfields":
            return client.getprocessfields(**kwargs)
        if action == "analyzelatestsynchronizationrun":
            return client.analyzelatestsynchronizationrun(**kwargs)
        if action == "analyzesynchronizationrun":
            return client.analyzesynchronizationrun(**kwargs)
        if action == "cancelsynchronization":
            return client.cancelsynchronization(**kwargs)
        if action == "getlatestsynchronizationrunanalysis":
            return client.getlatestsynchronizationrunanalysis(**kwargs)
        if action == "getsynchronizationrunanalysis":
            return client.getsynchronizationrunanalysis(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_inventory_data_quality_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-inventory-data-quality"})
    async def leanix_leanix_inventory_data_quality(
        action: str = Field(
            description="Action to perform. Must be one of: 'refreshembeddings', 'getrecommendationsapptobc', 'getrecommendationsagenttobc', 'submitfeedback', 'submitfeedback_1', 'submitdqicardfeedback', 'getdatamodel', 'getrelationnames', 'getfactsheettypes'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_inventory_data_quality_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix inventory data quality operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "refreshembeddings":
            return client.refreshembeddings(**kwargs)
        if action == "getrecommendationsapptobc":
            return client.getrecommendationsapptobc(**kwargs)
        if action == "getrecommendationsagenttobc":
            return client.getrecommendationsagenttobc(**kwargs)
        if action == "submitfeedback":
            return client.submitfeedback(**kwargs)
        if action == "submitfeedback_1":
            return client.submitfeedback_1(**kwargs)
        if action == "submitdqicardfeedback":
            return client.submitdqicardfeedback(**kwargs)
        if action == "getdatamodel":
            return client.getdatamodel(**kwargs)
        if action == "getrelationnames":
            return client.getrelationnames(**kwargs)
        if action == "getfactsheettypes":
            return client.getfactsheettypes(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_mtm_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-mtm"})
    async def leanix_leanix_mtm(
        action: str = Field(
            description="Action to perform. Must be one of: 'getaiaccess', 'gettaskbyid', 'createworkspacelabel', 'deleteworkspacelabel', 'getall', 'getlabelsbyworkspace', 'getlabelsbyworkspaces', 'token', 'get_data_breach_contact', 'add_data_breach_contact', 'delete_data_breach_contact', 'get_accounts', 'create_account', 'get_account', 'update_account', 'delete_account', 'get_contracts', 'get_events', 'get_instances', 'get_settings', 'get_users', 'get_workspaces', 'getapitokens', 'createapitoken', 'getapitoken', 'updateapitoken', 'deleteapitoken', 'getfeature', 'accessfeature', 'getapplication', 'getapplications', 'getedition', 'geteditions', 'getfeatures', 'create_contract', 'get_contract', 'update_contract', 'delete_contract', 'get_custom_features', 'create_custom_feature', 'get_custom_feature', 'update_custom_feature', 'delete_custom_feature', 'deletedomain', 'getdomain', 'getdomains', 'upsertdomain', 'getidentityproviders', 'getworkspaces_2', 'create_event', 'get_event', 'update_event', 'getraw', 'get_export', 'process_graph_ql', 'get_identity_providers', 'create_identity_provider', 'get_identity_provider', 'update_identity_provider', 'delete_identity_provider', 'get_domains', 'get_metadata', 'getworkspaces_3', 'activate', 'authenticate', 'checkip', 'invite', 'login', 'loginpractitioner', 'logout', 'reset_password', 'review', 'set_password', 'switchpermissionrole', 'inactive', 'create_instance', 'get_instance', 'update_instance', 'delete_instance', 'getinstancesbyworkspace', 'getpreferredinstance', 'switchdefaultinstance', 'list', 'create', 'invalidate', 'getpermissions', 'createpermission', 'getpermission', 'getsettings_2', 'getuserrandom', 'getsettings_3', 'createsetting', 'getsetting', 'updatesetting', 'deletesetting', 'getnotificationsettings', 'setworkspacenotificationstatus', 'gettechnicalusers', 'create_technical_user', 'get_technical_user', 'update_technical_user', 'delete_technical_user', 'replace_technical_user_api_token', 'getusers_1', 'createuser', 'createuserpassword', 'getevents_6', 'getpermissions_1', 'getsettings_4', 'getuser', 'updateuser', 'getuserrandom_1', 'setpassword_1', 'create_workspace', 'get_workspace', 'update_workspace', 'delete_workspace', 'get_feature_bundle', 'get_impersonations', 'get_permission', 'get_permission_stats', 'get_permissions', 'get_support_permissions', 'get_user_list_export', 'getworkspacesforbackup', 'permissions_search', 'getuserpiichanges', 'get_user_segment', 'create_or_update_user_segment', 'getworkspacemaintenance', 'createworkspacemaintenance', 'deleteworkspacemaintenance'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_mtm_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix mtm operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "getaiaccess":
            return client.getaiaccess(**kwargs)
        if action == "gettaskbyid":
            return client.gettaskbyid(**kwargs)
        if action == "createworkspacelabel":
            return client.createworkspacelabel(**kwargs)
        if action == "deleteworkspacelabel":
            return client.deleteworkspacelabel(**kwargs)
        if action == "getall":
            return client.getall(**kwargs)
        if action == "getlabelsbyworkspace":
            return client.getlabelsbyworkspace(**kwargs)
        if action == "getlabelsbyworkspaces":
            return client.getlabelsbyworkspaces(**kwargs)
        if action == "token":
            return client.token(**kwargs)
        if action == "get_data_breach_contact":
            return client.get_data_breach_contact(**kwargs)
        if action == "add_data_breach_contact":
            return client.add_data_breach_contact(**kwargs)
        if action == "delete_data_breach_contact":
            return client.delete_data_breach_contact(**kwargs)
        if action == "get_accounts":
            return client.get_accounts(**kwargs)
        if action == "create_account":
            return client.create_account(**kwargs)
        if action == "get_account":
            return client.get_account(**kwargs)
        if action == "update_account":
            return client.update_account(**kwargs)
        if action == "delete_account":
            return client.delete_account(**kwargs)
        if action == "get_contracts":
            return client.get_contracts(**kwargs)
        if action == "get_events":
            return client.get_events(**kwargs)
        if action == "get_instances":
            return client.get_instances(**kwargs)
        if action == "get_settings":
            return client.get_settings(**kwargs)
        if action == "get_users":
            return client.get_users(**kwargs)
        if action == "get_workspaces":
            return client.get_workspaces(**kwargs)
        if action == "getapitokens":
            return client.getapitokens(**kwargs)
        if action == "createapitoken":
            return client.createapitoken(**kwargs)
        if action == "getapitoken":
            return client.getapitoken(**kwargs)
        if action == "updateapitoken":
            return client.updateapitoken(**kwargs)
        if action == "deleteapitoken":
            return client.deleteapitoken(**kwargs)
        if action == "getfeature":
            return client.getfeature(**kwargs)
        if action == "accessfeature":
            return client.accessfeature(**kwargs)
        if action == "getapplication":
            return client.getapplication(**kwargs)
        if action == "getapplications":
            return client.getapplications(**kwargs)
        if action == "getedition":
            return client.getedition(**kwargs)
        if action == "geteditions":
            return client.geteditions(**kwargs)
        if action == "getfeatures":
            return client.getfeatures(**kwargs)
        if action == "create_contract":
            return client.create_contract(**kwargs)
        if action == "get_contract":
            return client.get_contract(**kwargs)
        if action == "update_contract":
            return client.update_contract(**kwargs)
        if action == "delete_contract":
            return client.delete_contract(**kwargs)
        if action == "get_custom_features":
            return client.get_custom_features(**kwargs)
        if action == "create_custom_feature":
            return client.create_custom_feature(**kwargs)
        if action == "get_custom_feature":
            return client.get_custom_feature(**kwargs)
        if action == "update_custom_feature":
            return client.update_custom_feature(**kwargs)
        if action == "delete_custom_feature":
            return client.delete_custom_feature(**kwargs)
        if action == "deletedomain":
            return client.deletedomain(**kwargs)
        if action == "getdomain":
            return client.getdomain(**kwargs)
        if action == "getdomains":
            return client.getdomains(**kwargs)
        if action == "upsertdomain":
            return client.upsertdomain(**kwargs)
        if action == "getidentityproviders":
            return client.getidentityproviders(**kwargs)
        if action == "getworkspaces_2":
            return client.getworkspaces_2(**kwargs)
        if action == "create_event":
            return client.create_event(**kwargs)
        if action == "get_event":
            return client.get_event(**kwargs)
        if action == "update_event":
            return client.update_event(**kwargs)
        if action == "getraw":
            return client.getraw(**kwargs)
        if action == "get_export":
            return client.get_export(**kwargs)
        if action == "process_graph_ql":
            return client.process_graph_ql(**kwargs)
        if action == "get_identity_providers":
            return client.get_identity_providers(**kwargs)
        if action == "create_identity_provider":
            return client.create_identity_provider(**kwargs)
        if action == "get_identity_provider":
            return client.get_identity_provider(**kwargs)
        if action == "update_identity_provider":
            return client.update_identity_provider(**kwargs)
        if action == "delete_identity_provider":
            return client.delete_identity_provider(**kwargs)
        if action == "get_domains":
            return client.get_domains(**kwargs)
        if action == "get_metadata":
            return client.get_metadata(**kwargs)
        if action == "getworkspaces_3":
            return client.getworkspaces_3(**kwargs)
        if action == "activate":
            return client.activate(**kwargs)
        if action == "authenticate":
            return client.authenticate(**kwargs)
        if action == "checkip":
            return client.checkip(**kwargs)
        if action == "invite":
            return client.invite(**kwargs)
        if action == "login":
            return client.login(**kwargs)
        if action == "loginpractitioner":
            return client.loginpractitioner(**kwargs)
        if action == "logout":
            return client.logout(**kwargs)
        if action == "reset_password":
            return client.reset_password(**kwargs)
        if action == "review":
            return client.review(**kwargs)
        if action == "set_password":
            return client.set_password(**kwargs)
        if action == "switchpermissionrole":
            return client.switchpermissionrole(**kwargs)
        if action == "inactive":
            return client.inactive(**kwargs)
        if action == "create_instance":
            return client.create_instance(**kwargs)
        if action == "get_instance":
            return client.get_instance(**kwargs)
        if action == "update_instance":
            return client.update_instance(**kwargs)
        if action == "delete_instance":
            return client.delete_instance(**kwargs)
        if action == "getinstancesbyworkspace":
            return client.getinstancesbyworkspace(**kwargs)
        if action == "getpreferredinstance":
            return client.getpreferredinstance(**kwargs)
        if action == "switchdefaultinstance":
            return client.switchdefaultinstance(**kwargs)
        if action == "list":
            return client.list(**kwargs)
        if action == "create":
            return client.create(**kwargs)
        if action == "invalidate":
            return client.invalidate(**kwargs)
        if action == "getpermissions":
            return client.getpermissions(**kwargs)
        if action == "createpermission":
            return client.createpermission(**kwargs)
        if action == "getpermission":
            return client.getpermission(**kwargs)
        if action == "getsettings_2":
            return client.getsettings_2(**kwargs)
        if action == "getuserrandom":
            return client.getuserrandom(**kwargs)
        if action == "getsettings_3":
            return client.getsettings_3(**kwargs)
        if action == "createsetting":
            return client.createsetting(**kwargs)
        if action == "getsetting":
            return client.getsetting(**kwargs)
        if action == "updatesetting":
            return client.updatesetting(**kwargs)
        if action == "deletesetting":
            return client.deletesetting(**kwargs)
        if action == "getnotificationsettings":
            return client.getnotificationsettings(**kwargs)
        if action == "setworkspacenotificationstatus":
            return client.setworkspacenotificationstatus(**kwargs)
        if action == "gettechnicalusers":
            return client.gettechnicalusers(**kwargs)
        if action == "create_technical_user":
            return client.create_technical_user(**kwargs)
        if action == "get_technical_user":
            return client.get_technical_user(**kwargs)
        if action == "update_technical_user":
            return client.update_technical_user(**kwargs)
        if action == "delete_technical_user":
            return client.delete_technical_user(**kwargs)
        if action == "replace_technical_user_api_token":
            return client.replace_technical_user_api_token(**kwargs)
        if action == "getusers_1":
            return client.getusers_1(**kwargs)
        if action == "createuser":
            return client.createuser(**kwargs)
        if action == "createuserpassword":
            return client.createuserpassword(**kwargs)
        if action == "getevents_6":
            return client.getevents_6(**kwargs)
        if action == "getpermissions_1":
            return client.getpermissions_1(**kwargs)
        if action == "getsettings_4":
            return client.getsettings_4(**kwargs)
        if action == "getuser":
            return client.getuser(**kwargs)
        if action == "updateuser":
            return client.updateuser(**kwargs)
        if action == "getuserrandom_1":
            return client.getuserrandom_1(**kwargs)
        if action == "setpassword_1":
            return client.setpassword_1(**kwargs)
        if action == "create_workspace":
            return client.create_workspace(**kwargs)
        if action == "get_workspace":
            return client.get_workspace(**kwargs)
        if action == "update_workspace":
            return client.update_workspace(**kwargs)
        if action == "delete_workspace":
            return client.delete_workspace(**kwargs)
        if action == "get_feature_bundle":
            return client.get_feature_bundle(**kwargs)
        if action == "get_impersonations":
            return client.get_impersonations(**kwargs)
        if action == "get_permission":
            return client.get_permission(**kwargs)
        if action == "get_permission_stats":
            return client.get_permission_stats(**kwargs)
        if action == "get_permissions":
            return client.get_permissions(**kwargs)
        if action == "get_support_permissions":
            return client.get_support_permissions(**kwargs)
        if action == "get_user_list_export":
            return client.get_user_list_export(**kwargs)
        if action == "getworkspacesforbackup":
            return client.getworkspacesforbackup(**kwargs)
        if action == "permissions_search":
            return client.permissions_search(**kwargs)
        if action == "getuserpiichanges":
            return client.getuserpiichanges(**kwargs)
        if action == "get_user_segment":
            return client.get_user_segment(**kwargs)
        if action == "create_or_update_user_segment":
            return client.create_or_update_user_segment(**kwargs)
        if action == "getworkspacemaintenance":
            return client.getworkspacemaintenance(**kwargs)
        if action == "createworkspacemaintenance":
            return client.createworkspacemaintenance(**kwargs)
        if action == "deleteworkspacemaintenance":
            return client.deleteworkspacemaintenance(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_managed_code_execution_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-managed-code-execution"})
    async def leanix_leanix_managed_code_execution(
        action: str = Field(
            description="Action to perform. Must be one of: 'getsecretbyid', 'updatesecret', 'deletesecret', 'getexecutionconfiguration', 'updateexecutionconfiguration', 'deleteexecutionconfiguration', 'updateexecutionconfigurationcapability', 'getallsecrets', 'createsecret', 'getexecutionconfigurations', 'createexecutionconfiguration', 'getexecutionconfigurationsbysecretid', 'getexecutionlogs', 'getexecutionlog', 'getexecutionconfigurationhistory'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_managed_code_execution_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix managed code execution operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "getsecretbyid":
            return client.getsecretbyid(**kwargs)
        if action == "updatesecret":
            return client.updatesecret(**kwargs)
        if action == "deletesecret":
            return client.deletesecret(**kwargs)
        if action == "getexecutionconfiguration":
            return client.getexecutionconfiguration(**kwargs)
        if action == "updateexecutionconfiguration":
            return client.updateexecutionconfiguration(**kwargs)
        if action == "deleteexecutionconfiguration":
            return client.deleteexecutionconfiguration(**kwargs)
        if action == "updateexecutionconfigurationcapability":
            return client.updateexecutionconfigurationcapability(**kwargs)
        if action == "getallsecrets":
            return client.getallsecrets(**kwargs)
        if action == "createsecret":
            return client.createsecret(**kwargs)
        if action == "getexecutionconfigurations":
            return client.getexecutionconfigurations(**kwargs)
        if action == "createexecutionconfiguration":
            return client.createexecutionconfiguration(**kwargs)
        if action == "getexecutionconfigurationsbysecretid":
            return client.getexecutionconfigurationsbysecretid(**kwargs)
        if action == "getexecutionlogs":
            return client.getexecutionlogs(**kwargs)
        if action == "getexecutionlog":
            return client.getexecutionlog(**kwargs)
        if action == "getexecutionconfigurationhistory":
            return client.getexecutionconfigurationhistory(**kwargs)
        raise ValueError(f"Unknown action: {action}")


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


def register_leanix_navigation_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-navigation"})
    async def leanix_leanix_navigation(
        action: str = Field(
            description="Action to perform. Must be one of: 'getallcollectiongroups', 'createcollectiongroup', 'batchputcollectiongroups', 'getcollectiongroupbyid', 'putcollectiongroupbyid', 'deletecollectiongroupbyid', 'postcollection', 'getcollections', 'putcollection', 'deletecollection', 'putcollectionnavigationitem', 'postcollectionnavigationitem', 'deletecollectionnavigationitem', 'getcollectionfolders', 'postfoldercontroller', 'updatefoldercontroller', 'executebatchmove', 'executebatchdelete', 'searchnavigationitem', 'getnavigationitemfavorite', 'postnavigationitemfavorite', 'deletenavigationitemfavorite', 'createslide', 'putslidebyid', 'deleteslidebyid', 'searchpresentation', 'createpresentation', 'getpresentationbyid', 'putpresentationbyid', 'deletepresentationbyid', 'getpresentationsharesbyid', 'sharepresentation', 'deletepresentationsharebyid'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_navigation_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix navigation operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "getallcollectiongroups":
            return client.getallcollectiongroups(**kwargs)
        if action == "createcollectiongroup":
            return client.createcollectiongroup(**kwargs)
        if action == "batchputcollectiongroups":
            return client.batchputcollectiongroups(**kwargs)
        if action == "getcollectiongroupbyid":
            return client.getcollectiongroupbyid(**kwargs)
        if action == "putcollectiongroupbyid":
            return client.putcollectiongroupbyid(**kwargs)
        if action == "deletecollectiongroupbyid":
            return client.deletecollectiongroupbyid(**kwargs)
        if action == "postcollection":
            return client.postcollection(**kwargs)
        if action == "getcollections":
            return client.getcollections(**kwargs)
        if action == "putcollection":
            return client.putcollection(**kwargs)
        if action == "deletecollection":
            return client.deletecollection(**kwargs)
        if action == "putcollectionnavigationitem":
            return client.putcollectionnavigationitem(**kwargs)
        if action == "postcollectionnavigationitem":
            return client.postcollectionnavigationitem(**kwargs)
        if action == "deletecollectionnavigationitem":
            return client.deletecollectionnavigationitem(**kwargs)
        if action == "getcollectionfolders":
            return client.getcollectionfolders(**kwargs)
        if action == "postfoldercontroller":
            return client.postfoldercontroller(**kwargs)
        if action == "updatefoldercontroller":
            return client.updatefoldercontroller(**kwargs)
        if action == "executebatchmove":
            return client.executebatchmove(**kwargs)
        if action == "executebatchdelete":
            return client.executebatchdelete(**kwargs)
        if action == "searchnavigationitem":
            return client.searchnavigationitem(**kwargs)
        if action == "getnavigationitemfavorite":
            return client.getnavigationitemfavorite(**kwargs)
        if action == "postnavigationitemfavorite":
            return client.postnavigationitemfavorite(**kwargs)
        if action == "deletenavigationitemfavorite":
            return client.deletenavigationitemfavorite(**kwargs)
        if action == "createslide":
            return client.createslide(**kwargs)
        if action == "putslidebyid":
            return client.putslidebyid(**kwargs)
        if action == "deleteslidebyid":
            return client.deleteslidebyid(**kwargs)
        if action == "searchpresentation":
            return client.searchpresentation(**kwargs)
        if action == "createpresentation":
            return client.createpresentation(**kwargs)
        if action == "getpresentationbyid":
            return client.getpresentationbyid(**kwargs)
        if action == "putpresentationbyid":
            return client.putpresentationbyid(**kwargs)
        if action == "deletepresentationbyid":
            return client.deletepresentationbyid(**kwargs)
        if action == "getpresentationsharesbyid":
            return client.getpresentationsharesbyid(**kwargs)
        if action == "sharepresentation":
            return client.sharepresentation(**kwargs)
        if action == "deletepresentationsharebyid":
            return client.deletepresentationsharebyid(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_pathfinder_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-pathfinder"})
    async def leanix_leanix_pathfinder(
        action: str = Field(
            description="Action to perform. Must be one of: 'download_asset', 'upsert_asset', 'delete_asset', 'get_bookmark_shares', 'createbookmarkshare', 'deletebookmarkshare', 'get_bookmark', 'update_bookmark', 'delete_bookmark', 'change_bookmark_owner', 'get_bookmarks', 'create_bookmark', 'get_all_versions_for_bookmark', 'get_data_model', 'update_data_model', 'get_enriched_data_model', 'create_full_export', 'download_export_file', 'get_exports', 'get_fact_sheet', 'update_fact_sheet', 'archive_fact_sheet', 'get_fact_sheets', 'create_fact_sheet', 'get_fact_sheet_relations', 'create_fact_sheet_relation', 'updatefactsheetrelation', 'delete_fact_sheet_relation', 'get_fact_sheet_hierarchy', 'get_feature', 'upsertfeature', 'get_features', 'process_graph_ql', 'process_graph_ql_multipart', 'get_access_control_entities', 'create_access_control_entity', 'readaccesscontrolentity', 'update_access_control_entity', 'delete_access_control_entity', 'get_authorization', 'update_authorization', 'get_fact_sheet_resource_model', 'update_fact_sheet_resource_model', 'get_language', 'update_language', 'get_reporting_model', 'update_reporting_model', 'get_view_model', 'update_view_model', 'get_model_customization', 'updatemodelswithcustomization', 'get_settings', 'update_settings', 'get_suggestions', 'get_meta_model', 'get_meta_model_actions', 'post_meta_model_actions', 'get_meta_model_actions_audit_log', 'get_meta_model_job', 'get_meta_model_permission_roles', 'get_meta_model_actions_for_node', 'get_action_batch', 'get_action_batches', 'post_action_batches', 'get_meta_model_authorization', 'get_meta_model_root', 'get_meta_model_for_type', 'get_preview_of_affected_data'"
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
        if action == "createbookmarkshare":
            return client.createbookmarkshare(**kwargs)
        if action == "deletebookmarkshare":
            return client.deletebookmarkshare(**kwargs)
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
        if action == "updatefactsheetrelation":
            return client.updatefactsheetrelation(**kwargs)
        if action == "delete_fact_sheet_relation":
            return client.delete_fact_sheet_relation(**kwargs)
        if action == "get_fact_sheet_hierarchy":
            return client.get_fact_sheet_hierarchy(**kwargs)
        if action == "get_feature":
            return client.get_feature(**kwargs)
        if action == "upsertfeature":
            return client.upsertfeature(**kwargs)
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
        if action == "readaccesscontrolentity":
            return client.readaccesscontrolentity(**kwargs)
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
        if action == "updatemodelswithcustomization":
            return client.updatemodelswithcustomization(**kwargs)
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


def register_leanix_poll_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-poll"})
    async def leanix_leanix_poll(
        action: str = Field(
            description="Action to perform. Must be one of: 'replay', 'get_polls_for_factsheet', 'get_polls', 'create_poll', 'get_poll', 'update_poll', 'delete_poll', 'get_poll_count', 'get_poll_recipient_details', 'get_poll_poll_runs', 'get_poll_result', 'update_poll_result', 'check_for_new_fact_sheets', 'create_poll_reminder', 'get_poll_runs', 'create_poll_run', 'get_poll_run', 'update_poll_run', 'delete_poll_run', 'get_added_recipients_for_run', 'get_poll_results_for_user', 'get_poll_run_results', 'get_poll_runs_kpi_counts', 'get_recipients_for_poll_run', 'get_reminders', 'get_results_for_poll_run', 'set_status', 'get_all', 'create_poll_template', 'get_by_id', 'delete_by_id'"
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


def register_leanix_discovery_sap_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-discovery-sap"})
    async def leanix_leanix_discovery_sap(
        action: str = Field(
            description="Action to perform. Must be one of: 'appcontroller_heartbeat', 'demodatacontroller_demodatalist', 'demodatacontroller_createcustomdemodata', 'integrationscontroller_integrationcreate', 'integrationscontroller_integrationslist', 'integrationscontroller_integrationget', 'integrationscontroller_integrationdelete', 'integrationscontroller_integrationpatch', 'integrationscontroller_integrationtriggersync'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_discovery_sap_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix discovery sap operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "appcontroller_heartbeat":
            return client.appcontroller_heartbeat(**kwargs)
        if action == "demodatacontroller_demodatalist":
            return client.demodatacontroller_demodatalist(**kwargs)
        if action == "demodatacontroller_createcustomdemodata":
            return client.demodatacontroller_createcustomdemodata(**kwargs)
        if action == "integrationscontroller_integrationcreate":
            return client.integrationscontroller_integrationcreate(**kwargs)
        if action == "integrationscontroller_integrationslist":
            return client.integrationscontroller_integrationslist(**kwargs)
        if action == "integrationscontroller_integrationget":
            return client.integrationscontroller_integrationget(**kwargs)
        if action == "integrationscontroller_integrationdelete":
            return client.integrationscontroller_integrationdelete(**kwargs)
        if action == "integrationscontroller_integrationpatch":
            return client.integrationscontroller_integrationpatch(**kwargs)
        if action == "integrationscontroller_integrationtriggersync":
            return client.integrationscontroller_integrationtriggersync(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_technology_discovery_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-technology-discovery"})
    async def leanix_leanix_technology_discovery(
        action: str = Field(
            description="Action to perform. Must be one of: 'leanix_v1_microservice_discovery_yaml_manifest_register', 'leanix_v1_factsheets_sboms_ingest', 'leanix_v1_factsheets_sboms_ingest_1', 'getcomponentsbyapplication', 'searchcomponentsbypurl', 'getalltechstacks', 'updatetechstackbyqueryparam', 'createtechstack', 'deletetechstackbyqueryparam', 'previewmatches', 'gettechstackdetailsbyqueryparam', 'getaggregatedcounts', 'getfactsheetsbylibrary', 'getlibraryusagedetails', 'getversionsbylibrary', 'getlibraries'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_technology_discovery_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix technology discovery operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "leanix_v1_microservice_discovery_yaml_manifest_register":
            return client.leanix_v1_microservice_discovery_yaml_manifest_register(
                **kwargs
            )
        if action == "leanix_v1_factsheets_sboms_ingest":
            return client.leanix_v1_factsheets_sboms_ingest(**kwargs)
        if action == "leanix_v1_factsheets_sboms_ingest_1":
            return client.leanix_v1_factsheets_sboms_ingest_1(**kwargs)
        if action == "getcomponentsbyapplication":
            return client.getcomponentsbyapplication(**kwargs)
        if action == "searchcomponentsbypurl":
            return client.searchcomponentsbypurl(**kwargs)
        if action == "getalltechstacks":
            return client.getalltechstacks(**kwargs)
        if action == "updatetechstackbyqueryparam":
            return client.updatetechstackbyqueryparam(**kwargs)
        if action == "createtechstack":
            return client.createtechstack(**kwargs)
        if action == "deletetechstackbyqueryparam":
            return client.deletetechstackbyqueryparam(**kwargs)
        if action == "previewmatches":
            return client.previewmatches(**kwargs)
        if action == "gettechstackdetailsbyqueryparam":
            return client.gettechstackdetailsbyqueryparam(**kwargs)
        if action == "getaggregatedcounts":
            return client.getaggregatedcounts(**kwargs)
        if action == "getfactsheetsbylibrary":
            return client.getfactsheetsbylibrary(**kwargs)
        if action == "getlibraryusagedetails":
            return client.getlibraryusagedetails(**kwargs)
        if action == "getversionsbylibrary":
            return client.getversionsbylibrary(**kwargs)
        if action == "getlibraries":
            return client.getlibraries(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_storage_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-storage"})
    async def leanix_leanix_storage(
        action: str = Field(
            description="Action to perform. Must be one of: 'getavatar', 'setavatar', 'deleteavatar', 'getlogo', 'setlogo', 'deletelogo', 'getfiles', 'addfiletoworkspace', 'deletefiles', 'getfile', 'deletefile', 'getfilecontent', 'setfileowner'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_storage_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix storage operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "getavatar":
            return client.getavatar(**kwargs)
        if action == "setavatar":
            return client.setavatar(**kwargs)
        if action == "deleteavatar":
            return client.deleteavatar(**kwargs)
        if action == "getlogo":
            return client.getlogo(**kwargs)
        if action == "setlogo":
            return client.setlogo(**kwargs)
        if action == "deletelogo":
            return client.deletelogo(**kwargs)
        if action == "getfiles":
            return client.getfiles(**kwargs)
        if action == "addfiletoworkspace":
            return client.addfiletoworkspace(**kwargs)
        if action == "deletefiles":
            return client.deletefiles(**kwargs)
        if action == "getfile":
            return client.getfile(**kwargs)
        if action == "deletefile":
            return client.deletefile(**kwargs)
        if action == "getfilecontent":
            return client.getfilecontent(**kwargs)
        if action == "setfileowner":
            return client.setfileowner(**kwargs)
        raise ValueError(f"Unknown action: {action}")


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


def register_leanix_synclog_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-synclog"})
    async def leanix_leanix_synclog(
        action: str = Field(
            description="Action to perform. Must be one of: 'getsyncitems', 'addsyncitembatch', 'getsynchronizations', 'createsynchronization', 'getsyncitems_1', 'deletesyncitems', 'getsynchronization', 'updatesynchronization', 'gettopics', 'gettriggers', 'requestabortion'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_synclog_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix synclog operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "getsyncitems":
            return client.getsyncitems(**kwargs)
        if action == "addsyncitembatch":
            return client.addsyncitembatch(**kwargs)
        if action == "getsynchronizations":
            return client.getsynchronizations(**kwargs)
        if action == "createsynchronization":
            return client.createsynchronization(**kwargs)
        if action == "getsyncitems_1":
            return client.getsyncitems_1(**kwargs)
        if action == "deletesyncitems":
            return client.deletesyncitems(**kwargs)
        if action == "getsynchronization":
            return client.getsynchronization(**kwargs)
        if action == "updatesynchronization":
            return client.updatesynchronization(**kwargs)
        if action == "gettopics":
            return client.gettopics(**kwargs)
        if action == "gettriggers":
            return client.gettriggers(**kwargs)
        if action == "requestabortion":
            return client.requestabortion(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_todo_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-todo"})
    async def leanix_leanix_todo(
        action: str = Field(
            description="Action to perform. Must be one of: 'managedrestorationrequests', 'managedsnapshotrequests', 'accepttodo', 'assigntome', 'get', 'createtodo', 'deletetodos', 'query', 'rejecttodo', 'replyandclosetodo', 'upserttodos'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_todo_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix todo operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "managedrestorationrequests":
            return client.managedrestorationrequests(**kwargs)
        if action == "managedsnapshotrequests":
            return client.managedsnapshotrequests(**kwargs)
        if action == "accepttodo":
            return client.accepttodo(**kwargs)
        if action == "assigntome":
            return client.assigntome(**kwargs)
        if action == "get":
            return client.get(**kwargs)
        if action == "createtodo":
            return client.createtodo(**kwargs)
        if action == "deletetodos":
            return client.deletetodos(**kwargs)
        if action == "query":
            return client.query(**kwargs)
        if action == "rejecttodo":
            return client.rejecttodo(**kwargs)
        if action == "replyandclosetodo":
            return client.replyandclosetodo(**kwargs)
        if action == "upserttodos":
            return client.upserttodos(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_transformations_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-transformations"})
    async def leanix_leanix_transformations(
        action: str = Field(
            description="Action to perform. Must be one of: 'createtransformation', 'gettransformations', 'gettransformation', 'puttransformation', 'deletetransformation', 'gettransformationcustomimpacts', 'posttransformationcustomimpacts', 'puttransformationcustomimpacts', 'deletetransformationcustomimpacts', 'posttransformationexecution', 'posttransformationsexecution'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_transformations_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix transformations operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "createtransformation":
            return client.createtransformation(**kwargs)
        if action == "gettransformations":
            return client.gettransformations(**kwargs)
        if action == "gettransformation":
            return client.gettransformation(**kwargs)
        if action == "puttransformation":
            return client.puttransformation(**kwargs)
        if action == "deletetransformation":
            return client.deletetransformation(**kwargs)
        if action == "gettransformationcustomimpacts":
            return client.gettransformationcustomimpacts(**kwargs)
        if action == "posttransformationcustomimpacts":
            return client.posttransformationcustomimpacts(**kwargs)
        if action == "puttransformationcustomimpacts":
            return client.puttransformationcustomimpacts(**kwargs)
        if action == "deletetransformationcustomimpacts":
            return client.deletetransformationcustomimpacts(**kwargs)
        if action == "posttransformationexecution":
            return client.posttransformationexecution(**kwargs)
        if action == "posttransformationsexecution":
            return client.posttransformationsexecution(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_leanix_webhooks_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-webhooks"})
    async def leanix_leanix_webhooks(
        action: str = Field(
            description="Action to perform. Must be one of: 'getcustomeventtags', 'createcustomeventtag', 'updatecustomeventtag', 'deletecustomeventtag', 'createevent', 'createeventbatch', 'geteventtags', 'getsubscriptions', 'createsubscription', 'getsubscription', 'updatesubscription', 'deletesubscription', 'getsubscriptiondeliveries', 'getsubscriptionevents', 'getsubscriptionstatus', 'getsubscriptionstatuses', 'updatesubscriptioncursor'"
        ),
        params_json: str = Field(
            default="{}", description="JSON string of parameters to pass to the action."
        ),
        client=Depends(get_webhooks_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Manage leanix leanix webhooks operations."""
        if ctx:
            ctx.info("Executing tool...")
        import json

        try:
            kwargs = json.loads(params_json)
        except Exception as e:
            return {"error": f"Invalid params_json: {e}"}

        kwargs = {k: v for k, v in kwargs.items() if v is not None}

        if action == "getcustomeventtags":
            return client.getcustomeventtags(**kwargs)
        if action == "createcustomeventtag":
            return client.createcustomeventtag(**kwargs)
        if action == "updatecustomeventtag":
            return client.updatecustomeventtag(**kwargs)
        if action == "deletecustomeventtag":
            return client.deletecustomeventtag(**kwargs)
        if action == "createevent":
            return client.createevent(**kwargs)
        if action == "createeventbatch":
            return client.createeventbatch(**kwargs)
        if action == "geteventtags":
            return client.geteventtags(**kwargs)
        if action == "getsubscriptions":
            return client.getsubscriptions(**kwargs)
        if action == "createsubscription":
            return client.createsubscription(**kwargs)
        if action == "getsubscription":
            return client.getsubscription(**kwargs)
        if action == "updatesubscription":
            return client.updatesubscription(**kwargs)
        if action == "deletesubscription":
            return client.deletesubscription(**kwargs)
        if action == "getsubscriptiondeliveries":
            return client.getsubscriptiondeliveries(**kwargs)
        if action == "getsubscriptionevents":
            return client.getsubscriptionevents(**kwargs)
        if action == "getsubscriptionstatus":
            return client.getsubscriptionstatus(**kwargs)
        if action == "getsubscriptionstatuses":
            return client.getsubscriptionstatuses(**kwargs)
        if action == "updatesubscriptioncursor":
            return client.updatesubscriptioncursor(**kwargs)
        raise ValueError(f"Unknown action: {action}")


def register_graphql_tools(mcp: FastMCP):
    from leanix_agent.auth import get_graphql_client

    @mcp.tool(tags={"graphql"})
    async def leanix_graphql(
        query: str = Field(
            description="The raw GraphQL query or mutation string to execute against the LeanIX Pathfinder API."
        ),
        variables: str = Field(
            default="{}",
            description="JSON string of variables to pass along with the query.",
        ),
        operation_name: str | None = Field(
            default=None,
            description="Optional operation name if executing a specific query within the document.",
        ),
        client=Depends(get_graphql_client),
        ctx: Context | None = Field(
            default=None, description="MCP context for progress reporting"
        ),
    ) -> dict:
        """Execute raw GraphQL queries and mutations natively on LeanIX Pathfinder API."""
        if ctx:
            await ctx.info("Executing LeanIX GraphQL query...")
        import json

        try:
            vars_dict = json.loads(variables) if variables else None
        except Exception as e:
            return {"error": f"Invalid variables JSON: {e}"}

        try:
            return client.execute_gql(
                query_str=query, variables=vars_dict, operation_name=operation_name
            )
        except Exception as e:
            return {"error": f"GraphQL execution failed: {str(e)}"}


def get_mcp_instance() -> tuple[Any, ...]:
    """Initialize and return the MCP instance."""
    load_dotenv(find_dotenv())
    args, mcp, middlewares = create_mcp_server(
        name="leanix-agent MCP",
        version=__version__,
        instructions="leanix-agent MCP Server — Condensed Action-Routed Tools.",
    )

    @mcp.custom_route("/health", methods=["GET"])
    async def health_check(request: Request) -> JSONResponse:
        return JSONResponse({"status": "OK"})

    DEFAULT_GRAPHQLTOOL = to_boolean(os.getenv("GRAPHQLTOOL", "True"))
    if DEFAULT_GRAPHQLTOOL:
        register_graphql_tools(mcp)

    DEFAULT_LEANIX_AI_INVENTORY_BUILDERTOOL = to_boolean(
        os.getenv("LEANIX_AI_INVENTORY_BUILDERTOOL", "True")
    )
    if DEFAULT_LEANIX_AI_INVENTORY_BUILDERTOOL:
        register_leanix_ai_inventory_builder_tools(mcp)
    DEFAULT_LEANIX_APPTIO_CONNECTORTOOL = to_boolean(
        os.getenv("LEANIX_APPTIO_CONNECTORTOOL", "True")
    )
    if DEFAULT_LEANIX_APPTIO_CONNECTORTOOL:
        register_leanix_apptio_connector_tools(mcp)
    DEFAULT_LEANIX_AUTOMATIONSTOOL = to_boolean(
        os.getenv("LEANIX_AUTOMATIONSTOOL", "True")
    )
    if DEFAULT_LEANIX_AUTOMATIONSTOOL:
        register_leanix_automations_tools(mcp)
    DEFAULT_LEANIX_REFERENCE_DATA_CATALOGTOOL = to_boolean(
        os.getenv("LEANIX_REFERENCE_DATA_CATALOGTOOL", "True")
    )
    if DEFAULT_LEANIX_REFERENCE_DATA_CATALOGTOOL:
        register_leanix_reference_data_catalog_tools(mcp)
    DEFAULT_LEANIX_DISCOVERY_AI_AGENTSTOOL = to_boolean(
        os.getenv("LEANIX_DISCOVERY_AI_AGENTSTOOL", "True")
    )
    if DEFAULT_LEANIX_DISCOVERY_AI_AGENTSTOOL:
        register_leanix_discovery_ai_agents_tools(mcp)
    DEFAULT_LEANIX_DISCOVERY_LINKING_V1TOOL = to_boolean(
        os.getenv("LEANIX_DISCOVERY_LINKING_V1TOOL", "True")
    )
    if DEFAULT_LEANIX_DISCOVERY_LINKING_V1TOOL:
        register_leanix_discovery_linking_v1_tools(mcp)
    DEFAULT_LEANIX_DISCOVERY_LINKING_V2TOOL = to_boolean(
        os.getenv("LEANIX_DISCOVERY_LINKING_V2TOOL", "True")
    )
    if DEFAULT_LEANIX_DISCOVERY_LINKING_V2TOOL:
        register_leanix_discovery_linking_v2_tools(mcp)
    DEFAULT_LEANIX_DISCOVERY_SAP_EXTENSIONTOOL = to_boolean(
        os.getenv("LEANIX_DISCOVERY_SAP_EXTENSIONTOOL", "True")
    )
    if DEFAULT_LEANIX_DISCOVERY_SAP_EXTENSIONTOOL:
        register_leanix_discovery_sap_extension_tools(mcp)
    DEFAULT_LEANIX_DISCOVERY_SAASTOOL = to_boolean(
        os.getenv("LEANIX_DISCOVERY_SAASTOOL", "True")
    )
    if DEFAULT_LEANIX_DISCOVERY_SAASTOOL:
        register_leanix_discovery_saas_tools(mcp)
    DEFAULT_LEANIX_DOCUMENTSTOOL = to_boolean(os.getenv("LEANIX_DOCUMENTSTOOL", "True"))
    if DEFAULT_LEANIX_DOCUMENTSTOOL:
        register_leanix_documents_tools(mcp)
    DEFAULT_LEANIX_IMPACTSTOOL = to_boolean(os.getenv("LEANIX_IMPACTSTOOL", "True"))
    if DEFAULT_LEANIX_IMPACTSTOOL:
        register_leanix_impacts_tools(mcp)
    DEFAULT_LEANIX_INTEGRATION_APITOOL = to_boolean(
        os.getenv("LEANIX_INTEGRATION_APITOOL", "True")
    )
    if DEFAULT_LEANIX_INTEGRATION_APITOOL:
        register_leanix_integration_api_tools(mcp)
    DEFAULT_LEANIX_INTEGRATION_COLLIBRATOOL = to_boolean(
        os.getenv("LEANIX_INTEGRATION_COLLIBRATOOL", "True")
    )
    if DEFAULT_LEANIX_INTEGRATION_COLLIBRATOOL:
        register_leanix_integration_collibra_tools(mcp)
    DEFAULT_LEANIX_INTEGRATION_SERVICENOWTOOL = to_boolean(
        os.getenv("LEANIX_INTEGRATION_SERVICENOWTOOL", "True")
    )
    if DEFAULT_LEANIX_INTEGRATION_SERVICENOWTOOL:
        register_leanix_integration_servicenow_tools(mcp)
    DEFAULT_LEANIX_INTEGRATION_SIGNAVIOTOOL = to_boolean(
        os.getenv("LEANIX_INTEGRATION_SIGNAVIOTOOL", "True")
    )
    if DEFAULT_LEANIX_INTEGRATION_SIGNAVIOTOOL:
        register_leanix_integration_signavio_tools(mcp)
    DEFAULT_LEANIX_INVENTORY_DATA_QUALITYTOOL = to_boolean(
        os.getenv("LEANIX_INVENTORY_DATA_QUALITYTOOL", "True")
    )
    if DEFAULT_LEANIX_INVENTORY_DATA_QUALITYTOOL:
        register_leanix_inventory_data_quality_tools(mcp)
    DEFAULT_LEANIX_MTMTOOL = to_boolean(os.getenv("LEANIX_MTMTOOL", "True"))
    if DEFAULT_LEANIX_MTMTOOL:
        register_leanix_mtm_tools(mcp)
    DEFAULT_LEANIX_MANAGED_CODE_EXECUTIONTOOL = to_boolean(
        os.getenv("LEANIX_MANAGED_CODE_EXECUTIONTOOL", "True")
    )
    if DEFAULT_LEANIX_MANAGED_CODE_EXECUTIONTOOL:
        register_leanix_managed_code_execution_tools(mcp)
    DEFAULT_LEANIX_METRICSTOOL = to_boolean(os.getenv("LEANIX_METRICSTOOL", "True"))
    if DEFAULT_LEANIX_METRICSTOOL:
        register_leanix_metrics_tools(mcp)
    DEFAULT_LEANIX_NAVIGATIONTOOL = to_boolean(
        os.getenv("LEANIX_NAVIGATIONTOOL", "True")
    )
    if DEFAULT_LEANIX_NAVIGATIONTOOL:
        register_leanix_navigation_tools(mcp)
    DEFAULT_LEANIX_PATHFINDERTOOL = to_boolean(
        os.getenv("LEANIX_PATHFINDERTOOL", "True")
    )
    if DEFAULT_LEANIX_PATHFINDERTOOL:
        register_leanix_pathfinder_tools(mcp)
    DEFAULT_LEANIX_POLLTOOL = to_boolean(os.getenv("LEANIX_POLLTOOL", "True"))
    if DEFAULT_LEANIX_POLLTOOL:
        register_leanix_poll_tools(mcp)
    DEFAULT_LEANIX_REFERENCE_DATATOOL = to_boolean(
        os.getenv("LEANIX_REFERENCE_DATATOOL", "True")
    )
    if DEFAULT_LEANIX_REFERENCE_DATATOOL:
        register_leanix_reference_data_tools(mcp)
    DEFAULT_LEANIX_DISCOVERY_SAPTOOL = to_boolean(
        os.getenv("LEANIX_DISCOVERY_SAPTOOL", "True")
    )
    if DEFAULT_LEANIX_DISCOVERY_SAPTOOL:
        register_leanix_discovery_sap_tools(mcp)
    DEFAULT_LEANIX_TECHNOLOGY_DISCOVERYTOOL = to_boolean(
        os.getenv("LEANIX_TECHNOLOGY_DISCOVERYTOOL", "True")
    )
    if DEFAULT_LEANIX_TECHNOLOGY_DISCOVERYTOOL:
        register_leanix_technology_discovery_tools(mcp)
    DEFAULT_LEANIX_STORAGETOOL = to_boolean(os.getenv("LEANIX_STORAGETOOL", "True"))
    if DEFAULT_LEANIX_STORAGETOOL:
        register_leanix_storage_tools(mcp)
    DEFAULT_LEANIX_SURVEYTOOL = to_boolean(os.getenv("LEANIX_SURVEYTOOL", "True"))
    if DEFAULT_LEANIX_SURVEYTOOL:
        register_leanix_survey_tools(mcp)
    DEFAULT_LEANIX_SYNCLOGTOOL = to_boolean(os.getenv("LEANIX_SYNCLOGTOOL", "True"))
    if DEFAULT_LEANIX_SYNCLOGTOOL:
        register_leanix_synclog_tools(mcp)
    DEFAULT_LEANIX_TODOTOOL = to_boolean(os.getenv("LEANIX_TODOTOOL", "True"))
    if DEFAULT_LEANIX_TODOTOOL:
        register_leanix_todo_tools(mcp)
    DEFAULT_LEANIX_TRANSFORMATIONSTOOL = to_boolean(
        os.getenv("LEANIX_TRANSFORMATIONSTOOL", "True")
    )
    if DEFAULT_LEANIX_TRANSFORMATIONSTOOL:
        register_leanix_transformations_tools(mcp)
    DEFAULT_LEANIX_WEBHOOKSTOOL = to_boolean(os.getenv("LEANIX_WEBHOOKSTOOL", "True"))
    if DEFAULT_LEANIX_WEBHOOKSTOOL:
        register_leanix_webhooks_tools(mcp)

    for mw in middlewares:
        mcp.add_middleware(mw)
    return mcp, args, middlewares


def mcp_server() -> None:
    mcp, args, middlewares = get_mcp_instance()
    print(f"leanix-agent MCP v{__version__}", file=sys.stderr)
    print("\nStarting MCP Server", file=sys.stderr)
    print(f"  Transport: {args.transport.upper()}", file=sys.stderr)
    print(f"  Auth: {args.auth_type}", file=sys.stderr)

    if args.transport == "stdio":
        mcp.run(transport="stdio")
    elif args.transport == "streamable-http":
        mcp.run(transport="streamable-http", host=args.host, port=args.port)
    elif args.transport == "sse":
        mcp.run(transport="sse", host=args.host, port=args.port)
    else:
        logger.error("Invalid transport", extra={"transport": args.transport})
        sys.exit(1)


if __name__ == "__main__":
    mcp_server()
