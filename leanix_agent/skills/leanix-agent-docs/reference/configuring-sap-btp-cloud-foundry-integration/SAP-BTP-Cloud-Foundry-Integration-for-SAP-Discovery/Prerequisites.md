##  Prerequisites
  * In SAP LeanIX:
    * Administrator access to your workspace.
    * Meta model v4
    * Activate the BTP extension to the meta model. If it’s not yet activated, you'll be prompted to do so when you activate the integration. This extension adds the needed entities to your workspace.
  * A platform user in your custom instance (IAS tenant) of SAP Cloud Identity Service with:
    * Active certificate generation. Learn how to enable users to generate and authenticate with certificates in [Enable Users to Generate and Authenticate with Certificates](https://help.sap.com/docs/cloud-identity-services/cloud-identity-services/enable-users-to-generate-and-authenticate-with-certificates "https://help.sap.com/docs/cloud-identity-services/cloud-identity-services/enable-users-to-generate-and-authenticate-with-certificates").
    * Trust established for relevant SAP BTP global and subaccounts. Learn how to establish trust in [Establish Trust and Federation of Custom Identity Providers for Platform Users](https://help.sap.com/docs/btp/sap-business-technology-platform/establish-trust-and-federation-of-custom-identity-providers-for-platform-users "https://help.sap.com/docs/btp/sap-business-technology-platform/establish-trust-and-federation-of-custom-identity-providers-for-platform-users").
    * Access to the relevant SAP BTP, Cloud Foundry organization and spaces with the roles “Org User” and “Space Auditor”.
  * Admin access to a service instance of SAP Cloud Management Service of SAP BTP with the service plan "central-viewer".
