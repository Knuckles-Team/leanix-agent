##  Option 1: Create a Webhook in the Administration Area
Create a webhook in the Webhooks section of the administration area. To learn how, see [Creating a Webhook](https://help.sap.com/docs/leanix/ea/webhooks?locale=en-US&state=PRODUCTION&version=CLOUD#loio275e18367a441014869bb7aa3562039e__creating_a_webhook).
Specify the following details for the webhook:
  * Type: PUSH
  * Target URL: Enter a URL for delivering webhook events. To test the automation, you can use a test target URL first.
  * Triggering Events: AUTOMATION_TRIGGERED
  * Callback: In the Callback field, enter a callback that contains the webhook tag that you specified in the automation configuration, as shown in the following code snippet. INSERT_AUTOMATION_WEBHOOK_TAG is the webhook tag that you specified in the automation configuration. Replace this placeholder with your value.
JavaScript

```
var payload = delivery.payload; if (payload.tag === 'INSERT_AUTOMATION_WEBHOOK_TAG') { delivery.active = true; } else { delivery.active = false; }

```



The tag binds the webhook to the automation that you created in the previous step. If you don’t provide a callback with a tag, the webhook will be triggered for all automations where the action is Send Webhook.
