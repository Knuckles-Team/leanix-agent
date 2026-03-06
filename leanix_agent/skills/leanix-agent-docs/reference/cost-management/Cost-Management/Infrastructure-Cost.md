##  Infrastructure Cost
Infrastructure costs cover costs that are required for enabling applications to be run through the help of IT components. Therefore, infrastructure cost are maintained on the application fact sheet, on the relation to IT components. Typically, these costs are summarized for one year why they are also called total annual cost.
Depending on your organizations definition, there can be different approaches to handle infrastructure cost:
  * SAP LeanIX default: Infrastructure costs as independent cost entity, not included in other costs
  * Configuration option: Infrastructure costs as part of the total cost of ownership of an application


Each approach on handling infrastructure cost has reasons and it mainly is a decision what helps you in your daily enterprise architecture work. If you want to include infrastructure costs in the total cost of ownership, this requires additional configurations like changing calculations.
Infrastructure Cost Field | Description | Where to Find
---|---|---
Total annual cost | Fees paid to acquire the right to use a software product. This can be a one-time perpetual license, an annual subscription, or usage-based charges, for example, per-user, per-CPU, or per-instance. Licensing is considered part of the total cost of ownership for an application. |  Application fact sheet > Sourcing section > IT components ![Form for entering IT component details, highlighting the total annual cost field.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio236e2912644349298bf3313709c75d96_HiRes.png)


### Calculations and Cost Allocation for Infrastructure Costs
Allocate infrastructure costs to the according business capability to get more detailed and helpful insights, for example, on the business capability cost report.
In the application fact sheet, set the Support Type on the relation between application and business capability to Leading or Supports. The cost allocation is calculated automatically based on this setting:
  * 0 Leading: Costs are split equally between these business capabilities
  * 1 leading business capability: Costs are allocated to this business capability only
  * +1 leading business capabilities: Costs are split equally between these business capabilities


### Analyze Infrastructure Costs
The available cost data can help you answer questions such as:
  * How much do we pay for a specific infrastructure asset?
  * Which applications drive infrastructure costs?
  * Which business capabilities have cost-saving potential?


IT Component Fact Sheet
At the IT component fact sheet, you can see how costs are distributed for applications relying on the IT component. Go to the IT component fact sheet and navigate to Sourcing section. Under Applications, you see the total annual cost per application.
![IT component fact sheet showing annual costs for software, hardware, and service items.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27550e377a4410148941ae3b4b34a035_LowRes.png)
Application Landscape Report
The Application Landscape report creates a heat map of the cost distribution in relation to Business Capabilities, Processes or Organization. Costs are color-coded to allow a quick analysis of the hot spots.
![Application Landscape heat map showing annual IT costs by application and business area.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio5b715fd12364418aa48840ab05b812e4_HiRes.png)
Business Capability Cost Report
The Business Capability Cost report summarizes the run costs by business capability.
![Bar chart showing total run costs per business capability in USD.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275138807a441014958ea2fa486beac3_LowRes.png)
Provider Cost Report
The provider cost report sums up the run costs by provider.
![Pie chart showing IT provider costs, with meshlab IT as the largest segment.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2756f2de7a441014905b8d1b9f830f5f_LowRes.png)
