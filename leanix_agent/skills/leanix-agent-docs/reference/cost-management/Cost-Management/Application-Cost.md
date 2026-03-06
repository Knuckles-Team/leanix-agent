##  Application Cost
**Note**
The total cost of ownership fields and calculations are not included in the predefined meta model. To use them, activate the Application Total Cost of Ownership extension to the meta model. For details, see [Application Total Cost of Ownership (TCO) Extension](https://help.sap.com/docs/leanix/ea/application-total-cost-of-ownership-extension?locale=en-US&state=PRODUCTION&version=CLOUD "Gain transparency into total cost of ownership with the extension that activates dedicated fields, calculations, as well as options for reports and KPIs for dashboards.").
Cost related to an application are summarized as total cost of ownership of applications. Application costs are maintained on the application fact sheet and cover all cost spanning the whole life time of an application.
Cost Type | Field | Description | Where to Find
---|---|---|---
Total cost of ownership Aggregates application relevant costs like, license, maintenance, support | License cost | Fees paid to acquire the right to use a software product. This can be a one-time perpetual license, an annual subscription, or usage-based charges, for example, per-user, per-CPU, or per-instance. Licensing is considered part of the total cost of ownership for an application. |  Application fact sheet ![Application costs section showing total, maintenance, licensing, and support costs in euros.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio56f9c06b9d1344d2bcf6d1b848f939d7_HiRes.png)
Maintenance cost | Recurring charges that entitle you to product updates, patches, and new releases. Maintenance ensures your software stays current and secure over its lifecycle. The costs are often occur annually and are considered part of the total cost of ownership for an application.
Support cost | Fees for access to vendor-provided assistance such as help-desk support, troubleshooting, incident response, and escalations. Support costs are considered part of the total cost of ownership for an application.


**Note**
You can modify the names of the existing fields in SAP LeanIX to better match your internal terminology. It’s also possible to add additional cost types depending how total cost of ownership is defined in your organization.
Make sure that any changes or additional fields will need to be reflected in the calculation that sums up the total cost of ownership of applications.
### Calculations and Cost Allocation for Application Costs
Cost allocation is calculated automatically. It’s based on either the support for business capabilities or the usage type for organizations:
  * No leading business capability / no owner (organization): Costs are divided equally between all related business capabilities, same treatment of support type supporting and no support type assignment
  * 1 leading business capability / 1 owner (organization): Costs are assigned to this business capability
  * More than 1 leading business capabilities / more than 1 owner (organization): Costs are divided equally between all leading business capabilities

![Business capabilities list showing support types: Leading, Supports, and unassigned.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio139e144a3f914e28acfe4306ba20b613_HiRes.png)
### Analyze Application Costs
Taking a closer look at your the total cost of ownership of applications can reveal insights on:
  * How are application costs distributed across business capabilities?
  * Which applications are the most cost-intensive and why?
  * Are there opportunities for cost savings? How would retiring or replacing an application impact the overall total cost of ownership for a business capability?
  * What is the cost distribution between license, maintenance, and support for each application?


Understand cost structures for business capabilities better with the Landscape report.
