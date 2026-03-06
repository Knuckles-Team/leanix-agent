##  Communication with ServiceNow
The communication between the SAP LeanIX integration running on SAP LeanIX servers and the ServiceNow system depends on the configuration specified in ServiceNow URL.
In case the ServiceNow URL is configured with an https schema, the communication is done through TLS encryption. Furthermore, all client credentials are stored as part of the configuration encrypted using theAES-256.
Additionally, the Integration User created can utilize both Basic Auth or oAuth 2.0 for authentication between the two systems.
**Note**
Communication method when using HTTPS Instance URL
The TLS version and cipher suites used for communication between SAP LeanIX and ServiceNow depends on the negotiation to the ServiceNow HTTPS server. In general, TLS v1.2 and TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256 is used for any HTTPS connection to ServiceNow.
Configure the ServiceNow URL and other user details on the Credentials tab on the configuration page.
![Credentials tab for connecting to the ServiceNow Instance](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2744b5507a4410148504937fafd15e94_LowRes.png)
Credentials tab for connecting to the ServiceNow Instance
