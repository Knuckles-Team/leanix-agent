##  Calculating with single-select fields
This processor enables calculations with single-select fields
Example:

```
{
 "connectorId": "id-92476445-10b3-40f7-9386-6f13c61e4b89",
 "connectorType": "ee",
 "connectorVersion": "1.2.0",
 "processingDirection": "inbound",
 "processingMode": "partial",
 "processors": [
  {
   "enabled": true,
   "filter": {
    "type": "DataObject"
   },
   "identifier": {
    "internal": "${content.id}"
   },
   "logLevel": "debug",
   "processorDescription": "Creates LeanIX Applications from Kubernetes Deployments",
   "processorName": "Apps from Deployments",
   "processorType": "inboundFactSheet",
   "read": {
    "fields": [
     "businessValue",
     "projectRisk",
     "dataClassification"
    ],
    "noNullForOrdinal": true
   },
   "run": 0,
   "type": "DataObject",
   "updates": [
    {
     "key": {
      "expr": "description"
     },
     "values": [
      {
       "expr": "No null - ${lx.toOrdinal('dataClassification')}"
      }
     ]
    }
   ],
   "variables": [
    {
     "key": "deploymentMaturity",
     "value": "${data.maturity}"
    }
   ]
  }
 ]
}
```



