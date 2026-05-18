#!/usr/bin/python
import warnings

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
from fastmcp import FastMCP
from fastmcp.dependencies import Depends
from fastmcp.utilities.logging import get_logger
from pydantic import Field
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

__version__ = "0.11.0"

logger = get_logger(name="leanix-agent")
logger.setLevel(logging.INFO)


def register_leanix_ai_inventory_builder_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-ai-inventory-builder"})
    async def leanix_leanix_ai_inventory_builder(
        action: str = Field(
            description="Action to perform. Must be one of: 'healthcheck', 'pipelines', 'getpipelines', 'sendpipelineaction', 'getpipelinesuggestions', 'getpipeline', 'deletepipeline', 'getpipelinefile', 'deletefailedpipelines', 'admindeletepipeline'"
        ),
        data: dict | None = Field(default=None, description="data"),
        pipeline_id: str | None = Field(default=None, description="pipeline id"),
        workspace_id: str | None = Field(default=None, description="workspace id"),
        client=Depends(get_ai_inventory_builder_client),
    ) -> dict:
        """Manage leanix ai inventory builder operations.

        Actions:
          - 'healthcheck': Healthcheck endpoint
          - 'pipelines': Create a Pipeline
          - 'getpipelines': Get all pipelines
          - 'sendpipelineaction': Send action to a pipeline
          - 'getpipelinesuggestions': Get suggestions from a pipeline that has been analyzed
          - 'getpipeline': Get a pipeline by id
          - 'deletepipeline': Delete a pipeline by id
          - 'getpipelinefile': Get file from a pipeline
          - 'deletefailedpipelines': Deletes all failed pipelines and their files
          - 'admindeletepipeline': Delete a pipeline by id (any status)
        """
        kwargs: dict[str, Any]
        if action == "healthcheck":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.healthcheck(**kwargs)
        if action == "pipelines":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.pipelines(**kwargs)
        if action == "getpipelines":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getpipelines(**kwargs)
        if action == "sendpipelineaction":
            kwargs = {"pipeline_id": pipeline_id, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.sendpipelineaction(**kwargs)
        if action == "getpipelinesuggestions":
            kwargs = {"pipeline_id": pipeline_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getpipelinesuggestions(**kwargs)
        if action == "getpipeline":
            kwargs = {"pipeline_id": pipeline_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getpipeline(**kwargs)
        if action == "deletepipeline":
            kwargs = {"pipeline_id": pipeline_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletepipeline(**kwargs)
        if action == "getpipelinefile":
            kwargs = {"pipeline_id": pipeline_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getpipelinefile(**kwargs)
        if action == "deletefailedpipelines":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletefailedpipelines(**kwargs)
        if action == "admindeletepipeline":
            kwargs = {
                "workspace_id": workspace_id,
                "pipeline_id": pipeline_id,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.admindeletepipeline(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: healthcheck', 'pipelines', 'getpipelines', 'sendpipelineaction', 'getpipelinesuggestions', 'getpipeline', 'deletepipeline', 'getpipelinefile', 'deletefailedpipelines', 'admindeletepipeline"
        )


def register_leanix_apptio_connector_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-apptio-connector"})
    async def leanix_leanix_apptio_connector(
        action: str = Field(
            description="Action to perform. Must be one of: 'getallconfigurations', 'upsertconfiguration', 'getconfigurations', 'deleteconfiguration', 'create', 'getresults', 'getresultsurl', 'getstats', 'getstatus', 'getwarnings'"
        ),
        config_id: str | None = Field(default=None, description="config id"),
        id_: str | None = Field(default=None, description="id "),
        client=Depends(get_apptio_connector_client),
    ) -> dict:
        """Manage leanix apptio connector operations.

        Actions:
          - 'getallconfigurations': Get all configurations
          - 'upsertconfiguration': Upsert a configuration
          - 'getconfigurations': Get configuration by id
          - 'deleteconfiguration': Delete a configuration
          - 'create': Create a new run
          - 'getresults': Get run results
          - 'getresultsurl': Get results_url of a run
          - 'getstats': Get stats of a run
          - 'getstatus': Get run status
          - 'getwarnings': Get warnings of a run
        """
        kwargs: dict[str, Any]
        if action == "getallconfigurations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getallconfigurations(**kwargs)
        if action == "upsertconfiguration":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.upsertconfiguration(**kwargs)
        if action == "getconfigurations":
            kwargs = {"config_id": config_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getconfigurations(**kwargs)
        if action == "deleteconfiguration":
            kwargs = {"config_id": config_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deleteconfiguration(**kwargs)
        if action == "create":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create(**kwargs)
        if action == "getresults":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getresults(**kwargs)
        if action == "getresultsurl":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getresultsurl(**kwargs)
        if action == "getstats":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getstats(**kwargs)
        if action == "getstatus":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getstatus(**kwargs)
        if action == "getwarnings":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getwarnings(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: getallconfigurations', 'upsertconfiguration', 'getconfigurations', 'deleteconfiguration', 'create', 'getresults', 'getresultsurl', 'getstats', 'getstatus', 'getwarnings"
        )


def register_leanix_automations_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-automations"})
    async def leanix_leanix_automations(
        action: str = Field(
            description="Action to perform. Must be one of: 'templatescontroller_getalltemplates', 'templatescontroller_createtemplate', 'templatescontroller_gettemplate', 'templatescontroller_updatetemplate', 'templatescontroller_patchtemplate', 'templatescontroller_deletetemplate', 'instancescontroller_findall', 'instancescontroller_quota', 'statisticscontroller_getstatistics', 'snapshotscontroller_managesnapshotrequests', 'snapshotscontroller_managedrestorationrequests', 'scriptscontroller_createmcescript', 'scriptscontroller_updatemcescript'"
        ),
        data: dict | None = Field(default=None, description="data"),
        id_: str | None = Field(default=None, description="id "),
        script_id: str | None = Field(default=None, description="script id"),
        client=Depends(get_automations_client),
    ) -> dict:
        """Manage leanix automations operations.

        Actions:
          - 'templatescontroller_getalltemplates': Call GET /templates
          - 'templatescontroller_createtemplate': Call POST /templates
          - 'templatescontroller_gettemplate': Call GET /templates/{id}
          - 'templatescontroller_updatetemplate': Call PUT /templates/{id_}
          - 'templatescontroller_patchtemplate': Call PATCH /templates/{id_}
          - 'templatescontroller_deletetemplate': Call DELETE /templates/{id_}
          - 'instancescontroller_findall': Call GET /instances
          - 'instancescontroller_quota': Call GET /instances/quota
          - 'statisticscontroller_getstatistics': Call GET /statistics
          - 'snapshotscontroller_managesnapshotrequests': Call POST /snapshots/managed_snapshot_requests
          - 'snapshotscontroller_managedrestorationrequests': Call POST /snapshots/managed_restoration_requests
          - 'scriptscontroller_createmcescript': Call POST /scripts
          - 'scriptscontroller_updatemcescript': Call PUT /scripts/{script_id}
        """
        kwargs: dict[str, Any]
        if action == "templatescontroller_getalltemplates":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.templatescontroller_getalltemplates(**kwargs)
        if action == "templatescontroller_createtemplate":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.templatescontroller_createtemplate(**kwargs)
        if action == "templatescontroller_gettemplate":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.templatescontroller_gettemplate(**kwargs)
        if action == "templatescontroller_updatetemplate":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.templatescontroller_updatetemplate(**kwargs)
        if action == "templatescontroller_patchtemplate":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.templatescontroller_patchtemplate(**kwargs)
        if action == "templatescontroller_deletetemplate":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.templatescontroller_deletetemplate(**kwargs)
        if action == "instancescontroller_findall":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.instancescontroller_findall(**kwargs)
        if action == "instancescontroller_quota":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.instancescontroller_quota(**kwargs)
        if action == "statisticscontroller_getstatistics":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.statisticscontroller_getstatistics(**kwargs)
        if action == "snapshotscontroller_managesnapshotrequests":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.snapshotscontroller_managesnapshotrequests(**kwargs)
        if action == "snapshotscontroller_managedrestorationrequests":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.snapshotscontroller_managedrestorationrequests(**kwargs)
        if action == "scriptscontroller_createmcescript":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.scriptscontroller_createmcescript(**kwargs)
        if action == "scriptscontroller_updatemcescript":
            kwargs = {"script_id": script_id, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.scriptscontroller_updatemcescript(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: templatescontroller_getalltemplates', 'templatescontroller_createtemplate', 'templatescontroller_gettemplate', 'templatescontroller_updatetemplate', 'templatescontroller_patchtemplate', 'templatescontroller_deletetemplate', 'instancescontroller_findall', 'instancescontroller_quota', 'statisticscontroller_getstatistics', 'snapshotscontroller_managesnapshotrequests', 'snapshotscontroller_managedrestorationrequests', 'scriptscontroller_createmcescript', 'scriptscontroller_updatemcescript"
        )


def register_leanix_reference_data_catalog_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-reference-data-catalog"})
    async def leanix_leanix_reference_data_catalog(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_recommendations', 'get_items', 'get_items_id', 'delete_links', 'post_links', 'post_requests', 'get_requests', 'post_requests_id_comments'"
        ),
        id_: str | None = Field(default=None, description="id "),
        data: dict | None = Field(default=None, description="data"),
        client=Depends(get_reference_data_catalog_client),
    ) -> dict:
        """Manage leanix reference data catalog operations.

        Actions:
          - 'get_recommendations': Get catalog recommendations.
          - 'get_items': Get catalog items.
          - 'get_items_id': Get catalog item by catalog id.
          - 'delete_links': Deletes a catalog link.
          - 'post_links': Creates a catalog link.
          - 'post_requests': Creates a request for a missing catalog item.
          - 'get_requests': Retrieves requests for missing catalog items.
          - 'post_requests_id_comments': Add a comment to a catalog request.
        """
        kwargs: dict[str, Any]
        if action == "get_recommendations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_recommendations(**kwargs)
        if action == "get_items":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_items(**kwargs)
        if action == "get_items_id":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_items_id(**kwargs)
        if action == "delete_links":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_links(**kwargs)
        if action == "post_links":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.post_links(**kwargs)
        if action == "post_requests":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.post_requests(**kwargs)
        if action == "get_requests":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_requests(**kwargs)
        if action == "post_requests_id_comments":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.post_requests_id_comments(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_recommendations', 'get_items', 'get_items_id', 'delete_links', 'post_links', 'post_requests', 'get_requests', 'post_requests_id_comments"
        )


def register_leanix_discovery_ai_agents_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-discovery-ai-agents"})
    async def leanix_leanix_discovery_ai_agents(
        action: str = Field(
            description="Action to perform. Must be one of: 'post_agents_a2a_cards', 'post_integrations', 'get_integrations', 'get_integrations_id', 'put_integrations_id_name', 'put_integrations_id_status', 'put_integrations_id_capabilities', 'put_integrations_id_credentials'"
        ),
        data: dict | None = Field(default=None, description="data"),
        id_: str | None = Field(default=None, description="id "),
        client=Depends(get_discovery_ai_agents_client),
    ) -> dict:
        """Manage leanix discovery ai agents operations.

        Actions:
          - 'post_agents_a2a_cards': Call POST /agents/a2a/cards
          - 'post_integrations': Call POST /integrations
          - 'get_integrations': Call GET /integrations
          - 'get_integrations_id': Call GET /integrations/{id}
          - 'put_integrations_id_name': Call PUT /integrations/{id}/name
          - 'put_integrations_id_status': Call PUT /integrations/{id}/status
          - 'put_integrations_id_capabilities': Call PUT /integrations/{id}/capabilities
          - 'put_integrations_id_credentials': Call PUT /integrations/{id}/credentials
        """
        kwargs: dict[str, Any]
        if action == "post_agents_a2a_cards":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.post_agents_a2a_cards(**kwargs)
        if action == "post_integrations":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.post_integrations(**kwargs)
        if action == "get_integrations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_integrations(**kwargs)
        if action == "get_integrations_id":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_integrations_id(**kwargs)
        if action == "put_integrations_id_name":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.put_integrations_id_name(**kwargs)
        if action == "put_integrations_id_status":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.put_integrations_id_status(**kwargs)
        if action == "put_integrations_id_capabilities":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.put_integrations_id_capabilities(**kwargs)
        if action == "put_integrations_id_credentials":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.put_integrations_id_credentials(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: post_agents_a2a_cards', 'post_integrations', 'get_integrations', 'get_integrations_id', 'put_integrations_id_name', 'put_integrations_id_status', 'put_integrations_id_capabilities', 'put_integrations_id_credentials"
        )


def register_leanix_discovery_linking_v1_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-discovery-linking-v1"})
    async def leanix_leanix_discovery_linking_v1(
        action: str = Field(
            description="Action to perform. Must be one of: 'link', 'bulk_link', 'discovery_itemsid', 'discovery_items', 'discovery_itemsidpre_validate_linkfactsheetid', 'discovery_itemsfilter_options', 'reject', 'discovery_itemslinking_progress', 'discovery_itemslinking_progressid', 'discovery_itemskpi_values', 'factsheetsiddetails'"
        ),
        data: dict | None = Field(default=None, description="data"),
        id_: str | None = Field(default=None, description="id "),
        fact_sheet_id: str | None = Field(default=None, description="fact sheet id"),
        client=Depends(get_discovery_linking_v1_client),
    ) -> dict:
        """Manage leanix discovery linking v1 operations.

        Actions:
          - 'link': Link a discovery item to a fact_sheet
          - 'bulk_link': Link multiple discovery items to fact_sheets
          - 'discovery_itemsid': Get a discovery item by ID
          - 'discovery_items': Get discovery items
          - 'discovery_itemsidpre_validate_linkfactsheetid': Pre-validate linking a discovery item to a fact_sheet
          - 'discovery_itemsfilter_options': Get filter options for discovery items
          - 'reject': Reject a linking suggestion
          - 'discovery_itemslinking_progress': Get Bulk linking progress for discovery items
          - 'discovery_itemslinking_progressid': Get linking progress for a discovery item
          - 'discovery_itemskpi_values': Get KPI values for discovery items
          - 'factsheetsiddetails': Get details of a fact_sheet
        """
        kwargs: dict[str, Any]
        if action == "link":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.link(**kwargs)
        if action == "bulk_link":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.bulk_link(**kwargs)
        if action == "discovery_itemsid":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.discovery_itemsid(**kwargs)
        if action == "discovery_items":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.discovery_items(**kwargs)
        if action == "discovery_itemsidpre_validate_linkfactsheetid":
            kwargs = {"id_": id_, "fact_sheet_id": fact_sheet_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.discovery_itemsidpre_validate_linkfactsheetid(**kwargs)
        if action == "discovery_itemsfilter_options":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.discovery_itemsfilter_options(**kwargs)
        if action == "reject":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.reject(**kwargs)
        if action == "discovery_itemslinking_progress":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.discovery_itemslinking_progress(**kwargs)
        if action == "discovery_itemslinking_progressid":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.discovery_itemslinking_progressid(**kwargs)
        if action == "discovery_itemskpi_values":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.discovery_itemskpi_values(**kwargs)
        if action == "factsheetsiddetails":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.factsheetsiddetails(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: link', 'bulk_link', 'discovery_itemsid', 'discovery_items', 'discovery_itemsidpre_validate_linkfactsheetid', 'discovery_itemsfilter_options', 'reject', 'discovery_itemslinking_progress', 'discovery_itemslinking_progressid', 'discovery_itemskpi_values', 'factsheetsiddetails"
        )


def register_leanix_discovery_linking_v2_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-discovery-linking-v2"})
    async def leanix_leanix_discovery_linking_v2(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_factsheets_id_links', 'get_origin_discoveryitems', 'get_origin_discoveryitems_export', 'put_origin_discoveryitems_link', 'get_origin_discoveryitems_linkingprogress', 'put_origin_discoveryitems_reject', 'get_origin_discoveryitems_sourceconfigs', 'get_origin_discoveryitems_id', 'get_origin_discoveryitems_id_changelogs', 'put_origin_discoveryitems_id_link', 'post_origin_discoveryitems_id_preview', 'get_origin_insights', 'get_origin_internal_events', 'get_origin_internal_events_compaction', 'post_origin_push', 'post_origin_push_id', 'get_origin_settings', 'get_origin_settings_autolinking', 'put_origin_settings_autolinking'"
        ),
        id_: str | None = Field(default=None, description="id "),
        origin: str | None = Field(default=None, description="origin"),
        data: dict | None = Field(default=None, description="data"),
        client=Depends(get_discovery_linking_v2_client),
    ) -> dict:
        """Manage leanix discovery linking v2 operations.

        Actions:
          - 'get_factsheets_id_links': Get discovery items linked to a fact sheet
          - 'get_origin_discoveryitems': Get discovery items with filtering, sorting and pagination
          - 'get_origin_discoveryitems_export': Export discovery items to CSV
          - 'put_origin_discoveryitems_link': Bulk link discovery items to fact sheets
          - 'get_origin_discoveryitems_linkingprogress': Get linking progress for a discovery item
          - 'put_origin_discoveryitems_reject': Reject discovery items
          - 'get_origin_discoveryitems_sourceconfigs': Get source configurations
          - 'get_origin_discoveryitems_id': Get discovery item by ID
          - 'get_origin_discoveryitems_id_changelogs': Get change logs for a discovery item
          - 'put_origin_discoveryitems_id_link': Link discovery item to fact sheets
          - 'post_origin_discoveryitems_id_preview': Get discovery item preview
          - 'get_origin_insights': Get insights for discovery inbox
          - 'get_origin_internal_events': Get ECST events
          - 'get_origin_internal_events_compaction': Load compaction events
          - 'post_origin_push': Initialize push to inbox
          - 'post_origin_push_id': Push discoveries to inbox
          - 'get_origin_settings': Get discovery inbox settings
          - 'get_origin_settings_autolinking': Get auto-linking configuration
          - 'put_origin_settings_autolinking': Update auto-linking configuration
        """
        kwargs: dict[str, Any]
        if action == "get_factsheets_id_links":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_factsheets_id_links(**kwargs)
        if action == "get_origin_discoveryitems":
            kwargs = {"origin": origin}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_origin_discoveryitems(**kwargs)
        if action == "get_origin_discoveryitems_export":
            kwargs = {"origin": origin}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_origin_discoveryitems_export(**kwargs)
        if action == "put_origin_discoveryitems_link":
            kwargs = {"origin": origin, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.put_origin_discoveryitems_link(**kwargs)
        if action == "get_origin_discoveryitems_linkingprogress":
            kwargs = {"origin": origin}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_origin_discoveryitems_linkingprogress(**kwargs)
        if action == "put_origin_discoveryitems_reject":
            kwargs = {"origin": origin, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.put_origin_discoveryitems_reject(**kwargs)
        if action == "get_origin_discoveryitems_sourceconfigs":
            kwargs = {"origin": origin}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_origin_discoveryitems_sourceconfigs(**kwargs)
        if action == "get_origin_discoveryitems_id":
            kwargs = {"origin": origin, "id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_origin_discoveryitems_id(**kwargs)
        if action == "get_origin_discoveryitems_id_changelogs":
            kwargs = {"origin": origin, "id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_origin_discoveryitems_id_changelogs(**kwargs)
        if action == "put_origin_discoveryitems_id_link":
            kwargs = {"origin": origin, "id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.put_origin_discoveryitems_id_link(**kwargs)
        if action == "post_origin_discoveryitems_id_preview":
            kwargs = {"origin": origin, "id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.post_origin_discoveryitems_id_preview(**kwargs)
        if action == "get_origin_insights":
            kwargs = {"origin": origin}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_origin_insights(**kwargs)
        if action == "get_origin_internal_events":
            kwargs = {"origin": origin}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_origin_internal_events(**kwargs)
        if action == "get_origin_internal_events_compaction":
            kwargs = {"origin": origin}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_origin_internal_events_compaction(**kwargs)
        if action == "post_origin_push":
            kwargs = {"origin": origin}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.post_origin_push(**kwargs)
        if action == "post_origin_push_id":
            kwargs = {"origin": origin, "id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.post_origin_push_id(**kwargs)
        if action == "get_origin_settings":
            kwargs = {"origin": origin}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_origin_settings(**kwargs)
        if action == "get_origin_settings_autolinking":
            kwargs = {"origin": origin}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_origin_settings_autolinking(**kwargs)
        if action == "put_origin_settings_autolinking":
            kwargs = {"origin": origin, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.put_origin_settings_autolinking(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_factsheets_id_links', 'get_origin_discoveryitems', 'get_origin_discoveryitems_export', 'put_origin_discoveryitems_link', 'get_origin_discoveryitems_linkingprogress', 'put_origin_discoveryitems_reject', 'get_origin_discoveryitems_sourceconfigs', 'get_origin_discoveryitems_id', 'get_origin_discoveryitems_id_changelogs', 'put_origin_discoveryitems_id_link', 'post_origin_discoveryitems_id_preview', 'get_origin_insights', 'get_origin_internal_events', 'get_origin_internal_events_compaction', 'post_origin_push', 'post_origin_push_id', 'get_origin_settings', 'get_origin_settings_autolinking', 'put_origin_settings_autolinking"
        )


def register_leanix_discovery_sap_extension_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-discovery-sap-extension"})
    async def leanix_leanix_discovery_sap_extension(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_cloud_foundry_domains', 'get_cloud_foundry_subject_pattern', 'put_integrations_id_credentials_cloud_foundry', 'post_cloud_foundry_infer_certificate_domain', 'get_credentials_type', 'post_credentials_verify_cms', 'get_health', 'post_integrations', 'get_integrations', 'put_integrations_id_credentials_cms', 'patch_integrations_id', 'delete_integrations_id_', 'post_integrations_credentials_verify', 'post_integrations_id_sync', 'get_kyma_spec_suggestions', 'post_kyma_verify_api_url', 'put_integrations_id_credentials_kyma', 'put_integrations_id_credentials_build', 'get_checkdatamodel', 'get_check_data_model'"
        ),
        id_: str | None = Field(default=None, description="id "),
        data: dict | None = Field(default=None, description="data"),
        type_: str | None = Field(default=None, description="type "),
        client=Depends(get_discovery_sap_extension_client),
    ) -> dict:
        """Manage leanix discovery sap extension operations.

        Actions:
          - 'get_cloud_foundry_domains': Call GET /cloud-foundry/domains
          - 'get_cloud_foundry_subject_pattern': Call GET /cloud-foundry/subject-pattern
          - 'put_integrations_id_credentials_cloud_foundry': Call PUT /integrations/{id}/credentials/cloud-foundry
          - 'post_cloud_foundry_infer_certificate_domain': Call POST /cloud-foundry/infer-certificate-domain
          - 'get_credentials_type': Call GET /credentials/{type}
          - 'post_credentials_verify_cms': Call POST /credentials/verify/cms
          - 'get_health': Call GET /health
          - 'post_integrations': Call POST /integrations
          - 'get_integrations': Call GET /integrations
          - 'put_integrations_id_credentials_cms': Call PUT /integrations/{id}/credentials/cms
          - 'patch_integrations_id': Call PATCH /integrations/{id}
          - 'delete_integrations_id_': Call DELETE /integrations/{id_}
          - 'post_integrations_credentials_verify': Call POST /integrations/credentials/verify
          - 'post_integrations_id_sync': Call POST /integrations/{id}/sync
          - 'get_kyma_spec_suggestions': Call GET /kyma/spec-suggestions
          - 'post_kyma_verify_api_url': Call POST /kyma/verify-api-url
          - 'put_integrations_id_credentials_kyma': Call PUT /integrations/{id}/credentials/kyma
          - 'put_integrations_id_credentials_build': Call PUT /integrations/{id}/credentials/build
          - 'get_checkdatamodel': Call GET /check_data_model
          - 'get_check_data_model': Call GET /check-data-model
        """
        kwargs: dict[str, Any]
        if action == "get_cloud_foundry_domains":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_cloud_foundry_domains(**kwargs)
        if action == "get_cloud_foundry_subject_pattern":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_cloud_foundry_subject_pattern(**kwargs)
        if action == "put_integrations_id_credentials_cloud_foundry":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.put_integrations_id_credentials_cloud_foundry(**kwargs)
        if action == "post_cloud_foundry_infer_certificate_domain":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.post_cloud_foundry_infer_certificate_domain(**kwargs)
        if action == "get_credentials_type":
            kwargs = {"type_": type_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_credentials_type(**kwargs)
        if action == "post_credentials_verify_cms":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.post_credentials_verify_cms(**kwargs)
        if action == "get_health":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_health(**kwargs)
        if action == "post_integrations":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.post_integrations(**kwargs)
        if action == "get_integrations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_integrations(**kwargs)
        if action == "put_integrations_id_credentials_cms":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.put_integrations_id_credentials_cms(**kwargs)
        if action == "patch_integrations_id":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.patch_integrations_id(**kwargs)
        if action == "delete_integrations_id_":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_integrations_id_(**kwargs)
        if action == "post_integrations_credentials_verify":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.post_integrations_credentials_verify(**kwargs)
        if action == "post_integrations_id_sync":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.post_integrations_id_sync(**kwargs)
        if action == "get_kyma_spec_suggestions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_kyma_spec_suggestions(**kwargs)
        if action == "post_kyma_verify_api_url":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.post_kyma_verify_api_url(**kwargs)
        if action == "put_integrations_id_credentials_kyma":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.put_integrations_id_credentials_kyma(**kwargs)
        if action == "put_integrations_id_credentials_build":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.put_integrations_id_credentials_build(**kwargs)
        if action == "get_checkdatamodel":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_checkdatamodel(**kwargs)
        if action == "get_check_data_model":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_check_data_model(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_cloud_foundry_domains', 'get_cloud_foundry_subject_pattern', 'put_integrations_id_credentials_cloud_foundry', 'post_cloud_foundry_infer_certificate_domain', 'get_credentials_type', 'post_credentials_verify_cms', 'get_health', 'post_integrations', 'get_integrations', 'put_integrations_id_credentials_cms', 'patch_integrations_id', 'delete_integrations_id_', 'post_integrations_credentials_verify', 'post_integrations_id_sync', 'get_kyma_spec_suggestions', 'post_kyma_verify_api_url', 'put_integrations_id_credentials_kyma', 'put_integrations_id_credentials_build', 'get_checkdatamodel', 'get_check_data_model"
        )


def register_leanix_discovery_saas_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-discovery-saas"})
    async def leanix_leanix_discovery_saas(
        action: str = Field(
            description="Action to perform. Must be one of: 'getavailableintegrations', 'postintegration', 'getintegrations', 'getintegrationbyid', 'deleteintegrationbyid', 'putintegrationnamebyid', 'putintegrationcapabilitiesbyid', 'putintegrationcredentialsbyid', 'putintegrationstatusbyid', 'getdiscoveries', 'getdiscoveryprioritybyid'"
        ),
        data: dict | None = Field(default=None, description="data"),
        id_: str | None = Field(default=None, description="id "),
        client=Depends(get_discovery_saas_client),
    ) -> dict:
        """Manage leanix discovery saas operations.

        Actions:
          - 'getavailableintegrations': Get list of available integrations for the workspace.
          - 'postintegration': Connect a new integration.
          - 'getintegrations': Get list of integrations in the workspace.
          - 'getintegrationbyid': Get integration details by ID.
          - 'deleteintegrationbyid': Delete integration by ID. Only integrations in 'duplicate' status can be deleted.
          - 'putintegrationnamebyid': Update name of the integration.
          - 'putintegrationcapabilitiesbyid': Update capabilities of the integration.
          - 'putintegrationcredentialsbyid': Update credentials of the integration.
          - 'putintegrationstatusbyid': Update status of the integration.
          - 'getdiscoveries': Get list of discoveries.
          - 'getdiscoveryprioritybyid': Get discovery priority by ID.
        """
        kwargs: dict[str, Any]
        if action == "getavailableintegrations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getavailableintegrations(**kwargs)
        if action == "postintegration":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.postintegration(**kwargs)
        if action == "getintegrations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getintegrations(**kwargs)
        if action == "getintegrationbyid":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getintegrationbyid(**kwargs)
        if action == "deleteintegrationbyid":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deleteintegrationbyid(**kwargs)
        if action == "putintegrationnamebyid":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.putintegrationnamebyid(**kwargs)
        if action == "putintegrationcapabilitiesbyid":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.putintegrationcapabilitiesbyid(**kwargs)
        if action == "putintegrationcredentialsbyid":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.putintegrationcredentialsbyid(**kwargs)
        if action == "putintegrationstatusbyid":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.putintegrationstatusbyid(**kwargs)
        if action == "getdiscoveries":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getdiscoveries(**kwargs)
        if action == "getdiscoveryprioritybyid":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getdiscoveryprioritybyid(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: getavailableintegrations', 'postintegration', 'getintegrations', 'getintegrationbyid', 'deleteintegrationbyid', 'putintegrationnamebyid', 'putintegrationcapabilitiesbyid', 'putintegrationcredentialsbyid', 'putintegrationstatusbyid', 'getdiscoveries', 'getdiscoveryprioritybyid"
        )


def register_leanix_documents_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-documents"})
    async def leanix_leanix_documents(
        action: str = Field(
            description="Action to perform. Must be one of: 'gettemplatecomponents', 'updatecomponents', 'createtemplatecomponents', 'gettemplatebyid', 'updatetemplate', 'deletetemplate', 'getdocumentbyid', 'updatedocument', 'deletedocumentbyid', 'getdocumentcomponents', 'updatedocumentcomponents', 'gettemplatespaginated', 'createtemplates', 'getdocumentspaginated', 'createdocuments', 'getdocumentscount', 'deletetemplatecomponent'"
        ),
        template_id: str | None = Field(default=None, description="template id"),
        data: dict | None = Field(default=None, description="data"),
        id_: str | None = Field(default=None, description="id "),
        document_id: str | None = Field(default=None, description="document id"),
        client=Depends(get_documents_client),
    ) -> dict:
        """Manage leanix documents operations.

        Actions:
          - 'gettemplatecomponents': Retrieve Components of a Template
          - 'updatecomponents': Update (multiple) template components of a template
          - 'createtemplatecomponents': Create (multiple) templates components
          - 'gettemplatebyid': Retrieve a specific template
          - 'updatetemplate': Update a template
          - 'deletetemplate': Delete a template
          - 'getdocumentbyid': Retrieve a specific document
          - 'updatedocument': Update a document
          - 'deletedocumentbyid': Delete a specific document
          - 'getdocumentcomponents': Retrieve components of a document
          - 'updatedocumentcomponents': Update (multiple) components of a document
          - 'gettemplatespaginated': Query for templates
          - 'createtemplates': Create (multiple) templates
          - 'getdocumentspaginated': Query for documents
          - 'createdocuments': Create (multiple) documents
          - 'getdocumentscount': Count of matching documents
          - 'deletetemplatecomponent': Delete a template component from a template
        """
        kwargs: dict[str, Any]
        if action == "gettemplatecomponents":
            kwargs = {"template_id": template_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.gettemplatecomponents(**kwargs)
        if action == "updatecomponents":
            kwargs = {"template_id": template_id, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updatecomponents(**kwargs)
        if action == "createtemplatecomponents":
            kwargs = {"template_id": template_id, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createtemplatecomponents(**kwargs)
        if action == "gettemplatebyid":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.gettemplatebyid(**kwargs)
        if action == "updatetemplate":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updatetemplate(**kwargs)
        if action == "deletetemplate":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletetemplate(**kwargs)
        if action == "getdocumentbyid":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getdocumentbyid(**kwargs)
        if action == "updatedocument":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updatedocument(**kwargs)
        if action == "deletedocumentbyid":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletedocumentbyid(**kwargs)
        if action == "getdocumentcomponents":
            kwargs = {"document_id": document_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getdocumentcomponents(**kwargs)
        if action == "updatedocumentcomponents":
            kwargs = {"document_id": document_id, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updatedocumentcomponents(**kwargs)
        if action == "gettemplatespaginated":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.gettemplatespaginated(**kwargs)
        if action == "createtemplates":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createtemplates(**kwargs)
        if action == "getdocumentspaginated":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getdocumentspaginated(**kwargs)
        if action == "createdocuments":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createdocuments(**kwargs)
        if action == "getdocumentscount":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getdocumentscount(**kwargs)
        if action == "deletetemplatecomponent":
            kwargs = {"id_": id_, "template_id": template_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletetemplatecomponent(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: gettemplatecomponents', 'updatecomponents', 'createtemplatecomponents', 'gettemplatebyid', 'updatetemplate', 'deletetemplate', 'getdocumentbyid', 'updatedocument', 'deletedocumentbyid', 'getdocumentcomponents', 'updatedocumentcomponents', 'gettemplatespaginated', 'createtemplates', 'getdocumentspaginated', 'createdocuments', 'getdocumentscount', 'deletetemplatecomponent"
        )


def register_leanix_impacts_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-impacts"})
    async def leanix_leanix_impacts(
        action: str = Field(
            description="Action to perform. Must be one of: 'get', 'update', 'compute', 'getprojection', 'getsinglefactsheetprojection'"
        ),
        data: dict | None = Field(default=None, description="data"),
        client=Depends(get_impacts_client),
    ) -> dict:
        """Manage leanix impacts operations.

        Actions:
          - 'get': Fetch configuration
          - 'update': Update configuration
          - 'compute': Call POST /obsolescence_reasons
          - 'getprojection': Calculate impact projection
          - 'getsinglefactsheetprojection': Calculate impact projection for a single Fact Sheet
        """
        kwargs: dict[str, Any]
        if action == "get":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get(**kwargs)
        if action == "update":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update(**kwargs)
        if action == "compute":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.compute(**kwargs)
        if action == "getprojection":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getprojection(**kwargs)
        if action == "getsinglefactsheetprojection":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsinglefactsheetprojection(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get', 'update', 'compute', 'getprojection', 'getsinglefactsheetprojection"
        )


def register_leanix_integration_api_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-integration-api"})
    async def leanix_leanix_integration_api(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_examples_starterexample', 'get_examples_advancedexample', 'getprocessorconfigurations', 'upsertprocessorconfiguration', 'deleteprocessorconfiguration', 'getsynchronizationrunsstatuslist', 'createsynchronizationrun', 'startsynchronizationrun', 'getsynchronizationrunprogress', 'stopsynchronizationrun', 'getsynchronizationrunstatus', 'getsynchronizationrunstats', 'getsynchronizationrunresults', 'getsynchronizationrunresultsurl', 'getsynchronizationrunwarnings', 'createsynchronizationrunwithconfig', 'createsynchronizationrunwithurlinput', 'createsynchronizationrunwithexecutiongroupandurlinput', 'createsynchronizationrunwithexecutiongroup', 'getsynchronizationrundebuginformation', 'getsynchronizationrundebugvariables', 'createsynchronizationfastrun', 'createsynchronizationfastrunwithconfig', 'createinazure'"
        ),
        id_: str | None = Field(default=None, description="id "),
        client=Depends(get_integration_api_client),
    ) -> dict:
        """Manage leanix integration api operations.

        Actions:
          - 'get_examples_starterexample': Returns a starter example including an Input object and processor configuration
          - 'get_examples_advancedexample': Returns an advanced example including an Input object and processor configuration
          - 'getprocessorconfigurations': Returns a list of available processor configurations
          - 'upsertprocessorconfiguration': Inserts a new processor configuration or updates an existing one
          - 'deleteprocessorconfiguration': Delete a single processor configuration
          - 'getsynchronizationrunsstatuslist': Returns the status of all existing synchronization runs
          - 'createsynchronizationrun': Creates a synchronization run.
          - 'startsynchronizationrun': Starts an existing but not yet started synchronization run
          - 'getsynchronizationrunprogress': Shows the progress of a synchronization run, it gives updated counters of the run level that is in execution.
          - 'stopsynchronizationrun': Stops a running synchronization run
          - 'getsynchronizationrunstatus': Returns the status of an existing synchronization run
          - 'getsynchronizationrunstats': Returns detailed statistics about the execution of a synchronization run
          - 'getsynchronizationrunresults': Returns the results of a finished synchronization run
          - 'getsynchronizationrunresultsurl': Returns the url to the results of a finished synchronization run
          - 'getsynchronizationrunwarnings': Returns the warnings of a synchronization run
          - 'createsynchronizationrunwithconfig': Starts a new synchronization run using the processor configuration and input object provided in the request. >__Please do not use this endpoint for production use cases. It was built for testing configurations only.__
          - 'createsynchronizationrunwithurlinput': Starts a new synchronization run using a DataProvider information to obtain the LDIF input
          - 'createsynchronizationrunwithexecutiongroupandurlinput': Starts a new synchronization run using a DataProvider information to obtain the LDIF input, but choose a configuration based on execution group.
          - 'createsynchronizationrunwithexecutiongroup': Starts a new synchronization run using combined processor configuration within an execution group and input object provided in the request.
          - 'getsynchronizationrundebuginformation': Provides the Debug logs generated during the synchronization runs.
          - 'getsynchronizationrundebugvariables': Provides the Debug variables generated during the synchronization runs.
          - 'createsynchronizationfastrun': Creates a fast synchronization run.
          - 'createsynchronizationfastrunwithconfig': Starts a new fast run synchronization using the processor configuration and input object provided in the request. >__Please do not use this endpoint for production use cases. It was built for testing configurations only.__
          - 'createinazure': Provides storage resources that can be used for synchronisation runs. It creates a blob file in Azure Storage.
        """
        kwargs: dict[str, Any]
        if action == "get_examples_starterexample":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_examples_starterexample(**kwargs)
        if action == "get_examples_advancedexample":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_examples_advancedexample(**kwargs)
        if action == "getprocessorconfigurations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getprocessorconfigurations(**kwargs)
        if action == "upsertprocessorconfiguration":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.upsertprocessorconfiguration(**kwargs)
        if action == "deleteprocessorconfiguration":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deleteprocessorconfiguration(**kwargs)
        if action == "getsynchronizationrunsstatuslist":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsynchronizationrunsstatuslist(**kwargs)
        if action == "createsynchronizationrun":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createsynchronizationrun(**kwargs)
        if action == "startsynchronizationrun":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.startsynchronizationrun(**kwargs)
        if action == "getsynchronizationrunprogress":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsynchronizationrunprogress(**kwargs)
        if action == "stopsynchronizationrun":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.stopsynchronizationrun(**kwargs)
        if action == "getsynchronizationrunstatus":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsynchronizationrunstatus(**kwargs)
        if action == "getsynchronizationrunstats":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsynchronizationrunstats(**kwargs)
        if action == "getsynchronizationrunresults":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsynchronizationrunresults(**kwargs)
        if action == "getsynchronizationrunresultsurl":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsynchronizationrunresultsurl(**kwargs)
        if action == "getsynchronizationrunwarnings":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsynchronizationrunwarnings(**kwargs)
        if action == "createsynchronizationrunwithconfig":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createsynchronizationrunwithconfig(**kwargs)
        if action == "createsynchronizationrunwithurlinput":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createsynchronizationrunwithurlinput(**kwargs)
        if action == "createsynchronizationrunwithexecutiongroupandurlinput":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createsynchronizationrunwithexecutiongroupandurlinput(
                **kwargs
            )
        if action == "createsynchronizationrunwithexecutiongroup":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createsynchronizationrunwithexecutiongroup(**kwargs)
        if action == "getsynchronizationrundebuginformation":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsynchronizationrundebuginformation(**kwargs)
        if action == "getsynchronizationrundebugvariables":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsynchronizationrundebugvariables(**kwargs)
        if action == "createsynchronizationfastrun":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createsynchronizationfastrun(**kwargs)
        if action == "createsynchronizationfastrunwithconfig":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createsynchronizationfastrunwithconfig(**kwargs)
        if action == "createinazure":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createinazure(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_examples_starterexample', 'get_examples_advancedexample', 'getprocessorconfigurations', 'upsertprocessorconfiguration', 'deleteprocessorconfiguration', 'getsynchronizationrunsstatuslist', 'createsynchronizationrun', 'startsynchronizationrun', 'getsynchronizationrunprogress', 'stopsynchronizationrun', 'getsynchronizationrunstatus', 'getsynchronizationrunstats', 'getsynchronizationrunresults', 'getsynchronizationrunresultsurl', 'getsynchronizationrunwarnings', 'createsynchronizationrunwithconfig', 'createsynchronizationrunwithurlinput', 'createsynchronizationrunwithexecutiongroupandurlinput', 'createsynchronizationrunwithexecutiongroup', 'getsynchronizationrundebuginformation', 'getsynchronizationrundebugvariables', 'createsynchronizationfastrun', 'createsynchronizationfastrunwithconfig', 'createinazure"
        )


def register_leanix_integration_collibra_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-integration-collibra"})
    async def leanix_leanix_integration_collibra(
        action: str = Field(
            description="Action to perform. Must be one of: 'createsynchronizationrun', 'getconfigurations', 'createconfiguration', 'getconfigurationbyid', 'updateconfiguration', 'deleteconfiguration', 'getoverview', 'getstatus', 'getfeaturetoggles', 'getfields', 'getrelationfields', 'getrelations', 'getsubscriptionroles', 'getcredentials', 'createcollibracredentials', 'getcollibracredentialsbyid', 'updatecollibracredentials', 'validatecollibracredentialsbyid', 'getattributetypesforassettype', 'getattributetypesforassettypebyscope', 'getassetstatuses', 'getassettypes', 'getattributetypes', 'getcommunities', 'getcomplexrelationtypes', 'getdomains', 'getrelationtypes', 'getresourceroles', 'getresponsibilityroles'"
        ),
        data: dict | None = Field(default=None, description="data"),
        id_: str | None = Field(default=None, description="id "),
        relation_name: str | None = Field(default=None, description="relation name"),
        asset_type_id: str | None = Field(default=None, description="asset type id"),
        client=Depends(get_integration_collibra_client),
    ) -> dict:
        """Manage leanix integration collibra operations.

        Actions:
          - 'createsynchronizationrun': Creates synchronization run for current EAM workspace.
          - 'getconfigurations': Returns a list of available configurations for current EAM workspace.
          - 'createconfiguration': Creates configuration for current EAM workspace.
          - 'getconfigurationbyid': Retrieves configuration for current EAM workspace by id.
          - 'updateconfiguration': Updates an existing configuration for current EAM workspace by id.
          - 'deleteconfiguration': Deletes an existing configuration for current EAM workspace by id.
          - 'getoverview': Returns overview of configuration for current workspace.
          - 'getstatus': Returns status of configurations for current EAM workspace.
          - 'getfeaturetoggles': Returns list of available feature toggles for current EAM workspace.
          - 'getfields': Returns list of available fields for a given Fact Sheet type.
          - 'getrelationfields': Returns list of available fields for the given relation.
          - 'getrelations': Returns list of available relations for a given Fact Sheet type.
          - 'getsubscriptionroles': Returns list of available subscription roles for a given Fact Sheet type.
          - 'getcredentials': Returns a list of available credentials for current EAM workspace.
          - 'createcollibracredentials': Creates collibra credentials for given EAM Workspace.
          - 'getcollibracredentialsbyid': Retrieves credentials for current EAM workspace by id.
          - 'updatecollibracredentials': Updates existing collibra credentials for given EAM Workspace by id.
          - 'validatecollibracredentialsbyid': Validates the given credentials id with Collibra
          - 'getattributetypesforassettype': Returns list of available collibra attribute types for the supplied asset type.
          - 'getattributetypesforassettypebyscope': Returns list of available collibra attribute types for the supplied asset type (grouped by Scope).
          - 'getassetstatuses': Returns list of available collibra asset statuses.
          - 'getassettypes': Returns list of available collibra asset types.
          - 'getattributetypes': Returns list of available collibra attribute types.
          - 'getcommunities': Returns list of available collibra communities.
          - 'getcomplexrelationtypes': Returns list of available complex relations.
          - 'getdomains': Returns list of available collibra domains.
          - 'getrelationtypes': Returns list of available simple relation types for the supplied from and to asset type ids including hierarchy.
          - 'getresourceroles': Returns list of available collibra resource_roles.
          - 'getresponsibilityroles': Returns list of available collibra responsibility_roles.
        """
        kwargs: dict[str, Any]
        if action == "createsynchronizationrun":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createsynchronizationrun(**kwargs)
        if action == "getconfigurations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getconfigurations(**kwargs)
        if action == "createconfiguration":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createconfiguration(**kwargs)
        if action == "getconfigurationbyid":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getconfigurationbyid(**kwargs)
        if action == "updateconfiguration":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updateconfiguration(**kwargs)
        if action == "deleteconfiguration":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deleteconfiguration(**kwargs)
        if action == "getoverview":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getoverview(**kwargs)
        if action == "getstatus":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getstatus(**kwargs)
        if action == "getfeaturetoggles":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getfeaturetoggles(**kwargs)
        if action == "getfields":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getfields(**kwargs)
        if action == "getrelationfields":
            kwargs = {"relation_name": relation_name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getrelationfields(**kwargs)
        if action == "getrelations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getrelations(**kwargs)
        if action == "getsubscriptionroles":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsubscriptionroles(**kwargs)
        if action == "getcredentials":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getcredentials(**kwargs)
        if action == "createcollibracredentials":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createcollibracredentials(**kwargs)
        if action == "getcollibracredentialsbyid":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getcollibracredentialsbyid(**kwargs)
        if action == "updatecollibracredentials":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updatecollibracredentials(**kwargs)
        if action == "validatecollibracredentialsbyid":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.validatecollibracredentialsbyid(**kwargs)
        if action == "getattributetypesforassettype":
            kwargs = {"asset_type_id": asset_type_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getattributetypesforassettype(**kwargs)
        if action == "getattributetypesforassettypebyscope":
            kwargs = {"asset_type_id": asset_type_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getattributetypesforassettypebyscope(**kwargs)
        if action == "getassetstatuses":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getassetstatuses(**kwargs)
        if action == "getassettypes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getassettypes(**kwargs)
        if action == "getattributetypes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getattributetypes(**kwargs)
        if action == "getcommunities":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getcommunities(**kwargs)
        if action == "getcomplexrelationtypes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getcomplexrelationtypes(**kwargs)
        if action == "getdomains":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getdomains(**kwargs)
        if action == "getrelationtypes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getrelationtypes(**kwargs)
        if action == "getresourceroles":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getresourceroles(**kwargs)
        if action == "getresponsibilityroles":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getresponsibilityroles(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: createsynchronizationrun', 'getconfigurations', 'createconfiguration', 'getconfigurationbyid', 'updateconfiguration', 'deleteconfiguration', 'getoverview', 'getstatus', 'getfeaturetoggles', 'getfields', 'getrelationfields', 'getrelations', 'getsubscriptionroles', 'getcredentials', 'createcollibracredentials', 'getcollibracredentialsbyid', 'updatecollibracredentials', 'validatecollibracredentialsbyid', 'getattributetypesforassettype', 'getattributetypesforassettypebyscope', 'getassetstatuses', 'getassettypes', 'getattributetypes', 'getcommunities', 'getcomplexrelationtypes', 'getdomains', 'getrelationtypes', 'getresourceroles', 'getresponsibilityroles"
        )


def register_leanix_integration_servicenow_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-integration-servicenow"})
    async def leanix_leanix_integration_servicenow(
        action: str = Field(
            description="Action to perform. Must be one of: 'getaggregatedfactsheetsummary', 'getaggregatedsoftwareinformation', 'getservicenowaggregatedsoftware', 'getfilterforfactsheet', 'getfilterforprovider', 'getfiltersforhardware', 'getservicenowaggregatedhardware', 'getstatusoverview', 'getallconfigurations', 'createconfiguration', 'getconfiguration', 'updateconfiguration', 'deleteconfiguration', 'synchronize', 'validateconfiguration', 'validateservicenowcredentials', 'getfilters', 'getservicenowsyncconstraintrules', 'getavailablerelcirelations', 'getinstalledservicenowpluginversion', 'getmappingtablerelations', 'getreferencefieldrelations', 'getservicenowmetadata', 'gettables', 'changes', 'hooks', 'sendprompt', 'sendpromptv2', 'abortallpendingandrunningsynchronizations', 'abortsynchronization', 'getcurrentlyrunningorlastcreatedrun', 'getversionbyid', 'getversions'"
        ),
        fact_sheet_id: str | None = Field(default=None, description="fact sheet id"),
        configuration_id: str | None = Field(
            default=None, description="configuration id"
        ),
        software_id: str | None = Field(default=None, description="software id"),
        data: dict | None = Field(default=None, description="data"),
        id_: str | None = Field(default=None, description="id "),
        run_id: str | None = Field(default=None, description="run id"),
        version_id: str | None = Field(default=None, description="version id"),
        client=Depends(get_integration_servicenow_client),
    ) -> dict:
        """Manage leanix integration servicenow operations.

        Actions:
          - 'getaggregatedfactsheetsummary': (INTERNAL) Provide summary integration information for a linked fact sheet
          - 'getaggregatedsoftwareinformation': (INTERNAL) Provide information of detected aggregated software
          - 'getservicenowaggregatedsoftware': (INTERNAL) Retrieve software installations found for a given fact sheet
          - 'getfilterforfactsheet': (INTERNAL) Retrieve all fact sheet filter options found for a given configuration
          - 'getfilterforprovider': (INTERNAL) Retrieve all providers filter options found for a given configuration
          - 'getfiltersforhardware': (INTERNAL) Retrieve all hardware filter options where aggregated software is installed for a given configuration
          - 'getservicenowaggregatedhardware': (INTERNAL) Retrieve hardware information for a given software installation
          - 'getstatusoverview': (INTERNAL) Provide statistics for A&L
          - 'getallconfigurations': (INTERNAL) Retrieve all ServiceNow configurations
          - 'createconfiguration': (INTERNAL) Create a new ServiceNow configuration
          - 'getconfiguration': (INTERNAL) Retrieve a ServiceNow configuration
          - 'updateconfiguration': (INTERNAL) Update a ServiceNow configuration
          - 'deleteconfiguration': (INTERNAL) Delete a ServiceNow configuration
          - 'synchronize': (INTERNAL) Submit a synchronization job to be enqueued for execution
          - 'validateconfiguration': (INTERNAL) Validate the uploaded ServiceNow configuration and provide list of issues
          - 'validateservicenowcredentials': (INTERNAL) Validate the credentials from an existing ServiceNow configuration
          - 'getfilters': (INTERNAL) Retrieve all assigned ServiceNow filters for a given table
          - 'getservicenowsyncconstraintrules': (INTERNAL) Retrieve all constraint rules for a given ServiceNow table
          - 'getavailablerelcirelations': (INTERNAL) Retrieve all possible ServiceNow CMDB_REL_CI relations between two tables
          - 'getinstalledservicenowpluginversion': (INTERNAL) Retrieve the installed ServiceNow plugin version
          - 'getmappingtablerelations': (INTERNAL) Retrieve all available ServiceNow MAPPING_TABLE relations for a given table
          - 'getreferencefieldrelations': (INTERNAL) Retrieve all available reference fields between two ServiceNow tables
          - 'getservicenowmetadata': (INTERNAL) Retrieve metadata of for a ServiceNow table
          - 'gettables': (INTERNAL) Retrieve all available ServiceNow table names in ServiceNow
          - 'changes': (INTERNAL) Consume ServiceNow events for changes on the ServiceNow side
          - 'hooks': (INTERNAL) Consume LeanIX events for changes on the LeanIX side
          - 'sendprompt': (INTERNAL) Retrieve an AI generated field mapping for a FactSheet type
          - 'sendpromptv2': (INTERNAL) (V2) Retrieve an AI generated field mapping for a FactSheet type
          - 'abortallpendingandrunningsynchronizations': (INTERNAL) Trigger the abortion of all the running and pending synchronizations for a configuration
          - 'abortsynchronization': (INTERNAL) Trigger the abortion of a specific synchronization run
          - 'getcurrentlyrunningorlastcreatedrun': (INTERNAL) Retrieve information about the current running synchronization for a given configuration or otherwise the one created most recently
          - 'getversionbyid': (INTERNAL) Retrieve one specific ServiceNow configuration-version by Id
          - 'getversions': (INTERNAL) Retrieve all ServiceNow configuration-versions
        """
        kwargs: dict[str, Any]
        if action == "getaggregatedfactsheetsummary":
            kwargs = {"fact_sheet_id": fact_sheet_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getaggregatedfactsheetsummary(**kwargs)
        if action == "getaggregatedsoftwareinformation":
            kwargs = {"configuration_id": configuration_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getaggregatedsoftwareinformation(**kwargs)
        if action == "getservicenowaggregatedsoftware":
            kwargs = {"fact_sheet_id": fact_sheet_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getservicenowaggregatedsoftware(**kwargs)
        if action == "getfilterforfactsheet":
            kwargs = {"configuration_id": configuration_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getfilterforfactsheet(**kwargs)
        if action == "getfilterforprovider":
            kwargs = {"configuration_id": configuration_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getfilterforprovider(**kwargs)
        if action == "getfiltersforhardware":
            kwargs = {"configuration_id": configuration_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getfiltersforhardware(**kwargs)
        if action == "getservicenowaggregatedhardware":
            kwargs = {
                "fact_sheet_id": fact_sheet_id,
                "software_id": software_id,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getservicenowaggregatedhardware(**kwargs)
        if action == "getstatusoverview":
            kwargs = {"configuration_id": configuration_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getstatusoverview(**kwargs)
        if action == "getallconfigurations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getallconfigurations(**kwargs)
        if action == "createconfiguration":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createconfiguration(**kwargs)
        if action == "getconfiguration":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getconfiguration(**kwargs)
        if action == "updateconfiguration":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updateconfiguration(**kwargs)
        if action == "deleteconfiguration":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deleteconfiguration(**kwargs)
        if action == "synchronize":
            kwargs = {
                "configuration_id": configuration_id,
                "data": data,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.synchronize(**kwargs)
        if action == "validateconfiguration":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.validateconfiguration(**kwargs)
        if action == "validateservicenowcredentials":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.validateservicenowcredentials(**kwargs)
        if action == "getfilters":
            kwargs = {"configuration_id": configuration_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getfilters(**kwargs)
        if action == "getservicenowsyncconstraintrules":
            kwargs = {"configuration_id": configuration_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getservicenowsyncconstraintrules(**kwargs)
        if action == "getavailablerelcirelations":
            kwargs = {"configuration_id": configuration_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getavailablerelcirelations(**kwargs)
        if action == "getinstalledservicenowpluginversion":
            kwargs = {"configuration_id": configuration_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getinstalledservicenowpluginversion(**kwargs)
        if action == "getmappingtablerelations":
            kwargs = {"configuration_id": configuration_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getmappingtablerelations(**kwargs)
        if action == "getreferencefieldrelations":
            kwargs = {"configuration_id": configuration_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getreferencefieldrelations(**kwargs)
        if action == "getservicenowmetadata":
            kwargs = {"configuration_id": configuration_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getservicenowmetadata(**kwargs)
        if action == "gettables":
            kwargs = {"configuration_id": configuration_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.gettables(**kwargs)
        if action == "changes":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.changes(**kwargs)
        if action == "hooks":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.hooks(**kwargs)
        if action == "sendprompt":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.sendprompt(**kwargs)
        if action == "sendpromptv2":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.sendpromptv2(**kwargs)
        if action == "abortallpendingandrunningsynchronizations":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.abortallpendingandrunningsynchronizations(**kwargs)
        if action == "abortsynchronization":
            kwargs = {"run_id": run_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.abortsynchronization(**kwargs)
        if action == "getcurrentlyrunningorlastcreatedrun":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getcurrentlyrunningorlastcreatedrun(**kwargs)
        if action == "getversionbyid":
            kwargs = {"version_id": version_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getversionbyid(**kwargs)
        if action == "getversions":
            kwargs = {"configuration_id": configuration_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getversions(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: getaggregatedfactsheetsummary', 'getaggregatedsoftwareinformation', 'getservicenowaggregatedsoftware', 'getfilterforfactsheet', 'getfilterforprovider', 'getfiltersforhardware', 'getservicenowaggregatedhardware', 'getstatusoverview', 'getallconfigurations', 'createconfiguration', 'getconfiguration', 'updateconfiguration', 'deleteconfiguration', 'synchronize', 'validateconfiguration', 'validateservicenowcredentials', 'getfilters', 'getservicenowsyncconstraintrules', 'getavailablerelcirelations', 'getinstalledservicenowpluginversion', 'getmappingtablerelations', 'getreferencefieldrelations', 'getservicenowmetadata', 'gettables', 'changes', 'hooks', 'sendprompt', 'sendpromptv2', 'abortallpendingandrunningsynchronizations', 'abortsynchronization', 'getcurrentlyrunningorlastcreatedrun', 'getversionbyid', 'getversions"
        )


def register_leanix_integration_signavio_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-integration-signavio"})
    async def leanix_leanix_integration_signavio(
        action: str = Field(
            description="Action to perform. Must be one of: 'getconfigurations', 'createconfiguration', 'getconfiguration', 'updateconfiguration', 'deleteconfiguration', 'synchronizeconfiguration', 'unassignformation', 'getformations', 'getdirectories', 'createcategory', 'getfactsheetfields', 'getlabels', 'getsignavioglossaryitemfields', 'getsignavioprocessfields', 'getprocessfields', 'analyzelatestsynchronizationrun', 'analyzesynchronizationrun', 'cancelsynchronization', 'getlatestsynchronizationrunanalysis', 'getsynchronizationrunanalysis'"
        ),
        data: dict | None = Field(default=None, description="data"),
        id_: str | None = Field(default=None, description="id "),
        run_id: str | None = Field(default=None, description="run id"),
        client=Depends(get_integration_signavio_client),
    ) -> dict:
        """Manage leanix integration signavio operations.

        Actions:
          - 'getconfigurations': List of configurations
          - 'createconfiguration': Create a configuration
          - 'getconfiguration': Fetch a configuration by id
          - 'updateconfiguration': Update a configuration
          - 'deleteconfiguration': Delete a configuration
          - 'synchronizeconfiguration': Trigger a synchronization run
          - 'unassignformation': Unassign formation from configuration
          - 'getformations': List of formations
          - 'getdirectories': List of SAP Signavio process directories that match with the search string for the given configuration
          - 'createcategory': Fetch dictionary categories information
          - 'getfactsheetfields': List all fields on a Fact Sheet available for mappings
          - 'getlabels': Provide the labels (names) for requested objects, like processes or directories.
          - 'getsignavioglossaryitemfields': List of fields of a dictionary item available for mappings
          - 'getsignavioprocessfields': List all SAP Signavio fields available for mappings
          - 'getprocessfields': List of processes that match with the search string
          - 'analyzelatestsynchronizationrun': Analyze the latest synchronization run
          - 'analyzesynchronizationrun': Analyze a synchronization run
          - 'cancelsynchronization': Trigger a synchronization cancellation
          - 'getlatestsynchronizationrunanalysis': Get analysis for the latest synchronization run
          - 'getsynchronizationrunanalysis': Get analysis for a synchronization run
        """
        kwargs: dict[str, Any]
        if action == "getconfigurations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getconfigurations(**kwargs)
        if action == "createconfiguration":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createconfiguration(**kwargs)
        if action == "getconfiguration":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getconfiguration(**kwargs)
        if action == "updateconfiguration":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updateconfiguration(**kwargs)
        if action == "deleteconfiguration":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deleteconfiguration(**kwargs)
        if action == "synchronizeconfiguration":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.synchronizeconfiguration(**kwargs)
        if action == "unassignformation":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.unassignformation(**kwargs)
        if action == "getformations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getformations(**kwargs)
        if action == "getdirectories":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getdirectories(**kwargs)
        if action == "createcategory":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createcategory(**kwargs)
        if action == "getfactsheetfields":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getfactsheetfields(**kwargs)
        if action == "getlabels":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getlabels(**kwargs)
        if action == "getsignavioglossaryitemfields":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsignavioglossaryitemfields(**kwargs)
        if action == "getsignavioprocessfields":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsignavioprocessfields(**kwargs)
        if action == "getprocessfields":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getprocessfields(**kwargs)
        if action == "analyzelatestsynchronizationrun":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.analyzelatestsynchronizationrun(**kwargs)
        if action == "analyzesynchronizationrun":
            kwargs = {"run_id": run_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.analyzesynchronizationrun(**kwargs)
        if action == "cancelsynchronization":
            kwargs = {"run_id": run_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.cancelsynchronization(**kwargs)
        if action == "getlatestsynchronizationrunanalysis":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getlatestsynchronizationrunanalysis(**kwargs)
        if action == "getsynchronizationrunanalysis":
            kwargs = {"run_id": run_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsynchronizationrunanalysis(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: getconfigurations', 'createconfiguration', 'getconfiguration', 'updateconfiguration', 'deleteconfiguration', 'synchronizeconfiguration', 'unassignformation', 'getformations', 'getdirectories', 'createcategory', 'getfactsheetfields', 'getlabels', 'getsignavioglossaryitemfields', 'getsignavioprocessfields', 'getprocessfields', 'analyzelatestsynchronizationrun', 'analyzesynchronizationrun', 'cancelsynchronization', 'getlatestsynchronizationrunanalysis', 'getsynchronizationrunanalysis"
        )


def register_leanix_inventory_data_quality_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-inventory-data-quality"})
    async def leanix_leanix_inventory_data_quality(
        action: str = Field(
            description="Action to perform. Must be one of: 'refreshembeddings', 'getrecommendationsapptobc', 'getrecommendationsagenttobc', 'submitfeedback', 'submitfeedback_1', 'submitdqicardfeedback', 'getdatamodel', 'getrelationnames', 'getfactsheettypes'"
        ),
        data: dict | None = Field(default=None, description="data"),
        client=Depends(get_inventory_data_quality_client),
    ) -> dict:
        """Manage leanix inventory data quality operations.

        Actions:
          - 'refreshembeddings': Refresh embeddings
          - 'getrecommendationsapptobc': Get App to BC recommendations
          - 'getrecommendationsagenttobc': Get Agent to BC recommendations
          - 'submitfeedback': Submit feedback
          - 'submitfeedback_1': Submit feedback
          - 'submitdqicardfeedback': Submit DQI Card feedback
          - 'getdatamodel': Call GET /api/v1/datamodel
          - 'getrelationnames': Call GET /api/v1/datamodel/relation-names
          - 'getfactsheettypes': Call GET /api/v1/datamodel/factsheet-types
        """
        kwargs: dict[str, Any]
        if action == "refreshembeddings":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.refreshembeddings(**kwargs)
        if action == "getrecommendationsapptobc":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getrecommendationsapptobc(**kwargs)
        if action == "getrecommendationsagenttobc":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getrecommendationsagenttobc(**kwargs)
        if action == "submitfeedback":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.submitfeedback(**kwargs)
        if action == "submitfeedback_1":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.submitfeedback_1(**kwargs)
        if action == "submitdqicardfeedback":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.submitdqicardfeedback(**kwargs)
        if action == "getdatamodel":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getdatamodel(**kwargs)
        if action == "getrelationnames":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getrelationnames(**kwargs)
        if action == "getfactsheettypes":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getfactsheettypes(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: refreshembeddings', 'getrecommendationsapptobc', 'getrecommendationsagenttobc', 'submitfeedback', 'submitfeedback_1', 'submitdqicardfeedback', 'getdatamodel', 'getrelationnames', 'getfactsheettypes"
        )


def register_leanix_mtm_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-mtm"})
    async def leanix_leanix_mtm(
        action: str = Field(
            description="Action to perform. Must be one of: 'getaiaccess', 'gettaskbyid', 'createworkspacelabel', 'deleteworkspacelabel', 'getall', 'getlabelsbyworkspace', 'getlabelsbyworkspaces', 'token', 'get_data_breach_contact', 'add_data_breach_contact', 'delete_data_breach_contact', 'get_accounts', 'create_account', 'get_account', 'update_account', 'delete_account', 'get_contracts', 'get_events', 'get_instances', 'get_settings', 'get_users', 'get_workspaces', 'getapitokens', 'createapitoken', 'getapitoken', 'updateapitoken', 'deleteapitoken', 'getfeature', 'accessfeature', 'getapplication', 'getapplications', 'getedition', 'geteditions', 'getfeatures', 'create_contract', 'get_contract', 'update_contract', 'delete_contract', 'get_custom_features', 'create_custom_feature', 'get_custom_feature', 'update_custom_feature', 'delete_custom_feature', 'deletedomain', 'getdomain', 'getdomains', 'upsertdomain', 'getidentityproviders', 'getworkspaces_2', 'create_event', 'get_event', 'update_event', 'getraw', 'get_export', 'process_graph_ql', 'get_identity_providers', 'create_identity_provider', 'get_identity_provider', 'update_identity_provider', 'delete_identity_provider', 'get_domains', 'get_metadata', 'getworkspaces_3', 'activate', 'authenticate', 'checkip', 'invite', 'login', 'loginpractitioner', 'logout', 'reset_password', 'review', 'set_password', 'switchpermissionrole', 'inactive', 'create_instance', 'get_instance', 'update_instance', 'delete_instance', 'getinstancesbyworkspace', 'getpreferredinstance', 'switchdefaultinstance', 'list', 'create', 'invalidate', 'getpermissions', 'createpermission', 'getpermission', 'getsettings_2', 'getuserrandom', 'getsettings_3', 'createsetting', 'getsetting', 'updatesetting', 'deletesetting', 'getnotificationsettings', 'setworkspacenotificationstatus', 'gettechnicalusers', 'create_technical_user', 'get_technical_user', 'update_technical_user', 'delete_technical_user', 'replace_technical_user_api_token', 'getusers_1', 'createuser', 'createuserpassword', 'getevents_6', 'getpermissions_1', 'getsettings_4', 'getuser', 'updateuser', 'getuserrandom_1', 'setpassword_1', 'create_workspace', 'get_workspace', 'update_workspace', 'delete_workspace', 'get_feature_bundle', 'get_impersonations', 'get_permission', 'get_permission_stats', 'get_permissions', 'get_support_permissions', 'get_user_list_export', 'getworkspacesforbackup', 'permissions_search', 'getuserpiichanges', 'get_user_segment', 'create_or_update_user_segment', 'getworkspacemaintenance', 'createworkspacemaintenance', 'deleteworkspacemaintenance'"
        ),
        workspace_id: str | None = Field(default=None, description="workspace id"),
        task_id: str | None = Field(default=None, description="task id"),
        label_id: str | None = Field(default=None, description="label id"),
        data: dict | None = Field(default=None, description="data"),
        account_id: str | None = Field(default=None, description="account id"),
        id_: str | None = Field(default=None, description="id "),
        name: str | None = Field(default=None, description="name"),
        feature_id: str | None = Field(default=None, description="feature id"),
        fqdn: str | None = Field(default=None, description="fqdn"),
        key: str | None = Field(default=None, description="key"),
        permission_id: str | None = Field(default=None, description="permission id"),
        user_id: str | None = Field(default=None, description="user id"),
        client=Depends(get_mtm_client),
    ) -> dict:
        """Manage leanix mtm operations.

        Actions:
          - 'getaiaccess': Returns AI feature access summary for the given workspace. Restricted to internal use only.
          - 'gettaskbyid': Get asynchronous task status by ID
          - 'createworkspacelabel': Adds a label to a workspace.
          - 'deleteworkspacelabel': Removes a label from a workspace.
          - 'getall': Get all labels
          - 'getlabelsbyworkspace': Get all currently existing labels on a workspace.
          - 'getlabelsbyworkspaces': Get all currently existing labels on a list of workspaces.
          - 'token': Creates an access token.
          - 'get_data_breach_contact': get_data_breach_contact
          - 'add_data_breach_contact': add_data_breach_contact
          - 'delete_data_breach_contact': delete_data_breach_contact
          - 'get_accounts': get_accounts
          - 'create_account': create_account
          - 'get_account': get_account
          - 'update_account': update_account
          - 'delete_account': delete_account
          - 'get_contracts': get_contracts
          - 'get_events': get_events
          - 'get_instances': get_instances
          - 'get_settings': get_settings
          - 'get_users': get_users
          - 'get_workspaces': get_workspaces
          - 'getapitokens': Retrieves all matching personal API Tokens.  Personal API Tokens are deprecated. Please use the 'Technical User' functionality to create an API Token.
          - 'createapitoken': Creates a personal API Token. Personal API Tokens are deprecated. Please use the 'Technical User' functionality to create an API Token.
          - 'getapitoken': Retrieves a personal API Token. Personal API Tokens are deprecated. Please use the 'Technical User' functionality to create an API Token.
          - 'updateapitoken': Updates a personal API Token. Personal API Tokens are deprecated. Please use the 'Technical User' functionality to create an API Token.
          - 'deleteapitoken': Deletes a personal API Token. Personal API Tokens are deprecated. Please use the 'Technical User' functionality to create an API Token.
          - 'getfeature': Get Feature
          - 'accessfeature': Access Feature
          - 'getapplication': Get Application
          - 'getapplications': Get Applications
          - 'getedition': Get Edition
          - 'geteditions': Get Editions
          - 'getfeatures': Get Features
          - 'create_contract': create_contract
          - 'get_contract': get_contract
          - 'update_contract': update_contract
          - 'delete_contract': delete_contract
          - 'get_custom_features': get_custom_features
          - 'create_custom_feature': create_custom_feature
          - 'get_custom_feature': get_custom_feature
          - 'update_custom_feature': update_custom_feature
          - 'delete_custom_feature': delete_custom_feature
          - 'deletedomain': Deletes a domain and the respective CNAME. Restricted to LeanIX internal use only.
          - 'getdomain': Retrieves a specific domain. Restricted to LeanIX internal use only.
          - 'getdomains': Retrieves all domains. Restricted to LeanIX internal use only.
          - 'upsertdomain': Creates or updates a domain and the respective CNAME. Restricted to LeanIX internal use only.
          - 'getidentityproviders': Retrieves all SIGNIN-based identity providers for a domain. Restricted to LeanIX internal use only.
          - 'getworkspaces_2': Retrieves all workspaces for a domain. Restricted to LeanIX internal use only.
          - 'create_event': create_event
          - 'get_event': get_event
          - 'update_event': update_event
          - 'getraw': Call GET /events/raw
          - 'get_export': get_export
          - 'process_graph_ql': process_graph_ql
          - 'get_identity_providers': get_identity_providers
          - 'create_identity_provider': create_identity_provider
          - 'get_identity_provider': get_identity_provider
          - 'update_identity_provider': update_identity_provider
          - 'delete_identity_provider': delete_identity_provider
          - 'get_domains': get_domains
          - 'get_metadata': get_metadata
          - 'getworkspaces_3': Retrieves all workspaces connected to an identity provider. Restricted to LeanIX internal use only.
          - 'activate': activate
          - 'authenticate': authenticate
          - 'checkip': Call POST /idm/check_ip
          - 'invite': invite
          - 'login': login
          - 'loginpractitioner': Call POST /idm/practitioner
          - 'logout': logout
          - 'reset_password': reset_password
          - 'review': review
          - 'set_password': set_password
          - 'switchpermissionrole': Call POST /idm/switch_permission_role
          - 'inactive': inactive
          - 'create_instance': create_instance
          - 'get_instance': get_instance
          - 'update_instance': update_instance
          - 'delete_instance': delete_instance
          - 'getinstancesbyworkspace': Call POST /instances/find_by_workspace_ids
          - 'getpreferredinstance': Call GET /instances/preferred
          - 'switchdefaultinstance': Call POST /instances/{id}/set_to_default
          - 'list': List all long-lived bearer tokens.
          - 'create': Create a new long-lived bearer token.
          - 'invalidate': Invalidate an existing long-lived bearer token.
          - 'getpermissions': Endpoint to list the user permissions. Restricted to LeanIX internal use only.
          - 'createpermission': Set a user permission for a workspace. If the related user object contains changed data, the data is persisted.
          - 'getpermission': Retrieves one permission for requested permission id.
          - 'getsettings_2': Endpoint to list the permission specific settings.
          - 'getuserrandom': Call GET /permissions/sample
          - 'getsettings_3': Retrieves settings
          - 'createsetting': Endpoint to set a setting.
          - 'getsetting': Endpoint to get_user_segment a setting.
          - 'updatesetting': Update a setting
          - 'deletesetting': Delete a setting
          - 'getnotificationsettings': Endpoint to get_user_segment all settings related to notifications, internal usage only.
          - 'setworkspacenotificationstatus': Endpoint to enable/disable notifications.
          - 'gettechnicalusers': Technical users
          - 'create_technical_user': create_technical_user
          - 'get_technical_user': get_technical_user
          - 'update_technical_user': update_technical_user
          - 'delete_technical_user': delete_technical_user
          - 'replace_technical_user_api_token': replace_technical_user_api_token
          - 'getusers_1': List or search all users.
          - 'createuser': Create a user
          - 'createuserpassword': Create a password for a user. Restricted to LeanIX internal use only.
          - 'getevents_6': Retrieves all events for an user (date must be ISO 8601 formatted)
          - 'getpermissions_1': Endpoint to list the user permissions.
          - 'getsettings_4': Endpoint to list the user specific settings.
          - 'getuser': Returns user data.
          - 'updateuser': Update a user
          - 'getuserrandom_1': Call GET /users/sample
          - 'setpassword_1': Endpoint to finish the reset the password process, can only be accessed by systems.
          - 'create_workspace': create_workspace
          - 'get_workspace': get_workspace
          - 'update_workspace': update_workspace
          - 'delete_workspace': delete_workspace
          - 'get_feature_bundle': get_feature_bundle
          - 'get_impersonations': get_impersonations
          - 'get_permission': get_permission
          - 'get_permission_stats': get_permission_stats
          - 'get_permissions': get_permissions
          - 'get_support_permissions': get_support_permissions
          - 'get_user_list_export': get_user_list_export
          - 'getworkspacesforbackup': Call GET /workspaces/backup_workspaces
          - 'permissions_search': permissions_search
          - 'getuserpiichanges': Get user PII changes
          - 'get_user_segment': get_user_segment
          - 'create_or_update_user_segment': create_or_update_user_segment
          - 'getworkspacemaintenance': Get maintenance mode
          - 'createworkspacemaintenance': Create a new maintenance
          - 'deleteworkspacemaintenance': Delete maintenance mode
        """
        kwargs: dict[str, Any]
        if action == "getaiaccess":
            kwargs = {"workspace_id": workspace_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getaiaccess(**kwargs)
        if action == "gettaskbyid":
            kwargs = {"task_id": task_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.gettaskbyid(**kwargs)
        if action == "createworkspacelabel":
            kwargs = {
                "label_id": label_id,
                "workspace_id": workspace_id,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createworkspacelabel(**kwargs)
        if action == "deleteworkspacelabel":
            kwargs = {
                "label_id": label_id,
                "workspace_id": workspace_id,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deleteworkspacelabel(**kwargs)
        if action == "getall":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getall(**kwargs)
        if action == "getlabelsbyworkspace":
            kwargs = {"workspace_id": workspace_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getlabelsbyworkspace(**kwargs)
        if action == "getlabelsbyworkspaces":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getlabelsbyworkspaces(**kwargs)
        if action == "token":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.token(**kwargs)
        if action == "get_data_breach_contact":
            kwargs = {"account_id": account_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_data_breach_contact(**kwargs)
        if action == "add_data_breach_contact":
            kwargs = {"account_id": account_id, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.add_data_breach_contact(**kwargs)
        if action == "delete_data_breach_contact":
            kwargs = {"account_id": account_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_data_breach_contact(**kwargs)
        if action == "get_accounts":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_accounts(**kwargs)
        if action == "create_account":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_account(**kwargs)
        if action == "get_account":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_account(**kwargs)
        if action == "update_account":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_account(**kwargs)
        if action == "delete_account":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_account(**kwargs)
        if action == "get_contracts":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_contracts(**kwargs)
        if action == "get_events":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_events(**kwargs)
        if action == "get_instances":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_instances(**kwargs)
        if action == "get_settings":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_settings(**kwargs)
        if action == "get_users":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_users(**kwargs)
        if action == "get_workspaces":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_workspaces(**kwargs)
        if action == "getapitokens":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getapitokens(**kwargs)
        if action == "createapitoken":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createapitoken(**kwargs)
        if action == "getapitoken":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getapitoken(**kwargs)
        if action == "updateapitoken":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updateapitoken(**kwargs)
        if action == "deleteapitoken":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deleteapitoken(**kwargs)
        if action == "getfeature":
            kwargs = {
                "name": name,
                "id_": id_,
                "feature_id": feature_id,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getfeature(**kwargs)
        if action == "accessfeature":
            kwargs = {
                "name": name,
                "id_": id_,
                "feature_id": feature_id,
                "data": data,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.accessfeature(**kwargs)
        if action == "getapplication":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getapplication(**kwargs)
        if action == "getapplications":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getapplications(**kwargs)
        if action == "getedition":
            kwargs = {"name": name, "id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getedition(**kwargs)
        if action == "geteditions":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.geteditions(**kwargs)
        if action == "getfeatures":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getfeatures(**kwargs)
        if action == "create_contract":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_contract(**kwargs)
        if action == "get_contract":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_contract(**kwargs)
        if action == "update_contract":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_contract(**kwargs)
        if action == "delete_contract":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_contract(**kwargs)
        if action == "get_custom_features":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_custom_features(**kwargs)
        if action == "create_custom_feature":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_custom_feature(**kwargs)
        if action == "get_custom_feature":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_custom_feature(**kwargs)
        if action == "update_custom_feature":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_custom_feature(**kwargs)
        if action == "delete_custom_feature":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_custom_feature(**kwargs)
        if action == "deletedomain":
            kwargs = {"fqdn": fqdn}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletedomain(**kwargs)
        if action == "getdomain":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getdomain(**kwargs)
        if action == "getdomains":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getdomains(**kwargs)
        if action == "upsertdomain":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.upsertdomain(**kwargs)
        if action == "getidentityproviders":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getidentityproviders(**kwargs)
        if action == "getworkspaces_2":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getworkspaces_2(**kwargs)
        if action == "create_event":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_event(**kwargs)
        if action == "get_event":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_event(**kwargs)
        if action == "update_event":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_event(**kwargs)
        if action == "getraw":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getraw(**kwargs)
        if action == "get_export":
            kwargs = {"key": key}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_export(**kwargs)
        if action == "process_graph_ql":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.process_graph_ql(**kwargs)
        if action == "get_identity_providers":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_identity_providers(**kwargs)
        if action == "create_identity_provider":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_identity_provider(**kwargs)
        if action == "get_identity_provider":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_identity_provider(**kwargs)
        if action == "update_identity_provider":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_identity_provider(**kwargs)
        if action == "delete_identity_provider":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_identity_provider(**kwargs)
        if action == "get_domains":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_domains(**kwargs)
        if action == "get_metadata":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_metadata(**kwargs)
        if action == "getworkspaces_3":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getworkspaces_3(**kwargs)
        if action == "activate":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.activate(**kwargs)
        if action == "authenticate":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.authenticate(**kwargs)
        if action == "checkip":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.checkip(**kwargs)
        if action == "invite":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.invite(**kwargs)
        if action == "login":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.login(**kwargs)
        if action == "loginpractitioner":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.loginpractitioner(**kwargs)
        if action == "logout":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.logout(**kwargs)
        if action == "reset_password":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.reset_password(**kwargs)
        if action == "review":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.review(**kwargs)
        if action == "set_password":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_password(**kwargs)
        if action == "switchpermissionrole":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.switchpermissionrole(**kwargs)
        if action == "inactive":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.inactive(**kwargs)
        if action == "create_instance":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_instance(**kwargs)
        if action == "get_instance":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_instance(**kwargs)
        if action == "update_instance":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_instance(**kwargs)
        if action == "delete_instance":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_instance(**kwargs)
        if action == "getinstancesbyworkspace":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getinstancesbyworkspace(**kwargs)
        if action == "getpreferredinstance":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getpreferredinstance(**kwargs)
        if action == "switchdefaultinstance":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.switchdefaultinstance(**kwargs)
        if action == "list":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.list(**kwargs)
        if action == "create":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create(**kwargs)
        if action == "invalidate":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.invalidate(**kwargs)
        if action == "getpermissions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getpermissions(**kwargs)
        if action == "createpermission":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createpermission(**kwargs)
        if action == "getpermission":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getpermission(**kwargs)
        if action == "getsettings_2":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsettings_2(**kwargs)
        if action == "getuserrandom":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getuserrandom(**kwargs)
        if action == "getsettings_3":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsettings_3(**kwargs)
        if action == "createsetting":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createsetting(**kwargs)
        if action == "getsetting":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsetting(**kwargs)
        if action == "updatesetting":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updatesetting(**kwargs)
        if action == "deletesetting":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletesetting(**kwargs)
        if action == "getnotificationsettings":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getnotificationsettings(**kwargs)
        if action == "setworkspacenotificationstatus":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.setworkspacenotificationstatus(**kwargs)
        if action == "gettechnicalusers":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.gettechnicalusers(**kwargs)
        if action == "create_technical_user":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_technical_user(**kwargs)
        if action == "get_technical_user":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_technical_user(**kwargs)
        if action == "update_technical_user":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_technical_user(**kwargs)
        if action == "delete_technical_user":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_technical_user(**kwargs)
        if action == "replace_technical_user_api_token":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.replace_technical_user_api_token(**kwargs)
        if action == "getusers_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getusers_1(**kwargs)
        if action == "createuser":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createuser(**kwargs)
        if action == "createuserpassword":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createuserpassword(**kwargs)
        if action == "getevents_6":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getevents_6(**kwargs)
        if action == "getpermissions_1":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getpermissions_1(**kwargs)
        if action == "getsettings_4":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsettings_4(**kwargs)
        if action == "getuser":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getuser(**kwargs)
        if action == "updateuser":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updateuser(**kwargs)
        if action == "getuserrandom_1":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getuserrandom_1(**kwargs)
        if action == "setpassword_1":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.setpassword_1(**kwargs)
        if action == "create_workspace":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_workspace(**kwargs)
        if action == "get_workspace":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_workspace(**kwargs)
        if action == "update_workspace":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_workspace(**kwargs)
        if action == "delete_workspace":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_workspace(**kwargs)
        if action == "get_feature_bundle":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_feature_bundle(**kwargs)
        if action == "get_impersonations":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_impersonations(**kwargs)
        if action == "get_permission":
            kwargs = {"id_": id_, "permission_id": permission_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_permission(**kwargs)
        if action == "get_permission_stats":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_permission_stats(**kwargs)
        if action == "get_permissions":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_permissions(**kwargs)
        if action == "get_support_permissions":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_support_permissions(**kwargs)
        if action == "get_user_list_export":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_user_list_export(**kwargs)
        if action == "getworkspacesforbackup":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getworkspacesforbackup(**kwargs)
        if action == "permissions_search":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.permissions_search(**kwargs)
        if action == "getuserpiichanges":
            kwargs = {"workspace_id": workspace_id, "user_id": user_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getuserpiichanges(**kwargs)
        if action == "get_user_segment":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_user_segment(**kwargs)
        if action == "create_or_update_user_segment":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_or_update_user_segment(**kwargs)
        if action == "getworkspacemaintenance":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getworkspacemaintenance(**kwargs)
        if action == "createworkspacemaintenance":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createworkspacemaintenance(**kwargs)
        if action == "deleteworkspacemaintenance":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deleteworkspacemaintenance(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: getaiaccess', 'gettaskbyid', 'createworkspacelabel', 'deleteworkspacelabel', 'getall', 'getlabelsbyworkspace', 'getlabelsbyworkspaces', 'token', 'get_data_breach_contact', 'add_data_breach_contact', 'delete_data_breach_contact', 'get_accounts', 'create_account', 'get_account', 'update_account', 'delete_account', 'get_contracts', 'get_events', 'get_instances', 'get_settings', 'get_users', 'get_workspaces', 'getapitokens', 'createapitoken', 'getapitoken', 'updateapitoken', 'deleteapitoken', 'getfeature', 'accessfeature', 'getapplication', 'getapplications', 'getedition', 'geteditions', 'getfeatures', 'create_contract', 'get_contract', 'update_contract', 'delete_contract', 'get_custom_features', 'create_custom_feature', 'get_custom_feature', 'update_custom_feature', 'delete_custom_feature', 'deletedomain', 'getdomain', 'getdomains', 'upsertdomain', 'getidentityproviders', 'getworkspaces_2', 'create_event', 'get_event', 'update_event', 'getraw', 'get_export', 'process_graph_ql', 'get_identity_providers', 'create_identity_provider', 'get_identity_provider', 'update_identity_provider', 'delete_identity_provider', 'get_domains', 'get_metadata', 'getworkspaces_3', 'activate', 'authenticate', 'checkip', 'invite', 'login', 'loginpractitioner', 'logout', 'reset_password', 'review', 'set_password', 'switchpermissionrole', 'inactive', 'create_instance', 'get_instance', 'update_instance', 'delete_instance', 'getinstancesbyworkspace', 'getpreferredinstance', 'switchdefaultinstance', 'list', 'create', 'invalidate', 'getpermissions', 'createpermission', 'getpermission', 'getsettings_2', 'getuserrandom', 'getsettings_3', 'createsetting', 'getsetting', 'updatesetting', 'deletesetting', 'getnotificationsettings', 'setworkspacenotificationstatus', 'gettechnicalusers', 'create_technical_user', 'get_technical_user', 'update_technical_user', 'delete_technical_user', 'replace_technical_user_api_token', 'getusers_1', 'createuser', 'createuserpassword', 'getevents_6', 'getpermissions_1', 'getsettings_4', 'getuser', 'updateuser', 'getuserrandom_1', 'setpassword_1', 'create_workspace', 'get_workspace', 'update_workspace', 'delete_workspace', 'get_feature_bundle', 'get_impersonations', 'get_permission', 'get_permission_stats', 'get_permissions', 'get_support_permissions', 'get_user_list_export', 'getworkspacesforbackup', 'permissions_search', 'getuserpiichanges', 'get_user_segment', 'create_or_update_user_segment', 'getworkspacemaintenance', 'createworkspacemaintenance', 'deleteworkspacemaintenance"
        )


def register_leanix_managed_code_execution_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-managed-code-execution"})
    async def leanix_leanix_managed_code_execution(
        action: str = Field(
            description="Action to perform. Must be one of: 'getsecretbyid', 'updatesecret', 'deletesecret', 'getexecutionconfiguration', 'updateexecutionconfiguration', 'deleteexecutionconfiguration', 'updateexecutionconfigurationcapability', 'getallsecrets', 'createsecret', 'getexecutionconfigurations', 'createexecutionconfiguration', 'getexecutionconfigurationsbysecretid', 'getexecutionlogs', 'getexecutionlog', 'getexecutionconfigurationhistory'"
        ),
        secret_id: str | None = Field(default=None, description="secret id"),
        data: dict | None = Field(default=None, description="data"),
        id_: str | None = Field(default=None, description="id "),
        execution_log_id: str | None = Field(
            default=None, description="execution log id"
        ),
        client=Depends(get_managed_code_execution_client),
    ) -> dict:
        """Manage leanix managed code execution operations.

        Actions:
          - 'getsecretbyid': Get a Secret by ID
          - 'updatesecret': Update a Secret
          - 'deletesecret': Delete a Secret
          - 'getexecutionconfiguration': Show details of specified ExecutionConfiguration
          - 'updateexecutionconfiguration': Update an existing ExecutionConfiguration
          - 'deleteexecutionconfiguration': Delete an existing ExecutionConfiguration
          - 'updateexecutionconfigurationcapability': Update capability of an ExecutionConfiguration
          - 'getallsecrets': Get all Secrets
          - 'createsecret': Create a new Secret
          - 'getexecutionconfigurations': List all available ExecutionConfigurations
          - 'createexecutionconfiguration': Create a new ExecutionConfiguration
          - 'getexecutionconfigurationsbysecretid': Get ExecutionConfigurations that reference a Secret
          - 'getexecutionlogs': List all available ExecutionLogs for one ExecutionConfiguration
          - 'getexecutionlog': Get a specific ExecutionLog for ExecutionConfiguration
          - 'getexecutionconfigurationhistory': List all versions of a given ExecutionConfiguration
        """
        kwargs: dict[str, Any]
        if action == "getsecretbyid":
            kwargs = {"secret_id": secret_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsecretbyid(**kwargs)
        if action == "updatesecret":
            kwargs = {"secret_id": secret_id, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updatesecret(**kwargs)
        if action == "deletesecret":
            kwargs = {"secret_id": secret_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletesecret(**kwargs)
        if action == "getexecutionconfiguration":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getexecutionconfiguration(**kwargs)
        if action == "updateexecutionconfiguration":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updateexecutionconfiguration(**kwargs)
        if action == "deleteexecutionconfiguration":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deleteexecutionconfiguration(**kwargs)
        if action == "updateexecutionconfigurationcapability":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updateexecutionconfigurationcapability(**kwargs)
        if action == "getallsecrets":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getallsecrets(**kwargs)
        if action == "createsecret":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createsecret(**kwargs)
        if action == "getexecutionconfigurations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getexecutionconfigurations(**kwargs)
        if action == "createexecutionconfiguration":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createexecutionconfiguration(**kwargs)
        if action == "getexecutionconfigurationsbysecretid":
            kwargs = {"secret_id": secret_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getexecutionconfigurationsbysecretid(**kwargs)
        if action == "getexecutionlogs":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getexecutionlogs(**kwargs)
        if action == "getexecutionlog":
            kwargs = {"id_": id_, "execution_log_id": execution_log_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getexecutionlog(**kwargs)
        if action == "getexecutionconfigurationhistory":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getexecutionconfigurationhistory(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: getsecretbyid', 'updatesecret', 'deletesecret', 'getexecutionconfiguration', 'updateexecutionconfiguration', 'deleteexecutionconfiguration', 'updateexecutionconfigurationcapability', 'getallsecrets', 'createsecret', 'getexecutionconfigurations', 'createexecutionconfiguration', 'getexecutionconfigurationsbysecretid', 'getexecutionlogs', 'getexecutionlog', 'getexecutionconfigurationhistory"
        )


def register_leanix_metrics_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-metrics"})
    async def leanix_leanix_metrics(
        action: str = Field(
            description="Action to perform. Must be one of: 'all_schemas_schemas_get', 'new_schema_schemas_post', 'find_schemas_schemas_find_get', 'one_schema_schemas__uuid__get', 'delete_schema_schemas__uuid__delete', 'all_points_schemas__uuid__points_get', 'new_point_schemas__uuid__points_post', 'delete_points_range_schemas__uuid__points_delete', 'get_aggregation_schemas__uuid__points_aggregation_post', 'one_point_schemas__uuid__points__timestamp__get', 'delete_one_point_schemas__uuid__points__timestamp__delete', 'trend_schemas__uuid__trends_get', 'all_kpis_kpis_get', 'put_kpi_kpis_put', 'new_kpi_kpis_post', 'patch_kpi_kpis_patch', 'all_kpis_simple_kpis_simple_get', 'one_kpi_kpis__uuid__get', 'delete_one_kpi_kpis__uuid__delete', 'validate_kpis_validate_post', 'healthcheck_healthcheck__get', 'ws_job_jobs_post', 'kpi_job_jobs_kpi__kpi_uuid__post', 'all_charts_charts_get', 'new_chart_charts_post', 'one_chart_charts__uuid__get', 'update_put_chart_charts__uuid__put', 'delete_chart_charts__uuid__delete', 'update_patch_chart_charts__uuid__patch'"
        ),
        data: dict | None = Field(default=None, description="data"),
        uuid: str | None = Field(default=None, description="uuid"),
        timestamp: str | None = Field(default=None, description="timestamp"),
        kpi_uuid: str | None = Field(default=None, description="kpi uuid"),
        client=Depends(get_metrics_client),
    ) -> dict:
        """Manage leanix metrics operations.

        Actions:
          - 'all_schemas_schemas_get': Return all schemas in workspace.
          - 'new_schema_schemas_post': Create a new schema.
          - 'find_schemas_schemas_find_get': Return single schema by UUID.
          - 'one_schema_schemas__uuid__get': Return single schema by UUID.
          - 'delete_schema_schemas__uuid__delete': Delete schema by UUID.
          - 'all_points_schemas__uuid__points_get': Return all points in schema.
          - 'new_point_schemas__uuid__points_post': Create or overwrite a point at the given timestamp.
          - 'delete_points_range_schemas__uuid__points_delete': Delete Points Range
          - 'get_aggregation_schemas__uuid__points_aggregation_post': Get an aggregation of points from a specified schema.
          - 'one_point_schemas__uuid__points__timestamp__get': Return single point in schema by timestamp.
          - 'delete_one_point_schemas__uuid__points__timestamp__delete': Delete One Point
          - 'trend_schemas__uuid__trends_get': Returns trend, difference and latest value for schema points.
          - 'all_kpis_kpis_get': Return all KPIs in workspace.
          - 'put_kpi_kpis_put': Update KPI.
          - 'new_kpi_kpis_post': Create a new KPI.
          - 'patch_kpi_kpis_patch': Patch KPI.
          - 'all_kpis_simple_kpis_simple_get': Return all KPIs in workspace with simplified data structure.
          - 'one_kpi_kpis__uuid__get': Return single KPI by UUID.
          - 'delete_one_kpi_kpis__uuid__delete': Delete KPI by UUID.
          - 'validate_kpis_validate_post': Validates a new KPI and return the result.
          - 'healthcheck_healthcheck__get': Show healthcheck status
          - 'ws_job_jobs_post': Trigger calculation of all KPIs in the user's workspace
          - 'kpi_job_jobs_kpi__kpi_uuid__post': Trigger calculation of a specific KPI
          - 'all_charts_charts_get': Return all Charts in a workspace.
          - 'new_chart_charts_post': Create a new Chart
          - 'one_chart_charts__uuid__get': Return a single Chart in a workspace.
          - 'update_put_chart_charts__uuid__put': Update all fields of a Chart
          - 'delete_chart_charts__uuid__delete': Delete a single Chart in a workspace.
          - 'update_patch_chart_charts__uuid__patch': Update only given fields of a Chart
        """
        kwargs: dict[str, Any]
        if action == "all_schemas_schemas_get":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.all_schemas_schemas_get(**kwargs)
        if action == "new_schema_schemas_post":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.new_schema_schemas_post(**kwargs)
        if action == "find_schemas_schemas_find_get":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.find_schemas_schemas_find_get(**kwargs)
        if action == "one_schema_schemas__uuid__get":
            kwargs = {"uuid": uuid}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.one_schema_schemas__uuid__get(**kwargs)
        if action == "delete_schema_schemas__uuid__delete":
            kwargs = {"uuid": uuid}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_schema_schemas__uuid__delete(**kwargs)
        if action == "all_points_schemas__uuid__points_get":
            kwargs = {"uuid": uuid}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.all_points_schemas__uuid__points_get(**kwargs)
        if action == "new_point_schemas__uuid__points_post":
            kwargs = {"uuid": uuid, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.new_point_schemas__uuid__points_post(**kwargs)
        if action == "delete_points_range_schemas__uuid__points_delete":
            kwargs = {"uuid": uuid}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_points_range_schemas__uuid__points_delete(**kwargs)
        if action == "get_aggregation_schemas__uuid__points_aggregation_post":
            kwargs = {"uuid": uuid, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_aggregation_schemas__uuid__points_aggregation_post(
                **kwargs
            )
        if action == "one_point_schemas__uuid__points__timestamp__get":
            kwargs = {"timestamp": timestamp, "uuid": uuid}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.one_point_schemas__uuid__points__timestamp__get(**kwargs)
        if action == "delete_one_point_schemas__uuid__points__timestamp__delete":
            kwargs = {"timestamp": timestamp, "uuid": uuid}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_one_point_schemas__uuid__points__timestamp__delete(
                **kwargs
            )
        if action == "trend_schemas__uuid__trends_get":
            kwargs = {"uuid": uuid}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.trend_schemas__uuid__trends_get(**kwargs)
        if action == "all_kpis_kpis_get":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.all_kpis_kpis_get(**kwargs)
        if action == "put_kpi_kpis_put":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.put_kpi_kpis_put(**kwargs)
        if action == "new_kpi_kpis_post":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.new_kpi_kpis_post(**kwargs)
        if action == "patch_kpi_kpis_patch":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.patch_kpi_kpis_patch(**kwargs)
        if action == "all_kpis_simple_kpis_simple_get":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.all_kpis_simple_kpis_simple_get(**kwargs)
        if action == "one_kpi_kpis__uuid__get":
            kwargs = {"uuid": uuid}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.one_kpi_kpis__uuid__get(**kwargs)
        if action == "delete_one_kpi_kpis__uuid__delete":
            kwargs = {"uuid": uuid}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_one_kpi_kpis__uuid__delete(**kwargs)
        if action == "validate_kpis_validate_post":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.validate_kpis_validate_post(**kwargs)
        if action == "healthcheck_healthcheck__get":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.healthcheck_healthcheck__get(**kwargs)
        if action == "ws_job_jobs_post":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.ws_job_jobs_post(**kwargs)
        if action == "kpi_job_jobs_kpi__kpi_uuid__post":
            kwargs = {"kpi_uuid": kpi_uuid}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.kpi_job_jobs_kpi__kpi_uuid__post(**kwargs)
        if action == "all_charts_charts_get":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.all_charts_charts_get(**kwargs)
        if action == "new_chart_charts_post":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.new_chart_charts_post(**kwargs)
        if action == "one_chart_charts__uuid__get":
            kwargs = {"uuid": uuid}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.one_chart_charts__uuid__get(**kwargs)
        if action == "update_put_chart_charts__uuid__put":
            kwargs = {"uuid": uuid, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_put_chart_charts__uuid__put(**kwargs)
        if action == "delete_chart_charts__uuid__delete":
            kwargs = {"uuid": uuid}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_chart_charts__uuid__delete(**kwargs)
        if action == "update_patch_chart_charts__uuid__patch":
            kwargs = {"uuid": uuid, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_patch_chart_charts__uuid__patch(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: all_schemas_schemas_get', 'new_schema_schemas_post', 'find_schemas_schemas_find_get', 'one_schema_schemas__uuid__get', 'delete_schema_schemas__uuid__delete', 'all_points_schemas__uuid__points_get', 'new_point_schemas__uuid__points_post', 'delete_points_range_schemas__uuid__points_delete', 'get_aggregation_schemas__uuid__points_aggregation_post', 'one_point_schemas__uuid__points__timestamp__get', 'delete_one_point_schemas__uuid__points__timestamp__delete', 'trend_schemas__uuid__trends_get', 'all_kpis_kpis_get', 'put_kpi_kpis_put', 'new_kpi_kpis_post', 'patch_kpi_kpis_patch', 'all_kpis_simple_kpis_simple_get', 'one_kpi_kpis__uuid__get', 'delete_one_kpi_kpis__uuid__delete', 'validate_kpis_validate_post', 'healthcheck_healthcheck__get', 'ws_job_jobs_post', 'kpi_job_jobs_kpi__kpi_uuid__post', 'all_charts_charts_get', 'new_chart_charts_post', 'one_chart_charts__uuid__get', 'update_put_chart_charts__uuid__put', 'delete_chart_charts__uuid__delete', 'update_patch_chart_charts__uuid__patch"
        )


def register_leanix_navigation_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-navigation"})
    async def leanix_leanix_navigation(
        action: str = Field(
            description="Action to perform. Must be one of: 'getallcollectiongroups', 'createcollectiongroup', 'batchputcollectiongroups', 'getcollectiongroupbyid', 'putcollectiongroupbyid', 'deletecollectiongroupbyid', 'postcollection', 'getcollections', 'putcollection', 'deletecollection', 'putcollectionnavigationitem', 'postcollectionnavigationitem', 'deletecollectionnavigationitem', 'getcollectionfolders', 'postfoldercontroller', 'updatefoldercontroller', 'executebatchmove', 'executebatchdelete', 'searchnavigationitem', 'getnavigationitemfavorite', 'postnavigationitemfavorite', 'deletenavigationitemfavorite', 'createslide', 'putslidebyid', 'deleteslidebyid', 'searchpresentation', 'createpresentation', 'getpresentationbyid', 'putpresentationbyid', 'deletepresentationbyid', 'getpresentationsharesbyid', 'sharepresentation', 'deletepresentationsharebyid'"
        ),
        data: dict | None = Field(default=None, description="data"),
        id_: str | None = Field(default=None, description="id "),
        collection_id: str | None = Field(default=None, description="collection id"),
        navigation_item_id: str | None = Field(
            default=None, description="navigation item id"
        ),
        folder_id: str | None = Field(default=None, description="folder id"),
        presentation_id: str | None = Field(
            default=None, description="presentation id"
        ),
        shared_with_user_id: str | None = Field(
            default=None, description="shared with user id"
        ),
        client=Depends(get_navigation_client),
    ) -> dict:
        """Manage leanix navigation operations.

        Actions:
          - 'getallcollectiongroups': Get all Collection Groups.
          - 'createcollectiongroup': Create a Collection Group
          - 'batchputcollectiongroups': Batch update collection groups.
          - 'getcollectiongroupbyid': Get Collection Group by ID.
          - 'putcollectiongroupbyid': Update Collection Group by ID.
          - 'deletecollectiongroupbyid': Delete Collection Group by ID.
          - 'postcollection': Create Collection.
          - 'getcollections': Get Collections.
          - 'putcollection': Update Collection.
          - 'deletecollection': Delete Collection.
          - 'putcollectionnavigationitem': Batch add navigation items into a collection.
          - 'postcollectionnavigationitem': Add Navigation Item to Collection.
          - 'deletecollectionnavigationitem': Remove Navigation Item from Collection.
          - 'getcollectionfolders': Get all folders of a collection.
          - 'postfoldercontroller': Create new folder.
          - 'updatefoldercontroller': Update folder.
          - 'executebatchmove': Batch move folders and items.
          - 'executebatchdelete': Batch delete folders and items.
          - 'searchnavigationitem': Search for navigation items
          - 'getnavigationitemfavorite': Get Navigation Item Favorite.
          - 'postnavigationitemfavorite': Create Navigation Item Favorite.
          - 'deletenavigationitemfavorite': Delete Navigation Item Favorite.
          - 'createslide': Create a slide.
          - 'putslidebyid': Update Slide by ID.
          - 'deleteslidebyid': Delete Slide by ID.
          - 'searchpresentation': Search for presentations
          - 'createpresentation': Create a presentation.
          - 'getpresentationbyid': Get Presentation by ID.
          - 'putpresentationbyid': Update Presentation by ID.
          - 'deletepresentationbyid': Delete Presentation by ID.
          - 'getpresentationsharesbyid': Get Presentation Shared With Users by ID.
          - 'sharepresentation': Share a presentation.
          - 'deletepresentationsharebyid': Revoke Presentation Share by ID.
        """
        kwargs: dict[str, Any]
        if action == "getallcollectiongroups":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getallcollectiongroups(**kwargs)
        if action == "createcollectiongroup":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createcollectiongroup(**kwargs)
        if action == "batchputcollectiongroups":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.batchputcollectiongroups(**kwargs)
        if action == "getcollectiongroupbyid":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getcollectiongroupbyid(**kwargs)
        if action == "putcollectiongroupbyid":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.putcollectiongroupbyid(**kwargs)
        if action == "deletecollectiongroupbyid":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletecollectiongroupbyid(**kwargs)
        if action == "postcollection":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.postcollection(**kwargs)
        if action == "getcollections":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getcollections(**kwargs)
        if action == "putcollection":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.putcollection(**kwargs)
        if action == "deletecollection":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletecollection(**kwargs)
        if action == "putcollectionnavigationitem":
            kwargs = {"collection_id": collection_id, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.putcollectionnavigationitem(**kwargs)
        if action == "postcollectionnavigationitem":
            kwargs = {
                "collection_id": collection_id,
                "navigation_item_id": navigation_item_id,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.postcollectionnavigationitem(**kwargs)
        if action == "deletecollectionnavigationitem":
            kwargs = {
                "collection_id": collection_id,
                "navigation_item_id": navigation_item_id,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletecollectionnavigationitem(**kwargs)
        if action == "getcollectionfolders":
            kwargs = {"collection_id": collection_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getcollectionfolders(**kwargs)
        if action == "postfoldercontroller":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.postfoldercontroller(**kwargs)
        if action == "updatefoldercontroller":
            kwargs = {"folder_id": folder_id, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updatefoldercontroller(**kwargs)
        if action == "executebatchmove":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.executebatchmove(**kwargs)
        if action == "executebatchdelete":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.executebatchdelete(**kwargs)
        if action == "searchnavigationitem":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.searchnavigationitem(**kwargs)
        if action == "getnavigationitemfavorite":
            kwargs = {"navigation_item_id": navigation_item_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getnavigationitemfavorite(**kwargs)
        if action == "postnavigationitemfavorite":
            kwargs = {"navigation_item_id": navigation_item_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.postnavigationitemfavorite(**kwargs)
        if action == "deletenavigationitemfavorite":
            kwargs = {"navigation_item_id": navigation_item_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletenavigationitemfavorite(**kwargs)
        if action == "createslide":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createslide(**kwargs)
        if action == "putslidebyid":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.putslidebyid(**kwargs)
        if action == "deleteslidebyid":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deleteslidebyid(**kwargs)
        if action == "searchpresentation":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.searchpresentation(**kwargs)
        if action == "createpresentation":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createpresentation(**kwargs)
        if action == "getpresentationbyid":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getpresentationbyid(**kwargs)
        if action == "putpresentationbyid":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.putpresentationbyid(**kwargs)
        if action == "deletepresentationbyid":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletepresentationbyid(**kwargs)
        if action == "getpresentationsharesbyid":
            kwargs = {"presentation_id": presentation_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getpresentationsharesbyid(**kwargs)
        if action == "sharepresentation":
            kwargs = {"presentation_id": presentation_id, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.sharepresentation(**kwargs)
        if action == "deletepresentationsharebyid":
            kwargs = {
                "presentation_id": presentation_id,
                "shared_with_user_id": shared_with_user_id,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletepresentationsharebyid(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: getallcollectiongroups', 'createcollectiongroup', 'batchputcollectiongroups', 'getcollectiongroupbyid', 'putcollectiongroupbyid', 'deletecollectiongroupbyid', 'postcollection', 'getcollections', 'putcollection', 'deletecollection', 'putcollectionnavigationitem', 'postcollectionnavigationitem', 'deletecollectionnavigationitem', 'getcollectionfolders', 'postfoldercontroller', 'updatefoldercontroller', 'executebatchmove', 'executebatchdelete', 'searchnavigationitem', 'getnavigationitemfavorite', 'postnavigationitemfavorite', 'deletenavigationitemfavorite', 'createslide', 'putslidebyid', 'deleteslidebyid', 'searchpresentation', 'createpresentation', 'getpresentationbyid', 'putpresentationbyid', 'deletepresentationbyid', 'getpresentationsharesbyid', 'sharepresentation', 'deletepresentationsharebyid"
        )


def register_leanix_pathfinder_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-pathfinder"})
    async def leanix_leanix_pathfinder(
        action: str = Field(
            description="Action to perform. Must be one of: 'download_asset', 'upsert_asset', 'delete_asset', 'get_bookmark_shares', 'createbookmarkshare', 'deletebookmarkshare', 'get_bookmark', 'update_bookmark', 'delete_bookmark', 'change_bookmark_owner', 'get_bookmarks', 'create_bookmark', 'get_all_versions_for_bookmark', 'get_data_model', 'update_data_model', 'get_enriched_data_model', 'create_full_export', 'download_export_file', 'get_exports', 'get_fact_sheet', 'update_fact_sheet', 'archive_fact_sheet', 'get_fact_sheets', 'create_fact_sheet', 'get_fact_sheet_relations', 'create_fact_sheet_relation', 'updatefactsheetrelation', 'delete_fact_sheet_relation', 'get_fact_sheet_hierarchy', 'get_feature', 'upsertfeature', 'get_features', 'process_graph_ql', 'process_graph_ql_multipart', 'get_access_control_entities', 'create_access_control_entity', 'readaccesscontrolentity', 'update_access_control_entity', 'delete_access_control_entity', 'get_authorization', 'update_authorization', 'get_fact_sheet_resource_model', 'update_fact_sheet_resource_model', 'get_language', 'update_language', 'get_reporting_model', 'update_reporting_model', 'get_view_model', 'update_view_model', 'get_model_customization', 'updatemodelswithcustomization', 'get_settings', 'update_settings', 'get_suggestions', 'get_meta_model', 'get_meta_model_actions', 'post_meta_model_actions', 'get_meta_model_actions_audit_log', 'get_meta_model_job', 'get_meta_model_permission_roles', 'get_meta_model_actions_for_node', 'get_action_batch', 'get_action_batches', 'post_action_batches', 'get_meta_model_authorization', 'get_meta_model_root', 'get_meta_model_for_type', 'get_preview_of_affected_data'"
        ),
        asset: str | None = Field(default=None, description="asset"),
        data: dict | None = Field(default=None, description="data"),
        id_: str | None = Field(default=None, description="id "),
        workspace_id: str | None = Field(default=None, description="workspace id"),
        relation_id: str | None = Field(default=None, description="relation id"),
        root_id: str | None = Field(default=None, description="root id"),
        fact_sheet_type: str | None = Field(
            default=None, description="fact sheet type"
        ),
        client=Depends(get_pathfinder_client),
    ) -> dict:
        """Manage leanix pathfinder operations.

        Actions:
          - 'download_asset': download_asset
          - 'upsert_asset': upsert_asset
          - 'delete_asset': delete_asset
          - 'get_bookmark_shares': get_bookmark_shares
          - 'createbookmarkshare': Call createbookmarkshare
          - 'deletebookmarkshare': Call deletebookmarkshare
          - 'get_bookmark': get_bookmark
          - 'update_bookmark': update_bookmark
          - 'delete_bookmark': delete_bookmark
          - 'change_bookmark_owner': change_bookmark_owner
          - 'get_bookmarks': get_bookmarks
          - 'create_bookmark': create_bookmark
          - 'get_all_versions_for_bookmark': get_all_versions_for_bookmark
          - 'get_data_model': get_data_model
          - 'update_data_model': update_data_model
          - 'get_enriched_data_model': get_enriched_data_model
          - 'create_full_export': create_full_export
          - 'download_export_file': download_export_file
          - 'get_exports': get_exports
          - 'get_fact_sheet': get_fact_sheet
          - 'update_fact_sheet': update_fact_sheet
          - 'archive_fact_sheet': archive_fact_sheet
          - 'get_fact_sheets': get_fact_sheets
          - 'create_fact_sheet': create_fact_sheet
          - 'get_fact_sheet_relations': get_fact_sheet_relations
          - 'create_fact_sheet_relation': create_fact_sheet_relation
          - 'updatefactsheetrelation': Call updatefactsheetrelation
          - 'delete_fact_sheet_relation': delete_fact_sheet_relation
          - 'get_fact_sheet_hierarchy': get_fact_sheet_hierarchy
          - 'get_feature': get_feature
          - 'upsertfeature': Call upsertfeature
          - 'get_features': get_features
          - 'process_graph_ql': process_graph_ql
          - 'process_graph_ql_multipart': process_graph_ql_multipart
          - 'get_access_control_entities': get_access_control_entities
          - 'create_access_control_entity': create_access_control_entity
          - 'readaccesscontrolentity': Call readaccesscontrolentity
          - 'update_access_control_entity': update_access_control_entity
          - 'delete_access_control_entity': delete_access_control_entity
          - 'get_authorization': Call get_authorization
          - 'update_authorization': Call update_authorization
          - 'get_fact_sheet_resource_model': Call get_fact_sheet_resource_model
          - 'update_fact_sheet_resource_model': Call update_fact_sheet_resource_model
          - 'get_language': Call get_language
          - 'update_language': Call update_language
          - 'get_reporting_model': Call get_reporting_model
          - 'update_reporting_model': Call update_reporting_model
          - 'get_view_model': Call get_view_model
          - 'update_view_model': Call update_view_model
          - 'get_model_customization': Call get_model_customization
          - 'updatemodelswithcustomization': Call updatemodelswithcustomization
          - 'get_settings': Call get_settings
          - 'update_settings': Call update_settings
          - 'get_suggestions': Call get_suggestions
          - 'get_meta_model': Call get_meta_model
          - 'get_meta_model_actions': Call get_meta_model_actions
          - 'post_meta_model_actions': Call post_meta_model_actions
          - 'get_meta_model_actions_audit_log': Call get_meta_model_actions_audit_log
          - 'get_meta_model_job': Call get_meta_model_job
          - 'get_meta_model_permission_roles': Call get_meta_model_permission_roles
          - 'get_meta_model_actions_for_node': Call get_meta_model_actions_for_node
          - 'get_action_batch': Call get_action_batch
          - 'get_action_batches': Call get_action_batches
          - 'post_action_batches': Call post_action_batches
          - 'get_meta_model_authorization': Call get_meta_model_authorization
          - 'get_meta_model_root': Call get_meta_model_root
          - 'get_meta_model_for_type': Call get_meta_model_for_type
          - 'get_preview_of_affected_data': Call get_preview_of_affected_data
        """
        kwargs: dict[str, Any]
        if action == "download_asset":
            kwargs = {"asset": asset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.download_asset(**kwargs)
        if action == "upsert_asset":
            kwargs = {"asset": asset, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.upsert_asset(**kwargs)
        if action == "delete_asset":
            kwargs = {"asset": asset}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_asset(**kwargs)
        if action == "get_bookmark_shares":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_bookmark_shares(**kwargs)
        if action == "createbookmarkshare":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createbookmarkshare(**kwargs)
        if action == "deletebookmarkshare":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletebookmarkshare(**kwargs)
        if action == "get_bookmark":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_bookmark(**kwargs)
        if action == "update_bookmark":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_bookmark(**kwargs)
        if action == "delete_bookmark":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_bookmark(**kwargs)
        if action == "change_bookmark_owner":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.change_bookmark_owner(**kwargs)
        if action == "get_bookmarks":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_bookmarks(**kwargs)
        if action == "create_bookmark":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_bookmark(**kwargs)
        if action == "get_all_versions_for_bookmark":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_all_versions_for_bookmark(**kwargs)
        if action == "get_data_model":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_data_model(**kwargs)
        if action == "update_data_model":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_data_model(**kwargs)
        if action == "get_enriched_data_model":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_enriched_data_model(**kwargs)
        if action == "create_full_export":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_full_export(**kwargs)
        if action == "download_export_file":
            kwargs = {"workspace_id": workspace_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.download_export_file(**kwargs)
        if action == "get_exports":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_exports(**kwargs)
        if action == "get_fact_sheet":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_fact_sheet(**kwargs)
        if action == "update_fact_sheet":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_fact_sheet(**kwargs)
        if action == "archive_fact_sheet":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.archive_fact_sheet(**kwargs)
        if action == "get_fact_sheets":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_fact_sheets(**kwargs)
        if action == "create_fact_sheet":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_fact_sheet(**kwargs)
        if action == "get_fact_sheet_relations":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_fact_sheet_relations(**kwargs)
        if action == "create_fact_sheet_relation":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_fact_sheet_relation(**kwargs)
        if action == "updatefactsheetrelation":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updatefactsheetrelation(**kwargs)
        if action == "delete_fact_sheet_relation":
            kwargs = {"id_": id_, "relation_id": relation_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_fact_sheet_relation(**kwargs)
        if action == "get_fact_sheet_hierarchy":
            kwargs = {"root_id": root_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_fact_sheet_hierarchy(**kwargs)
        if action == "get_feature":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_feature(**kwargs)
        if action == "upsertfeature":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.upsertfeature(**kwargs)
        if action == "get_features":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_features(**kwargs)
        if action == "process_graph_ql":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.process_graph_ql(**kwargs)
        if action == "process_graph_ql_multipart":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.process_graph_ql_multipart(**kwargs)
        if action == "get_access_control_entities":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_access_control_entities(**kwargs)
        if action == "create_access_control_entity":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_access_control_entity(**kwargs)
        if action == "readaccesscontrolentity":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.readaccesscontrolentity(**kwargs)
        if action == "update_access_control_entity":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_access_control_entity(**kwargs)
        if action == "delete_access_control_entity":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_access_control_entity(**kwargs)
        if action == "get_authorization":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_authorization(**kwargs)
        if action == "update_authorization":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_authorization(**kwargs)
        if action == "get_fact_sheet_resource_model":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_fact_sheet_resource_model(**kwargs)
        if action == "update_fact_sheet_resource_model":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_fact_sheet_resource_model(**kwargs)
        if action == "get_language":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_language(**kwargs)
        if action == "update_language":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_language(**kwargs)
        if action == "get_reporting_model":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_reporting_model(**kwargs)
        if action == "update_reporting_model":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_reporting_model(**kwargs)
        if action == "get_view_model":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_view_model(**kwargs)
        if action == "update_view_model":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_view_model(**kwargs)
        if action == "get_model_customization":
            kwargs = {"fact_sheet_type": fact_sheet_type}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_model_customization(**kwargs)
        if action == "updatemodelswithcustomization":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updatemodelswithcustomization(**kwargs)
        if action == "get_settings":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_settings(**kwargs)
        if action == "update_settings":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_settings(**kwargs)
        if action == "get_suggestions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_suggestions(**kwargs)
        if action == "get_meta_model":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_meta_model(**kwargs)
        if action == "get_meta_model_actions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_meta_model_actions(**kwargs)
        if action == "post_meta_model_actions":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.post_meta_model_actions(**kwargs)
        if action == "get_meta_model_actions_audit_log":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_meta_model_actions_audit_log(**kwargs)
        if action == "get_meta_model_job":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_meta_model_job(**kwargs)
        if action == "get_meta_model_permission_roles":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_meta_model_permission_roles(**kwargs)
        if action == "get_meta_model_actions_for_node":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_meta_model_actions_for_node(**kwargs)
        if action == "get_action_batch":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_action_batch(**kwargs)
        if action == "get_action_batches":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_action_batches(**kwargs)
        if action == "post_action_batches":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.post_action_batches(**kwargs)
        if action == "get_meta_model_authorization":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_meta_model_authorization(**kwargs)
        if action == "get_meta_model_root":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_meta_model_root(**kwargs)
        if action == "get_meta_model_for_type":
            kwargs = {"fact_sheet_type": fact_sheet_type}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_meta_model_for_type(**kwargs)
        if action == "get_preview_of_affected_data":
            kwargs = {"fact_sheet_type": fact_sheet_type}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_preview_of_affected_data(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: download_asset', 'upsert_asset', 'delete_asset', 'get_bookmark_shares', 'createbookmarkshare', 'deletebookmarkshare', 'get_bookmark', 'update_bookmark', 'delete_bookmark', 'change_bookmark_owner', 'get_bookmarks', 'create_bookmark', 'get_all_versions_for_bookmark', 'get_data_model', 'update_data_model', 'get_enriched_data_model', 'create_full_export', 'download_export_file', 'get_exports', 'get_fact_sheet', 'update_fact_sheet', 'archive_fact_sheet', 'get_fact_sheets', 'create_fact_sheet', 'get_fact_sheet_relations', 'create_fact_sheet_relation', 'updatefactsheetrelation', 'delete_fact_sheet_relation', 'get_fact_sheet_hierarchy', 'get_feature', 'upsertfeature', 'get_features', 'process_graph_ql', 'process_graph_ql_multipart', 'get_access_control_entities', 'create_access_control_entity', 'readaccesscontrolentity', 'update_access_control_entity', 'delete_access_control_entity', 'get_authorization', 'update_authorization', 'get_fact_sheet_resource_model', 'update_fact_sheet_resource_model', 'get_language', 'update_language', 'get_reporting_model', 'update_reporting_model', 'get_view_model', 'update_view_model', 'get_model_customization', 'updatemodelswithcustomization', 'get_settings', 'update_settings', 'get_suggestions', 'get_meta_model', 'get_meta_model_actions', 'post_meta_model_actions', 'get_meta_model_actions_audit_log', 'get_meta_model_job', 'get_meta_model_permission_roles', 'get_meta_model_actions_for_node', 'get_action_batch', 'get_action_batches', 'post_action_batches', 'get_meta_model_authorization', 'get_meta_model_root', 'get_meta_model_for_type', 'get_preview_of_affected_data"
        )


def register_leanix_poll_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-poll"})
    async def leanix_leanix_poll(
        action: str = Field(
            description="Action to perform. Must be one of: 'replay', 'get_polls_for_factsheet', 'get_polls', 'create_poll', 'get_poll', 'update_poll', 'delete_poll', 'get_poll_count', 'get_poll_recipient_details', 'get_poll_poll_runs', 'get_poll_result', 'update_poll_result', 'check_for_new_fact_sheets', 'create_poll_reminder', 'get_poll_runs', 'create_poll_run', 'get_poll_run', 'update_poll_run', 'delete_poll_run', 'get_added_recipients_for_run', 'get_poll_results_for_user', 'get_poll_run_results', 'get_poll_runs_kpi_counts', 'get_recipients_for_poll_run', 'get_reminders', 'get_results_for_poll_run', 'set_status', 'get_all', 'create_poll_template', 'get_by_id', 'delete_by_id'"
        ),
        fact_sheet_id: str | None = Field(default=None, description="fact sheet id"),
        data: dict | None = Field(default=None, description="data"),
        id_: str | None = Field(default=None, description="id "),
        user_uuid: str | None = Field(default=None, description="user uuid"),
        client=Depends(get_poll_client),
    ) -> dict:
        """Manage leanix poll operations.

        Actions:
          - 'replay': replay
          - 'get_polls_for_factsheet': get_polls_for_factsheet
          - 'get_polls': get_polls
          - 'create_poll': create_poll
          - 'get_poll': get_poll
          - 'update_poll': update_poll
          - 'delete_poll': delete_poll
          - 'get_poll_count': get_poll_count
          - 'get_poll_recipient_details': get_poll_recipient_details
          - 'get_poll_poll_runs': get_poll_poll_runs
          - 'get_poll_result': get_poll_result
          - 'update_poll_result': update_poll_result
          - 'check_for_new_fact_sheets': check_for_new_fact_sheets
          - 'create_poll_reminder': create_poll_reminder
          - 'get_poll_runs': get_poll_runs
          - 'create_poll_run': create_poll_run
          - 'get_poll_run': get_poll_run
          - 'update_poll_run': update_poll_run
          - 'delete_poll_run': delete_poll_run
          - 'get_added_recipients_for_run': get_added_recipients_for_run
          - 'get_poll_results_for_user': get_poll_results_for_user
          - 'get_poll_run_results': get_poll_run_results
          - 'get_poll_runs_kpi_counts': get_poll_runs_kpi_counts
          - 'get_recipients_for_poll_run': get_recipients_for_poll_run
          - 'get_reminders': get_reminders
          - 'get_results_for_poll_run': get_results_for_poll_run
          - 'set_status': set_status
          - 'get_all': get_all
          - 'create_poll_template': create_poll_template
          - 'get_by_id': get_by_id
          - 'delete_by_id': delete_by_id
        """
        kwargs: dict[str, Any]
        if action == "replay":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.replay(**kwargs)
        if action == "get_polls_for_factsheet":
            kwargs = {"fact_sheet_id": fact_sheet_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_polls_for_factsheet(**kwargs)
        if action == "get_polls":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_polls(**kwargs)
        if action == "create_poll":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_poll(**kwargs)
        if action == "get_poll":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_poll(**kwargs)
        if action == "update_poll":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_poll(**kwargs)
        if action == "delete_poll":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_poll(**kwargs)
        if action == "get_poll_count":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_poll_count(**kwargs)
        if action == "get_poll_recipient_details":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_poll_recipient_details(**kwargs)
        if action == "get_poll_poll_runs":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_poll_poll_runs(**kwargs)
        if action == "get_poll_result":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_poll_result(**kwargs)
        if action == "update_poll_result":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_poll_result(**kwargs)
        if action == "check_for_new_fact_sheets":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.check_for_new_fact_sheets(**kwargs)
        if action == "create_poll_reminder":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_poll_reminder(**kwargs)
        if action == "get_poll_runs":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_poll_runs(**kwargs)
        if action == "create_poll_run":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_poll_run(**kwargs)
        if action == "get_poll_run":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_poll_run(**kwargs)
        if action == "update_poll_run":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_poll_run(**kwargs)
        if action == "delete_poll_run":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_poll_run(**kwargs)
        if action == "get_added_recipients_for_run":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_added_recipients_for_run(**kwargs)
        if action == "get_poll_results_for_user":
            kwargs = {"id_": id_, "user_uuid": user_uuid}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_poll_results_for_user(**kwargs)
        if action == "get_poll_run_results":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_poll_run_results(**kwargs)
        if action == "get_poll_runs_kpi_counts":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_poll_runs_kpi_counts(**kwargs)
        if action == "get_recipients_for_poll_run":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_recipients_for_poll_run(**kwargs)
        if action == "get_reminders":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_reminders(**kwargs)
        if action == "get_results_for_poll_run":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_results_for_poll_run(**kwargs)
        if action == "set_status":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.set_status(**kwargs)
        if action == "get_all":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_all(**kwargs)
        if action == "create_poll_template":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_poll_template(**kwargs)
        if action == "get_by_id":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_by_id(**kwargs)
        if action == "delete_by_id":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_by_id(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: replay', 'get_polls_for_factsheet', 'get_polls', 'create_poll', 'get_poll', 'update_poll', 'delete_poll', 'get_poll_count', 'get_poll_recipient_details', 'get_poll_poll_runs', 'get_poll_result', 'update_poll_result', 'check_for_new_fact_sheets', 'create_poll_reminder', 'get_poll_runs', 'create_poll_run', 'get_poll_run', 'update_poll_run', 'delete_poll_run', 'get_added_recipients_for_run', 'get_poll_results_for_user', 'get_poll_run_results', 'get_poll_runs_kpi_counts', 'get_recipients_for_poll_run', 'get_reminders', 'get_results_for_poll_run', 'set_status', 'get_all', 'create_poll_template', 'get_by_id', 'delete_by_id"
        )


def register_leanix_reference_data_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-reference-data"})
    async def leanix_leanix_reference_data(
        action: str = Field(
            description="Action to perform. Must be one of: 'gettbmtaxonomy', 'getfactsheetsbysourcename', 'getlatestrecommendationrun', 'putusedtechnolotrecommendationcontroller', 'getusedtechnolotrecommendationcontroller', 'get_source_name_fact_sheets_id', 'getlinksbysourcename', 'putlinksbysourcename', 'putsourcehierarchylinkcontroller', 'putbulklinksbysourcename', 'putbulksourcehierarchylinkscontroller', 'getlinksbyfactsheettype', 'getlinkbysourcename', 'deletelinkbysourcename', 'getrequests', 'putrequests', 'getrequestscount', 'getrefresh', 'getrefreshes', 'postrefresh', 'refreshltlslinks', 'batchlinks', 'clonelinks', 'getlink', 'getconfigurationmodels', 'getconfiguration', 'putconfiguration', 'getsaasconfiguration', 'putsaasconfiguration', 'gettechcategoryconfiguration', 'puttechcategoryconfiguration', 'getbuscapconfiguration', 'putbuscapconfiguration', 'getprovisioning', 'putprovisioning', 'getlinks', 'clearduplicatelinks', 'validatelink', 'gettbmmigrationstatus', 'tbmmigrationstatusupdate', 'startmappingexport', 'getexportstatus', 'getexportfile', 'putimporttbm', 'precomputedrecommendations', 'getbusinesscapability', 'postbusinesscapability', 'filteredfactsheetscount', 'post_jobs', 'get_jobs', 'fetchbusinesscapabilitymetrics', 'post_managedsnapshotrequests', 'post_managedrestorationrequests'"
        ),
        name: str | None = Field(default=None, description="name"),
        data: dict | None = Field(default=None, description="data"),
        id_: str | None = Field(default=None, description="id "),
        factsheet_type: str | None = Field(default=None, description="factsheet type"),
        target_fact_sheet_id: str | None = Field(
            default=None, description="target fact sheet id"
        ),
        run_id: str | None = Field(default=None, description="run id"),
        industry: str | None = Field(default=None, description="industry"),
        client=Depends(get_reference_data_client),
    ) -> dict:
        """Manage leanix reference data operations.

        Actions:
          - 'gettbmtaxonomy': Get TBM Taxonomy
          - 'getfactsheetsbysourcename': Get Fact Sheets by source name
          - 'getlatestrecommendationrun': Fetches the latest recommendation run for a workspace
          - 'putusedtechnolotrecommendationcontroller': Inserts entries of Technolot recommendations used by batch-linking
          - 'getusedtechnolotrecommendationcontroller': Get entries of Technolot recommendations used by LTLS by workspace_ids/LTLS FactSheet Ids
          - 'get_source_name_fact_sheets_id': Get Fact Sheet by source name, and by Fact Sheet id
          - 'getlinksbysourcename': Get existing links to your workspace by source name
          - 'putlinksbysourcename': Inserts or updates a link to your workspace by source name
          - 'putsourcehierarchylinkcontroller': Inserts or updates a link to your workspace
          - 'putbulklinksbysourcename': Inserts or updates a multiple links to your workspace by source name
          - 'putbulksourcehierarchylinkscontroller': Inserts or updates a multiple links to your workspace by source name
          - 'getlinksbyfactsheettype': Get links based on factsheet type
          - 'getlinkbysourcename': Get the unique link to a Fact Sheet of the Fact Sheet in the target workspace by source name
          - 'deletelinkbysourcename': Delete the unique link to a source Fact Sheet of the Fact Sheet in the target workspace
          - 'getrequests': Get requests of your workspace by source name
          - 'putrequests': Inserts or updates a missing request for your Fact Sheet by source name
          - 'getrequestscount': Get the count of different types of requests for a workspace
          - 'getrefresh': Get the refresh of your workspace by source name
          - 'getrefreshes': Get all the refreshes of your workspace by source name
          - 'postrefresh': Creates and asynchronously starts a refresh for your workspace. That refresh synchronizes all data of existing links.
          - 'refreshltlslinks': Updates the InternalId of LTLS Links if incorrect
          - 'batchlinks': Fetches Catalog links and suggestions in batches
          - 'clonelinks': Clones a link to your workspace by source name
          - 'getlink': Get the missing request for this Fact Sheet in the target workspace by source name
          - 'getconfigurationmodels': Get the view model, data model and translation model from the source workspace
          - 'getconfiguration': Get the configuration for your source workspace
          - 'putconfiguration': Inserts or updates the configuration for your source workspace
          - 'getsaasconfiguration': Get the configuration for your source workspace
          - 'putsaasconfiguration': Inserts or updates the configuration for your source workspace
          - 'gettechcategoryconfiguration': Get the configuration for your source workspace
          - 'puttechcategoryconfiguration': Inserts or updates the configuration for your source workspace
          - 'getbuscapconfiguration': Get the configuration for your source workspace
          - 'putbuscapconfiguration': Inserts or updates the configuration for your source workspace
          - 'getprovisioning': Get information about the provisioning status of the data model and the translation model of your workspace
          - 'putprovisioning': Trigger the provisioning for your workspace
          - 'getlinks': Get the IDs of workspaces with existing links by source name
          - 'clearduplicatelinks': Clears Duplicate Links in reference-data for a workspace
          - 'validatelink': Validates the details of link
          - 'gettbmmigrationstatus': Get status of tbm migration cron job.
          - 'tbmmigrationstatusupdate': Put status of tbm migration cron job.
          - 'startmappingexport': Start the Excel export for the respective workspace, with details of possible new TBM mappings for existing Tech Categories of IT Components
          - 'getexportstatus': Get the status of export for the run_id
          - 'getexportfile': Get the Excel file path for the run_id
          - 'putimporttbm': Start automate import tbm in the workspace
          - 'precomputedrecommendations': Endpoint to fetch the precomputed recommendations
          - 'getbusinesscapability': Fetch hierarchy for queried industry
          - 'postbusinesscapability': Endpoint to fetch business capability catalog factsheets for given ids and industry
          - 'filteredfactsheetscount': Endpoint to fetch the precomputed recommendations
          - 'post_jobs': The endpoint creates a job for asynchronous processing.
          - 'get_jobs': The endpoint to retrieve the created async processing jobs.
          - 'fetchbusinesscapabilitymetrics': Endpoint to fetch the Business Capability Metrics
          - 'post_managedsnapshotrequests': Endpoint to create snapshots for workspace
          - 'post_managedrestorationrequests': Endpoint to restore snapshots for workspaces
        """
        kwargs: dict[str, Any]
        if action == "gettbmtaxonomy":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.gettbmtaxonomy(**kwargs)
        if action == "getfactsheetsbysourcename":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getfactsheetsbysourcename(**kwargs)
        if action == "getlatestrecommendationrun":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getlatestrecommendationrun(**kwargs)
        if action == "putusedtechnolotrecommendationcontroller":
            kwargs = {"name": name, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.putusedtechnolotrecommendationcontroller(**kwargs)
        if action == "getusedtechnolotrecommendationcontroller":
            kwargs = {"name": name, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getusedtechnolotrecommendationcontroller(**kwargs)
        if action == "get_source_name_fact_sheets_id":
            kwargs = {"name": name, "id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_source_name_fact_sheets_id(**kwargs)
        if action == "getlinksbysourcename":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getlinksbysourcename(**kwargs)
        if action == "putlinksbysourcename":
            kwargs = {"name": name, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.putlinksbysourcename(**kwargs)
        if action == "putsourcehierarchylinkcontroller":
            kwargs = {"name": name, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.putsourcehierarchylinkcontroller(**kwargs)
        if action == "putbulklinksbysourcename":
            kwargs = {"name": name, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.putbulklinksbysourcename(**kwargs)
        if action == "putbulksourcehierarchylinkscontroller":
            kwargs = {"name": name, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.putbulksourcehierarchylinkscontroller(**kwargs)
        if action == "getlinksbyfactsheettype":
            kwargs = {"name": name, "factsheet_type": factsheet_type}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getlinksbyfactsheettype(**kwargs)
        if action == "getlinkbysourcename":
            kwargs = {
                "name": name,
                "target_fact_sheet_id": target_fact_sheet_id,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getlinkbysourcename(**kwargs)
        if action == "deletelinkbysourcename":
            kwargs = {
                "name": name,
                "target_fact_sheet_id": target_fact_sheet_id,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletelinkbysourcename(**kwargs)
        if action == "getrequests":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getrequests(**kwargs)
        if action == "putrequests":
            kwargs = {"name": name, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.putrequests(**kwargs)
        if action == "getrequestscount":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getrequestscount(**kwargs)
        if action == "getrefresh":
            kwargs = {"name": name, "id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getrefresh(**kwargs)
        if action == "getrefreshes":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getrefreshes(**kwargs)
        if action == "postrefresh":
            kwargs = {"name": name, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.postrefresh(**kwargs)
        if action == "refreshltlslinks":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.refreshltlslinks(**kwargs)
        if action == "batchlinks":
            kwargs = {"name": name, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.batchlinks(**kwargs)
        if action == "clonelinks":
            kwargs = {"name": name, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.clonelinks(**kwargs)
        if action == "getlink":
            kwargs = {
                "name": name,
                "target_fact_sheet_id": target_fact_sheet_id,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getlink(**kwargs)
        if action == "getconfigurationmodels":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getconfigurationmodels(**kwargs)
        if action == "getconfiguration":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getconfiguration(**kwargs)
        if action == "putconfiguration":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.putconfiguration(**kwargs)
        if action == "getsaasconfiguration":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsaasconfiguration(**kwargs)
        if action == "putsaasconfiguration":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.putsaasconfiguration(**kwargs)
        if action == "gettechcategoryconfiguration":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.gettechcategoryconfiguration(**kwargs)
        if action == "puttechcategoryconfiguration":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.puttechcategoryconfiguration(**kwargs)
        if action == "getbuscapconfiguration":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getbuscapconfiguration(**kwargs)
        if action == "putbuscapconfiguration":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.putbuscapconfiguration(**kwargs)
        if action == "getprovisioning":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getprovisioning(**kwargs)
        if action == "putprovisioning":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.putprovisioning(**kwargs)
        if action == "getlinks":
            kwargs = {"name": name}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getlinks(**kwargs)
        if action == "clearduplicatelinks":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.clearduplicatelinks(**kwargs)
        if action == "validatelink":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.validatelink(**kwargs)
        if action == "gettbmmigrationstatus":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.gettbmmigrationstatus(**kwargs)
        if action == "tbmmigrationstatusupdate":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.tbmmigrationstatusupdate(**kwargs)
        if action == "startmappingexport":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.startmappingexport(**kwargs)
        if action == "getexportstatus":
            kwargs = {"run_id": run_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getexportstatus(**kwargs)
        if action == "getexportfile":
            kwargs = {"run_id": run_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getexportfile(**kwargs)
        if action == "putimporttbm":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.putimporttbm(**kwargs)
        if action == "precomputedrecommendations":
            kwargs = {"name": name, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.precomputedrecommendations(**kwargs)
        if action == "getbusinesscapability":
            kwargs = {"name": name, "industry": industry}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getbusinesscapability(**kwargs)
        if action == "postbusinesscapability":
            kwargs = {"name": name, "industry": industry, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.postbusinesscapability(**kwargs)
        if action == "filteredfactsheetscount":
            kwargs = {"name": name, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.filteredfactsheetscount(**kwargs)
        if action == "post_jobs":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.post_jobs(**kwargs)
        if action == "get_jobs":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_jobs(**kwargs)
        if action == "fetchbusinesscapabilitymetrics":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.fetchbusinesscapabilitymetrics(**kwargs)
        if action == "post_managedsnapshotrequests":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.post_managedsnapshotrequests(**kwargs)
        if action == "post_managedrestorationrequests":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.post_managedrestorationrequests(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: gettbmtaxonomy', 'getfactsheetsbysourcename', 'getlatestrecommendationrun', 'putusedtechnolotrecommendationcontroller', 'getusedtechnolotrecommendationcontroller', 'get_source_name_fact_sheets_id', 'getlinksbysourcename', 'putlinksbysourcename', 'putsourcehierarchylinkcontroller', 'putbulklinksbysourcename', 'putbulksourcehierarchylinkscontroller', 'getlinksbyfactsheettype', 'getlinkbysourcename', 'deletelinkbysourcename', 'getrequests', 'putrequests', 'getrequestscount', 'getrefresh', 'getrefreshes', 'postrefresh', 'refreshltlslinks', 'batchlinks', 'clonelinks', 'getlink', 'getconfigurationmodels', 'getconfiguration', 'putconfiguration', 'getsaasconfiguration', 'putsaasconfiguration', 'gettechcategoryconfiguration', 'puttechcategoryconfiguration', 'getbuscapconfiguration', 'putbuscapconfiguration', 'getprovisioning', 'putprovisioning', 'getlinks', 'clearduplicatelinks', 'validatelink', 'gettbmmigrationstatus', 'tbmmigrationstatusupdate', 'startmappingexport', 'getexportstatus', 'getexportfile', 'putimporttbm', 'precomputedrecommendations', 'getbusinesscapability', 'postbusinesscapability', 'filteredfactsheetscount', 'post_jobs', 'get_jobs', 'fetchbusinesscapabilitymetrics', 'post_managedsnapshotrequests', 'post_managedrestorationrequests"
        )


def register_leanix_discovery_sap_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-discovery-sap"})
    async def leanix_leanix_discovery_sap(
        action: str = Field(
            description="Action to perform. Must be one of: 'appcontroller_heartbeat', 'demodatacontroller_demodatalist', 'demodatacontroller_createcustomdemodata', 'integrationscontroller_integrationcreate', 'integrationscontroller_integrationslist', 'integrationscontroller_integrationget', 'integrationscontroller_integrationdelete', 'integrationscontroller_integrationpatch', 'integrationscontroller_integrationtriggersync'"
        ),
        data: dict | None = Field(default=None, description="data"),
        id_: str | None = Field(default=None, description="id "),
        client=Depends(get_discovery_sap_client),
    ) -> dict:
        """Manage leanix discovery sap operations.

        Actions:
          - 'appcontroller_heartbeat': Call GET /heartbeat
          - 'demodatacontroller_demodatalist': Call GET /demo-data
          - 'demodatacontroller_createcustomdemodata': Call POST /demo-data
          - 'integrationscontroller_integrationcreate': Call POST /integrations
          - 'integrationscontroller_integrationslist': Call GET /integrations
          - 'integrationscontroller_integrationget': Call GET /integrations/{id}
          - 'integrationscontroller_integrationdelete': Call DELETE /integrations/{id_}
          - 'integrationscontroller_integrationpatch': Call PATCH /integrations/{id_}
          - 'integrationscontroller_integrationtriggersync': Call POST /integrations/{id}/sync
        """
        kwargs: dict[str, Any]
        if action == "appcontroller_heartbeat":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.appcontroller_heartbeat(**kwargs)
        if action == "demodatacontroller_demodatalist":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.demodatacontroller_demodatalist(**kwargs)
        if action == "demodatacontroller_createcustomdemodata":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.demodatacontroller_createcustomdemodata(**kwargs)
        if action == "integrationscontroller_integrationcreate":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.integrationscontroller_integrationcreate(**kwargs)
        if action == "integrationscontroller_integrationslist":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.integrationscontroller_integrationslist(**kwargs)
        if action == "integrationscontroller_integrationget":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.integrationscontroller_integrationget(**kwargs)
        if action == "integrationscontroller_integrationdelete":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.integrationscontroller_integrationdelete(**kwargs)
        if action == "integrationscontroller_integrationpatch":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.integrationscontroller_integrationpatch(**kwargs)
        if action == "integrationscontroller_integrationtriggersync":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.integrationscontroller_integrationtriggersync(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: appcontroller_heartbeat', 'demodatacontroller_demodatalist', 'demodatacontroller_createcustomdemodata', 'integrationscontroller_integrationcreate', 'integrationscontroller_integrationslist', 'integrationscontroller_integrationget', 'integrationscontroller_integrationdelete', 'integrationscontroller_integrationpatch', 'integrationscontroller_integrationtriggersync"
        )


def register_leanix_technology_discovery_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-technology-discovery"})
    async def leanix_leanix_technology_discovery(
        action: str = Field(
            description="Action to perform. Must be one of: 'leanix_v1_microservice_discovery_yaml_manifest_register', 'leanix_v1_factsheets_sboms_ingest', 'leanix_v1_factsheets_sboms_ingest_1', 'getcomponentsbyapplication', 'searchcomponentsbypurl', 'getalltechstacks', 'updatetechstackbyqueryparam', 'createtechstack', 'deletetechstackbyqueryparam', 'previewmatches', 'gettechstackdetailsbyqueryparam', 'getaggregatedcounts', 'getfactsheetsbylibrary', 'getlibraryusagedetails', 'getversionsbylibrary', 'getlibraries'"
        ),
        data: dict | None = Field(default=None, description="data"),
        fact_sheet_id: str | None = Field(default=None, description="fact sheet id"),
        job_id: str | None = Field(default=None, description="job id"),
        library_id: str | None = Field(default=None, description="library id"),
        id_: str | None = Field(default=None, description="id "),
        client=Depends(get_technology_discovery_client),
    ) -> dict:
        """Manage leanix technology discovery operations.

        Actions:
          - 'leanix_v1_microservice_discovery_yaml_manifest_register': Microservice Discovery Through YAML Manifest File
          - 'leanix_v1_factsheets_sboms_ingest': Attach Software Bill of Materials (SBOM) to a Fact Sheet
          - 'leanix_v1_factsheets_sboms_ingest_1': Get the status of an SBOM ingestion job
          - 'getcomponentsbyapplication': Retrieve library components for a business application
          - 'searchcomponentsbypurl': Search components by PURL
          - 'getalltechstacks': Retrieve all tech stacks
          - 'updatetechstackbyqueryparam': Update an existing custom tech stack
          - 'createtechstack': Create a new custom tech stack
          - 'deletetechstackbyqueryparam': Delete a custom tech stack
          - 'previewmatches': Preview tech stack rule matches
          - 'gettechstackdetailsbyqueryparam': Get tech stack details
          - 'getaggregatedcounts': Get aggregated tech stack counts
          - 'getfactsheetsbylibrary': Get fact sheets using a specific library
          - 'getlibraryusagedetails': Get detailed library usage information
          - 'getversionsbylibrary': Get library versions by library name
          - 'getlibraries': Retrieve libraries with aggregated counts
        """
        kwargs: dict[str, Any]
        if action == "leanix_v1_microservice_discovery_yaml_manifest_register":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.leanix_v1_microservice_discovery_yaml_manifest_register(
                **kwargs
            )
        if action == "leanix_v1_factsheets_sboms_ingest":
            kwargs = {"fact_sheet_id": fact_sheet_id, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.leanix_v1_factsheets_sboms_ingest(**kwargs)
        if action == "leanix_v1_factsheets_sboms_ingest_1":
            kwargs = {"job_id": job_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.leanix_v1_factsheets_sboms_ingest_1(**kwargs)
        if action == "getcomponentsbyapplication":
            kwargs = {"fact_sheet_id": fact_sheet_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getcomponentsbyapplication(**kwargs)
        if action == "searchcomponentsbypurl":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.searchcomponentsbypurl(**kwargs)
        if action == "getalltechstacks":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getalltechstacks(**kwargs)
        if action == "updatetechstackbyqueryparam":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updatetechstackbyqueryparam(**kwargs)
        if action == "createtechstack":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createtechstack(**kwargs)
        if action == "deletetechstackbyqueryparam":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletetechstackbyqueryparam(**kwargs)
        if action == "previewmatches":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.previewmatches(**kwargs)
        if action == "gettechstackdetailsbyqueryparam":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.gettechstackdetailsbyqueryparam(**kwargs)
        if action == "getaggregatedcounts":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getaggregatedcounts(**kwargs)
        if action == "getfactsheetsbylibrary":
            kwargs = {"library_id": library_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getfactsheetsbylibrary(**kwargs)
        if action == "getlibraryusagedetails":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getlibraryusagedetails(**kwargs)
        if action == "getversionsbylibrary":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getversionsbylibrary(**kwargs)
        if action == "getlibraries":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getlibraries(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: leanix_v1_microservice_discovery_yaml_manifest_register', 'leanix_v1_factsheets_sboms_ingest', 'leanix_v1_factsheets_sboms_ingest_1', 'getcomponentsbyapplication', 'searchcomponentsbypurl', 'getalltechstacks', 'updatetechstackbyqueryparam', 'createtechstack', 'deletetechstackbyqueryparam', 'previewmatches', 'gettechstackdetailsbyqueryparam', 'getaggregatedcounts', 'getfactsheetsbylibrary', 'getlibraryusagedetails', 'getversionsbylibrary', 'getlibraries"
        )


def register_leanix_storage_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-storage"})
    async def leanix_leanix_storage(
        action: str = Field(
            description="Action to perform. Must be one of: 'getavatar', 'setavatar', 'deleteavatar', 'getlogo', 'setlogo', 'deletelogo', 'getfiles', 'addfiletoworkspace', 'deletefiles', 'getfile', 'deletefile', 'getfilecontent', 'setfileowner'"
        ),
        user_id: str | None = Field(default=None, description="user id"),
        workspace_id: str | None = Field(default=None, description="workspace id"),
        fact_sheet_id: str | None = Field(default=None, description="fact sheet id"),
        _workspace_id: str | None = Field(default=None, description=" workspace id"),
        file_id: str | None = Field(default=None, description="file id"),
        client=Depends(get_storage_client),
    ) -> dict:
        """Manage leanix storage operations.

        Actions:
          - 'getavatar': Retrieve a user's avatar
          - 'setavatar': Update a user's avatar
          - 'deleteavatar': Delete a user avatar
          - 'getlogo': Retrieve a fact sheet logo
          - 'setlogo': Assign a logo to a fact sheet
          - 'deletelogo': Delete a fact sheet logo
          - 'getfiles': Retrieve a list of workspace files
          - 'addfiletoworkspace': Upload a new file.
          - 'deletefiles': Delete workspace files
          - 'getfile': Retrieve workspace file
          - 'deletefile': Delete workspace file
          - 'getfilecontent': Retrieve workspace file contents
          - 'setfileowner': Update file owner
        """
        kwargs: dict[str, Any]
        if action == "getavatar":
            kwargs = {"user_id": user_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getavatar(**kwargs)
        if action == "setavatar":
            kwargs = {"user_id": user_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.setavatar(**kwargs)
        if action == "deleteavatar":
            kwargs = {"user_id": user_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deleteavatar(**kwargs)
        if action == "getlogo":
            kwargs = {
                "workspace_id": workspace_id,
                "fact_sheet_id": fact_sheet_id,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getlogo(**kwargs)
        if action == "setlogo":
            kwargs = {
                "workspace_id": workspace_id,
                "fact_sheet_id": fact_sheet_id,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.setlogo(**kwargs)
        if action == "deletelogo":
            kwargs = {
                "workspace_id": workspace_id,
                "fact_sheet_id": fact_sheet_id,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletelogo(**kwargs)
        if action == "getfiles":
            kwargs = {
                "_workspace_id": _workspace_id,
                "workspace_id": workspace_id,
            }
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getfiles(**kwargs)
        if action == "addfiletoworkspace":
            kwargs = {"workspace_id": workspace_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.addfiletoworkspace(**kwargs)
        if action == "deletefiles":
            kwargs = {"workspace_id": workspace_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletefiles(**kwargs)
        if action == "getfile":
            kwargs = {"workspace_id": workspace_id, "file_id": file_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getfile(**kwargs)
        if action == "deletefile":
            kwargs = {"workspace_id": workspace_id, "file_id": file_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletefile(**kwargs)
        if action == "getfilecontent":
            kwargs = {"workspace_id": workspace_id, "file_id": file_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getfilecontent(**kwargs)
        if action == "setfileowner":
            kwargs = {"workspace_id": workspace_id, "file_id": file_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.setfileowner(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: getavatar', 'setavatar', 'deleteavatar', 'getlogo', 'setlogo', 'deletelogo', 'getfiles', 'addfiletoworkspace', 'deletefiles', 'getfile', 'deletefile', 'getfilecontent', 'setfileowner"
        )


def register_leanix_survey_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-survey"})
    async def leanix_leanix_survey(
        action: str = Field(
            description="Action to perform. Must be one of: 'get_poll', 'update_poll', 'delete_poll_by_id', 'get_poll_run_by_id', 'update_poll_run', 'delete_poll_run', 'update_poll_run_status', 'get_poll_result', 'update_poll_result', 'get_polls', 'create_poll', 'get_poll_runs', 'create_poll_run', 'create_poll_reminder', 'check_for_new_fact_sheets', 'replay_all_workspaces', 'replay_workspace_by_id', 'get_polls_for_fact_sheet', 'get_recipients_and_fact_sheets_for_poll', 'get_poll_runs_by_poll', 'get_poll_count', 'get_all_templates', 'get_templates_by_id', 'get_poll_results_for_user', 'get_all_reminders_for_poll_run', 'get_recipients_and_fact_sheets_for_poll_run', 'getpollrunresultsasexcel', 'get_poll_results_by_poll_run_id', 'get_added_recipients_for_poll_run'"
        ),
        poll_id: str | None = Field(default=None, description="poll id"),
        data: dict | None = Field(default=None, description="data"),
        poll_run_id: str | None = Field(default=None, description="poll run id"),
        poll_result_id: str | None = Field(default=None, description="poll result id"),
        workspace_id: str | None = Field(default=None, description="workspace id"),
        fact_sheet_id: str | None = Field(default=None, description="fact sheet id"),
        poll_template_id: str | None = Field(
            default=None, description="poll template id"
        ),
        user_id: str | None = Field(default=None, description="user id"),
        client=Depends(get_survey_client),
    ) -> dict:
        """Manage leanix survey operations.

        Actions:
          - 'get_poll': get_poll
          - 'update_poll': update_poll
          - 'delete_poll_by_id': delete_poll_by_id
          - 'get_poll_run_by_id': get_poll_run_by_id
          - 'update_poll_run': update_poll_run
          - 'delete_poll_run': delete_poll_run
          - 'update_poll_run_status': update_poll_run_status
          - 'get_poll_result': get_poll_result
          - 'update_poll_result': update_poll_result
          - 'get_polls': get_polls
          - 'create_poll': create_poll
          - 'get_poll_runs': get_poll_runs
          - 'create_poll_run': create_poll_run
          - 'create_poll_reminder': create_poll_reminder
          - 'check_for_new_fact_sheets': check_for_new_fact_sheets
          - 'replay_all_workspaces': replay_all_workspaces
          - 'replay_workspace_by_id': replay_workspace_by_id
          - 'get_polls_for_fact_sheet': get_polls_for_fact_sheet
          - 'get_recipients_and_fact_sheets_for_poll': get_recipients_and_fact_sheets_for_poll
          - 'get_poll_runs_by_poll': get_poll_runs_by_poll
          - 'get_poll_count': get_poll_count
          - 'get_all_templates': get_all_templates
          - 'get_templates_by_id': get_templates_by_id
          - 'get_poll_results_for_user': get_poll_results_for_user
          - 'get_all_reminders_for_poll_run': get_all_reminders_for_poll_run
          - 'get_recipients_and_fact_sheets_for_poll_run': get_recipients_and_fact_sheets_for_poll_run
          - 'getpollrunresultsasexcel': Call GET /pollRuns/{poll_run_id}/pollResults.xlsx
          - 'get_poll_results_by_poll_run_id': get_poll_results_by_poll_run_id
          - 'get_added_recipients_for_poll_run': get_added_recipients_for_poll_run
        """
        kwargs: dict[str, Any]
        if action == "get_poll":
            kwargs = {"poll_id": poll_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_poll(**kwargs)
        if action == "update_poll":
            kwargs = {"poll_id": poll_id, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_poll(**kwargs)
        if action == "delete_poll_by_id":
            kwargs = {"poll_id": poll_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_poll_by_id(**kwargs)
        if action == "get_poll_run_by_id":
            kwargs = {"poll_run_id": poll_run_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_poll_run_by_id(**kwargs)
        if action == "update_poll_run":
            kwargs = {"poll_run_id": poll_run_id, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_poll_run(**kwargs)
        if action == "delete_poll_run":
            kwargs = {"poll_run_id": poll_run_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.delete_poll_run(**kwargs)
        if action == "update_poll_run_status":
            kwargs = {"poll_run_id": poll_run_id, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_poll_run_status(**kwargs)
        if action == "get_poll_result":
            kwargs = {"poll_result_id": poll_result_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_poll_result(**kwargs)
        if action == "update_poll_result":
            kwargs = {"poll_result_id": poll_result_id, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.update_poll_result(**kwargs)
        if action == "get_polls":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_polls(**kwargs)
        if action == "create_poll":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_poll(**kwargs)
        if action == "get_poll_runs":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_poll_runs(**kwargs)
        if action == "create_poll_run":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_poll_run(**kwargs)
        if action == "create_poll_reminder":
            kwargs = {"poll_run_id": poll_run_id, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.create_poll_reminder(**kwargs)
        if action == "check_for_new_fact_sheets":
            kwargs = {"poll_run_id": poll_run_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.check_for_new_fact_sheets(**kwargs)
        if action == "replay_all_workspaces":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.replay_all_workspaces(**kwargs)
        if action == "replay_workspace_by_id":
            kwargs = {"workspace_id": workspace_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.replay_workspace_by_id(**kwargs)
        if action == "get_polls_for_fact_sheet":
            kwargs = {"fact_sheet_id": fact_sheet_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_polls_for_fact_sheet(**kwargs)
        if action == "get_recipients_and_fact_sheets_for_poll":
            kwargs = {"poll_id": poll_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_recipients_and_fact_sheets_for_poll(**kwargs)
        if action == "get_poll_runs_by_poll":
            kwargs = {"poll_id": poll_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_poll_runs_by_poll(**kwargs)
        if action == "get_poll_count":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_poll_count(**kwargs)
        if action == "get_all_templates":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_all_templates(**kwargs)
        if action == "get_templates_by_id":
            kwargs = {"poll_template_id": poll_template_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_templates_by_id(**kwargs)
        if action == "get_poll_results_for_user":
            kwargs = {"poll_run_id": poll_run_id, "user_id": user_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_poll_results_for_user(**kwargs)
        if action == "get_all_reminders_for_poll_run":
            kwargs = {"poll_run_id": poll_run_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_all_reminders_for_poll_run(**kwargs)
        if action == "get_recipients_and_fact_sheets_for_poll_run":
            kwargs = {"poll_run_id": poll_run_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_recipients_and_fact_sheets_for_poll_run(**kwargs)
        if action == "getpollrunresultsasexcel":
            kwargs = {"poll_run_id": poll_run_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getpollrunresultsasexcel(**kwargs)
        if action == "get_poll_results_by_poll_run_id":
            kwargs = {"poll_run_id": poll_run_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_poll_results_by_poll_run_id(**kwargs)
        if action == "get_added_recipients_for_poll_run":
            kwargs = {"poll_run_id": poll_run_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get_added_recipients_for_poll_run(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: get_poll', 'update_poll', 'delete_poll_by_id', 'get_poll_run_by_id', 'update_poll_run', 'delete_poll_run', 'update_poll_run_status', 'get_poll_result', 'update_poll_result', 'get_polls', 'create_poll', 'get_poll_runs', 'create_poll_run', 'create_poll_reminder', 'check_for_new_fact_sheets', 'replay_all_workspaces', 'replay_workspace_by_id', 'get_polls_for_fact_sheet', 'get_recipients_and_fact_sheets_for_poll', 'get_poll_runs_by_poll', 'get_poll_count', 'get_all_templates', 'get_templates_by_id', 'get_poll_results_for_user', 'get_all_reminders_for_poll_run', 'get_recipients_and_fact_sheets_for_poll_run', 'getpollrunresultsasexcel', 'get_poll_results_by_poll_run_id', 'get_added_recipients_for_poll_run"
        )


def register_leanix_synclog_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-synclog"})
    async def leanix_leanix_synclog(
        action: str = Field(
            description="Action to perform. Must be one of: 'getsyncitems', 'addsyncitembatch', 'getsynchronizations', 'createsynchronization', 'getsyncitems_1', 'deletesyncitems', 'getsynchronization', 'updatesynchronization', 'gettopics', 'gettriggers', 'requestabortion'"
        ),
        id_: str | None = Field(default=None, description="id "),
        data: dict | None = Field(default=None, description="data"),
        client=Depends(get_synclog_client),
    ) -> dict:
        """Manage leanix synclog operations.

        Actions:
          - 'getsyncitems': Query for Synchronization Items
          - 'addsyncitembatch': Add new Sync Items into a Synchronization
          - 'getsynchronizations': List Synchronizations
          - 'createsynchronization': Creates a new Synchronization
          - 'getsyncitems_1': List all Sync Items of a Synchronization
          - 'deletesyncitems': Delete all Sync Items of a Synchronization
          - 'getsynchronization': Provide a Synchronization by its id
          - 'updatesynchronization': Update a Synchronization
          - 'gettopics': List all possible topics for a given workspace
          - 'gettriggers': List all possible triggers for a given workspace
          - 'requestabortion': Requests a synchronization run to cancel
        """
        kwargs: dict[str, Any]
        if action == "getsyncitems":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsyncitems(**kwargs)
        if action == "addsyncitembatch":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.addsyncitembatch(**kwargs)
        if action == "getsynchronizations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsynchronizations(**kwargs)
        if action == "createsynchronization":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createsynchronization(**kwargs)
        if action == "getsyncitems_1":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsyncitems_1(**kwargs)
        if action == "deletesyncitems":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletesyncitems(**kwargs)
        if action == "getsynchronization":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsynchronization(**kwargs)
        if action == "updatesynchronization":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updatesynchronization(**kwargs)
        if action == "gettopics":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.gettopics(**kwargs)
        if action == "gettriggers":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.gettriggers(**kwargs)
        if action == "requestabortion":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.requestabortion(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: getsyncitems', 'addsyncitembatch', 'getsynchronizations', 'createsynchronization', 'getsyncitems_1', 'deletesyncitems', 'getsynchronization', 'updatesynchronization', 'gettopics', 'gettriggers', 'requestabortion"
        )


def register_leanix_todo_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-todo"})
    async def leanix_leanix_todo(
        action: str = Field(
            description="Action to perform. Must be one of: 'managedrestorationrequests', 'managedsnapshotrequests', 'accepttodo', 'assigntome', 'get', 'createtodo', 'deletetodos', 'query', 'rejecttodo', 'replyandclosetodo', 'upserttodos'"
        ),
        data: dict | None = Field(default=None, description="data"),
        todo_id: str | None = Field(default=None, description="todo id"),
        client=Depends(get_todo_client),
    ) -> dict:
        """Manage leanix todo operations.

        Actions:
          - 'managedrestorationrequests': Trigger the snapshot restore of the To-Dos of a workspace
          - 'managedsnapshotrequests': Trigger the snapshotting of the To-Dos of a workspace
          - 'accepttodo': Import and/or Link an Application into this workspace, connecting it to SI to receive nightly data updates. Set the resolution to accepted of a to-do with type 'Link' or 'Import' and set the to-do state to closed. The calling user will also be assigned as the Owner of this to-do.
          - 'assigntome': Assign yourself as the to-do owner of this to-do and set it to in progress
          - 'get': Get to-dos on your workspace
          - 'createtodo': Create a to-do
          - 'deletetodos': Delete to-dos that match the given query body on a workspace
          - 'query': Get all to-dos matching a query of a specific workspace
          - 'rejecttodo': Set the resolution to rejected of a to-do with type 'Link' or 'Import' or 'Answer' or 'Approval' and set the to-do state to closed. the calling user will also be assigned as the Owner of this to-do.
          - 'replyandclosetodo': Add a reply to the question in the to-do with type 'Answer' and set the to-do state to closed. The reply is also added as a reply to the comment thread created by this to-do in the related base fact sheet.
          - 'upserttodos': Upsert to-dos
        """
        kwargs: dict[str, Any]
        if action == "managedrestorationrequests":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.managedrestorationrequests(**kwargs)
        if action == "managedsnapshotrequests":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.managedsnapshotrequests(**kwargs)
        if action == "accepttodo":
            kwargs = {"todo_id": todo_id, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.accepttodo(**kwargs)
        if action == "assigntome":
            kwargs = {"todo_id": todo_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.assigntome(**kwargs)
        if action == "get":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.get(**kwargs)
        if action == "createtodo":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createtodo(**kwargs)
        if action == "deletetodos":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletetodos(**kwargs)
        if action == "query":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.query(**kwargs)
        if action == "rejecttodo":
            kwargs = {"todo_id": todo_id, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.rejecttodo(**kwargs)
        if action == "replyandclosetodo":
            kwargs = {"todo_id": todo_id, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.replyandclosetodo(**kwargs)
        if action == "upserttodos":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.upserttodos(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: managedrestorationrequests', 'managedsnapshotrequests', 'accepttodo', 'assigntome', 'get', 'createtodo', 'deletetodos', 'query', 'rejecttodo', 'replyandclosetodo', 'upserttodos"
        )


def register_leanix_transformations_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-transformations"})
    async def leanix_leanix_transformations(
        action: str = Field(
            description="Action to perform. Must be one of: 'createtransformation', 'gettransformations', 'gettransformation', 'puttransformation', 'deletetransformation', 'gettransformationcustomimpacts', 'posttransformationcustomimpacts', 'puttransformationcustomimpacts', 'deletetransformationcustomimpacts', 'posttransformationexecution', 'posttransformationsexecution'"
        ),
        data: dict | None = Field(default=None, description="data"),
        id_: str | None = Field(default=None, description="id "),
        impact_id: str | None = Field(default=None, description="impact id"),
        client=Depends(get_transformations_client),
    ) -> dict:
        """Manage leanix transformations operations.

        Actions:
          - 'createtransformation': Creates a transformation
          - 'gettransformations': Returns a list of transformations
          - 'gettransformation': Returns a single transformation by id
          - 'puttransformation': Updates a transformation
          - 'deletetransformation': Deletes a single transformation by id
          - 'gettransformationcustomimpacts': Returns a list of all custom impacts belonging to a transformation
          - 'posttransformationcustomimpacts': Creates a custom impact on that transformation
          - 'puttransformationcustomimpacts': Updates a custom impact on that transformation
          - 'deletetransformationcustomimpacts': Deletes a custom impact on that transformation by id
          - 'posttransformationexecution': Materializes the changes of the transformation in the workspaces inventory
          - 'posttransformationsexecution': Materializes the changes of multiple transformations in the workspaces inventory
        """
        kwargs: dict[str, Any]
        if action == "createtransformation":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createtransformation(**kwargs)
        if action == "gettransformations":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.gettransformations(**kwargs)
        if action == "gettransformation":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.gettransformation(**kwargs)
        if action == "puttransformation":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.puttransformation(**kwargs)
        if action == "deletetransformation":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletetransformation(**kwargs)
        if action == "gettransformationcustomimpacts":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.gettransformationcustomimpacts(**kwargs)
        if action == "posttransformationcustomimpacts":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.posttransformationcustomimpacts(**kwargs)
        if action == "puttransformationcustomimpacts":
            kwargs = {"id_": id_, "impact_id": impact_id, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.puttransformationcustomimpacts(**kwargs)
        if action == "deletetransformationcustomimpacts":
            kwargs = {"id_": id_, "impact_id": impact_id}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletetransformationcustomimpacts(**kwargs)
        if action == "posttransformationexecution":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.posttransformationexecution(**kwargs)
        if action == "posttransformationsexecution":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.posttransformationsexecution(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: createtransformation', 'gettransformations', 'gettransformation', 'puttransformation', 'deletetransformation', 'gettransformationcustomimpacts', 'posttransformationcustomimpacts', 'puttransformationcustomimpacts', 'deletetransformationcustomimpacts', 'posttransformationexecution', 'posttransformationsexecution"
        )


def register_leanix_webhooks_tools(mcp: FastMCP):
    @mcp.tool(tags={"leanix-webhooks"})
    async def leanix_leanix_webhooks(
        action: str = Field(
            description="Action to perform. Must be one of: 'getcustomeventtags', 'createcustomeventtag', 'updatecustomeventtag', 'deletecustomeventtag', 'createevent', 'createeventbatch', 'geteventtags', 'getsubscriptions', 'createsubscription', 'getsubscription', 'updatesubscription', 'deletesubscription', 'getsubscriptiondeliveries', 'getsubscriptionevents', 'getsubscriptionstatus', 'getsubscriptionstatuses', 'updatesubscriptioncursor'"
        ),
        data: dict | None = Field(default=None, description="data"),
        id_: str | None = Field(default=None, description="id "),
        client=Depends(get_webhooks_client),
    ) -> dict:
        """Manage leanix webhooks operations.

        Actions:
          - 'getcustomeventtags': Get custom event tags with an identifier for the given workspace and service.
          - 'createcustomeventtag': Create a custom event tag.
          - 'updatecustomeventtag': Update a custom event tag.
          - 'deletecustomeventtag': Delete a custom event tag.
          - 'createevent': Create a new event.
          - 'createeventbatch': Create a batch of new events.
          - 'geteventtags': Get all event tags for the given workspace.
          - 'getsubscriptions': Get all subscriptions.
          - 'createsubscription': Create a new subscription.
          - 'getsubscription': Get a subscription by id.
          - 'updatesubscription': Update a subscription by id.
          - 'deletesubscription': Delete a subscription by id.
          - 'getsubscriptiondeliveries': Get the deliveries of a given subscription.
          - 'getsubscriptionevents': Get the next batch of events for a PULL subscription.
          - 'getsubscriptionstatus': Get subscription status by subscription id.
          - 'getsubscriptionstatuses': Get subscription statuses for all subscriptions.
          - 'updatesubscriptioncursor': Marks events up to the given offset as consumed for the given subscription.
        """
        kwargs: dict[str, Any]
        if action == "getcustomeventtags":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getcustomeventtags(**kwargs)
        if action == "createcustomeventtag":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createcustomeventtag(**kwargs)
        if action == "updatecustomeventtag":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updatecustomeventtag(**kwargs)
        if action == "deletecustomeventtag":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletecustomeventtag(**kwargs)
        if action == "createevent":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createevent(**kwargs)
        if action == "createeventbatch":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createeventbatch(**kwargs)
        if action == "geteventtags":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.geteventtags(**kwargs)
        if action == "getsubscriptions":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsubscriptions(**kwargs)
        if action == "createsubscription":
            kwargs = {"data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.createsubscription(**kwargs)
        if action == "getsubscription":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsubscription(**kwargs)
        if action == "updatesubscription":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updatesubscription(**kwargs)
        if action == "deletesubscription":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.deletesubscription(**kwargs)
        if action == "getsubscriptiondeliveries":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsubscriptiondeliveries(**kwargs)
        if action == "getsubscriptionevents":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsubscriptionevents(**kwargs)
        if action == "getsubscriptionstatus":
            kwargs = {"id_": id_}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsubscriptionstatus(**kwargs)
        if action == "getsubscriptionstatuses":
            kwargs = {}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.getsubscriptionstatuses(**kwargs)
        if action == "updatesubscriptioncursor":
            kwargs = {"id_": id_, "data": data}
            kwargs = {k: v for k, v in kwargs.items() if v is not None}
            return client.updatesubscriptioncursor(**kwargs)
        raise ValueError(
            f"Unknown action: {action}. Must be one of: getcustomeventtags', 'createcustomeventtag', 'updatecustomeventtag', 'deletecustomeventtag', 'createevent', 'createeventbatch', 'geteventtags', 'getsubscriptions', 'createsubscription', 'getsubscription', 'updatesubscription', 'deletesubscription', 'getsubscriptiondeliveries', 'getsubscriptionevents', 'getsubscriptionstatus', 'getsubscriptionstatuses', 'updatesubscriptioncursor"
        )


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
