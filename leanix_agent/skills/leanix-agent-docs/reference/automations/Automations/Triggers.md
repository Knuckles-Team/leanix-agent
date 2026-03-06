##  Triggers
The following table lists the available triggering events for automations. When a triggering event occurs, the conditions are checked, and if met, actions are initiated.
A trigger is configured for a specific fact sheet type. The Fact Sheet Type list contains all fact sheet types defined in the meta model configuration. You can only select one fact sheet type.
Event | Values | Additional Information
---|---|---
Fact sheet is created | N/a | The trigger is the creation of a fact sheet of a specific type.
Field value is changed |
  * Double fields
  * Integer fields
  * String fields
  * Single-select fields
  * Lifecycle field
  * Unused fields

|  String fields: Any changes to a string field trigger an automation Single-select fields: Select initial and target values in the From and To lists. These lists include specific values, as well as “Empty” and “Anything.” An automation is triggered when a field is updated from the selected source to the target value.
Lifecycle state is reached |
  * Field: all available lifecycle fields, including custom lifecycles
  * States: all defined phases of the lifecycle field

|  Important: This trigger is only checked nightly. Automation is triggered when the fact sheet reaches the selected lifecycle phase.  Optionally, you can specify whether the automation should be activated before or after the specified lifecycle phase date is reached using the Trigger before/after toggle. Enable the toggle, then specify the number of days before or after the lifecycle phase date is reached.
Quality state is changed to |
  * Approved
  * Broken
  * Draft
  * Rejected

| The transition to the selected quality state triggers an automation.
Subscription is added | All subscription types and, if applicable, all combinations of subscription types and roles, as defined in the workspace configuration | You can only select one subscription type or, if applicable, a combination of a subscription type and role.
Subscription is removed | All subscription types and, if applicable, all combinations of subscription types and roles, as defined in the workspace configuration | You can only select one subscription type or, if applicable, a combination of a subscription type and role.
Tag is added | All tags configured for the selected fact sheet type | You can only select one tag.
Tag is removed
Completion score is changed | N/a | You can use changes in the completion score as a condition in your automations. This lets you set logical operators to define the range.
Relation is added | All relations configured for the selected fact sheet type | Configure automations that initiate when a relation is added, changed, or removed.
Relation is changed
Relation is removed


