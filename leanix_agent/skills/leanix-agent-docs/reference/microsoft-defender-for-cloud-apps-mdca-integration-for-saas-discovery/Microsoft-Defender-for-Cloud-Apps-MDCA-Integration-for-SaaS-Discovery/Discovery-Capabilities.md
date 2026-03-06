##  Discovery Capabilities
Available capabilities | Description | MDCA resource
---|---|---
SaaS Discovery (Standard) | SaaS discovery automatically identifies your organization's SaaS applications. | Discovered Apps
Usage Indication (Optional) | Provides insights into how users in your organization access applications. This helps you make informed decisions about adding discovered applications to the inventory. | Active Users (Over the past month)


You get the following information about the discovered SaaS:
Field | Description
---|---
External Category |
Description | Description of the SaaS.
Organization | Indicates the parent company.
HQ Location | The country/region of the provider's headquarters.
Supports SAML | Indicates whether the application supports SAML as a sign-on mode.
Active Users* | Number of users using an application in the last 30 days.
Sanctioned State | Indicates whether an application is approved and safe (Sanctioned) or prohibited and unwanted apps (Unsanctioned)
IP Addresses Count | Indicates how many IP addresses have accessed this application.
Upload Bytes | Information about the total amount of traffic (in MB) uploaded by the device over the selected period of time.
Download Bytes | Information about the total amount of traffic (in MB) downloaded by the device over the selected period of time.
Total Bytes | Information about the total amount of traffic (in MB) over the selected period of time.
Total Events |
Blocked Events |
Revised Total Security Score | The revised total security score is a measure of the security posture of your applications and systems. It is calculated based on various factors, such as the number of applications scanned, the number of threats detected, and the number of threats removed. A higher revised total security score indicates that your applications and systems are more secure.
First Used | Indicates when the app was first used.
Last Modified | Indicates the date and time when the application's metadata was last updated. This includes information such as the application name, publisher, version, file path, and more. If you notice that an application's last modified date has changed, you should investigate the application to determine if it has been modified by malware or if it is simply being updated by the application's publisher.
Last seen at | Last time the discovered SaaS was seen in the source system
Item status in source |  Status of the discovered SaaS in the source system. It can be the following:
  * Active: The application has been seen in Microsoft Defender for Cloud Apps in the last week.
  * Inactive: The application has not been seen in the last week.


TID |
Stream ID |


*Shown only if you enable Usage Indication capability in the configuration settings. To learn how, see [Enter the Copied Credentials in SAP LeanIX](https://help.sap.com/docs/leanix/ea/microsoft-defender-for-cloud-apps-mdca-integration-for-saas-discovery?locale=en-US&state=PRODUCTION&version=CLOUD#loio275b305c7a441014baf6d28ea63f74a4__enter_the_copied_credentials_in_sap_leanix).
