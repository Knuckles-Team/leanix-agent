##  Use Relations to Create Separate Data Object
Last example shows how to use the relation (alternatively tag or subscription) information to create separate data object from it.
The example as well shows, how to filter specific relations from being written to the LDIF. In the example all relations with description "skipme" will not be exported. Please see the [Setting Filters](https://help.sap.com/docs/leanix/ea/outbound-processors?locale=en-US&state=PRODUCTION&version=CLOUD#loio275baac17a441014aeb793a21501b0b6__setting_filters) section for more information on filters.
Example outbound processor that uses relations to create a separate data object:

```
{
 "scope": {
  "facetFilters": [
   {
    "keys": [
     "Application"
    ],
    "facetKey": "FactSheetTypes",
    "operator": "OR"
   }
  ],
  "ids": []
 },
 "processors": [
  {
   "processorType": "outboundFactSheet",
   "processorName": "Relations relFromApp",
   "processorDescription": "Export all relations for Apps",
   "filter": {
    "advanced": "${integration.valueOfForEach.description!='skipme'}"
   },
   "enabled": true,
   "fields": [
    "description",
    "name"
   ],
   "relations": {
    "filter": [
     "relApplicationToBusinessCapability"
    ],
    "fields": [
     "description",
     "activeFrom",
     "activeUntil",
     "functionalSuitability"
    ],
    "targetFields": []
   },
   "forEach": "${lx.relations}",
   "output": [
    {
     "key": {
      "expr": "content.id"
     },
     "values": [
      {
       "expr": "0"
      }
     ]
    },
    {
     "key": {
      "expr": "content.type"
     },
     "values": [
      {
       "expr": "lxRelApplicationToBusinessCapability"
      }
     ]
    },
    {
     "key": {
      "expr": "lxId"
     },
     "values": [
      {
       "expr": "${lx.factsheet.id}"
      }
     ]
    },
    {
     "key": {
      "expr": "lxTargetId"
     },
     "values": [
      {
       "expr": "${integration.valueOfForEach.target.id}"
      }
     ]
    },
    {
     "key": {
      "expr": "lxFsName"
     },
     "values": [
      {
       "expr": "${lx.factsheet.name}"
      }
     ]
    }
   ]
  }
 ]
}
```



