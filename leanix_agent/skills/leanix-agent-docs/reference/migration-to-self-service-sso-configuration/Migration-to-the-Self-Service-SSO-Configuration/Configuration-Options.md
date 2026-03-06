##  Configuration Options
(Recommended) Option 1: Dedicated IdP Applications per Workspace | Option 2: Shared IdP Application Across Multiple Workspaces
---|---
![Diagram showing each SAP LeanIX workspace \(production, sandbox, and test\) connected to its own dedicated IdP application.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio071fdfaa1a2740e98fdd30299981c264_LowRes.png) Dedicated IdP Applications per Workspace Each SAP LeanIX workspace connects to its own IdP application. |  ![Diagram showing multiple SAP LeanIX workspaces \(production, sandbox, and test\) connected to the same IdP application.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio4f83181d68c141af9665acbf69123734_LowRes.png) Shared IdP Application Across Multiple Workspaces Multiple SAP LeanIX workspaces connect to the same IdP application. Note that some identity providers may not support multiple entity IDs and reply (ACS) URLs.


