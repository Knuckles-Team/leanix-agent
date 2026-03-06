##  General Guidelines for Modeling SAP ERP 6.0
  * Like other SAP applications, SAP ERP 6.0 should be modeled as a level 1 application, with underlying modules, such as SAP MM and SAP FI, as level 2 applications.
  * Model SAP product versions, enhancement packages, add-ons, and industry solutions as IT components.


![Business Perspective](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275702c87a441014a1918986293fc50f_LowRes.png)
SAP LeanIX Modeling Best Practice for SAP ERP 6.0
Our general recommendation is to focus on the business perspective. This aligns with SAP LeanIX’s application-centric view and the core objective of SAP LeanIX: to bring IT and business together to support strategic planning and decision-making. Bring all instances of an SAP application with business impact into SAP LeanIX, as this reflects the SAP LeanIX concept of an application.
In some scenarios, organizations may opt for a technical perspective following the logic of SAP System ID (SID) (unique identifier for an SAP system within the landscape, typically encompassing a database and multiple application servers) and Client (Mandant (logical partition or container within an SAP system, addressing a specific user group and containing its own data). For instance, if an organization frequently acquires new companies and prefers to keep SAP clients separate, it's better to model SIDs as level 1 applications, SAP Clients as level 2 applications, and individual SAP applications as level 3 applications in SAP LeanIX. This approach maintains a logical structure while accommodating specific business needs.
![Technical Perspective](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2753c5d97a441014a47bba685e855d63_LowRes.png)
Technical modeling approach
