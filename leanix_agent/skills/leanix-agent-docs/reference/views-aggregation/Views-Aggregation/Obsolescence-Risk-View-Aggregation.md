##  Obsolescence Risk View Aggregation
The aggregated obsolescence risk is calculated based on the lifecycle status of the underlying IT components that support your applications. The calculation for aggregated obsolescence risk considers all IT components related to an application in the following ways:
  * Directly linked IT components: IT components that are directly linked to the application via the relApplicationToITComponent relation and are active are considered. Inactive relations are excluded; the 'active from/until' field in the relation between IT components and applications determines the active or inactive status.
  * Indirectly linked IT components: These are IT components indirectly connected to an application either through hierarchical relations relToChild between IT components or as required/required by relations relToRequires between IT components.
**Note**
relToRequires relations directly between IT components and applications are not considered.
  * Indirectly linked via other applications: IT components indirectly connected to the application through another application with an active hierarchical relation relToChild are also included in the risk assessment.
  * Indirectly linked via microservice subtype: IT components that are indirectly connected to an application through microservices are also included in risk aggregation. We recommend linking only the versioned IT component that is actually in use to the microservice to avoid surfacing aggregated obsolescence risk from the product line level IT component. For more details, see [Aggregating Obsolescence Risk for Self-Built Software](https://help.sap.com/docs/leanix/ea/obsolescence-risk-management-advanced?version=CLOUD#aggregating-obsolescence-risk-for-self-built-software "https://help.sap.com/docs/leanix/ea/obsolescence-risk-management-advanced?version=CLOUD#aggregating-obsolescence-risk-for-self-built-software")


The following order, from highest to lowest, indicates the severity of the risk status of applications:
  * Unaddressed Risk
  * Unaddressed Phase Out
  * Upcoming Risk
  * Missing IT Component Information
  * Risk Accepted
  * Risk Addressed
  * No Risk


Aggregation of Obsolescence Risk![Aggregation of Obsolescence Risk](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiof75ab0a4baea47cdae1fc034adb13d37_LowRes.png)
**Note**
  * For customers using SAP LeanIX Technology Risk and Compliance, the vendor-provided end-of-support date is automatically populated and synced from the reference catalog. To learn more, see [Vendor-Provided Lifecycle Information for IT Components](https://help.sap.com/docs/leanix/ea/obsolescence-risk-management-capabilities?locale=en-US&state=PRODUCTION&version=CLOUD#loio275b7d287a4410148716e8d55ebf2ec4__vendor-provided_lifecycle_information_for_it_components).
  * The algorithm considers internal, vendor-provided, and custom vendor lifecycle fields for view aggregation.
