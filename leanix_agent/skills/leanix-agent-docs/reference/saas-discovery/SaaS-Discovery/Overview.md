##  Overview
SaaS discovery identifies your organization's Software as a Service (SaaS) applications through integrations with third-party systems like Single-Sign-on (SSO), Secure Access Simplified (SASE), and Cloud Access Security Broker (CASB) solutions. Once a new SaaS application is discovered, you can:
  * Automatically or manually link the discovered SaaS application to existing application fact sheets or create new fact sheets and link them to the catalog item
  * Enrich existing or newly created fact sheets by automatically linking the discovered SaaS to the reference catalog


The SaaS discovery feature integrates with third-party systems via APIs. To set up these integrations, you need to provide credentials with appropriate permissions for those systems. You can find detailed instructions for setting up each available integration in [Setting Up Integrations for SaaS Discovery](https://help.sap.com/docs/leanix/ea/saas-discovery?locale=en-US&state=PRODUCTION&version=CLOUD#loio275c3d767a441014ae0c923a790beb3d__setting_up_integrations_for_saas_discovery). Once an integration is set up, SAP LeanIX verifies the credentials and retrieves information about your organization’s applications, usually twice a day.
**Note**
Since the SaaS discovery feature operates through integration with third-party systems, applications that are not from the application gallery but are developed or registered by the organization itself in their application landscape are not discovered.
