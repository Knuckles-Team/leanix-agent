##  Assigning an Action Item to Specific Users on Quality State Changes
When the quality state changes, this automation assigns an action item (to-do) to fixed users, even if they're not subscribed to a fact sheet. This enables you to ensure that key users, such as enterprise architects or solution architects, are promptly notified when the quality seal on a mission-critical application is broken.
The following image shows the logic of the automation.
![Automation: Assigning an Action Item to Fixed Users on Quality State Changes](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274558a37a4410149b8cb2cd2263d7e3_LowRes.png)
Automation: Assigning an Action Item to Specific Users on Quality State Changes
To configure the automation, follow these steps:
  1. Enter a name and select an owner for the automation. Optionally, enter a description.
  2. In the When section, specify the trigger for the automation:
    1. In the Fact Sheet Type list, select a fact sheet type.
    2. In the Event list, select Quality State changes to, then select a state (for example, Broken).
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
