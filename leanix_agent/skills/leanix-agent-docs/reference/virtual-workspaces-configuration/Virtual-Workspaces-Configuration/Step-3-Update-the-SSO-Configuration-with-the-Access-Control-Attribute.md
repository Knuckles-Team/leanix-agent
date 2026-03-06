##  Step 3: Update the SSO Configuration with the Access Control Attribute
In the SSO configuration, you need to add a new attribute. You do this in your IdP, for example Okta, Entra ID, or similar. The exact steps depend on your IdP. In general, access control is configured in a similar way that you assign roles. To learn more, see [Single Sign-On](https://help.sap.com/docs/leanix/ea/single-sign-on-sso?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to configure single sign-on \(SSO\) with SAP LeanIX.").
  1. In your IdP, create the Active Directory (AD) groups for the assignment of access control entities. Add users to the AD groups.
  2. In the IdP, navigate to the SSO configuration for your SAP LeanIX application.
  3. Add the new attribute ace.
  4. Assign the ace values to the corresponding AD user groups.
Ensure the attribute value is uppercase with no spaces. Underscores are allowed.
Each attribute value must match the access control entity ID configured in SAP LeanIX. For example, the ace value FINANCE_DEPT matches the access control entity ID FINANCE_DEPT.
  5. Verify that the IdP sends the correct ace value to SAP LeanIX.
Use one of the following options to test the ace values:
     * Recommended: [Check the Session Details](https://help.sap.com/docs/leanix/ea/virtual-workspaces-configuration?locale=en-US&state=PRODUCTION&version=CLOUD#loio275e00cc7a441014a1c5d23aaa5a3877__check_the_session_details)
As this option is more precise it is recommended especially for troubleshooting.
     * [Check the Profile Details](https://help.sap.com/docs/leanix/ea/virtual-workspaces-configuration?locale=en-US&state=PRODUCTION&version=CLOUD#loio275e00cc7a441014a1c5d23aaa5a3877__check_the_profile_details)
