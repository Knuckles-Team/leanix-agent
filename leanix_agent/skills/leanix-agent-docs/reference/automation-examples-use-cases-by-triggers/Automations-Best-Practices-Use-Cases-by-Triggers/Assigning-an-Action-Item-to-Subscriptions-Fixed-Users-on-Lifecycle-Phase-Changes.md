##  Assigning an Action Item to Subscriptions (Fixed Users) on Lifecycle Phase Changes
Responding to lifecycle phase changes significantly enhances actionability, especially when assigning to-dos to relevant users. The ability to specify the number of days before or after a specific lifecycle date, including custom lifecycle states, provides flexibility to align with your processes. This automation is particularly useful for milestone checks, such as approaching End of Life dates. For example, you can assign to-dos to your enterprise architecture team or the application owners when an End of Life date is approaching.
In the context of application rationalization, this automation can assist in coordinating with relevant stakeholders by creating to-dos 90 or 30 days before an anticipated phase change. This ensures timely communication and effective planning.
The following image shows the logic of the automation.
![Automation: Creating an Action Time on Lifecycle Phase Changes](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274727897a441014a215aaeb1df041d1_LowRes.png)
Automation: Creating an Action Item on Lifecycle Phase Changes
To configure the automation, follow these steps:
  1. Enter a name and select an owner for the automation. Optionally, enter a description.
  2. In the When section, specify the trigger for the automation:
    1. In the Fact Sheet Type list, select a fact sheet type.
    2. In the Event list, select Lifecycle phase change.
    3. In the Field list, select Lifecycle, then select a lifecycle phase.
    4. Optional: To define when the automation should be initiated (before or after the phase change date), click the Trigger before/after toggle and set the timing in days.
  3. Optional: In the If section, specify conditions for the automation: fact sheet category, assigned tags, or single-select field values.
  4. In the Then section, specify the action for the automation:
    1. Click Add Action, then select Create To-Do: Action Item.
    2. Enter a name for the action item and, optionally, a description.
    3. In the Assignee(s) list, select Users or Fact Sheet subscriptions. Depending on the option you selected, select specific users or subscription types and roles.
Instead of selecting a fixed list of users, you can use subscriptions from a fixed reference fact sheet of any type within the workspace. This could be a fact sheet of the organization type or a custom type representing team or organizational entities. This method minimizes manual maintenance and allows dynamic assignment. To implement this, in the Assignee(s) list, select Fixed Fact Sheet subscriptions, select a reference fact sheet, then select subscription types and roles.
    4. In the Due (in days) field, enter the number of days indicating when the to-do item is due.
  5. Save the automation.
