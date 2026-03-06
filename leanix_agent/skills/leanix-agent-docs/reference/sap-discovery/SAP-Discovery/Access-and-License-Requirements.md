##  Access and License Requirements
Before you set up SAP discovery integrations, ensure you have the necessary access rights and licenses.
You need the following access for all integrations:
  * SAP LeanIX administrator access to set up integrations.
  * SAP BTP Cockpit Global Account Administrator access to configure SAP BTP settings.
  * S-User with SAP for Me access to create support tickets.


### Additional Access by Integration
Use this table to find integration-specific access requirements.
Integration | Additional Access Required
---|---
SAP Cloud ALM Integration for SAP Discovery |
  * SAP for Me administrator: Check the Automated System Updates flag.
  * Maintenance Planner administrator: Add new innovations as a prerequisite for discovery.
  * SAP Cloud ALM administrator: Add customer numbers and check discovered items.


SAP Build Integration for SAP Discovery | SAP Build Process Automation administrator: Check SAP Build.
SAP BTP, Cloud Foundry Integration for SAP Discovery |  A platform user account in your SAP Cloud Identity Services (IAS) tenant with the following:
  * Active certificate generation.
  * Trust set up for relevant SAP BTP global and subaccounts.
  * Access to SAP BTP, Cloud Foundry organizations and spaces with these roles:
    * Org Auditor
    * Space Auditor




### License Requirements
You need SAP LeanIX Application Portfolio Management for all SAP discovery integrations. You also need a license for each SAP product you want to integrate.
Integration Type | Required SAP License
---|---
SAP Cloud ALM Integration for SAP Discovery  | SAP Cloud ALM
SAP Build Integration for SAP Discovery  | SAP Build Process Automation
SAP BTP, Cloud Foundry Integration for SAP Discovery  | SAP BTP, Cloud Foundry Runtime


YesNo
Send
