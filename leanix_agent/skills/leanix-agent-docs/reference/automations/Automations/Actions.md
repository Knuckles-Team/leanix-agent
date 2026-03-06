##  Actions
The following table lists the available actions that are initiated by an automation.
Actions | Values and Parameters | Additional Information
---|---|---
Create To-Do: Action item |
  * Action Item Name
  * Description
  * Assignees (Fact Sheet creator, Fact Sheet subscriptions, Fixed Fact Sheet subscriptions, Users)
  * Due (in days)
  * Users: fixed users
  * Due (in days)
  * Pause until "Marked as Complete"

|  Assigns a to-do item to users. Selecting the Fixed Fact Sheet subscriptions option for assignees enables you to dynamically assign user groups to fact sheets, which eliminates the need for manual maintenance in automations. The Pause until "Marked as Complete" toggle enables you to pause the execution of the following action in the sequence until the to-do is marked as complete. Any automation run that is not completed within 180 days is stopped.
Create To-Do: Approval |
  * Title
  * Description
  * Assignees (Fact Sheet creator, Fact Sheet subscriptions, Fixed Fact Sheet subscriptions, Users)
  * Due (in days)
  * Action when resolution status is "Rejected" (Set field, Set Quality State)

|  Creates an approval to-do that allows users to either approve or reject a to-do item assigned to them. For more information, see [To-Dos](https://help.sap.com/docs/leanix/ea/to-dos?locale=en-US&state=PRODUCTION&version=CLOUD "To-dos facilitate task delegation, collaboration, and governance and can be used to ensure data integrity and quality through transparent task management."). Any automation run that is not completed within 180 days is stopped.
Set field | Single select-field values, as well as the Empty option | In the To list, select the value to be set on the fact sheet.
Set Quality State |
  * Approved
  * Broken
  * Draft
  * Rejected

| Automations can only set the quality state to Approved when all the mandatory attributes are set.
Add subscription |
  * New subscriber (Fact sheet creator, User)
  * Subscription type and, if applicable, subscription roles

| Adds a subscription only if the settings of the workflow and already existing subscriptions allow it. You can select only one subscription type but multiple subscription roles.
Set subscription |
  * New subscriber (Fact sheet creator, User)
  * Subscription type and, if applicable, subscription roles

| Sets a subscription and overwrites all existing subscriptions of the selected user. You can select only one subscription type but multiple subscription roles.
Add tag | All tags configured for the selected fact sheet type | You can only select one tag. A tag from a single-select tag group replaces the currently assigned tag from this group. A tag from a multi-select tag group is assigned in addition to other tags from this group.
Remove tag | All tags configured for the selected fact sheet type | You can only select one tag. The automation removes the tag regardless of the tag mode.
Send Webhook | Webhook tag that serves as the automation identifier | For more information, see [Sending a Webhook from an Automation](https://help.sap.com/docs/leanix/ea/automations?locale=en-US&state=PRODUCTION&version=CLOUD#loio2758d6af7a441014b829a7547e83bfd4__sending_a_webhook_from_an_automation).
Send Email |  Specify the following:
  * Recipients: You can choose from a fact sheet creator, subscribers, or fixed subscribers as email recipients. Alternatively, you can use specific email addresses, with a limit of up to 10. To notify more users, use distribution lists instead of individual addresses.
  * Subject: Create a custom email subject. If the subject exceeds 200 characters, it appears truncated.
  * Message: Craft a custom email body. The editor supports Markdown syntax.

You can add placeholders for affected fact sheets to the email subject and body. Placeholders are available for the fact sheet display name and link. The system validates placeholders in the email body for correctness. Valid placeholders appear highlighted in green, while invalid ones are highlighted in red. | A custom email is sent to the specified recipients. Sent notifications appear in the audit log in the Notifications Center section of the administration area. To learn more, see [Audit Log](https://help.sap.com/docs/leanix/ea/notifications-center?locale=en-US&state=PRODUCTION&version=CLOUD#loio275b6c897a44101499dcb03a773b34f1__audit_log).
Run Script | Define the script logic in the script editor. | For more information, see [Automations with Scripts](https://help.sap.com/docs/leanix/ea/automations-with-scripts?locale=en-US&state=PRODUCTION&version=CLOUD "Use automations with scripts to update fact sheet fields or call SAP LeanIX APIs. Define the script logic in a script editor in SAP LeanIX.").


