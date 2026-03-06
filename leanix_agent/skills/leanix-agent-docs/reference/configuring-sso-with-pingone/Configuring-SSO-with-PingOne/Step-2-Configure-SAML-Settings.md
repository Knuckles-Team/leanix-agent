##  Step 2: Configure SAML Settings
Follow these steps:
  1. In the SAML Configuration section, under Provide Application Metadata, select Import Metadata and upload the metadata file. Alternatively, select Manually Enter and specify the following:
     * Entity ID:: https://{REGION}-signin.leanix.net/realms/service-provider/broker/{UUID}
     * ACS URL: https://{REGION}-signin.leanix.net/realms/service-provider/broker/{UUID}/endpoint
  2. Save the changes.
