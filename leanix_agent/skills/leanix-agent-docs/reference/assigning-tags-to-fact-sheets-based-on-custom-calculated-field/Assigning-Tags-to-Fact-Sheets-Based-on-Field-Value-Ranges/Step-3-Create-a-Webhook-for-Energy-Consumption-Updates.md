##  Step 3: Create a Webhook for Energy Consumption Updates
Create a webhook that triggers upon updates to the EnergyConsumptionLevel field on IT component fact sheets.
Follow these steps:
  1. On the user profile, select Administration, and then select Webhooks in the sidebar.
  2. On the Webhooks page, click New Webhook.
  3. Specify the webhook details:
     * Triggering Events: Select FACT_SHEET_UPDATED.
     * Managing User: Select a technical user with admin permissions.
     * Type: Select PUSH.
     * Target URL: Enter the URL of the endpoint to send webhook notifications to. Before you complete other steps in this tutorial, enter a test target URL.
  4. Optional: In the Callback field, enter JavaScript code to manipulate the webhook payload.
Sample code:

```
var payload = delivery.payload;
delivery.active = false;
var tempDict = {};
tempDict['fields'] = [];
var attributeList = ['EnergyConsumptionLevel'];

if (payload.factSheet.type === 'ITComponent') {
    tempDict['id'] = payload.factSheet.id;
    tempDict['type'] = payload.factSheet.type;
    tempDict['rev'] = payload.factSheet.rev;

    for (var i = 0; i < payload.factSheet.fields.length; ++i) {
        if (attributeList.indexOf(payload.factSheet.fields[i].name) >= 0) {
            tempDict.fields.push({ key: payload.factSheet.fields[i].name, value: payload.factSheet.fields[i].data });
        }
    }

    if (tempDict['fields'].length > 0) {
        delivery.payload = tempDict;
        delivery.active = true;
    }
}
```



With the provided callback, the webhook payload appears as follows.
Example webhook payload:

```
{
    "fields": [
        {
            "key": "EnergyConsumptionLevel",
            "value": {
                "value": 820,
                "type": "IntegerValue"
            }
        }
    ],
    "id": "cb943942-39fd-4b45-8909-916b99c1286a",
    "type": "ITComponent",
    "rev": 15
}
```



  5. Optional: Specify other optional webhook details.
  6. Click Create.


A webhook with a test target URL is created. To test the webhook, update the energy consumption value on an IT component fact sheet and verify the payload sent to the target URL.
