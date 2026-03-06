##  SCIM Attribute Mapping
The following table lists attributes that are supported in the SCIM integration. Your IdP may require other attributes that are not listed in the table.
Attribute | Required | Description
---|---|---
userName | Required | As configured in SSO in the uid claim
givenName | Required | User's given name
familyName | Required | User's family name
emails or email | Required | User's work email address
active | Required (in Microsoft Entra ID) | Controls provisioning and deprovisioning


The username and email address are unique user identifiers. The following scenarios are possible:
  * The username and email address in SAP LeanIX match with the provisioned information: The user can be matched. No changes to the user in SAP LeanIX are applied.
  * The username or email address in SAP LeanIX matches with the provisioned information: The user can be matched. The user in SAP LeanIX gets updated with the provisioned information.
  * Neither the username nor email address matches with the provisioned information: The user can’t be matched. A new user is created in SAP LeanIX.


YesNo
Send
