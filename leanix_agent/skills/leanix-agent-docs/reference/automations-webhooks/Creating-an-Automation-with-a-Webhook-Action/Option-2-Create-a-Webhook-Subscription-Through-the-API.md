##  Option 2: Create a Webhook Subscription Through the API
To create a webhook subscription through the [Webhooks API![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fapp.leanix.net%2Fopenapi-explorer%2F%3Furls.primaryName%3DWebhooks "https://app.leanix.net/openapi-explorer/?urls.primaryName=Webhooks"), make a POST request to the following endpoint:

```
https://{SUBDOMAIN}.leanix.net/services/webhooks/v1/subscriptions

```



Replace {SUBDOMAIN} with your value. You can copy your subdomain value from the workspace URL.
Sample request body:

```
{
    "identifier": "Webhook for automation",
    "targetUrl": "<your target URL>",
    "targetMethod": "POST",
    "authorizationHeader": null,
    "workspaceId": "<your workspaceId>",
    "callback": null,
    "tagSets": [
        [
            "automations",
            "AUTOMATION_TRIGGERED",
            "INSERT_AUTOMATION_WEBHOOK_TAG"
        ]
    ],
    "deliveryType": "PUSH",
    "ignoreError": false,
    "active": true
}

```



The table below lists the parameters used in the request body. Modify other parameters as needed.
Parameter | Value
---|---
targetUrl | The target URL for delivering the webhook.
workspaceId | The ID of your workspace. To find the ID, go to the API Tokens section in the administration area and copy the WorkspaceId value.
tagSets | Specify the event type AUTOMATION_TRIGGERED and the webhook tag you created in the automation configuration. Replace the placeholder INSERT_AUTOMATION_WEBHOOK_TAG with your value.
deliveryType | PUSH


Once you've created an automation with a webhook action, you can set up workflows using an automation platform of your choice or any alternative method. You can use SAP LeanIX APIs to retrieve and update your workspace data. For more information, see [SAP LeanIX APIs](https://help.sap.com/docs/leanix/ea/sap-leanix-apis?locale=en-US&state=PRODUCTION&version=CLOUD "Explore SAP LeanIX APIs and learn when to use each API.").
