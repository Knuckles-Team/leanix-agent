##  Prioritization of Discovered SaaS Items
Discovered items are assigned a priority score and categorized into 3 priority levels: low, medium, and high. This helps you quickly identify and focus on the most critical and relevant discovered items in your inbox, especially when dealing with large data volumes.
Priority levels are determined by score ranges: 1-60 (low), 61-90 (medium), and 91-100 (high), with the priority score calculated based on the following criteria:
  * The number of applications in the same category
  * The usage indication of an application:
    * Unique active users for Zscaler and MDCA integrations
    * Number of sign-ins for Entra ID integration
  * The average business criticality rating for that application across global customer workspaces
  * The average functional fit rating for that application across global customer workspaces


Click on a discovered item to open the side panel and select the Priority tab to see the detailed breakdown of the score. If an application lacks data for one criterion, it is marked with the Missing Data label. However, the priority score will still be calculated based on other available criteria that provide the needed information.
Missing data could be for the following reasons:
  * Usage indication: The integration does not provide usage data (Okta, Netskope), or you have disabled usage indication in the configuration.
  * Average business criticality/functional fit: Fewer than 5 customers have rated the application, making the sample size too small for assessment.


![Priority Tab on the Side Panel Detailing the Priority Score](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274dadb37a44101485ebf4b682f1d90f_LowRes.png)
Priority Tab on the Side Panel Detailing the Priority Score
