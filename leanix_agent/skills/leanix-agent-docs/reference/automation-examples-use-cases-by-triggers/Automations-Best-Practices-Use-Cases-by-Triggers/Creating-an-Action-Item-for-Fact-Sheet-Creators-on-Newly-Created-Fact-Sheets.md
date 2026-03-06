##  Creating an Action Item for Fact Sheet Creators on Newly Created Fact Sheets
This automation creates an action item (to-do) for fact sheet creators. In the to-do, you can include comprehensive instructions on what the fact sheet creator needs to do, such as filling mandatory fields, approving the fact sheet, or identifying the application owner. This guidance ensures a smooth and efficient approval process of new fact sheets.
The following image shows the logic of the automation.
![Automation: Creating an Action Item for Fact Sheet Creators on Newly Created Fact Sheets](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2742f82b7a4410149425c00503391462_LowRes.png)
Automation: Creating an Action Item for Fact Sheet Creators on Newly Created Fact Sheets
To configure the automation, follow these steps:
  1. Enter a name and select an owner for the automation. Optionally, enter a description.
  2. In the When section, specify the trigger for the automation:
    1. In the Fact Sheet Type list, select a fact sheet type.
    2. In the Event list, select Fact Sheet is created.
  3. In the If section, specify conditions for the automation:
    1. Include or ignore fact sheets that are created by technical users.
    2. Optional: Add a condition for a specific fact sheet category to trigger the automation for.
  4. In the Then section, specify the action for the automation:
    1. Click Add Action, then select Create To-Do: Action Item.
    2. Enter a name for the action item and, optionally, a description.
    3. In the Assignee(s) list, select Fact Sheet creator.
    4. In the Due (in days) field, enter the number of days indicating when the to-do item is due.
  5. Save the automation.
