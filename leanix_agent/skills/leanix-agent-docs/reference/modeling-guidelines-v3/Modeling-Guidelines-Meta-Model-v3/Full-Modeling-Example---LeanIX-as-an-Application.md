##  Full Modeling Example - LeanIX as an Application
The following is a full-fledged modeling example based on LeanIX as an application. The screenshot below was created in the Diagrams section of the LeanIX workspace.
![2018](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274fc2317a441014b425e2291c1cbdcd_LowRes.png)
"LeanIX Enterprise Application Suite" is an Application. It operates within a business context, has business users and interfaces with other Applications.
The business context comprises all three dimensions:
  * What is LeanIX doing? It is supporting the Business Capability "Information Management" which is part of "Information Technology".
  * How is LeanIX being used? It is embedded in the standard project Process, within the sub-steps "1. Project Setup" and "4. Architecture Review".
  * Who is using LeanIX? Besides the "Headquarters", the User Groups "Australia" and "Brazil" are currently active.


In the information and data context, an Interface to "SAP Signavio" has been implemented. It is provided by LeanIX and transports the Data Objects "IT Application" and "Process".
From a hosting perspective, two IT Components have been modeled, both with a Provider and a Tech Category.
  * LeanIX is SaaS, so the provider "LeanIX GmbH" provides an IT Component called "Application Hosting" (service). It is grouped in the Tech Category "Operations / Hosting".
  * SSO is implemented, so LeanIX depends on an IT Component called "ADFS 4.0 - Windows Server 2016" (software). The provider is "Microsoft", and it is grouped as "Middleware / Identity Management".


Finally, LeanIX is included in the scope of the Project "Introduction of Enterprise Architecture Management".
