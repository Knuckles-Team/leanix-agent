##  Adding Tags or Setting Single-Select Field Values on Newly Created Fact Sheets
This automation pre-populates newly created fact sheets with initial tags, enhancing data quality and reducing manual effort. For example, you can automatically add a default tag "New" to new fact sheets.
Alternatively, you can set single-select fields to specific values on newly created fact sheets.
While our customer support team can set default values, this automation enables you to customize them yourself. An added advantage is that the user who creates a fact sheet doesn't need to have permissions to update the fact sheet.
The following image shows the logic of the automation.
![Automation: Adding Tags on Newly Created Fact Sheets](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27467a3a7a441014bd7eea2386bb3660_LowRes.png)
Automation: Adding Tags on Newly Created Fact Sheets
To configure the automation, follow these steps:
  1. Enter a name and select an owner for the automation. Optionally, enter a description.
  2. In the When section, specify the trigger for the automation:
    1. In the Fact Sheet Type list, select a fact sheet type.
    2. In the Event list, select Fact Sheet is created.
  3. In the If section, specify conditions for the automation:
    1. Include or ignore fact sheets that are created by technical users.
    2. Optional: Add a condition for a specific fact sheet category to trigger the automation for.
  4. In the Then section, specify the actions for the automation:
    1. Click Add Action, select Add tag, then select a tag to add to fact sheets.
    2. If needed, repeat the process to add more actions for tags.
  5. Save the automation.
