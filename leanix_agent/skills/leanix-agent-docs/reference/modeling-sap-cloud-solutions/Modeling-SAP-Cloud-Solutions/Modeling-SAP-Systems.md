##  Modeling SAP Systems
An SAP system represents the complete technical environment that supports ERP solutions and related business applications. It includes a combination of hardware and software components, such as the application server, database, and system-specific configurations.
Using the SAP system fact sheet subtype, you can gain system-centric views when managing ERP transformations and upgrades. This fact sheet subtype lets you capture key SAP-specific data, such as system ID (for example, "POP" or"P42"), system number, installation number, and customer number directly within SAP LeanIX. This allows you to get a characteristic overview of your SAP landscape, for example, using an aggregated report view based on the deployment model, such as public cloud, private cloud, or on-premise, or based on environments like development (DEV), quality assurance (QA), and production (PROD). To learn more, see [System Modeling Guidelines](https://help.sap.com/docs/leanix/ea/system-modeling-guidelines?locale=en-US&state=PRODUCTION&version=CLOUD "Modeling guidelines, best practices, use cases, and recommendations for system fact sheets.").
![Landscape Report Showing Applications by Deployment Type](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loioa6210205d77a4efa9e07e02192cfc2c8_HiRes.png)
Though transformation planning should still happen at the application level, incorporating system-level insights helps you contextualize changes and manage dependencies more effectively.
By establishing relations between the system fact sheet and other fact sheets, such as application, IT component, and initiative, you can answer key questions about your IT landscape. For example:
  * Which applications run on a specific system?
  * Which IT components are hosted on that system?
  * Which transformation initiatives impact or involve the system?

![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio43e771e00edc48b597d0b21669438bd1_HiRes.png)
With a clearer view of dependencies, you can manage transformations more effectively across your SAP landscape.
