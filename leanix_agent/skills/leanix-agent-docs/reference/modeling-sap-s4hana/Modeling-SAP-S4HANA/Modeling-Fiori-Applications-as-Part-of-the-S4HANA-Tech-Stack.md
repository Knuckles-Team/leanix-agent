##  Modeling Fiori Applications as Part of the S4/HANA Tech Stack
With the introduction of SAP S/4HANA, Fiori applications are an integral part of the SAP landscape. SAP provides a set of standard Fiori apps that can be customized to fit your organization's needs. Additionally, you can create custom Fiori apps using different SAP programming models ([RAP](https://help.sap.com/docs/ABAP_PLATFORM_NEW/fc4c71aa50014fd1b43721701471913d/289477a81eec4d4e84c0302fb6835035.html "https://help.sap.com/docs/ABAP_PLATFORM_NEW/fc4c71aa50014fd1b43721701471913d/289477a81eec4d4e84c0302fb6835035.html") or [CAP![Information published on SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/sap_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fcap.cloud.sap%2Fdocs%2F "https://cap.cloud.sap/docs/")). To learn more about standard Fiori apps, see
Fiori applications generally fall into two categories:
  * Standard Fiori Apps: These apps are used mostly as delivered by SAP, supporting standard processes and functionalities in SAP S/4HANA. They function more like components within the system.
  * Custom Fiori Apps: These apps are either developed in-house or customized from the standard set. They add specific value, create custom outputs, create documents, or have a high significance in differentiating your organization.


Our best practice is to model only custom Fiori apps in SAP LeanIX as level-3 applications under the SAP line of business application. We recommend against modeling a large number of standard Fiori apps, as this adds unnecessary complexity to your application repository without providing significant value.
YesNo
Send
