# Filtering in GraphQL
### On this page
  * [Filters](https://help.sap.com/docs/leanix/ea/filtering-in-graphql?version=CLOUD#filters)
  * [Logical Operators](https://help.sap.com/docs/leanix/ea/filtering-in-graphql?version=CLOUD#logical-operators)
  * [Facet Keys](https://help.sap.com/docs/leanix/ea/filtering-in-graphql?version=CLOUD#facet-keys)
  * [Global Facet Keys](https://help.sap.com/docs/leanix/ea/filtering-in-graphql?version=CLOUD#global-facet-keys)
  * [Facet Keys Specific to Fact Sheet Types](https://help.sap.com/docs/leanix/ea/filtering-in-graphql?version=CLOUD#facet-keys-specific-to-fact-sheet-types)
  * [Retrieving Facet Filters](https://help.sap.com/docs/leanix/ea/filtering-in-graphql?version=CLOUD#retrieving-facet-filters)
  * [Examples](https://help.sap.com/docs/leanix/ea/filtering-in-graphql?version=CLOUD#examples)


Learn how filtering in GraphQL works and how to apply filters to your queries.
Data filtering is crucial for extracting relevant insights from your organization's data. GraphQL allows you to filter data accurately based on specific criteria, enhancing data retrieval and management efficiency.
This document offers an overview of data filtering in GraphQL, with a focus on its implementation in the SAP LeanIX GraphQL API. You'll learn how to fetch available filters and use them in your GraphQL queries.
**Tip**
You can export GraphQL queries from the inventory based on your inventory data, including any applied filters and sorting options. To learn more, see [Exporting Queries from the Inventory](https://help.sap.com/docs/leanix/ea/graphql-api?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a6d497a4410149a8bffcc34da11b9__section_gym_cf3_jhc).
**Note**
Understanding which GraphQL operations support filtering is key to using filters effectively. You can explore available filters by navigating through the GraphiQL interface in your SAP LeanIX workspace. This interface provides a comprehensive and interactive overview of the GraphQL schema. To learn more about GraphiQL and how to navigate to it, see [GraphiQL Tool](https://help.sap.com/docs/leanix/ea/graphql-api?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a6d497a4410149a8bffcc34da11b9__graphiql_tool).
