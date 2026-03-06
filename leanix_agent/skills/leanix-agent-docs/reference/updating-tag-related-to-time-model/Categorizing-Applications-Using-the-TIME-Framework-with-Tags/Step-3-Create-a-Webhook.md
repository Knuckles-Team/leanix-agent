##  Step 3: Create a Webhook
To learn more about webhooks, see [Webhooks](https://help.sap.com/docs/leanix/ea/webhooks?locale=en-US&state=PRODUCTION&version=CLOUD "Listen to events in SAP LeanIX using webhooks.").
To create a webhook, follow these steps:
  1. Create a PUSH webhook for the following events: FACT_SHEET_CREATED and FACT_SHEET_UPDATED.
  2. In the Target URL field, enter the invoke URL of your Azure function.
  3. In the Callback field, enter the callback function from the callback.js file.
  4. Select the Ignore Errors checkbox.
  5. Click Save.
