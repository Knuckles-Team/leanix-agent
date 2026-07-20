---
name: leanix-enterprise-architecture-operations
description: >-
  Operate LeanIX enterprise architecture through the governed leanix-agent MCP
  and GraphOS surfaces. Use when Codex must inventory or resolve FactSheets,
  traverse or aggregate the Pathfinder GraphQL model, run bounded read/change
  workflows, synchronize authoritative LeanIX records into epistemic-graph with
  provenance, inspect impacts or data quality, or troubleshoot LeanIX
  authentication, AgentConfig, and mandatory TLS-profile configuration.
---

# Operate LeanIX Enterprise Architecture

Use the governed `leanix-agent` MCP surface through GraphOS delegation.

## Workflow

1. Resolve the runtime connection, authentication, and TLS profile from
   [configuration and TLS](references/configuration-and-tls.md).
2. Discover the current condensed tool surface before selecting a tool; do not
   assume a generated tool name or schema is unchanged.
3. Choose the narrowest procedure: [FactSheet inventory](references/factsheet-inventory.md),
   [Pathfinder GraphQL](references/pathfinder-graphql.md), or
   [knowledge-graph ingestion](references/knowledge-graph-ingestion.md).
4. Read and bound the target set before any change. Require explicit approval
   for mutations or externally visible operations.
5. Page large reads with the returned opaque cursor. Synchronize through the
   signed connector preset and governed ChangeEnvelope path.
6. Verify counts, durable graph state, provenance, and trace evidence before
   reporting completion.

## Safety contract

- Never persist credentials, endpoint values, raw personal identifiers,
  workstation names, or local filesystem paths.
- Keep TLS verification enabled. Configure private trust, mTLS, and proxy policy
  only through an AgentConfig TLS profile or secret reference.
- Treat unknown tenant, ACL, schema, tool-contract, or graph-session state as a
  hard failure.
- Prefer typed read tools over raw GraphQL. Use GraphQL only for fields,
  relations, or aggregations the typed surface cannot provide.
- Reject unbounded queries and never place secret values in parameters, logs,
  traces, or graph properties.
