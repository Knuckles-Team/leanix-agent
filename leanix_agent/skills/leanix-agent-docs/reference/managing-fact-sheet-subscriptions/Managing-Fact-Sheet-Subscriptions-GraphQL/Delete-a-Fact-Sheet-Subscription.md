##  Delete a Fact Sheet Subscription
Before you delete a fact sheet subscription, get the subscription id. To learn how to retrieve all fact sheet subscriptions, see [Retrieving Fact Sheet Subscriptions](https://help.sap.com/docs/leanix/ea/managing-fact-sheet-subscriptions?locale=en-US&state=PRODUCTION&version=CLOUD#loio275af7677a4410148931efc16c6b337e__retrieving_fact_sheet_subscriptions).
To delete a subscription, use the deleteSubscription mutation.
Example mutation:

```
mutation {
  deleteSubscription(id: "abd9ca16-b4a7-4199-a0ad-36e5a6de117b") {
    id
    name
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
    "deleteSubscription": {
      "id": "01740698-1ffa-4729-94fa-da6194ebd7cd",
      "name": "AC Management"
    }
  }
}
```



YesNo
Send
