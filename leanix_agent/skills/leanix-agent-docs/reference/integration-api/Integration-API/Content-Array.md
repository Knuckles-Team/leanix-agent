##  Content Array
The content section contains a list of Data Objects. This section contains the data collected from the external system or the data to be sent to the external system. Each Data Object is defined by an "id" (typically a UUID in the source system), a type to group the source information and a map of data elements. The keys "id", "type" and "data" are mandatory. The data map may be flat or hierarchical maps. Values of map entries may be single string values, maps or lists.
### Mandatory Attributes
The following table lists mandatory attributes for the content array in the input data.
Attribute | Description
---|---
id | Contains a string typically representing a unique identifier that allows to track back the item in the source system and to ensure updates in SAP LeanIX always go to the same Fact Sheet. SAP LeanIX Data processors will provide an efficient matching option to allow configuration of specific mapping rules based on IDs or groups of IDs that can be identified by patterns.
type | A string representing any required high level structuring of the source data. Example content in case of Kubernetes are e.g. "Cluster" (containing data that identifies the whole Kubernetes instance) or "Deployment" (which can represent a type of application in Kubernetes) Will typically be used to create different types or subtypes of Fact Sheets or relations from. SAP LeanIX Data processors will provide an efficient matching option to allow configuration of specific mapping rules based on Type or groups of Type strings that can be identified by patterns.
data | The data extracted from the source system. The format is simple: All data has to be in a Map. Each map can contain a single string as a value for a key, a list of strings as a value or contain a map. The map again has to follow the rules just described.


### Optional Attributes
The following table lists optional attributes for the content array in the input data.
Attribute | Description
---|---
processingMode | May contain "PARTIAL" (default if not existing) or "FULL". Full mode allows to automatically remove all Fact Sheets that match a configured query and are not touched by the integration.
chunkInformation | If existing, it contains "firstDataObject", "lastDataObject" and "maxDataObject". Each value is a number defining what is in this potentially chunked LDIF.
description | The description can contain any string that may help to identify source or type of data. Sometimes it is helpful to add some information to analysis purposes or when setting up configuration on SAP LeanIX side
customFields | This optional section may contain a map of fields and values defined by the producer of the LDIF. All data can be referenced in any data processor. It will be used for globally available custom meta data.
lxWorkspace |  Defines the SAP LeanIX workspace the data is supposed to be sent to or received from. The content will be used for additional validation by the integration API to check if data will be sent to the right workspace. The content has to match the string visible in the URL when accessing the workspace in a browser. Users need to enter the UUID of the workspace in order to make use of this additional security mechanism. The UUID can e.g. be read from the administration page where API Tokens are created. Example "lxWorkspace": "19fcafab-cb8a-4b7c-97fe-7c779345e20e"


**Note**
  * Additional fields in the LDIF that do not match the requirements of defined here will be silently ignored.
  * Each of the values listed above, except the values in the "content" section must not be longer than 500 characters.


Example input data for importing fact sheets:

```
{
  "connectorType": "cloudockit",
  "connectorId": "CDK",
  "connectorVersion": "1.0.0",
  "lxVersion": "1.0.0",
  "lxWorkspace": "workspace-id",
  "description": "Imports Cloudockit data into LeanIX",
  "processingDirection": "inbound",
  "processingMode": "partial",
  "content": [
    {
      "type": "ITComponent",
      "id": "b6992b1d-4e4d",
      "data": {
        "name": "Gatsby.j",
        "description": "Gatsby is a free and open source framework based on React that helps developers build websites and apps.",
        "category": "sample_software",
        "provider": "gcp",
        "applicationId": "28db27b1-fc55-4e44"
      }
    },
    {
      "type": "ITComponent",
      "id": "cd4fab6c-4336",
      "data": {
        "name": "Contentful",
        "description": "Beyond headless CMS, Contentful is an API-first content management infrastructure to create, manage and distribute content to any platform or device.",
        "category": "cloud_service",
        "provider": "gcp",
        "applicationId": "28db27b1-fc55-4e44"
      }
    },
    {
      "type": "ITComponent",
      "id": "3eaaa629-5338-41f4",
      "data": {
        "name": "GitHub",
        "description": "GitHub is a tool that provides hosting for software development version control using Git.",
        "category": "cloud_service",
        "provider": "gcp",
        "applicationId": "28db27b1-fc55-4e44"
      }
    },
    {
      "type": "Application",
      "id": "28db27b1-fc55-4e44",
      "data": {
        "name": "Book a Room Internal",
        "description": "Web application that's used internal to book rooms for a meeting."
      }
    }
  ]
}
```



Example input data for importing lifecycle information:

```
{
  "connectorType": "cloudockit",
  "connectorId": "CDK",
  "connectorVersion": "1.0.0",
  "lxVersion": "1.0.0",
  "lxWorkspace": "workspace-id",
  "description": "Imports Cloudockit data into LeanIX",
  "processingDirection": "inbound",
  "processingMode": "partial",
  "content": [
    {
      "type": "Application",
      "id": "company_app_1",
      "data": {
        "name": "TurboTax",
        "plan": null,
        "phaseIn": "2016-12-29",
        "active": "2019-12-29",
        "phaseOut": "2020-06-29",
        "endOfLife": "2020-12-29"
      }
    },
    {
      "type": "Application",
      "id": "company_app_2",
      "data": {
        "name": "QuickBooks",
        "plan": null,
        "phaseIn": "2016-11-29",
        "active": "2019-11-29",
        "phaseOut": "2020-05-29",
        "endOfLife": "2020-11-29"
      }
    }
  ]
}
```



