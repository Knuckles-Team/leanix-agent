##  Configuring Attribute Mapping
To learn how to configure attribute mapping, see [Attribute Mapping](https://help.sap.com/docs/leanix/ea/single-sign-on-sso?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cc8227a441014a371975e4b816f0a__attribute-mapping).
When using AD FS for SSO, you can pass values in addition to the authentication values. These values are defined as Claim Rules in the Relying Party Trust. To edit Claim Rules, select the Relying Party Trusts folder in AD FS Management, then select Edit Claim Rules in the Actions sidebar.
You should also configure custom claim rules. Please see example AD FS claim rules below.

```
@RuleName = "Get tokenGroups"
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]
 => add(store = "Active Directory", types = ("http://claims.contoso.com/tokenGroups"), query = ";tokenGroups;{0}", param = c.Value);

@RuleName = "Add Given-Name from AD"
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]
 => add(store = "Active Directory", types = ("http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname"), query = ";givenName;{0}", param = c.Value);

@RuleName = "Add Surname from AD"
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]
 => add(store = "Active Directory", types = ("http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname"), query = ";sn;{0}", param = c.Value);

@RuleName = "Add UPN from AD"
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]
 => add(store = "Active Directory", types = ("http://claims.contoso.com/ADupn"), query = ";userPrincipalName;{0}", param = c.Value);

@RuleName = "Add E-Mail-Address from AD"
c:[Type == "http://schemas.microsoft.com/ws/2008/06/identity/claims/windowsaccountname", Issuer == "AD AUTHORITY"]
 => add(store = "Active Directory", types = ("http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"), query = ";mail;{0}", param = c.Value);

@RuleName = "Send Given-Name as firstname"
c:[Type == "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/givenname"]
 => issue(Type = "firstname", Value = c.Value, Issuer = c.Issuer, Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/attributename"] = "urn:oasis:names:tc:SAML:2.0:attrname-format:uri");

@RuleName = "Send Surname as lastname"
c:[Type == "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/surname"]
 => issue(Type = "lastname", Value = c.Value, Issuer = c.Issuer, Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/attributename"] = "urn:oasis:names:tc:SAML:2.0:attrname-format:uri");

@RuleName = "Send ADUPN as uid"
c:[Type == "http://claims.contoso.com/ADupn"]
 => issue(Type = "uid", Value = c.Value, Issuer = c.Issuer, Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/attributename"] = "urn:oasis:names:tc:SAML:2.0:attrname-format:uri");

@RuleName = "Send E-Mail-Address as email"
c:[Type == "http://schemas.xmlsoap.org/ws/2005/05/identity/claims/emailaddress"]
 => issue(Type = "email", Value = c.Value, Issuer = c.Issuer, Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/attributename"] = "urn:oasis:names:tc:SAML:2.0:attrname-format:uri");

@RuleName = "Send role ADMIN"
EXISTS([Type == "http://claims.contoso.com/tokenGroups", Value == "EAM-ADMIN"])
 => issue(Type = "role", Value = "ADMIN", Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/attributename"] = "urn:oasis:names:tc:SAML:2.0:attrname-format:uri");

@RuleName = "Send role MEMBER"
EXISTS([Type == "http://claims.contoso.com/tokenGroups", Value =~ "^EAM-MEMBER*"])
 => issue(Type = "role", Value = "MEMBER", Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/attributename"] = "urn:oasis:names:tc:SAML:2.0:attrname-format:uri");

@RuleName = "Send role VIEWER"
EXISTS([Type == "http://claims.contoso.com/tokenGroups", Value == "EAM-VIEWER"])
 => issue(Type = "role", Value = "VIEWER", Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/attributename"] = "urn:oasis:names:tc:SAML:2.0:attrname-format:uri");

@RuleName = "Send customer_roles CUSTOMERROLE1"
EXISTS([Type == "http://claims.contoso.com/tokenGroups", Value == "EAM-CUSTOMERROLE1"])
 => issue(Type = "customer_roles", Value = "CUSTOMERROLE1", Properties["http://schemas.xmlsoap.org/ws/2005/05/identity/claimproperties/attributename"] = "urn:oasis:names:tc:SAML:2.0:attrname-format:uri");

```



### Verify your SSO Configuration
To verify your SSO configuration, first, access your workspace at https://{SUBDOMAIN}.leanix.netand log in, then open a SAML tracer browser extension or desktop application. In the SAML tracing you can see a list of required user attributes.
YesNo
Send
![close icon](https://consent.trustarc.com/get?name=sapglow-close-icon.png)
This site uses cookies and related technologies, as described in our Cookie Statement, for purposes that may include site operation, analytics, enhanced user experience, or advertising. You may choose to consent to our use of these technologies, or manage your own preferences.
Understood Manage Settings
[Privacy Statement](https://help.sap.com/docs/privacy)|[Cookie Statement](https://www.sap.com/about/legal/privacy/cookies.html)
