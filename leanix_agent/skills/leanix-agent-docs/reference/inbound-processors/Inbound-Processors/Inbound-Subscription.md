##  Inbound Subscription
Variables to be set in the output section:
Variable | Required | Notes
---|---|---
user | Required | Users' email (either user or newUser" needs to be present.
newUser | Required | Works like "user" but creates a new user if not existing
subscriptionType | Required |
subscriptionRoles | Optional | It may or may not be required because it is based on the specific configuration set in each workspace
addSubscriptionRoles | Optional | Same as "subscriptionRoles" but adds to existing roles instead of completely replacing all existing roles
optional | Optional | Boolean(Disables warnings related to new user creation in case inboundSubscription only works for existing users)
comment | Optional |


Example inboundSubscription processor:

```
{
  "processorType": "inboundSubscription",
  "processorName": "Subscription creation",
  "processorDescription": "Creates subscriptions",
  "filter": {
    "exactType": "ITComponent"
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
  "updates": [
    {
      "key": {
        "expr": "user"
      },
      "values": [
        {
          "expr": "jane.doe@leanix.net"
        }
      ]
    },
    {
      "key": {
        "expr": "subscriptionType"
      },
      "values": [
        {
          "expr": "RESPONSIBLE"
        }
      ]
    },
    {
      "key": {
        "expr": "subscriptionRoles"
      },
      "values": [
        {
          "map": [
            {
              "key": "roleName",
              "value": "Business Owner"
            },
            {
              "key": "comment",
              "value": "This person is the business owner"
            }
          ]
        }
      ]
    },
    {
      "key": {
        "expr": "newUser.userName"
      },
      "values": [
        {
          "expr": "jane.doe@leanix.net"
        }
      ]
    },
    {
      "key": {
        "expr": "newUser.email"
      },
      "values": [
        {
          "expr": "jane.doe@leanix.net"
        }
      ]
    },
    {
      "key": {
        "expr": "newUser.firstName"
      },
      "values": [
        {
          "expr": "Jane"
        }
      ]
    },
    {
      "key": {
        "expr": "newUser.lastName"
      },
      "values": [
        {
          "expr": "Doe"
        }
      ]
    }
  ]
}

```



