##  Automation Logic
To implement relation inheritance, you need a set of four automations.
Automations for Relation Inheritance Automation | Fact Sheet Type | Trigger Event | Logic
---|---|---|---
[Automation 1: Relation Is Added (Business Context to Child)](https://help.sap.com/docs/leanix/ea/propagating-business-context-relations-to-parent-applications-relation-inheritance?locale=en-US&state=PRODUCTION&version=CLOUD#loio2ad6775d50c442168a6dd398192dab72__automation-1) | Application | Relation is added: business contexts | When a business context relation is added to a child application, it's propagated to the parent.
[Automation 2: Relation Is Removed (Business Context from Child)](https://help.sap.com/docs/leanix/ea/propagating-business-context-relations-to-parent-applications-relation-inheritance?locale=en-US&state=PRODUCTION&version=CLOUD#loio2ad6775d50c442168a6dd398192dab72__automation-2) | Application | Relation is removed: business contexts | When a business context relation is removed from a child application, the parent is updated accordingly.
[Automation 3: Child Unlinked from Parent (Parent Side)](https://help.sap.com/docs/leanix/ea/propagating-business-context-relations-to-parent-applications-relation-inheritance?locale=en-US&state=PRODUCTION&version=CLOUD#loio2ad6775d50c442168a6dd398192dab72__automation-3) | Application | Relation is removed: children | When a child is unlinked from a parent (triggered on the parent), inherited business contexts are reconciled.
[Automation 4: Child Removes Parent Relation (Catch-All)](https://help.sap.com/docs/leanix/ea/propagating-business-context-relations-to-parent-applications-relation-inheritance?locale=en-US&state=PRODUCTION&version=CLOUD#loio2ad6775d50c442168a6dd398192dab72__automation-4) | Application | Relation is removed: parent | Catch-all: when a child removes its parent relation, all potential parents are reconciled.


