---
name: leanix-integrations
skill_type: skill
description: >-
  Run LeanIX integrations: the integration API with processor configurations and
  synchronization runs, Collibra, ServiceNow and Signavio connectors, workspace
  automations, webhook subscriptions and events, managed code execution, and workspace
  file storage. Use when data must move between LeanIX and another system or an event must
  trigger work. Do NOT use for discovery (leanix-discovery-and-linking).
license: MIT
tags: [leanix, integration, webhooks, collibra, servicenow, signavio, automation, mcp]
metadata:
  author: Knuckles-Team
  version: '1.0.0'
---
# LeanIX Integrations

Integrations keep LeanIX and neighbouring systems in step. A configuration says what maps to what, a synchronization run moves the data and reports progress and warnings, and webhooks tell other systems when something changed.

## When to use
- Define processor configurations and start, watch and stop synchronization runs.
- Configure and run Collibra, ServiceNow and Signavio synchronizations.
- Manage automation templates and scripts.
- Create webhook subscriptions and read deliveries and events.
- Run managed code; manage workspace files, logo and avatar.

## When NOT to use
- Discovering external items: use leanix-discovery-and-linking.

## Workflow
1. Read the configuration and validate credentials.
2. Start a run, then poll its progress and status until it finishes.
3. Read warnings and results; report counts.

## Safety
- Stopping or aborting a run can leave data half-synced; ask first.
- Never print integration credentials or webhook secrets.

## Tools (164)

Each tool is one API operation; pass its path, query and body fields as named arguments.


### Automations

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_automations_instancescontroller_findall` | GET | Call GET /instances |
| `leanix_leanix_automations_instancescontroller_quota` | GET | Call GET /instances/quota |
| `leanix_leanix_automations_statisticscontroller_getstatistics` | GET | Call GET /statistics |
| `leanix_leanix_automations_templatescontroller_getalltemplates` | GET | Call GET /templates |
| `leanix_leanix_automations_templatescontroller_gettemplate` | GET | Call GET /templates/{id} |
| `leanix_leanix_automations_scriptscontroller_createmcescript` | POST | Call POST /scripts |
| `leanix_leanix_automations_snapshotscontroller_managedrestorationrequests` | POST | Call POST /snapshots/managed_restoration_requests |
| `leanix_leanix_automations_snapshotscontroller_managesnapshotrequests` | POST | Call POST /snapshots/managed_snapshot_requests |
| `leanix_leanix_automations_templatescontroller_createtemplate` | POST | Call POST /templates |
| `leanix_leanix_automations_scriptscontroller_updatemcescript` | PUT | Call PUT /scripts/{script_id} |
| `leanix_leanix_automations_templatescontroller_patchtemplate` | PATCH | Call PATCH /templates/{id_} |
| `leanix_leanix_automations_templatescontroller_updatetemplate` | PUT | Call PUT /templates/{id_} |
| `leanix_leanix_automations_templatescontroller_deletetemplate` | DELETE | Call DELETE /templates/{id_} |

### Integration Api

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_integration_api_createinazure` | GET | Provides storage resources that can be used for synchronisation runs. It creates a blob file in Azure Storage. |
| `leanix_leanix_integration_api_get_examples_advancedexample` | GET | Returns an advanced example including an Input object and processor configuration |
| `leanix_leanix_integration_api_get_examples_starterexample` | GET | Returns a starter example including an Input object and processor configuration |
| `leanix_leanix_integration_api_getprocessorconfigurations` | GET | Returns a list of available processor configurations |
| `leanix_leanix_integration_api_getsynchronizationrundebuginformation` | GET | Provides the Debug logs generated during the synchronization runs. |
| `leanix_leanix_integration_api_getsynchronizationrundebugvariables` | GET | Provides the Debug variables generated during the synchronization runs. |
| `leanix_leanix_integration_api_getsynchronizationrunprogress` | GET | Shows the progress of a synchronization run, it gives updated counters of the run level that is in execution. |
| `leanix_leanix_integration_api_getsynchronizationrunresults` | GET | Returns the results of a finished synchronization run |
| `leanix_leanix_integration_api_getsynchronizationrunresultsurl` | GET | Returns the url to the results of a finished synchronization run |
| `leanix_leanix_integration_api_getsynchronizationrunsstatuslist` | GET | Returns the status of all existing synchronization runs |
| `leanix_leanix_integration_api_getsynchronizationrunstats` | GET | Returns detailed statistics about the execution of a synchronization run |
| `leanix_leanix_integration_api_getsynchronizationrunstatus` | GET | Returns the status of an existing synchronization run |
| `leanix_leanix_integration_api_getsynchronizationrunwarnings` | GET | Returns the warnings of a synchronization run |
| `leanix_leanix_integration_api_createsynchronizationfastrun` | POST | Creates a fast synchronization run. |
| `leanix_leanix_integration_api_createsynchronizationfastrunwithconfig` | POST | Starts a new fast run synchronization using the processor configuration and input object provided in the... |
| `leanix_leanix_integration_api_createsynchronizationrun` | POST | Creates a synchronization run. |
| `leanix_leanix_integration_api_createsynchronizationrunwithconfig` | POST | Starts a new synchronization run using the processor configuration and input object provided in the request.... |
| `leanix_leanix_integration_api_createsynchronizationrunwithexecutiongroup` | POST | Starts a new synchronization run using combined processor configuration within an execution group and input... |
| `leanix_leanix_integration_api_createsynchronizationrunwithexecutiongroupandurlinput` | POST | Starts a new synchronization run using a DataProvider information to obtain the LDIF input, but choose a... |
| `leanix_leanix_integration_api_createsynchronizationrunwithurlinput` | POST | Starts a new synchronization run using a DataProvider information to obtain the LDIF input |
| `leanix_leanix_integration_api_startsynchronizationrun` | POST | Starts an existing but not yet started synchronization run |
| `leanix_leanix_integration_api_stopsynchronizationrun` | POST | Stops a running synchronization run |
| `leanix_leanix_integration_api_upsertprocessorconfiguration` | PUT | Inserts a new processor configuration or updates an existing one |
| `leanix_leanix_integration_api_deleteprocessorconfiguration` | DELETE | Delete a single processor configuration |

### Integration Collibra

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_integration_collibra_getassetstatuses` | GET | Returns list of available collibra asset statuses. |
| `leanix_leanix_integration_collibra_getassettypes` | GET | Returns list of available collibra asset types. |
| `leanix_leanix_integration_collibra_getattributetypes` | GET | Returns list of available collibra attribute types. |
| `leanix_leanix_integration_collibra_getattributetypesforassettype` | GET | Returns list of available collibra attribute types for the supplied asset type. |
| `leanix_leanix_integration_collibra_getattributetypesforassettypebyscope` | GET | Returns list of available collibra attribute types for the supplied asset type (grouped by Scope). |
| `leanix_leanix_integration_collibra_getcollibracredentialsbyid` | GET | Retrieves credentials for current EAM workspace by id. |
| `leanix_leanix_integration_collibra_getcommunities` | GET | Returns list of available collibra communities. |
| `leanix_leanix_integration_collibra_getcomplexrelationtypes` | GET | Returns list of available complex relations. |
| `leanix_leanix_integration_collibra_getconfigurationbyid` | GET | Retrieves configuration for current EAM workspace by id. |
| `leanix_leanix_integration_collibra_getconfigurations` | GET | Returns a list of available configurations for current EAM workspace. |
| `leanix_leanix_integration_collibra_getcredentials` | GET | Returns a list of available credentials for current EAM workspace. |
| `leanix_leanix_integration_collibra_getdomains` | GET | Returns list of available collibra domains. |
| `leanix_leanix_integration_collibra_getfeaturetoggles` | GET | Returns list of available feature toggles for current EAM workspace. |
| `leanix_leanix_integration_collibra_getfields` | GET | Returns list of available fields for a given Fact Sheet type. |
| `leanix_leanix_integration_collibra_getoverview` | GET | Returns overview of configuration for current workspace. |
| `leanix_leanix_integration_collibra_getrelationfields` | GET | Returns list of available fields for the given relation. |
| `leanix_leanix_integration_collibra_getrelations` | GET | Returns list of available relations for a given Fact Sheet type. |
| `leanix_leanix_integration_collibra_getrelationtypes` | GET | Returns list of available simple relation types for the supplied from and to asset type ids including... |
| `leanix_leanix_integration_collibra_getresourceroles` | GET | Returns list of available collibra resource_roles. |
| `leanix_leanix_integration_collibra_getresponsibilityroles` | GET | Returns list of available collibra responsibility_roles. |
| `leanix_leanix_integration_collibra_getstatus` | GET | Returns status of configurations for current EAM workspace. |
| `leanix_leanix_integration_collibra_getsubscriptionroles` | GET | Returns list of available subscription roles for a given Fact Sheet type. |
| `leanix_leanix_integration_collibra_validatecollibracredentialsbyid` | GET | Validates the given credentials id with Collibra |
| `leanix_leanix_integration_collibra_createcollibracredentials` | POST | Creates collibra credentials for given EAM Workspace. |
| `leanix_leanix_integration_collibra_createconfiguration` | POST | Creates configuration for current EAM workspace. |
| `leanix_leanix_integration_collibra_createsynchronizationrun` | POST | Creates synchronization run for current EAM workspace. |
| `leanix_leanix_integration_collibra_updatecollibracredentials` | PUT | Updates existing collibra credentials for given EAM Workspace by id. |
| `leanix_leanix_integration_collibra_updateconfiguration` | PUT | Updates an existing configuration for current EAM workspace by id. |
| `leanix_leanix_integration_collibra_deleteconfiguration` | DELETE | Deletes an existing configuration for current EAM workspace by id. |

### Integration Servicenow

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_integration_servicenow_getaggregatedfactsheetsummary` | GET | (INTERNAL) Provide summary integration information for a linked fact sheet |
| `leanix_leanix_integration_servicenow_getaggregatedsoftwareinformation` | GET | (INTERNAL) Provide information of detected aggregated software |
| `leanix_leanix_integration_servicenow_getallconfigurations` | GET | (INTERNAL) Retrieve all ServiceNow configurations |
| `leanix_leanix_integration_servicenow_getavailablerelcirelations` | GET | (INTERNAL) Retrieve all possible ServiceNow CMDB_REL_CI relations between two tables |
| `leanix_leanix_integration_servicenow_getconfiguration` | GET | (INTERNAL) Retrieve a ServiceNow configuration |
| `leanix_leanix_integration_servicenow_getcurrentlyrunningorlastcreatedrun` | GET | (INTERNAL) Retrieve information about the current running synchronization for a given configuration or... |
| `leanix_leanix_integration_servicenow_getfilterforfactsheet` | GET | (INTERNAL) Retrieve all fact sheet filter options found for a given configuration |
| `leanix_leanix_integration_servicenow_getfilterforprovider` | GET | (INTERNAL) Retrieve all providers filter options found for a given configuration |
| `leanix_leanix_integration_servicenow_getfilters` | GET | (INTERNAL) Retrieve all assigned ServiceNow filters for a given table |
| `leanix_leanix_integration_servicenow_getfiltersforhardware` | GET | (INTERNAL) Retrieve all hardware filter options where aggregated software is installed for a given... |
| `leanix_leanix_integration_servicenow_getinstalledservicenowpluginversion` | GET | (INTERNAL) Retrieve the installed ServiceNow plugin version |
| `leanix_leanix_integration_servicenow_getmappingtablerelations` | GET | (INTERNAL) Retrieve all available ServiceNow MAPPING_TABLE relations for a given table |
| `leanix_leanix_integration_servicenow_getreferencefieldrelations` | GET | (INTERNAL) Retrieve all available reference fields between two ServiceNow tables |
| `leanix_leanix_integration_servicenow_getservicenowaggregatedhardware` | GET | (INTERNAL) Retrieve hardware information for a given software installation |
| `leanix_leanix_integration_servicenow_getservicenowaggregatedsoftware` | GET | (INTERNAL) Retrieve software installations found for a given fact sheet |
| `leanix_leanix_integration_servicenow_getservicenowmetadata` | GET | (INTERNAL) Retrieve metadata of for a ServiceNow table |
| `leanix_leanix_integration_servicenow_getservicenowsyncconstraintrules` | GET | (INTERNAL) Retrieve all constraint rules for a given ServiceNow table |
| `leanix_leanix_integration_servicenow_getstatusoverview` | GET | (INTERNAL) Provide statistics for A&L |
| `leanix_leanix_integration_servicenow_gettables` | GET | (INTERNAL) Retrieve all available ServiceNow table names in ServiceNow |
| `leanix_leanix_integration_servicenow_getversionbyid` | GET | (INTERNAL) Retrieve one specific ServiceNow configuration-version by Id |
| `leanix_leanix_integration_servicenow_getversions` | GET | (INTERNAL) Retrieve all ServiceNow configuration-versions |
| `leanix_leanix_integration_servicenow_sendprompt` | GET | (INTERNAL) Retrieve an AI generated field mapping for a FactSheet type |
| `leanix_leanix_integration_servicenow_sendpromptv2` | GET | (INTERNAL) (V2) Retrieve an AI generated field mapping for a FactSheet type |
| `leanix_leanix_integration_servicenow_validateconfiguration` | POST | (INTERNAL) Validate the uploaded ServiceNow configuration and provide list of issues |
| `leanix_leanix_integration_servicenow_validateservicenowcredentials` | GET | (INTERNAL) Validate the credentials from an existing ServiceNow configuration |
| `leanix_leanix_integration_servicenow_abortallpendingandrunningsynchronizations` | POST | (INTERNAL) Trigger the abortion of all the running and pending synchronizations for a configuration |
| `leanix_leanix_integration_servicenow_abortsynchronization` | POST | (INTERNAL) Trigger the abortion of a specific synchronization run |
| `leanix_leanix_integration_servicenow_changes` | POST | (INTERNAL) Consume ServiceNow events for changes on the ServiceNow side |
| `leanix_leanix_integration_servicenow_createconfiguration` | POST | (INTERNAL) Create a new ServiceNow configuration |
| `leanix_leanix_integration_servicenow_hooks` | POST | (INTERNAL) Consume LeanIX events for changes on the LeanIX side |
| `leanix_leanix_integration_servicenow_synchronize` | POST | (INTERNAL) Submit a synchronization job to be enqueued for execution |
| `leanix_leanix_integration_servicenow_updateconfiguration` | PUT | (INTERNAL) Update a ServiceNow configuration |
| `leanix_leanix_integration_servicenow_deleteconfiguration` | DELETE | (INTERNAL) Delete a ServiceNow configuration |

### Integration Signavio

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_integration_signavio_createcategory` | GET | Fetch dictionary categories information |
| `leanix_leanix_integration_signavio_getconfiguration` | GET | Fetch a configuration by id |
| `leanix_leanix_integration_signavio_getconfigurations` | GET | List of configurations |
| `leanix_leanix_integration_signavio_getdirectories` | GET | List of SAP Signavio process directories that match with the search string for the given configuration |
| `leanix_leanix_integration_signavio_getfactsheetfields` | GET | List all fields on a Fact Sheet available for mappings |
| `leanix_leanix_integration_signavio_getformations` | GET | List of formations |
| `leanix_leanix_integration_signavio_getlabels` | GET | Provide the labels (names) for requested objects, like processes or directories. |
| `leanix_leanix_integration_signavio_getlatestsynchronizationrunanalysis` | GET | Get analysis for the latest synchronization run |
| `leanix_leanix_integration_signavio_getprocessfields` | GET | List of processes that match with the search string |
| `leanix_leanix_integration_signavio_getsignavioglossaryitemfields` | GET | List of fields of a dictionary item available for mappings |
| `leanix_leanix_integration_signavio_getsignavioprocessfields` | GET | List all SAP Signavio fields available for mappings |
| `leanix_leanix_integration_signavio_getsynchronizationrunanalysis` | GET | Get analysis for a synchronization run |
| `leanix_leanix_integration_signavio_analyzelatestsynchronizationrun` | POST | Analyze the latest synchronization run |
| `leanix_leanix_integration_signavio_analyzesynchronizationrun` | POST | Analyze a synchronization run |
| `leanix_leanix_integration_signavio_cancelsynchronization` | POST | Trigger a synchronization cancellation |
| `leanix_leanix_integration_signavio_createconfiguration` | POST | Create a configuration |
| `leanix_leanix_integration_signavio_synchronizeconfiguration` | POST | Trigger a synchronization run |
| `leanix_leanix_integration_signavio_unassignformation` | POST | Unassign formation from configuration |
| `leanix_leanix_integration_signavio_updateconfiguration` | PUT | Update a configuration |
| `leanix_leanix_integration_signavio_deleteconfiguration` | DELETE | Delete a configuration |

### Managed Code Execution

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_managed_code_execution_getallsecrets` | GET | Get all Secrets |
| `leanix_leanix_managed_code_execution_getexecutionconfiguration` | GET | Show details of specified ExecutionConfiguration |
| `leanix_leanix_managed_code_execution_getexecutionconfigurationhistory` | GET | List all versions of a given ExecutionConfiguration |
| `leanix_leanix_managed_code_execution_getexecutionconfigurations` | GET | List all available ExecutionConfigurations |
| `leanix_leanix_managed_code_execution_getexecutionconfigurationsbysecretid` | GET | Get ExecutionConfigurations that reference a Secret |
| `leanix_leanix_managed_code_execution_getexecutionlog` | GET | Get a specific ExecutionLog for ExecutionConfiguration |
| `leanix_leanix_managed_code_execution_getexecutionlogs` | GET | List all available ExecutionLogs for one ExecutionConfiguration |
| `leanix_leanix_managed_code_execution_getsecretbyid` | GET | Get a Secret by ID |
| `leanix_leanix_managed_code_execution_createexecutionconfiguration` | POST | Create a new ExecutionConfiguration |
| `leanix_leanix_managed_code_execution_createsecret` | POST | Create a new Secret |
| `leanix_leanix_managed_code_execution_updateexecutionconfiguration` | PUT | Update an existing ExecutionConfiguration |
| `leanix_leanix_managed_code_execution_updateexecutionconfigurationcapability` | PUT | Update capability of an ExecutionConfiguration |
| `leanix_leanix_managed_code_execution_updatesecret` | PUT | Update a Secret |
| `leanix_leanix_managed_code_execution_deleteexecutionconfiguration` | DELETE | Delete an existing ExecutionConfiguration |
| `leanix_leanix_managed_code_execution_deletesecret` | DELETE | Delete a Secret |

### Storage

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_storage_getavatar` | GET | Retrieve a user's avatar |
| `leanix_leanix_storage_getfile` | GET | Retrieve workspace file |
| `leanix_leanix_storage_getfilecontent` | GET | Retrieve workspace file contents |
| `leanix_leanix_storage_getfiles` | GET | Retrieve a list of workspace files |
| `leanix_leanix_storage_getlogo` | GET | Retrieve a fact sheet logo |
| `leanix_leanix_storage_addfiletoworkspace` | POST | Upload a new file. |
| `leanix_leanix_storage_setavatar` | PUT | Update a user's avatar |
| `leanix_leanix_storage_setfileowner` | PUT | Update file owner |
| `leanix_leanix_storage_setlogo` | PUT | Assign a logo to a fact sheet |
| `leanix_leanix_storage_deleteavatar` | DELETE | Delete a user avatar |
| `leanix_leanix_storage_deletefile` | DELETE | Delete workspace file |
| `leanix_leanix_storage_deletefiles` | DELETE | Delete workspace files |
| `leanix_leanix_storage_deletelogo` | DELETE | Delete a fact sheet logo |

### Webhooks

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_webhooks_getcustomeventtags` | GET | Get custom event tags with an identifier for the given workspace and service. |
| `leanix_leanix_webhooks_geteventtags` | GET | Get all event tags for the given workspace. |
| `leanix_leanix_webhooks_getsubscription` | GET | Get a subscription by id. |
| `leanix_leanix_webhooks_getsubscriptiondeliveries` | GET | Get the deliveries of a given subscription. |
| `leanix_leanix_webhooks_getsubscriptionevents` | GET | Get the next batch of events for a PULL subscription. |
| `leanix_leanix_webhooks_getsubscriptions` | GET | Get all subscriptions. |
| `leanix_leanix_webhooks_getsubscriptionstatus` | GET | Get subscription status by subscription id. |
| `leanix_leanix_webhooks_getsubscriptionstatuses` | GET | Get subscription statuses for all subscriptions. |
| `leanix_leanix_webhooks_createcustomeventtag` | POST | Create a custom event tag. |
| `leanix_leanix_webhooks_createevent` | POST | Create a new event. |
| `leanix_leanix_webhooks_createeventbatch` | POST | Create a batch of new events. |
| `leanix_leanix_webhooks_createsubscription` | POST | Create a new subscription. |
| `leanix_leanix_webhooks_updatecustomeventtag` | PUT | Update a custom event tag. |
| `leanix_leanix_webhooks_updatesubscription` | PUT | Update a subscription by id. |
| `leanix_leanix_webhooks_updatesubscriptioncursor` | PUT | Marks events up to the given offset as consumed for the given subscription. |
| `leanix_leanix_webhooks_deletecustomeventtag` | DELETE | Delete a custom event tag. |
| `leanix_leanix_webhooks_deletesubscription` | DELETE | Delete a subscription by id. |
