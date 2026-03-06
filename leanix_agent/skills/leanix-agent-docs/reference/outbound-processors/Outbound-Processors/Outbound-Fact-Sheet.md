##  Outbound Fact Sheet
This processor is capable writing Fact Sheet, relation, tag, document, subscription and metrics information from SAP LeanIX to LDIF.
In order to write LDIF, the scope of total Fact Sheets to read data from needs to be defined by a search. The Integration API UI allows to set the scope and add this scope to the configuration of an outbound configuration. Users then only have to regularly request the LDIF and will receive one LDIF with most current information matching the defined query. The exported data is configurable using same mechanisms as we do the inbound way.
Scopes can be defined globally for all processors or inside each processor. In case both was defined, the scope in the processor takes priority over the global used as a fallback only if the processor has not defined any.
Basic structure of the outboundFactSheet processor.
Example outboundFactSheet processor:

```
{
 "scope": {
  "facetFilters": [],
  "ids": []
 },
 "processors": [
  {
   "processorType": "outboundFactSheet",
   "processorName": "Export to LDIF",
   "processorDescription": "This is an example how to use the processor",
   "enabled": true,
   "fields": [
    "lifecycle",
    "location",
    "createdAt",
    "description",
    "technicalSuitabilityDescription"
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
      "expr": "Description"
     },
     "values": [
      {
       "expr": "${lx.factsheet.description}"
      }
     ],
     "optional": true
    },
    {
     "key": {
      "expr": "creationDateTime"
     },
     "mode": "selectFirst",
     "values": [
      {
       "expr": "${lx.factsheet.createdAt}"
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
