##  Write LDIF using Modes, Map and ForEach
Produced LDIF may not only contain simple key-value pairs in the data section but lists and maps as well. The below illustrated how to configure a data processor to write these data types.
Mode | Details
---|---
list | Collects all entries and writes the result as a list.
selectFirst | Is the default setting, it selecting the first value that is not empty and uses it to write to the target key.


### LDIF from Processor Set to Mode: List
In this case, the mode was switched to "list". The default ("selectFirst") would pick the first value that is not empty and use it to write to the target key. Mode list collects all entries and writes the result as a list.
outboundFactSheet processor configuration writing values to list:
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
      "expr": "lifecycleTimes"
     },
     "mode": "list",
     "values": [
      {
       "expr": "endOfLife:${lx.factsheet.lifecycle.endOfLife}",
       "regexMatch": ".*:.+$"
      },
      {
       "expr": "active:${lx.factsheet.lifecycle.active}",
       "regexMatch": ".*:.+$"
      },
      {
       "expr": "phaseOut:${lx.factsheet.lifecycle.phaseOut}",
       "regexMatch": ".*:.+$"
      },
      {
       "expr": "phaseIn:${lx.factsheet.lifecycle.phaseIn}",
       "regexMatch": ".*:.+$"
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
LDIF result with list values:

```
{
 "connectorType": "lxExport",
 "connectorId": "007",
 "connectorVersion": "1.0.0",
 "lxVersion": "1.0.0",
 "content": [
  {
   "type": "Application",
   "id": "28fe4aa2-6e46-41a1-a131-72afb3acf256",
   "data": {
    "lifecycleTimes": [
     "endOfLife:2021-08-06",
     "active:2018-08-06",
     "phaseOut:2021-05-06",
     "phaseIn:2018-05-06"
    ]
   }
  },
  {
   "type": "Application",
   "id": "001d3e51-a3be-4d5b-90f7-5b7a9e0b9458",
   "data": {
    "lifecycleTimes": [
     "active:2018-08-06",
     "phaseIn:2018-05-06"
    ]
   }
  }
 ]
}

```



**Caution**
Empty values are not written to the LDIF.
Please note that the list in the result LDIF does not always contain all elements but only the ones that are populated. This is done by additional configuration of a "regexMatch" key eliminating all values with no content. By removing this, the second data object would contain all four elements including the empty ones with values like "phaseOut:"
### LDIF from Processor Writing Relations: Map
The desired LDIF output and sample outbound processor are:
Sample outbound processor configuration to write relations:
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
   "processorDescription": "This is an example how to use the outboundFactSheet processor",
   "enabled": true,
   "fields": [],
   "relations": {
    "filter": [
     "relApplicationToITComponent"
    ],
    "fields": [
     "description"
    ],
    "targetFields": [
     "displayName",
     "externalId"
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
 ]
}
```



LDIF result containing relations:

```
{
 "connectorType": "lxExport",
 "connectorId": "007",
 "connectorVersion": "1.0.0",
 "lxVersion": "1.0.0",
 "content": [
  {
   "type": "Application",
   "id": "28fe4aa2-6e46-41a1-a131-72afb3acf256",
   "data": {
    "relations": [
     {
      "object": {
       "id": "5da3529f-2d40-4f00-9a22-ab8ddb4fc216",
       "type": "relApplicationToITComponent",
       "target": {
        "id": "20be4187-c384-4557-a6eb-c7a3d1e5eb40",
        "type": "ITComponent",
        "displayName": "Visual Studio 2011"
       },
       "description": ""
      },
      "relationName": "relApplicationToITComponent"
     },
     {
      "object": {
       "id": "51663856-ca7e-4a53-8412-14e6811df0ab",
       "type": "relApplicationToITComponent",
       "target": {
        "id": "5719d96b-4c45-497a-b006-c77e0d8e767b",
        "type": "ITComponent",
        "displayName": "meshlab IT Application Hosting"
       },
       "description": ""
      },
      "relationName": "relApplicationToITComponent"
     }
    ]
   }
  },
  {
   "type": "Application",
   "id": "001d3e51-a3be-4d5b-90f7-5b7a9e0b9458",
   "data": {
    "relations": [
     {
      "object": {
       "id": "509511e4-b5ff-43b1-b523-1ae5eb0522e0",
       "type": "relApplicationToITComponent",
       "target": {
        "id": "1d05f6ca-2d81-4998-8e6a-be70a0c33378",
        "type": "ITComponent",
        "displayName": "Test Cisco Router 3925"
       },
       "description": ""
      },
      "relationName": "relApplicationToITComponent"
     }
    ]
   }
  }
 ]
}
```



In this case, we again use the output mode "list" to generate a list and not only select the first valid result (We expect potentially multiple relations). Output of maps will work with mode "selectFirst" as well and export a single map as a value.
In the above example we use two new concepts:
### Definitions: map & forEach
Data Type | Details
---|---
map | Here we define the set of key names and value names we want to see in the output. Both are evaluated dynamically and can contain JUEL expressions referencing available data like Fact Sheet data.
forEach | *Following the same pattern we see for the forEach in inbound processors, we iterate over a given list variable. In the example the list of found relations. For each relation entry we expect to see one map with the configured keys and values.


**Note**
Expression-based filtering for Outbound Data Processors.
The forEach as well provides an expression based filtering to e.g. only output specific relations (${integration.output.valueOfForEach.type=='relApplicationToITComponent'} in case multiple different relations have been requested in the relations section. More useful filtering may be done on target id or specific fields of a Fact Sheet or relation.
To learn more about forEach and other advanced functionality please see [Advanced Use Cases for the Integration API](https://help.sap.com/docs/leanix/ea/advanced-use-cases-for-integration-api?locale=en-US&state=PRODUCTION&version=CLOUD "Explore advanced scenarios and examples for the Integration API.").
