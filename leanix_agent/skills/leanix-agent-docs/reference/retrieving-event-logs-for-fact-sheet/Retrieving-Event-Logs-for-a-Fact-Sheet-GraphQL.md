# Retrieving Event Logs for a Fact Sheet (GraphQL)
Retrieve event logs for a fact sheet using the GraphQL API.
**Note**
You can retrieve event logs for fact sheets only through the GraphQL API. Our REST APIs don't offer a dedicated endpoint for this operation.
All updates to a fact sheet are recorded in the event logs. You can use event logs to create audit trails and get insights into the dynamics of your workspace. In the application user interface, event logs appear on the Last Update tab of the fact sheet page.
To retrieve event logs through the GraphQL API, use the allLogEvents query. factSheetId is a required argument for this query. To learn how to get the ID of a fact sheet, see [Retrieving Fact Sheets](https://help.sap.com/docs/leanix/ea/retrieving-fact-sheets?locale=en-US&state=PRODUCTION&version=CLOUD "Example queries for retrieving fact sheets through the GraphQL API.").
To filter logs by a specific event type, add the eventTypes argument to the allLogEvents query. To view the full list of event types, navigate to the GraphiQL tool in your workspace and search for the EventTypes schema type. To include multiple event types in the query, use an array of values, as shown in the following example: eventTypes: [FACT_SHEET_TAG_ADDED, FACT_SHEET_TAG_REMOVED].
**Tip**
You can automate the routine retrieval of event logs by setting up cron jobs or using automation tools. To fetch event logs for all fact sheets or for specific types of fact sheets, create a script with a loop that iterates over the fact sheet IDs. To obtain all fact sheet IDs, use the allFactSheets query. These IDs can then be used as input for the allLogEvents query. To learn how to fetch fact sheets, see [Retrieving Fact Sheets](https://help.sap.com/docs/leanix/ea/retrieving-fact-sheets?locale=en-US&state=PRODUCTION&version=CLOUD "Example queries for retrieving fact sheets through the GraphQL API.").
To receive real-time updates for specific events automatically without pulling them, consider using webhooks. To learn more, see [Webhooks](https://help.sap.com/docs/leanix/ea/webhooks?locale=en-US&state=PRODUCTION&version=CLOUD "Listen to events in SAP LeanIX using webhooks.").
In the following example query, we retrieve events of the QUALITY_SEAL_APPROVED type, which indicates the approval of the quality seal on a fact sheet.
The createdAt attribute in the response denotes the time stamp of the event. By using this value, you can identify when the quality seal is set to expire. For example, if the expiration time of the quality seal is set to three months, it means that it will expire three months after the createdAt date — unless a breaking event occurs earlier. You can use this information to get a snapshot of fact sheets whose quality seals will expire soon.
As an administrator, you can set the expiration time of the quality seal in the fact sheet configuration. To learn more, see [Quality Seal](https://help.sap.com/docs/leanix/ea/quality-seal?locale=en-US&state=PRODUCTION&version=CLOUD "Quality seal ensures data integrity by assigning approval responsibility to accountable and responsible subscribers of fact sheets. When broken, it prompts verification and approval of fact sheet information.").
Example query:

```
{
  allLogEvents(
    factSheetId: "2efa37b5-18aa-48d8-9d70-1328c0d856d7"
    eventTypes: QUALITY_SEAL_APPROVED
  ) {
    edges {
      node {
        id
        eventType
        path
        oldValue
        newValue
        message
        secondsPast
        createdAt
        user {
          id
          firstName
          lastName
          displayName
          email
          technicalUser
        }
      }
    }
  }
}

```



Example response:

```
{
  "data": {
    "allLogEvents": {
      "edges": [
        {
          "node": {
            "id": "42574",
            "eventType": "QUALITY_SEAL_APPROVED",
            "path": "/qualitySeal",
            "oldValue": null,
            "newValue": "APPROVED",
            "message": "The quality seal was approved by user 'John Doe'",
            "secondsPast": 4928370,
            "createdAt": "2024-02-13T14:44:06.299466554Z",
            "user": {
              "id": "5ee78c21-98a2-4377-acaa-fc66ff2b78fg",
              "firstName": "John",
              "lastName": "Doe",
              "displayName": "John Doe",
              "email": "john.doe@example.com",
              "technicalUser": false
            }
          }
        }
      ]
    }
  }
}

```



