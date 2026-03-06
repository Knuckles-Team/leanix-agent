##  Comments in Processors
Integration API allows to solve simple mapping tasks as well solving highly complex processing and aggregation use cases.
Documentation of more complex processing is key for maintenance work in case of changes. Integration API allows to add "description" keys in the locations listed in the below examples. The free text will be stored with the configuration but not be used for any processing. It is just used to document more complex expressions used.
Example inbound processor with descriptions:

```
{
  "identifier": {
    "description": "We iterate over all Fact Sheets of type 'Application'"
  },
  "variables": [
    {
      "description": "Write a variable for each found child to copy description to that later",
      "key": "collectedChild_${integration.variables.valueOfForEach.target.id}",
      "value": "${lx.factsheet.description}",
      "forEach": {
        "elementOf": "${lx.relations}"
      }
    },
    {
      "description": "Write all children to one variable to iterate over in later processor",
      "key": "collectedChildren",
      "value": "${integration.variables.valueOfForEach.target.id}",
      "forEach": {
        "elementOf": "${lx.relations}"
      }
    }
  ],
  "updates": [
    {
      "description": "Values to writing the field Business Fit are taken from a variable",
      "values": [
        {
          "description": "The source variable is names Businessfit_[currentFactSheetId]"
        }
      ]
    }
  ]
}
```



Example outbound processor with descriptions:

```
{
  "output": [
    {
      "description": "Example description",
      "key": {
        "expr": "content.id"
      },
      "values": [
        {
          "description": "Example description"
        }
      ]
    }
  ]
}
```



