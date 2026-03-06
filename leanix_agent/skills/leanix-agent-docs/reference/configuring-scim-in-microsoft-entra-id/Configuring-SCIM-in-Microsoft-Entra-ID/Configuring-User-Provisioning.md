##  Configuring User Provisioning
Follow these steps:
  1. In Microsoft Entra ID, navigate to the SSO application for SAP LeanIX.
  2. On the Provisioning page, configure provisioning settings.
    1. In the Provisioning Mode list, select Automatic.
    2. Under Admin Credentials, in the Tenant URL field, enter the following URL:

```
https://{SUBDOMAIN}.leanix.net/services/mtm/v1/scim/v2

```



    3. In the Secret Token field, enter the long-lived access token that you obtained.
![Configuring Provisioning Settings in Microsoft Entra ID](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2741993f7a441014ac5f9b68560f35aa_LowRes.png)
Configuring Provisioning Settings in Microsoft Entra ID
    4. Under Mappings, ensure that provisioning for Active Directory Groups is disabled.
![Mapping Settings on the Provisioning Page](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274398a97a441014a9aafeb9749d001f_LowRes.png)
Mapping Settings on the Provisioning Page
  3. On the Attribute Mapping page, update attribute mapping to include only the following attributes and delete all other attributes.
     * userPrincipalName: Please ensure that the property you're passing is identical to your SSO configuration. Change the SCIM property as needed. This property must be in the email format.
     * mail
     * Switch
     * givenName
     * surname
     * department
![Required Attribute Mappings for SCIM Provisioning Between Microsoft Entra ID and SAP LeanIX](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275451217a441014b79fff7a5e379506_LowRes.png)
Required Attribute Mappings for SCIM Provisioning Between Microsoft Entra ID and SAP LeanIX
To make Entra ID compatible with the SCIM implementation, configure the predefined email attribute as a matching attribute with the Matching precedence set to 2.
![Configuring the Email Attribute](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27416ab77a441014beb3eb2eaf360c14_LowRes.png)
Configuring the Email Attribute
**Note**
To learn more about attribute mapping and SCIM provisioning, refer to the Microsoft Entra ID documentation:
       * [Customize attribute mappings![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fentra%2Fidentity%2Fapp-provisioning%2Fcustomize-application-attributes "https://learn.microsoft.com/en-us/entra/identity/app-provisioning/customize-application-attributes")
       * [Plan provisioning for a SCIM endpoint![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Flearn.microsoft.com%2Fen-us%2Fentra%2Fidentity%2Fapp-provisioning%2Fuse-scim-to-provision-users-and-groups "https://learn.microsoft.com/en-us/entra/identity/app-provisioning/use-scim-to-provision-users-and-groups")
  4. To test provisioning, select Provision on demand and enable provisioning for a test user.
![Selecting the](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2755d7897a441014ba0fb2b4099d5b9d_LowRes.png)
Selecting the Provision on demand Option for Testing the Configuration
  5. After you've tested provisioning for a test user, click Start provisioning.


SCIM provisioning between Microsoft Entra ID and SAP LeanIX is enabled.
