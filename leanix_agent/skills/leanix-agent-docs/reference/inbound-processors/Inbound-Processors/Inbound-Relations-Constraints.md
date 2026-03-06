##  Inbound Relations Constraints
The relation processor allows to set constraining relations as well. In order to do so, a target key "constrainingRelations" needs to be defined (in the output section similar to the example target key "description in the example above"). All values of the resulting values list will be written as constraints. Existing ones will be removed. Alternatively the key "addConstrainingRelations" may be used to add constraints to existing ones.
Example configuration to read information of constraining relations from an LDIF input:

```
{
  "key": {
    "expr": "constrainingRelations"
  },
  "values": [
    {
      "forEach": {
        "elementOf": "${integration.valueOfForEach.rels.constrainingRelations.relations}"
      },
      "map": [
        {
          "key": "type",
          "value": "${integration.output.valueOfForEach.type}"
        },
        {
          "key": "targetExternalIdType",
          "value": "externalId"
        },
        {
          "key": "targetExternalIdValue",
          "value": "${integration.output.valueOfForEach.target.externalId}"
        }
      ]
    }
  ]
}
```



Example configuration to generate an LDIF output with information about constraining relations:

```
{
  "scope": {
    "ids": [
      "7750c7ba-5d24-4849-a1b4-564bc6c874a0"
    ],
    "facetFilters": [
      {
        "keys": [
          "Application"
        ],
        "facetKey": "FactSheetTypes",
        "operator": "OR"
      }
    ]
  },
  "processors": [
    {
      "processorType": "outboundFactSheet",
      "processorName": "Export to LDIF",
      "processorDescription": "This is an example how to use the outboundFactSheet processor",
      "enabled": true,
      "fields": [
        "lifecycle",
        "name",
        "location",
        "createdAt",
        "technicalSuitabilityDescription",
        "description"
      ],
      "relations": {
        "filter": [
          "relApplicationToProcess"
        ],
        "fields": [
          "description"
        ],
        "targetFields": [
          "displayName",
          "externalId"
        ],
        "constrainingRelations": true
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
            "expr": "Name"
          },
          "values": [
            {
              "expr": "${lx.factsheet.name}"
            }
          ],
          "optional": true
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
