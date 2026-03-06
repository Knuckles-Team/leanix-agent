##  Dynamic Variable Handling
Example for dynamic variables:

```
${variables[integration.valueOfForEach.concat('_cost')].sum()}
(which is same as: variables['12345_cost'].sum() in case valueOfForEach is "12345")
```



