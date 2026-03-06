##  AI Agent Fact Sheet Subtype
New subsection AI Agent Details (A2A) with the following attributes:
Attribute | Type | Description
---|---|---
AI Agent Service Endpoint | Text | URL to reach the AI agent.
A2A Capabilities | Text | Supported A2A protocol features like streaming or push notifications.
Authentication | Single-select | Authentication method for accessing the agent's endpoint.
Other Authentication | Text | Conditional attribute upon selecting “Other“ for “Authentication.”
Skills | Text area | Specific capability, function, or area of expertise the agent can perform or address.


New subsection MCP Server with the following attributes:
Attribute | Type | Description
---|---|---
MCP Server Support | Single-select | Select whether the agent or application can be accessed via an MCP server.
MCP Server Endpoint | Text | URL to reach the MCP server.
MCP Server Classification | Single-select | Indicate whether the MCP server queries data or has writing permissions.


New subsection AI Governance and Adoption with the following attributes:
Attribute | Type | Description
---|---|---
AI Agent Type | Single-select | Categorize agents based on how they interact with users, whether through direct conversation or by performing tasks autonomously in the background.
AI Agent Nature | Single-select | Configuration mode of the agent, whether it was custom, pre-built, or pre-built expanded.
AI Risk | Single-select | Assessment of threats to the safety, livelihoods, and rights of people according to the EU AI Act.
Approval State | Single-select | Agent's approval state.


New subsection AI Agent Business Value with the following attributes:
Attribute | Type | Description
---|---|---
Type of Business Value | Multi-select | Business value type that best describes the agent’s primary benefit.
Usage | Integer | Quantified agent's usage, for example, based on users, session runs, sent messages, or any other relevant metric.
Cost Savings per Unit (Conditional based on type) | Double, displayed as costs | Attribute value is an input field for the new calculation of Total Expected Cost Savings.
Revenue Increase per Unit (Conditional based on type) | Double, displayed as costs | Attribute value is an input field for the new calculation of Total Expected Revenue Increase.
Risk Reduction per Unit (Conditional based on type) | Double, displayed as costs | Attribute value is an input field for the new calculation of Total Expected Risk Reduction.


New subsection AI Agent Business Value Summary with the following attributes. These attributes are automatically calculated. For details, see [Calculations for AI Agents](https://help.sap.com/docs/leanix/ea/calculations-for-ai-agents?locale=en-US&state=PRODUCTION&version=CLOUD "Automatically calculate the business value of your AI agents.").
Attribute | Type | Description
---|---|---
Total Expected Cost Savings (Conditional based on type) | Double, displayed as costs |  The value is automatically computed from other fields' values: Usage x Cost Savings per Unit = Total Expected Cost Savings
Total Expected Revenue Increase (Conditional based on type) | Double, displayed as costs |  The value is automatically computed from other fields' values: Usage x Revenue Increase per Unit = Total Expected Risk Reduction
Total Expected Risk Reduction (Conditional based on type) | Double, displayed as costs |  The value is automatically computed from other fields' values: Usage x Risk Reduction per Unit = Total Expected Revenue Increase


