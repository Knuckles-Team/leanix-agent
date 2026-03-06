##  Configuring SCIM
To configure SCIM between your IdP and SAP LeanIX, follow these steps:
  1. In SAP LeanIX, create a technical user with the admin permission role. Save the API token that appears. For instructions, see [Technical Users](https://help.sap.com/docs/leanix/ea/technical-users?locale=en-US&state=PRODUCTION&version=CLOUD "To get an API token, create a technical user. Manage technical users collaboratively with other administrators.").
  2. Request the ACCOUNTADMIN role for the technical user by [submitting a ticket![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fwww.leanix.net%2Fsupport "https://www.leanix.net/support") to support. If you're an SAP customer, submit a request from the [SAP for Me![Information published on SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/sap_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fme.sap.com%2F "https://me.sap.com/") portal. In the request, provide the name of the technical user.
  3. Get an access token required for the SCIM integration:
    1. Using the API token of the technical user, get a short-lived access token. For instructions, see [Get a Short-Lived Access Token](https://help.sap.com/docs/leanix/ea/access-tokens-required-for-scim?locale=en-US&state=PRODUCTION&version=CLOUD#loio27584fdb7a441014b39cc735479e4c85__get_a_short-lived_access_token).
    2. Using the short-lived access token, get a long-lived access token. For instructions, see [Get a Long-Lived Access Token](https://help.sap.com/docs/leanix/ea/access-tokens-required-for-scim?locale=en-US&state=PRODUCTION&version=CLOUD#loio27584fdb7a441014b39cc735479e4c85__get_a_long-lived_access_token).
  4. In your IdP, configure user provisioning. For instructions, refer to the documentation of your IdP. Use the following details:
     * SCIM endpoint: https://{SUBDOMAIN}.leanix.net/services/mtm/v1/scim/v2
     * SCIM access token: Long-lived access token that you obtained.
  5. In your IdP, configure attribute mapping. For more information, see [SCIM Attribute Mapping](https://help.sap.com/docs/leanix/ea/scim-provisioning?locale=en-US&state=PRODUCTION&version=CLOUD#loio275c86fa7a44101492b6d27589f6c558__scim_attribute_mapping).
  6. Depending on the configuration of your IdP, you may need to enable the synchronization of user states.


After you've set up SCIM, user states are synchronized between your IdP and SAP LeanIX.
