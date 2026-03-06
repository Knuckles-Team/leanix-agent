##  Adding a Subscription on Tag Addition or Removal
Certain tags may require higher visibility, such as the "Mission critical" tag on applications. As notifications about changes to fact sheets are typically sent to subscribers, it's beneficial to assign a primary responsible party, such as the Security Officer, as a subscriber to those fact sheets. This automation ensures that vital updates are promptly communicated to the appropriate party.
The following image shows the logic of the automation.
![612](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2751d2a37a44101480389bd942667895_LowRes.png)
Automation: Adding a Subscription on Tag Addition or Removal
To configure the automation, follow these steps:
  1. Enter a name and select an owner for the automation. Optionally, enter a description.
  2. In the When section, specify the trigger for the automation:
    1. In the Fact Sheet Type list, select a fact sheet type.
    2. In the Event list, select Tag is added or Tag is removed, then select a tag.
  3. In the If section, specify conditions for the automation:
    1. Include or ignore fact sheets that are updated by technical users.
    2. Optional: Add conditions to trigger the automation for: fact sheet category, assigned tags, or single-select field values.
  4. In the Then section, specify the action for the automation:
    1. Click Add Action, then select Add subscription (or Set subscription).
    2. In the New Subscriber list, select User, then select a user.
    3. Select a subscription type and, if applicable, one or more subscription roles to apply.
    4. If needed, repeat the process to add more users.
  5. Save the automation.
