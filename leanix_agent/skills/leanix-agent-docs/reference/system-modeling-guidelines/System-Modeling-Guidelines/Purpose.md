##  Purpose
Capturing system-level information is valuable in two main scenarios:
  * Enable enterprise architects in consistent risk management with a configuration management database (CMDB), particularly with ServiceNow.
  * Enable solution architects and system architects to understand dependencies and details for ERP transformations, particularly when driven by SAP discovery


The system fact sheet offers insights into:
  * Hosting or deployment environments (such as development, production, testing, or quality assurance)
  * Deployment models (such as public cloud, private cloud, or on-premise)
  * Instance-level information, for example, local instances for high availability setups.


The following gives an agnostic overview of the interplay of applications, systems, and IT components.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio322ad27617d745dea806c68f9ece49cf_LowRes.png)
Interplay of Applications, Systems, and IT Components
The following table provides a clear distinction:
Systems | Applications | IT Components
---|---|---
  * Systems that run an application, for example, ERP systems.
  * Testing and sandbox environments
  * Staging and quality assurance environments
  * Stand-by fallback environments

|  Applications serve a business purpose and have a defined business context. Different applications usually have different owners and life cycles. For example:
  * Regional application instances - SAP FI France, SAP FI Germany, etc.

|  Non-instance level technologies, including software and hardware, or services that an organization’s applications and systems depend on. For example:
  * Oracle DB 11.1
  * AWS EC2
  * Microsoft .NET Framework 4.8




**Note**
  * The system fact sheet is an optional fact sheet type. It's not included in the predefined meta model by default. You can add this fact sheet type to your meta model by following the instructions in [Activating the System Fact Sheet](https://help.sap.com/docs/leanix/ea/system-modeling-guidelines?locale=en-US&state=PRODUCTION&version=CLOUD#loio2957f4829fe749efbe704d30c35c4e8a__section_pjr_z5m_sfc).
  * System fact sheets are meant to be created and maintained automatically through imports, for example, from SAP discovery and ServiceNow integrations.
