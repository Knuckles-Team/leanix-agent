##  Step 1: Create or Verify the IAS Platform User
In IAS, create or identify the user that LeanIX uses as the platform user for SAP BTP, Cloud Foundry access. For guidance, see [_Create a New User_](https://help.sap.com/docs/cloud-identity-services/cloud-identity-services/create-new-user "https://help.sap.com/docs/cloud-identity-services/cloud-identity-services/create-new-user").
Make sure of the following:
  1. You provide a first name and last name for the user.
  2. The user’s email address or another mapped attribute matches what you plan to use in the trusted certificate pattern. For example, as part of the Distinguished Name.
  3. Certificate authentication is disabled for all user types, including the one used by this platform user, as described in [_Enable Users to Generate and Authenticate with Certificates_](https://help.sap.com/docs/cloud-identity-services/cloud-identity-services/enable-users-to-generate-and-authenticate-with-certificates "https://help.sap.com/docs/cloud-identity-services/cloud-identity-services/enable-users-to-generate-and-authenticate-with-certificates").
