##  SAP LeanIX Meta Model v3
At its core, LeanIX offers a proven, easy to understand Meta Model. The out-of-the-box Meta Model covers all layers in the architecture. In order to fully leverage the capabilities of LeanIX's platform offering, it is important to understand how the range of different LeanIX EAM objects fit together. Below you will find the core entities, that we call Fact Sheets, and their relationships, as well as detailed descriptions below.
![1589](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2753b3dd7a441014a05fdf2a149bdcf3_LowRes.png)
LeanIX EAM Meta Model
The following table contains definitions of the out-of-the-box Fact Sheets:
Fact Sheet | Defintion
---|---
Objective | Objectives allow high-level definitions and progress tracking of transformation initiatives and can be linked to Business Capabilities.
Project / fka Transformation Item for BTM customers | Projects groups activities that change the application portfolio over time. They allow to make dependencies, schedules, and costs transparent, e.g. synchronized with a PPM tool.
Business Capability | Business capabilities (also called domains) model what your applications do in order to support your business goals. Business capabilities are typically nested to allow analyses at different granularity level, e.g. with the application landscape report.
Process | Processes model how your applications help you to support your business goals. In contrast to capabilities, they focus on activities. A process in LeanIX is a container as LeanIX is no dedicated process modelling tool. Out-of-the-box integrations, e.g. to Signavio, are provided.
User Group | User groups model who uses your application. By relating them to capabilities and processes, you get powerful business support output. User groups can be modeled among different dimensions, e.g. organizational entities, locations, or customers.
Application | Applications are the central entities in LeanIX as they provide the link between business and IT. An application is used by a user group in a business context (capability / process) and is developed & operated based on IT components.
Interface | Interfaces are connections between Applications. They transfer data objects and are implemented via IT components.
Data Object | Data objects represent a business view on major data entities used, e.g. customer, employees or contracts. Data objects are transferred or managed by applications. They help to identify redundancies & for data security or analytics questions.
IT Component | IT Components represent the technology your applications depend on. They can provide information on both development & operations. IT Components are grouped into services, software & hardware. They are used to model operating costs as well as technological risks.
Provider | Provider is used to capture who is responsible for hosting, maintaining and changing your applications. For this purpose, they are linked to IT components and projects to manage provider costs and relations.
Tech Category | Tech Category Fact Sheets are technical domains and allow to classify the IT components by technical characteristics. This classification can be used to govern your IT-landscape from the technical side, e.g. by analyses via the IT component landscape report.


