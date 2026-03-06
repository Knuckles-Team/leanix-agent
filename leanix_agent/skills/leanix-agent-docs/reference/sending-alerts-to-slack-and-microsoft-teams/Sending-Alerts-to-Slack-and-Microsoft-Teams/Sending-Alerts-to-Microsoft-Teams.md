##  Sending Alerts to Microsoft Teams
To send alerts for failed integration events to Microsoft Teams, create a webhook in SAP LeanIX. For instructions, see [Creating a Webhook](https://help.sap.com/docs/leanix/ea/webhooks?locale=en-US&state=PRODUCTION&version=CLOUD#loio275e18367a441014869bb7aa3562039e__creating_a_webhook).
Specify the following details for the webhook:
  * Type: PUSH
  * Target URL: To get a target URL for event notifications, create a workflow in Microsoft Teams. Workflows enable you to automate processes that connect one or more apps to Microsoft Teams. To learn how to create workflows, refer to the [Microsoft documentation![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fprod.support.services.microsoft.com%2Fen-us%2Foffice%2Fcreate-incoming-webhooks-with-workflows-for-microsoft-teams-8ae491c7-0394-4861-ba59-055e33f75498 "https://prod.support.services.microsoft.com/en-us/office/create-incoming-webhooks-with-workflows-for-microsoft-teams-8ae491c7-0394-4861-ba59-055e33f75498"). If you're using Office 365 connectors, migrate your existing connectors to workflows. To learn more, see the blog entry [Retirement of Office 365 connectors within Microsoft Teams![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdevblogs.microsoft.com%2Fmicrosoft365dev%2Fretirement-of-office-365-connectors-within-microsoft-teams%2F "https://devblogs.microsoft.com/microsoft365dev/retirement-of-office-365-connectors-within-microsoft-teams/") on the Microsoft 365 Developer Blog.
  * Triggering Events: Select INTEGRATION_RUN_FINISHED and INTEGRATION_RUN_ABORTED.
  * Callback: Enter the following code to filter failed events. Replace workspace_url with your workspace URL that includes the workspace name, for example, https://your-company.leanix.net/WorkspaceName.

```
var payload = delivery.payload;
delivery.active = false;
var base_url = 'workspace_url';
if (payload.errorCount > 0) {
    delivery.active = true;
    var uri = base_url + '/admin/synclog/' + payload.synchronizationId
    var text = payload.type + ' with Scope: ' + payload.scope + ' has status: ' + payload.progress + ' and error count: ' + payload.errorCount + '.';
    text += "Click **Sync Log** to check details!";
}
delivery.payload = {

    "type":"message",
    "attachments":[
       {
          "contentType":"application/vnd.microsoft.card.adaptive",
          "contentUrl":null,
          "content":{
             "$schema":"http://adaptivecards.io/schemas/adaptive-card.json",
             "type":"AdaptiveCard",
             "version":"1.2",
             "body":[
                {
                    "type": "TextBlock",
                    "size": "Medium",
                    "weight": "Bolder",
                    "text": payload.type+" Failed",
                    "style": "heading",
                    "wrap": true
                },
                 {
                 "type": "TextBlock",
                 "text": text,
                 "wrap":true
                 }
             ],
             "actions": [
                 {
                    "type": "Action.OpenUrl",
                    "title": "Sync Log",
                    "url": uri,
                    "role": "Button"
                }
            ],
          }
       }
    ]
}
```





YesNo
Send
