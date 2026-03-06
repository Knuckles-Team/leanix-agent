##  Deletion for multiple external sources
Advanced deletion is as well available for Fact Sheets but works slightly different. Advanced Fact Sheet deletion supports multiple external sources for one SAP LeanIX Fact Sheet. Deletion would not happen unless the last referenced source of a Fact Sheet does not longer contain information about the Fact Sheet.
This functionality is helpful in cases where a Fact Sheet might be created and again removed by potentially more than one foreign system providing separate LDIF to update the SAP LeanIX side.
In cases, where the Fact Sheet was no longer referenced by one of the sources, a deletion would not be a valid solution unless all sources no longer contain the information.
For such cases, the advanced deletion allows every sources to set a unique id as a marker. If this marker, called "owner", was found in the configuration, the Integration API first checks the field with all markers and only removes (archives) the Face Sheet if the list of markers found in the field is empty. The field to store the markers needs to be created in the data model as a standard String type. Integration API will read the content ant treat as a JSON list.
The below example shows example usage including the way to add the marker for a specific owner as part of the output section.
Please note that the example uses the "alias" field to store the owner information. This is for testing and demonstration as it allows easy inspection and required no data model work. For production usage, this needs to be written to a new created field not visible in the UI.
Advanced fact sheet deletion:

```
{
 "deletionScope": {
  "factSheets": [
   {
    "scope": {
     "ids": [],
     "facetFilters": [
      {
       "keys": [
        "Process"
       ],
       "facetKey": "FactSheetTypes",
       "operator": "OR"
      }
     ]
    },
    "owner": {
     "fieldName": "alias",
     "ownerId": "myOwner"
    }
   }
  ]
 },
 "processors": [
  {
   "processorType": "inboundFactSheet",
   "processorName": "Apps from Deployments",
   "processorDescription": "Creates LeanIX Applications from Kubernetes Deployments",
   "type": "Process",
   "identifier": {
    "external": {
     "id": {
      "expr": "fullSyncOwnerTest ${integration.valueOfForEach}"
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
       "expr": "Full Sync Owner Test ${integration.valueOfForEach}"
      }
     ]
    },
    {
     "key": {
      "expr": "alias"
     },
     "values": [
      {
       "expr": "${helper:addIfNotExisting(lx.factsheet.alias, 'myOwner')}"
      }
     ]
    }
   ],
   "enabled": false,
   "forEach": "${data.tags}",
   "logLevel": "debug",
   "read": {
    "fields": [
     "alias"
    ]
   }
  }
 ]
}
```



