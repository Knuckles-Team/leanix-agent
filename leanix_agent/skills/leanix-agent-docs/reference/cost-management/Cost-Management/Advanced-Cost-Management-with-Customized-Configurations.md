##  Advanced Cost Management with Customized Configurations
Costs can be a complex topic and highly depend on your organization and business case. To adjust SAP LeanIX to your needs, you can consider further configuration options. For example, an adapted permission model can make cost data available or hide costs from specific user groups; and you can add more cost data fields and aggregate them with calculations to suite your cost definition.
**Note**
The total cost of ownership fields and calculations are not included in the predefined meta model. To use them, activate the Application Total Cost of Ownership extension to the meta model. For details, see [Application Total Cost of Ownership (TCO) Extension](https://help.sap.com/docs/leanix/ea/application-total-cost-of-ownership-extension?locale=en-US&state=PRODUCTION&version=CLOUD "Gain transparency into total cost of ownership with the extension that activates dedicated fields, calculations, as well as options for reports and KPIs for dashboards.").
### Example: Include Total Annual Cost in the Total Cost of Ownership
This custom calculation enhances the standard total cost of ownership for applications by incorporating total annual cost. By integrating infrastructure expenses directly into application costs, this calculation provides a more complete financial picture.
**Note**
Total annual cost will be kept separate in the fact sheet even though the total cost of ownership field now includes them.
![Application costs and total annual cost fields highlighted in a software management dashboard.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio4217292f01814ee0ab6f3eed37be22f1_HiRes.png)
Update the standard total cost of ownership for applications (TCO) calculation:

```
export function main() {
   const lxApplicationMaintenanceCosts = data.lxApplicationMaintenanceCosts || 0;
   const lxApplicationSupportCosts = data.lxApplicationSupportCosts || 0;
   const lxApplicationLicensingCosts = data.lxApplicationLicensingCosts || 0;
   let relTotalAnnualCost = 0;
   const rels = data.relApplicationToITComponent || [];
   for (const rel of rels) { if (rel.costTotalAnnual != null) { relTotalAnnualCost += rel.costTotalAnnual; } }
   return lxApplicationMaintenanceCosts +
       lxApplicationSupportCosts +
       lxApplicationLicensingCosts +
       relTotalAnnualCost;
}
```



### Example: Use Percentages to Allocate Application Cost to Business Capabilities and Organizations
By default, total cost of ownership calculations allocate costs based on usage patterns and support type. However, you can customize this allocation method to use percentage-based distribution instead.
This approach is particularly valuable when applications are used by different business capabilities or organizations, making it difficult to assign costs to specific ones. Percentage-based allocation provides greater flexibility and accuracy in these complex scenarios, giving you a clearer understanding of your true cost structure across shared resources.
Required steps:
  1. In the meta model configuration, add 2 new custom fields named Allocation Percentage in the following locations:
     * On the relation between application and business capability
     * On the relation between application and organizations
![Table showing organizations with allocation percentage values highlighted.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio74b37cff638c4b17983680dc50340c1e_HiRes.png)
  2. Add the following new calculations for total cost of ownership allocation of applications:
For the allocation to business capabilities

```
export function main() {
  const cost = data.fromFactSheet.lxApplicationTotalCostOfOwnership;
  const bcAllocation = data.allocationPercentage;
  if (cost != null && bcAllocation != null) {
    return cost * bcAllocation;
  }
}
```



For the allocation to organizations

```
export function main() {
  const cost = data.fromFactSheet.lxApplicationTotalCostOfOwnership;
  const orgAllocation = data.allocationPercentage;
  if (cost != null && orgAllocation != null) {
    return cost * orgAllocation;
  }
}
```





### Example: Use the Number of Users to Allocate Application Cost to Organizations
The calculation divides the application's TCO among organizations proportionally, with each organization's cost share directly corresponding to their number of users. Organizations with more users bear a larger portion of the costs, while those with fewer users pay proportionally less.
This approach provides a fair and transparent way to allocate shared application expenses, ensuring that costs align with actual organizational usage patterns.
Required steps:
  1. Fill in the user count the field Number of Users on the relation between application and organization.
  2. Update the calculation for total cost of ownership of application as provided:

```
export function main() {
    let sumOfUsers = 0;
    for (const orgRelation of data.fromFactSheet.relApplicationToOrganization) {
        if (orgRelation.numberOfUsers != null) {
            sumOfUsers += orgRelation.numberOfUsers;
        }
    }
    if(data.numberOfUsers != null && data.fromFactSheet.lxApplicationTotalCostOfOwnership != null && sumOfUsers > 0){
        return data.fromFactSheet.lxApplicationTotalCostOfOwnership * data.numberOfUsers / sumOfUsers;
    }
}
```



