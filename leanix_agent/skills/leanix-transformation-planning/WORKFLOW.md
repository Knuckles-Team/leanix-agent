# LeanIX Transformation Planning

Plan and communicate architecture change in LeanIX: transformations and their impacts, impact projections, navigation collections and presentations, documents and templates, to-dos, surveys and polls with runs and results, and metrics schemas, KPIs and charts. Use when the agent must model a change, ask stakeholders, report progress or publish a view. Do NOT use for inventory records (leanix-factsheet-inventory).

# LeanIX Transformation Planning

Planning work sits on top of the inventory: a transformation groups changes and computes their impact, surveys collect owner input on FactSheets, documents and presentations carry the story, and metrics track progress over time.

## When to use
- Create, read, update and execute transformations and their custom impacts.
- Compute impacts and projections for FactSheets.
- Create and run surveys and polls, send reminders and read results.
- Manage collections, folders, presentations and shares.
- Create documents and templates; manage to-dos.
- Read and write metric schemas, points, KPIs and charts.

## When NOT to use
- Reading or editing FactSheets: use leanix-factsheet-inventory.

## Workflow
1. Read the transformation or survey you will change.
2. Make the change and read it back.
3. For a survey, create the run, send reminders only on request, then read results.
4. Report ids and the resulting state.

## Safety
- Executing a transformation changes FactSheets; ask first.
- Poll reminders reach real people; ask before sending.
- Deleting a collection, presentation or KPI is not reversible from this connector.

## Tools (167)

Each tool is one API operation; pass its path, query and body fields as named arguments.


### Documents

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_documents_getdocumentbyid` | GET | Retrieve a specific document |
| `leanix_leanix_documents_getdocumentcomponents` | GET | Retrieve components of a document |
| `leanix_leanix_documents_getdocumentscount` | GET | Count of matching documents |
| `leanix_leanix_documents_getdocumentspaginated` | GET | Query for documents |
| `leanix_leanix_documents_gettemplatebyid` | GET | Retrieve a specific template |
| `leanix_leanix_documents_gettemplatecomponents` | GET | Retrieve Components of a Template |
| `leanix_leanix_documents_gettemplatespaginated` | GET | Query for templates |
| `leanix_leanix_documents_createdocuments` | POST | Create (multiple) documents |
| `leanix_leanix_documents_createtemplatecomponents` | POST | Create (multiple) templates components |
| `leanix_leanix_documents_createtemplates` | POST | Create (multiple) templates |
| `leanix_leanix_documents_updatecomponents` | PUT | Update (multiple) template components of a template |
| `leanix_leanix_documents_updatedocument` | PUT | Update a document |
| `leanix_leanix_documents_updatedocumentcomponents` | PUT | Update (multiple) components of a document |
| `leanix_leanix_documents_updatetemplate` | PUT | Update a template |
| `leanix_leanix_documents_deletedocumentbyid` | DELETE | Delete a specific document |
| `leanix_leanix_documents_deletetemplate` | DELETE | Delete a template |
| `leanix_leanix_documents_deletetemplatecomponent` | DELETE | Delete a template component from a template |

### Impacts

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_impacts_get` | GET | Fetch configuration |
| `leanix_leanix_impacts_getprojection` | POST | Calculate impact projection |
| `leanix_leanix_impacts_getsinglefactsheetprojection` | POST | Calculate impact projection for a single Fact Sheet |
| `leanix_leanix_impacts_compute` | POST | Call POST /obsolescence_reasons |
| `leanix_leanix_impacts_update` | PUT | Update configuration |

### Metrics

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_metrics_all_charts_charts_get` | GET | Return all Charts in a workspace. |
| `leanix_leanix_metrics_all_kpis_kpis_get` | GET | Return all KPIs in workspace. |
| `leanix_leanix_metrics_all_kpis_simple_kpis_simple_get` | GET | Return all KPIs in workspace with simplified data structure. |
| `leanix_leanix_metrics_all_points_schemas__uuid__points_get` | GET | Return all points in schema. |
| `leanix_leanix_metrics_all_schemas_schemas_get` | GET | Return all schemas in workspace. |
| `leanix_leanix_metrics_find_schemas_schemas_find_get` | GET | Return single schema by UUID. |
| `leanix_leanix_metrics_get_aggregation_schemas__uuid__points_aggregation_post` | POST | Get an aggregation of points from a specified schema. |
| `leanix_leanix_metrics_healthcheck_healthcheck__get` | GET | Show healthcheck status |
| `leanix_leanix_metrics_one_chart_charts__uuid__get` | GET | Return a single Chart in a workspace. |
| `leanix_leanix_metrics_one_kpi_kpis__uuid__get` | GET | Return single KPI by UUID. |
| `leanix_leanix_metrics_one_point_schemas__uuid__points__timestamp__get` | GET | Return single point in schema by timestamp. |
| `leanix_leanix_metrics_one_schema_schemas__uuid__get` | GET | Return single schema by UUID. |
| `leanix_leanix_metrics_trend_schemas__uuid__trends_get` | GET | Returns trend, difference and latest value for schema points. |
| `leanix_leanix_metrics_validate_kpis_validate_post` | POST | Validates a new KPI and return the result. |
| `leanix_leanix_metrics_kpi_job_jobs_kpi__kpi_uuid__post` | POST | Trigger calculation of a specific KPI |
| `leanix_leanix_metrics_new_chart_charts_post` | POST | Create a new Chart |
| `leanix_leanix_metrics_new_kpi_kpis_post` | POST | Create a new KPI. |
| `leanix_leanix_metrics_new_point_schemas__uuid__points_post` | POST | Create or overwrite a point at the given timestamp. |
| `leanix_leanix_metrics_new_schema_schemas_post` | POST | Create a new schema. |
| `leanix_leanix_metrics_ws_job_jobs_post` | POST | Trigger calculation of all KPIs in the user's workspace |
| `leanix_leanix_metrics_patch_kpi_kpis_patch` | PATCH | Patch KPI. |
| `leanix_leanix_metrics_put_kpi_kpis_put` | PUT | Update KPI. |
| `leanix_leanix_metrics_update_patch_chart_charts__uuid__patch` | PATCH | Update only given fields of a Chart |
| `leanix_leanix_metrics_update_put_chart_charts__uuid__put` | PUT | Update all fields of a Chart |
| `leanix_leanix_metrics_delete_chart_charts__uuid__delete` | DELETE | Delete a single Chart in a workspace. |
| `leanix_leanix_metrics_delete_one_kpi_kpis__uuid__delete` | DELETE | Delete KPI by UUID. |
| `leanix_leanix_metrics_delete_one_point_schemas__uuid__points__timestamp__delete` | DELETE | Delete One Point |
| `leanix_leanix_metrics_delete_points_range_schemas__uuid__points_delete` | DELETE | Delete Points Range |
| `leanix_leanix_metrics_delete_schema_schemas__uuid__delete` | DELETE | Delete schema by UUID. |

### Navigation

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_navigation_getallcollectiongroups` | GET | Get all Collection Groups. |
| `leanix_leanix_navigation_getcollectionfolders` | GET | Get all folders of a collection. |
| `leanix_leanix_navigation_getcollectiongroupbyid` | GET | Get Collection Group by ID. |
| `leanix_leanix_navigation_getcollections` | GET | Get Collections. |
| `leanix_leanix_navigation_getnavigationitemfavorite` | GET | Get Navigation Item Favorite. |
| `leanix_leanix_navigation_getpresentationbyid` | GET | Get Presentation by ID. |
| `leanix_leanix_navigation_getpresentationsharesbyid` | GET | Get Presentation Shared With Users by ID. |
| `leanix_leanix_navigation_searchnavigationitem` | GET | Search for navigation items |
| `leanix_leanix_navigation_searchpresentation` | GET | Search for presentations |
| `leanix_leanix_navigation_createcollectiongroup` | POST | Create a Collection Group |
| `leanix_leanix_navigation_createpresentation` | POST | Create a presentation. |
| `leanix_leanix_navigation_createslide` | POST | Create a slide. |
| `leanix_leanix_navigation_postcollection` | POST | Create Collection. |
| `leanix_leanix_navigation_postcollectionnavigationitem` | POST | Add Navigation Item to Collection. |
| `leanix_leanix_navigation_postfoldercontroller` | POST | Create new folder. |
| `leanix_leanix_navigation_postnavigationitemfavorite` | POST | Create Navigation Item Favorite. |
| `leanix_leanix_navigation_putcollectionnavigationitem` | POST | Batch add navigation items into a collection. |
| `leanix_leanix_navigation_sharepresentation` | POST | Share a presentation. |
| `leanix_leanix_navigation_batchputcollectiongroups` | PUT | Batch update collection groups. |
| `leanix_leanix_navigation_executebatchmove` | PUT | Batch move folders and items. |
| `leanix_leanix_navigation_putcollection` | PUT | Update Collection. |
| `leanix_leanix_navigation_putcollectiongroupbyid` | PUT | Update Collection Group by ID. |
| `leanix_leanix_navigation_putpresentationbyid` | PUT | Update Presentation by ID. |
| `leanix_leanix_navigation_putslidebyid` | PUT | Update Slide by ID. |
| `leanix_leanix_navigation_updatefoldercontroller` | PUT | Update folder. |
| `leanix_leanix_navigation_deletecollection` | DELETE | Delete Collection. |
| `leanix_leanix_navigation_deletecollectiongroupbyid` | DELETE | Delete Collection Group by ID. |
| `leanix_leanix_navigation_deletecollectionnavigationitem` | DELETE | Remove Navigation Item from Collection. |
| `leanix_leanix_navigation_deletenavigationitemfavorite` | DELETE | Delete Navigation Item Favorite. |
| `leanix_leanix_navigation_deletepresentationbyid` | DELETE | Delete Presentation by ID. |
| `leanix_leanix_navigation_deletepresentationsharebyid` | DELETE | Revoke Presentation Share by ID. |
| `leanix_leanix_navigation_deleteslidebyid` | DELETE | Delete Slide by ID. |
| `leanix_leanix_navigation_executebatchdelete` | DELETE | Batch delete folders and items. |

### Poll

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_poll_get_added_recipients_for_run` | GET | get_added_recipients_for_run |
| `leanix_leanix_poll_get_all` | GET | get_all |
| `leanix_leanix_poll_get_by_id` | GET | get_by_id |
| `leanix_leanix_poll_get_poll` | GET | get_poll |
| `leanix_leanix_poll_get_poll_count` | GET | get_poll_count |
| `leanix_leanix_poll_get_poll_poll_runs` | GET | get_poll_poll_runs |
| `leanix_leanix_poll_get_poll_recipient_details` | GET | get_poll_recipient_details |
| `leanix_leanix_poll_get_poll_result` | GET | get_poll_result |
| `leanix_leanix_poll_get_poll_results_for_user` | GET | get_poll_results_for_user |
| `leanix_leanix_poll_get_poll_run` | GET | get_poll_run |
| `leanix_leanix_poll_get_poll_run_results` | GET | get_poll_run_results |
| `leanix_leanix_poll_get_poll_runs` | GET | get_poll_runs |
| `leanix_leanix_poll_get_poll_runs_kpi_counts` | GET | get_poll_runs_kpi_counts |
| `leanix_leanix_poll_get_polls` | GET | get_polls |
| `leanix_leanix_poll_get_polls_for_factsheet` | GET | get_polls_for_factsheet |
| `leanix_leanix_poll_get_recipients_for_poll_run` | GET | get_recipients_for_poll_run |
| `leanix_leanix_poll_get_reminders` | GET | get_reminders |
| `leanix_leanix_poll_get_results_for_poll_run` | GET | get_results_for_poll_run |
| `leanix_leanix_poll_create_poll` | POST | create_poll |
| `leanix_leanix_poll_create_poll_reminder` | POST | create_poll_reminder |
| `leanix_leanix_poll_create_poll_run` | POST | create_poll_run |
| `leanix_leanix_poll_create_poll_template` | POST | create_poll_template |
| `leanix_leanix_poll_replay` | POST | replay |
| `leanix_leanix_poll_replay_1` | POST | replay_1_1 |
| `leanix_leanix_poll_check_for_new_fact_sheets` | PUT | check_for_new_fact_sheets |
| `leanix_leanix_poll_set_status` | PUT | set_status |
| `leanix_leanix_poll_update_poll` | PUT | update_poll |
| `leanix_leanix_poll_update_poll_result` | PUT | update_poll_result |
| `leanix_leanix_poll_update_poll_run` | PUT | update_poll_run |
| `leanix_leanix_poll_delete_by_id` | DELETE | delete_by_id |
| `leanix_leanix_poll_delete_poll` | DELETE | delete_poll |
| `leanix_leanix_poll_delete_poll_run` | DELETE | delete_poll_run |

### Survey

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_survey_check_for_new_fact_sheets` | POST | check_for_new_fact_sheets |
| `leanix_leanix_survey_get_added_recipients_for_poll_run` | GET | get_added_recipients_for_poll_run |
| `leanix_leanix_survey_get_all_reminders_for_poll_run` | GET | get_all_reminders_for_poll_run |
| `leanix_leanix_survey_get_all_templates` | GET | get_all_templates |
| `leanix_leanix_survey_get_poll` | GET | get_poll |
| `leanix_leanix_survey_get_poll_count` | GET | get_poll_count |
| `leanix_leanix_survey_get_poll_result` | GET | get_poll_result |
| `leanix_leanix_survey_get_poll_results_by_poll_run_id` | GET | get_poll_results_by_poll_run_id |
| `leanix_leanix_survey_get_poll_results_for_user` | GET | get_poll_results_for_user |
| `leanix_leanix_survey_get_poll_run_by_id` | GET | get_poll_run_by_id |
| `leanix_leanix_survey_get_poll_runs` | GET | get_poll_runs |
| `leanix_leanix_survey_get_poll_runs_by_poll` | GET | get_poll_runs_by_poll |
| `leanix_leanix_survey_get_polls` | GET | get_polls |
| `leanix_leanix_survey_get_polls_for_fact_sheet` | GET | get_polls_for_fact_sheet |
| `leanix_leanix_survey_get_recipients_and_fact_sheets_for_poll` | GET | get_recipients_and_fact_sheets_for_poll |
| `leanix_leanix_survey_get_recipients_and_fact_sheets_for_poll_run` | GET | get_recipients_and_fact_sheets_for_poll_run |
| `leanix_leanix_survey_get_templates_by_id` | GET | get_templates_by_id |
| `leanix_leanix_survey_getpollrunresultsasexcel` | GET | Call GET /pollRuns/{poll_run_id}/pollResults.xlsx |
| `leanix_leanix_survey_create_poll` | POST | create_poll |
| `leanix_leanix_survey_create_poll_reminder` | POST | create_poll_reminder |
| `leanix_leanix_survey_create_poll_run` | POST | create_poll_run |
| `leanix_leanix_survey_replay_all_workspaces` | POST | replay_all_workspaces |
| `leanix_leanix_survey_replay_workspace_by_id` | POST | replay_workspace_by_id |
| `leanix_leanix_survey_update_poll` | PUT | update_poll |
| `leanix_leanix_survey_update_poll_result` | PUT | update_poll_result |
| `leanix_leanix_survey_update_poll_run` | PUT | update_poll_run |
| `leanix_leanix_survey_update_poll_run_status` | PUT | update_poll_run_status |
| `leanix_leanix_survey_delete_poll_by_id` | DELETE | delete_poll_by_id |
| `leanix_leanix_survey_delete_poll_run` | DELETE | delete_poll_run |

### Todo

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_todo_get` | GET | Get to-dos on your workspace |
| `leanix_leanix_todo_query` | POST | Get all to-dos matching a query of a specific workspace |
| `leanix_leanix_todo_createtodo` | POST | Create a to-do |
| `leanix_leanix_todo_deletetodos` | POST | Delete to-dos that match the given query body on a workspace |
| `leanix_leanix_todo_managedrestorationrequests` | POST | Trigger the snapshot restore of the To-Dos of a workspace |
| `leanix_leanix_todo_managedsnapshotrequests` | POST | Trigger the snapshotting of the To-Dos of a workspace |
| `leanix_leanix_todo_upserttodos` | POST | Upsert to-dos |
| `leanix_leanix_todo_accepttodo` | PUT | Import and/or Link an Application into this workspace, connecting it to SI to receive nightly data updates.... |
| `leanix_leanix_todo_assigntome` | PUT | Assign yourself as the to-do owner of this to-do and set it to in progress |
| `leanix_leanix_todo_rejecttodo` | PUT | Set the resolution to rejected of a to-do with type 'Link' or 'Import' or 'Answer' or 'Approval' and set the... |
| `leanix_leanix_todo_replyandclosetodo` | PUT | Add a reply to the question in the to-do with type 'Answer' and set the to-do state to closed. The reply is... |

### Transformations

| Tool | Method | Purpose |
|---|---|---|
| `leanix_leanix_transformations_gettransformation` | GET | Returns a single transformation by id |
| `leanix_leanix_transformations_gettransformationcustomimpacts` | GET | Returns a list of all custom impacts belonging to a transformation |
| `leanix_leanix_transformations_gettransformations` | GET | Returns a list of transformations |
| `leanix_leanix_transformations_createtransformation` | POST | Creates a transformation |
| `leanix_leanix_transformations_posttransformationcustomimpacts` | POST | Creates a custom impact on that transformation |
| `leanix_leanix_transformations_posttransformationexecution` | POST | Materializes the changes of the transformation in the workspaces inventory |
| `leanix_leanix_transformations_posttransformationsexecution` | POST | Materializes the changes of multiple transformations in the workspaces inventory |
| `leanix_leanix_transformations_puttransformation` | PUT | Updates a transformation |
| `leanix_leanix_transformations_puttransformationcustomimpacts` | PUT | Updates a custom impact on that transformation |
| `leanix_leanix_transformations_deletetransformation` | DELETE | Deletes a single transformation by id |
| `leanix_leanix_transformations_deletetransformationcustomimpacts` | DELETE | Deletes a custom impact on that transformation by id |
