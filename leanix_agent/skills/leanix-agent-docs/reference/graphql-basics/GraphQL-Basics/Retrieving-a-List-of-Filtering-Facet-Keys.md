##  Retrieving a List of Filtering Facet Keys
The following example shows how to retrieve a list of all facet keys within a workspace.
Example query:

```
{
  allFactSheets{
    filterOptions {
      facets {
        facetKey
        results {
          name
          key
        }
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
    "allFactSheets": {
      "filterOptions": {
        "facets": [
          {
            "facetKey": "FactSheetTypes",
            "results": [
              {
                "name": "BusinessCapability",
                "key": "BusinessCapability"
              },
              {
                "name": "Process",
                "key": "Process"
              },
              {
                "name": "UserGroup",
                "key": "UserGroup"
              },
              {
                "name": "Project",
                "key": "Project"
              },
              {
                "name": "Application",
                "key": "Application"
              },
              {
                "name": "Interface",
                "key": "Interface"
              },
              {
                "name": "DataObject",
                "key": "DataObject"
              },
              {
                "name": "ITComponent",
                "key": "ITComponent"
              },
              {
                "name": "Provider",
                "key": "Provider"
              },
              {
                "name": "TechnicalStack",
                "key": "TechnicalStack"
              }
            ]
          },
          {
            "facetKey": "hierarchyLevel",
            "results": [
              {
                "name": "1",
                "key": "1"
              },
              {
                "name": "2",
                "key": "2"
              },
              {
                "name": "3",
                "key": "3"
              }
            ]
          },
          {
            "facetKey": "DataQuality",
            "results": [
              {
                "name": "noResponsible",
                "key": "_noResponsible_"
              },
              {
                "name": "qualitySealBroken",
                "key": "_qualitySealBroken_"
              },
              {
                "name": "noDescription",
                "key": "_noDescription_"
              },
              {
                "name": "noLifecycle",
                "key": "_noLifecycle_"
              }
            ]
          },
          {
            "facetKey": "_TAGS_",
            "results": [
              {
                "name": "Headquarter",
                "key": "aa51ccc9-db61-48df-89d1-f217f37757ea"
              },
              {
                "name": "Tag2",
                "key": "819d3d4f-f044-470a-8f5d-c11bc15eff67"
              }
            ]
          }
        ]
      }
    }
  },
  "errors": null
}
```



