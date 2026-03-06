##  Inbound Impact
The processor is used to write impacts to the SAP LeanIX backend.
A processor always writes a single impact. In case a list of input data is given where "forEach" can iterate over, multiple impacts can be written by a single processor. Different types of impacts should be split into different processors in order to keep a configuration readable as different impacts have different parameters.
The example below shows how to define Impacts. Please be aware that each type of impacts may require a different set of keys to be configured.
**Tip**
To find out about the different keys required for each Impact type, create the needed types of impacts in the UI, then export using an outbound processor or by using the "read" section in an inbound processor and either export to LDIF or write to a field like "description"
Example inboundImpact processor:

```
{
  "processors": [
    {
      "processorType": "inboundImpact",
      "updates": [
        {
          "key": {
            "expr": "groupName"
          },
          "values": [
            {
              "expr": "G1"
            }
          ]
        },
        {
          "key": {
            "expr": "description"
          },
          "values": [
            {
              "expr": "Group Description 2"
            }
          ]
        },
        {
          "key": {
            "expr": "impacts"
          },
          "values": [
            {
              "map": [
                {
                  "key": "type",
                  "value": "FACTSHEET_SET"
                },
                {
                  "key": "factSheetId",
                  "value": "28fe4aa2-6e46-41a1-a131-72afb3acf256"
                },
                {
                  "key": "fieldName",
                  "value": "functionalSuitabilityDescription"
                },
                {
                  "key": "fieldValue",
                  "value": "${data.value}"
                }
              ]
            }
          ]
        }
      ],
      "identifier": {
        "internal": "6d8acf0c-fa4e-40ed-9986-97da860f3414"
      },
      "logLevel": "warning"
    }
  ]
}
```



