##  Delete tags of multiple groups
Use case: Remove all tags of two tag groups from Fact Sheets of a given type can be performed as easy as shown in the below example. The deletion scope marks all Fact Sheets with tags in the tag groups and the given Fact Sheet type to be deleted if not touched. Then the processor configuration stays empty. No Fact Sheet will be touched when processing. At the end of the run, all tags will be removed.
Please do not forget to increase the deletion limit set to 50% by default to 101 to allow removing even 100% of the tags.
Removing all tags from all fact sheets of a specific type:

```
{
 "deletionScope": {
  "maximumDeletionRatio": {
   "tags": 101
  },
  "tags": [
   {
    "tagScopes": [
     {
      "group": "Cloud:Region",
      "tag": ".*"
     }
    ],
    "scope": {
     "facetFilters": [
      {
       "facetKey": "FactSheetTypes",
       "operator": "OR",
       "keys": [
        "CloudComponent"
       ]
      }
     ],
     "ids": []
    }
   },
   {
    "tagScopes": [
     {
      "group": "Cloud:Cloud Service",
      "tag": ".*"
     }
    ],
    "scope": {
     "facetFilters": [
      {
       "facetKey": "FactSheetTypes",
       "operator": "OR",
       "keys": [
        "CloudComponent"
       ]
      }
     ],
     "ids": []
    }
   },
   {
    "tagScopes": [
     {
      "group": "Cloud:Tech Category",
      "tag": ".*"
     }
    ],
    "scope": {
     "facetFilters": [
      {
       "facetKey": "FactSheetTypes",
       "operator": "OR",
       "keys": [
        "CloudComponent"
       ]
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
