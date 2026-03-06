##  Step 2: Map Risk Scores to Risk Tiers
Map the total risk score to a user-friendly risk tier. Here's an example mapping:
Risk Score | Risk Tier
---|---
< 10 | Green
10–16 | Yellow
17–23 | Orange
> 23 | Red


Include these mappings in the processor configuration, as described in the following step.

```
{
  "key": {
    "expr": "RiskTier"
  },
  "values": [
    {
      "expr": "${ lx.factsheet.TotalRiskScore < 10 ? 'Green' : lx.factsheet.TotalRiskScore < 17 ? 'Yellow' : lx.factsheet.TotalRiskScore < 24 ? 'Orange' : lx.factsheet.TotalRiskScore > 23 ? 'Red' : null}"
    }
  ]
}
```



