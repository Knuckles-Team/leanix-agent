##  Synchronization
The following section explains the types of synchronization offered depending on the configurations.
Synchronization Type | Sync Logging Name | Details
---|---|---
Full Sync | FULL_SYNC | Sync of all the configured mapping that takes place at a set schedule.
Manual Full Sync | FULL_SYNC_MANUAL | Sync of all configured mapping that gets triggered manually by the SAP LeanIX admin
Partial Sync - ServiceNow | SERVICENOW_CHANGES | Sync of changes due to an event trigger of Business Rules from ServiceNow's side.
Partial Sync - SAP LeanIX | LEANIX_CHANGES | Sync of changes due to an event from the SAP LeanIX side.


To view the details of synchronization runs, navigate to the Sync Logging section in the administration area. Incomplete mappings or errors while updating an attribute appear as errors in the synchronization logs. If a mapping issue occurs due to a change in the configuration in the background, this is also displayed in the synchronization logs.
To configure notifications for errors during synchronizations, you can use webhooks. To learn how to send notifications to Slack and Teams, see [Sending Alerts to Slack and Teams](https://help.sap.com/docs/leanix/ea/sending-alerts-to-slack-and-microsoft-teams?locale=en-US&state=PRODUCTION&version=CLOUD "Set up a webhook to receive notifications about failed events in your integration runs.").
Only the fields that are specified in the mapping configuration are synchronized. Any other fields in the respective system are not synchronized.
