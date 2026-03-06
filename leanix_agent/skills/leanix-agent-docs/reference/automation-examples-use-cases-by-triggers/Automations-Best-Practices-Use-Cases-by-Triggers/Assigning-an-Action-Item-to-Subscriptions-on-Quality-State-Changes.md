##  Assigning an Action Item to Subscriptions on Quality State Changes
This automation assigns an action item (to-do) to subscribers when the quality state on a fact sheet changes. This prompts subscribers, such as application and business owners, to review the changes in the audit log and reapply the quality seal.
The following image shows the logic of the automation.
![Automation: Assigning an Action Item to Subscriptions on Quality State Changes](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2748b7f47a4410148147f3ecc42d1ddb_LowRes.png)
Automation: Assigning an Action Item to Subscriptions on Quality State Changes
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
    3. In the Assignee(s) list, select Fact Sheet subscriptions, then select subscription types and, if applicable, roles.
    4. In the Due (in days) field, enter the number of days indicating when the to-do item is due.
  5. Save the automation.
