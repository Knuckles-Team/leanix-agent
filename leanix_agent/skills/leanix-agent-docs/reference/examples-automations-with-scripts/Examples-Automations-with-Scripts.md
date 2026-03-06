# Examples: Automations with Scripts
Explore use cases for automations with scripts.
Automations with Scripts: Use Cases Use Case | Trigger Event | Description
---|---|---
[Synchronizing Subscriptions Across Related Fact Sheets (Subscription Inheritance)](https://help.sap.com/docs/leanix/ea/synchronizing-subscriptions-across-related-fact-sheets-subscription-inheritance?locale=en-US&state=PRODUCTION&version=CLOUD "Configure automations with scripts to automatically synchronize subscriptions across related fact sheets.") |
  * Subscription is added
  * Subscription is removed
  * Relation is added
  * Relation is removed

|  Synchronize subscriptions across related fact sheets when a subscription or a relation is added or removed. For example, when an application owner is assigned to an application, they are also assigned to all related IT components. The scripts call the GraphQL API endpoint to update fact sheet data.
[Propagating Business Context Relations to Parent Applications (Relation Inheritance)](https://help.sap.com/docs/leanix/ea/propagating-business-context-relations-to-parent-applications-relation-inheritance?locale=en-US&state=PRODUCTION&version=CLOUD "Configure automations with scripts to automatically propagate relations from business contexts to parent applications.") |
  * Relation is added
  * Relation is removed

|  Propagate business contexts from child applications to parent applications. The scripts call the GraphQL API endpoint to update fact sheet data.
[Breaking Application Quality Seals when Initiatives Reach End of Life](https://help.sap.com/docs/leanix/ea/breaking-application-quality-seals-when-initiatives-reach-end-of-life?locale=en-US&state=PRODUCTION&version=CLOUD "Configure automations with scripts to automatically break quality seals on applications when related initiatives reach End of Life.") |
  * Lifecycle state is reached
  * Relation is added

|  When initiatives reach the End of Life phase, automatically break quality seals on all related applications to ensure they are reviewed and updated. The scripts call the GraphQL API endpoint to update fact sheet data.
[Validating the Plan Lifecycle Phase](https://help.sap.com/docs/leanix/ea/validating-plan-lifecycle-phase?locale=en-US&state=PRODUCTION&version=CLOUD "Configure an automation with a script to validate the Plan lifecycle phase on fact sheets and adjust it if needed.") | Field value is changed | To ensure the Plan lifecycle phase for applications isn't set in the future, create an automation that validates the date for this phase. If the date is in the future, the automation sets it to the current date. You can also notify fact sheet subscribers to check other lifecycle dates by sending to-dos.
[Updating a Lifecycle Phase and Approving the Quality Seal](https://help.sap.com/docs/leanix/ea/updating-lifecycle-phase-and-approving-quality-seal?locale=en-US&state=PRODUCTION&version=CLOUD "Configure an automation with a script to check lifecycle phases on fact sheets and require reapproval from fact sheet owners.") | Field value is changed | Ensure that the installation status of applications is in sync with their lifecycle. When the installation status (custom field) is automatically updated by an integration, a script infers the lifecycle based on the sync date and sets the quality seal to Draft. An approval to-do is sent to fact sheet subscribers to approve the changes. Once approved, the quality seal is set to Approved.
[Syncing Tags with the Current Lifecycle Phases](https://help.sap.com/docs/leanix/ea/syncing-tags-with-current-lifecycle-phases?locale=en-US&state=PRODUCTION&version=CLOUD "Configure an automation with a script to add tags that match the current lifecycle phase to fact sheets.") | Field value is changed | Sync tags on fact sheets with their current lifecycle phases. For example, when applications enter the active lifecycle phase, automatically add the tag "Active."
[Updating Lifecycle Phases](https://help.sap.com/docs/leanix/ea/updating-lifecycle-phases?locale=en-US&state=PRODUCTION&version=CLOUD "Configure an automation with a script to update lifecycle phases on applications based on your defined timeframes.") | Field value is changed | Automatically update lifecycle phases according to your organization’s policies. For example, you can set a minimum timeframe for each phase to 90 days.


