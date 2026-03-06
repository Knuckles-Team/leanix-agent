##  How to Model MCP Servers
MCP servers facilitate secure communication and coordinate interactions between systems. To effectively represent these servers in your system landscape, it’s important to clarify how information flows between your applications through these interfaces.
We recommend documenting the following:
  * MCP server endpoint: Enter the URL used to reach the MCP server. This serves as a concrete reference to the integration point, allowing technical teams to locate and manage connections.
  * Authentication: Specify the protocols used for authentication, such as OAuth 2.0 or API key. This helps evaluate the security of the interface and whether it meets organizational standards.
  * MCP server classification: Indicate whether the MCP server provides read-only access or supports write operations. This determines the level of interaction permitted and helps identify potential risks or limitations.
  * Authorized tools: List the tools and systems the MCP server is permitted to interact with. This clarifies the server’s role in the broader ecosystem and supports dependency mapping.
  * MCP server type: Define whether the communication is local (within the same environment) or remote (across environments). This can affect decisions related to latency, performance, and security.


Once you populate these fields, you can model MCP servers similarly to REST APIs: a provider application, an interface (representing the MCP server), and a consumer application.
Example of Modeling MCP Servers
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio44706c24f356494397552f41baff71da_LowRes.png)
