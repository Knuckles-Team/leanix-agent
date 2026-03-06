##  Step 2: Get an Access Token
Now that you have an API token, you can obtain an access token.
### Request an Access Token
To request an access token, make a POST request to the following endpoint:

```
https://{SUBDOMAIN}.leanix.net/services/mtm/v1/oauth2/token
```



This API uses the Basic HTTP authentication scheme. For more information, see [The 'Basic' HTTP Authentication Scheme![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fwww.rfc-editor.org%2Frfc%2Frfc7617 "https://www.rfc-editor.org/rfc/rfc7617") section of the Internet Standards Track document issued by the Internet Engineering Task Force (IETF).
For credentials, use apitoken as the username and the obtained API token as the password. Set the grant_type to client_credentials.
The following examples show how to make a request to obtain an access token. JAANYFMYQcNtZ6ettSH9pF88RLdVBGfuY6bDFThw is an example API token that we use for illustrative purposes.
Example request:
cURL

```
curl -u apitoken:JAANYFMYQcNtZ6ettSH9pF88RLdVBGfuY6bDFThw \
	--request POST https://{SUBDOMAIN}.leanix.net/services/mtm/v1/oauth2/token \
	--data grant_type=client_credentials
```



JavaScript

```
const axios = require('axios');
const qs = require('qs');
const username = "apitoken"
const password = "JAANYFMYQcNtZ6ettSH9pF88RLdVBGfuY6bDFThw"
const data = { 'grant_type': 'client_credentials'};
const instance = "https://{SUBDOMAIN}.leanix.net";
const tokenEndpoint = "https://{SUBDOMAIN}.leanix.net/services/mtm/v1/oauth2/token"

// Step 2: Make a POST request to obtain the access token
const getToken = async () => {
  try {
    const response = await axios.post(
      tokenEndpoint,
      data: qs.stringify(data),
      {
        auth: {
          username: username,
          password: password,
        },
        headers: {
          'Content-Type': 'application/x-www-form-urlencoded',
        },
      }
    );

    // Step 3: Receive and use the access token
    const accessToken = response.data.access_token;
  } catch (error) {
    console.error('Error obtaining access token:', error.message);
  }
};
```



Java

```
OkHttpClient client = new OkHttpClient();

MediaType mediaType = MediaType.parse("application/x-www-form-urlencoded");
RequestBody body = RequestBody.create(mediaType, "grant_type=client_credentials");
Request request = new Request.Builder()
  .url("https://{SUBDOMAIN}.leanix.net/services/mtm/v1/oauth2/token")
  .post(body)
  .addHeader("Authorization", Credentials.basic("apitoken", "JAANYFMYQcNtZ6ettSH9pF88RLdVBGfuY6bDFThw"))
  .build();

Response response = client.newCall(request).execute();
```



Python

```
import requests

# Set a timeout to prevent hanging requests
TIMEOUT = 10
OAUTH2_URL = "https://{SUBDOMAIN}.leanix.net/services/mtm/v1/oauth2/token"

# Step 2: Make a POST request to obtain the access token, for obtain the access token we
# use the Basic Authorization scheme, you can implement this by using the `auth` parameter
# of the requests library.
response = requests.post(
    OAUTH2_URL,
    auth=("apitoken", "JAANYFMYQcNtZ6ettSH9pF88RLdVBGfuY6bDFThw"),
    data={"grant_type": "client_credentials"},
    timeout=TIMEOUT,
)
# Check if the request was succesfull
response.raise_for_status()
# The access token is available under the `access_token` response field.
response_payload = response.json()
access_token = response_payload["access_token"]

```



### Review the Response
The response from the https://{SUBDOMAIN}.leanix.net/services/mtm/v1/oauth2/token endpoint includes your access token. Handle the response according to your programming language or tool.
Example response:

```
{
 "scope":"",
 "expired":false,
 "access_token":"eyJhbGciOiJSUzI1NiJ9.eyJz [...] ssqaPSA",
 "token_type":"bearer",
 "expires_in":3599
}
```



The access_token is returned in JWT (JSON Web Token) format. JWTs are encoded tokens that carry information in a compact and self-contained manner. In the context of OAuth 2.0, access tokens are often JWTs.
Tokens are signed with a private key, enabling our APIs to validate their authenticity. The signing process ensures that the token has not been tampered with and comes from a trusted source.
You can decode your access token using tools such as [JWT.IO![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=http%3A%2F%2Fjwt.io%2F "http://jwt.io/"). Once you have decoded your token, you can view the token details, such as:
  * Permissions: Information about the user's permissions or scope, indicating what actions or resources the token holder is authorized to access.
  * Expiration time: The validity duration of the access token in seconds is specified in expires_in. The access token is valid for 3600 seconds, which is equivalent to one hour.


**Note**
OAuth 2.0 access tokens often have a limited lifespan for security purposes. By setting an expiration time, the system can automatically revoke access after a certain period, minimizing the risk of unauthorized access if the token is compromised. This practice is part of the OAuth 2.0 security model to ensure that tokens are regularly refreshed, requiring the client to reauthenticate to obtain a new valid token.
