##  Technical Details
### Endpoint
The scripts call the GraphQL API endpoint to update fact sheet data.

```
/services/pathfinder/v1/graphql
```



### Authentication
The automation requires access to the SAP LeanIX GraphQL API. An API token needed for authentication is generated automatically. This secret is referenced in automation scripts through context.secrets.
### Idempotency
The scripts check the current quality seal state before updating and skip applications already in BROKEN_QUALITY_SEAL state. This ensures that running the automation multiple times produces the same correct result.
### Date Validation
For automation 2, the script validates that the initiative's End of Life date has been reached before breaking quality seals.
### Processing Time
For fact sheets with many relations (for example, an initiative with more than 50 applications), the script may take several seconds to complete as it processes each related application sequentially.
