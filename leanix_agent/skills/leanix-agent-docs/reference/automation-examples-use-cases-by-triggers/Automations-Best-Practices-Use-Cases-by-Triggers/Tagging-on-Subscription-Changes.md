##  Tagging on Subscription Changes
As mentioned earlier, missing or removed subscriptions often require action. A practical way to draw attention to these fact sheets is by assigning a specific tag (for example, "Application Owner Missing") when a subscription is removed. This tagging system simplifies the process of filtering for these fact sheets, ensuring prompt attention.
The following image shows the logic of the automation.
![Automation: Adding a Tag on Adding or Removing a Subscription](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2755527b7a441014af3e8635ca7de0bb_LowRes.png)
Automation: Adding a Tag on Subscription Addition or Removal
To configure the automation, follow these steps:
  1. Enter a name and select an owner for the automation. Optionally, enter a description.
  2. In the When section, specify the trigger for the automation:
    1. In the Fact Sheet Type list, select a fact sheet type.
    2. In the Event list, select Subscription is added (or Subscription is removed).
    3. Select a subscription type and, if applicable, subscription role.
  3. In the If section, specify conditions for the automation:
    1. Include or ignore fact sheets that are updated by technical users.
    2. Optional: Add conditions to trigger the automation for: fact sheet category, assigned tags, or single-select field values.
  4. In the Then section, specify the action for the automation:
    1. Click Add Action, select Add tag (or Remove tag), then select a tag.
    2. If needed, repeat the process to add more actions for tags.
  5. Save the automation.
