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
### Reconciliation Logic
The scripts use reconciliation-based logic, meaning they:
  1. Query the current state of subscriptions.
  2. Determine the desired state based on related fact sheets.
  3. Add missing subscriptions and remove extras.


This approach ensures idempotency: running the automation multiple times produces the same correct result, regardless of which trigger was initiated.
### Processing Time
For fact sheets with many relations (for example, an application with more than 50 IT components), the script may take several seconds to complete as it processes each related fact sheet sequentially.
