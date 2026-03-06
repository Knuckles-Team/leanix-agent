##  Write data to Apptio (upload)
In case data should be uploaded to Apptio, the "apptioWriteConfigs" needs to be specified.
### apptioWriteConfigs
This array contains one or more Apptio write configurations for uploading data. Each write configuration has the following JSON structure:

```
{
 "type": "detailed",
 "host": "bizdev-r12.apptio.com",
 "project": "Cost Transparency",
 "tableName": "Mainframe Data",
 "period": "Jun:FY2018",
 "overwrite": true
}

```



Parameters:
  * type: must be "detailed"
  * host: the url host section for the Apptio environment being used
  * project: project name containing the target table
  * tableName: name of the target table
  * period: the period where to upload the data for that table. Like downloading data from Apptio, it uses the MMM:'FY'yyyy format (Three characters month, colon, FY literal string, 4-digit year). The keyword "CURRENT" can be used also to upload to the current month period
  * overwrite: true/false. If true, all previous table contents will be deleted and replaced with the new content uploaded. If false, previous contents will be kept and new content will be added to the target table


### dataProvider
If a "dataProvider" (optional) section is defined (see example configuration), for the current version, "type" must be "url". The "url" field next must define an url for an Ldif file to be read and used as input for the upload process.
