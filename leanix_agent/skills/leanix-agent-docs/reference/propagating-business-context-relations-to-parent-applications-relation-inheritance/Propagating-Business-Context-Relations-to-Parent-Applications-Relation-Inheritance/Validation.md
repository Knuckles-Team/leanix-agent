##  Validation
After configuring all four automations, validate the implementation using the following test scenarios:
Test Scenarios for Validation Test Scenario | Expected Result
---|---
Add a business context to a child application. | The business context appears on the parent application with [Auto-inherited from: Child Name] in the description.
Remove a business context from a child (other children still have it). | The parent's business context description updates to show remaining children.
Remove a business context from a child (no children have it). | The business context is removed from the parent.
Unlink a child from a parent (from the parent side). | The parent's inherited business contexts are reconciled.
A child removes its parent relation. | Catch-all reconciles all potential parents.
Manually add a business context to a parent. | Business contexts added manually are preserved and not affected by automation.


