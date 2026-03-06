##  Discovery Capabilities
Zscaler integration offers the following capabilities:
Available Capabilities | Description | Zscaler Resource
---|---|---
SaaS Discovery (Standard) | SaaS discovery automatically identifies your organization's SaaS applications. | Discovered apps
Usage Indication (Standard) | Provides insights into how users in your organization access applications. This helps you make informed decisions about adding discovered applications to the inventory. | Active users (Over the past month)


You get the following information about the discovered SaaS:
Field | Description
---|---
External Category |
Locations | The number of unauthenticated locations from where the application is accessed.
Application Status | The application status, whether it's sanctioned or unsanctioned.
Active Users* | The total number of users using the application in the last 30 days.
Upload Bytes | The total upload data bytes for the application.
Download Bytes | The total download data bytes for the application.
Total Bytes | The total bytes consumed by the application, both upload and download.
Application Risk Index | The risk index for the applications.
Data Breaches in Last 3 Years | Indicates whether there have been data breaches in the last 3 years for the application (yes/no).
MFA Support | Indicates whether the application supports MFA (yes/no).
Certifications | If applicable, this field shows the application's certifications (e.g., HIPAA).
Tags | The tags assigned to the application.
Notes | The notes that you added for the application on the Application Information page. The column stays blank if you haven't added any notes.
Potential Integrations | The number of potential integrations associated with the application in your organization. For example, if your organization uses Grammarly and the application shows at least one integration in this column, then Grammarly has potential access to your corporate SaaS platforms, such as Google Workspace.
Last seen at | Last time the discovered SaaS was seen in the source system
Item status in source |  Status of the discovered SaaS in the source system. It can be the following:
  * Active: The application has been seen in Zscaler in the last week.
  * Inactive: The application has not been seen in the last week.




*Shown only if you enable Usage Indication capability in the configuration settings. To learn how, see [Enter the Necessary Credentials in SAP LeanIX](https://help.sap.com/docs/leanix/ea/zscaler-integration-for-saas-discovery?locale=en-US&state=PRODUCTION&version=CLOUD#loio275e48807a441014941bb71072c6d2d9__enter_the_necessary_credentials_in_sap_leanix).
