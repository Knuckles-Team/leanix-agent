##  Step 1: Import Fact Sheets with Basic Information
In the first step, import application fact sheets with the following attributes:
Attribute Key | Type | Description
---|---|---
name |  STRING | The name of the fact sheet.
description |  STRING | The description of the fact sheet.


**Tip**
To get attribute keys, go to the processor configuration page, click the three-dot icon in the upper-right corner, then select Get Data Model. The data model of the workspace is returned in the Output Log section, where you can find the keys of specific attributes.
![Getting the Data Model of the Workspace from the Processor Page](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27464c077a441014a7918df4b4e20f20_LowRes.png)
Getting the Data Model of the Workspace from the Processor Page
To configure and run a connector, follow these steps:
  1. Go to the Integration API section in the administration area.
  2. Click New Processor Configuration, fill in the required details, and then click Create.
  3. On the connector configuration page, enter the processor configuration in the left-side section.
  4. In the Input section on the right, enter the input data.
  5. To start a test run, click Test run. If successful, proceed to the next step.
  6. To start a run, click Run.
  7. To save the connector, click Save in the lower-left corner.


Two application fact sheets are imported into the workspace with their names and descriptions. You can check the created fact sheets in the inventory. To learn how to use the inventory, see [Inventory](https://help.sap.com/docs/leanix/ea/inventory?locale=en-US&state=PRODUCTION&version=CLOUD "The inventory is your centralized repository for managing and documenting enterprise architecture objects. You create, edit, and organize fact sheets to maintain an accurate depiction of your IT landscape. It is the go-to place for anyone seeking information from the fact sheets.").
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
**Note**
The id passed in the content array represents the record ID in the external system. This ID is written to the externalId field (External ID). A unique fact sheet ID is generated automatically upon fact sheet creation.
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
        "description": "AC Management description"
      }
    },
    {
      "type": "Application",
      "id": "APP-0002",
      "data": {
        "name": "AC Management Cloud",
        "description": "AC Management Cloud description"
      }
    }
  ]
}
```



