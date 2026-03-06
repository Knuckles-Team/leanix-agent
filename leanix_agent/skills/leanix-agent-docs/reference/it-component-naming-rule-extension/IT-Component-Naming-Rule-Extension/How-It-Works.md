##  How It Works
### Pre-Validation
Removing the parent prefix could, in rare cases, result in two IT components ending up with the same name. To avoid that, before any changes are made, the extension verifies that the new names will not create duplicate display names in your workspace.
If conflicts are detected, the extension does not proceed. Instead, it provides a detailed list of affected IT components that need to be renamed first. Once resolved, you can re-run the extension.
If validation passes, the change is scheduled for execution.
### Scheduled Execution
Applying the new naming rule requires a workspace-level operation that temporarily prevents other changes. To ensure system continuity and avoid disruption during your working day, the change is automatically scheduled outside of your usual working hours. You will be notified in the product once the update is complete.
