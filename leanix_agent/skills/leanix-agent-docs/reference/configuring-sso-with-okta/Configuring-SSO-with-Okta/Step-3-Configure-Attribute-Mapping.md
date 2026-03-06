##  Step 3: Configure Attribute Mapping
Follow these steps:
  1. On the Sign On tab of your application, select Configure profile mapping.
![Selecting the Configure Profile Mapping Link on the Sign On Tab of an SSO Application in Okta](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2750c3847a441014b08ab264f80274bd_LowRes.png)
Selecting the "Configure Profile Mapping" Link on the "Sign On" Tab of an SSO Application
  2. In the overlay that appears, click Cancel.
  3. In the Attributes section, click Add Attribute.
  4. Specify the attribute details.
     * Data type: Select string.
     * Display name, Variable name, and External name: Enter role to match the attribute that you added to the SAML assertion.
     * Enum: Select Define enumerated list of values and create a list of user roles that the Okta admin can select from. The values in the following table correspond to the SAP LeanIX standard roles, but you can adjust the list according to your needs.
Display Name | Value
---|---
ADMIN |  ADMIN
MEMBER |  MEMBER
VIEWER |  VIEWER


     * Attribute type: Select Group.
![Configuring General SAML Settings for an SSO Application in Okta](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274c8fa27a441014968db146debee732_LowRes.png)
Adding an Attribute to a Profile in Okta
  5. Save the changes.
