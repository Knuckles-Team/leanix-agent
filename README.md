# Leanix Agent
## CLI or API | MCP | Agent

![PyPI - Version](https://img.shields.io/pypi/v/leanix-agent)
![MCP Server](https://badge.mcpx.dev?type=server 'MCP Server')
![PyPI - Downloads](https://img.shields.io/pypi/dd/leanix-agent)
![GitHub Repo stars](https://img.shields.io/github/stars/Knuckles-Team/leanix-agent)
![GitHub forks](https://img.shields.io/github/forks/Knuckles-Team/leanix-agent)
![GitHub contributors](https://img.shields.io/github/contributors/Knuckles-Team/leanix-agent)
![PyPI - License](https://img.shields.io/pypi/l/leanix-agent)
![GitHub](https://img.shields.io/github/license/Knuckles-Team/leanix-agent)
![GitHub last commit (by committer)](https://img.shields.io/github/last-commit/Knuckles-Team/leanix-agent)
![GitHub pull requests](https://img.shields.io/github/issues-pr/Knuckles-Team/leanix-agent)
![GitHub closed pull requests](https://img.shields.io/github/issues-pr-closed/Knuckles-Team/leanix-agent)
![GitHub issues](https://img.shields.io/github/issues/Knuckles-Team/leanix-agent)
![GitHub top language](https://img.shields.io/github/languages/top/Knuckles-Team/leanix-agent)
![GitHub language count](https://img.shields.io/github/languages/count/Knuckles-Team/leanix-agent)
![GitHub repo size](https://img.shields.io/github/repo-size/Knuckles-Team/leanix-agent)
![GitHub repo file count (file type)](https://img.shields.io/github/directory-file-count/Knuckles-Team/leanix-agent)
![PyPI - Wheel](https://img.shields.io/pypi/wheel/leanix-agent)
![PyPI - Implementation](https://img.shields.io/pypi/implementation/leanix-agent)

*Version: 0.23.1*

---

## Table of Contents
- [Overview](#overview)
- [Key Features](#key-features)
- [CLI or API](#cli-or-api)
- [MCP](#mcp)
  - [Available MCP Tools](#available-mcp-tools)
  - [MCP Configuration Examples](#mcp-configuration-examples)
  - [Dynamic Tool Selection & Visibility](#dynamic-tool-selection--visibility)
- [Agent](#agent)
  - [Running the Agent CLI](#running-the-agent-cli)
  - [Docker Compose Orchestration](#docker-compose-orchestration)
- [Security & Governance](#security--governance)
- [Installation](#installation)
- [Contribute](#contribute)

---

## Overview

**Leanix Agent** is a production-grade Agent and Model Context Protocol (MCP) server designed to interface directly with Agent package for communicating with LeanIX Enterprise Architecture Management via REST APIs and GraphQL..

---

## Key Features

- **Consolidated Action-Routed MCP Tools:** Minimizes token overhead and eliminates tool bloat in LLM contexts by grouping methods into optimized, togglable tool modules.
- **Enterprise-Grade Security:** Comprehensive support for Eunomia policies, OIDC token delegation, and granular execution context tracking.
- **Integrated Graph Agent:** Built-in Pydantic AI agent supporting the Agent Control Protocol (ACP) and standard Web interfaces (AG-UI).
- **Native Telemetry & Tracing:** Out-of-the-box OpenTelemetry exports and native Langfuse tracing.

---

## CLI or API

This agent wraps the Agent package for communicating with LeanIX Enterprise Architecture Management via REST APIs and GraphQL. API. You can interact with it programmatically or via its integrated execution entrypoints.

Detailed instructions on how to use the underlying API wrappers, extended schema bindings, and developer SDK references are maintained in [docs/index.md](docs/index.md).

---

## MCP

This server utilizes dynamic Action-Routed tools to optimize token overhead and maximize IDE compatibility.

### Available MCP Tools
| Tool Module | Toggle Env Var | Enabled by Default | Description & Nested Methods |
|-------------|----------------|--------------------|------------------------------|
| **Leanix Ai Inventory Builder** | `LEANIX_AI_INVENTORY_BUILDER_TOOL` | `True` | Manage leanix leanix ai inventory builder operations. Action-routed methods: `admindeletepipeline`, `deletefailedpipelines`, `deletepipeline`, `getpipeline`, `getpipelinefile`, `getpipelines`, `getpipelinesuggestions`, `healthcheck`, `pipelines`, `sendpipelineaction`. |
| **Leanix Apptio Connector** | `LEANIX_APPTIO_CONNECTOR_TOOL` | `True` | Manage leanix leanix apptio connector operations. Action-routed methods: `create`, `deleteconfiguration`, `getallconfigurations`, `getconfigurations`, `getresults`, `getresultsurl`, `getstats`, `getstatus`, `getwarnings`, `upsertconfiguration`. |
| **Leanix Automations** | `LEANIX_AUTOMATIONS_TOOL` | `True` | Manage leanix leanix automations operations. Action-routed methods: `instancescontroller_findall`, `instancescontroller_quota`, `scriptscontroller_createmcescript`, `scriptscontroller_updatemcescript`, `snapshotscontroller_managedrestorationrequests`, `snapshotscontroller_managesnapshotrequests`, `statisticscontroller_getstatistics`, `templatescontroller_createtemplate`, `templatescontroller_deletetemplate`, `templatescontroller_getalltemplates`, `templatescontroller_gettemplate`, `templatescontroller_patchtemplate`, `templatescontroller_updatetemplate`. |
| **Leanix Reference Data Catalog** | `LEANIX_REFERENCE_DATA_CATALOG_TOOL` | `True` | Manage leanix leanix reference data catalog operations. Action-routed methods: `delete_links`, `get_items`, `get_items_id`, `get_recommendations`, `get_requests`, `post_links`, `post_requests`, `post_requests_id_comments`. |
| **Leanix Discovery Ai Agents** | `LEANIX_DISCOVERY_AI_AGENTS_TOOL` | `True` | Manage leanix leanix discovery ai agents operations. Action-routed methods: `get_integrations`, `get_integrations_id`, `post_agents_a2a_cards`, `post_integrations`, `put_integrations_id_capabilities`, `put_integrations_id_credentials`, `put_integrations_id_name`, `put_integrations_id_status`. |
| **Leanix Discovery Linking V1** | `LEANIX_DISCOVERY_LINKING_V1_TOOL` | `True` | Manage leanix leanix discovery linking v1 operations. Action-routed methods: `bulk_link`, `discovery_items`, `discovery_itemsfilter_options`, `discovery_itemsid`, `discovery_itemsidpre_validate_linkfactsheetid`, `discovery_itemskpi_values`, `discovery_itemslinking_progress`, `discovery_itemslinking_progressid`, `factsheetsiddetails`, `link`, `reject`. |
| **Leanix Discovery Linking V2** | `LEANIX_DISCOVERY_LINKING_V2_TOOL` | `True` | Manage leanix leanix discovery linking v2 operations. Action-routed methods: `get_factsheets_id_links`, `get_origin_discoveryitems`, `get_origin_discoveryitems_export`, `get_origin_discoveryitems_id`, `get_origin_discoveryitems_id_changelogs`, `get_origin_discoveryitems_linkingprogress`, `get_origin_discoveryitems_sourceconfigs`, `get_origin_insights`, `get_origin_internal_events`, `get_origin_internal_events_compaction`, `get_origin_settings`, `get_origin_settings_autolinking`, `post_origin_discoveryitems_id_preview`, `post_origin_push`, `post_origin_push_id`, `put_origin_discoveryitems_id_link`, `put_origin_discoveryitems_link`, `put_origin_discoveryitems_reject`, `put_origin_settings_autolinking`. |
| **Leanix Discovery Sap Extension** | `LEANIX_DISCOVERY_SAP_EXTENSION_TOOL` | `True` | Manage leanix leanix discovery sap extension operations. Action-routed methods: `delete_integrations_id_`, `get_check_data_model`, `get_checkdatamodel`, `get_cloud_foundry_domains`, `get_cloud_foundry_subject_pattern`, `get_credentials_type`, `get_health`, `get_integrations`, `get_kyma_spec_suggestions`, `patch_integrations_id`, `post_cloud_foundry_infer_certificate_domain`, `post_credentials_verify_cms`, `post_integrations`, `post_integrations_credentials_verify`, `post_integrations_id_sync`, `post_kyma_verify_api_url`, `put_integrations_id_credentials_build`, `put_integrations_id_credentials_cloud_foundry`, `put_integrations_id_credentials_cms`, `put_integrations_id_credentials_kyma`. |
| **Leanix Discovery Saas** | `LEANIX_DISCOVERY_SAAS_TOOL` | `True` | Manage leanix leanix discovery saas operations. Action-routed methods: `deleteintegrationbyid`, `getavailableintegrations`, `getdiscoveries`, `getdiscoveryprioritybyid`, `getintegrationbyid`, `getintegrations`, `postintegration`, `putintegrationcapabilitiesbyid`, `putintegrationcredentialsbyid`, `putintegrationnamebyid`, `putintegrationstatusbyid`. |
| **Leanix Documents** | `LEANIX_DOCUMENTS_TOOL` | `True` | Manage leanix leanix documents operations. Action-routed methods: `createdocuments`, `createtemplatecomponents`, `createtemplates`, `deletedocumentbyid`, `deletetemplate`, `deletetemplatecomponent`, `getdocumentbyid`, `getdocumentcomponents`, `getdocumentscount`, `getdocumentspaginated`, `gettemplatebyid`, `gettemplatecomponents`, `gettemplatespaginated`, `updatecomponents`, `updatedocument`, `updatedocumentcomponents`, `updatetemplate`. |
| **Leanix Impacts** | `LEANIX_IMPACTS_TOOL` | `True` | Manage leanix leanix impacts operations. Action-routed methods: `compute`, `get`, `getprojection`, `getsinglefactsheetprojection`, `update`. |
| **Leanix Integration Api** | `LEANIX_INTEGRATION_API_TOOL` | `True` | Manage leanix leanix integration api operations. Action-routed methods: `createinazure`, `createsynchronizationfastrun`, `createsynchronizationfastrunwithconfig`, `createsynchronizationrun`, `createsynchronizationrunwithconfig`, `createsynchronizationrunwithexecutiongroup`, `createsynchronizationrunwithexecutiongroupandurlinput`, `createsynchronizationrunwithurlinput`, `deleteprocessorconfiguration`, `get_examples_advancedexample`, `get_examples_starterexample`, `getprocessorconfigurations`, `getsynchronizationrundebuginformation`, `getsynchronizationrundebugvariables`, `getsynchronizationrunprogress`, `getsynchronizationrunresults`, `getsynchronizationrunresultsurl`, `getsynchronizationrunsstatuslist`, `getsynchronizationrunstats`, `getsynchronizationrunstatus`, `getsynchronizationrunwarnings`, `startsynchronizationrun`, `stopsynchronizationrun`, `upsertprocessorconfiguration`. |
| **Leanix Integration Collibra** | `LEANIX_INTEGRATION_COLLIBRA_TOOL` | `True` | Manage leanix leanix integration collibra operations. Action-routed methods: `createcollibracredentials`, `createconfiguration`, `createsynchronizationrun`, `deleteconfiguration`, `getassetstatuses`, `getassettypes`, `getattributetypes`, `getattributetypesforassettype`, `getattributetypesforassettypebyscope`, `getcollibracredentialsbyid`, `getcommunities`, `getcomplexrelationtypes`, `getconfigurationbyid`, `getconfigurations`, `getcredentials`, `getdomains`, `getfeaturetoggles`, `getfields`, `getoverview`, `getrelationfields`, `getrelations`, `getrelationtypes`, `getresourceroles`, `getresponsibilityroles`, `getstatus`, `getsubscriptionroles`, `updatecollibracredentials`, `updateconfiguration`, `validatecollibracredentialsbyid`. |
| **Leanix Integration Servicenow** | `LEANIX_INTEGRATION_SERVICENOW_TOOL` | `True` | Manage leanix leanix integration servicenow operations. Action-routed methods: `abortallpendingandrunningsynchronizations`, `abortsynchronization`, `changes`, `createconfiguration`, `deleteconfiguration`, `getaggregatedfactsheetsummary`, `getaggregatedsoftwareinformation`, `getallconfigurations`, `getavailablerelcirelations`, `getconfiguration`, `getcurrentlyrunningorlastcreatedrun`, `getfilterforfactsheet`, `getfilterforprovider`, `getfilters`, `getfiltersforhardware`, `getinstalledservicenowpluginversion`, `getmappingtablerelations`, `getreferencefieldrelations`, `getservicenowaggregatedhardware`, `getservicenowaggregatedsoftware`, `getservicenowmetadata`, `getservicenowsyncconstraintrules`, `getstatusoverview`, `gettables`, `getversionbyid`, `getversions`, `hooks`, `sendprompt`, `sendpromptv2`, `synchronize`, `updateconfiguration`, `validateconfiguration`, `validateservicenowcredentials`. |
| **Leanix Integration Signavio** | `LEANIX_INTEGRATION_SIGNAVIO_TOOL` | `True` | Manage leanix leanix integration signavio operations. Action-routed methods: `analyzelatestsynchronizationrun`, `analyzesynchronizationrun`, `cancelsynchronization`, `createcategory`, `createconfiguration`, `deleteconfiguration`, `getconfiguration`, `getconfigurations`, `getdirectories`, `getfactsheetfields`, `getformations`, `getlabels`, `getlatestsynchronizationrunanalysis`, `getprocessfields`, `getsignavioglossaryitemfields`, `getsignavioprocessfields`, `getsynchronizationrunanalysis`, `synchronizeconfiguration`, `unassignformation`, `updateconfiguration`. |
| **Leanix Inventory Data Quality** | `LEANIX_INVENTORY_DATA_QUALITY_TOOL` | `True` | Manage leanix leanix inventory data quality operations. Action-routed methods: `getdatamodel`, `getfactsheettypes`, `getrecommendationsagenttobc`, `getrecommendationsapptobc`, `getrelationnames`, `refreshembeddings`, `submitdqicardfeedback`, `submitfeedback`, `submitfeedback_1`. |
| **Leanix Mtm** | `LEANIX_MTM_TOOL` | `True` | Manage leanix leanix mtm operations. Action-routed methods: `accessfeature`, `activate`, `add_data_breach_contact`, `authenticate`, `checkip`, `create`, `create_account`, `create_contract`, `create_custom_feature`, `create_event`, `create_identity_provider`, `create_instance`, `create_or_update_user_segment`, `create_technical_user`, `create_workspace`, `createapitoken`, `createpermission`, `createsetting`, `createuser`, `createuserpassword`, `createworkspacelabel`, `createworkspacemaintenance`, `delete_account`, `delete_contract`, `delete_custom_feature`, `delete_data_breach_contact`, `delete_identity_provider`, `delete_instance`, `delete_technical_user`, `delete_workspace`, `deleteapitoken`, `deletedomain`, `deletesetting`, `deleteworkspacelabel`, `deleteworkspacemaintenance`, `get_account`, `get_accounts`, `get_contract`, `get_contracts`, `get_contracts_1`, `get_custom_feature`, `get_custom_feature_1`, `get_custom_features`, `get_custom_features_1`, `get_custom_features_2`, `get_data_breach_contact`, `get_domains`, `get_domains_1`, `get_event`, `get_events`, `get_events_1`, `get_events_2`, `get_events_3`, `get_events_4`, `get_events_5`, `get_events_6`, `get_export`, `get_feature_bundle`, `get_identity_provider`, `get_identity_providers`, `get_impersonations`, `get_instance`, `get_instances`, `get_instances_1`, `get_instances_2`, `get_metadata`, `get_permission`, `get_permission_stats`, `get_permissions`, `get_settings`, `get_settings_1`, `get_settings_2`, `get_support_permissions`, `get_technical_user`, `get_user_list_export`, `get_user_segment`, `get_users`, `get_users_1`, `get_users_2`, `get_workspace`, `get_workspaces`, `get_workspaces_1`, `get_workspaces_2`, `get_workspaces_3`, `getaiaccess`, `getall`, `getapitoken`, `getapitokens`, `getapplication`, `getapplications`, `getdomain`, `getdomains`, `getedition`, `geteditions`, `getevents_6`, `getfeature`, `getfeatures`, `getidentityproviders`, `getinstancesbyworkspace`, `getlabelsbyworkspace`, `getlabelsbyworkspaces`, `getnotificationsettings`, `getpermission`, `getpermissions`, `getpermissions_1`, `getpreferredinstance`, `getraw`, `getsetting`, `getsettings_2`, `getsettings_3`, `getsettings_4`, `gettaskbyid`, `gettechnicalusers`, `getuser`, `getuserpiichanges`, `getuserrandom`, `getuserrandom_1`, `getusers_1`, `getworkspacemaintenance`, `getworkspaces_2`, `getworkspaces_3`, `getworkspacesforbackup`, `inactive`, `invalidate`, `invite`, `list`, `login`, `loginpractitioner`, `logout`, `permissions_search`, `process_graph_ql`, `replace_technical_user_api_token`, `reset_password`, `review`, `set_password`, `setpassword_1`, `setworkspacenotificationstatus`, `switchdefaultinstance`, `switchpermissionrole`, `token`, `update_account`, `update_contract`, `update_custom_feature`, `update_event`, `update_identity_provider`, `update_instance`, `update_technical_user`, `update_workspace`, `updateapitoken`, `updatesetting`, `updateuser`, `upsertdomain`. |
| **Leanix Managed Code Execution** | `LEANIX_MANAGED_CODE_EXECUTION_TOOL` | `True` | Manage leanix leanix managed code execution operations. Action-routed methods: `createexecutionconfiguration`, `createsecret`, `deleteexecutionconfiguration`, `deletesecret`, `getallsecrets`, `getexecutionconfiguration`, `getexecutionconfigurationhistory`, `getexecutionconfigurations`, `getexecutionconfigurationsbysecretid`, `getexecutionlog`, `getexecutionlogs`, `getsecretbyid`, `updateexecutionconfiguration`, `updateexecutionconfigurationcapability`, `updatesecret`. |
| **Leanix Metrics** | `LEANIX_METRICS_TOOL` | `True` | Manage leanix leanix metrics operations. Action-routed methods: `all_charts_charts_get`, `all_kpis_kpis_get`, `all_kpis_simple_kpis_simple_get`, `all_points_schemas__uuid__points_get`, `all_schemas_schemas_get`, `delete_chart_charts__uuid__delete`, `delete_one_kpi_kpis__uuid__delete`, `delete_one_point_schemas__uuid__points__timestamp__delete`, `delete_points_range_schemas__uuid__points_delete`, `delete_schema_schemas__uuid__delete`, `find_schemas_schemas_find_get`, `get_aggregation_schemas__uuid__points_aggregation_post`, `healthcheck_healthcheck__get`, `kpi_job_jobs_kpi__kpi_uuid__post`, `new_chart_charts_post`, `new_kpi_kpis_post`, `new_point_schemas__uuid__points_post`, `new_schema_schemas_post`, `one_chart_charts__uuid__get`, `one_kpi_kpis__uuid__get`, `one_point_schemas__uuid__points__timestamp__get`, `one_schema_schemas__uuid__get`, `patch_kpi_kpis_patch`, `put_kpi_kpis_put`, `trend_schemas__uuid__trends_get`, `update_patch_chart_charts__uuid__patch`, `update_put_chart_charts__uuid__put`, `validate_kpis_validate_post`, `ws_job_jobs_post`. |
| **Leanix Navigation** | `LEANIX_NAVIGATION_TOOL` | `True` | Manage leanix leanix navigation operations. Action-routed methods: `batchputcollectiongroups`, `createcollectiongroup`, `createpresentation`, `createslide`, `deletecollection`, `deletecollectiongroupbyid`, `deletecollectionnavigationitem`, `deletenavigationitemfavorite`, `deletepresentationbyid`, `deletepresentationsharebyid`, `deleteslidebyid`, `executebatchdelete`, `executebatchmove`, `getallcollectiongroups`, `getcollectionfolders`, `getcollectiongroupbyid`, `getcollections`, `getnavigationitemfavorite`, `getpresentationbyid`, `getpresentationsharesbyid`, `postcollection`, `postcollectionnavigationitem`, `postfoldercontroller`, `postnavigationitemfavorite`, `putcollection`, `putcollectiongroupbyid`, `putcollectionnavigationitem`, `putpresentationbyid`, `putslidebyid`, `searchnavigationitem`, `searchpresentation`, `sharepresentation`, `updatefoldercontroller`. |
| **Leanix Pathfinder** | `LEANIX_PATHFINDER_TOOL` | `True` | Manage leanix leanix pathfinder operations. Action-routed methods: `archive_fact_sheet`, `change_bookmark_owner`, `create_access_control_entity`, `create_bookmark`, `create_bookmark_shares`, `create_fact_sheet`, `create_fact_sheet_relation`, `create_full_export`, `delete_access_control_entity`, `delete_asset`, `delete_bookmark`, `delete_bookmark_shares`, `delete_fact_sheet_relation`, `download_asset`, `download_export_file`, `get_access_control_entities`, `get_access_control_entity`, `get_action_batch`, `get_action_batches`, `get_all_versions_for_bookmark`, `get_authorization`, `get_bookmark`, `get_bookmark_shares`, `get_bookmarks`, `get_data_model`, `get_enriched_data_model`, `get_exports`, `get_fact_sheet`, `get_fact_sheet_hierarchy`, `get_fact_sheet_relations`, `get_fact_sheet_resource_model`, `get_fact_sheets`, `get_feature`, `get_features`, `get_language`, `get_meta_model`, `get_meta_model_actions`, `get_meta_model_actions_audit_log`, `get_meta_model_actions_for_node`, `get_meta_model_authorization`, `get_meta_model_for_type`, `get_meta_model_job`, `get_meta_model_permission_roles`, `get_meta_model_root`, `get_model_customization`, `get_preview_of_affected_data`, `get_reporting_model`, `get_settings`, `get_suggestions`, `get_view_model`, `post_action_batches`, `post_meta_model_actions`, `process_graph_ql`, `process_graph_ql_multipart`, `update_access_control_entity`, `update_authorization`, `update_bookmark`, `update_data_model`, `update_fact_sheet`, `update_fact_sheet_relation`, `update_fact_sheet_resource_model`, `update_feature`, `update_language`, `update_models_with_customization`, `update_reporting_model`, `update_settings`, `update_view_model`, `upsert_asset`. |
| **Leanix Poll** | `LEANIX_POLL_TOOL` | `True` | Manage leanix leanix poll operations. Action-routed methods: `check_for_new_fact_sheets`, `create_poll`, `create_poll_reminder`, `create_poll_run`, `create_poll_template`, `delete_by_id`, `delete_poll`, `delete_poll_run`, `get_added_recipients_for_run`, `get_all`, `get_by_id`, `get_poll`, `get_poll_count`, `get_poll_poll_runs`, `get_poll_recipient_details`, `get_poll_result`, `get_poll_results_for_user`, `get_poll_run`, `get_poll_run_results`, `get_poll_runs`, `get_poll_runs_kpi_counts`, `get_polls`, `get_polls_for_factsheet`, `get_recipients_for_poll_run`, `get_reminders`, `get_results_for_poll_run`, `replay`, `replay_1`, `set_status`, `update_poll`, `update_poll_result`, `update_poll_run`. |
| **Leanix Reference Data** | `LEANIX_REFERENCE_DATA_TOOL` | `True` | Manage leanix leanix reference data operations. Action-routed methods: `batchlinks`, `clearduplicatelinks`, `clonelinks`, `deletelinkbysourcename`, `fetchbusinesscapabilitymetrics`, `filteredfactsheetscount`, `get_jobs`, `get_source_name_fact_sheets_id`, `getbuscapconfiguration`, `getbusinesscapability`, `getconfiguration`, `getconfigurationmodels`, `getexportfile`, `getexportstatus`, `getfactsheetsbysourcename`, `getlatestrecommendationrun`, `getlink`, `getlinkbysourcename`, `getlinks`, `getlinksbyfactsheettype`, `getlinksbysourcename`, `getprovisioning`, `getrefresh`, `getrefreshes`, `getrequests`, `getrequestscount`, `getsaasconfiguration`, `gettbmmigrationstatus`, `gettbmtaxonomy`, `gettechcategoryconfiguration`, `getusedtechnolotrecommendationcontroller`, `post_jobs`, `post_managedrestorationrequests`, `post_managedsnapshotrequests`, `postbusinesscapability`, `postrefresh`, `precomputedrecommendations`, `putbulklinksbysourcename`, `putbulksourcehierarchylinkscontroller`, `putbuscapconfiguration`, `putconfiguration`, `putimporttbm`, `putlinksbysourcename`, `putprovisioning`, `putrequests`, `putsaasconfiguration`, `putsourcehierarchylinkcontroller`, `puttechcategoryconfiguration`, `putusedtechnolotrecommendationcontroller`, `refreshltlslinks`, `startmappingexport`, `tbmmigrationstatusupdate`, `validatelink`. |
| **Leanix Discovery Sap** | `LEANIX_DISCOVERY_SAP_TOOL` | `True` | Manage leanix leanix discovery sap operations. Action-routed methods: `appcontroller_heartbeat`, `demodatacontroller_createcustomdemodata`, `demodatacontroller_demodatalist`, `integrationscontroller_integrationcreate`, `integrationscontroller_integrationdelete`, `integrationscontroller_integrationget`, `integrationscontroller_integrationpatch`, `integrationscontroller_integrationslist`, `integrationscontroller_integrationtriggersync`. |
| **Leanix Technology Discovery** | `LEANIX_TECHNOLOGY_DISCOVERY_TOOL` | `True` | Manage leanix leanix technology discovery operations. Action-routed methods: `createtechstack`, `deletetechstackbyqueryparam`, `getaggregatedcounts`, `getalltechstacks`, `getcomponentsbyapplication`, `getfactsheetsbylibrary`, `getlibraries`, `getlibraryusagedetails`, `gettechstackdetailsbyqueryparam`, `getversionsbylibrary`, `leanix_v1_factsheets_sboms_ingest`, `leanix_v1_factsheets_sboms_ingest_1`, `leanix_v1_microservice_discovery_yaml_manifest_register`, `previewmatches`, `searchcomponentsbypurl`, `updatetechstackbyqueryparam`. |
| **Leanix Storage** | `LEANIX_STORAGE_TOOL` | `True` | Manage leanix leanix storage operations. Action-routed methods: `addfiletoworkspace`, `deleteavatar`, `deletefile`, `deletefiles`, `deletelogo`, `getavatar`, `getfile`, `getfilecontent`, `getfiles`, `getlogo`, `setavatar`, `setfileowner`, `setlogo`. |
| **Leanix Survey** | `LEANIX_SURVEY_TOOL` | `True` | Manage leanix leanix survey operations. Action-routed methods: `check_for_new_fact_sheets`, `create_poll`, `create_poll_reminder`, `create_poll_run`, `delete_poll_by_id`, `delete_poll_run`, `get_added_recipients_for_poll_run`, `get_all_reminders_for_poll_run`, `get_all_templates`, `get_poll`, `get_poll_count`, `get_poll_result`, `get_poll_results_by_poll_run_id`, `get_poll_results_for_user`, `get_poll_run_by_id`, `get_poll_runs`, `get_poll_runs_by_poll`, `get_polls`, `get_polls_for_fact_sheet`, `get_recipients_and_fact_sheets_for_poll`, `get_recipients_and_fact_sheets_for_poll_run`, `get_templates_by_id`, `getpollrunresultsasexcel`, `replay_all_workspaces`, `replay_workspace_by_id`, `update_poll`, `update_poll_result`, `update_poll_run`, `update_poll_run_status`. |
| **Leanix Synclog** | `LEANIX_SYNCLOG_TOOL` | `True` | Manage leanix leanix synclog operations. Action-routed methods: `addsyncitembatch`, `createsynchronization`, `deletesyncitems`, `getsynchronization`, `getsynchronizations`, `getsyncitems`, `getsyncitems_1`, `gettopics`, `gettriggers`, `requestabortion`, `updatesynchronization`. |
| **Leanix Todo** | `LEANIX_TODO_TOOL` | `True` | Manage leanix leanix todo operations. Action-routed methods: `accepttodo`, `assigntome`, `createtodo`, `deletetodos`, `get`, `managedrestorationrequests`, `managedsnapshotrequests`, `query`, `rejecttodo`, `replyandclosetodo`, `upserttodos`. |
| **Leanix Transformations** | `LEANIX_TRANSFORMATIONS_TOOL` | `True` | Manage leanix leanix transformations operations. Action-routed methods: `createtransformation`, `deletetransformation`, `deletetransformationcustomimpacts`, `gettransformation`, `gettransformationcustomimpacts`, `gettransformations`, `posttransformationcustomimpacts`, `posttransformationexecution`, `posttransformationsexecution`, `puttransformation`, `puttransformationcustomimpacts`. |
| **Leanix Webhooks** | `LEANIX_WEBHOOKS_TOOL` | `True` | Manage leanix leanix webhooks operations. Action-routed methods: `createcustomeventtag`, `createevent`, `createeventbatch`, `createsubscription`, `deletecustomeventtag`, `deletesubscription`, `getcustomeventtags`, `geteventtags`, `getsubscription`, `getsubscriptiondeliveries`, `getsubscriptionevents`, `getsubscriptions`, `getsubscriptionstatus`, `getsubscriptionstatuses`, `updatecustomeventtag`, `updatesubscription`, `updatesubscriptioncursor`. |
| **Graphql** | `GRAPHQL_TOOL` | `True` | Execute raw GraphQL queries and mutations natively on LeanIX Pathfinder API. |

Detailed tool schemas, parameter shapes, and validation constraints are preserved in [docs/mcp.md](docs/mcp.md).

### Dynamic Tool Selection & Visibility

This MCP server supports dynamic toolset selection and visibility filtering at runtime. This allows you to restrict the set of exposed tools in order to prevent blowing up the LLM's context window.

You can configure tool filtering via multiple input channels:

- **CLI Arguments:** Pass `--tools` or `--toolsets` (or their disabled counterparts `--disabled-tools` and `--disabled-toolsets`) during startup.
- **Environment Variables:** Define standard environment variables:
  - `MCP_ENABLED_TOOLS` / `MCP_DISABLED_TOOLS`
  - `MCP_ENABLED_TAGS` / `MCP_DISABLED_TAGS`
- **HTTP SSE Request Headers:** Pass custom headers during transport initialization:
  - `x-mcp-enabled-tools` / `x-mcp-disabled-tools`
  - `x-mcp-enabled-tags` / `x-mcp-disabled-tags`
- **HTTP SSE Request Query Parameters:** Append query parameters directly to your transport connection URL:
  - `?tools=tool1,tool2`
  - `?tags=tag1`

When query strings or parameters are supplied, an LLM-free **Knowledge Graph resolution layer** (using `DynamicToolOrchestrator`) matches query intents against known tool tags, names, or descriptions, with safe fallback and automated 24-hour background cache refreshing.

---

### MCP Configuration Examples

#### stdio Transport (Recommended for local IDEs e.g., Cursor, Claude Desktop)
Configure your IDE's `mcp.json` to launch the MCP server via `uvx`:

```json
{
  "mcpServers": {
    "leanix-agent": {
      "command": "uvx",
      "args": [
        "--from",
        "leanix-agent",
        "leanix-mcp"
      ],
      "env": {
        "LEANIX_WORKSPACE": "your_leanix_workspace_here",
        "LEANIX_API_TOKEN": "your_leanix_api_token_here",
        "SSL_VERIFY": "your_ssl_verify_here",
        "DEBUG": "your_debug_here",
        "PYTHONUNBUFFERED": "your_pythonunbuffered_here",
        "LEANIX_TOKEN": "your_leanix_token_here"
      }
    }
  }
}
```

#### Streamable-HTTP Transport (Recommended for production deployments)
Configure your client's `mcp.json` to launch the Streamable-HTTP server via `uvx` with explicit host and port definition:

```json
{
  "mcpServers": {
    "leanix-agent": {
      "command": "uvx",
      "args": [
        "--from",
        "leanix-agent",
        "leanix-mcp"
      ],
      "env": {
        "TRANSPORT": "streamable-http",
        "HOST": "0.0.0.0",
        "PORT": "8000",
        "LEANIX_WORKSPACE": "your_leanix_workspace_here",
        "LEANIX_API_TOKEN": "your_leanix_api_token_here",
        "SSL_VERIFY": "your_ssl_verify_here",
        "DEBUG": "your_debug_here",
        "PYTHONUNBUFFERED": "your_pythonunbuffered_here",
        "LEANIX_TOKEN": "your_leanix_token_here"
      }
    }
  }
}
```

Alternatively, connect to a pre-deployed remote or local Streamable-HTTP instance:

```json
{
  "mcpServers": {
    "leanix-agent": {
      "url": "http://localhost:8000/leanix-agent/mcp"
    }
  }
}
```

Deploying the Streamable-HTTP server via Docker:

```bash
docker run -d \
  --name leanix-agent-mcp \
  -p 8000:8000 \
  -e TRANSPORT=streamable-http \
  -e PORT=8000 \
  -e LEANIX_WORKSPACE="your_value" \
  -e LEANIX_API_TOKEN="your_value" \
  -e SSL_VERIFY="your_value" \
  -e DEBUG="your_value" \
  -e PYTHONUNBUFFERED="your_value" \
  -e LEANIX_TOKEN="your_value" \
  knucklessg1/leanix-agent:latest
```

---

## Agent

This repository features a fully integrated Pydantic AI Graph Agent. It communicates over the **Agent Control Protocol (ACP)** and interacts seamlessly with the **Agent Web UI (AG-UI)** and Terminal interface.

### Running the Agent CLI
To start the interactive command-line agent:

```bash
# Set credentials
export LEANIX_WORKSPACE="your_value"
export LEANIX_API_TOKEN="your_value"
export SSL_VERIFY="your_value"
export DEBUG="your_value"
export PYTHONUNBUFFERED="your_value"
export LEANIX_TOKEN="your_value"

# Run the agent server
leanix-agent --provider openai --model-id gpt-4o
```

### Docker Compose Orchestration
The following `docker/agent.compose.yml` configures the Agent, Web UI, and Terminal Interface together:

```yaml
version: '3.8'

services:
  leanix-agent-mcp:
    image: knucklessg1/leanix-agent:latest
    container_name: leanix-agent-mcp
    hostname: leanix-agent-mcp
    restart: always
    env_file:
      - ../.env
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=8000
      - TRANSPORT=streamable-http
    ports:
      - "8000:8000"
    healthcheck:
      test: ["CMD", "python3", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:8000/health')"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

  leanix-agent-agent:
    image: knucklessg1/leanix-agent:latest
    container_name: leanix-agent-agent
    hostname: leanix-agent-agent
    restart: always
    depends_on:
      - leanix-agent-mcp
    env_file:
      - ../.env
    command: [ "leanix-agent" ]
    environment:
      - PYTHONUNBUFFERED=1
      - HOST=0.0.0.0
      - PORT=9004
      - MCP_URL=http://leanix-agent-mcp:8000/mcp
      - PROVIDER=${PROVIDER:-openai}
      - MODEL_ID=${MODEL_ID:-gpt-4o}
      - ENABLE_WEB_UI=True
      - ENABLE_OTEL=True
    ports:
      - "9004:9004"
    healthcheck:
      test: ["CMD", "python3", "-c", "import urllib.request; urllib.request.urlopen('http://localhost:9004/health')"]
      interval: 30s
      timeout: 10s
      retries: 3
      start_period: 10s
    logging:
      driver: json-file
      options:
        max-size: "10m"
        max-file: "3"

```

Detailed graph node architecture explanations, custom skill configurations, and agentic trace guides are available in [docs/agent.md](docs/agent.md).

---

## Security & Governance

Built directly upon the enterprise-ready [`agent-utilities`](https://github.com/Knuckles-Team/agent-utilities) core, standard security parameters are fully supported:

### Access Control & Policy Enforcement
- **Eunomia Policies:** Fine-grained, policy-driven tool authorization. Supports `none`, local `embedded` (`mcp_policies.json`), or centralized `remote` modes.
- **OIDC Token Delegation:** Compliant with RFC 8693 token exchange for flowing authenticating user credentials from Web UI / ACP → Agent → MCP.
- **Scoped Credentials:** Execution context runs restricted to the specific caller identity.

### Runtime Security Grid
| Feature | Functionality | Enablement |
|---------|---------------|------------|
| **Tool Guard** | Sensitivity inspection with human-in-the-loop validation | Enabled by default |
| **Prompt Injection Defense** | Input scanning, repetition monitoring, and recursive loop blocks | Enabled by default |
| **Context Safety Guard** | Stuck-loop detectors and contextual overflow preemptive alerts | Enabled by default |

---

## Installation

Install the Python package locally:

```bash
# Using uv (highly recommended)
uv pip install leanix-agent[all]

# Using standard pip
python -m pip install leanix-agent[all]
```

---

## Repository Owners

<img width="100%" height="180em" src="https://github-readme-stats.vercel.app/api?username=Knucklessg1&show_icons=true&hide_border=true&&count_private=true&include_all_commits=true" />

![GitHub followers](https://img.shields.io/github/followers/Knucklessg1)
![GitHub User's stars](https://img.shields.io/github/stars/Knucklessg1)

---

## Contribute

Contributions are welcome! Please ensure code quality by executing local checks before submitting pull requests:
- Format code using `ruff format .`
- Lint code using `ruff check .`
- Validate type-safety with `mypy .`
- Execute test suites using `pytest`
