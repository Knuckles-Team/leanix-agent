##  Write-back to Fact Sheet
inboundFactsheet processor, the inboundRelation and the writeToLdif processor allow to read information from the Fact Sheet (currently supported: fields, relations, subscriptions, tags, documents and metrics) and use the information when writing back to the Fact Sheet. In case you need to work with read information in other processors, please write results to a variable first. The below example shows two use case examples, where a cost field is increased by the incoming value and an update of the risk section will only be done if the description is not starting with a key word "manually".
The example as well contains information how to use this feature. In case you define the read section for the inboundRelation processor, the fields will be read for the Fact Sheet defined in the "from" section. You can still read the fields from the target Fact Sheet using the "relations/targetFields" as shown below.
For the example to work, the workspace needs to contain a Project Fact Sheet with external ID "12345". Or change the LDIF data to an external ID of a Project Fact Sheet existing in the workspace.
Write to fact sheet based on current content:

```
{
 "processors": [
  {
   "processorType": "inboundFactSheet",
   "processorName": "Apps from Deployments",
   "processorDescription": "Creates LeanIX Applications from Kubernetes Deployments",
   "type": "Project",
   "filter": {
    "exactType": "prj"
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
      "expr": "budgetOpEx"
     },
     "values": [
      {
       "expr": "${lx.factsheet.budgetOpEx+data.monthlyOpEx}"
      }
     ]
    },
    {
     "key": {
      "expr": "projectRisk"
     },
     "values": [
      {
       "expr": "${(lx.tags.toString().contains('\"name\":\"MANUAL_INPUT'))?null:data.risk}",
       "regexMatch": ".+"
      }
     ],
     "optional": true
    },
    {
     "key": {
      "expr": "projectRiskDescription"
     },
     "values": [
      {
       "expr": "${(lx.tags.toString().contains('\"name\":\"MANUAL_INPUT'))?null:data.riskDescription}",
       "regexMatch": ".+"
      }
     ],
     "optional": true
    },
    {
     "key": {
      "expr": "metrics"
     },
     "values": [
      {
       "expr": "${integration.toJson(lx.metrics.variableName.values)}"
      }
     ]
    }
   ],
   "logLevel": "debug",
   "read": {
    "fields": [
     "budgetOpEx"
    ],
    "tags": {
     "groups": [
      "Other tags"
     ]
    },
    "relations": {
     "filter": [
      "relToParent",
      "relApplicationToITComponent"
     ],
     "fields": [
      "description"
     ],
     "targetFields": [
      "displayName",
      "externalId",
      "location"
     ]
    },
    "subscriptions": {
     "types": [
      "RESPONSIBLE"
     ]
    },
    "metrics": [
     {
      "name": "variableName",
      "measurement": "money",
      "fieldName": "dollars_per_day",
      "aggregationFunction": "MEAN",
      "groupBy": "1h",
      "start": "2020-01-20T00:00:00Z",
      "duration": "P0DT24H30M",
      "rules": {
       "key": "factSheetId",
       "comparator": "=",
       "compareWith": "${lx.factsheet.id}"
      }
     }
    ],
    "impacts": {
     "readAll": true
    }
   }
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
  "connectorType": "showcaseUpdate",
  "connectorId": "showcaseUpdate",
  "connectorVersion": "1.0.0",
  "lxVersion": "1.0.0",
  "content": [
    {
      "type": "prj",
      "id": "12345",
      "data": {
        "monthlyOpEx": 50000,
        "risk": "lowProjectRisk",
        "riskDescription": "The risk is considered to be low."
      }
    }
  ]
}
```



Example to access fields on relations and on the target Fact sheet of a relation:

```
{
 "lx.relationsElement": {
  "id": "9316291b-361a-4050-ac79-bf9f96811fb1",
  "type": "relApplicationToITComponent",
  "target": {
   "id": "161abc0d-7bed-4440-b756-5c14a741e1ad",
   "name": "Application Development",
   "type": "ITComponent"
  },
  "activeFrom": "2021-01-18",
  "description": ""
 }
}
```



**Note**
Access to fields on relations and relation target fields.
By defining the fields on the relations and on the target Fact Sheets of a relation, admins can use the values in JUEL expressions in the output section. The found relations need to be iterated using "forEach". Each element will then contain the standard information about e.g. name and type of a relation plus the requested fields. They can be accesses following the structure shown in the below example
