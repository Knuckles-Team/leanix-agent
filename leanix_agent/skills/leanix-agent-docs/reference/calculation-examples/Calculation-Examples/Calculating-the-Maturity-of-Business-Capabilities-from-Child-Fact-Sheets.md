##  Calculating the Maturity of Business Capabilities from Child Fact Sheets
This calculation determines the maturity of a parent business capability by identifying the lowest maturity level among its child fact sheets.
**Sample Code**

```
export function main() {
    const scoring = {
        adhoc: 1,
        repeatable: 2,
        defined: 3,
        managed: 4,
        optimized: 5,
    };
    let maturityScore = 6;

    for (const child of data.relToChild) {
        if (child.factSheet.currentMaturity != null) {
            if (scoring[child.factSheet.currentMaturity] < maturityScore) {
                maturityScore = scoring[child.factSheet.currentMaturity];
            }
        }
    }

    switch (maturityScore) {
        case 1:
            return "adhoc";
        case 2:
            return "repeatable";
        case 3:
            return "defined";
        case 4:
            return "managed";
        case 5:
            return "optimized";
    }
}
```



