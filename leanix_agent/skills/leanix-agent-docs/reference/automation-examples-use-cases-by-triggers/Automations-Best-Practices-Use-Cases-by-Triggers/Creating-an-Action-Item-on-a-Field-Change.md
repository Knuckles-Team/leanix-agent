##  Creating an Action Item on a Field Change
This automation creates an action item (to-do) based on changes in single-select fact sheet fields. The automation is especially beneficial in the following scenarios:
  * When a critical field value is modified, automatically create actions items for relevant users (either fixed users or subscriptions) to verify the legitimacy of the change.
  * When a new critical field value is added, automatically create a check to determine if further actions are required.


For example, if an application's business criticality is set to Mission critical, or if the business criticality changes from Mission critical to another value, the automation generates an action item for the enterprise architecture team. This ensures that critical changes are promptly addressed.
The following image shows the logic of the automation.
![Automation: Creating an Action Item Based on a Field Change](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27485e797a441014b97fe5e014244396_LowRes.png)
Automation: Creating an Action Item on a Field Change
To configure the automation, follow these steps:
  1. Enter a name and select an owner for the automation. Optionally, enter a description.
  2. In the When section, specify the trigger for the automation:
    1. In the Fact Sheet Type list, select a fact sheet type.
    2. In the Event list, select Field changes.
    3. In the Field list, select a single-select field, then select values in the To and From lists.
  3. In the If section, specify conditions for the automation:
    1. Include or ignore fact sheets that are updated by technical users.
    2. Optional: Add conditions to trigger the automation for: fact sheet category, assigned tags, or single-select field values.
  4. In the Then section, specify the action for the automation:
    1. Click Add Action, then select Create To-Do: Action Item.
    2. Enter a name for the action item and, optionally, a description.
    3. In the Assignee(s) list, select Users or Fact Sheet subscriptions. Depending on the option you selected, select specific users or subscription types and roles.
Instead of selecting a fixed list of users, you can use subscriptions from a fixed reference fact sheet of any type within the workspace. This could be a fact sheet of the organization type or a custom type representing team or organizational entities. This method minimizes manual maintenance and allows dynamic assignment. To implement this, in the Assignee(s) list, select Fixed Fact Sheet subscriptions, select a reference fact sheet, then select subscription types and roles.
    4. In the Due (in days) field, enter the number of days indicating when the to-do item is due.
  5. Save the automation.
