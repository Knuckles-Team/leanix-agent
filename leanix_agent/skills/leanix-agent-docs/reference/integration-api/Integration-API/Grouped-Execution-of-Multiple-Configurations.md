##  Grouped Execution of Multiple Configurations
A new key "executionGroups" added to the main section now allows Integration API to execute multiple Integration API configurations as if they were one. This is advanced functionality, not available in the UI but only when using the REST API. For details, navigate to the OpenAPI Explorer.
Example processor with grouped execution:

```
{
  "processors": [
    {
      "processorType": "inboundTag",
      "processorName": "Set TIME tags",
      "processorDescription": "Sets the TIME tags based on existing Fact Sheet values",
      "filter": {
        "advanced": "${integration.contentIndex==0}"
      },
      "identifier": {
        "search": {
          "scope": {
            "ids": [],
            "facetFilters": [
              {
                "keys": [
                  "Application"
                ],
                "facetKey": "FactSheetTypes",
                "operator": "OR"
              }
            ]
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
              "expr": "${((lx.factsheet.functionalSuitability=='unreasonable' || lx.factsheet.functionalSuitability=='insufficient') && (lx.factsheet.technicalSuitability=='inappropriate' || lx.factsheet.technicalSuitability=='unreasonable'))?'Eliminate':null}"
            },
            {
              "expr": "${((lx.factsheet.functionalSuitability=='appropriate' || lx.factsheet.functionalSuitability=='perfect') && (lx.factsheet.technicalSuitability=='inappropriate' || lx.factsheet.technicalSuitability=='unreasonable'))?'Migrate':null}"
            },
            {
              "expr": "${((lx.factsheet.functionalSuitability=='unreasonable' || lx.factsheet.functionalSuitability=='insufficient') && (lx.factsheet.technicalSuitability=='adequate' || lx.factsheet.technicalSuitability=='fullyAppropriate'))?'Tolerate':null}"
            },
            {
              "expr": "${((lx.factsheet.functionalSuitability=='appropriate' || lx.factsheet.functionalSuitability=='perfect') && (lx.factsheet.technicalSuitability=='adequate' || lx.factsheet.technicalSuitability=='fullyAppropriate'))?'Invest':null}"
            },
            {
              "expr": "No Data"
            }
          ]
        },
        {
          "key": {
            "expr": "group.name"
          },
          "values": [
            {
              "expr": "Time Model"
            }
          ]
        }
      ],
      "logLevel": "warning",
      "read": {
        "fields": [
          "technicalSuitability",
          "name",
          "functionalSuitability"
        ]
      }
    }
  ],
  "executionGroups": [
    "customGroupA",
    "anotherGroup",
    "myGroup"
  ]
}
```



Calling /synchronizationRuns/createSynchronizationRunWithExecutionGroup with parameter customGroupA will run all configurations that contain customGroupA in the list of executionGroups defined.
**Caution**
Advanced functionality: use with careful management of configurations.
The system will merge the configurations and use all processors from all configurations. There will be no ordering applied. Processors from different configurations with same run levels will run in parallel.
Conflicting settings like mixing inbound and outbound configurations will result in an error. Other special logic like settings for e.g. a data consumer will be taken from any configuration. If multiple ones are found, the run will be executed with the last found configuration.
In order to detect the "last found configuration", Integration API configurations with a matching tag will be sorted alphabetically and merged one by one. Sorting happens by type, then id, then version.
