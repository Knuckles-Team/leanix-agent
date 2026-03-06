##  Optional: Enable OAuth 2.0 for Authentication
[OAuth 2.0![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.servicenow.com%2Fbundle%2Frome-application-development%2Fpage%2Fintegrate%2Finbound-rest%2Ftask%2Ft_EnableOAuthWithREST.html?locale=en-US&state=PRODUCTION&version=CLOUD "https://docs.servicenow.com/bundle/rome-application-development/page/integrate/inbound-rest/task/t_EnableOAuthWithREST.html") can be configured for additional security during the authentication between SAP LeanIX and ServiceNow.
![3496](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274a57417a4410149a58ff29fda1edb1_LowRes.png)
SAP LeanIX Integration uses the "oAuth API endpoint for external clients" method.
After enabling the plugin, the method used by SAP LeanIX is "OAuth API endpoint for external clients" to retrieve a clientId and a clientSecret. Here is an example -
![3496](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274e0cdb7a441014b79daf972c39af38_LowRes.png)
This example shows one OAuth API Application Registration used for communication between SAP LeanIX and ServiceNow via OAuth2.0
Once created copy the Client ID and Client Secret and store it in a safe location to use when configuring the Integration on the SAP LeanIX side.
