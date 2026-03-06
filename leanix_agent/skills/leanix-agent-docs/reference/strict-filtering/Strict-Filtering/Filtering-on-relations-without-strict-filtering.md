##  Filtering on relations without strict filtering
SAP LeanIX will retrieve all fact sheets that apply to a certain filter and then retrieve all relations of those fact sheets and not just the ones that apply to the filter.
If users specify a filter based on a relation target, e.g., all applications that use a specific data object, then all applications are returned, including their properties and relations. In the case of “non-strict filtering”, the filter is not applied to the relations, and therefore relations that don't fit the filter are returned as well.
![1226](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27427c3d7a441014adb3e75c352a0888_LowRes.png)
Filtering for all applications that use the data object “Customer”, will retrieve all applications that use the data object “Customer” along with all their relations, i.e., also relations to the data objects that weren't specified in the filter, e.g., “Order”
