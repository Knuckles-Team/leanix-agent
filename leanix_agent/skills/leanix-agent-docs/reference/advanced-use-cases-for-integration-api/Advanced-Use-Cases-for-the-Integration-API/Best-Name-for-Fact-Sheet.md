##  Best Name for Fact Sheet
There are situations where it is not easy to find the best potential name for a Fact Sheet based on incoming data. The best name may not be available as it is not unique. Another use case might be that the source may provide different candidates for a name where we want to select from best possible option to lower ranked options automatically based on information availability for each data object.
On the other hand we want to ensure that we do not change names of already created Fact Sheets all of a sudden just because a better name option became available during an update.
All the above use cases can be covered simply by providing a list of potential name candidates. Every candidate that results in a null (evaluated in the 'values' section) or is already taken by another Fact Sheet will be skipped. In case I want to keep a name once set and not changed after creation, admins configure to read current Fact Sheet content and use the existing name as a first option. This will automatically be skipped if the Fact Sheet is not yet existing.
### Example
Please see the example of a processor and a sample LDIF. You may test play around with matching against existing Fact Sheet names and remove/rename some of the keys from the source data and do test runs:
Best fact sheet name selection:
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
   "run": 0,
   "updates": [
    {
     "key": {
      "expr": "name"
     },
     "values": [
      {
       "expr": "${lx.factsheet.name}"
      },
      {
       "expr": "${data.app}"
      },
      {
       "expr": "${data.app2}"
      },
      {
       "expr": "${data.app3}"
      }
     ]
    }
   ],
   "read": {
    "fields": [
     "name"
    ]
   },
   "logLevel": "debug"
  }
 ]
}

```



Sample LDIF for best name suggestion:

```
{
 "connectorType": "ee",
 "connectorId": "Kub Dev-001",
 "connectorVersion": "1.2.0",
 "lxVersion": "1.0.0",
 "description": "Imports kubernetes data into LeanIX",
 "processingDirection": "inbound",
 "processingMode": "partial",
 "customFields": {},
 "content": [
  {
   "type": "Deployment",
   "id": "634c16bf-198c-1129-9d08-92630b573fbf",
   "data": {
    "app3": "veryLongAndUnhandyNameIDoNotWantToSeeIfPossible",
    "app2": "littleBitBetterNameButStillNotGood",
    "app": "Best Name"
   }
  }
 ]
}
```



