##  Sending Alerts to Slack
To send alerts for failed integration events to Slack, create a webhook in SAP LeanIX. For instructions, see [Creating a Webhook](https://help.sap.com/docs/leanix/ea/webhooks?locale=en-US&state=PRODUCTION&version=CLOUD#loio275e18367a441014869bb7aa3562039e__creating_a_webhook).
Specify the following details for the webhook:
  * Type: PUSH
  * Target URL: You can get a target URL from the [incoming webhook![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fmy.slack.com%2Fservices%2Fnew%2Fincoming-webhook%2F "https://my.slack.com/services/new/incoming-webhook/") that you've set up in Slack.
  * Triggering Events: Select INTEGRATION_RUN_FINISHED and INTEGRATION_RUN_ABORTED.
  * Callback: Enter the following code to filter failed events. Replace workspace_url with your workspace URL that includes the workspace name, for example, https://your-company.leanix.net/WorkspaceName.

```
var payload = delivery.payload;
delivery.active = false;
var base_url = 'workspace_url';
if (payload.errorCount > 0) {
    delivery.active = true;
    var text = payload.type + ' with Scope: ' + payload.scope + ' has status: ' + payload.progress + ' and error count: ' + payload.errorCount; text += '. Synclog link : ' + base_url + '/admin/synclog/' + payload.synchronizationId;
}
delivery.payload = { text: text }
```



