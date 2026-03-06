##  Exporting All Relations and Fields within Relations
In the example below all of the relations that exist in a workspace have been associated to the processor. Along with all of the attributes available within the relations, such as the "Active From" and "Active Until" fields and "Total Annual Cost". Any custom relations and or attributes can be added to the appropriate object within the LDIF.
Example processor configuration with all relations and fields within relations:

```
{
 "processors": [
  {
   "processorType": "outboundFactSheet",
   "processorName": "Export to LDIF",
   "processorDescription": "This is an example how to use the outboundFactSheet processor",
   "enabled": true,
   "fields": [
    "displayName",
    "externalId"
   ],
   "relations": {
    "filter": [
     "relToParent",
     "relToRequires",
     "relToSuccessor",
     "relApplicationToUserGroup",
     "relApplicationToDataObject",
     "relApplicationToITComponent",
     "relApplicationToProject",
     "relProviderApplicationToInterface",
     "relConsumerApplicationToInterface",
     "relApplicationToProcess",
     "relApplicationToBusinessCapability",
     "relITComponentToTechnologyStack",
     "relITComponentToUserGroup",
     "relITComponentToProvider",
     "relInterfaceToDataObject",
     "relInterfaceToITComponent",
     "relProcessToBusinessCapability",
     "relProjectToBusinessCapability",
     "relProjectToITComponent",
     "relProjectToProcess",
     "relProjectToUserGroup",
     "relProjectToProvider"
    ],
    "fields": [
     "activeFrom",
     "activeUntil",
     "description",
     "functionalSuitability",
     "numberOfUsers",
     "usageType",
     "usage",
     "costTotalAnnual",
     "technicalSuitability",
     "serviceLevel",
     "supportType",
     "resourceClassification",
     "orderNo",
     "orderedCapex",
     "orderedOpex"
    ],
    "targetFields": [
     "displayName",
     "externalId",
     "category"
    ]
   },
   "output": [
    {
     "key": {
      "expr": "content.id"
     },
     "mode": "selectFirst",
     "values": [
      {
       "expr": "${lx.factsheet.id}"
      }
     ]
    },
    {
     "key": {
      "expr": "content.type"
     },
     "mode": "selectFirst",
     "values": [
      {
       "expr": "${lx.factsheet.type}"
      }
     ]
    },
    {
     "key": {
      "expr": "displayName"
     },
     "mode": "selectFirst",
     "values": [
      {
       "expr": "${lx.factsheet.displayName}"
      }
     ]
    },
    {
     "key": {
      "expr": "externalId"
     },
     "mode": "selectFirst",
     "values": [
      {
       "expr": "${lx.factsheet.externalId}"
      }
     ]
    },
    {
     "key": {
      "expr": "relations"
     },
     "mode": "list",
     "values": [
      {
       "forEach": {
        "elementOf": "${lx.relations}",
        "filter": "${true}"
       },
       "map": [
        {
         "key": "relationName",
         "value": "${integration.output.valueOfForEach.type}"
        },
        {
         "key": "object",
         "value": "${integration.output.valueOfForEach}"
        }
       ]
      }
     ]
    }
   ]
  }
 ],
 "scope": {
  "facetFilters": [],
  "ids": []
 }
}
```



