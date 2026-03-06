##  Use "object" key to output all objects
The "object" key might be used instead of "map" or "expr" to retrieve a representation of any potential input object as a defined value. This allows to easily export all information without need to know about the details inside the object.
Use Object key Value:

```
{
 "scope": {
  "facetFilters": [
   {
    "facetKey": "FactSheetTypes",
    "operator": "OR",
    "keys": [
     "Application"
    ]
   }
  ],
  "ids": [
   "90a8296c-92fe-4009-a4cf-21db710719ec"
  ]
 },
 "processors": [
  {
   "processorType": "outboundFactSheet",
   "logLevel": "debug",
   "fields": [
    "lifecycle"
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
       "expr": "${lx.factsheet.type}"
      }
     ]
    },
    {
     "key": {
      "expr": "description"
     },
     "values": [
      {
       "object": "${lx.factsheet.lifecycle}"
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
