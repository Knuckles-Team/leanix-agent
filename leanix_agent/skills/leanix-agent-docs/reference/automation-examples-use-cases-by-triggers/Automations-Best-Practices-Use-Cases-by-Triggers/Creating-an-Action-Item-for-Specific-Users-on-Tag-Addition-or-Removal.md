##  Creating an Action Item for Specific Users on Tag Addition or Removal
Tag changes often necessitate user action. For example, when an "Eliminate" tag is added to an application, enterprise architects should prepare for its retirement. This automation enables you to notify specific users with an action item (to-do).
The following image shows the logic of the automation.
![612](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2742484b7a441014ac49bbfb01e5d3ac_LowRes.png)
Automation: Creating an Action Item for Specific Users on Tag Addition or Removal
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
    3. In the Assignee(s) list, select Users, then select users.
Instead of selecting a fixed list of users, you can use subscriptions from a fixed reference fact sheet of any type within the workspace. This could be a fact sheet of the organization type or a custom type representing team or organizational entities. This method minimizes manual maintenance and allows dynamic assignment. To implement this, in the Assignee(s) list, select Fixed Fact Sheet subscriptions, select a reference fact sheet, then select subscription types and roles.
    4. In the Due (in days) field, enter the number of days indicating when the to-do item is due.
  5. Save the automation.
