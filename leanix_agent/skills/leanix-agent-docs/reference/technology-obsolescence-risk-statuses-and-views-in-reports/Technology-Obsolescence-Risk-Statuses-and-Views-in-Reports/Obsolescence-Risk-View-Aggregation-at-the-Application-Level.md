##  Obsolescence Risk View Aggregation at the Application Level
The aggregated obsolescence risk is calculated based on the lifecycle status of the underlying IT components that support your applications. The calculation for aggregated obsolescence risk considers all IT components related to an application in the following ways:
  * Directly linked IT components: IT components that are directly linked to the application via the relApplicationToITComponent relation and are active are considered. Inactive relations are excluded; the 'active from/until' field in the relation between IT components and applications determines the active or inactive status.
  * Indirectly linked IT components: These are IT components indirectly connected to an application either through hierarchical relations relToChild between IT components or as required/required by relations relToRequires between IT components.
  * Indirectly linked via other applications: IT components indirectly connected to the application through another application with an active hierarchical relation relToChild are also included in the risk assessment.


The following order, from highest to lowest, indicates the severity of the risk status of applications:
  * Unaddressed Risk
  * Unaddressed Phase Out
  * Upcoming Risk
  * Missing IT Component Information
  * Risk Accepted
  * Risk Addressed
  * No Risk


![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiof75ab0a4baea47cdae1fc034adb13d37_LowRes.png)
Aggregation of Obsolescence Risk
