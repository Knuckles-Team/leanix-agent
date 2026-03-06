##  Automation 1: Relation Is Added (Business Context to Child)
Automation Configuration Parameter | Configuration
---|---
Trigger (When) |
  * Fact Sheet Type: Application
  * Event: Relation is added
  * Fact Sheet Relation: Business contexts


Conditions (If) | Configure optional conditions for the automation.
Actions (Then) | Run Script: See the sample code provided below.


**Sample Code**

```
/**
 * Business Context Propagate to Parent - Full Reconciliation
 *
 * Propagates Business Context relations from child Applications to parent Applications.
 * When a BC is linked to a child, the parent should also have that BC.
 * When a BC is removed from all children, it should be removed from the parent.
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
  const appId = data?.factSheet?.id;
  if (!appId || data?.factSheet?.type !== "Application") return {};

  const token = context?.secrets?.["default_automations_secret"]?.value?.bearerToken;
  if (!token) throw new Error("ABORT AUTOMATION RUN - Missing bearerToken");

  const graphqlUrl = "https://{SUBDOMAIN}.leanix.net/services/pathfinder/v1/graphql";

  // Step 1: Query this Application and its parent
  const appQuery = `query ($id: ID!) {
    factSheet(id: $id) {
      id name type
      ... on Application {
        relToParent { edges { node { factSheet { id name rev type } } } }
        relApplicationToBusinessContext { edges { node { factSheet { id name } } } }
      }
    }
  }`;

  const appRes = await fetch(graphqlUrl, {
    method: "POST",
    headers: { Authorization: `Bearer ${token}", "Content-Type": "application/json" },
    body: JSON.stringify({ query: appQuery, variables: { id: appId } }),
  });

  const appJson = await appRes.json();
  if (appJson?.errors) throw new Error(`GraphQL failed: ${JSON.stringify(appJson.errors)}`);

  const app = appJson?.data?.factSheet;
  if (!app) return {};

  // Get parent Application
  const parentEdges = (app.relToParent?.edges || []).map(e => e?.node?.factSheet).filter(Boolean);
  const parent = parentEdges.find(p => p.type === "Application");
  if (!parent) return {}; // No parent Application, nothing to do

  // Step 2: Query parent with all its children and their BCs
  const parentQuery = `query ($id: ID!) {
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

  const parentRes = await fetch(graphqlUrl, {
    method: "POST",
    headers: { Authorization: `Bearer ${token}", "Content-Type": "application/json" },
    body: JSON.stringify({ query: parentQuery, variables: { id: parent.id } }),
  });

  const parentJson = await parentRes.json();
  if (parentJson?.errors) throw new Error(`GraphQL failed: ${JSON.stringify(parentJson.errors)}`);

  const parentFs = parentJson?.data?.factSheet;
  if (!parentFs) throw new Error("ABORT AUTOMATION RUN - Parent not found");

  let currentRev = parentFs.rev;

  // Step 3: Collect all BCs from all children (desired state)
  const desiredBCs = new Map(); // bcId -> { id, name, childNames: string[] }
  const children = (parentFs.relToChild?.edges || [])
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

  // Step 4: Get parent's current BC relations
  const parentBCRelations = (parentFs.relApplicationToBusinessContext?.edges || [])
    .map(e => e?.node)
    .filter(Boolean);

  // Separate inherited vs manually-added relations
  const inheritedRelations = new Map();
  const manualRelations = new Set();

  for (const rel of parentBCRelations) {
    const bcId = rel.factSheet?.id;
    if (!bcId) continue;

    if (isInheritedRelation(rel.description)) {
      inheritedRelations.set(bcId, {
        relationId: rel.id,
        bcId: bcId,
        bcName: rel.factSheet.name,
        description: rel.description,
      });
    } else {
      manualRelations.add(bcId);
    }
  }

  // Step 5: Add missing BCs to parent
  for (const [bcId, bc] of desiredBCs) {
    if (manualRelations.has(bcId)) continue;

    const newDescription = buildInheritedDescription(bc.childNames);

    if (inheritedRelations.has(bcId)) {
      const existing = inheritedRelations.get(bcId);
      if (existing.description === newDescription) continue;

      // Update the relation description with new child names
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
            id: parentFs.id,
            rev: currentRev,
            patches: [{
              op: "replace",
              path: `/relApplicationToBusinessContext/${existing.relationId}`,
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
      continue;
    }

    // Add new BC relation to parent
    const addRes = await fetch(graphqlUrl, {
      method: "POST",
      headers: { Authorization: `Bearer ${token}", "Content-Type": "application/json" },
      body: JSON.stringify({
        query: `mutation ($id: ID!, $rev: Long!, $patches: [Patch]!) {
          updateFactSheet(id: $id, rev: $rev, patches: $patches, validateOnly: false) {
            factSheet { id rev }
          }
        }`,
        variables: {
          id: parentFs.id,
          rev: currentRev,
          patches: [{
            op: "add",
            path: `/relApplicationToBusinessContext/new_${bcId}`,
            value: JSON.stringify({
              factSheetId: bcId,
              description: newDescription,
            }),
          }],
        },
      }),
    });

    const addJson = await addRes.json();
    if (addJson?.errors) throw new Error(`Add BC failed: ${JSON.stringify(addJson.errors)}`);
    currentRev = addJson?.data?.updateFactSheet?.factSheet?.rev ?? currentRev;
  }

  // Step 6: Remove inherited BCs that no child has anymore
  for (const [bcId, rel] of inheritedRelations) {
    if (desiredBCs.has(bcId)) continue;

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
          id: parentFs.id,
          rev: currentRev,
          patches: [{
            op: "remove",
            path: `/relApplicationToBusinessContext/${rel.relationId}`,
          }],
        },
      }),
    });

    const removeJson = await removeRes.json();
    if (removeJson?.errors) throw new Error(`Remove BC failed: ${JSON.stringify(removeJson.errors)}`);
    currentRev = removeJson?.data?.updateFactSheet?.factSheet?.rev ?? currentRev;
  }

  return {};
}
```



