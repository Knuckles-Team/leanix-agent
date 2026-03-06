##  Automation 4: Child Removes Parent Relation (Catch-All)
This automation handles the edge case when a child application removes its own parent relation. Since the child can no longer see its former parent, this script queries all applications with inherited business context relations and reconciles them.
When a child removes relToParent, the trigger initiates on the child, but it can no longer see its former parent. This script queries all applications with inherited business context relations and reconciles each one based on their current children.
Automation Configuration Parameter | Configuration
---|---
Trigger (When) |
  * Fact Sheet Type: Application
  * Event: Relation is removed
  * Fact Sheet Relation: Parent


Conditions (If) | Configure optional conditions for the automation.
Actions (Then) | Run Script: See the sample code provided below.


**Sample Code**

```
/**
 * Business Context Reconcile All Parents (Catch-All)
 *
 * When a child Application removes its parent relationship (relToParent),
 * we can no longer see the former parent. This script reconciles ALL parent
 * Applications to ensure inherited BCs are correct.
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

  // Check if this app still has a parent - if so, the normal script handles it
  const checkQuery = `query ($id: ID!) {
    factSheet(id: $id) {
      id
      ... on Application {
        relToParent { edges { node { factSheet { id type } } } }
      }
    }
  }`;

  const checkRes = await fetch(graphqlUrl, {
    method: "POST",
    headers: { Authorization: `Bearer ${token}", "Content-Type": "application/json" },
    body: JSON.stringify({ query: checkQuery, variables: { id: appId } }),
  });

  const checkJson = await checkRes.json();
  if (checkJson?.errors) throw new Error(`GraphQL failed: ${JSON.stringify(checkJson.errors)}`);

  const hasParent = (checkJson?.data?.factSheet?.relToParent?.edges || [])
    .some(e => e?.node?.factSheet?.type === "Application");

  // If still has a parent, the normal bc-propagate-to-parent.js handles it
  if (hasParent) return {};

  // This app no longer has a parent - reconcile ALL parent Applications
  const allAppsQuery = `query ($first: Int!, $after: String) {
    allFactSheets(
      first: $first
      after: $after
      filter: { facetFilters: [{ facetKey: "FactSheetTypes", keys: ["Application"] }] }
    ) {
      pageInfo { hasNextPage endCursor }
      edges {
        node {
          id name rev
          ... on Application {
            relToChild {
              edges { node { factSheet { id name type } } }
            }
            relApplicationToBusinessContext {
              edges {
                node {
                  id description
                  factSheet { id name }
                }
              }
            }
          }
        }
      }
    }
  }`;

  // Find all Applications that have inherited BC relations
  let potentialParents = [];
  let hasMore = true;
  let after = null;

  while (hasMore) {
    const res = await fetch(graphqlUrl, {
      method: "POST",
      headers: { Authorization: `Bearer ${token}", "Content-Type": "application/json" },
      body: JSON.stringify({
        query: allAppsQuery,
        variables: { first: 100, after },
      }),
    });

    const json = await res.json();
    if (json?.errors) throw new Error(`GraphQL failed: ${JSON.stringify(json.errors)}`);

    const page = json?.data?.allFactSheets;
    const apps = (page?.edges || []).map(e => e?.node).filter(Boolean);

    for (const app of apps) {
      const bcRels = (app.relApplicationToBusinessContext?.edges || [])
        .map(e => e?.node)
        .filter(Boolean);

      const hasInheritedBCs = bcRels.some(rel => isInheritedRelation(rel.description));

      if (hasInheritedBCs) {
        potentialParents.push(app);
      }
    }

    hasMore = page?.pageInfo?.hasNextPage || false;
    after = page?.pageInfo?.endCursor || null;
  }

  if (potentialParents.length === 0) return {};

  // Reconcile each potential parent
  for (const parent of potentialParents) {
    const parentQuery = `query ($id: ID!) {
      factSheet(id: $id) {
        id name rev
        ... on Application {
          relApplicationToBusinessContext {
            edges {
              node {
                id description
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
    if (parentJson?.errors) continue;

    const parentFs = parentJson?.data?.factSheet;
    if (!parentFs) continue;

    let currentRev = parentFs.rev;

    // Collect all BCs from CURRENT children
    const desiredBCs = new Map();
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

    // Check parent's inherited BCs
    const parentBCRelations = (parentFs.relApplicationToBusinessContext?.edges || [])
      .map(e => e?.node)
      .filter(Boolean);

    for (const rel of parentBCRelations) {
      const bcId = rel.factSheet?.id;
      if (!bcId) continue;
      if (!isInheritedRelation(rel.description)) continue;

      // If no child has this BC anymore, remove it
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
              id: parentFs.id,
              rev: currentRev,
              patches: [{ op: "remove", path: `/relApplicationToBusinessContext/${rel.id}` }],
            },
          }),
        });

        const removeJson = await removeRes.json();
        if (removeJson?.errors) continue;
        currentRev = removeJson?.data?.updateFactSheet?.factSheet?.rev ?? currentRev;
        continue;
      }

      // Update description if child names changed
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
            id: parentFs.id,
            rev: currentRev,
            patches: [{
              op: "replace",
              path: `/relApplicationToBusinessContext/${rel.id}`,
              value: JSON.stringify({ factSheetId: bcId, description: newDescription }),
            }],
          },
        }),
      });

      const updateJson = await updateRes.json();
      if (updateJson?.errors) continue;
      currentRev = updateJson?.data?.updateFactSheet?.factSheet?.rev ?? currentRev;
    }
  }

  return {};
}
```



