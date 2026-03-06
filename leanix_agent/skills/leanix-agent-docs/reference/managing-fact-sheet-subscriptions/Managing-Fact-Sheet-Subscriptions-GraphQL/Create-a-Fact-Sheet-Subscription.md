##  Create a Fact Sheet Subscription
To create a subscription to a fact sheet for a user, use the createSubscription mutation. The following arguments are required for this mutation:
  * factSheetId: The ID of the fact sheet to subscribe the user to. To learn how to get the ID of a fact sheet, see [Retrieving Fact Sheets](https://help.sap.com/docs/leanix/ea/retrieving-fact-sheets?locale=en-US&state=PRODUCTION&version=CLOUD "Example queries for retrieving fact sheets through the GraphQL API.").
  * user: The user to be subscribed to a fact sheet. Pass one of the following attributes in the object: id or email.
  * type: The subscription type. Possible values:
    * ACCOUNTABLE: User who carries overall accountability for a fact sheet.
    * RESPONSIBLE: User responsible for keeping the fact sheet data accurate and up to date.
    * OBSERVER: User who follows fact sheet updates.


To specify subscription roles, use the roleIds argument. To retrieve the IDs of subscription roles, use the allSubscriptionRoles query. Once you get all the required parameters, create a subscription using the createSubscription mutation. In the example, we subscribe a user as RESPONSIBLE with the Application Manager subscription role.
Example mutation:

```
mutation {
  createSubscription(factSheetId: "01740698-1ffa-4729-94fa-da6194ebd7cd",
  user: {id: "e45f0d10-c59e-4c80-bd56-56b9e7325gf6"},
  type: RESPONSIBLE,
  roleIds: ["b4ccabdc-f0c4-4386-8ff0-b54e0882605f"]) {
    id
    user {
      id
      email
    }
    type
    roles {
      id
      name
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
    "createSubscription": {
      "id": "abd9ca16-b4a7-4199-a0ad-36e5a6de117b",
      "user": {
        "id": "e45f0d10-c59e-4c80-bd56-56b9e7325gf6",
        "email": "john.doeC@organization.com"
      },
      "type": "RESPONSIBLE",
      "roles": [
        {
          "id": "b4ccabdc-f0c4-4386-8ff0-b54e0882605f",
          "name": "Application Manager"
        }
      ]
    }
  }
}
```



