##  Callback
To manipulate the webhook payload before it's sent out to the target URL, you can define a callback using JavaScript code. You do this on the Callback tab of the webhook configuration page.
In the JavaScript code, the object data is available in the global scope. It includes the following properties, which you can modify directly in your code:
  * active
  * payload
  * targetMethod
  * targetUrl


You can view all custom code configurations used in webhooks with callbacks in the Managed Code section of the administration area. Here, you can monitor execution logs to track history and resolve issues. For more information, see [Managed Code](https://help.sap.com/docs/leanix/ea/managed-code?locale=en-US&state=PRODUCTION&version=CLOUD "View and manage all custom code configurations used in automations, calculations, and webhooks across your workspace. Monitor execution logs to track history, troubleshoot issues, and ensure your code runs as expected.").
YesNo
Send
