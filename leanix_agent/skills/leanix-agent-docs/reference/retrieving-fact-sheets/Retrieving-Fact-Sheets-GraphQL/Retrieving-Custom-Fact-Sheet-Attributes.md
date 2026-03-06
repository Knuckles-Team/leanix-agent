##  Retrieving Custom Fact Sheet Attributes
You can retrieve data specific to a certain fact sheet type using inline fragments. To understand how inline fragments work in GraphQL, refer to [Inline Fragments![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fgraphql.org%2Flearn%2Fqueries%2F%23inline-fragments "https://graphql.org/learn/queries/#inline-fragments") in the GraphQL documentation.
Fact sheets come with standard attributes defined in the meta model configuration. You can also add custom attributes to a fact sheet to tailor the configuration to your needs. For more details, see [Adding Custom Attributes](https://help.sap.com/docs/leanix/ea/meta-model-configuration?locale=en-US&state=PRODUCTION&version=CLOUD#loio275955467a441014a5dce078bf2e383c__adding_custom_attributes).
The following example query returns all fact sheets with these attributes:
  * Standard fields: id, name, and type
  * Custom fields specific to IT component fact sheets: capEx and opEx


We use an inline fragment ... on ITComponent to request custom fields for IT component fact sheets. These fields aren't returned for other types of fact sheets.
Example query:

```
{
  allFactSheets {
    totalCount
    edges {
      node {
        id
        name
        type
        ... on ITComponent {
          capEx
          opEx
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
      "totalCount": 120,
      "edges": [
        {
          "node": {
            "id": "28fe4aa2-6e46-41a1-a131-72afb3acf256",
            "name": "AC Management",
            "type": "Application"
          }
        },
        {
          "node": {
            "id": "9deb9733-5701-42f1-8c52-c165acaa6487",
            "name": "App Maintenance & Support Service",
            "type": "ITComponent",
            "capEx": 2000,
            "opEx": 1500
          }
        },
        ...
      ]
    }
  }
}
```



