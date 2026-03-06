##  Conditions
The following table lists the available conditions for initiating automations. An automation is initiated only if all the specified conditions are met.
Conditions | Values | Additional Information
---|---|---
Technical user |
  * Ignored
  * Included

| Defines whether actions initiated by technical users should be included or ignored as triggering events.
Category | All categories defined for the selected fact sheet type | You can only select one category.
Tag(s) | All tags configured for the selected fact sheet type | You can select multiple tags. For single-select tag groups, you can only select one tag.
Single- select field | All single-select fields of the selected fact sheet type and all of their values, as well as the Empty option | You can add multiple conditions for single-select fields to an automation. Within a condition, the OR logical operator is used, which means that any of the specified field values is included.
Lifecycle field |  All available lifecycle fields, including custom lifecycles |  Checks if the lifecycle phase for a fact sheet matches the selected phases when the automation triggers. Optionally, you can specify if a fact sheet's lifecycle phase should match the selected phases for a certain number of days before or after the automation triggers.
String fields | All string fields configured for the selected fact sheet type | Select logical operators for string fields to check values against specific conditions.
Numeric fields:
  * Integer
  * Double

| All numeric fields configured for the selected fact sheet type | Select a condition for numeric fields and enter a value.
Completion score |  Logical operators for a value:
  * Equals
  * Greater than
  * Less than
  * Greater than or equal
  * Less than or equal

| Select a condition for the completion score and enter a value.


