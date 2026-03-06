##  Step 1: Create a Platform User in Your IAS Tenant
Create a platform user for the relevant Cloud Foundry organizations and spaces that you'll onboard to SAP LeanIX. This connects SAP LeanIX workspaces to SAP BTP, Cloud Foundry environments and allows you to read metadata about deployed applications, including their service bindings.
  1. In the SAP BTP cockpit, go to the relevant Cloud Foundry organization and space.
  2. Enable users to generate and verify identity with certificates.
Learn more in [Enable Users to Generate and Authenticate with Certificates](https://help.sap.com/docs/cloud-identity-services/cloud-identity-services/enable-users-to-generate-and-authenticate-with-certificates?version=LATEST&locale=en-US "https://help.sap.com/docs/cloud-identity-services/cloud-identity-services/enable-users-to-generate-and-authenticate-with-certificates?version=LATEST&locale=en-US").
  3. Create a new user with the user type selected in the previous step, such as "Public" or "Customer".
Learn how to create users in [Create a New User](https://help.sap.com/docs/cloud-identity-services/cloud-identity-services/create-new-user "https://help.sap.com/docs/cloud-identity-services/cloud-identity-services/create-new-user").
    1. Fill in the required fields in the dialog box, including first name and last name.
    2. Select Set initial password, and record the password that you set.
    3. Save the new user.
If the email address of the new user doesn’t exist in the system, edit the user and select Verify Email to validate the user’s email address.
  4. To set a new password, go to the Profile Management section of the default domain for the IAS tenant and log on with the user created in step 3.
The URL is similar to https://<tenant ID>.accounts.ondemand.com/ui/protected/profilemanagement.
  5. Optional: If you don't know the subdomain, go to the subaccount in the SAP BTP Cockpit and choose Trust Configuration. The **Open** link in the **SAP BTP Cockpit** column contains the URL behind?idp=.
For example, https://emea.cockpit.btp.cloud.sap/cockpit/?idp=cidppuxhm.accounts.ondemand.com.


After you create the user, generate and download a certificate for passwordless authentication. For more information, see [Certificate Authentication](https://help.sap.com/docs/cloud-identity-services/cloud-identity-services/passwordless-authentication?version=Cloud#certificate-authentication "https://help.sap.com/docs/cloud-identity-services/cloud-identity-services/passwordless-authentication?version=Cloud#certificate-authentication").
