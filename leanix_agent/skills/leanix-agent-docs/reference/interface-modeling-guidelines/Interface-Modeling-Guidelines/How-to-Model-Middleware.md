##  How to Model Middleware
Modeling middleware, for example, integration platforms such as MuleSoft and Dell Boomi, in SAP LeanIX lets you gain the following insights:
  * Understand which interfaces depend on their integration platform.
  * Identify which connection methods (for example, FTP, HTTPS, etc.) are used.
  * Specify a different connection method for the same interface for each application connected to the interface (for example, FTP for application 1 and HTTPS for application 2).


There are two different approaches you can choose from:
### Recommended Approach
  1. Add the attribute Connection Method as a field on relation between your interface and application fact sheet types.
  2. Establish the interface and necessary application relations.
  3. Model the integration platform as an IT component attached to the interface.
  4. Specify a connection method for each interface-application relation.

![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2751e6447a441014b738da3e1e116d87_LowRes.png)
Here, you can see the data flow between the applications AC Management and HR Admin. You can see that the applications AC Management and HR Admin share a data object called "Customer," using the interface "AC Management to HR Admin" via the IT component "MuleSoft."
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274e17ce7a441014905ef51b19f1cd42_LowRes.png)
Though this method is a lean, low-effort way to document the connection method, you can't visualize the connection method"as a field on relation in diagrams and reports.
If representing the connection method is more relevant to you, the next approach may be more suitable. It uses a custom field to capture the connection method on the interface fact sheet. However, this comes with the trade-off of an increased number of interface fact sheets, which requires more maintenance
### Connection-Focused Approach
This approach creates two interfaces to accommodate a different connection method. You would model the interface this way because two different applications might require two different data flows.
  1. Add a Connection Method attribute on the interface fact sheet.
  2. Create two interfaces, one for each connection method.
  3. Model the integration platform as an IT component attached to each interface.

![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275406d27a441014bf4d954fe7779263_LowRes.png)
You can see that the data flow between the applications is differentiated by the interface AC Management to HR Admin and HR Admin to AC Management.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275185cf7a44101498d1cf5d26634942_LowRes.png)
