##  Remove tags
Deletion of Tags works similar. One or more deletion scope sections of type "tags" needs to be configured. The scope defines the set of Fact Sheets to be looked at when removing tags and allows to configure a tag group and a tag name to be deleted. Tag names support regular expression matching to allow removal of tags based on name patterns. Please note that tags will be removed from the Fact Sheets where no longer referenced by processors adding them but tags themselves will not be deleted.
The following example processor removes tags and subscriptions from fact sheets.
Example configuration to remove tags and subscriptions from fact sheets:

```
{
 "deletionScope": {
  "maximumDeletionRatio": {
   "tags": 40
  },
  "tags": [
   {
    "tagScopes": [
     {
      "group": "myGroup",
      "tag": "Prefix_.*"
     }
    ],
    "scope": {
     "facetFilters": [
      {
       "keys": [
        "Project"
       ],
       "facetKey": "FactSheetTypes",
       "operator": "OR"
      }
     ],
     "ids": []
    },
    "advanced": "${lx.tag.tagGroup.name==null}"
   }
  ],
  "subscriptions": [
   {
    "subscriptionScopes": [
     {
      "type": "RESPONSIBLE",
      "roles": [
       "My Role"
      ]
     }
    ],
    "scope": {
     "facetFilters": [
      {
       "keys": [
        "Project"
       ],
       "facetKey": "FactSheetTypes",
       "operator": "OR"
      }
     ],
     "ids": []
    }
   }
  ]
 },
 "processors": []
}
```



