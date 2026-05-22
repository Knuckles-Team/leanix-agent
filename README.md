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

*Version: 0.13.0*

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

Detailed instructions on how to use the underlying API wrappers, extended schema bindings, and developer SDK references are maintained in [docs/index.md](file:///home/apps/workspace/agent-packages/agents/leanix-agent/docs/index.md).

---

## MCP

This server utilizes dynamic Action-Routed tools to optimize token overhead and maximize IDE compatibility.

### Available MCP Tools
| Tool Module | Toggle Env Var | Enabled by Default | Description & Nested Methods |
|-------------|----------------|--------------------|------------------------------|
| **Leanix Ai Inventory Builder** | `LEANIX_AI_INVENTORY_BUILDERTOOL` | `True` | Manage leanix leanix ai inventory builder operations. Action-routed methods: `healthcheck`, `pipelines`, `getpipelines`, `sendpipelineaction`, `getpipelinesuggestions`, `getpipeline`, `deletepipeline`, `getpipelinefile`, `deletefailedpipelines`, `admindeletepipeline`. |
| **Leanix Apptio Connector** | `LEANIX_APPTIO_CONNECTORTOOL` | `True` | Manage leanix leanix apptio connector operations. Action-routed methods: `getallconfigurations`, `upsertconfiguration`, `getconfigurations`, `deleteconfiguration`, `create`, `getresults`, `getresultsurl`, `getstats`, `getstatus`, `getwarnings`. |
| **Leanix Automations** | `LEANIX_AUTOMATIONSTOOL` | `True` | Manage leanix leanix automations operations. Action-routed methods: `templatescontroller_getalltemplates`, `templatescontroller_createtemplate`, `templatescontroller_gettemplate`, `templatescontroller_updatetemplate`, `templatescontroller_patchtemplate`, `templatescontroller_deletetemplate`, `instancescontroller_findall`, `instancescontroller_quota`, `statisticscontroller_getstatistics`, `snapshotscontroller_managesnapshotrequests`, `snapshotscontroller_managedrestorationrequests`, `scriptscontroller_createmcescript`, `scriptscontroller_updatemcescript`. |
| **Leanix Reference Data Catalog** | `LEANIX_REFERENCE_DATA_CATALOGTOOL` | `True` | Manage leanix leanix reference data catalog operations. Action-routed methods: `get_recommendations`, `get_items`, `get_items_id`, `delete_links`, `post_links`, `post_requests`, `get_requests`, `post_requests_id_comments`. |
| **Leanix Discovery Ai Agents** | `LEANIX_DISCOVERY_AI_AGENTSTOOL` | `True` | Manage leanix leanix discovery ai agents operations. Action-routed methods: `post_agents_a2a_cards`, `post_integrations`, `get_integrations`, `get_integrations_id`, `put_integrations_id_name`, `put_integrations_id_status`, `put_integrations_id_capabilities`, `put_integrations_id_credentials`. |
| **Leanix Discovery Linking V1** | `LEANIX_DISCOVERY_LINKING_V1TOOL` | `True` | Manage leanix leanix discovery linking v1 operations. Action-routed methods: `link`, `bulk_link`, `discovery_itemsid`, `discovery_items`, `discovery_itemsidpre_validate_linkfactsheetid`, `discovery_itemsfilter_options`, `reject`, `discovery_itemslinking_progress`, `discovery_itemslinking_progressid`, `discovery_itemskpi_values`, `factsheetsiddetails`. |
| **Leanix Discovery Linking V2** | `LEANIX_DISCOVERY_LINKING_V2TOOL` | `True` | Manage leanix leanix discovery linking v2 operations. Action-routed methods: `get_factsheets_id_links`, `get_origin_discoveryitems`, `get_origin_discoveryitems_export`, `put_origin_discoveryitems_link`, `get_origin_discoveryitems_linkingprogress`, `put_origin_discoveryitems_reject`, `get_origin_discoveryitems_sourceconfigs`, `get_origin_discoveryitems_id`, `get_origin_discoveryitems_id_changelogs`, `put_origin_discoveryitems_id_link`, `post_origin_discoveryitems_id_preview`, `get_origin_insights`, `get_origin_internal_events`, `get_origin_internal_events_compaction`, `post_origin_push`, `post_origin_push_id`, `get_origin_settings`, `get_origin_settings_autolinking`, `put_origin_settings_autolinking`. |
| **Leanix Discovery Sap Extension** | `LEANIX_DISCOVERY_SAP_EXTENSIONTOOL` | `True` | Manage leanix leanix discovery sap extension operations. Action-routed methods: `get_cloud_foundry_domains`, `get_cloud_foundry_subject_pattern`, `put_integrations_id_credentials_cloud_foundry`, `post_cloud_foundry_infer_certificate_domain`, `get_credentials_type`, `post_credentials_verify_cms`, `get_health`, `post_integrations`, `get_integrations`, `put_integrations_id_credentials_cms`, `patch_integrations_id`, `delete_integrations_id_`, `post_integrations_credentials_verify`, `post_integrations_id_sync`, `get_kyma_spec_suggestions`, `post_kyma_verify_api_url`, `put_integrations_id_credentials_kyma`, `put_integrations_id_credentials_build`, `get_checkdatamodel`, `get_check_data_model`. |
| **Leanix Discovery Saas** | `LEANIX_DISCOVERY_SAASTOOL` | `True` | Manage leanix leanix discovery saas operations. Action-routed methods: `getavailableintegrations`, `postintegration`, `getintegrations`, `getintegrationbyid`, `deleteintegrationbyid`, `putintegrationnamebyid`, `putintegrationcapabilitiesbyid`, `putintegrationcredentialsbyid`, `putintegrationstatusbyid`, `getdiscoveries`, `getdiscoveryprioritybyid`. |
| **Leanix Documents** | `LEANIX_DOCUMENTSTOOL` | `True` | Manage leanix leanix documents operations. Action-routed methods: `gettemplatecomponents`, `updatecomponents`, `createtemplatecomponents`, `gettemplatebyid`, `updatetemplate`, `deletetemplate`, `getdocumentbyid`, `updatedocument`, `deletedocumentbyid`, `getdocumentcomponents`, `updatedocumentcomponents`, `gettemplatespaginated`, `createtemplates`, `getdocumentspaginated`, `createdocuments`, `getdocumentscount`, `deletetemplatecomponent`. |
| **Leanix Impacts** | `LEANIX_IMPACTSTOOL` | `True` | Manage leanix leanix impacts operations. Action-routed methods: `get`, `update`, `compute`, `getprojection`, `getsinglefactsheetprojection`. |
| **Leanix Integration Api** | `LEANIX_INTEGRATION_APITOOL` | `True` | Manage leanix leanix integration api operations. Action-routed methods: `get_examples_starterexample`, `get_examples_advancedexample`, `getprocessorconfigurations`, `upsertprocessorconfiguration`, `deleteprocessorconfiguration`, `getsynchronizationrunsstatuslist`, `createsynchronizationrun`, `startsynchronizationrun`, `getsynchronizationrunprogress`, `stopsynchronizationrun`, `getsynchronizationrunstatus`, `getsynchronizationrunstats`, `getsynchronizationrunresults`, `getsynchronizationrunresultsurl`, `getsynchronizationrunwarnings`, `createsynchronizationrunwithconfig`, `createsynchronizationrunwithurlinput`, `createsynchronizationrunwithexecutiongroupandurlinput`, `createsynchronizationrunwithexecutiongroup`, `getsynchronizationrundebuginformation`, `getsynchronizationrundebugvariables`, `createsynchronizationfastrun`, `createsynchronizationfastrunwithconfig`, `createinazure`. |
| **Leanix Integration Collibra** | `LEANIX_INTEGRATION_COLLIBRATOOL` | `True` | Manage leanix leanix integration collibra operations. Action-routed methods: `createsynchronizationrun`, `getconfigurations`, `createconfiguration`, `getconfigurationbyid`, `updateconfiguration`, `deleteconfiguration`, `getoverview`, `getstatus`, `getfeaturetoggles`, `getfields`, `getrelationfields`, `getrelations`, `getsubscriptionroles`, `getcredentials`, `createcollibracredentials`, `getcollibracredentialsbyid`, `updatecollibracredentials`, `validatecollibracredentialsbyid`, `getattributetypesforassettype`, `getattributetypesforassettypebyscope`, `getassetstatuses`, `getassettypes`, `getattributetypes`, `getcommunities`, `getcomplexrelationtypes`, `getdomains`, `getrelationtypes`, `getresourceroles`, `getresponsibilityroles`. |
| **Leanix Integration Servicenow** | `LEANIX_INTEGRATION_SERVICENOWTOOL` | `True` | Manage leanix leanix integration servicenow operations. Action-routed methods: `getaggregatedfactsheetsummary`, `getaggregatedsoftwareinformation`, `getservicenowaggregatedsoftware`, `getfilterforfactsheet`, `getfilterforprovider`, `getfiltersforhardware`, `getservicenowaggregatedhardware`, `getstatusoverview`, `getallconfigurations`, `createconfiguration`, `getconfiguration`, `updateconfiguration`, `deleteconfiguration`, `synchronize`, `validateconfiguration`, `validateservicenowcredentials`, `getfilters`, `getservicenowsyncconstraintrules`, `getavailablerelcirelations`, `getinstalledservicenowpluginversion`, `getmappingtablerelations`, `getreferencefieldrelations`, `getservicenowmetadata`, `gettables`, `changes`, `hooks`, `sendprompt`, `sendpromptv2`, `abortallpendingandrunningsynchronizations`, `abortsynchronization`, `getcurrentlyrunningorlastcreatedrun`, `getversionbyid`, `getversions`. |
| **Leanix Integration Signavio** | `LEANIX_INTEGRATION_SIGNAVIOTOOL` | `True` | Manage leanix leanix integration signavio operations. Action-routed methods: `getconfigurations`, `createconfiguration`, `getconfiguration`, `updateconfiguration`, `deleteconfiguration`, `synchronizeconfiguration`, `unassignformation`, `getformations`, `getdirectories`, `createcategory`, `getfactsheetfields`, `getlabels`, `getsignavioglossaryitemfields`, `getsignavioprocessfields`, `getprocessfields`, `analyzelatestsynchronizationrun`, `analyzesynchronizationrun`, `cancelsynchronization`, `getlatestsynchronizationrunanalysis`, `getsynchronizationrunanalysis`. |
| **Leanix Inventory Data Quality** | `LEANIX_INVENTORY_DATA_QUALITYTOOL` | `True` | Manage leanix leanix inventory data quality operations. Action-routed methods: `refreshembeddings`, `getrecommendationsapptobc`, `getrecommendationsagenttobc`, `submitfeedback`, `submitfeedback_1`, `submitdqicardfeedback`, `getdatamodel`, `getrelationnames`, `getfactsheettypes`. |
| **Leanix Mtm** | `LEANIX_MTMTOOL` | `True` | Manage leanix leanix mtm operations. Action-routed methods: `getaiaccess`, `gettaskbyid`, `createworkspacelabel`, `deleteworkspacelabel`, `getall`, `getlabelsbyworkspace`, `getlabelsbyworkspaces`, `token`, `get_data_breach_contact`, `add_data_breach_contact`, `delete_data_breach_contact`, `get_accounts`, `create_account`, `get_account`, `update_account`, `delete_account`, `get_contracts`, `get_events`, `get_instances`, `get_settings`, `get_users`, `get_workspaces`, `getapitokens`, `createapitoken`, `getapitoken`, `updateapitoken`, `deleteapitoken`, `getfeature`, `accessfeature`, `getapplication`, `getapplications`, `getedition`, `geteditions`, `getfeatures`, `create_contract`, `get_contract`, `update_contract`, `delete_contract`, `get_custom_features`, `create_custom_feature`, `get_custom_feature`, `update_custom_feature`, `delete_custom_feature`, `deletedomain`, `getdomain`, `getdomains`, `upsertdomain`, `getidentityproviders`, `getworkspaces_2`, `create_event`, `get_event`, `update_event`, `getraw`, `get_export`, `process_graph_ql`, `get_identity_providers`, `create_identity_provider`, `get_identity_provider`, `update_identity_provider`, `delete_identity_provider`, `get_domains`, `get_metadata`, `getworkspaces_3`, `activate`, `authenticate`, `checkip`, `invite`, `login`, `loginpractitioner`, `logout`, `reset_password`, `review`, `set_password`, `switchpermissionrole`, `inactive`, `create_instance`, `get_instance`, `update_instance`, `delete_instance`, `getinstancesbyworkspace`, `getpreferredinstance`, `switchdefaultinstance`, `list`, `create`, `invalidate`, `getpermissions`, `createpermission`, `getpermission`, `getsettings_2`, `getuserrandom`, `getsettings_3`, `createsetting`, `getsetting`, `updatesetting`, `deletesetting`, `getnotificationsettings`, `setworkspacenotificationstatus`, `gettechnicalusers`, `create_technical_user`, `get_technical_user`, `update_technical_user`, `delete_technical_user`, `replace_technical_user_api_token`, `getusers_1`, `createuser`, `createuserpassword`, `getevents_6`, `getpermissions_1`, `getsettings_4`, `getuser`, `updateuser`, `getuserrandom_1`, `setpassword_1`, `create_workspace`, `get_workspace`, `update_workspace`, `delete_workspace`, `get_feature_bundle`, `get_impersonations`, `get_permission`, `get_permission_stats`, `get_permissions`, `get_support_permissions`, `get_user_list_export`, `getworkspacesforbackup`, `permissions_search`, `getuserpiichanges`, `get_user_segment`, `create_or_update_user_segment`, `getworkspacemaintenance`, `createworkspacemaintenance`, `deleteworkspacemaintenance`. |
| **Leanix Managed Code Execution** | `LEANIX_MANAGED_CODE_EXECUTIONTOOL` | `True` | Manage leanix leanix managed code execution operations. Action-routed methods: `getsecretbyid`, `updatesecret`, `deletesecret`, `getexecutionconfiguration`, `updateexecutionconfiguration`, `deleteexecutionconfiguration`, `updateexecutionconfigurationcapability`, `getallsecrets`, `createsecret`, `getexecutionconfigurations`, `createexecutionconfiguration`, `getexecutionconfigurationsbysecretid`, `getexecutionlogs`, `getexecutionlog`, `getexecutionconfigurationhistory`. |
| **Leanix Metrics** | `LEANIX_METRICSTOOL` | `True` | Manage leanix leanix metrics operations. Action-routed methods: `all_schemas_schemas_get`, `new_schema_schemas_post`, `find_schemas_schemas_find_get`, `one_schema_schemas__uuid__get`, `delete_schema_schemas__uuid__delete`, `all_points_schemas__uuid__points_get`, `new_point_schemas__uuid__points_post`, `delete_points_range_schemas__uuid__points_delete`, `get_aggregation_schemas__uuid__points_aggregation_post`, `one_point_schemas__uuid__points__timestamp__get`, `delete_one_point_schemas__uuid__points__timestamp__delete`, `trend_schemas__uuid__trends_get`, `all_kpis_kpis_get`, `put_kpi_kpis_put`, `new_kpi_kpis_post`, `patch_kpi_kpis_patch`, `all_kpis_simple_kpis_simple_get`, `one_kpi_kpis__uuid__get`, `delete_one_kpi_kpis__uuid__delete`, `validate_kpis_validate_post`, `healthcheck_healthcheck__get`, `ws_job_jobs_post`, `kpi_job_jobs_kpi__kpi_uuid__post`, `all_charts_charts_get`, `new_chart_charts_post`, `one_chart_charts__uuid__get`, `update_put_chart_charts__uuid__put`, `delete_chart_charts__uuid__delete`, `update_patch_chart_charts__uuid__patch`. |
| **Leanix Navigation** | `LEANIX_NAVIGATIONTOOL` | `True` | Manage leanix leanix navigation operations. Action-routed methods: `getallcollectiongroups`, `createcollectiongroup`, `batchputcollectiongroups`, `getcollectiongroupbyid`, `putcollectiongroupbyid`, `deletecollectiongroupbyid`, `postcollection`, `getcollections`, `putcollection`, `deletecollection`, `putcollectionnavigationitem`, `postcollectionnavigationitem`, `deletecollectionnavigationitem`, `getcollectionfolders`, `postfoldercontroller`, `updatefoldercontroller`, `executebatchmove`, `executebatchdelete`, `searchnavigationitem`, `getnavigationitemfavorite`, `postnavigationitemfavorite`, `deletenavigationitemfavorite`, `createslide`, `putslidebyid`, `deleteslidebyid`, `searchpresentation`, `createpresentation`, `getpresentationbyid`, `putpresentationbyid`, `deletepresentationbyid`, `getpresentationsharesbyid`, `sharepresentation`, `deletepresentationsharebyid`. |
| **Leanix Pathfinder** | `LEANIX_PATHFINDERTOOL` | `True` | Manage leanix leanix pathfinder operations. Action-routed methods: `download_asset`, `upsert_asset`, `delete_asset`, `get_bookmark_shares`, `createbookmarkshare`, `deletebookmarkshare`, `get_bookmark`, `update_bookmark`, `delete_bookmark`, `change_bookmark_owner`, `get_bookmarks`, `create_bookmark`, `get_all_versions_for_bookmark`, `get_data_model`, `update_data_model`, `get_enriched_data_model`, `create_full_export`, `download_export_file`, `get_exports`, `get_fact_sheet`, `update_fact_sheet`, `archive_fact_sheet`, `get_fact_sheets`, `create_fact_sheet`, `get_fact_sheet_relations`, `create_fact_sheet_relation`, `updatefactsheetrelation`, `delete_fact_sheet_relation`, `get_fact_sheet_hierarchy`, `get_feature`, `upsertfeature`, `get_features`, `process_graph_ql`, `process_graph_ql_multipart`, `get_access_control_entities`, `create_access_control_entity`, `readaccesscontrolentity`, `update_access_control_entity`, `delete_access_control_entity`, `get_authorization`, `update_authorization`, `get_fact_sheet_resource_model`, `update_fact_sheet_resource_model`, `get_language`, `update_language`, `get_reporting_model`, `update_reporting_model`, `get_view_model`, `update_view_model`, `get_model_customization`, `updatemodelswithcustomization`, `get_settings`, `update_settings`, `get_suggestions`, `get_meta_model`, `get_meta_model_actions`, `post_meta_model_actions`, `get_meta_model_actions_audit_log`, `get_meta_model_job`, `get_meta_model_permission_roles`, `get_meta_model_actions_for_node`, `get_action_batch`, `get_action_batches`, `post_action_batches`, `get_meta_model_authorization`, `get_meta_model_root`, `get_meta_model_for_type`, `get_preview_of_affected_data`. |
| **Leanix Poll** | `LEANIX_POLLTOOL` | `True` | Manage leanix leanix poll operations. Action-routed methods: `replay`, `get_polls_for_factsheet`, `get_polls`, `create_poll`, `get_poll`, `update_poll`, `delete_poll`, `get_poll_count`, `get_poll_recipient_details`, `get_poll_poll_runs`, `get_poll_result`, `update_poll_result`, `check_for_new_fact_sheets`, `create_poll_reminder`, `get_poll_runs`, `create_poll_run`, `get_poll_run`, `update_poll_run`, `delete_poll_run`, `get_added_recipients_for_run`, `get_poll_results_for_user`, `get_poll_run_results`, `get_poll_runs_kpi_counts`, `get_recipients_for_poll_run`, `get_reminders`, `get_results_for_poll_run`, `set_status`, `get_all`, `create_poll_template`, `get_by_id`, `delete_by_id`. |
| **Leanix Reference Data** | `LEANIX_REFERENCE_DATA_CATALOGTOOL` | `True` | Manage leanix leanix reference data operations. Action-routed methods: `gettbmtaxonomy`, `getfactsheetsbysourcename`, `getlatestrecommendationrun`, `putusedtechnolotrecommendationcontroller`, `getusedtechnolotrecommendationcontroller`, `get_source_name_fact_sheets_id`, `getlinksbysourcename`, `putlinksbysourcename`, `putsourcehierarchylinkcontroller`, `putbulklinksbysourcename`, `putbulksourcehierarchylinkscontroller`, `getlinksbyfactsheettype`, `getlinkbysourcename`, `deletelinkbysourcename`, `getrequests`, `putrequests`, `getrequestscount`, `getrefresh`, `getrefreshes`, `postrefresh`, `refreshltlslinks`, `batchlinks`, `clonelinks`, `getlink`, `getconfigurationmodels`, `getconfiguration`, `putconfiguration`, `getsaasconfiguration`, `putsaasconfiguration`, `gettechcategoryconfiguration`, `puttechcategoryconfiguration`, `getbuscapconfiguration`, `putbuscapconfiguration`, `getprovisioning`, `putprovisioning`, `getlinks`, `clearduplicatelinks`, `validatelink`, `gettbmmigrationstatus`, `tbmmigrationstatusupdate`, `startmappingexport`, `getexportstatus`, `getexportfile`, `putimporttbm`, `precomputedrecommendations`, `getbusinesscapability`, `postbusinesscapability`, `filteredfactsheetscount`, `post_jobs`, `get_jobs`, `fetchbusinesscapabilitymetrics`, `post_managedsnapshotrequests`, `post_managedrestorationrequests`. |
| **Leanix Discovery Sap** | `LEANIX_DISCOVERY_SAP_EXTENSIONTOOL` | `True` | Manage leanix leanix discovery sap operations. Action-routed methods: `appcontroller_heartbeat`, `demodatacontroller_demodatalist`, `demodatacontroller_createcustomdemodata`, `integrationscontroller_integrationcreate`, `integrationscontroller_integrationslist`, `integrationscontroller_integrationget`, `integrationscontroller_integrationdelete`, `integrationscontroller_integrationpatch`, `integrationscontroller_integrationtriggersync`. |
| **Leanix Technology Discovery** | `LEANIX_TECHNOLOGY_DISCOVERYTOOL` | `True` | Manage leanix leanix technology discovery operations. Action-routed methods: `leanix_v1_microservice_discovery_yaml_manifest_register`, `leanix_v1_factsheets_sboms_ingest`, `leanix_v1_factsheets_sboms_ingest_1`, `getcomponentsbyapplication`, `searchcomponentsbypurl`, `getalltechstacks`, `updatetechstackbyqueryparam`, `createtechstack`, `deletetechstackbyqueryparam`, `previewmatches`, `gettechstackdetailsbyqueryparam`, `getaggregatedcounts`, `getfactsheetsbylibrary`, `getlibraryusagedetails`, `getversionsbylibrary`, `getlibraries`. |
| **Leanix Storage** | `LEANIX_STORAGETOOL` | `True` | Manage leanix leanix storage operations. Action-routed methods: `getavatar`, `setavatar`, `deleteavatar`, `getlogo`, `setlogo`, `deletelogo`, `getfiles`, `addfiletoworkspace`, `deletefiles`, `getfile`, `deletefile`, `getfilecontent`, `setfileowner`. |
| **Leanix Survey** | `LEANIX_SURVEYTOOL` | `True` | Manage leanix leanix survey operations. Action-routed methods: `get_poll`, `update_poll`, `delete_poll_by_id`, `get_poll_run_by_id`, `update_poll_run`, `delete_poll_run`, `update_poll_run_status`, `get_poll_result`, `update_poll_result`, `get_polls`, `create_poll`, `get_poll_runs`, `create_poll_run`, `create_poll_reminder`, `check_for_new_fact_sheets`, `replay_all_workspaces`, `replay_workspace_by_id`, `get_polls_for_fact_sheet`, `get_recipients_and_fact_sheets_for_poll`, `get_poll_runs_by_poll`, `get_poll_count`, `get_all_templates`, `get_templates_by_id`, `get_poll_results_for_user`, `get_all_reminders_for_poll_run`, `get_recipients_and_fact_sheets_for_poll_run`, `getpollrunresultsasexcel`, `get_poll_results_by_poll_run_id`, `get_added_recipients_for_poll_run`. |
| **Leanix Synclog** | `LEANIX_SYNCLOGTOOL` | `True` | Manage leanix leanix synclog operations. Action-routed methods: `getsyncitems`, `addsyncitembatch`, `getsynchronizations`, `createsynchronization`, `getsyncitems_1`, `deletesyncitems`, `getsynchronization`, `updatesynchronization`, `gettopics`, `gettriggers`, `requestabortion`. |
| **Leanix Todo** | `LEANIX_TODOTOOL` | `True` | Manage leanix leanix todo operations. Action-routed methods: `managedrestorationrequests`, `managedsnapshotrequests`, `accepttodo`, `assigntome`, `get`, `createtodo`, `deletetodos`, `query`, `rejecttodo`, `replyandclosetodo`, `upserttodos`. |
| **Leanix Transformations** | `LEANIX_TRANSFORMATIONSTOOL` | `True` | Manage leanix leanix transformations operations. Action-routed methods: `createtransformation`, `gettransformations`, `gettransformation`, `puttransformation`, `deletetransformation`, `gettransformationcustomimpacts`, `posttransformationcustomimpacts`, `puttransformationcustomimpacts`, `deletetransformationcustomimpacts`, `posttransformationexecution`, `posttransformationsexecution`. |
| **Leanix Webhooks** | `LEANIX_WEBHOOKSTOOL` | `True` | Manage leanix leanix webhooks operations. Action-routed methods: `getcustomeventtags`, `createcustomeventtag`, `updatecustomeventtag`, `deletecustomeventtag`, `createevent`, `createeventbatch`, `geteventtags`, `getsubscriptions`, `createsubscription`, `getsubscription`, `updatesubscription`, `deletesubscription`, `getsubscriptiondeliveries`, `getsubscriptionevents`, `getsubscriptionstatus`, `getsubscriptionstatuses`, `updatesubscriptioncursor`. |
| **Graphql** | `GRAPHQLTOOL` | `True` | Execute raw GraphQL queries and mutations natively on LeanIX Pathfinder API. |

Detailed tool schemas, parameter shapes, and validation constraints are preserved in [docs/mcp.md](file:///home/apps/workspace/agent-packages/agents/leanix-agent/docs/mcp.md).

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

Detailed graph node architecture explanations, custom skill configurations, and agentic trace guides are available in [docs/agent.md](file:///home/apps/workspace/agent-packages/agents/leanix-agent/docs/agent.md).

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
