##  Troubleshooting
If you cannot connect SAP BTP Cloud Foundry integration in LeanIX or if the LeanIX log or UI shows an authentication error and IAS does not display a clear error message, consider the following:
  1. Certificate authentication is still active in IAS
     * Verify that certificate authentication is disabled for all user types in IAS. For more information, see [Enable Users to Generate and Authenticate with Certificates](https://help.sap.com/docs/cloud-identity-services/cloud-identity-services/enable-users-to-generate-and-authenticate-with-certificates "https://help.sap.com/docs/cloud-identity-services/cloud-identity-services/enable-users-to-generate-and-authenticate-with-certificates").
     * If any user type can generate certificates, IAS does not accept trusted certificate authentication for the tenant. Authentication from LeanIX will not succeed.
  2. X.509 pattern mismatch
     * Check that the pattern you configured in IAS exactly matches the pattern shown in LeanIX.
     * If necessary, copy the pattern again from LeanIX and paste it into IAS, as described in
[Configure X.509 Client Certificates for User Authentication](https://help.sap.com/docs/cloud-identity-services/cloud-identity-services/configure-x-509-client-certificates-for-user-authentication "https://help.sap.com/docs/cloud-identity-services/cloud-identity-services/configure-x-509-client-certificates-for-user-authentication").
  3. Incorrect origin key or IAS tenant domain
     * Confirm that the origin key and IAS tenant domain in LeanIX match the values in your SAP BTP subaccount trust configuration.


YesNo
Send
