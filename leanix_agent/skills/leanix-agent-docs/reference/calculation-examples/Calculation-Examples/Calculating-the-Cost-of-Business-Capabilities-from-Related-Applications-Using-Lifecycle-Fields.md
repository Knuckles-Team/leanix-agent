##  Calculating the Cost of Business Capabilities from Related Applications Using Lifecycle Fields
This calculation determines the total cost of business capabilities by iterating through related applications. It checks if each application is in the active lifecycle phase. If it is, its total cost of ownership (TCO) is added to the total cost.
**Sample Code**

```
export function main() {
    let cost = 0;
    for (const app of data.relBusinessCapabilityToApplication) {
        if (!app.factSheet.lifecycle) {
            return;
        }
        // check the current phase if active, then count in the cost for it
        if (app.factSheet.lifecycle.currentPhase === 'active') {
            cost += app.factSheet.lxApplicationTCO;
        }
    }
    return cost;
}
```



This calculation also determines the cost of business capabilities. It includes an additional check for application's active date. The function verifies if the active date is less than or equal to the current date. If it is, the function adds the application's TCO to the total cost.
**Sample Code**

```
export function main() {
    let cost = 0;
    for (const app of data.relBusinessCapabilityToApplication) {
        if (!app.factSheet.lifecycle || !app.factSheet.lifecycle.active) {
            return;
        }

        // check if app active, then count in the cost for it
        if (new Date(app.factSheet.lifecycle.active) <= new Date()) {
            cost += app.factSheet.lxApplicationTCO;
        }
    }
    return cost;
}
```



