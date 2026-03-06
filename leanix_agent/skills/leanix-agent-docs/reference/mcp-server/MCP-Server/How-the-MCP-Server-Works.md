##  How the MCP Server Works
SAP LeanIX uses MCP to expose selected APIs as AI tools, making them understandable and invokable by AI applications. These tools are described in a structured, standardized format that includes descriptions, inputs, and output types. This setup enables large language models (LLMs) to facilitate the exposed APIs by using the structured metadata provided by MCP.
Here's an example scenario:
  1. An AI assistant asks, "What tools can I use?"
  2. The MCP server returns a list of capabilities in SAP LeanIX.
  3. The assistant can then invoke tools like "Get application by ID" or "List fact sheets with low completeness score" as part of its workflow.


This process aligns with current LLM architectures.
