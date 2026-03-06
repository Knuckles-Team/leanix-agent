##  General Guidelines and Best Practices for SAP BTP Modeling
The SAP BTP is the current technical platform for building extensions to your SAP ERP. Going forward, it is expected to become the primary platform for your ERP system. Setting up your account model in SAP BTP becomes a critical aspect of designing your future SAP ERP system. Therefore, your Subaccount structure should properly reflect the structure suggested in the platform fact sheets. It's important to make an informed decision on whether to have only Subaccounts used for production or to provide a more comprehensive view.
![Example of Account Model With Directories and Subaccounts](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2748c0647a441014892cec37acf3e3ba_LowRes.png)
Example of Account Model With Directories and Subaccounts
The best-practice way to model SAP BTP in SAP LeanIX is as follows:
  * Define your SAP BTP account structure with the platform fact sheet, which reflects SAP BTP's logical governance structure. It consolidates all your SAP BTP Global and Subaccounts, showing responsibility and potentially costs for major BTP elements.
    * Start with SAP Business Technology as level 1. This will allow you to filter your landscape to SAP BTP.
    * Model Global Accounts on level 2 and Subaccounts on level 3.
    * <Optional:> model directories and spaces if it helps to create views that are relevant to your organization.
    * <Optional:> Add additional information, like cost centers, using tags.
![Platform Landscape Report Showing Global Accounts at Level 2, and Directory at Level 3](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27516f077a44101497dbda2747ed55e2_LowRes.png)
Platform Landscape Report Showing Global Accounts at Level 2, and Directory at Level 3
  * To automate the process, retrieve the Subaccount structure through an API from SAP BTP Cockpit and import costs from the BTP Cockpit to SAP LeanIX. To learn more about the APIs, see [Core Services of SAP BTP![Information published on SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/sap_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fapi.sap.com%2Fpackage%2FSAPCloudPlatformCoreServices%2Frest "https://api.sap.com/package/SAPCloudPlatformCoreServices/rest").
  * Define objectives and intiatives to build up your SAP BTP instance to your strategic ERP platform of the future. You can also link other objectives and initiatives to your platform fact sheets.
  * Link fact sheets from the business architecture layer (organization, business capability, business context) to get a good understanding of the business value of your SAP BTP solutions.
  * Model custom-built and deployed apps on SAP BTP with application fact sheets. We suggest focusing on major applications that address business challenges, such as customized Fiori apps. In the BTP Cockpit, HTML5 applications would be an application in SAP LeanIX. Link the applications to the platform in which they are deployed.
![You HTML5 Application Documented Using Application Fact Sheet](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274cd5827a441014af87c2a5a27a8b42_LowRes.png)
You HTML5 Application Documented Using Application Fact Sheet
  * Connect these applications to the relevant PaaS services using IT component fact sheets and link them to underlying SAP ERP systems via interface fact sheets if they retrieve data from those systems.
  * By linking to IT components, you can document the region and cloud provider used for each Subaccount.
![Documenting Used Region and Cloud Provider for a Subaccount](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275367f07a441014ae36c8886d075315_LowRes.png)
Documenting Used Region and Cloud Provider for a Subaccount
  * Import all SAP BTP PaaS services and assess them based on your organization's requirements. Stay with generic services and avoiding modeling all instances of a service. Instead, link them to the platforms and applications where they are used.


**Note**
  * To learn more about various fact sheet types and how to use them, see [Fact Sheet Modeling Guidelines](https://help.sap.com/docs/leanix/ea/fact-sheet-modeling-guidelines?locale=en-US&state=PRODUCTION&version=CLOUD).
  * To learn about SAP LeanIX meta model v4, see [Meta Model](https://help.sap.com/docs/leanix/ea/meta-model?locale=en-US&state=PRODUCTION&version=CLOUD "Get an overview of the SAP LeanIX meta model and its key concepts.").


![Fact Sheets for SAP BTP Modeling](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274dd44d7a4410148ac8a3034f71078d_LowRes.png)
Fact Sheets for SAP BTP Modeling
A typical hybrid SAP and BTP landscape would look like this in SAP LeanIX:
![Modeling SAP BTP](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274318d57a441014a5fe91b12426bcae_LowRes.png)
Modeling SAP BTP
