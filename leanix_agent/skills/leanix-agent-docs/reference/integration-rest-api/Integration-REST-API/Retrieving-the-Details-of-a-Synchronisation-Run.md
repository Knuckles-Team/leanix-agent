##  Retrieving the Details of a Synchronisation Run
With the id of a synchronization run, you can get additional details about it. To do that, use the following endpoints listed in the table.
Method | Endpoint | Details
---|---|---
GET |  https://{SUBDOMAIN}.leanix.net/services/integration-api/v1/synchronizationRuns/runId/status | Get the status of a synchronization run.
GET |  https://{SUBDOMAIN}.leanix.net/services/integration-api/v1/synchronizationRuns/runId/results | Get the results of a synchronization run in LDIF format. The LDIF output includes all Fact Sheet data which is defined in the corresponding processor declared in a workspace.
GET |  https://{SUBDOMAIN}.leanix.net/services/integration-api/v1/synchronizationRuns/runId/warnings | Get warning messages for a synchronization run. For example, if an attribute that is included in a processor does not exist in a workspace, this information is returned in a warning message.


