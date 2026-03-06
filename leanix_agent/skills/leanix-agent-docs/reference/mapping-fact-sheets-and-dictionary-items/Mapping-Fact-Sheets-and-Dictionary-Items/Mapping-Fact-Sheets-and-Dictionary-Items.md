##  Mapping Fact Sheets and Dictionary Items
Mapping the fact sheets and dictionary items primarily involves deciding the source for each mapping, mapping fact sheet types to corresponding dictionary categories, and selecting a sync mode to manage data updates and deletions. This is done in the Basic Configuration tab of the integration configuration page.
![Mapping Fact Sheets and Dictionary Items](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27474ee27a441014b440dbbe6a613399_LowRes.png)
Mapping Fact Sheets and Dictionary Items
##  Mapping Fact Sheets and Dictionary Items
To map the fact sheets to dictionary items between SAP LeanIX and SAP Signavio, do the following:
  1. From the Fact Sheet Type drop-down list, select the specific fact sheet type you want to read from or write to. The list includes fact sheet types that have an external ID field provisioned for SAP Signavio. By default, these fact sheet types include application, business capability, organization, data object, and interface, along with their subtypes. If you need the external ID field provisioned for additional fact sheet types, you can submit a configuration request ticket to [SAP LeanIX Support![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fwww.leanix.net%2Fsupport "https://www.leanix.net/support") or [SAP for Me![Information published on SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/sap_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fme.sap.com%2F "https://me.sap.com/").
  2. From the Dictionary Category Name drop-down list, select the corresponding SAP Signavio dictionary category. Depending on the system you have designated as the source, the fact sheets will either be written as dictionary items into this category or read from existing dictionary items.


**Note**
We recommend using SAP LeanIX as the source of truth for applications, business capabilities, organizations, and data objects.
**Note**
In SAP Signavio, there is no default dictionary category for business capabilities. To import dictionary items from SAP LeanIX you first need to create a relevant custom category if a default dictionary category doesn't exist.
To link dictionary items imported from SAP LeanIX to processes and use them in process definition, you also have to create custom attributes with the data type of corresponding dictionary categories, either at the process diagram level or the object level. We recommend creating the following custom attributes at a minimum:
  * Linked Applications (at the task level)
  * Linked Business Capabilities (at the diagram level)
  * Linked Organizations (at the diagram level)


For a step-by-step guide on creating such custom attributes, see [Creating Custom Attributes in Dictionary Categories](https://help.sap.com/docs/leanix/ea/best-practices-and-tutorials?locale=en-US&state=PRODUCTION&version=CLOUD#loio2758ecda7a4410148fc2e2c4b70df0d1__creating_custom_attributes_in_dictionary_categories).
