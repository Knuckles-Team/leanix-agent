##  Filtering Fact Sheets by Subscriptions
To filter fact sheets by subscriptions, use the Subscriptions facet key with the allFactSheets query. To learn more about subscriptions, refer to:
  * [Fact Sheet Subscription](https://help.sap.com/docs/leanix/ea/fact-sheet-subscription?locale=en-US&state=PRODUCTION&version=CLOUD "Fact sheet subscription assigns responsibility and accountability to users for maintaining data. Learn about fact sheet subscriptions, including types, roles, and how to assign and subscribe to fact sheets to promote stakeholder involvement and ensure data accuracy and completeness.")
  * [Subscription Roles](https://help.sap.com/docs/leanix/ea/subscription-roles?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to create, edit, and delete subscription roles and manage settings like enabling the 'Accountable' type, limiting multiple subscriptions, and enforcing mandatory role selection.")


In the following example, we filter fact sheets by user ID, subscription type, and subscription role. We aim to retrieve fact sheets where a specific user is subscribed as ACCOUNTABLE (subscription type) and Solution Architect (custom subscription role).
Subscription types are predefined, with possible values of ACCOUNTABLE, RESPONSIBLE, or OBSERVER. Workspace admins define subscription roles, which are associated with unique IDs. To get the IDs of subscription roles, use the allSubscriptionRoles query.
Example query:

```
query getSubscriptionRoles {
  allSubscriptionRoles {
    edges {
      node {
        id
        name
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
    "allSubscriptionRoles": {
      "edges": [
        {
          "node": {
            "id": "8d1aab90-4d86-43e5-9a75-bafccee81732",
            "name": "Data Architect"
          }
        },
        {
          "node": {
            "id": "a523b819-208c-49ef-a0c6-8d8b84464f6e",
            "name": "Solution Architect"
          }
        }
      ]
    }
  }
}
```



To filter fact sheets that a specific user is subscribed to, pass the user id in the keys array. You can provide multiple user IDs.
  * To get user IDs, retrieve all workspace users by making a GET request to the following endpoint on the MTM REST API. For the endpoint schema, visit the [API documentation![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fapp.leanix.net%2Fopenapi-explorer%2F%23%2Fworkspaces%2FgetUsers "https://app.leanix.net/openapi-explorer/#/workspaces/getUsers").

```
https://{SUBDOMAIN}.leanix.net/services/mtm/v1/workspaces/{id}/users
```



  * To find your user ID, go to the API Tokens section in the admin area and look for the UserId value.


In the example, we use the FactSheetTypes facet key to return fact sheets of the application type.
Example query:

```
query retrieveFactSheetsBySubscriber($filter: FilterInput!) {
  allFactSheets(filter: $filter) {
    totalCount
    edges {
      node {
        id
        displayName
        type
      }
    }
  }
}
```



Variables:

```
{
  "filter": {
    "facetFilters": [
      {
        "facetKey": "FactSheetTypes",
        "operator": "OR",
        "keys": [
          "Application"
        ]
      },
      {
        "facetKey": "Subscriptions",
        "operator": "OR",
        "keys": [
          "87678c21-98a2-9567-acaa-fc66ff2b9d56"
        ],
        "subscriptionFilter": {
          "type": "ACCOUNTABLE",
          "roleId": "a523b819-208c-49ef-a0c6-8d8b84464f6e"
        }
      }
    ]
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
    "allFactSheets": {
      "totalCount": 2,
      "edges": [
        {
          "node": {
            "id": "01740698-1ffa-4729-94fa-da6194ebd7cd",
            "displayName": "AC Management",
            "type": "Application"
          }
        },
        {
          "node": {
            "id": "4d121f64-116b-4ccc-a292-eb4e4f8d1b24",
            "displayName": "AC Management Cloud",
            "type": "Application"
          }
        }
      ]
    }
  }
}
```



