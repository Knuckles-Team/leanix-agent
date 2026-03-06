##  Guidelines and Best Practices
There is no direct relation from the provider to the application because many companies see large parts of their landscape hosted in more complex setups than straightforward SaaS apps. The provider -> IT component -> application relation supports complex hosting structures, such as an application provided by Company A that you are running on servers by Company B. SaaS is simplified further by the reference catalog.
  * Leverage the reference catalog: SAP LeanIX will automatically add the respective providers when adding IT components from the reference catalog. SAP LeanIX has a catalog of 9000 providers. In addition, the catalog creates a standard nomenclature (hierarchy) for more complex providers, e.g., HP, Linux, etc.
  * Classify provider relationships. Classify the providers based on their strategic importance and the extent of their impact on your organization. Categorize vendors into different tiers based on dependency, spending, etc.
  * If you want to manage self-developed software applications, e.g., with the breakdown to microservices, we recommend modeling such internal engineering or developer teams as [organization with subtype team](https://help.sap.com/docs/leanix/ea/organization-modeling-guidelines?locale=en-US&state=PRODUCTION&version=CLOUD#loio275ba0157a441014bcd0f61d7839746c__organizations_fact_sheet_subtypes).


When you model the provider correctly, you can now leverage various reports, such as the provider cost report.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2743008b7a441014bc20fa5c6aec00d8_LowRes.png)
