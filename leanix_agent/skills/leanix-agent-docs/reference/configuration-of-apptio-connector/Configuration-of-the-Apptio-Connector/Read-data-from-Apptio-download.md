##  Read data from Apptio (download)
If data is to be read from Apptio, the "apptioReadConfigs" section must contain data.
### apptioReadConfigs
This array contains one or more Apptio read configurations for downloading data. Each read configuration has the following JSON structure:

```
{
 "type": "url",
 "url": "https://bizdev-r12.apptio.com/biit/api/v2.tsv?date=Jul:FY2020&dataPath=-@Cleanixpartner.com%3ACost+Transparency2/Data/.DateGoesHere/Data+Center+Detail/ExecutionSteps/Output/!SORT/!LIMIT%5B0%2C2147483647%5D/!LIMIT_COLUMNS%5B%5D&environment=stg",
 "tableName": "Data Center Detail"
}

```



Parameters:
  * type: must be url
  * url: Apptio target table url from where the data will be read. This API url can be generated in Apptio TBM Studio for the desired table. The format used is the tsv format or the legacy tsv format from the tables in TBM Studio
  * tableName: name of the table to be used as "type" for the resulting LDIF content items


**Note**
Apptio API Integration and format
This integration is designed to pull and read from the tables within TBM studio only.
The format used is the tsv format or the legacy tsv format from the tables in TBM Studio.
**Note**
Apptio period to download/upload
In the URL for the table where to download data from, a period must be specified indicating the month and year for that target table (it can be part of the URL or the "date" query parameter depending on the URL format).
A period uses the MMM:'FY'yyyy format (Three characters month, colon, FY literal string, 4-digit year). Also, the keyword "CURRENT" can be used to download from the current month period.
### dataConsumer
If a "dataConsumer" (optional) section is defined (see example configuration), the "type" must always be set to "leanixStorage". For this configuration the resulting LDIF will be stored into the database and is accessible via API call (/runs//results). If no "dataConsumer" is specified, the resulting LDIF is stored on Azure storage. The url to this LDIF is provided via API (/runs/ /resultsUrl).
