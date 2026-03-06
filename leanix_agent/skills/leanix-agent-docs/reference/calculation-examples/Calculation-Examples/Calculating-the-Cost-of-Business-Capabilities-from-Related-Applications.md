##  Calculating the Cost of Business Capabilities from Related Applications
This calculation determines the cost of business capability fact sheets by summing up the total cost of ownership (TCO) of all related applications. For each related application, if the TCO (lixApplicationTCO) is not null, its value is added to the cumulative cost. The function then returns the final total cost.
**Sample Code**

```
export function main() {
    let cost = 0;
    for (const app of data.relBusinessCapabilityToApplication) {
        if (app.factSheet.lixApplicationTCO != null) {
            cost += app.factSheet.lixApplicationTCO;
        }
    }
    return cost;
}
```



