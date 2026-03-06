##  Automation 3: Child Unlinked from Parent (Parent Side)
This automation handles the case when a child application is unlinked from its parent, triggered on the parent application. When the relToChild relation is removed from the parent side, we need to reconcile the parent's inherited business contexts based on the remaining children.
Automation Configuration Parameter | Configuration
---|---
Trigger (When) |
  * Fact Sheet Type: Application
  * Event: Relation is removed
  * Fact Sheet Relation: Children


Conditions (If) | Configure optional conditions for the automation.
Actions (Then) | Run Script: See the sample code provided below.


**Sample Code**

```
/**
 * Business Context Cleanup on Child Unlink
 *
 * When a child Application is unlinked from its parent, this script
 * reconciles the parent's inherited Business Contexts based on remaining children.
 */

const INHERITED_MARKER = "[Auto-inherited from:";
const INHERITED_MARKER_END = "]";

function buildInheritedDescription(childNames) {
  return `${INHERITED_MARKER} ${childNames.join(", ")}${INHERITED_MARKER_END}`;
}

function isInheritedRelation(description) {
  return description && description.includes(INHERITED_MARKER);
}

export async function main() {
  const parentId = data?.factSheet?.id;
  if (!parentId || data?.factSheet?.type !== "Application") return {};

  const token = context?.secrets?.["default_automations_secret"]?.value?.bearerToken;
  if (!token) throw new Error("ABORT AUTOMATION RUN - Missing bearerToken");

  const graphqlUrl = "https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/graphql";

  // Query parent with remaining children and their BCs
  const query = `query ($id: ID!) {
    factSheet(id: $id) {
      id name rev type
      ... on Application {
        relApplicationToBusinessContext {
          edges {
            node {
              id
              description
              factSheet { id name }
            }
          }
        }
        relToChild {
          edges {
            node {
              factSheet {
                id name type
                ... on Application {
                  relApplicationToBusinessContext {
                    edges { node { factSheet { id name } } }
                  }
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
    body: JSON.stringify({ query, variables: { id: parentId } }),
  });

  const json = await res.json();
  if (json?.errors) throw new Error(`GraphQL failed: ${JSON.stringify(json.errors)}`);

  const parent = json?.data?.factSheet;
  if (!parent) return {};

  let currentRev = parent.rev;

  // Collect all BCs from remaining children
  const desiredBCs = new Map();
  const children = (parent.relToChild?.edges || [])
    .map(e => e?.node?.factSheet)
    .filter(c => c && c.type === "Application");

  for (const child of children) {
    const childBCs = (child.relApplicationToBusinessContext?.edges || [])
      .map(e => e?.node?.factSheet)
      .filter(Boolean);
    for (const bc of childBCs) {
      if (desiredBCs.has(bc.id)) {
        desiredBCs.get(bc.id).childNames.push(child.name);
      } else {
        desiredBCs.set(bc.id, { id: bc.id, name: bc.name, childNames: [child.name] });
      }
    }
  }

  // Find inherited BC relations to update or remove
  const parentBCRelations = (parent.relApplicationToBusinessContext?.edges || [])
    .map(e => e?.node)
    .filter(Boolean);

  for (const rel of parentBCRelations) {
    const bcId = rel.factSheet?.id;
    if (!bcId) continue;
    if (!isInheritedRelation(rel.description)) continue;

    // If no remaining child has this BC, remove it
    if (!desiredBCs.has(bcId)) {
      const removeRes = await fetch(graphqlUrl, {
        method: "POST",
        headers: { Authorization: `Bearer ${token}", "Content-Type": "application/json" },
        body: JSON.stringify({
          query: `mutation ($id: ID!, $rev: Long!, $patches: [Patch]!) {
            updateFactSheet(id: $id, rev: $rev, patches: $patches, validateOnly: false) {
              factSheet { id rev }
            }
          }`,
          variables: {
            id: parent.id,
            rev: currentRev,
            patches: [{
              op: "remove",
              path: `/relApplicationToBusinessContext/${rel.id}`,
            }],
          },
        }),
      });

      const removeJson = await removeRes.json();
      if (removeJson?.errors) throw new Error(`Remove BC failed: ${JSON.stringify(removeJson.errors)}`);
      currentRev = removeJson?.data?.updateFactSheet?.factSheet?.rev ?? currentRev;
      continue;
    }

    // Update description if child names have changed
    const bc = desiredBCs.get(bcId);
    const newDescription = buildInheritedDescription(bc.childNames);
    if (rel.description === newDescription) continue;

    const updateRes = await fetch(graphqlUrl, {
      method: "POST",
      headers: { Authorization: `Bearer ${token}", "Content-Type": "application/json" },
      body: JSON.stringify({
        query: `mutation ($id: ID!, $rev: Long!, $patches: [Patch]!) {
          updateFactSheet(id: $id, rev: $rev, patches: $patches, validateOnly: false) {
            factSheet { id rev }
          }
        }`,
        variables: {
          id: parent.id,
          rev: currentRev,
          patches: [{
            op: "replace",
            path: `/relApplicationToBusinessContext/${rel.id}`,
            value: JSON.stringify({
              factSheetId: bcId,
              description: newDescription,
            }),
          }],
        },
      }),
    });

    const updateJson = await updateRes.json();
    if (updateJson?.errors) throw new Error(`Update BC failed: ${JSON.stringify(updateJson.errors)}`);
    currentRev = updateJson?.data?.updateFactSheet?.factSheet?.rev ?? currentRev;
  }

  return {};
}
```



