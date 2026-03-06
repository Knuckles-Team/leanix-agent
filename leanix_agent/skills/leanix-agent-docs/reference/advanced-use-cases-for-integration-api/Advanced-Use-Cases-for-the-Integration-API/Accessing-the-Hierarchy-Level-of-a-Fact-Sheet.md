##  Accessing the "Hierarchy Level" of a Fact Sheet
It is easily possible to access the hierarchy level of a Fact Sheet just by reading the field "level" provided by the pathfinder backend. This information can be used to filter for certain hierarchy levels or do calculations.
In the below example, it is used to filter for Level 2 Project Fact Sheets for export.
This could of-course have been done by just applying the restriction to the pathfinder scope query. The below is just to show case and allow extending for more advanced filtering.
Export Only Processes In Hierarchy Level 2:

```
{
 "scope": {
  "facetFilters": [
   {
    "facetKey": "FactSheetTypes",
    "operator": "OR",
    "keys": [
     "Project"
    ]
   }
  ],
  "ids": []
 },
 "processors": [
  {
   "processorType": "outboundFactSheet",
   "processorName": "Export Projects L2",
   "processorDescription": "Exports only Level 2",
   "enabled": true,
   "filter": {
    "advanced": "${lx.factsheet.level==2}"
   },
   "fields": [
    "name",
    "level"
   ],
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
       "expr": "project}"
      }
     ]
    },
    {
     "key": {
      "expr": "name"
     },
     "values": [
      {
       "expr": "${lx.factsheet.name}"
      }
     ]
    },
    {
     "key": {
      "expr": "level"
     },
     "values": [
      {
       "expr": "${lx.factsheet.level}"
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
