##  Include Archived Fact Sheets in scope result
It is even possible to tell iAPI to include archived Fact Sheets in the result by enabling a specific flag. Just set "omitArchivedFactSheets" to false in the scope:
Include archived fact sheets in search results:

```
{
        "scope": {
            "omitArchivedFactSheets": false,
                "ids": [],
                "facetFilters": [
                        {
                                "keys": [
                                        "BusinessCapability"
                                ],
                                "facetKey": "FactSheetTypes",
                                "operator": "OR"
                        },
                        {
                                "keys": [
                                        "archived"
                                ],
                                "facetKey": "TrashBin",
                                "operator": "OR"
                        }
                ]
        },
        "processors": [
                ....
        ]
}
```



**Note**
Using ExternalIDs in search based scope (and in deletion scope).
Scope filters may not only filter for items by their internal ids (key "ids") but by external ids as well. To use this, the key "externalIds needs to be defined and contain an array of searched external ids. Each need to be prefixed with the name of the external id field and a slash. See example below
The Below example can even be dynamic and inject content from the LDIF custom fields:
"externalIds": ["${'externalId/'.concat(header.customFields.myExternalId)}"]
Example how to use external ids in search based scope:

```
{
 "scope": {
  "facetFilters": [],
  "externalIds": [
   "externalId/Ext-ID-0m0NiY6Z"
  ]
 }
}
```



