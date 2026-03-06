##  Write to LDIF
The processor allows Administrators to configure an inbound Integration API run to write a new LDIF file. The resulting LDIF will be available using the /results and the /resultsUrl endpoints same as with outbound Integration API runs.
With this functionality, inbound runs can be used in all combinations to read, process, update Pathfinder entities and even write a new LDIF in one step. Integrations that write to SAP LeanIX and read data from SAP LeanIX can be written and managed in one Integration API configuration executed with a single call.
The new processor can even be used to only export data or just transform an LDIF into another LDIF.
In a configuration, all defined processors will write to a single, globally defined LDIF. This allows to collect all kinds of data objects to the target LDIF from multiple processors including content from aggregations and other processing (e.g. variables).
The LDIF header definition needs to be set as a global key in the Integration API congifuration. All fields can be freely configured and will be evaluated to a String using JUEL. Exception is the "customFields" key. If defined, the value will be interpreted as an object and passed to the target LDIF. Please ensure the expression always results in a map object to not break the LDIF format.
Example writeToLdif processor:

```
{
  "processors": [
    {
      "processorType": "writeToLdif",
      "updates": [
        {
          "key": {
            "expr": "content.id"
          },
          "values": [
            {
              "expr": "${content.id}"
            }
          ]
        },
        {
          "key": {
            "expr": "content.type"
          },
          "values": [
            {
              "expr": "${content.type}"
            }
          ]
        },
        {
          "key": {
            "expr": "description"
          },
          "values": [
            {
              "expr": "Just a test. Could be any read content or JUEL calculation"
            }
          ]
        }
      ]
    }
  ],
  "targetLdif": {
    "dataConsumer": {
      "type": "leanixStorage"
    },
    "ldifKeys": [
      {
        "key": "connectorType",
        "value": "myNewLdif"
      },
      {
        "key": "connectorId",
        "value": "mycreatedId"
      },
      {
        "key": "customFields",
        "value": "${integration.toObject('{\"anyKey\":\"anyValue\"}')}"
      }
    ]
  }
}

```



A more advanced example shows how to read content from Pathfinder and write it to an LDIF using the processor. It requires an input LDIF with at lease one data object but content is not relevant. The data object is only used to trigger.
writeToLdif can write variables as well (run levels are supported and variables are available one run after creation). You may even define multiple writeToLdif processors. All content will be collected and written to one resulting LDIF.
Please ensure to adjust the search scope to your workspace and change the id to an existing one.
Advanced example of the writeToLdif processor:

```
{
  "processors": [
    {
      "processorType": "writeToLdif",
      "filter": {
        "advanced": "${integration.contentIndex==0}",
        "onRead": "${lx.factsheet.description!=''}"
      },
      "identifier": {
        "search": {
          "scope": {
            "ids": [
              "8de51ff7-6f13-47df-8af8-9132ada2e74d"
            ],
            "facetFilters": []
          },
          "filter": "${true}",
          "multipleMatchesAllowed": true
        }
      },
      "run": 0,
      "updates": [
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
              "expr": "${lx.factsheet.name}"
            }
          ]
        },
        {
          "key": {
            "expr": "description"
          },
          "values": [
            {
              "expr": "${lx.factsheet.description}"
            }
          ]
        }
      ],
      "logLevel": "warning",
      "read": {
        "fields": [
          "description"
        ]
      }
    }
  ],
  "targetLdif": {
    "dataConsumer": {
      "type": "leanixStorage"
    },
    "ldifKeys": [
      {
        "key": "connectorType",
        "value": "${header.connectorType}_export"
      },
      {
        "key": "connectorId",
        "value": "${header.connectorId}_export"
      },
      {
        "key": "description",
        "value": "Enriched imporeted LDIF for Applications"
      }
    ]
  }
}
```



Example input in LDIF format:

```
{
  "connectorType": "example",
  "connectorId": "example",
  "lxVersion": "1.0.0",
  "processingDirection": "inbound",
  "processingMode": "partial",
  "content": [
    {
      "type": "",
      "id": "",
      "data": {}
    }
  ]
}
```



