##  Changing a Field Value Based on Another Field Value
This automation enables you to set the value of certain fact sheet fields based on the values of others. For example, if any single-select fields pertaining to the personal data of employees, suppliers, or customers are marked as "Yes," the automation can automatically set a read-only field, such as "Compliance Relevance," to "Yes." This reduces data inconsistency and eliminates the need for manual data clean-up efforts.
The following image shows the logic of the automation.
![1530](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274fcd217a44101485c98e3bd4cbd17d_LowRes.png)
Automation: Changing a Field Value Based on Another Field Value
To configure the automation, follow these steps:
  1. Enter a name and select an owner for the automation. Optionally, enter a description.
  2. In the When section, specify the trigger for the automation:
    1. In the Fact Sheet Type list, select a fact sheet type.
    2. In the Event list, select Field changes.
    3. In the Field list, select a single-select field, then select values in the To and From lists.
  3. In the If section, specify conditions for the automation:
    1. Include or ignore fact sheets that are updated by technical users.
    2. Optional: Add conditions to trigger the automation for: fact sheet category, assigned tags, or single-select field values.
  4. In the Then section, specify the actions for the automation:
    1. Click Add Action, select Set field, select a single-select field, then select a value based on the value that you specified as trigger.
    2. If needed, repeat the process to add more actions for setting field values.
  5. Save the automation.
