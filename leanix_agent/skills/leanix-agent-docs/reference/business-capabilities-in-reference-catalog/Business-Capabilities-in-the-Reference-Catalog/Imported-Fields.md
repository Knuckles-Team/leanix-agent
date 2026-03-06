##  Imported Fields
The table below lists the fields set on business capability fact sheets during import from the reference catalog:
Fields | Synced with the Catalog | Notes
---|---|---
  * Name
  * Description

|  No These fields are not synced with the catalog when the catalog data changes or when a fact sheet is linked to a different catalog item. | If fact sheets with the same name already exist in the inventory, their names and descriptions are overwritten during import.
  * Relevance for Industries: Provides information about the industries where the business capabilities apply.
  * Enterprise Domain: Classifies business capabilities into four enterprise domains: Corporate, Customer, Products and Services, and Supply.
  * SAP Reference ID: Serves as an identifier for the business capability within the reference architecture used across SAP products.

|  Yes These fields stay in sync with the catalog when the catalog data changes or when a fact sheet is linked to a different catalog item. To sync fields with the reference catalog, provision the workspace on the Business Capability tab of the reference catalog page in the admin area. | These fields are editable, but it's not recommended to change them as it may cause inconsistencies when updating data from the catalog. If needed, admins can move these fields from the Name & Description subsection to another subsection or hide them. For guidance on managing fields, see [Fact Sheet Fields](https://help.sap.com/docs/leanix/ea/fact-sheet-fields?locale=en-US&state=PRODUCTION&version=CLOUD "Fact sheet fields are designed for storing information on specific data points. You can configure existing fields and create custom ones.").


