##  Adding a Subscription on Subscription Addition or Removal
Certain subscription changes, especially removals, may require increased visibility, for example, when an Accountable or Responsible user is removed from applications marked as Mission critical. Since notifications about fact sheet changes are primarily sent to subscribers, it's beneficial to assign additional users, such as enterprise architects, as subscribers to these fact sheets. This ensures that subscribed users can monitor the situation and seek a replacement if necessary.
The following image shows the logic of the automation.
![Automation: Adding a Subscription on Adding or Removing a Subscription](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2754be637a441014811586571cdae9b6_LowRes.png)
Automation: Adding a Subscription on Subscription Addition or Removal
To configure the automation, follow these steps:
  1. Enter a name and select an owner for the automation. Optionally, enter a description.
  2. In the When section, specify the trigger for the automation:
    1. In the Fact Sheet Type list, select a fact sheet type.
    2. In the Event list, select Subscription is added (or Subscription is removed).
    3. Select a subscription type and, if applicable, subscription role.
  3. In the If section, specify conditions for the automation:
    1. Include or ignore fact sheets that are updated by technical users.
    2. Optional: Add conditions to trigger the automation for: fact sheet category, assigned tags, or single-select field values.
  4. In the Then section, specify the action for the automation:
    1. Click Add Action, then select Add subscription (or Set subscription).
    2. In the New Subscriber list, select User, then select a user.
    3. Select a subscription type and, if applicable, one or more subscription roles to apply.
    4. If needed, repeat the process to add more users.
  5. Save the automation.
