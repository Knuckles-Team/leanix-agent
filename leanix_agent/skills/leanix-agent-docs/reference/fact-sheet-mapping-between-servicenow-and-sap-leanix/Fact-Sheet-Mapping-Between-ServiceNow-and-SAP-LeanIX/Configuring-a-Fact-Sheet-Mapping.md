##  Configuring a Fact Sheet Mapping
To configure mappings between fact sheet fields and ServiceNow tables, start by creating fact sheet mappings. After that, proceed to configure field mappings.
**Note**
When you create a new ServiceNow configuration, it already contains default mappings. You can adjust the default configuration to suit your needs.
To view detailed information on mappings, view the mapping matrix: [Download a copy of the Excel file![Information published on SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/sap_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fd.dam.sap.com%2Fa%2FR5iKkB9%3Frc%3D10%26doi%3DSAP1226473 "https://d.dam.sap.com/a/R5iKkB9?rc=10&doi=SAP1226473").
Follow these steps:
  1. On the ServiceNow configuration page, navigate to the Mappings tab.
  2. To create a new mapping, under Fact Sheet Mapping, click Add Fact Sheet Mapping. If the mapping you need already exists, select it and adjust the configuration as needed.
![Adding a Fact Sheet Mapping](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27437f657a441014a2d7e62a894fdadf_LowRes.png)
Adding a Fact Sheet Mapping
  3. Configure mapping parameters.
    1. Define the fact sheet type, synchronization direction, ServiceNow table, and synchronization mode.
    2. Configure field mappings. For detailed information, see [Configuring Field Mappings](https://help.sap.com/docs/leanix/ea/fact-sheet-mapping-between-servicenow-and-sap-leanix?locale=en-US&state=PRODUCTION&version=CLOUD#loio275ca5f57a4410149871ec89426715ea__configuring_field_mappings).
    3. Optionally, configure synchronization filters (constraints) to limit the number of synced records. For details, see [Synchronization Filters](https://help.sap.com/docs/leanix/ea/fact-sheet-mapping-between-servicenow-and-sap-leanix?locale=en-US&state=PRODUCTION&version=CLOUD#loio275ca5f57a4410149871ec89426715ea__synchronization_filters).
  4. To save a mapping without activating it, turn off the toggle next to the fact sheet type.
  5. Save your changes.


Once you’ve added fact sheet mappings, you can modify, activate, deactivate, or delete them.
