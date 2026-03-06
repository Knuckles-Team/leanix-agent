##  Automation Logic
To implement subscription inheritance, you need a set of four automations.
Automations for Subscription Inheritance Automation | Fact Sheet Type | Trigger Event | Logic
---|---|---|---
[Automation 1: Subscription Is Added](https://help.sap.com/docs/leanix/ea/synchronizing-subscriptions-across-related-fact-sheets-subscription-inheritance?locale=en-US&state=PRODUCTION&version=CLOUD#loioe51af489e10b4881960c990ec046e62f__automation-1) | Application | Subscription is added | When a subscription is added to an application, it’s also added to related IT components.
[Automation 2: Subscription Is Removed](https://help.sap.com/docs/leanix/ea/synchronizing-subscriptions-across-related-fact-sheets-subscription-inheritance?locale=en-US&state=PRODUCTION&version=CLOUD#loioe51af489e10b4881960c990ec046e62f__automation-2) | Application | Subscription is removed | When a subscription is removed from an application, it's also removed from all related IT components.
[Automation 3: Relation Is Added](https://help.sap.com/docs/leanix/ea/synchronizing-subscriptions-across-related-fact-sheets-subscription-inheritance?locale=en-US&state=PRODUCTION&version=CLOUD#loioe51af489e10b4881960c990ec046e62f__automation-3) | Application | Relation is added | When a relation is added from an application to an IT component, all subscriptions are propagated to the IT component.
[Automation 4: Relation Is Removed](https://help.sap.com/docs/leanix/ea/synchronizing-subscriptions-across-related-fact-sheets-subscription-inheritance?locale=en-US&state=PRODUCTION&version=CLOUD#loioe51af489e10b4881960c990ec046e62f__automation-4) | IT component | Relation is removed | When a relation to consuming applications is removed from an IT component, all subscriptions are removed from the IT component.


