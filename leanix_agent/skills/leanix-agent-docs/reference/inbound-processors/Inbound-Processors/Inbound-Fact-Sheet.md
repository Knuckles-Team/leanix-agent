##  Inbound Fact Sheet
Example inboundFactSheet processor:

```
{
  "processors": [
    {
      "processorType": "inboundFactSheet",
      "processorName": "Create IT Components",
      "processorDescription": "One Processor for IT Components",
      "enabled": true,
      "type": "ITComponent",
      "identifier": {
        "external": {
          "id": {
            "expr": "${content.id.replaceAll('/','_')}"
          },
          "type": {
            "expr": "externalId"
          }
        }
      },
      "filter": {
        "exactType": "ITComponent"
      },
      "updates": [
        {
          "key": {
            "expr": "name"
          },
          "values": [
            {
              "expr": "${data.name}"
            }
          ]
        },
        {
          "key": {
            "expr": "cloudProvider"
          },
          "values": [
            {
              "expr": "${data.provider}"
            }
          ]
        },
        {
          "key": {
            "expr": "category"
          },
          "values": [
            {
              "expr": "${data.category}",
              "regexMatch": "(cloud_service)",
              "regexReplace": {
                "match": "^.*$",
                "replace": "cloudService"
              }
            },
            {
              "expr": "${data.category}",
              "regexMatch": "(sample_software)",
              "regexReplace": {
                "match": "^.*$",
                "replace": "software"
              }
            }
          ]
        }
      ],
      "vars": []
    }
  ]
}
```



