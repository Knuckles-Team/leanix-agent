##  Retrieving Facet Filters
You can retrieve the available filter options for specific fact sheet types. This feature helps you understand the available facets, their keys, the possible operators you can use with them, and the options for applying a specific filter.
The following GraphQL query retrieves the available facet filters for the Application fact sheet type:

```
query availableFaceFilters {
  allFactSheets(factSheetType: Application) {
    filterOptions {
      facets {
        facetKey
        possibleOperators
        operator
        results {
          name
          key
        }
        dateFilter {
          from
          to
          type
          minDate
          maxDate
        }
        relationFieldsFilterOperator
        relationFieldsFilter {
          fieldName
          values {
            key
            selected
          }
        }
      }
    }
  }
}
```



The query returns a list of facets for the Application fact sheet type. Each facet includes the following attributes:
  * facetKey: The facet's key.
  * possibleOperators: A list of logical operators you can use with the facet.
  * operator: The logical operator used with the facet.
  * results: A list of available options for using the facet. Each option has a name and a key.
  * dateFilter: If the filter supports date ranges, this attribute provides details and options, including the range (from and to), type, and the minimum and maximum dates (minDate and maxDate).
  * relationFieldsFilterOperator: The operator used with the relational fields filter.
  * relationFieldsFilter: Details of the relational fields filter, including the field name (fieldName) and a list of values. Each value has a key and a selected status.


The following example response is shortened and doesn't include all available filter options.

```
{
  "data": {
    "allFactSheets": {
      "filterOptions": {
        "facets": [
          {
            "facetKey": "FactSheetTypes",
            "possibleOperators": [],
            "operator": "OR",
            "results": [
              {
                "name": "Objective",
                "key": "Objective"
              },
              {
                "name": "Platform",
                "key": "Platform"
              },
              {
                "name": "Initiative",
                "key": "Initiative"
              },
              {
                "name": "BusinessCapability",
                "key": "BusinessCapability"
              },
              {
                "name": "BusinessContext",
                "key": "BusinessContext"
              },
              {
                "name": "Organization",
                "key": "Organization"
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
            ],
            "dateFilter": null,
            "relationFieldsFilterOperator": null,
            "relationFieldsFilter": null
          },
          {
            "facetKey": "DataQuality",
            "possibleOperators": [
              "OR",
              "AND",
              "NOR"
            ],
            "operator": "OR",
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
            ],
            "dateFilter": null,
            "relationFieldsFilterOperator": null,
            "relationFieldsFilter": null
          },
          {
            "facetKey": "lxState",
            "possibleOperators": [
              "OR",
              "NOR"
            ],
            "operator": "OR",
            "results": [
              {
                "name": "BROKEN_QUALITY_SEAL",
                "key": "BROKEN_QUALITY_SEAL"
              },
              {
                "name": "DRAFT",
                "key": "DRAFT"
              },
              {
                "name": "REJECTED",
                "key": "REJECTED"
              },
              {
                "name": "APPROVED",
                "key": "APPROVED"
              }
            ],
            "dateFilter": null,
            "relationFieldsFilterOperator": null,
            "relationFieldsFilter": null
          },
          ...
        ]
      }
    }
  }
}
```



