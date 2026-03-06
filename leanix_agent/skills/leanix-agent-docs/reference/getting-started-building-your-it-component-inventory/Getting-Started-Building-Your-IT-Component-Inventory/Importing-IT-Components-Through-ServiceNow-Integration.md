##  Importing IT Components Through ServiceNow Integration
The SAP LeanIX and ServiceNow integration connects enterprise architecture data with IT operations data in ServiceNow.
In the integration configuration, on a high level, you do the following:
  1. Map the IT component fact sheet to the ServiceNow tables cmdb_software_product_model and cmdb_hardware_product_model.
  2. Set up field mappings to match ServiceNow fields with fact sheet attributes.
  3. Set the sync direction from ServiceNow to SAP LeanIX.
  4. Map the relations between records to relations between fact sheets to link the imported IT components to the relevant application fact sheets.


If the SAM module is enabled in ServiceNow, you can map the IT component fact sheet to the cmdb_sam_sw_discovery_model and cmdb_ci_spkg tables. For more details, see [Aggregation and Linkage of Software Records](https://help.sap.com/docs/leanix/ea/aggregation-and-linkage-of-software-records?locale=en-US&state=PRODUCTION&version=CLOUD "The aggregation and linkage feature allows you to import multiple software records from ServiceNow in an aggregated way while automatically linking consolidated fact sheets to the reference catalog."). This ensures that the imported fact sheets are also automatically linked to the reference catalog item, ensuring they stay updated as the catalog data evolves. It also links the IT component fact sheet to the associated provider and tech category fact sheets if you have configured the reference catalog that way. To learn more, see [IT Components in the Reference Catalog](https://help.sap.com/docs/leanix/ea/it-components-in-reference-catalog?locale=en-US&state=PRODUCTION&version=CLOUD "By using reference data for IT component fact sheets, you can increase standardization and data quality, set relations to other fact sheets for best-practice modeling, as well as manage technology obsolescence risks by using vendor lifecycle information.").
For a detailed guide, see [ServiceNow Integration](https://help.sap.com/docs/leanix/ea/servicenow-integration?locale=en-US&state=PRODUCTION&version=CLOUD "Fundamentals of the SAP LeanIX integration with ServiceNow \(CMDB\).").
![Mapping Fact Sheets and Relations in Integration Settings](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio4068cebb75864e41b382f0ecb8a9585b_LowRes.png)
Mapping Fact Sheets and Relations in Integration Settings
