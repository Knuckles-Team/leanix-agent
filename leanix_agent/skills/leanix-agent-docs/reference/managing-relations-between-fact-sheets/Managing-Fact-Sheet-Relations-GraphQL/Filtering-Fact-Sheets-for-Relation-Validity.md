##  Filtering Fact Sheets for Relation Validity
Relation validity ("activeFrom" and "activeUntil") is the time interval during which a relation between fact sheets is deemed to exist. The two values are dates in ISO format like 2018-07-01(no time).
Any of them may be unspecified, which means the Relation validity is not bounded in this direction of time. If both of these values of the relation are not set, then the Relation is considered to always exist.
For this purpose, the DateFilterInput argument type contains the fields from and to and the DateFilterType in field type.
These are the possible values of the type field:
  * Of main importance is only the date filter type RANGE.
  * RANGE_START and RANGE_ENDS are not implemented for relation validity filtering and behave like RANGE for now.
  * POINT behaves like RANGE, but the given value for to is ignored and always considered to be equal to from.
  * TODAY, END_OF_MONTH, and END_OF_YEAR are special cases of POINT where the given values of from and to are ignored and considered to be equal to the day corresponding to the type.


The values of the fields from and to are dates in ISO format (no time) and define the filter interval. Any of the two values may be null, meaning the interval is unbounded in that direction.
The relation validity filtering semantics is the following: a relation is matched by the filter if and only if the relation validity interval has a non-empty intersection with the filter interval. In other words, if the time span defined by the relation's activeFrom and activeUntil fields and the time span defined by the filter's from and to fields overlap.
In the GraphQL API, you can filter Fact Sheets for relation validity in the:
  * Relation facets
  * Relation validity filter


### Filtering Relations in the Relation Facet
You can filter relations in the relation facets (filter ->facetFilter -> dateFilter argument of the allFactSheets top level query field).
For now, instead of the dateFilter on the individual relation facets, the dateFilter on the lifecycle facet is used. This will change in a future version. The key field of this lifecycle filter facet is ignored for the purpose of relation validity filtering.
Example query:

```
{
     allFactSheets(filter:
       {facetFilters: [
         {facetKey:"FactSheetTypes" keys:["UserGroup"]}
         {facetKey: "relUserGroupToApplication" keys: ["e3a08f5f-5c3e-4dc1-8444-ed87bdd48634"]}
         {facetKey:"lifecycle" keys:"__any__" dateFilter:{type:RANGE from:"2018-07-01" to:"2018-07-31"}}
       ]})
     {
       edges {
         node {
           type
           displayName
         }
       }
     }
   }
```



### Filtering Relations in the Relation Validity Filter
This is a filter that restricts the relations that are returned in the relation fields of a concrete Fact Sheet type, for example, field relApplicationToUserGroup in typeApplication. Those fields accept an argument validityFilter containing the fields activeFrom and activeUntil, which behave like from and to in DateFilterInput (see above).
Example query:

```
{
     factSheet(id: "e3a08f5f-5c3e-4dc1-8444-ed87bdd48634") {
       displayName
       ... on Application {
         relApplicationToUserGroup(validityFilter: {activeFrom: "2018-07-01", activeUntil: "2018-07-31"}) {
           edges {
             node {
               activeFrom
               factSheet {
                 displayName
               }
             }
           }
         }
       }
     }
   }
```



