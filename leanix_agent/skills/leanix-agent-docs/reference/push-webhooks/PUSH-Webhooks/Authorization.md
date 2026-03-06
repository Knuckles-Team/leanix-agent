##  Authorization
In webhooks, we support the HTTPS protocol for the target URL, enhancing the security of your data transmission. Ensure to keep your target URL private to prevent unauthorized access.
We offer several authorization methods within the webhook configuration to further secure the delivery of webhook events to your target URLs. These include the Authorization header and OAuth 2.0. Additionally, you can append a token to the query string of the target URL for an extra layer of security. This ensures that only authorized entities can access your webhooks, further enhancing the security of your PUSH webhooks.
### Authorization Header
This method uses an authorization header secret for security. To use it, generate a unique secret in your instance. For added protection, add a Basic authorization header by clicking Add basic authorization header. The username and password you supply will be encoded for Basic authorization, ensuring their confidentiality during transmission.
### OAuth 2.0
This method is recommended for its enhanced security. It involves authenticating with your identity provider (IdP) and using the Bearer token issued by your IdP to authorize with your target URL. To implement OAuth 2.0 authorization, configure your target URL instance to accept authorization through a Bearer token from your IdP. Once your JWT settings are correctly configured, specify the following details in the webhook configuration:
  * Token URL: The endpoint in your IdP used to issue an OAuth 2.0 Bearer token.
  * Client ID: The unique identifier for the client to which the Bearer token is issued.
  * Client Secret: The client secret used to issue the Bearer token.
  * Scopes: Scopes required for accessing the target URL endpoint. The Bearer token is issued with these scopes.
  * Credentials Location: Select where to place credentials in the request:
    * Authorization Header: Credentials are sent as a Base64-encoded Basic authorization header.
    * URL Encoded Body Request: Credentials are sent in the request body as URL-encoded parameters.
  * Request Body Parameters: A set of key/value pairs to include in the request body.
  * Request Query Parameters: A set of key/value pairs to include as query parameters.
