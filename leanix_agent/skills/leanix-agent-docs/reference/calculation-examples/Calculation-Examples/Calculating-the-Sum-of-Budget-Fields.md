##  Calculating the Sum of Budget Fields
This calculation determines the total budget for initiative fact sheets by summing the values of CapEx (Budget) and OpEx (Budget). The function first checks if both budgetCapEx and budgetOpEx values are defined. If both values are present, it computes their sum and returns the total budget (totalBudget). If either value is missing, the function returns null, and the target field is set to empty.
**Sample Code**

```
export function main() {
    if (data.budgetCapEx == null || data.budgetOpEx == null) {
        return null;
    }

    const totalBudget = data.budgetCapEx + data.budgetOpEx;
    return totalBudget;
}
```



