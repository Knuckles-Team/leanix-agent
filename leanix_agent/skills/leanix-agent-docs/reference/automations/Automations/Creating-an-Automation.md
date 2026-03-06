##  Creating an Automation
To create an automation, follow these steps:
  1. In the administration area, navigate to Automations.
  2. Click New Automation.
  3. Enter a name and, optionally, a description for the automation.
  4. Select an owner for the automation.
Any workspace user can be an automation owner. They serve as a default assignee for "orphaned" to-dos created by an automation and as a default subscriber to a fact sheet when the intended user is unavailable (for example, when the user no longer exists). As a fallback solution for automations, owners are expected to reassign to-dos or modify subscriptions directed to them as needed.
  5. In the When section, specify the trigger for the automation:
    1. In the Fact Sheet Type list, select a fact sheet type.
    2. In the Event list, select an event for which the automation is triggered.
    3. Depending on the event that you selected, specify the required values.
  6. In the If section, specify conditions for the automation.
    1. Decide whether you want to include or exclude events initiated by technical users.
Technical users are used in integrations, the reference catalog, and more. Excluding events initiated by technical users is beneficial when you want to prevent triggering automations from mass changes to your workspace. For example, you might not want an approval to be triggered when a fact sheet is created from the catalog.
    2. Optional: Specify one or more additional conditions: fact sheet category, assigned tags, or single-select field values. An automation is initiated only if all the specified conditions are met.
You can add multiple conditions for single-select fields to an automation. Within a condition, the OR logical operator is used, which means that any of the specified field values is included.
For tags, the AND logical operator is used within a condition, which means that all of the specified tags must be included.
  7. In the Then section, specify actions for the automation.
You can add up to 100 actions for an automation. Actions are initiated sequentially in the order that you specify.
  8. Decide whether you want to activate the automation after saving it or only save it in draft state:
     * To activate the automation after saving it, click Save and Run Automation.
     * To save the automation in draft state, click the arrow button, then click Save in Draft State.
