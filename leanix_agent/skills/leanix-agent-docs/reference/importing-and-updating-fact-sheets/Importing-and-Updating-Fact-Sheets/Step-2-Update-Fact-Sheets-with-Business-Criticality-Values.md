##  Step 2: Update Fact Sheets with Business Criticality Values
In this step, update the imported fact sheets with business criticality values. The names and descriptions remain unchanged.
Attribute Key | Type | Description
---|---|---
businessCriticality |  SINGLE_SELECT | Indicates the importance of an application to the functioning and success of a business. Possible values: missionCritical (Mission critical), businessCritical (Business critical), businessOperational (Business operational), or administrativeService (Administrative service).


Consider a scenario where business criticality values differ between the external customer's system and SAP LeanIX. To address this, create a mapping of business criticality values and provide these mappings in the processor configuration. This setup lets you import business criticality values from your external system by aligning them with SAP LeanIX values.
External Value | SAP LeanIX Value
---|---
1-Critical |  missionCritical
2-High |  businessCritical
3-Low |  businessOperational
0-NonCritical |  administrativeService


In the connector you created in the previous step, update the processor configurations and input data. Then, run the connector. This updates two application fact sheets you imported earlier. Business criticality values are mapped from the external system to SAP LeanIX.
### Processor Configuration
Example processor configuration:

```
{
  "processors": [
    {
      "processorType": "inboundFactSheet",
      "processorName": "Create applications",
      "processorDescription": "Creates application fact sheets",
      "type": "Application",
      "filter": {
        "type": "Application"
      },
      "identifier": {
        "external": {
          "id": {
            "expr": "${content.id}"
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
              "expr": "${data.name}"
            }
          ]
        },
        {
          "key": {
            "expr": "description"
          },
          "values": [
            {
              "expr": "${data.description}"
            }
          ]
        },
        {
          "key": {
            "expr": "businessCriticality"
          },
          "values": [
            {
              "expr": "${data.businessCriticality}",
              "regexMatch": "1-Critical",
              "regexReplace": {
                "match": "^.*$",
                "replace": "missionCritical"
              }
            },
            {
              "expr": "${data.businessCriticality}",
              "regexMatch": "2-High",
              "regexReplace": {
                "match": "^.*$",
                "replace": "businessCritical"
              }
            },
            {
              "expr": "${data.businessCriticality}",
              "regexMatch": "3-Low",
              "regexReplace": {
                "match": "^.*$",
                "replace": "businessOperational"
              }
            },
            {
              "expr": "${data.businessCriticality}",
              "regexMatch": "0-NonCritical",
              "regexReplace": {
                "match": "^.*$",
                "replace": "administrativeService"
              }
            }
          ]
        }
      ],
      "enabled": true,
      "variables": [],
      "logLevel": "warning"
    }
  ]
}
```



### Input Data
Example input data:

```
{
  "connectorType": "Basic-ImportApplications",
  "connectorId": "ImportApplications",
  "connectorVersion": "1.0.0",
  "lxVersion": "1.0.0",
  "description": "",
  "processingDirection": "inbound",
  "processingMode": "full",
  "customFields": {},
  "content": [
    {
      "type": "Application",
      "id": "APP-0001",
      "data": {
        "name": "AC Management",
        "description": "AC Management description",
        "businessCriticality": "1-Critical"
      }
    },
    {
      "type": "Application",
      "id": "APP-0002",
      "data": {
        "name": "AC Management Cloud",
        "description": "AC Management Cloud description",
        "businessCriticality": "2-High"
      }
    }
  ]
}
```



