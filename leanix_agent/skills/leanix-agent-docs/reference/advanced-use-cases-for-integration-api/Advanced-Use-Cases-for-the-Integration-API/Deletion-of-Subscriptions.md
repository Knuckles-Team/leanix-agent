##  Deletion of Subscriptions
Example configuration to use advanced deletion on subscriptions. Here, to remove all subscriptions on application Fact Sheets that have an anonymised user as a subscriber for a subscription of type "RESPONSIBLE".
Please note, that the below configuration does not configure any processors, thus can work with an empty LDIF as input to trigger Integration API.
Delete all RESPONSIBLE subscriptions of anonymized users for application fact sheets:

```
{
 "deletionScope": {
  "subscriptions": [
   {
    "subscriptionScopes": [
     {
      "type": "RESPONSIBLE",
      "roles": []
     }
    ],
    "scope": {
     "facetFilters": [
      {
       "keys": [
        "Application"
       ],
       "facetKey": "FactSheetTypes",
       "operator": "OR"
      }
     ]
    },
    "advanced": "${lx.subscription.user.userName=='AnonymizedUser'}"
   }
  ]
 },
 "processors": []
}
```



Empty LDIF for advanced deletion:

```
{
 "connectorId": "subscription",
 "connectorType": "subscription",
 "connectorVersion": "1.0.0",
 "content": [],
 "lxVersion": "1.0.0"
}
```



**Note**
Using External IDs in pathfinder search scopes.
When working with integrations, specifically with deletion scopes it is handy to know that pathfinder is capable filtering documents by their external id. and not only by internal id which is most of the times not known to foreign systems.
To filter by external ids, just use the field "externalIds" instead of "ids" in the search scope definition.
Please note that Pathfinder required a special syntax when defining external ids using the name of the externalID field, a slash ("/") then value of the externalId.
Example for the default externalId field:
"externalIds": ["${'externalId/'.concat(header.customFields.myExternalId)}"]
