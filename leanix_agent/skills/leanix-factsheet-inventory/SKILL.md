---
name: leanix-factsheet-inventory
skill_type: skill
description: >-
  Read and maintain the LeanIX enterprise-architecture inventory: list and read
  FactSheets, create, update, relate and archive them, read the data model, bookmarks,
  exports, access control and settings through Pathfinder, browse reference data and its
  catalog, and read data-quality and AI inventory-builder results. Use when the agent must
  browse, triage or change FactSheets and their relations. Do NOT use for free-form
  GraphQL (leanix-graphql-query), planning (leanix-transformation-planning) or graph
  mirroring (leanix-kg-ingestion).
license: MIT
tags: [leanix, enterprise-architecture, factsheet, inventory, pathfinder, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# LeanIX FactSheet Inventory

A FactSheet is one inventory record: an application, IT component, business capability, data object, interface, provider or project. Pathfinder is the REST service that reads and writes them; reference data supplies the external catalog of technologies and categories they link to.

## When to use
- List FactSheets by type with cursor paging and read one by id.
- Create, update, relate and archive FactSheets through the Pathfinder tools.
- Read the data model, view model, bookmarks, exports, features and access-control entities.
- Look up reference data sources, recommendations and the catalog.
- Read data-quality recommendations and AI inventory-builder pipelines.
- Send a raw request when no typed tool covers an endpoint.

## When NOT to use
- Free-form traversals: use leanix-graphql-query.
- Transformations, surveys and impact analysis: use leanix-transformation-planning.
- Mirroring FactSheets into the graph: use leanix-kg-ingestion.

## Workflow
1. Read the meta-model if the FactSheet type or field names are not certain.
2. List with the type filter and page with the returned cursor; read one FactSheet by id before changing it.
3. Make one change, then read the FactSheet and its relations back.
4. Report the id, type and the fields that changed.

## Safety
- Archiving a FactSheet removes it from every view; ask first and name it.
- Data-model and access-control updates affect the whole workspace; ask first.
- Prefer a typed tool over the raw request tools whenever one exists.

## Tools (152)

Each tool is one API operation; pass its path, query and body fields as named arguments.


### Ai Inventory Builder

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_ai_inventory_builder_getpipeline` | GET | Get a pipeline by id |
| `leanix_leanix_ai_inventory_builder_getpipelinefile` | GET | Get file from a pipeline |
| `leanix_leanix_ai_inventory_builder_getpipelines` | GET | Get all pipelines |
| `leanix_leanix_ai_inventory_builder_getpipelinesuggestions` | GET | Get suggestions from a pipeline that has been analyzed |
| `leanix_leanix_ai_inventory_builder_healthcheck` | GET | Healthcheck endpoint |
| `leanix_leanix_ai_inventory_builder_pipelines` | POST | Create a Pipeline |
| `leanix_leanix_ai_inventory_builder_sendpipelineaction` | POST | Send action to a pipeline |
| `leanix_leanix_ai_inventory_builder_admindeletepipeline` | DELETE | Delete a pipeline by id (any status) |
| `leanix_leanix_ai_inventory_builder_deletefailedpipelines` | DELETE | Deletes all failed pipelines and their files |
| `leanix_leanix_ai_inventory_builder_deletepipeline` | DELETE | Delete a pipeline by id |

### Factsheets

| Tool | Method | Purpose |
|---|---|---|
| `leanix_get_factsheet` | GET | Read one FactSheet by id |
| `leanix_get_factsheets` | GET | List FactSheets with type filter and cursor paging |

### Inventory Data Quality

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_inventory_data_quality_getdatamodel` | GET | Call GET /api/v1/datamodel |
| `leanix_leanix_inventory_data_quality_getfactsheettypes` | GET | Call GET /api/v1/datamodel/factsheet-types |
| `leanix_leanix_inventory_data_quality_getrecommendationsagenttobc` | POST | Get Agent to BC recommendations |
| `leanix_leanix_inventory_data_quality_getrecommendationsapptobc` | POST | Get App to BC recommendations |
| `leanix_leanix_inventory_data_quality_getrelationnames` | GET | Call GET /api/v1/datamodel/relation-names |
| `leanix_leanix_inventory_data_quality_refreshembeddings` | POST | Refresh embeddings |
| `leanix_leanix_inventory_data_quality_submitdqicardfeedback` | POST | Submit DQI Card feedback |
| `leanix_leanix_inventory_data_quality_submitfeedback` | POST | Submit feedback |
| `leanix_leanix_inventory_data_quality_submitfeedback_1` | POST | Submit feedback |

### Pathfinder

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_pathfinder_download_asset` | GET | download_asset |
| `leanix_leanix_pathfinder_download_export_file` | GET | download_export_file |
| `leanix_leanix_pathfinder_get_access_control_entities` | GET | get_access_control_entities |
| `leanix_leanix_pathfinder_get_access_control_entity` | GET | get_access_control_entity |
| `leanix_leanix_pathfinder_get_action_batch` | GET | get action batch |
| `leanix_leanix_pathfinder_get_action_batches` | GET | get action batches |
| `leanix_leanix_pathfinder_get_all_versions_for_bookmark` | GET | get_all_versions_for_bookmark |
| `leanix_leanix_pathfinder_get_authorization` | GET | get authorization |
| `leanix_leanix_pathfinder_get_bookmark` | GET | get_bookmark |
| `leanix_leanix_pathfinder_get_bookmark_shares` | GET | get_bookmark_shares |
| `leanix_leanix_pathfinder_get_bookmarks` | GET | get_bookmarks |
| `leanix_leanix_pathfinder_get_data_model` | GET | get_data_model |
| `leanix_leanix_pathfinder_get_enriched_data_model` | GET | get_enriched_data_model |
| `leanix_leanix_pathfinder_get_exports` | GET | get_exports |
| `leanix_leanix_pathfinder_get_fact_sheet` | GET | get_fact_sheet |
| `leanix_leanix_pathfinder_get_fact_sheet_hierarchy` | GET | get_fact_sheet_hierarchy |
| `leanix_leanix_pathfinder_get_fact_sheet_relations` | GET | get_fact_sheet_relations |
| `leanix_leanix_pathfinder_get_fact_sheet_resource_model` | GET | get fact sheet resource model |
| `leanix_leanix_pathfinder_get_fact_sheets` | GET | get_fact_sheets |
| `leanix_leanix_pathfinder_get_feature` | GET | get_feature |
| `leanix_leanix_pathfinder_get_features` | GET | get_features |
| `leanix_leanix_pathfinder_get_language` | GET | get language |
| `leanix_leanix_pathfinder_get_meta_model` | GET | get meta model |
| `leanix_leanix_pathfinder_get_meta_model_actions` | GET | get meta model actions |
| `leanix_leanix_pathfinder_get_meta_model_actions_audit_log` | GET | get meta model actions audit log |
| `leanix_leanix_pathfinder_get_meta_model_actions_for_node` | GET | get meta model actions for node |
| `leanix_leanix_pathfinder_get_meta_model_authorization` | GET | get meta model authorization |
| `leanix_leanix_pathfinder_get_meta_model_for_type` | GET | get meta model for type |
| `leanix_leanix_pathfinder_get_meta_model_job` | GET | get meta model job |
| `leanix_leanix_pathfinder_get_meta_model_permission_roles` | GET | get meta model permission roles |
| `leanix_leanix_pathfinder_get_meta_model_root` | GET | get meta model root |
| `leanix_leanix_pathfinder_get_model_customization` | GET | get model customization |
| `leanix_leanix_pathfinder_get_preview_of_affected_data` | GET | get preview of affected data |
| `leanix_leanix_pathfinder_get_reporting_model` | GET | get reporting model |
| `leanix_leanix_pathfinder_get_settings` | GET | get settings |
| `leanix_leanix_pathfinder_get_suggestions` | GET | get suggestions |
| `leanix_leanix_pathfinder_get_view_model` | GET | get view model |
| `leanix_leanix_pathfinder_create_access_control_entity` | POST | create_access_control_entity |
| `leanix_leanix_pathfinder_create_bookmark` | POST | create_bookmark |
| `leanix_leanix_pathfinder_create_bookmark_shares` | POST | create_bookmark_shares |
| `leanix_leanix_pathfinder_create_fact_sheet` | POST | create_fact_sheet |
| `leanix_leanix_pathfinder_create_fact_sheet_relation` | POST | create_fact_sheet_relation |
| `leanix_leanix_pathfinder_create_full_export` | POST | create_full_export |
| `leanix_leanix_pathfinder_post_action_batches` | POST | post action batches |
| `leanix_leanix_pathfinder_post_meta_model_actions` | POST | post meta model actions |
| `leanix_leanix_pathfinder_process_graph_ql` | POST | process_graph_ql |
| `leanix_leanix_pathfinder_process_graph_ql_multipart` | POST | process_graph_ql_multipart |
| `leanix_leanix_pathfinder_update_feature` | POST | update_feature |
| `leanix_leanix_pathfinder_upsert_asset` | POST | upsert_asset |
| `leanix_leanix_pathfinder_change_bookmark_owner` | PATCH | change_bookmark_owner |
| `leanix_leanix_pathfinder_update_access_control_entity` | PUT | update_access_control_entity |
| `leanix_leanix_pathfinder_update_authorization` | PUT | update authorization |
| `leanix_leanix_pathfinder_update_bookmark` | PUT | update_bookmark |
| `leanix_leanix_pathfinder_update_data_model` | PUT | update_data_model |
| `leanix_leanix_pathfinder_update_fact_sheet` | PUT | update_fact_sheet |
| `leanix_leanix_pathfinder_update_fact_sheet_relation` | PUT | update_fact_sheet_relation |
| `leanix_leanix_pathfinder_update_fact_sheet_resource_model` | PUT | update fact sheet resource model |
| `leanix_leanix_pathfinder_update_language` | PUT | update language |
| `leanix_leanix_pathfinder_update_models_with_customization` | PUT | update models with customization |
| `leanix_leanix_pathfinder_update_reporting_model` | PUT | update reporting model |
| `leanix_leanix_pathfinder_update_settings` | PUT | update settings |
| `leanix_leanix_pathfinder_update_view_model` | PUT | update view model |
| `leanix_leanix_pathfinder_archive_fact_sheet` | DELETE | archive_fact_sheet |
| `leanix_leanix_pathfinder_delete_access_control_entity` | DELETE | delete_access_control_entity |
| `leanix_leanix_pathfinder_delete_asset` | DELETE | delete_asset |
| `leanix_leanix_pathfinder_delete_bookmark` | DELETE | delete_bookmark |
| `leanix_leanix_pathfinder_delete_bookmark_shares` | DELETE | delete_bookmark_shares |
| `leanix_leanix_pathfinder_delete_fact_sheet_relation` | DELETE | delete_fact_sheet_relation |

### Raw Requests

| Tool | Method | Purpose |
|---|---|---|
| `leanix_request_api` | POST | Send one raw request to a LeanIX service for an endpoint no typed tool covers |
| `leanix_rest_api` | POST | Send one workspace-scoped request to any configured LeanIX service, mutating only when allowed |

### Reference Data

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_reference_data_fetchbusinesscapabilitymetrics` | POST | Endpoint to fetch the Business Capability Metrics |
| `leanix_leanix_reference_data_get_jobs` | GET | The endpoint to retrieve the created async processing jobs. |
| `leanix_leanix_reference_data_get_source_name_fact_sheets_id` | GET | Get Fact Sheet by source name, and by Fact Sheet id |
| `leanix_leanix_reference_data_getbuscapconfiguration` | GET | Get the configuration for your source workspace |
| `leanix_leanix_reference_data_getbusinesscapability` | GET | Fetch hierarchy for queried industry |
| `leanix_leanix_reference_data_getconfiguration` | GET | Get the configuration for your source workspace |
| `leanix_leanix_reference_data_getconfigurationmodels` | GET | Get the view model, data model and translation model from the source workspace |
| `leanix_leanix_reference_data_getexportfile` | GET | Get the Excel file path for the run_id |
| `leanix_leanix_reference_data_getexportstatus` | GET | Get the status of export for the run_id |
| `leanix_leanix_reference_data_getfactsheetsbysourcename` | GET | Get Fact Sheets by source name |
| `leanix_leanix_reference_data_getlatestrecommendationrun` | GET | Fetches the latest recommendation run for a workspace |
| `leanix_leanix_reference_data_getlink` | GET | Get the missing request for this Fact Sheet in the target workspace by source name |
| `leanix_leanix_reference_data_getlinkbysourcename` | GET | Get the unique link to a Fact Sheet of the Fact Sheet in the target workspace by source name |
| `leanix_leanix_reference_data_getlinks` | GET | Get the IDs of workspaces with existing links by source name |
| `leanix_leanix_reference_data_getlinksbyfactsheettype` | GET | Get links based on factsheet type |
| `leanix_leanix_reference_data_getlinksbysourcename` | GET | Get existing links to your workspace by source name |
| `leanix_leanix_reference_data_getprovisioning` | GET | Get information about the provisioning status of the data model and the translation model of your workspace |
| `leanix_leanix_reference_data_getrefresh` | GET | Get the refresh of your workspace by source name |
| `leanix_leanix_reference_data_getrefreshes` | GET | Get all the refreshes of your workspace by source name |
| `leanix_leanix_reference_data_getrequests` | POST | Get requests of your workspace by source name |
| `leanix_leanix_reference_data_getrequestscount` | POST | Get the count of different types of requests for a workspace |
| `leanix_leanix_reference_data_getsaasconfiguration` | GET | Get the configuration for your source workspace |
| `leanix_leanix_reference_data_gettbmmigrationstatus` | POST | Get status of tbm migration cron job. |
| `leanix_leanix_reference_data_gettbmtaxonomy` | GET | Get TBM Taxonomy |
| `leanix_leanix_reference_data_gettechcategoryconfiguration` | GET | Get the configuration for your source workspace |
| `leanix_leanix_reference_data_getusedtechnolotrecommendationcontroller` | POST | Get entries of Technolot recommendations used by LTLS by workspace_ids/LTLS FactSheet Ids |
| `leanix_leanix_reference_data_validatelink` | GET | Validates the details of link |
| `leanix_leanix_reference_data_batchlinks` | POST | Fetches Catalog links and suggestions in batches |
| `leanix_leanix_reference_data_clearduplicatelinks` | POST | Clears Duplicate Links in reference-data for a workspace |
| `leanix_leanix_reference_data_clonelinks` | POST | Clones a link to your workspace by source name |
| `leanix_leanix_reference_data_filteredfactsheetscount` | POST | Endpoint to fetch the precomputed recommendations |
| `leanix_leanix_reference_data_post_jobs` | POST | The endpoint creates a job for asynchronous processing. |
| `leanix_leanix_reference_data_post_managedrestorationrequests` | POST | Endpoint to restore snapshots for workspaces |
| `leanix_leanix_reference_data_post_managedsnapshotrequests` | POST | Endpoint to create snapshots for workspace |
| `leanix_leanix_reference_data_postbusinesscapability` | POST | Endpoint to fetch business capability catalog factsheets for given ids and industry |
| `leanix_leanix_reference_data_postrefresh` | POST | Creates and asynchronously starts a refresh for your workspace. That refresh synchronizes all data of... |
| `leanix_leanix_reference_data_precomputedrecommendations` | POST | Endpoint to fetch the precomputed recommendations |
| `leanix_leanix_reference_data_putbulklinksbysourcename` | PUT | Inserts or updates a multiple links to your workspace by source name |
| `leanix_leanix_reference_data_putbulksourcehierarchylinkscontroller` | PUT | Inserts or updates a multiple links to your workspace by source name |
| `leanix_leanix_reference_data_putbuscapconfiguration` | PUT | Inserts or updates the configuration for your source workspace |
| `leanix_leanix_reference_data_putconfiguration` | PUT | Inserts or updates the configuration for your source workspace |
| `leanix_leanix_reference_data_putimporttbm` | PUT | Start automate import tbm in the workspace |
| `leanix_leanix_reference_data_putlinksbysourcename` | PUT | Inserts or updates a link to your workspace by source name |
| `leanix_leanix_reference_data_putprovisioning` | PUT | Trigger the provisioning for your workspace |
| `leanix_leanix_reference_data_putrequests` | PUT | Inserts or updates a missing request for your Fact Sheet by source name |
| `leanix_leanix_reference_data_putsaasconfiguration` | PUT | Inserts or updates the configuration for your source workspace |
| `leanix_leanix_reference_data_putsourcehierarchylinkcontroller` | PUT | Inserts or updates a link to your workspace |
| `leanix_leanix_reference_data_puttechcategoryconfiguration` | PUT | Inserts or updates the configuration for your source workspace |
| `leanix_leanix_reference_data_putusedtechnolotrecommendationcontroller` | PUT | Inserts entries of Technolot recommendations used by batch-linking |
| `leanix_leanix_reference_data_refreshltlslinks` | PUT | Updates the InternalId of LTLS Links if incorrect |
| `leanix_leanix_reference_data_startmappingexport` | PUT | Start the Excel export for the respective workspace, with details of possible new TBM mappings for existing... |
| `leanix_leanix_reference_data_tbmmigrationstatusupdate` | PUT | Put status of tbm migration cron job. |
| `leanix_leanix_reference_data_deletelinkbysourcename` | DELETE | Delete the unique link to a source Fact Sheet of the Fact Sheet in the target workspace |

### Reference Data Catalog

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_reference_data_catalog_get_items` | GET | Get catalog items. |
| `leanix_leanix_reference_data_catalog_get_items_id` | GET | Get catalog item by catalog id. |
| `leanix_leanix_reference_data_catalog_get_recommendations` | GET | Get catalog recommendations. |
| `leanix_leanix_reference_data_catalog_get_requests` | GET | Retrieves requests for missing catalog items. |
| `leanix_leanix_reference_data_catalog_post_links` | POST | Creates a catalog link. |
| `leanix_leanix_reference_data_catalog_post_requests` | POST | Creates a request for a missing catalog item. |
| `leanix_leanix_reference_data_catalog_post_requests_id_comments` | POST | Add a comment to a catalog request. |
| `leanix_leanix_reference_data_catalog_delete_links` | DELETE | Deletes a catalog link. |
