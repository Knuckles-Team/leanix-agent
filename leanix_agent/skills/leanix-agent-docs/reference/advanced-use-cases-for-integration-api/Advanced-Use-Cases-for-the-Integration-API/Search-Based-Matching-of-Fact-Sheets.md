##  Search Based Matching of Fact Sheets
When using the "search" based identification of the Fact Sheet that are supposed to be updated by the incoming data object, then the section may contain a section to limit the scope of searched Fact Sheets and an expression filtering the Fact Sheets that should be updated.
In case Integration API iterates over a search result, two variables can be used in all JUEL expressions: search.resultSize (indicating the total number of items we iterate over in the processor) and search.resultIndex (number of current item being iterated)
When configuring an inboundFactsheet processor, a key "search" is now allowed. the value of this key is an object as defined in the example below. One or more Fact Sheets may be identified by the search and be updated based on the same data object in the LDIF.
The search works in two steps:
  1. The "scope" defines a search against the pathfinder backend and limits the number of Fact Sheets to be matched. A valid scope can e.g. be created by using an outbound Integration API configuration and click on "set scope". Then the Scope can be copied from there.
  2. After reducing the scope of Fact Sheets potentially in scope as good as possible with pathfinder filtering options, an additional JUEL expression is being executed to further narrow down the scope (key: "filter"). This is the far more costly process but allows much more flexibility identifying the right Fact Sheets. Admins should always try to limit the scope in phase 1 as far as possible to avoid long processing times. In the JUEL expression all fields defined in the "read" section can be used for filtering (e.g. ${lx.factsheet.description.startsWith('Autoupdate: ')}


As the Outcome, all identified Fact Sheets will be processed as if they had been found by the processor one by one.
The "search" key can be used in conjunction with the "external" key. In this scenario, the Integration API first tries to find based on the external ID. If that fails, the search will be executed. If that fails as well, the integration API will try to create the Fact Sheet based on information in the "external" value. The last step can be avoided if creation is not allowed for the use case by adding an onRead filter and check for "lx.factsheet" not being null.
From a use case perspective, it allows to search for a Fact Sheet with a specific external id, if not existing then search for a Fact Sheet with e.g. a specific name and add the external id in case it is existing. OR create a new Fact Sheet in case a Fact Sheet with the name was not found.
The key "multipleMatchesAllowed" allows to define the API behaviour in case multiple Fact Sheets are matching the search criteria. Some use cases may only want to update if exactly one Fact Sheet was found (then the value will be set to "false"). By allowing multiple matches, bulk updates on multiple Fact Sheets are possible. Default if not existing is "true"
The following example processor will update all descriptions of Application Fact Sheets that have a tag "AsiaPacific" in the tag group "Region".
Search based on fact sheet identification:

```
{
 "processors": [
  {
   "processorType": "inboundFactSheet",
   "processorName": "Update all Cloud Apps",
   "processorDescription": "Updates all Apps with tag 'Cloud'",
   "type": "Application",
   "filter": {
    "exactType": "AppUpdate"
   },
   "identifier": {
    "search": {
     "scope": {
      "facetFilters": [
       {
        "facetKey": "FactSheetTypes",
        "operator": "OR",
        "keys": [
         "Application"
        ]
       },
       {
        "facetKey": "${integration.tags.getTagGroupId('Region')}",
        "operator": "OR",
        "keys": [
         "${integration.tags.getTagId('Region','AsiaPacific')}"
        ]
       }
      ],
      "ids": []
     },
     "filter": "${true}",
     "multipleMatchesAllowed": true
    }
   },
   "logLevel": "debug",
   "updates": [
    {
     "key": {
      "expr": "description"
     },
     "values": [
      {
       "expr": "External sync executed ${data.dateTime}"
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
Sample LDIF:

```
{
 "connectorType": "searchBasedScope",
 "connectorId": "searchBasedScope",
 "connectorVersion": "1.0.0",
 "lxVersion": "1.0.0",
 "description": "Updates external sync date",
 "processingDirection": "inbound",
 "processingMode": "partial",
 "customFields": {},
 "content": [
  {
   "type": "AppUpdate",
   "id": "apps",
   "data": {
    "dateTime": "06/08/2019"
   }
  }
 ]
}
```



Extending the example is easy to e.g. only match update the Fact Sheets where the description already starts with a specific text, indicating that an automatic update was allowed:
Extended example with filter option set:

```
{
 "processors": [
  {
   "processorType": "inboundFactSheet",
   "processorName": "Update all Cloud Apps",
   "processorDescription": "Updates all Apps with tag 'Cloud'",
   "type": "Application",
   "filter": {
    "exactType": "AppUpdate"
   },
   "identifier": {
    "search": {
     "scope": {
      "facetFilters": [
       {
        "facetKey": "FactSheetTypes",
        "operator": "OR",
        "keys": [
         "Application"
        ]
       },
       {
        "facetKey": "${integration.tags.getTagGroupId('Region')}",
        "operator": "OR",
        "keys": [
         "${integration.tags.getTagId('Region','AsiaPacific')}"
        ]
       }
      ],
      "ids": []
     },
     "filter": "${lx.factsheet.description.startsWith('External sync')}",
     "multipleMatchesAllowed": true
    }
   },
   "logLevel": "debug",
   "read": {
    "fields": [
     "description"
    ]
   },
   "updates": [
    {
     "key": {
      "expr": "description"
     },
     "values": [
      {
       "expr": "External sync executed ${data.dateTime}"
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
