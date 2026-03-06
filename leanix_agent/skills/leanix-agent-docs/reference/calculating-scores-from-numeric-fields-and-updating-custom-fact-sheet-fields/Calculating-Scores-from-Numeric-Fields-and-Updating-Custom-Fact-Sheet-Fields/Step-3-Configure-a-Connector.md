##  Step 3: Configure a Connector
To configure and run a connector, follow these steps:
  1. Go to the Integration API section in the administration area.
  2. Click New Processor Configuration, fill in the required details, and then click Create.
  3. On the connector configuration page, enter processors in the left-side section.
  4. In the Input section on the right, enter the input data.
  5. To start a test run, click Test run. If successful, proceed to the next step.
  6. To start a run, click Run.
  7. To save the connector, click Save in the lower-left corner.


**Tip**
You can configure the processor to run automatically every day, keeping your inventory data up to date. To learn how to configure daily runs, refer to [Configuring Automated Nightly Runs for Inbound Processors](https://help.sap.com/docs/leanix/ea/configuring-automated-nightly-runs-for-inbound-processors?locale=en-US&state=PRODUCTION&version=CLOUD "Adjust the configuration of inbound Integration API processors to enable automated nightly runs.").
### Processor Steps
The connector includes three processors that perform these tasks:
  1. Read values from the InfrastructureRiskScore and ApplicationOperationalRiskScore numeric fields and store them in the TotalRiskScore variable.
  2. Write the calculated total risk score to the TotalRiskScore field.
  3. Map the total risk score to a user-friendly risk tier and write it to the RiskTier field.


**Tip**
When specifying multiple processors in the configuration, use the run attribute to set the execution order. Numeration starts at 0, so the processor with "run": 0 runs first, the processor with "run": 1 runs second, and so on.
### Processor Configuration
Example processor configuration:

```
{
  "processors": [
    {
      "processorType": "inboundFactSheet",
      "processorName": "1. Gather scores and store in variables",
      "processorDescription": "Gather Scores and Store in Variables",
      "type": "Application",
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
      "enabled": true,
      "variables": [
        {
          "key": "${lx.factsheet.id.concat('_TotalRiskScore')}",
          "value": "${helper:toList(lx.factsheet.InfrastructureRiskScore,lx.factsheet.ApplicationOperationalRiskScore)}"
        }
      ],
      "read": {
        "fields": [
          "InfrastructureRiskScore",
          "ApplicationOperationalRiskScore"
        ]
      }
    },
    {
      "processorType": "inboundFactSheet",
      "processorName": "2. Write total risk score",
      "processorDescription": "Gather Scores and Store in Variables",
      "type": "Application",
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
      "run": 1,
      "updates": [
        {
          "key": {
            "expr": "TotalRiskScore"
          },
          "values": [
            {
              "expr": "${variables[lx.factsheet.id.concat('_TotalRiskScore')].getNumbers().sum() != 0 ? variables[lx.factsheet.id.concat('_TotalRiskScore')].getNumbers().sum() : null }"
            }
          ]
        }
      ],
      "enabled": true
    },
    {
      "processorType": "inboundFactSheet",
      "processorName": "3. Write Risk Tier",
      "processorDescription": "Assign Risk Tier based on Total Risk Score",
      "type": "Application",
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
      "run": 2,
      "updates": [
        {
          "key": {
            "expr": "RiskTier"
          },
          "values": [
            {
              "expr": "${ lx.factsheet.TotalRiskScore < 10 ? 'Green' : lx.factsheet.TotalRiskScore < 17 ? 'Yellow' : lx.factsheet.TotalRiskScore < 24 ? 'Orange' : lx.factsheet.TotalRiskScore > 23 ? 'Red' : null}"
            }
          ]
        }
      ],
      "enabled": true,
      "read": {
        "fields": [
          "TotalRiskScore"
        ]
      }
    }
  ],
  "variables": {}
}
```



### Input Data
Example input data:

```
{
  "connectorType": "DerivedScoring",
  "connectorId": "DerivedScoring",
  "connectorVersion": "1.0.0",
  "lxVersion": "1.0.0",
  "description": "",
  "processingDirection": "inbound",
  "processingMode": "partial",
  "customFields": {},
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
