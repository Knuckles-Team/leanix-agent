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
  1. Query the current state of business context relations on the parent.
  2. Query all child applications and their business context relations.
  3. Determine the desired state (union of all children's business contexts).
  4. Add missing business contexts, update descriptions for existing business contexts, and remove inherited business contexts that no child has.


This approach ensures idempotency: running the automation multiple times produces the same correct result, regardless of which trigger was initiated.
### Inherited Relation Marking
Inherited relations are marked with a description in the format: [Auto-inherited from: Child App 1, Child App 2]. This marking:
  * Distinguishes inherited relations from manually-added ones.
  * Tracks which children contributed to each business context.
  * Allows the automation to know which relations it should manage.
  * Preserves any manually-added business context relations on the parent.


### Processing Time
  * For applications with many children or business contexts, the script may take several seconds to complete.
  * Automation 4 (catch-all) queries all applications with inherited business context relations, which may take longer in large workspaces but guarantees correctness.
