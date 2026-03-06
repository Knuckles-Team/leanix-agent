##  Conditional Tagging
Tags can sometimes be interdependent. Using triggers on tag addition or removal, especially in combination with additional conditions, can help maintain data consistency in these scenarios. For example, when a tag from the "Region" tag group related to GDPR is applied, the "GDPR Relevant" tag can be automatically added. This automation eliminates the need to assign or remove tags based on other tags.
The following image shows the logic of the automation.
![612](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274cfaad7a441014b251ee51beb19ed7_LowRes.png)
Automation: Adding a Tag on Tag Addition or Removal
To configure the automation, follow these steps:
  1. Enter a name and select an owner for the automation. Optionally, enter a description.
  2. In the When section, specify the trigger for the automation:
    1. In the Fact Sheet Type list, select a fact sheet type.
    2. In the Event list, select Tag is added (or Tag is removed), then select a tag.
  3. In the If section, specify conditions for the automation:
    1. Include or ignore fact sheets that are updated by technical users.
    2. Optional: Add conditions to trigger the automation for: fact sheet category, assigned tags, or single-select field values.
  4. In the Then section, specify the action for the automation:
    1. Click Add Action, select Add tag (or Remove tag), then select a tag.
    2. If needed, repeat the process to add more actions for tags.
  5. Save the automation.
