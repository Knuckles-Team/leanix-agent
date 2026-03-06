##  Step 2: Configure SAML Token Attributes
Configure SAML 2.0 attribute mapping in Microsoft Entra ID. For more information, see [Attribute Mapping](https://help.sap.com/docs/leanix/ea/single-sign-on-sso?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cc8227a441014a371975e4b816f0a__attribute-mapping). Mapping attributes are defined as SAML Token Attributes in the Relying Party Trust.
Follow these steps:
  1. Under Attributes & Claims, configure additional claims using the following values:
Claim Name | Type | Value
---|---|---
firstname | SAML |  user.givenname
lastname | SAML |  user.surname
email | SAML |  user.mail
role | SAML |  user.assignedroles
uid | SAML |  user.userprincipalname


  2. For each claim, delete the Namespace value in the configuration.
![Leaving the](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2753af837a4410148f63c9682c8c9cb2_LowRes.png)
Leaving the "Namespace" Value Blank in the Claim Configuration


Basic SSO configuration is set up.
