##  Examples
The table below lists common scenarios and the recommended feature for each.
Example Scenarios and Recommended Features Scenario | Recommended Feature | Explanation
---|---|---
Populate the TIME Classification field on applications based on updates to the Functional Fit or Technical Fit fields | Calculations | Activate a predefined calculation template for TIME classification. To learn more about templates, see [Calculation Templates](https://help.sap.com/docs/leanix/ea/calculations?locale=en-US&state=PRODUCTION&version=CLOUD#loio275919c67a441014a04fa34f480310eb__calculation_templates).
Cost aggregation: calculate an application’s total cost by summing up costs from other fields | Calculations | Define custom logic to aggregate costs from multiple fields. You can also include additional operations, such as using weights or values from related fact sheets, which allows for more complex scenarios.
Add a tag when a subscription is removed | Automations |  Calculations don't support tags. Create an automation with the following parameters:
  * Trigger: Subscription removed
  * Action: Add a tag


Send email notifications for applications entering the End of Life lifecycle phase | Automations |  Calculations don’t support sending emails. Create an automation with the following parameters:
  * Trigger: Lifecycle phase reached
  * Action: Send an email


Calculate a technical risk score and send an email if the score is above the specified value | Calculations and automations |  Use both features:
  1. Create a calculation to calculate a risk score and write it to a target field.
  2. Create an automation where the trigger is a field value for the technical risk score and the action is sending an email.




YesNo
Send
![close icon](https://consent.trustarc.com/get?name=sapglow-close-icon.png)
This site uses cookies and related technologies, as described in our Cookie Statement, for purposes that may include site operation, analytics, enhanced user experience, or advertising. You may choose to consent to our use of these technologies, or manage your own preferences.
Understood Manage Settings
[Privacy Statement](https://help.sap.com/docs/privacy)|[Cookie Statement](https://www.sap.com/about/legal/privacy/cookies.html)
