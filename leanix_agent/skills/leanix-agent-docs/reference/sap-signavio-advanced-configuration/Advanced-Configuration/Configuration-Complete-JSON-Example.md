##  Configuration Complete JSON Example
A complete sample configuration structure is shown below. It is a JSON map where top level keywords represents global options that are applied to every synchronization. The sample list has been obfuscated to hide sensitive information, it is intended to be used only as a reference , not to be copied into your configuration.

```
{
 "active": true,
 "timerBasedSync": false,
 "strict": false,
 "processFactSheetType": "Process",
 "leanixConfig": {
  "workspaceId": "XXXXXX-5391-40c7-a47e-YYYYYY",
  "targetSystem": "https://url.for.server",
  "userId": "xxxxxxx-336a-4092-ae60-yyyy"
 },
 "signavioConfig": {
  "url": "https://editor.signavio.com",
  "username": "user@company.net",
  "password": "xxxxxxxxxx-xxxxxxxxxx",
  "tenantId": "f6a3ca755bec1e13xxfeb",
  "loginParams": ""
 },
 "glossaryCategorySyncDescriptors": [
  {
   "active": true,
   "factSheetType": "Application",
   "masterSite": "LEANIX",
   "strict": false,
   "relationName": "relProcessToApplication",
   "inboundMappings": [],
   "filter": null,
   "glossaryCategoryId": "d693d09****f87e290"
  }
 ],
 "processSyncDescriptors": [
  {
   "inboundMappings": [],
   "active": false,
   "directoryIds": [
    "1111111111111111"
   ],
   "linkProcessingMode": "NO_PROCESSING",
   "publishedOnly": false,
   "startNodeId": null,
   "leanixParentFactSheetId": null,
   "blacklist": [],
   "shortDescription": ""
  }
 ]
}

```



The corresponding Basic section for the previous Advanced data configuration is shown in the following image.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274c42a67a441014a609b4c76ce430b2_LowRes.png)
We can identify some elements between both sections, like the strict property, set to False as it is unchecked in the Basic section, similarly, the property processFactSheetType represents the Fact Sheet Type field set as Process, and the rows we have in sections SAP Signavio Processes and Glossary Category Mappings are kept in processSyncDescriptors and glossaryCategorySyncDescriptors properties in the structure.
Because almost all elements in the configuration are easily managed by using the Basic section, we will explain in detail the inboundMappings property where we will find elements that can be extended only using the Advanced section.
