##  Load large LDIFs
Depending on the source of the incoming data, LDIF files can be very large. The Integration API may not accept LDIF larger than 50 MB. If your file is bigger, it needs to be provided as a URL reference on an Azure Blob storage.
The configuration can be added to the Processor configuration part:
Read LDIF from Azure Blob Storage:

```
{
  "dataProvider": {
    "url": "${header.customFields.url}"
  },
  "processors": [
  ]
}
```



The value can be configured fix or as in the example passed in as part of the custom fields information in the LDIF. Please ensure to not send the "content" section in case you want to read from Azure. If content is part of the API call, this content will be used instead of the content in the Azure storage.
The URL needs to contain the path to the blob storage entry plus the Azure SAS token. For details, refer to the [Azure documentation![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Flearn.microsoft.com%2Fbs-latn-ba%2Fazure%2Fstorage%2Fblobs%2Fstorage-blob-user-delegation-sas-create-cli "https://learn.microsoft.com/bs-latn-ba/azure/storage/blobs/storage-blob-user-delegation-sas-create-cli").
**Note**
No support for IP whitelisting.
Please note that we process from our Azure infrastructure where IP addresses can dynamically change. Reading data from a URL only works if no IP whitelisting is set. Instead SaS tokens with limited ttl can be used.
