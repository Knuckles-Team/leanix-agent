# LeanIX Discovery and Linking

Discover and link external inventory to LeanIX FactSheets: SaaS discovery integrations, SAP and SAP-extension discovery, AI-agent discovery, discovery items with linking and rejection in both linking versions, technology discovery with SBOM and microservice ingestion and tech stacks, and Apptio connector runs. Use when external systems must be matched to FactSheets or technology usage must be read. Do NOT use for general integrations (leanix-integrations).

# LeanIX Discovery and Linking

Discovery finds what exists outside the inventory. Each discovered item is previewed, linked to a FactSheet or rejected; technology discovery records libraries and versions per application.

## When to use
- Configure discovery integrations and read what they found.
- List discovery items, preview a match, link or reject.
- Read and change auto-linking settings.
- Register microservice manifests and SBOMs; search components by package URL.
- Read and write tech stacks; run and read Apptio exports.

## When NOT to use
- Collibra, ServiceNow, Signavio and workflow integrations: use leanix-integrations.

## Workflow
1. Read the integration and its status.
2. List discovery items; preview before linking.
3. Link or reject one item at a time and read the result back.

## Safety
- Credentials are write-only; never echo them.
- Linking and rejecting change the inventory; ask before bulk actions.

## Tools (104)

Each tool is one API operation; pass its path, query and body fields as named arguments.


### Apptio Connector

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_apptio_connector_getallconfigurations` | GET | Get all configurations |
| `leanix_leanix_apptio_connector_getconfigurations` | GET | Get configuration by id |
| `leanix_leanix_apptio_connector_getresults` | GET | Get run results |
| `leanix_leanix_apptio_connector_getresultsurl` | GET | Get results_url of a run |
| `leanix_leanix_apptio_connector_getstats` | GET | Get stats of a run |
| `leanix_leanix_apptio_connector_getstatus` | GET | Get run status |
| `leanix_leanix_apptio_connector_getwarnings` | GET | Get warnings of a run |
| `leanix_leanix_apptio_connector_create` | POST | Create a new run |
| `leanix_leanix_apptio_connector_upsertconfiguration` | PUT | Upsert a configuration |
| `leanix_leanix_apptio_connector_deleteconfiguration` | DELETE | Delete a configuration |

### Discovery Ai Agents

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_discovery_ai_agents_get_integrations` | GET | Call GET /integrations |
| `leanix_leanix_discovery_ai_agents_get_integrations_id` | GET | Call GET /integrations/{id} |
| `leanix_leanix_discovery_ai_agents_post_agents_a2a_cards` | POST | Call POST /agents/a2a/cards |
| `leanix_leanix_discovery_ai_agents_post_integrations` | POST | Call POST /integrations |
| `leanix_leanix_discovery_ai_agents_put_integrations_id_capabilities` | PUT | Call PUT /integrations/{id}/capabilities |
| `leanix_leanix_discovery_ai_agents_put_integrations_id_credentials` | PUT | Call PUT /integrations/{id}/credentials |
| `leanix_leanix_discovery_ai_agents_put_integrations_id_name` | PUT | Call PUT /integrations/{id}/name |
| `leanix_leanix_discovery_ai_agents_put_integrations_id_status` | PUT | Call PUT /integrations/{id}/status |

### Discovery Linking V1

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_discovery_linking_v1_discovery_itemsfilter_options` | GET | Get filter options for discovery items |
| `leanix_leanix_discovery_linking_v1_discovery_itemsid` | GET | Get a discovery item by ID |
| `leanix_leanix_discovery_linking_v1_discovery_itemsidpre_validate_linkfactsheetid` | GET | Pre-validate linking a discovery item to a fact_sheet |
| `leanix_leanix_discovery_linking_v1_discovery_itemskpi_values` | GET | Get KPI values for discovery items |
| `leanix_leanix_discovery_linking_v1_discovery_itemslinking_progressid` | GET | Get linking progress for a discovery item |
| `leanix_leanix_discovery_linking_v1_factsheetsiddetails` | GET | Get details of a fact_sheet |
| `leanix_leanix_discovery_linking_v1_bulk_link` | POST | Link multiple discovery items to fact_sheets |
| `leanix_leanix_discovery_linking_v1_discovery_items` | POST | Get discovery items |
| `leanix_leanix_discovery_linking_v1_discovery_itemslinking_progress` | POST | Get Bulk linking progress for discovery items |
| `leanix_leanix_discovery_linking_v1_link` | POST | Link a discovery item to a fact_sheet |
| `leanix_leanix_discovery_linking_v1_reject` | POST | Reject a linking suggestion |

### Discovery Linking V2

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_discovery_linking_v2_get_factsheets_id_links` | GET | Get discovery items linked to a fact sheet |
| `leanix_leanix_discovery_linking_v2_get_origin_discoveryitems` | GET | Get discovery items with filtering, sorting and pagination |
| `leanix_leanix_discovery_linking_v2_get_origin_discoveryitems_export` | GET | Export discovery items to CSV |
| `leanix_leanix_discovery_linking_v2_get_origin_discoveryitems_id` | GET | Get discovery item by ID |
| `leanix_leanix_discovery_linking_v2_get_origin_discoveryitems_id_changelogs` | GET | Get change logs for a discovery item |
| `leanix_leanix_discovery_linking_v2_get_origin_discoveryitems_linkingprogress` | GET | Get linking progress for a discovery item |
| `leanix_leanix_discovery_linking_v2_get_origin_discoveryitems_sourceconfigs` | GET | Get source configurations |
| `leanix_leanix_discovery_linking_v2_get_origin_insights` | GET | Get insights for discovery inbox |
| `leanix_leanix_discovery_linking_v2_get_origin_internal_events` | GET | Get ECST events |
| `leanix_leanix_discovery_linking_v2_get_origin_internal_events_compaction` | GET | Load compaction events |
| `leanix_leanix_discovery_linking_v2_get_origin_settings` | GET | Get discovery inbox settings |
| `leanix_leanix_discovery_linking_v2_get_origin_settings_autolinking` | GET | Get auto-linking configuration |
| `leanix_leanix_discovery_linking_v2_post_origin_discoveryitems_id_preview` | POST | Get discovery item preview |
| `leanix_leanix_discovery_linking_v2_post_origin_push` | POST | Initialize push to inbox |
| `leanix_leanix_discovery_linking_v2_post_origin_push_id` | POST | Push discoveries to inbox |
| `leanix_leanix_discovery_linking_v2_put_origin_discoveryitems_id_link` | PUT | Link discovery item to fact sheets |
| `leanix_leanix_discovery_linking_v2_put_origin_discoveryitems_link` | PUT | Bulk link discovery items to fact sheets |
| `leanix_leanix_discovery_linking_v2_put_origin_discoveryitems_reject` | PUT | Reject discovery items |
| `leanix_leanix_discovery_linking_v2_put_origin_settings_autolinking` | PUT | Update auto-linking configuration |

### Discovery Saas

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_discovery_saas_getavailableintegrations` | GET | Get list of available integrations for the workspace. |
| `leanix_leanix_discovery_saas_getdiscoveries` | GET | Get list of discoveries. |
| `leanix_leanix_discovery_saas_getdiscoveryprioritybyid` | GET | Get discovery priority by ID. |
| `leanix_leanix_discovery_saas_getintegrationbyid` | GET | Get integration details by ID. |
| `leanix_leanix_discovery_saas_getintegrations` | GET | Get list of integrations in the workspace. |
| `leanix_leanix_discovery_saas_postintegration` | POST | Connect a new integration. |
| `leanix_leanix_discovery_saas_putintegrationcapabilitiesbyid` | PUT | Update capabilities of the integration. |
| `leanix_leanix_discovery_saas_putintegrationcredentialsbyid` | PUT | Update credentials of the integration. |
| `leanix_leanix_discovery_saas_putintegrationnamebyid` | PUT | Update name of the integration. |
| `leanix_leanix_discovery_saas_putintegrationstatusbyid` | PUT | Update status of the integration. |
| `leanix_leanix_discovery_saas_deleteintegrationbyid` | DELETE | Delete integration by ID. Only integrations in 'duplicate' status can be deleted. |

### Discovery Sap

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_discovery_sap_appcontroller_heartbeat` | GET | Call GET /heartbeat |
| `leanix_leanix_discovery_sap_demodatacontroller_demodatalist` | GET | Call GET /demo-data |
| `leanix_leanix_discovery_sap_integrationscontroller_integrationget` | GET | Call GET /integrations/{id} |
| `leanix_leanix_discovery_sap_integrationscontroller_integrationslist` | GET | Call GET /integrations |
| `leanix_leanix_discovery_sap_demodatacontroller_createcustomdemodata` | POST | Call POST /demo-data |
| `leanix_leanix_discovery_sap_integrationscontroller_integrationcreate` | POST | Call POST /integrations |
| `leanix_leanix_discovery_sap_integrationscontroller_integrationtriggersync` | POST | Call POST /integrations/{id}/sync |
| `leanix_leanix_discovery_sap_integrationscontroller_integrationpatch` | PATCH | Call PATCH /integrations/{id_} |
| `leanix_leanix_discovery_sap_integrationscontroller_integrationdelete` | DELETE | Call DELETE /integrations/{id_} |

### Discovery Sap Extension

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_discovery_sap_extension_get_check_data_model` | GET | Call GET /check-data-model |
| `leanix_leanix_discovery_sap_extension_get_checkdatamodel` | GET | Call GET /check_data_model |
| `leanix_leanix_discovery_sap_extension_get_cloud_foundry_domains` | GET | Call GET /cloud-foundry/domains |
| `leanix_leanix_discovery_sap_extension_get_cloud_foundry_subject_pattern` | GET | Call GET /cloud-foundry/subject-pattern |
| `leanix_leanix_discovery_sap_extension_get_credentials_type` | GET | Call GET /credentials/{type} |
| `leanix_leanix_discovery_sap_extension_get_health` | GET | Call GET /health |
| `leanix_leanix_discovery_sap_extension_get_integrations` | GET | Call GET /integrations |
| `leanix_leanix_discovery_sap_extension_get_kyma_spec_suggestions` | GET | Call GET /kyma/spec-suggestions |
| `leanix_leanix_discovery_sap_extension_post_cloud_foundry_infer_certificate_domain` | POST | Call POST /cloud-foundry/infer-certificate-domain |
| `leanix_leanix_discovery_sap_extension_post_credentials_verify_cms` | POST | Call POST /credentials/verify/cms |
| `leanix_leanix_discovery_sap_extension_post_integrations` | POST | Call POST /integrations |
| `leanix_leanix_discovery_sap_extension_post_integrations_credentials_verify` | POST | Call POST /integrations/credentials/verify |
| `leanix_leanix_discovery_sap_extension_post_integrations_id_sync` | POST | Call POST /integrations/{id}/sync |
| `leanix_leanix_discovery_sap_extension_post_kyma_verify_api_url` | POST | Call POST /kyma/verify-api-url |
| `leanix_leanix_discovery_sap_extension_patch_integrations_id` | PATCH | Call PATCH /integrations/{id} |
| `leanix_leanix_discovery_sap_extension_put_integrations_id_credentials_build` | PUT | Call PUT /integrations/{id}/credentials/build |
| `leanix_leanix_discovery_sap_extension_put_integrations_id_credentials_cloud_foundry` | PUT | Call PUT /integrations/{id}/credentials/cloud-foundry |
| `leanix_leanix_discovery_sap_extension_put_integrations_id_credentials_cms` | PUT | Call PUT /integrations/{id}/credentials/cms |
| `leanix_leanix_discovery_sap_extension_put_integrations_id_credentials_kyma` | PUT | Call PUT /integrations/{id}/credentials/kyma |
| `leanix_leanix_discovery_sap_extension_delete_integrations_id_` | DELETE | Call DELETE /integrations/{id_} |

### Technology Discovery

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_technology_discovery_getaggregatedcounts` | GET | Get aggregated tech stack counts |
| `leanix_leanix_technology_discovery_getalltechstacks` | GET | Retrieve all tech stacks |
| `leanix_leanix_technology_discovery_getcomponentsbyapplication` | GET | Retrieve library components for a business application |
| `leanix_leanix_technology_discovery_getfactsheetsbylibrary` | GET | Get fact sheets using a specific library |
| `leanix_leanix_technology_discovery_getlibraries` | GET | Retrieve libraries with aggregated counts |
| `leanix_leanix_technology_discovery_getlibraryusagedetails` | GET | Get detailed library usage information |
| `leanix_leanix_technology_discovery_gettechstackdetailsbyqueryparam` | GET | Get tech stack details |
| `leanix_leanix_technology_discovery_getversionsbylibrary` | GET | Get library versions by library name |
| `leanix_leanix_technology_discovery_leanix_v1_factsheets_sboms_ingest_1` | GET | Get the status of an SBOM ingestion job |
| `leanix_leanix_technology_discovery_searchcomponentsbypurl` | GET | Search components by PURL |
| `leanix_leanix_technology_discovery_createtechstack` | POST | Create a new custom tech stack |
| `leanix_leanix_technology_discovery_leanix_v1_factsheets_sboms_ingest` | POST | Attach Software Bill of Materials (SBOM) to a Fact Sheet |
| `leanix_leanix_technology_discovery_previewmatches` | POST | Preview tech stack rule matches |
| `leanix_leanix_technology_discovery_leanix_v1_microservice_discovery_yaml_manifest_register` | PUT | Microservice Discovery Through YAML Manifest File |
| `leanix_leanix_technology_discovery_updatetechstackbyqueryparam` | PUT | Update an existing custom tech stack |
| `leanix_leanix_technology_discovery_deletetechstackbyqueryparam` | DELETE | Delete a custom tech stack |
