##  Creating a Fact Sheet in the Inventory
Creating a fact sheet in the inventory is more than filling out a form; it’s about ensuring sufficient data quality to provide meaningful value to your organization. Key features that support this include:
  * Data from reference catalog: While creating fact sheets, as you type the name of the fact sheet, you get matching fact sheet recommendations from the reference catalog. Selecting a recommendation pre-fills the fact sheet with essential information from the catalog. To learn about the reference catalog, see [Reference Catalog](https://help.sap.com/docs/leanix/ea/reference-catalog?locale=en-US&state=PRODUCTION&version=CLOUD "The reference catalog provides reference data for business capabilities, applications, IT components, and tech categories, which enables you to set up and maintain your inventory more efficiently.")
  * Mandatory subscriber assignment: Admins can enforce that the fact sheet creators assign a subscriber while creating the fact sheet. To do so, admins need to make a subscription type or a subscription role a mandatory attribute. This ensures accountability and responsibility for maintaining data quality. To learn more, see [Fact Sheet Subscription](https://help.sap.com/docs/leanix/ea/fact-sheet-subscription?locale=en-US&state=PRODUCTION&version=CLOUD "Fact sheet subscription assigns responsibility and accountability to users for maintaining data. Learn about fact sheet subscriptions, including types, roles, and how to assign and subscribe to fact sheets to promote stakeholder involvement and ensure data accuracy and completeness."). To learn about mandatory attributes, see [Mandatory Attributes](https://help.sap.com/docs/leanix/ea/mandatory-attributes?locale=en-US&state=PRODUCTION&version=CLOUD "Mandatory attributes are essential fields specified by admins to ensure data integrity and quality in fact sheets. They must be filled out for fact sheets to approve quality seal, ensuring consistent and reliable information.").
  * Avoiding duplicate fact sheet creation: As you type the fact sheet's name, you also get a list of existing fact sheets in your inventory that match the name. Selecting a fact sheet lets you preview its information in the right-side pane, helping you avoid creating duplicates.
  * Quick access via URL: You can access the fact sheet creation form directly using its URL. You can share it with relevant stakeholders and contributors in your organization to involve them in building the inventory. For example:
    * https://leanix.net/companyDomain/inventory/factsheet/new - replace "companyDomain" with your workspace domain.
    * https://leanix.net/companyDomain/inventory/factsheet/new?factSheetType=ExampleType - replace "companyDomain" with your workspace domain and "ExampleType" with any valid fact sheet type in your workspace.


### Creating a Fact Sheet
To create a fact sheet, do the following:
  1. Navigate to the Inventory tab of your workspace.
  2. At the top, click New Fact Sheet. This leads to the fact sheet creation form.
  3. Type in the name of the fact sheet. This gives you a list of recommendations and also existing matching fact sheets.
  4. You can either:
    1. You can select a recommended item and click Use Recommendation. A preview of the available information is shown in the right-side pane before you confirm. Using a recommendation pre-fills the fact sheet with essential information from the catalog.
    2. Or, you can click Continue Without Recommendation if the fact sheet you are creating is not available in the reference catalog or if no suitable match is found. In this case, you can create the fact sheet from scratch by filling in the required attributes.
  5. Fill in the necessary fields and click Create and Open to finish, or Create and Start Another to continue creating more fact sheets.


![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiob5bd70f9e6844187a6c6e4cfadf63679_LowRes.gif)
Creating a Fact Sheet
**Tip**
While creating the fact sheet, if you do not know who to assign as a subscriber, you can temporarily assign it to yourself and then assign it to the right person later.
**Note**
  * Note a limitation: only subscription roles specifically defined as accountable, responsible, or observer are available in the fact sheet creation form. Subscription roles set to 'all' type, even when made mandatory, will not appear in the form. To learn about subscription role creation, see [Creating a Subscription Role](https://help.sap.com/docs/leanix/ea/subscription-roles?locale=en-US&state=PRODUCTION&version=CLOUD#loio275af3a27a4410148eada5eb5d54814b__creating_a_subscription_role)
  * If you are unable to add the same user as a subscriber under multiple roles, it means your admin has restricted multiple subscriptions in the settings. To learn more, see [Restricting Multiple Subscriptions from the Same User to a Fact Sheet](https://help.sap.com/docs/leanix/ea/subscription-roles?locale=en-US&state=PRODUCTION&version=CLOUD#loio275af3a27a4410148eada5eb5d54814b__restricting_multiple_subscriptions_from_the_same_user_to_a_fact_sheet)
  * When creating a fact sheet from the recommendations, if you are unable to change the fact sheet’s name, it is because, in the reference catalog settings, your admin has chosen to sync the name field from the reference catalog.
