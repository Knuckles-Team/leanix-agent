##  Automation Logic
When initiatives reach the End of Life phase, quality seals automatically break on all related applications. If an application is related to multiple initiatives, the quality seal breaks if any one of these initiatives reaches End of Life. Fact sheet owners need to reapprove quality seals.
To implement this scenario, you need a set of two automations.
Automation | Fact Sheet Type | Trigger Event | Logic
---|---|---|---
[Automation 1: Lifecycle Phase Is Reached](https://help.sap.com/docs/leanix/ea/breaking-application-quality-seals-when-initiatives-reach-end-of-life?locale=en-US&state=PRODUCTION&version=CLOUD#loiofe9ac3c172fe4d3faf012356d850e8a8__automation-1-lifecycle-phase-is-reached) | Initiative | Lifecycle state is reached: End of Life | When an initiative reaches End of Life, break quality seals on all related applications.
[Automation 2: Relation Is Added](https://help.sap.com/docs/leanix/ea/breaking-application-quality-seals-when-initiatives-reach-end-of-life?locale=en-US&state=PRODUCTION&version=CLOUD#loiofe9ac3c172fe4d3faf012356d850e8a8__automation-2-relation-is-added) | Application | Relation is added | When an initiative is linked to an application, check if the related initiative's lifecycle date is End of Life and break the quality seal if needed.


