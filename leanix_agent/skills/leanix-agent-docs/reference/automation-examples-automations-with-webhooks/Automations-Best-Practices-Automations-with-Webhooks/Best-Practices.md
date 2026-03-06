##  Best Practices
  * Before implementing an automation with a webhook, use a test target URL.
  * Use an automation platform of your choice or any alternative method to process webhook payloads and initiate event-based actions. Here are example workflows that you can configure:
    * Initiating calculations
    * Updating fact sheet fields
    * Sending notifications to users
    * Initiating survey runs
    * Creating and updating related fact sheets
    * Managing user subscriptions on related fact sheets
  * To retrieve and update your workspace data, use SAP LeanIX APIs. For more information, see [SAP LeanIX APIs](https://help.sap.com/docs/leanix/ea/sap-leanix-apis?locale=en-US&state=PRODUCTION&version=CLOUD "Explore SAP LeanIX APIs and learn when to use each API.").
  * If relevant, add a webhook action to existing automations to get event notifications.
