##  Calculating a Maturity Gap
This calculation determines and categorizes a maturity gap by comparing the target maturity level with the current maturity level of a fact sheet. The main function first defines a scoring object that maps maturity levels (ranging from adhoc to optimized) to numerical scores (from 1 to 5). It then initializes a variable maturityGapScore to 0.
If both the targetMaturity and currentMaturity fields contain values, the function calculates the maturityGapScore by subtracting the score of the current maturity level from the score of the target maturity level. If either field is empty, the function returns null, and the target field is set to empty.
Once the maturityGapScore is calculated, the function categorizes it into different levels based on its value: from none to veryHigh. This categorization helps you understand the extent of the gap between the current and target maturity levels.
**Sample Code**

```
export function main() {
    if (data.targetMaturity == null || data.currentMaturity == null) {
        return null;
    }

    const scoring = {
    optimized: 5,
    managed: 4,
    defined: 3,
    repeatable: 2,
    adhoc: 1,
    };
    const maturityGapScore = scoring[data.targetMaturity] - scoring[data.currentMaturity];

    if (maturityGapScore <= 0) {
        return 'none'
    };
    if (maturityGapScore === 1) {
        return 'low'
    };
    if (maturityGapScore === 2) {
        return 'medium'
    }
    if (maturityGapScore === 3) {
        return 'high'
    }
    if (maturityGapScore === 4) {
        return 'veryHigh'
    }
}
```



