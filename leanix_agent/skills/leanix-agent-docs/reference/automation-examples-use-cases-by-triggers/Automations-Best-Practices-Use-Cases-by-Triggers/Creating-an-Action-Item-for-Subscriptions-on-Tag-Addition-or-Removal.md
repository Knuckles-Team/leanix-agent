##  Creating an Action Item for Subscriptions on Tag Addition or Removal
Tags are important for clustering and categorizing fact sheets. Changes to tags often necessitate actions from certain users. For example, when an "Eliminate" tag is added to an application, the application owner needs to follow a specific checklist. This automation assigns an action item (to-do) to fact sheet subscriptions, which ensures that users are notified and can take appropriate action.
The following image shows the logic of the automation.
![612](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2741549c7a441014b8eff0f97f72eb4e_LowRes.png)
Automation: Creating an Action Item for Subscriptions on Tag Addition or Removal
To configure the automation, follow these steps:
  1. Enter a name and select an owner for the automation. Optionally, enter a description.
  2. In the When section, specify the trigger for the automation:
    1. In the Fact Sheet Type list, select a fact sheet type.
    2. In the Event list, select Tag is added or Tag is removed, then select a tag.
  3. In the If section, specify conditions for the automation:
    1. Include or ignore fact sheets that are updated by technical users.
    2. Optional: Add conditions to trigger the automation for: fact sheet category, assigned tags, or single-select field values.
  4. In the Then section, specify the action for the automation:
    1. Click Add Action, then select Create To-Do: Action Item.
    2. Enter a name for the action item and, optionally, a description.
    3. In the Assignee(s) list, select Fact sheet subscriptions, then select subscription types and, if applicable, roles.
    4. In the Due (in days) field, enter the number of days indicating when the to-do item is due.
  5. Save the automation.
