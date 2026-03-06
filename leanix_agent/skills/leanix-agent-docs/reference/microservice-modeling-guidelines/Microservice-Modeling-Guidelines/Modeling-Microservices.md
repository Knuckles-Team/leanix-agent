##  Modeling Microservices
Organizations developing in-house software most often need to capture components of their software. The microservice subtype is used to represent these functional composites of the application in SAP LeanIX. It can be useful for:
  * Identifying opportunities for reusing microservices across different applications
  * Understanding technical ownership - identify which development teams are responsible for specific microservices
  * Planning and executing the transition from monolithic applications to a microservices architecture to improve functional fit and adaptability
  * Compiling low-level data flow based on APIs
  * Distinguishing functional building blocks (microservices) from the underlying technical composites of the application (IT components)


Modeling microservices using the microservice subtype allows you to leverage the full capabilities of reports and diagrams. For example, you can see the data flow between microservices using an interface circle map. As a best practice, we recommend modeling down to the level of specific microservices that form the core of relevant applications. This provides clear visibility into the technical dependencies of the product architecture, which is useful for technical transformations, such as re-architecting key applications.
In certain scenarios, such as during application modernization planning, manual maintenance of microservices can be useful. However, we generally recommend automating the creation and management of microservices fact sheets using SAP LeanIX Technology Risk and Compliance. It automates the discovery of microservices to keep up with frequent changes. While manual maintenance of microservices can become increasingly difficult as the number of microservices grows. To learn more, see [SAP LeanIX Technology Risk and Compliance](https://help.sap.com/docs/leanix/ea/sap-leanix-technology-risk-and-compliance?locale=en-US&state=PRODUCTION&version=CLOUD "Get an overview of SAP LeanIX Technology Risk and Compliance, with links to detailed guides for managing obsolescence risk, optimizing technology usage, and enforcing tech standards across your IT landscape.").
Microservices don’t usually answer typical business application questions and generally do not exist independently of the business application. They can be related to the business layer through the business application subtype but can also have direct relations to business capabilities.
The following example shows the modeling of microservices:
![Modeling Microservices](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27449a737a441014a2c6d0f3df79718e_LowRes.png)
Modeling Microservices
In the example, B2B Website.com and B2B MobileApps are business applications composed of several microservices like Core Iris, event-mirror, functional-validation, Payment Service, and Checkout Service. A microservice can also relate to multiple applications; therefore, the relationship between applications and microservices should be many-to-many rather than a parent/child relation.
You can map the relations between microservices by detailing their APIs using API fact sheets, a subtype of interface fact sheets. This also allows you to represent data flow between microservices. The example below shows the data flow between microservices within each application and across different applications.
![Mapping the Relation Between Microservices with API Fact Sheets](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275756677a441014bd09eedd0ee8f8c5_LowRes.png)
Mapping the Relation Between Microservices with API Fact Sheets
