##  Step 2: Configure SAML Settings
In the Configuration section of the application settings, enter the following:
  * Audience (Entity ID): https://{REGION}-signin.leanix.net/realms/service-provider/broker/{UUID}
  * Recipient: https://{REGION}-signin.leanix.net/realms/service-provider/broker/{UUID}/endpoint
  * ACS (Consumer) URL Validator: ^https:\/\/{REGION}-signin\\.leanix\\.net\/realms\/service-provider\/broker\/{UUID}\/endpoint$
  * ACS (Consumer) URL: https://{REGION}-signin.leanix.net/realms/service-provider/broker/{UUID}/endpoint
  * Login URL: https://{SUBDOMAIN}.leanix.net/{WORKSPACE}
