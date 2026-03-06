##  Step 4: Assign Users to the Application
You can assign specific users or user groups to the SSO application.
Follow these steps:
  1. On the Assignments tab of the application, click Assign > Assign to Groups.
![Selecting the Assign to Groups Option on the Assignments Tab of an SSO Application](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274f197c7a441014a8c1af09a04ac948_LowRes.png)
Selecting the "Assign to Groups" Option on the "Assignments" Tab of an SSO Application
  2. In the overlay that appears, select a user group to assign to the application.
  3. In the role list, select an SAP LeanIX role to be assigned to users in this group.
![Selecting a User Role to Be Assigned to Users of the SSO Application](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274fefab7a4410148d01912246667092_LowRes.png)
Selecting a Role to Be Assigned to Users of an SSO Application
  4. Optional: If needed, modify other attributes, then save the configuration.
  5. Optional: If needed, on the Sign On tab of the application, in the Sign On Policy section, specify rules for your sign-on policies, for example, multi-factor authentication.
![Sign On Policy Section on the Sign On Tab of an SSO Application](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27495f847a4410148ca996266348247a_LowRes.png)
"Sign On Policy" Section on the "Sign On" Tab of an SSO Application


### Verify your SSO Configuration
To verify your SSO configuration, first, access your workspace at https://{SUBDOMAIN}.leanix.netand log in, then open a SAML tracer browser extension or desktop application. In the SAML tracing you can see a list of required user attributes.
