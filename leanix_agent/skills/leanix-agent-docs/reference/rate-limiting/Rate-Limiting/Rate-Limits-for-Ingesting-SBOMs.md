##  Rate Limits for Ingesting SBOMs
The SBOM ingestion endpoint /technology-discovery/v1/factSheets/{factSheetId}/sboms on the [Self-Built Software Discovery API![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fapp.leanix.net%2Fopenapi-explorer%2F%3Furls.primaryName%3DSelf-Built%2BSoftware%2BDiscovery "https://app.leanix.net/openapi-explorer/?urls.primaryName=Self-Built+Software+Discovery") enforces a rate limit of 300 requests per minute per workspace. If you exceed this limit, you receive a 429 Too Many Requests response.
Ensure your integrations handle 429 responses with retry logic and exponential backoff:
To learn more about self-built software discovery and ingesting SBOMs, refer to:
  * [Self-Built Software Discovery](https://help.sap.com/docs/leanix/ea/self-built-software-discovery?locale=en-US&state=PRODUCTION&version=CLOUD "SAP LeanIX Technology Risk and Compliance enables you to automate the discovery of your self-built software by integrating this process into your developer toolchain.")
  * [Step 4: Upload the Manifest File](https://help.sap.com/docs/leanix/ea/microservice-discovery-in-your-ci-cd-pipeline?locale=en-US&state=PRODUCTION&version=CLOUD#loio275b281a7a4410149cec9b547ba635be__step_4_upload_the_manifest_file)


YesNo
Send
