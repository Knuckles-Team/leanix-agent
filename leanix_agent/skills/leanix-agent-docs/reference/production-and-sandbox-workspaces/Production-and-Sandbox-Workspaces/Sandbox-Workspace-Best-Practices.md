##  Sandbox Workspace Best Practices
A sandbox workspace is useful for testing large-scale changes to data without impacting the live workspace, ensuring safe implementation before applying changes to production. Some common use cases are:
  * Initial Setup of Out-of-the-Box Integrations (e.g., SAP Signavio, ServiceNow, Collibra)
These integrations may create dozens or even hundreds of fact sheets during the first sync, which can have a significant impact. It's recommended to set up and review the first sync in a sandbox before applying it to the live workspace.
  * Building Custom Integrations
Custom integrations using SAP LeanIX's public APIs can also create and alter large volumes of data. Hence, implement and test these integrations iteratively in a sandbox workspace before applying them to the live workspace.
  * Initial Setup of Large-Scope Automations
Automations that trigger changes to a large number of fact sheets (e.g., when many fact sheets are created simultaneously by integrations, and you have set fact sheet creation as a trigger for the automation) should be tested in a sandbox first. Since changes made by automation are only logged in the audit trail of each changed fact sheet, testing in a sandbox helps ensure the process runs smoothly before applying it to the live workspace.
