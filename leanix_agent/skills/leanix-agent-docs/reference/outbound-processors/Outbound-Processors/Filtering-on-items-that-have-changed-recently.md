##  Filtering on items that have changed recently
Integration API can produce 'delta' extracts, reflecting only recently updated Fact Sheets. This functionality is scoped to updates for entries in the audit history for specific Fact Sheets; It does not work for changes on documents or relations.
To filter, just add an additional key "updatedInDuration" to the filter section as shown below in the example:
Example processor that filters items by the change date:

```
{
 "scope": {
  "ids": [
   "28fe4aa2-6e46-41a1-a131-72afb3acf256"
  ],
  "facetFilters": []
 },
 "processors": [
  {
   "processorType": "outboundFactSheet",
   "processorName": "Export to LDIF",
   "processorDescription": "This is an example how to use the processor",
   "filter": {
    "updatedInDuration": "${header.customFields.age}"
   },
   "enabled": true,
   "fields": [
    "lifecycle",
    "location",
    "createdAt",
    "technicalSuitabilityDescription",
    "description"
   ],
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
     "externalId"
    ],
    "constrainingRelations": false
   },
   "tags": {
    "groups": [
     "Other tags",
     "Cloud Transformation"
    ]
   },
   "subscriptions": {
    "types": [
     "RESPONSIBLE"
    ]
   },
   "documents": {
    "filter": ".*"
   },
   "output": [
    {
     "key": {
      "expr": "content.id"
     },
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
     "values": [
      {
       "expr": "${lx.factsheet.type}"
      }
     ]
    },
    {
     "key": {
      "expr": "updatedAt"
     },
     "mode": "selectFirst",
     "values": [
      {
       "expr": "${lx.factsheet.updatedAt}"
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
To pass the value for updatedInDuration, just use the below LDIF when calling the outbound run. The example exports all Fact Sheets that changed in the last 3 days. Of course it is possible to add the P3D directly into the configuration if this does not need to be a parameter.
**Note**
Duration is encoded in ISO 8601 duration format.
Example LDIF that contains the duration for updates to be exported:

```
{
 "connectorType": "test",
 "connectorId": "test",
 "connectorVersion": "1.0.0",
 "processingDirection": "outbound",
 "processingMode": "partial",
 "customFields": {
  "age": "P3D"
 }
}
```



