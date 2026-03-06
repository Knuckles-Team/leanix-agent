##  Automation 2: Relation Is Added
When an application is linked to an initiative that has already reached its End of Life, automation 1 is not activated because the End of Life date is in the past. Automation 2 checks all initiatives linked to the application and breaks the quality seal if any initiative is already at End of Life.
Automation Configuration Parameter | Configuration
---|---
Trigger (When) |
  * Fact Sheet Type: Application
  * Event: Relation is added
  * Fact Sheet Relation: Initiative


Conditions (If) | Configure optional conditions for the automation.
Actions (Then) | Run Script: See the sample code provided below.


**Sample Code**

```
/**
 * Check Initiative EOL When Application Relation Added
 *
 * When an Initiative is added to an Application (relation added), check if the
 * linked Initiative has reached End of Life and break the Application's quality
 * seal if needed.
 *
 * Trigger (on Application):
 *   - Relation is added
 *
 * Logic:
 *   1. Query the Application and ALL its related Initiatives (with lifecycle)
 *   2. Check if ANY Initiative has reached End of Life (date validation)
 *   3. Break quality seal if ANY Initiative is at EOL and seal not already broken
 */

export async function main() {
  const appId = data?.factSheet?.id;
  if (!appId || data?.factSheet?.type !== "Application") return {};

  const token = context?.secrets?.["default_automations_secret"]?.value?.bearerToken;
  if (!token) throw new Error("ABORT AUTOMATION RUN - Missing bearerToken");

  const graphqlUrl = "https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/graphql";

  // Query the Application with ALL related Initiatives and their lifecycle phases
  const query = `query ($id: ID!) {
    factSheet(id: $id) {
      id name rev type
      lxState
      ... on Application {
        relApplicationToInitiative {
          edges {
            node {
              factSheet {
                id name type
                ... on Initiative {
                  lifecycle { phases { phase startDate } }
                }
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
    body: JSON.stringify({ query, variables: { id: appId } }),
  });

  const json = await res.json();
  if (json?.errors) throw new Error(`GraphQL failed: ${JSON.stringify(json.errors)}`);

  const app = json?.data?.factSheet;
  if (!app) return {};

  // Check if seal is already broken - no action needed
  if (app.lxState === "BROKEN_QUALITY_SEAL") return {};

  // Get all related Initiatives
  const initiatives = (app.relApplicationToInitiative?.edges || [])
    .map(e => e?.node?.factSheet)
    .filter(Boolean);

  if (initiatives.length === 0) return {};

  // Helper function to check if Initiative has reached EOL
  const isEOLReached = (lifecycle) => {
    const eolPhase = lifecycle?.phases?.find(p => p.phase === "endOfLife");
    if (!eolPhase?.startDate) return false;
    const eolDate = new Date(eolPhase.startDate + "T00:00:00Z");
    const today = new Date();
    today.setUTCHours(0, 0, 0, 0);
    return today >= eolDate;
  };

  // Check if ANY Initiative has reached EOL
  const anyInitiativeAtEOL = initiatives.some(init => isEOLReached(init.lifecycle));

  // If no Initiative is at EOL, no action needed
  if (!anyInitiativeAtEOL) return {};

  // Break the quality seal
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
    throw new Error(`Mutation failed: ${JSON.stringify(mutationJson.errors)}`);
  }

  return {};
}

```



