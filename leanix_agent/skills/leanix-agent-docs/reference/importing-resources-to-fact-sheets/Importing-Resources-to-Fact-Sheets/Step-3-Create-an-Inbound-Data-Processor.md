##  Step 3: Create an Inbound Data Processor
Now that you have data to be imported in the required LDIF format, you can create a data processor for the Integration API and complete a run to import links to Applications in batch.
The inboundDocument processor is used to create, update, and delete resources linked to fact sheets. To learn more about the processor, see [Inbound Document](https://help.sap.com/docs/leanix/ea/inbound-processors?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a8a067a4410148b1fcfe89dcdedca__inbound_document).
To create a processor, follow these steps:
  1. In the administration area of SAP LeanIX, select Integration API.
  2. Click New Processor Configuration.
  3. Enter parameters for the processor:
     * Connector Type: Enter a name for the connector type.
     * Connector Id: Enter an ID for the connector.
     * Connector Version: Enter 1.0.0.
     * Processing Direction: Select inbound.
     * Processing Mode: Select partial.
     * Integrated Tool: Select None.
  4. Click Create.


A processor is created.
