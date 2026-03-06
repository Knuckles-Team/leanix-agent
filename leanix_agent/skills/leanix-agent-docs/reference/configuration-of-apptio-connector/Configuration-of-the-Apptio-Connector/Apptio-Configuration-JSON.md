##  Apptio Configuration JSON
Apptio configuration JSON contains the credentials needed to connect to the user's Apptio environment and configurations per table needed for read (download) and write (upload) to these tables.
Apptio example JSON configuration:

```
{
 "configId": "lxApptio",
 "data": {
  "apptioConnectionConfig": {
   "loginUrl": "https://frontdoor.apptio.com/service/apikeylogin",
   "keyAccess": "{{pub}}",
   "keySecret": "{{secret}}",
   "domain": "leanixpartner.com",
   "environmentName": "sandbox",
   "ulsUrl": "https://datalink.apptio.com/uls/api/v1"
  },
  "apptioWriteConfigs": [
   {
    "type": "detailed",
    "host": "bizdev-r12.apptio.com",
    "project": "Cost Transparency",
    "tableName": "Mainframe Data",
    "period": "Jun:FY2018",
    "overwrite": true
   }
  ],
  "dataProvider": {
   "type": "url",
   "url": "https://input_file_url"
  },
  "apptioReadConfigs": [
   {
    "type": "url",
    "url": "https://bizdev-r12.apptio.com/biit/api/v2.tsv?date=Jul:FY2020&dataPath=-@Cleanixpartner.com%3ACost+Transparency2/Data/.DateGoesHere/Data+Center+Detail/ExecutionSteps/Output/!SORT/!LIMIT%5B0%2C2147483647%5D/!LIMIT_COLUMNS%5B%5D&environment=stg",
    "tableName": "Data Center Detail"
   }
  ],
  "dataConsumer": {
   "type": "leanixStorage"
  }
 },
 "active": true
}

```



