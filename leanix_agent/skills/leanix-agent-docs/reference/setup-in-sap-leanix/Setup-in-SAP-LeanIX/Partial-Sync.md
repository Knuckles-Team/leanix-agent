##  Partial Sync
Partial syncs are event-driven that get triggered from both sides (SAP LeanIX and ServiceNow). In each case, it gets triggered any time a Fact Sheet or a record is created, updated, or deleted in the systems.
In the default model (flag 'short event buffering' is not set), the partial sync is triggered as soon as the batch is full (5000 changes have been logged) or the batch wait time has been exceeded (15 minutes after the first change was logged).
For ServiceNow, the SAP LeanIX application installs a couple of Business Rules to track these events and trigger a sync as seen here -
![3496](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274a67af7a441014a6d3b7be42ad9d3b_LowRes.png)
Business Rules installed by the SAP LeanIX app that looks for events to trigger a Partial Sync
Partial Sync Supported Tables | Business Rule Name
---|---
cmdb_ci which by inheritance includes any table in sync such as -cmdb_ci_business_app,cmdb_ci_business_capability, cmdb_ci_hardware or any other custom table. | CMDB CI
CI Relationship - cmdb_rel_ci | CI Relationship
SAM/SAM Pro - cmdb_sam_sw_install Legacy - cmdb_software_instance | SAM Software Install & Software Instance
Product Model - (cmdb_model) which by inheritance includes -cmdb_hardware_product_modelcmdb_software_product_model | Product Model


