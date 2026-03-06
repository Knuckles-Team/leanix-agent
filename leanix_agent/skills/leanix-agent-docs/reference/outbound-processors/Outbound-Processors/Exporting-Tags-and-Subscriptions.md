##  Exporting Tags and Subscriptions
For Tags, users can define a list of tag groups they are interested in using for export purposes. All tags in the listed tag groups will be part of the output scope and can be used in JUEL expressions "lx.tags" and "lx.subscriptions". As for relations, the tags and subscriptions are collected in a list. This list can be processed to output LDIF in multiple ways.
Iterating with an outer "forEach" allows to create separate data objects for every tag/subscription. Using the inner "forEach" in the output section allows to add the information to the data object written for the Fact Sheet.
Below is an example that shows multiple ways to convert the information to an output LDIF. It is recommended to potentially first try an output with the full tag/subscription object. This will allow you to see and review all of the contained fields. After which point, you could update the processor by limiting the output to the very specific content that needs to be part of the result LDIF.
Example outbound processor that exports relations, tags, and subscriptions into LDIF format:
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
   },
   {
    "keys": [
     "__any__"
    ],
    "facetKey": "lifecycle",
    "operator": "OR",
    "dateFilter": {
     "to": "2024-12-31",
     "from": "2018-01-01",
     "type": "RANGE",
     "maxDate": "2021-08-06",
     "minDate": "2010-11-07"
    }
   },
   {
    "keys": [],
    "facetKey": "relApplicationToITComponent",
    "operator": "OR"
   }
  ],
  "ids": []
 },
 "processors": [
  {
   "processorType": "outboundFactSheet",
   "processorName": "Export to LDIF",
   "processorDescription": "This is an example how to use the outboundFactSheet processor",
   "enabled": true,
   "fields": [
    "lifecycle",
    "location",
    "createdAt",
    "technicalSuitabilityDescription",
    "description",
    "name"
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
    ]
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
    },
    {
     "key": {
      "expr": "technicalSuitabilityDescription"
     },
     "values": [
      {
       "expr": "${lx.factsheet.technicalSuitabilityDescription}"
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
         "key": "objectForFindingRelevantFields",
         "value": "${integration.output.valueOfForEach}"
        }
       ]
      }
     ]
    },
    {
     "key": {
      "expr": "tags"
     },
     "mode": "list",
     "values": [
      {
       "forEach": {
        "elementOf": "${lx.tags}",
        "filter": "${true}"
       },
       "map": [
        {
         "key": "tagGroup",
         "value": "${integration.output.valueOfForEach.tagGroup.name}"
        },
        {
         "key": "tagName",
         "value": "${integration.output.valueOfForEach.name}"
        }
       ]
      }
     ]
    },
    {
     "key": {
      "expr": "subscriptions"
     },
     "mode": "list",
     "values": [
      {
       "forEach": {
        "elementOf": "${lx.subscriptions}",
        "filter": "${true}"
       },
       "map": [
        {
         "key": "subscriptionObjectForTestOnly",
         "value": "${integration.output.valueOfForEach}"
        },
        {
         "key": "subscriptionType",
         "value": "${integration.output.valueOfForEach.type}"
        },
        {
         "key": "subscriptionRoles",
         "value": "${integration.output.valueOfForEach.roles}"
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
Below is a sample of what the lx.subscriptions object looks like, which can be accessed in the list as defined above.
Example lx.subscriptions object:

```
"lx.subscriptions": [
 {
  "id": "76cf02fa-c358-4653-af09-e1d9729960fa",
  "type": "RESPONSIBLE",
  "user": {
   "id": "2d9b1cbb-158f-4679-b9b8-60136a52de3e",
   "email": "22345@leanix.net",
   "lastName": "User",
   "userName": "anonymized.user@leanix.net",
   "firstName": "Anonymized",
   "displayName": "Anonymized User"
  },
  "roles": [
   {
    "id": "1b3e71fe-781a-4fd9-988e-56ba42b33a51",
    "name": "Business Owner"
   }
  ],
  "createdAt": "2022-12-12T09:04:40.214367Z"
 },
 {
  "id": "94fbbaf1-8c75-4cf2-a6ac-98d92e277877",
  "type": "RESPONSIBLE",
  "user": {
   "id": "8b189683-7852-4ff7-9845-f1725e324670",
   "email": "abel.tuter@example.com",
   "lastName": "tuter",
   "userName": "Abel.tuter@example.com",
   "firstName": "abel",
   "displayName": "abel tuter"
  },
  "roles": [
   {
    "id": "60d53ae5-34f0-4f8c-8ca3-9aa7f674f41f",
    "name": "Application Owner Deputy",
    "comment": "Deputy Comment"
   }
  ],
  "createdAt": "2023-04-10T11:34:40.145262Z"
 }
]
```



**Note**
Outbound Data Processors need to have mandatory fields configured.
An outbound Fact Sheet processor will fail if the mandatory output fields "content.id" and "content.type" are not defined as they are mandatory part of any LDIF.
**Note**
The created file may contain more optional fields. The above displays a short version for understanding the mandatory structure. See detailed description above
