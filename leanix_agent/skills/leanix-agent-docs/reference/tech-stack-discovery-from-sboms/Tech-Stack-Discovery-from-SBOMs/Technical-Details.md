##  Technical Details
The process of automatically discovering tech stacks from ingested SBOMs involves the following steps:
  1. You ingest SBOMs into SAP LeanIX using the [GitHub Enterprise integration](https://help.sap.com/docs/leanix/ea/github-enterprise-integration?locale=en-US&state=PRODUCTION&version=CLOUD "Set up self-built software discovery using our out-of-the-box integration with GitHub Enterprise Server.") or by directly uploading them through the [Self-Built Software Discovery API![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Feu.leanix.net%2Fservices%2Ftechnology-discovery%2Fv1%2Fopenapi%2Fswagger-ui%2Findex.html%23%2F "https://eu.leanix.net/services/technology-discovery/v1/openapi/swagger-ui/index.html#/").
Here is an example request that demonstrates how to upload SBOMs using the Self-Built Software Discovery API:

```
curl --request POST \
  --url https://{SUBDOMAIN}.leanix.net/services/technology-discovery/v1/factSheets/{factSheetId}/sboms \
  --header 'Authorization: Bearer {TOKEN}' \
  --header 'Content-Type: multipart/form-data' \
  --form 'sbom=@/Documents/SBOM.json;type=application/json'

```



  2. The system parses individual SBOM components to produce the SBOM view.
  3. Asynchronously, the backend processes the SBOM components provided as part of the SBOM. It matches them against the reference catalog using the core [purl![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fgithub.com%2Fpackage-url%2Fpurl-spec%2Fblob%2Fmaster%2FPURL-SPECIFICATION.rst "https://github.com/package-url/purl-spec/blob/master/PURL-SPECIFICATION.rst").
There might be a delay of a few seconds between SBOM ingestion through the API and tech stack creation. This delay occurs because we use eventing for library processing. Learn more about [eventual consistency![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fen.wikipedia.org%2Fwiki%2FEventual_consistency "https://en.wikipedia.org/wiki/Eventual_consistency").
Example: For the incoming purl pkg:maven/org.springframework.boot/[spring-boot-starter@2.3.5](mailto:spring-boot-starter@2.3.5), here's the JSON of the matched IT component:

```
{
  "name": "Spring Boot",
  "purl": "pkg:maven/org.springframework.boot/spring-boot-starter",
  "description": "Spring Boot makes it easy to create stand-alone, production-grade Spring based Applications that you can 'just run'. It simplifies Spring configuration."
}

```



  4. If the system finds a match, it uses the microservice ID from step 1 to create an IT component of subtype software for the microservice fact sheet.


![Discovered IT Component](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2746c8a37a441014838594d77ea5da24_LowRes.png)
IT Component Discovered from a SBOM
