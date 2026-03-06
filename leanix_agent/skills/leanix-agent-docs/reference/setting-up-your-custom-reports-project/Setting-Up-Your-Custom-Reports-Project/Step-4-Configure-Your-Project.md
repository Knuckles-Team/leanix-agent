##  Step 4: Configure Your Project
You can change the configuration of your project in the lxr.json and package.json files.
### lxr.json
The lxr.json file contains the configuration for the development server and your SAP LeanIX workspace.
lxr.json

```
{
  "host": "app.leanix.net",
  "workspace": "",
  "apitoken": "{{YOUR_API_TOKEN}}",
  "proxyURL": "",
  "localPort": "8080"
}
```



If you're working behind a proxy, you can specify the proxy URL using the proxyURL property. By default, the development web server runs on port 8080. If this port is already in use by another application on your system, you can modify the port using the localPort property.
The LeanIX Reporting CLI development server generates a self-signed SSL certificate for development purposes. If you prefer to use your own generated SSL certificate, you can specify it using the ssl property.
lxr.json

```
{
  "host": "app.leanix.net",
  "workspace": "",
  "apitoken": "{{YOUR_API_TOKEN}}",
  "proxyURL": "",
  "localPort": "8080",
  "ssl" {
    "cert": "/path/to/cert",
    "key": "/path/to/key"
  }
}
```



### package.json
If you have experience with npm, you know that the package.json file is an essential element of any Node.js project. Understanding how to use the file is required to work with Node.js, npm, and modern JavaScript.
This file is also used in the LeanIX Reporting Library for configuring custom report projects.
The scaffolding process also generates specific settings for the LeanIX Reporting Library in the package.json file.

```
{
  "name": "Custom Reports Demo",
  "author": "LeanIX GmbH",
  "version": "1.0.0",
  "description": "This is a custom reports demo",
  "leanixReport": {
    "id": "custom.reports.demo",
    "title": "Custom Reports Demo",
    "defaultConfig": {}
}
```



The following table contains configurable fields within the package.json file.
Property | Description | Required
---|---|---
name | The name of the project. | Required
version | The version of the custom report as displayed in the workspace. | Required
author | The author of the custom report. | Optional
description | The description of the custom report. | Optional
leanixReport | The object that contains additional information related to the report. | Required


The leanixReport object contains fields listed in the following table.
Property | Description | Required
---|---|---
id | The unique ID of the report. | Required
title | The title of the report that is displayed in the user interface. | Optional
documentationLink | The link to the report documentation. | Optional
defaultConfig | The default configuration object. | Optional


**Note**
id adheres to the [Java package naming convention![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fdocs.oracle.com%2Fjavase%2Ftutorial%2Fjava%2Fpackage%2Fnamingpkgs.html?locale=en-US&state=PRODUCTION&version=CLOUD "https://docs.oracle.com/javase/tutorial/java/package/namingpkgs.html"), which specifies alphanumeric strings with underscores _ and dots . allowed ([a-z,0-9,_,.]).
The id value must not end with a dot or comma. This ensures consistency and readability within the codebase.
The part of the id parameter following the last dot is the unique identifier that is displayed in the reporting menu. To avoid overriding existing reports, ensure that this identifier is unique.
