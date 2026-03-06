##  Enriching IT Component Details from the Reference Catalog
Connecting IT components to the reference catalog enriches fact sheets with curated data from the catalog, improving data quality. It helps you build a more consistent and better-governed IT inventory:
  * It ensures naming consistency across fact sheets and helps avoid duplicates when multiple import methods are used.
  * Linked fact sheets stay automatically updated when catalog information changes, ensuring your inventory reflects the latest information.
  * You get vendor lifecycle data to manage technology obsolescence risks.
  * Linking to the catalog helps automatically establish relationships between other fact sheets, following best-practice modeling, so you get a complete and accurate picture of your IT landscape.


As an admin, you can configure how to use catalog data for IT component fact sheets. For a detailed guide, see [IT Components in the Reference Catalog](https://help.sap.com/docs/leanix/ea/it-components-in-reference-catalog?locale=en-US&state=PRODUCTION&version=CLOUD "By using reference data for IT component fact sheets, you can increase standardization and data quality, set relations to other fact sheets for best-practice modeling, as well as manage technology obsolescence risks by using vendor lifecycle information.").
If you have IT components already in your inventory that aren't linked to the reference catalog, you can link them manually. This is common when you've imported data from spreadsheets or created fact sheets manually before catalog linking was configured. The most efficient way to link IT components is through automatic linking during the import or discovery process. When you use these methods, IT components are linked to the reference catalog automatically.
### Manual Linking
Once the reference catalog is configured, you can manually link the IT components in the following way:
Ways of Manual Linking Ways of Manual Linking | Illustration
---|---
Link multiple IT component fact sheets in bulk in the reference catalog. For a detailed guide, see [Bulk Linking IT Component Fact Sheets](https://help.sap.com/docs/leanix/ea/it-components-in-reference-catalog?locale=en-US&state=PRODUCTION&version=CLOUD#loio275adf737a44101482dccd5ff2ab307e__bulk_linking_it_component_fact_sheets_from_the_inventory). If you have imported IT component fact sheets through an Excel spreadsheet, then this method is particularly suitable for you. |  ![Linking Multiple It Component Fact Sheets in Bulk in the Reference Catalog](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2e0e864e16464bbeb4243d5f1840e2bf_LowRes.png) Linking Multiple It Component Fact Sheets in Bulk in the Reference Catalog
Link individual fact sheets from the right side pane of the fact sheet. For a detailed guide, see  [Linking an IT Component Fact Sheet from the Fact Sheet Page](https://help.sap.com/docs/leanix/ea/it-components-in-reference-catalog?locale=en-US&state=PRODUCTION&version=CLOUD#loio275adf737a44101482dccd5ff2ab307e__linking_an_it_component_fact_sheet_from_the_fact_sheet_page). |  ![Linking Individual Fact Sheets from the Right Side Pane of the Fact Sheet](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio9604bfc0c1354ac9b8af8a7648d73168_LowRes.png) Linking Individual Fact Sheets from the Right Side Pane of the Fact Sheet
When you are manually creating an IT component, if you choose to create from a recommendation, then the fact sheet is also linked to the catalog item.  |  ![Linking to Reference Catalog While Creating Fact Sheet](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loioc9e28c9cdbd64940ba11c349046a7365_LowRes.png) Linking to Reference Catalog While Creating Fact Sheet


### Automatic Linking
Scenarios of Automatic Linking Scenarios of Automatic Linking | Detail
---|---
SAP discovery | When importing IT component fact sheets through SAP Discovery, any IT component that you create or any IT component you link to a discovered item is automatically linked to the corresponding catalog item.
Inventory builder | When importing IT component fact sheets through inventory builder, any IT component that you create or any IT component you link to a discovered item is automatically linked to the corresponding catalog item.
ServiceNow integration | When importing IT component fact sheets via the ServiceNow integration, if the SAM module is enabled, you can use the aggregation and linkage feature to link the imported fact sheets to the reference catalog automatically. For more details, see [Aggregation and Linkage of Software Records](https://help.sap.com/docs/leanix/ea/aggregation-and-linkage-of-software-records?locale=en-US&state=PRODUCTION&version=CLOUD "The aggregation and linkage feature allows you to import multiple software records from ServiceNow in an aggregated way while automatically linking consolidated fact sheets to the reference catalog.").
Self-built software discovery | IT components created from a self-built software discovery feature are automatically linked to the reference catalog.
SaaS discovery | IT components linked to the discovered SaaS are automatically linked to the reference catalog.


