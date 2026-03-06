##  Configuring the OData Integration
  1. In SAP LeanIX:
    1. In the Integrations section of the administration area, enable the OData integration.
    2. In the inventory, create and save searches with the required fields within the table view. OData sharing is only available for saved searches created in this view.
    3. In the configuration of saved searches, enable OData sharing and set the permission to Unrestricted or Write Restricted. To learn more, see [Enabling OData Sharing for a Saved Search](https://help.sap.com/docs/leanix/ea/odata-integration?locale=en-US&state=PRODUCTION&version=CLOUD#loio275b87d97a441014bd23aa84c81ee542__enabling_odata_sharing_for_a_saved_search).
  2. In your BI tool:
    1. Access the OData endpoint of your workspace with an API token that you created. To learn how to choose the right endpoint, refer to [OData Endpoints](https://help.sap.com/docs/leanix/ea/odata-integration?locale=en-US&state=PRODUCTION&version=CLOUD#loio275b87d97a441014bd23aa84c81ee542__odata_endpoints).
    2. Import saved searches into your BI tool by connecting to the OData data source. For detailed instructions, refer to the documentation of your BI tool.


**Note**
If you disable the OData integration in the administration area, the imported data remains shared with the BI tool as long as OData sharing is enabled for individual saved searches.
