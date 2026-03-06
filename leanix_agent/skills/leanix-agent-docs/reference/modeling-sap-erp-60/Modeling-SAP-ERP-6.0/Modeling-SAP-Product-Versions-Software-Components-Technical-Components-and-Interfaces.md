##  Modeling SAP Product Versions, Software Components, Technical Components, and Interfaces
This section provides guidance on modeling the technical details of the SAP ERP 6.0 application landscape. To do so effectively, it's essential to understand the SAP product structure, which is illustrated below:
![SAP Product Model](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2750cbc37a4410149f72e834a06a342d_LowRes.png)
SAP Product Model
As previously mentioned, SAP applications and modules are modeled as applications in SAP LeanIX. However, an SAP ERP 6.0 application often uses multiple product versions and various software components. The best practice is to map SAP product versions, enhancement packages, add-ons, and industry solutions to IT components in SAP LeanIX. Additionally, specific SAP software components are represented using IT components:
![Modeling Product Versions, Enhanced Packages, Add-ons, and Industry Solutions to IT Components](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2751cb067a441014aafaaea02f242e49_LowRes.png)
Modeling Product Versions, Enhanced Packages, Add-ons, and Industry Solutions to IT Components
Use the tech category fact sheet if you want to categorize and structure different types of product versions:
![Using Tech Category to Model Different Types of Product Versions](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274258027a441014b89fe1ae48a80cf4_LowRes.png)
Using Tech Category to Model Different Types of Product Versions
You can also use the tech category to map technical objects and systems, such as application servers, databases, operating systems, etc., to IT components:
![Use Tech Category to Map Technical Objects](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274d40427a4410148c90b62c4454877c_LowRes.png)
Using Tech Category to Map Technical Objects
You can determine the level of detail for your model—for example, whether you want to model interfaces on level 1 or level 2 of applications. Typically, at this level, you would also consider modeling data objects to understand how data flows between applications. This is an important insight for ERP transformation use cases, as it helps visualize data movement and identify potential dependencies or bottlenecks in the system.
The following diagram shows an example of how to model SAP interfaces in SAP LeanIX:
![Data Objects and Interfaces](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274b91787a4410148997e101612006de_LowRes.png)
Example for Modeling ERP 6.0 including Data Objects and Interfaces
It is also possible to map your SAP company codes and providers to SAP LeanIX. We recommend mapping them to the organization and provider fact sheet types.
