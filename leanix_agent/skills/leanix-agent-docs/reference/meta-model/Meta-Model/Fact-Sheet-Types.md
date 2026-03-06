##  Fact Sheet Types
The fundamental building blocks of the SAP LeanIX meta model are called fact sheet types. By default there are 12 different fact sheet types in the meta model v4 as detailed below. On the type level, relations, attributes, subscriptions, tags, access, and more are defined.
Relations between fact sheets define how different architectural elements are connected to each other. They describe who uses what, depends on what, and supports what across your enterprise architecture.
For example:
  * A business capability is supported by an application
  * An application runs on an IT component
  * An organization uses an application
  * An application interfaces with another application

These relations are the basis for all the reports and allow you to analyze impact of changes, dependencies, risks, redundancies and more.
![Default and Optional Fact Sheet Types and Subtypes with Relations](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio5a7c6dcc53e94c0ba5d72d25c5e6ec86_LowRes.png)
Default and Optional Fact Sheet Types and Subtypes with Relations
**Note**
You can download the SAP LeanIX meta model illustration as an XML file to import and edit in diagram. [Download Meta Model![Information published on SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/sap_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fd.dam.sap.com%2Fa%2FTFZhXtR%3Frc%3D10%26doi%3DSAP1273133 "https://d.dam.sap.com/a/TFZhXtR?rc=10&doi=SAP1273133")
Title | Layer | Definition
---|---|---
Objective | Strategy & Transformation | Objectives capture the goals that your organization aims to achieve. These drive initiatives to improve business capabilities and transform the IT landscape.
Platform | Strategy & Transformation | Platforms are groupings of business capabilities, applications, and technologies that provide common functionalities.
Initiative | Strategy & Transformation | Initiatives capture the planned projects or programs within your organization that impact its enterprise architecture and are aimed at achieving specific goals or objectives.
Organization | 1. Business Architecture | Organizations represent your organization's hierarchical business architecture, detailing departments and teams.
Business capability | 1. Business Architecture | Business capabilities (also called domains) model what your applications do to support your business goals.
Business context | 1. Business Architecture | Business contexts capture the specific activities your organization performs to achieve its business goals.
Data Object | 2. Application & Data Architecture | Data objects provide an overview of general data processed and exchanged by specific applications.
Application | 2. Application & Data Architecture | Applications are the software systems or programs that process or analyze business data to support business tasks, processes, or aspects of your organization's business model. They are the central entities in SAP LeanIX because they link business and IT.
Interface | 2. Application & Data Architecture | Interfaces are the connections between applications that illustrate how data exchange occurs.
Provider | 3. Technical architecture | Providers are the companies or entities that supply IT solutions, services, or technologies to support your organization in achieving its objectives and operational efficiency.
IT component | 3. Technical architecture | IT components represent the technology or services that your applications depend on. They can provide information on both development and operations. They are used to model operating costs as well as technological risks.
Tech category | 3. Technical architecture | Tech categories are used to group IT components into different categories of technology.
System | 3. Technical architecture |  Systems represent the technical environment underlying applications, such as a server or virtual machine with its operating system, database, runtime configurations, and more. **Note** The system fact sheet is an optional fact sheet type.


**Note**
Since a tech category can be seen as a relatively stable structure, it will look similar for different companies. To start classifying your IT components using a tech category, you should look at our [Best Practice Technology Stacks![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fwww.leanix.net%2Fen%2Fdownload%2Fbest-practices-to-define-technology-stacks "https://www.leanix.net/en/download/best-practices-to-define-technology-stacks").
