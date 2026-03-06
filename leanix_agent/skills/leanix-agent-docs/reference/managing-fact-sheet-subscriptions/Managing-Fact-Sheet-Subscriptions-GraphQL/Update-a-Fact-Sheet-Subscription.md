##  Update a Fact Sheet Subscription
Before you update a fact sheet subscription, get the subscription id. To learn how to retrieve all fact sheet subscriptions, see [Retrieving Fact Sheet Subscriptions](https://help.sap.com/docs/leanix/ea/managing-fact-sheet-subscriptions?locale=en-US&state=PRODUCTION&version=CLOUD#loio275af7677a4410148931efc16c6b337e__retrieving_fact_sheet_subscriptions).
To update a subscription, use the updateSubscription mutation. The following arguments are required for this mutation:
  * id: The ID of the subscription.
  * user: The user subscribed to a fact sheet. Pass one of the following attributes in the object: id or email.
  * type: The subscription type. Possible values:
    * ACCOUNTABLE: User who carries overall accountability for a fact sheet.
    * RESPONSIBLE: User responsible for keeping the fact sheet data accurate and up to date.
    * OBSERVER: User who follows fact sheet updates.


In the example, we change the subscription role of the user from Application Manager to Solution Architect using the roleIds argument. You can optionally add a comment.
Example mutation:

```
mutation {
  updateSubscription(
    id: "abd9ca16-b4a7-4199-a0ad-36e5a6de117b"
    user: {id: "e45f0d10-c59e-4c80-bd56-56b9e7325gf6"}
    type: RESPONSIBLE
    roles: [{id: "1d7f3a77-9a33-4029-9077-d21ae4562575", comment: "Changing the subscription role"}]
  ) {
    id
    user {
      id
      email
    }
    type
    roles {
      id
      name
      comment
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
    "updateSubscription": {
      "id": "abd9ca16-b4a7-4199-a0ad-36e5a6de117b",
      "user": {
        "id": "e45f0d10-c59e-4c80-bd56-56b9e7325gf6",
        "email": "john.doeC@organization.com"
      },
      "type": "RESPONSIBLE",
      "roles": [
        {
          "id": "1d7f3a77-9a33-4029-9077-d21ae4562575",
          "name": "Solution Architect",
          "comment": "Changing the subscription role"
        }
      ]
    }
  }
}
```



