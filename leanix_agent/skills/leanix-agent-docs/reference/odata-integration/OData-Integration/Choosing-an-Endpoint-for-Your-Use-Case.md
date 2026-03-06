##  Choosing an Endpoint for Your Use Case
The table below lists recommended endpoints for various use cases.
Use Case | Recommended Endpoint | Reasoning
---|---|---
Self-service analytics (for example, in Microsoft Power BI or Tableau) without complex transformations | BookmarkService.svc | It's easier to understand and use directly in reports.
Ad hoc analysis and quick insights | BookmarkService.svc | It's more user-friendly for exploration.
Long-term report stability | BookmarkDataService.svc | It reduces risk when field names change.
Data integration and transformations (merging with other sources, stable references) | BookmarkDataService.svc | It offers more stable field references, unaffected by name changes.


When choosing an OData endpoint, also consider the following:
  * If your reports rely on stable field identifiers, use BookmarkDataService.svc to prevent issues when field names change.
  * If you prioritize readability and work mainly within Microsoft Power BI or Tableau without merging external data, BookmarkService.svc is the simpler option.
  * If you're unsure, test both endpoints to determine which best fits your workflow.


**Note**
Single and multi-select values for any field are always displayed with their internal technical key (for example, category_1 instead of the label Category 1).
