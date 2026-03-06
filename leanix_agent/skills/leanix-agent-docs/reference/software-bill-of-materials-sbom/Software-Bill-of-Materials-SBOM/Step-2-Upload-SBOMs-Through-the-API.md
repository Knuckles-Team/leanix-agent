##  Step 2: Upload SBOMs Through the API
Upload SBOMs into SAP LeanIX: Ingest your SBOMs into SAP LeanIX using the [Self-Built Software Discovery API![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Feu.leanix.net%2Fservices%2Ftechnology-discovery%2Fv1%2Fopenapi%2Fswagger-ui%2Findex.html?locale=en-US&state=PRODUCTION&version=CLOUD "https://eu.leanix.net/services/technology-discovery/v1/openapi/swagger-ui/index.html"). The API integrates seamlessly with your build processes, allowing for automatic ingestion of SBOM data generated during your software's build process. This ensures a near real-time view of your software composition.
Currently, the API doesn't detect individual versions of the underlying technologies that carry a lifecycle to then link them to the reference catalog. The API only supports technology standards management capabilities (not obsolescence risk management). To learn more about automated tech stack discovery from SBOMs, see [Tech Stack Discovery from SBOMs](https://help.sap.com/docs/leanix/ea/tech-stack-discovery-from-sboms?locale=en-US&state=PRODUCTION&version=CLOUD "Automatically discover tech stacks from ingested SBOMs. Add custom tech stacks manually to complete your technology portfolio.").
To upload a SBOM file and link it to a fact sheet, make a POST request to the /factSheets/{factSheetId}/sboms endpoint. This endpoint enforces a rate limit of 300 requests per minute per workspace. If you exceed this limit, you receive a 429 Too Many Requests response.
To learn how to authenticate your API requests, refer to [Authentication to SAP LeanIX Services](https://help.sap.com/docs/leanix/ea/authentication-to-sap-leanix-services?locale=en-US&state=PRODUCTION&version=CLOUD "Learn how to authenticate to SAP LeanIX services.").
Example cURL request:
**Sample Code**

```
curl --request POST \
  --url https://{SUBDOMAIN}.leanix.net/services/technology-discovery/v1/factSheets/{factSheetId}/sboms \
  --header 'Authorization: Bearer {TOKEN}' \
  --header 'content-type: multipart/form-data' \
  --form 'sbom=@/Documents/SBOM.json;type=application/json'

```



