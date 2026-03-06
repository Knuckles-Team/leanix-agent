##  Get Subscription Roles
Before you start, get subscription roles configured in your workspace using the allSubscriptionRoles query.
Example query:

```
{
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
            "id": "1d7f3a77-9a33-4029-9077-d21ae4562575",
            "name": "Solution Architect"
          }
        },
        {
          "node": {
            "id": "b4ccabdc-f0c4-4386-8ff0-b54e0882605f",
            "name": "Application Manager"
          }
        }
      ]
    }
  }
}
```



