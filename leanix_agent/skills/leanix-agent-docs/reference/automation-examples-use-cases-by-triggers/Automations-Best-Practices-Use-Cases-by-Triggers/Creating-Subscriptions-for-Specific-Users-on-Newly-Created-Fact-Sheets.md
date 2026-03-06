##  Creating Subscriptions for Specific Users on Newly Created Fact Sheets
This automation creates subscriptions for certain fixed users on new fact sheets. A common use case is subscribing specific users, such as enterprise architects, to new application fact sheets.
The following image shows the logic of the automation.
![Automation Configuration: Creating Subscriptions for Specific Users](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2753a7287a441014a7379217aa12708c_LowRes.png)
Automation: Creating Subscriptions for Specific Users on Newly Created Fact Sheets
To configure the automation, follow these steps:
  1. Enter a name and select an owner for the automation. Optionally, enter a description.
  2. In the When section, specify the trigger for the automation:
    1. In the Fact Sheet Type list, select a fact sheet type.
    2. In the Event list, select Fact Sheet is created.
  3. In the If section, specify conditions for the automation:
    1. Include or ignore fact sheets that are created by technical users.
    2. Optional: Add a condition for a specific fact sheet category to trigger the automation for.
  4. In the Then section, specify the action for the automation:
    1. Click Add Action, then select Add subscription (or Set subscription).
    2. In the New Subscriber list, select User, then select a user.
    3. Select a subscription type and, if applicable, one or more subscription roles to apply.
    4. If needed, repeat the process to add more users.
  5. Save the automation.
