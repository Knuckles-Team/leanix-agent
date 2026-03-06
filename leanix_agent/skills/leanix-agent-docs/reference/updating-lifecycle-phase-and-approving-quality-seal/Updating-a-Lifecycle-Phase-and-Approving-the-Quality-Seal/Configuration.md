##  Configuration
Configure an automation in the Automations section of the administration area.
Automation Parameters Parameter | Configuration
---|---
Trigger (When) |
  * Fact Sheet Type: Application
  * Event: Field value is changed
  * Field: Installation status (custom single-select field)
  * From and To: Anything


Conditions (If) | Configure optional conditions for the automation.
Actions (Then) | Run Script: See the sample code provided below.
Set Quality State: Draft
Create To-Do: Approval: Specify the following:
  * In the description, note that an application's lifecycle phase and date have changed, and ask fact sheet subscribers to review and approve the changes.
  * Choose assignees who'll receive a to-do and specify their subscription types.
  * Set a due date for the to-do.
  * Add an action for when the resolution status is Rejected: set the quality seal state to Rejected. Ensure that this state is enabled in the quality seal configuration.

To learn more about approval to-dos, see [Creating Approval To-Dos](https://help.sap.com/docs/leanix/ea/to-dos-administration?locale=en-US&state=PRODUCTION&version=CLOUD#loio275dbdde7a4410148637f298598afe49__creating_approval_to-dos).
Set Quality State: Approved


