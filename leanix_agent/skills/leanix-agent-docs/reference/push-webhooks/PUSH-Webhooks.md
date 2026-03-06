# PUSH Webhooks
### On this page
  * [Authorization](https://help.sap.com/docs/leanix/ea/push-webhooks#authorization)
  * [Error Handling](https://help.sap.com/docs/leanix/ea/push-webhooks#error-handling)
  * [Automatic Deactivation](https://help.sap.com/docs/leanix/ea/push-webhooks#automatic-deactivation)
  * [Callback](https://help.sap.com/docs/leanix/ea/push-webhooks#callback)


Receive events to a target URL as they occur in your workspace.
With PUSH webhooks, each time an event occurs in SAP LeanIX, it's sent to the specified target URL through an HTTP POST request. The request body contains an event payload in JSON format.
Your server should return a successful HTTP response code to confirm successful delivery. Delivery results for the past 30 days are listed on the webhook details page, below the configuration fields.
