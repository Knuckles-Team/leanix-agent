##  Creating a Webhook
Follow these steps:
  1. In the administration area, navigate to the Webhooks section.
  2. Click New Webhook.
  3. Optional: Enter a name and description for the webhook.
  4. Configure the visibility of the webhook:
     * Private: Only you can access the webhook.
     * Workspace: Any admin in the workspace can view, modify, or delete the webhook.
  5. Select the delivery type and configure relevant parameters:
     * PUSH: Enter a target URL for delivering events. Optionally, decide whether you want to skip events that can’t be delivered.
After you save the webhook, you have the option to select an authorization method and enter a callback to manipulate the payload. For more information, see [PUSH Webhooks](https://help.sap.com/docs/leanix/ea/push-webhooks?locale=en-US&state=PRODUCTION&version=CLOUD "Receive events to a target URL as they occur in your workspace.").
     * PULL: Optionally, adjust the maximum batch size that defines a soft upper limit for data in event batches. To learn how to fetch events, see [PULL Webhooks](https://help.sap.com/docs/leanix/ea/pull-webhooks?locale=en-US&state=PRODUCTION&version=CLOUD "Request events by polling an API endpoint.").
  6. The webhook is active by default. To deactivate the webhook, switch it off under **Status**.
  7. In the Triggering Events section, click Add new set to add a triggering event for the webhook. For a full list of events, see [Webhook Events](https://help.sap.com/docs/leanix/ea/webhook-events?locale=en-US&state=PRODUCTION&version=CLOUD "Available event types for webhook subscriptions.").
  8. Click Save.


A webhook is created. You can update its configuration or delete it if needed.
![Creating a PUSH Webhook](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio532e0cc16abe4b1188009447403b943a_LowRes.png)
