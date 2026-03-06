##  Creating an Action Item for Subscriptions on Subscription Addition or Removal
Subscriptions play a crucial role in engaging users and collaborating on a fact sheet. Changes to subscriptions often necessitate action from other users. For example, if an Accountable or Responsible role is added or removed from an application, other subscribers need to ensure a replacement is found or understand why the person was removed. To facilitate this, you can create an automation to notify subscribed users with a to-do.
The following image shows the logic of the automation.
![Automation: Creating an Action Item for Subscriptions on Adding or Removing a Subscription](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274c1e927a441014b3a791fae78b08f7_LowRes.png)
Automation: Creating an Action Item for Subscriptions on Subscription Addition or Removal
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
    1. Click Add Action, then select Create To-Do: Action Item.
    2. Enter a name for the action item and, optionally, a description.
    3. In the Assignee(s) list, select Fact Sheet subscriptions.
    4. Select a subscription type and, if applicable, one or more subscription roles to assign the to-do item to.
    5. In the Due (in days) field, enter the number of days indicating when the to-do item is due.
  5. Save the automation.
