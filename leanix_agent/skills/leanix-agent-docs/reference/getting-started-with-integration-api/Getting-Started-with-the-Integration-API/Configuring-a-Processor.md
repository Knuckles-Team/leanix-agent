##  Configuring a Processor
Follow these steps:
  1. In the administration area, go to the Integration API section.
  2. Click New Processor Configuration.
  3. Specify the processor details, then click Save. Once you save the processor, you can add new versions and update the integrated tool. You can't change any other details.
![Creating a Processor](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2756be227a441014b511ee2e57d981a3_LowRes.png)
Creating a Processor
  4. On the left side of the configuration page, define the processor configuration. You can add multiple processors.
  5. In the Input section, enter the following depending on the processor direction:
     * Inbound: Enter the data to be imported in LDIF format. For more details, see [LeanIX Data Interchange Format (LDIF)](https://help.sap.com/docs/leanix/ea/integration-api?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a99087a441014a04fa6cda4e0ec2b__leanix_data_interchange_format_ldif).
     * Outbound: To define the scope of data to export in LDIF format, in the upper-right corner, click the three-dot icon > Define Scope, then select fact sheets using inventory filters. The scope in the processor configuration on the left side is populated accordingly.
  6. Click Save.


After saving a processor, you can test and run it, as described in the following sections.
![Processor Configuration Page](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27540a997a4410149bb78ff47132e7ee_LowRes.png)
Processor Configuration Page
**Note**
Processor configuration and data are strictly separated in the Integration API to ensure synchronization runs are reliable, repeatable, and auditable. Whenever you save the configuration of processors, only the processors are stored. The system does not store any LDIF data.
