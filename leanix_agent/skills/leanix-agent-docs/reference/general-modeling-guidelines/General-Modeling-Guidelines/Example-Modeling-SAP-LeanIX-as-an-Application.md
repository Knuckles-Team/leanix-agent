##  Example: Modeling SAP LeanIX as an Application
In this example, SAP LeanIX is modeled as an application. It is positioned within a business context, used by multiple business units, and interfaces with other applications.
**Tip**
The diagram below has been created with SAP LeanIX diagrams. [Diagrams](https://help.sap.com/docs/leanix/ea/diagrams?locale=en-US&state=PRODUCTION&version=CLOUD) are great to start modeling anything in SAP LeanIX. They are intuitive to new users, and you can easily visualize multiple fact sheet types and additional architecture objects together and share them with anyone.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274368fa7a441014a19ea34144a2e3aa_LowRes.png)
We are looking at three dimensions:
  * What is SAP LeanIX doing? — It supports the business capability “Information Technology”, which is part of “Information Management”.
  * How is SAP LeanIX being used? — It is embedded in the business context of the subtype process. There it is part of “Planning & Controlling”, more specifically, the Process to “Implementation Process”, within the sub-steps “1. Project Setup” and “4. Architecture Setup”.
  * Who is using SAP LeanIX? — “Headquarters”, “Australia” and “Brazil” use SAP LeanIX.


An interface to “SAP Signavio” has been implemented. They exchange the data objects “IT Application” and “Process.”
From a hosting perspective, an IT component has been modeled, and related to a provider and a tech category.
  * SAP LeanIX is SaaS, so the provider “LeanIX GmbH” provides an IT component called “Application Hosting” (service). It is grouped in the tech category “Hosting / Operations.”


Finally, SAP LeanIX is included in the initiative “Introduction of Enterprise Architecture Management” scope.
Related Information
[Using Tags and Custom Fields](https://help.sap.com/docs/leanix/ea/tags-and-custom-fields?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to effectively use tags and custom fields in SAP LeanIX.")
[Using Relations](https://help.sap.com/docs/leanix/ea/relations?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to use different types of relations to model dependencies and interactions between fact sheets.")
[Modeling and Reports](https://help.sap.com/docs/leanix/ea/modeling-and-reports?locale=en-US&state=PRODUCTION&version=CLOUD)
