##  OAuth 2.0
OAuth 2.0 allows the integration to authenticate via your IdP. It uses a bearer token from your IdP to securely communicate with Collibra. We recommend using the OAuth 2.0 authentication over Basic Auth as it is more secure.
![OAuth 2.0 Authentication](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2750c7eb7a441014b631f6dc60543b85_LowRes.png)
OAuth 2.0 Authentication
To configure authentication via OAuth 2.0, please make sure your Collibra instance is configured to allow authentication with a bearer token issued by your IdP.
Once you have configured the appropriate JWT settings in Collibra, enter the following credentials in your SAP LeanIX workspace:
  * Collibra Domain: Your Collibra instance domain without schema or trailing slashes. For example, if you access your Collibra instance in the browser with [<https://my-own.collibra.com>], enter <my-own.collibra.com>.
  * Token URL: The endpoint in your IdP that is used to issue an OAuth 2.0 bearer token.
  * Client ID: The client ID with which the bearer token is to be issued.
  * Client Secret: The client secret credential to issue the bearer token.
  * Scopes: Scopes required for accessing the Collibra endpoint. The bearer token is issued with the provided scopes.
  * Credentials Location: Select where to place credentials in the request:
    * Authorization Header: Credentials are sent as a Base64-encoded basic authorization header.
    * URL Encoded Body Request: Credentials are sent in the request body as URL-encoded parameters.
  * Request Body Parameters: A set of key/value pairs to include in the request body.
  * Request Query Parameters: A set of key/value pairs to include as query parameters.
