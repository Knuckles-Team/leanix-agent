##  Automation 1: Lifecycle Phase Is Reached
When an initiative reaches End of Life, this automation breaks quality seals on all related applications. Lifecycle changes are checked nightly, not in real-time.
Automation Configuration Parameter | Configuration
---|---
Trigger (When) |
  * Fact Sheet Type: Initiative
  * Event: Lifecycle state is reached
  * Lifecycle Phase: End of Life
  * Days Before/After: 0


Conditions (If) | Configure optional conditions for the automation.
Actions (Then) | Run Script: See the sample code provided below.


**Sample Code**

```
/**
 * Break Quality Seal on Initiative End of Life
 *
 * When an Initiative reaches "End of Life" lifecycle phase,
 * this script breaks the quality seal on all related Applications.
 *
 * Trigger (on Initiative):
 *   - Lifecycle state is reached: End of Life
 *
 * Logic:
 *   1. Query the Initiative and its related Applications
 *   2. For each Application, set quality seal to BROKEN
 *   3. Skip if already broken (idempotent)
 */

export async function main() {
  const initiativeId = data?.factSheet?.id;
  if (!initiativeId || data?.factSheet?.type !== "Initiative") return {};

  const token = context?.secrets?.["default_automations_secret"]?.value?.bearerToken;
  if (!token) throw new Error("ABORT AUTOMATION RUN - Missing bearerToken");

  const graphqlUrl = "https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/graphql";

  // Query the Initiative and its related Applications
  const query = `query ($id: ID!) {
    factSheet(id: $id) {
      id name
      ... on Initiative {
        relInitiativeToApplication {
          edges {
            node {
              factSheet {
                id name rev type
                lxState
              }
            }
          }
        }
      }
    }
  }`;

  const res = await fetch(graphqlUrl, {
    method: "POST",
    headers: { Authorization: `Bearer ${token}", "Content-Type": "application/json" },
    body: JSON.stringify({ query, variables: { id: initiativeId } }),
  });

  const json = await res.json();
  if (json?.errors) throw new Error(`GraphQL failed: ${JSON.stringify(json.errors)}`);

  const initiative = json?.data?.factSheet;
  if (!initiative) return {};

  // Get related Applications
  const applications = (initiative.relInitiativeToApplication?.edges || [])
    .map(e => e?.node?.factSheet)
    .filter(app => app && app.type === "Application");

  if (applications.length === 0) return {};

  // Break quality seal on each Application
  for (const app of applications) {
    // Skip if already broken (idempotent)
    if (app.lxState === "BROKEN_QUALITY_SEAL") continue;

    const mutationRes = await fetch(graphqlUrl, {
      method: "POST",
      headers: { Authorization: `Bearer ${token}", "Content-Type": "application/json" },
      body: JSON.stringify({
        query: `mutation ($id: ID!, $rev: Long!, $patches: [Patch]!) {
          updateFactSheet(id: $id, rev: $rev, patches: $patches, validateOnly: false) {
            factSheet { id rev lxState }
          }
        }`,
        variables: {
          id: app.id,
          rev: app.rev,
          patches: [{
            op: "replace",
            path: "/lxState",
            value: "BROKEN_QUALITY_SEAL",
          }],
        },
      }),
    });

    const mutationJson = await mutationRes.json();
    if (mutationJson?.errors) {
      // Continue with other Applications on error
      continue;
    }
  }

  return {};
}

```



