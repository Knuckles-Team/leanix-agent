##  Step 3: Make Authenticated Requests to Services
After obtaining an access token, you can use it to make authenticated requests to SAP LeanIX services.
To authorize your request, insert your access token into the Authorization header. Be sure to include the Bearer prefix to specify the token type.
As an example, let's fetch a list of Applications, internally referred to as services, from the IT Inventory of a Workspace.
**Note**
Reuse the access token in your API requests within the token lifetime. Do not request new access tokens while the current token is still valid.
Repeatedly requesting new tokens without necessity may lead to security vulnerabilities and unnecessary load on the authorization server. Adhere to the token expiration time and only request a new token when necessary.
In the following example request, the access token (eyJhbGciOiJSUzI1NiJ9.eyJz [...] ssqaPSA) is shortened. When implementing this in your applications, ensure that you use a complete and unaltered access token.
Example request:
cURL

```
curl -H "Authorization: Bearer {ACCESS_TOKEN}" \
	https://{SUBDOMAIN}.leanix.net/services/poll/v2/pollRuns
```



JavaScript

```
const axios = require('axios');

// Replace {SUBDOMAIN} with your actual subdomain
const url = 'https://{SUBDOMAIN}.leanix.net/services/poll/v2/pollRuns';
const accessToken = 'eyJhbGciOiJSUzI1NiJ9.eyJz [...] ssqaPSA'; // Replace with your actual access token

// Step 2: Make a GET request to the /v1/services API endpoint
axios.get(url, {
  headers: {
    'Authorization': `Bearer ${accessToken}`,
  },
})
  .then(response => {
    // Process the response as needed
    console.log(response.data);
  })
  .catch(error => {
    console.error('Error:', error.message);
  });
```



Java

```
OkHttpClient client = new OkHttpClient();

Request request = new Request.Builder()
  .url("https://{SUBDOMAIN}.leanix.net/services/poll/v2/pollRuns")
  .get()
  .addHeader("Authorization", "Bearer eyJhbGciOiJSUzI1NiJ9.eyJz [...] ssqaPSA")
  .build();

Response response = client.newCall(request).execute();
```



Python

```
import requests

timeout = 20
url = 'https://{SUBDOMAIN}.leanix.net/services/poll/v2/pollRuns'
headers = {'Authorization': 'Bearer eyJhbGciOiJSUzI1NiJ9.eyJz [...] ssqaPSA'}

response = requests.get(url, headers=headers, timeout=timeout)

# Process the response as needed
print(response.text)
```



