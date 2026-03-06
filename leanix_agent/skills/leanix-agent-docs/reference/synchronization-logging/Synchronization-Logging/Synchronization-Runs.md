##  Synchronization Runs
The Synchronization Logging page shows synchronization runs for all active integrations configured within a workspace.
During a synchronization run, the system checks if data is synchronized between the source and the target. If there is a mismatch in data, the corresponding operation to create, update, or delete a resource is performed.
Full synchronization runs are automatically initiated by the integration. In most cases, synchronizations are initiated at least once per day. You can also initiate a synchronization run manually.
The following table lists parameters of a synchronization run that appear on the Synchronization Logging page.
Parameter | Description
---|---
Date | The date and time when the synchronization run started.
Type | The associated integration, for example, Signavio or ServiceNow.
Name |  This parameter is only relevant for some integration types. Examples:
  * Signavio: The name of the configuration (if you're using multiple workspaces).
  * Integrations that are set up through the [Integration API](https://help.sap.com/docs/leanix/ea/integration-api?locale=en-US&state=PRODUCTION&version=CLOUD "Overview of the Integration API."): The name of the processor.


Trigger |  The trigger of the synchronization run. Example triggers:
  * FULL_SYNC_JOB: Full synchronization run that is automatically initiated by the integration.
  * FULL_SYNC_MANUAL: Full synchronization run that an administrator initiates manually. To learn more, see [Initiate a Synchronization Run Manually](https://help.sap.com/docs/leanix/ea/synchronization-logging?locale=en-US&state=PRODUCTION&version=CLOUD#loio275d86a77a4410149a3cc45e299aa022__initiating_a_synchronization_run_manually).
  * LEANIX_CHANGES or <INTEGRATION>_CHANGES: Triggers for partial synchronizations. Partial synchronizations are only triggered for specific integration types, for example, Signavio and ServiceNow. If a change is detected on the SAP LeanIX side or the external system side, a partial synchronization run is triggered.


Progress | The progress of the synchronization run: PENDING, RUNNING, ABORTED, FINISHED, or ABORTION PENDING.
Duration | The duration of the synchronization run.
Status |  The final status of the synchronization. This status is a computation of the statuses of the related synchronization actions.
  * OK: All actions in the synchronization run were successful.
  * ERROR: At least one action in the synchronization run resulted in an error.
  * WARNING: At least one action in the synchronization run triggered a warning, and no errors occurred.
  * INFO: At least one action in the synchronization run triggered an info message, and no errors or warnings occurred.


Processed | The number of messages generated during the synchronization run.
Updates | The number of actions of the UPDATE type that occurred during the synchronization run.
Warnings | The number of actions with the WARNING status that occurred during the synchronization run.
Errors | The number of actions with the ERROR status that occurred during the synchronization run.
Actions | For synchronization runs in progress, the Cancel Sync button appears in this column. The option to cancel a synchronization run is only available for specific integration types. For some integration types, it’s impossible to cancel a synchronization run in progress.


