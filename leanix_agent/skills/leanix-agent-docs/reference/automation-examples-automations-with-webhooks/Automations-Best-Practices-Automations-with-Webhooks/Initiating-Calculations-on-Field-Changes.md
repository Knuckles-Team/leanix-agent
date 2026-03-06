##  Initiating Calculations on Field Changes
You can set up a custom calculation, such as risk scores, to be triggered when certain fields change. Follow these steps:
  1. In the Meta Model Configuration section of the administration area, create single-select fields for risk assessment:
     * Data Sensitivity: Low, Medium, or High
     * Regulatory Compliance: Compliant, Partially Compliant, or Non-Compliant
  2. Map risk scores to each option. Example scores:
     * Data Sensitivity: Low (1), Medium (2), or High (3)
     * Regulatory Compliance: Compliant (1), Partially Compliant (2), or Non-Compliant (3)
  3. In the Automations section of the administration area, set up an automation.
     * Trigger: Select the Field changes event, then choose specific fields and values to monitor.
     * Conditions: Optionally, specify additional conditions for the automation.
     * Actions: Send a webhook to a target URL.
  4. On your automation platform, set up a process to:
     * Receive the webhook.
     * Calculate the risk score based on the current values of Data Sensitivity and Regulatory Compliance. The total risk score is the sum of the two individual scores.


Example scenarios:
  * If an application's Data Sensitivity changes from Low (1) to High (3), the risk score increases accordingly.
  * If Regulatory Compliance changes from Compliant (1) to Non-Compliant (3), the risk score also increases.


YesNo
Send
![close icon](https://consent.trustarc.com/get?name=sapglow-close-icon.png)
This site uses cookies and related technologies, as described in our Cookie Statement, for purposes that may include site operation, analytics, enhanced user experience, or advertising. You may choose to consent to our use of these technologies, or manage your own preferences.
Understood Manage Settings
[Privacy Statement](https://help.sap.com/docs/privacy)|[Cookie Statement](https://www.sap.com/about/legal/privacy/cookies.html)
