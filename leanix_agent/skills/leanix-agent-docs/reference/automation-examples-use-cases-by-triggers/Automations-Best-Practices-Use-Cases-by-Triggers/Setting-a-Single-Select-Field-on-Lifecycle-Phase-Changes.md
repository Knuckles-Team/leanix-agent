##  Setting a Single-Select Field on Lifecycle Phase Changes
This automation streamlines responses to lifecycle phase changes by automatically setting single-select field values on fact sheets. For example, you can automatically update a read-only field with the current lifecycle phase, which enhances visibility of the fact sheet state and simplifies filtering.
Additionally, you can map lifecycle states to other custom fields, such as "inactive" or "active." These single-select fields can then be used as conditions in other automations.
The following image shows the logic of the automation.
![Automation: Setting a Single-Select Field on Lifecycle Phase Changes](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274567307a441014bf93fa29870db466_LowRes.png)
Automation: Setting a Single-Select Field on Lifecycle Phase Changes
To configure the automation, follow these steps:
  1. Enter a name and select an owner for the automation. Optionally, enter a description.
  2. In the When section, specify the trigger for the automation:
    1. In the Fact Sheet Type list, select a fact sheet type.
    2. In the Event list, select Lifecycle phase change.
    3. In the Field list, select Lifecycle, then select a lifecycle phase.
    4. Optional: To define when the automation should be initiated (before or after the phase change date), click the Trigger before/after toggle and set the timing in days.
  3. Optional: In the If section, specify conditions for the automation: fact sheet category, assigned tags, or single-select field values.
  4. In the Then section, specify the action for the automation:
    1. Click Add Action, select Set field, select a single-select field, then select a value based on the value that you specified as trigger.
    2. If needed, repeat the process to add more actions for setting field values.
  5. Save the automation.
