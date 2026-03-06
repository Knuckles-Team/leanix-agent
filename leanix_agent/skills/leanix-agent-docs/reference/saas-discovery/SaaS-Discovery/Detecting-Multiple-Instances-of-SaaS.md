##  Detecting Multiple Instances of SaaS
SaaS Discovery detects multiple instances of the same SaaS across different SSO systems. Currently, it is supported for Entra ID and Okta integrations.
Multiple instances of SaaS are often used to support regional requirements, to separate data of different legal entities of the same company, or to facilitate the use of test systems alongside production systems. Also, in situations like mergers and acquisitions, managing multiple instances becomes crucial. Therefore, identifying these instances is important for Enterprise Architects, as knowing about their existence can influence application rationalization efforts.
SAP LeanIX SaaS discovery identifies SaaS instances by examining Application IDs, External IDs, and External names used in the SSOs. When multiple SaaS instances share the same application IDs, the unique external IDs and external names are used to distinguish the service instances. External IDs are unique IDs assigned by the SSO for each service instance, while external names are manually assigned names in the SSO.
To help identify different instances, the external name is displayed below the name of the discovered SaaS item in the SaaS discovery inbox.
![Multiple Instances of Same SaaS Listed in Discovery Inbox](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274991637a4410148a31c5873501db8d_LowRes.png)
Multiple Instances of the Same SaaS Listed in the SaaS Discovery Inbox
You can view the external ID by opening the side panel when clicking on a SaaS item. In the example below, the first discovery item appears to be a dedicated development instance, while the latter is the production instance. These instances can now be linked to two different fact sheets if necessary. Alternatively, if instances don't play a big role in your workspace, you can link them to the same fact sheet.
![Discovered SaaS Item’s Detail Showing External ID](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274aca077a441014b9c48a0d8602f315_LowRes.png)
Discovered SaaS Item’s Detail Showing External ID
![Discovered SaaS Item’s Detail Showing External ID](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274bb2e57a4410149346b99146dea12b_LowRes.png)
Discovered SaaS Item’s Detail Showing External ID
**Note**
The auto-link feature operates on a first-come, first-served basis. This means when multiple SaaS instances have the same application IDs, the first item that exactly matches with the name of the fact sheet is linked. The matching is based on the external name.
