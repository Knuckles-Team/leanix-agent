# Setup in ServiceNow
### On this page
  * [Create a Technical User](https://help.sap.com/docs/leanix/ea/setup-in-servicenow#create-a-technical-user)
  * [Installation of LeanIX Integration App](https://help.sap.com/docs/leanix/ea/setup-in-servicenow#installation-of-leanix-integration-app)
  * [Update SAP LeanIX Integration App (for admins)](https://help.sap.com/docs/leanix/ea/setup-in-servicenow#update-sap-leanix-integration-app-\(for-admins\))
  * [Configuration and Setup of Integration User](https://help.sap.com/docs/leanix/ea/setup-in-servicenow#configuration-and-setup-of-integration-user)
  * [Create an Integration user](https://help.sap.com/docs/leanix/ea/setup-in-servicenow#create-an-integration-user)
  * [Customised System Tables in ServiceNow](https://help.sap.com/docs/leanix/ea/setup-in-servicenow#customised-system-tables-in-servicenow)
  * [Optional: Add ACLs in ServiceNow](https://help.sap.com/docs/leanix/ea/setup-in-servicenow#optional:-add-acls-in-servicenow)
  * [Optional: Enable OAuth 2.0 for Authentication](https://help.sap.com/docs/leanix/ea/setup-in-servicenow#optional:-enable-oauth-2.0-for-authentication)


View all
Configure the ServiceNow integration on the ServiceNow side.
The following document assumes that there are point of contacts ready both on the SAP LeanIX side (SAP LeanIX admin user) and ServiceNow (ServiceNow Instance admin) who have the necessary rights and roles within the organization to make the outlined changes.
Steps order | Step | Details
---|---|---
1 | Activation of the Integration on the SAP LeanIX side | You may reach out to support at [SAP LeanIX Support![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fwww.leanix.net%2Fsupport "https://www.leanix.net/support") or reach out to your CSM to ensure the integration is activated on your workspace. If you're an SAP customer, submit a request from the [SAP for Me![Information published on SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/sap_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fme.sap.com%2F "https://me.sap.com/"). Proceed only after the confirmation.
2. | Create a technical user | Technical user created on the SAP LeanIX side that generates an API Token to be set on the ServiceNow side. It is also used as a Managing User which is detailed in the [Setup in SAP LeanIX](https://help.sap.com/docs/leanix/ea/setup-in-sap-leanix?locale=en-US&state=PRODUCTION&version=CLOUD "After configuring the SAP LeanIX app in ServiceNow, set up the integration in SAP LeanIX.") section.
3. | Installation of the SAP LeanIX Integration App(s) |  [ServiceNow Store![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fstore.servicenow.com%2Fsn_appstore_store.do%23%21%2Fstore%2Fsearch%3Fq%3Dleanix "https://store.servicenow.com/sn_appstore_store.do#!/store/search?q=leanix")
4. | Configuration & Setup of Integration User | [Configuration and Setup of Integration User](https://help.sap.com/docs/leanix/ea/setup-in-servicenow?locale=en-US&state=PRODUCTION&version=CLOUD#loio275cc0f97a441014ab90fe667ea172ba__configuration_setup_of_integration_user)
5. | Additional Information | Additional information related to the configuration depends on use-cases.


Once the integration is activated on the SAP LeanIX workspace, you can leverage the Sandbox workspace to ensure data mappings and incoming data are correct before moving to the Production workspace.
**Tip**
Ensure that data imported from ServiceNow follows our formatting guidelines. For example, field values must not contain symbols such as < (less than) or ; (semicolon). For additional information, see [General Formatting Rules](https://help.sap.com/docs/leanix/ea/importing-fact-sheet-data-through-excel-file?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a86917a441014872eecad909f5e9e__general_formatting_rules).
