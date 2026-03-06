##  SAP S/4HANA Modeling Best Practices and Guidelines
Modeling SAP S/4HANA is not too different compared to modeling [SAP ERP 6.0](https://help.sap.com/docs/leanix/ea/modeling-sap-erp-60?locale=en-US&state=PRODUCTION&version=CLOUD "Learn key approaches for modeling SAP ERP 6.0, including product versions, software components, technical components, and interfaces, as well as modeling system instances, such as local customizations."):
  * Use level-1 applications to represent S/4HANA or S/4HANA Cloud and level-2 applications to represent the lines of business, such as Finance, Sourcing and Procurement, and Marketing—similar to how SAP modules are modeled as level-2 applications in ERP 6.0.
  * A key difference in S/4HANA is the addition of Fiori apps. The best practice is to only model custom Fiori applications and including them as level-3 applications in SAP LeanIX.
  * Depending on the desired level of granularity, choose two or three application levels. Since S/4HANA employs a different technical backbone than ERP 6.0 (using the HANA database and given that S/4HANA environments are often cloud-based) the IT components vary from those in ERP 6.0.
  * Link the business capabilities to the lines of business and lower-level applications. You can always get an aggregated view at the ERP level in the reports when needed.


![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio7b086d01fc434529922941c19732caad_LowRes.png)
Modeling SAP S/4HANA Applications and IT Components
The following diagrams show best practices for modeling different deployment models:
