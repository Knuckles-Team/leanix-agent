##  Adding or Removing a Tag on Lifecycle Phase Changes
This automation streamlines responses to lifecycle phase changes by automatically adding or removing tags. For example, you can automatically add tags such as "End of Life Reached" or "Archive" or remove tags from a fact sheet once a specific lifecycle phase is reached. This eliminates the need for manual data maintenance and enhances data quality.
The following image shows the logic of the automation.
![Automation: Adding a Tag on Lifecycle Phase Changes](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274e1b707a44101491ba8954d5f26f04_LowRes.png)
Automation: Adding a Tag on Lifecycle Phase Changes
To configure the automation, follow these steps:
  1. Enter a name and select an owner for the automation. Optionally, enter a description.
  2. In the When section, specify the trigger for the automation:
    1. In the Fact Sheet Type list, select a fact sheet type.
    2. In the Event list, select Lifecycle phase change.
    3. In the Field list, select Lifecycle, then select a lifecycle phase.
    4. Optional: To define when the automation should be initiated (before or after the phase change date), click the Trigger before/after toggle and set the timing in days.
  3. Optional: In the If section, specify conditions for the automation: fact sheet category, assigned tags, or single-select field values.
  4. In the Then section, specify the action for the automation:
    1. Click Add Action, select Add tag, then select a tag to add to fact sheets.
    2. If needed, repeat the process to add more actions for adding tags.
  5. Save the automation.
