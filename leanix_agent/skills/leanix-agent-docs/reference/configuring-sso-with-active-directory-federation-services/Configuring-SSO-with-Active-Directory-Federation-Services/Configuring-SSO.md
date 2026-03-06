##  Configuring SSO
You can configure SSO for SAP LeanIX through a self-hosted Active Directory Federation Services (AD FS) server. AD FS is a service provided by Microsoft as a standard role for Windows Server that provides a web login using existing Active Directory credentials.
The SAP LeanIX SAML service provider is based on SIGNIN. To learn how to set up AD FS SAML federation with SIGNIN, please refer to the [Microsoft documentation![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fblogs.msdn.microsoft.com%2Fcard%2F2010%2F06%2F21%2Fa-quick-walkthrough-setting-up-ad-fs-saml-federation-with-a-shibboleth-sp%2F "https://blogs.msdn.microsoft.com/card/2010/06/21/a-quick-walkthrough-setting-up-ad-fs-saml-federation-with-a-shibboleth-sp/").
Usually, the AD FS metadata information is available at the following URL:
```
https:///FederationMetadata/2007-06/FederationMetadata.xml

```
