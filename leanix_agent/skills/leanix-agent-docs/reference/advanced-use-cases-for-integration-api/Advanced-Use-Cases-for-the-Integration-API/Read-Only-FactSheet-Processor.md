##  Read-Only FactSheet Processor
In case you want to collect information from the resulting FactSheets into variables, you can enable the "readonly" mode on the inboundFactsheet processor. In the example below, all entries of the "releases" field of each application are collected into a variable releases. Results could then be used in a next run.
Using the "filter": "${myExpression}", the set of Fact Sheet values collected can be even more narrowed down according to the use case. This feature comes handy to save processing time as the processor does not need to prepare any write operation.
Example how to set the "readonly" mode on an inboundFactSheet processor:

```
{
 "processorType": "inboundFactSheet",
 "processorName": "Process variables with Search Scope",
 "processorDescription": "Collect deploymentMaturity ",
 "type": "Application",
 "filter": {
  "exactType": "Deployment"
 },
 "identifier": {
  "search": {
   "scope": {
    "ids": [],
    "facetFilters": [
     {
      "keys": [
       "Application"
      ],
      "facetKey": "FactSheetTypes",
      "operator": "OR"
     }
    ]
   }
  }
 },
 "run": 0,
 "enabled": true,
 "variables": [
  {
   "key": "releases",
   "value": "${lx.release}"
  }
 ],
 "logLevel": "debug",
 "readOnly": true
}
```



