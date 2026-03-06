##  How to export Fact Sheets that are archived
To include archived Fact Sheets when using outbound processors, a flag "omitArchivedFactSheets" needs to be set to false as in the sample below. Default for Integration API is to ignore all archived Fact Sheets when exporting.
Example scope definition to export Fact Sheets including archived ones:
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
  "processors": [...]
}

```



