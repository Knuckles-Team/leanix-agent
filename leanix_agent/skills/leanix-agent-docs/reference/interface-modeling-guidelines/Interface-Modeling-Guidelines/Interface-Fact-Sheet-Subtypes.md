##  Interface Fact Sheet Subtypes
In SAP LeanIX, there are three fact sheet subtypes for different categories of interfaces:
  * Logical interface
  * API
  * MCP server


**Tip**
For a step-by-step guide on creating fact sheet subtypes, refer to [Add Fact Sheet Subtypes](https://help.sap.com/docs/leanix/ea/configure-workspace-meta-model-v4?locale=en-US&state=PRODUCTION&version=CLOUD#loio27595ce97a4410149c60a90e0f529a04__add_fact_sheet_subtypes_to_several_fact_sheet_types).
### Logical Interface
A logical interface provides a clear and conceptual view of how data, services, or information flows between various components, applications, or systems within an IT landscape. Logical interfaces are ideal for modeling business-level interactions without specifying technical implementation details.
Logical interfaces are used to model:
  * Data flow between business applications
  * Communication patterns
  * Methods and protocols


Example: SAP LeanIX to SAP Signavio.
### API
APIs provide functionalities accessible to external applications, enabling communication and integration between different systems, such as microservices.
APIs are used to model:
  * System-to-system integrations
  * Microservice communication
  * Technical endpoints


Examples: Metrics API, Import API.
There is an option to model the relation between logical interfaces and the API subtype. APIs, as a subtype of interfaces, are most meaningful to model when the microservice subtype of applications is present. [Microservices](https://help.sap.com/docs/leanix/ea/application-modeling-guidelines?locale=en-US&state=PRODUCTION&version=CLOUD#loio275892ca7a441014ab86c9b2e6382a33__microservice "https://help.sap.com/docs/leanix/ea/application-modeling-guidelines?locale=en-US&state=PRODUCTION&version=CLOUD#loio275892ca7a441014ab86c9b2e6382a33__microservice") are an optional subtype not part of the standard meta model. Therefore, the relation between the API and logical interface subtypes is also an option, allowing you to adjust your modeling approach based on your specific architectural requirements.
In this context, a logical interface can be associated with multiple APIs, representing business interfaces and their corresponding technical implementations. To effectively capture these relationships, SAP LeanIX recommends two alternative approaches:
  * Business data flow using the logical interface subtype. If you focus on business-oriented data flow, you should model your connections using the logical interface. This approach involves linking applications and interfaces and provides a comprehensive view of how business processes interact with different applications through logical interfaces.
  * Technical data flow using the API subtype. Alternatively, if your architecture involves microservices, modeling the relationships through the API subtype offers a more technical perspective.


### MCP Server
MCP (Model Context Protocol) servers are managed communication endpoints that expose specific capabilities to AI applications or systems using standardized protocol interfaces. They act as intermediaries for data exchange and tool orchestration.
MCP servers are used to model:
  * Intelligent agent interactions
  * Protocol-based communication
  * Endpoints and access controls


Examples: Microsoft Graph FastMCP, SAP UI5 MCP Server
