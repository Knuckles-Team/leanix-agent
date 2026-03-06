##  Automation to Trigger an End-of-Life Process
SAP LeanIX provides an easy-to-use, no-code automation feature that allows admins to configure workflows triggered by specific events and set off sequential actions.
You can set up automation to initiate an end-of-life process for applications well before the end of life date of an IT component it relies on. This approach creates early awareness of the upcoming risk, enabling decision-makers to plan mitigation actions or even accept the resulting risk accordingly.
To set up the automation, follow these instructions:
  1. In the administration area, select Automation.
  2. Select New Automation and provide the name, description, and owner for the Automation.
  3. In the When section define the trigger for the Automation:
Field in Trigger | Selection to Make
---|---
Fact Sheet Type | IT Component
Event | Lifecycle phase change
Field | Lifecycle
State | End of life


Also, specify in days when the trigger should be executed before the IT component reaches the end of life.
![Defining the Trigger for the Automation](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27537a457a441014b8fd8f0ec8934ac7_LowRes.png)
Defining the Trigger for the Automation
![Defining the Trigger for the Automation](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27537a457a441014b8fd8f0ec8934ac7_LowRes.png)
Defining the Trigger for the Automation
![Defining the Trigger for the Automation](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27537a457a441014b8fd8f0ec8934ac7_LowRes.png)
Defining the Trigger for the Automation
  4. In the Then section, click + Add Action and select Create To-Do: Action Item.
  5. Define what actions should be executed when the Automation is triggered:
    1. Add a name and description for the action item. Describe what needs to be done, for example, prompt the user to check the end-of-life date of the IT component and initiate the decommissioning process. Tasks can include planning the deletion or archiving of data and starting the contract cancellation process.
    2. Select Fact Sheet subscriptions for Assignee(s) and select an appropriate subscription role in the Select Fact Sheet Subscription(s) field to assign responsibilities.
    3. Specify the due date in days for the completion of the to-do task.
![Defining the Action for the Automation](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2749f23a7a441014a16ba2372a9fbbe7_LowRes.png)
Defining the Action for the Automation
  6. Click Save and run Automation to complete setting up the automation.


Whenever an IT component meets the specified criteria, the automation will create a to-dos item for the individual responsible for the IT component. Additionally, it will also break the quality seal of the IT component to notify the subscribers of the fact sheet.
