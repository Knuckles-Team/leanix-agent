##  Example: forEach to update dynamic fields
Example how to use forEach to update a dynamic set of fact sheet fields:

```
{
 "processors": [
  {
   "processorType": "inboundFactSheet",
   "processorName": "Apps from Deployments",
   "processorDescription": "Creates LeanIX Applications from Kubernetes Deployments",
   "type": "Application",
   "filter": {
    "exactType": "Deployment"
   },
   "logLevel": "debug",
   "identifier": {
    "external": {
     "id": {
      "expr": "${content.id}"
     },
     "type": {
      "expr": "externalId"
     }
    }
   },
   "updates": [
    {
     "key": {
      "expr": "${integration.updates.keyOfForEach}"
     },
     "values": [
      {
       "expr": "${integration.updates.valueOfForEach}"
      }
     ],
     "forEach": {
      "elementOf": "${data}",
      "filter": "${integration.updates.valueOfForEach!='toBeFiltered'}"
     }
    }
   ]
  }
 ]
}
```



Sample LDIF:

```
{
 "connectorType": "Kubernetes",
 "connectorId": "Kub Dev-001",
 "connectorVersion": "1.2.0",
 "lxVersion": "1.0.0",
 "description": "Imports Kubernetes data into LeanIX",
 "processingDirection": "inbound",
 "processingMode": "partial",
 "customFields": {},
 "content": [
  {
   "type": "Deployment",
   "id": "634c16bf-198c-1129-9d08-92630b573fbf",
   "data": {
    "name": "HR Service",
    "version": "toBeFiltered",
    "description": "test description"
   }
  }
 ]
}
```



