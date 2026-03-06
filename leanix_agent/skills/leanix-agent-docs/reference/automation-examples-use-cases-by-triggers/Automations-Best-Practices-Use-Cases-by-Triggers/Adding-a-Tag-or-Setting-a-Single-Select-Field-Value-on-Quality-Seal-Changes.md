##  Adding a Tag or Setting a Single-Select Field Value on Quality Seal Changes
While the quality state is a standalone field on a fact sheet with various uses, associating a tag (from a designated single-select tag group with all states as tags) based on quality state changes can unlock additional opportunities. For example, it enables you to use these values in pie and bar charts with key performance indicators (KPIs).
Alternatively, you can use a single-select field for quality state changes.
The following image shows the logic of the automation.
![Automation: Adding a Tag on Quality Seal Changes](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275602a67a441014b4b088ecf95dffae_LowRes.png)
Automation: Adding a Tag on Quality Seal Changes
In the following example, we add a tag and set a single-select field value on a fact sheet.
To configure the automation, follow these steps:
  1. Enter a name and select an owner for the automation. Optionally, enter a description.
  2. In the When section, specify the trigger for the automation:
    1. In the Fact Sheet Type list, select a fact sheet type.
    2. In the Event list, select Quality State changes to, then select a state (for example, Broken).
  3. In the If section, specify conditions for the automation:
    1. Include or ignore fact sheets that are updated by technical users.
    2. Optional: Add conditions to trigger the automation for: fact sheet category, assigned tags, or single-select field values.
  4. In the Then section, specify the action for the automation:
    1. Click Add Action, select Add tag, then select a tag to add to fact sheets.
    2. Click Add Action, select Set field, select a field, then select the field value to set on fact sheets.
    3. If needed, repeat the process to add more actions for tags and fields.
  5. Save the automation.
  6. Create automations for other quality states as described in this instruction. To streamline the process, you can copy an automation and make the necessary changes in the configuration.
