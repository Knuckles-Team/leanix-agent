##  Case 9: Mapping SAP Signavio Glossary Items to Fact Sheets
In this case, we will create Fact Sheets based on SAP Signavio Glossary Items making use of advanced inbound mapping capabilities. The Glossary Item in SAP Signavio Dictionary is shown bellow.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274de79d7a441014ac7784d593bb196c_LowRes.png)
In the bellow data configuration we can see the glossaryCategorySyncDescriptors property of the global configuration that contains one element defining the options for the synchronization. We suppressed some parts of the config for clarity and shows only the inboundMappings section.

```
{
 "glossaryCategorySyncDescriptors": [
  {
   "inboundMappings": [
    {
     "leanixType": "factSheetField",
     "fields": [
      {
       "leanixFieldName": "meta_cause",
       "inboundPropertyPath": "${glossary.metaDataValues['meta-cause']}",
       "valueMappings": [
        {
         "outputExpression": "${input.replaceAll('^[0-9.]+ (.*)','$1')}",
         "regexMatch": "^[0-9.]+ .*"
        }
       ]
      },
      {
       "leanixFieldName": "meta_consequence",
       "inboundPropertyPath": "${glossary.metaDataValues['meta-consequence']}",
       "valueMappings": [
        {
         "outputExpression": "${input.toUpperCase()}",
         "regexMatch": "^possible.*"
        }
       ]
      }
     ]
    }
   ]
  }
 ]
}

```



In the previous data configuration, there are two elements that define mapping options for two Fact Sheets fields:
  * In leanixFieldName = meta_cause Field: It takes the value from SAP Signavio attribute meta-cause obtained using the mechanism explained in Signavio Endpoints section. Using valueMappings we are only considering those values that have numbers in its content. The last expression inside outputExpression defines how to modify the data before applying to the Fact Sheet, for our example we are removing the numeric part from 0.1.2 Admission of candidates.
  * In leanixFieldName = meta_consequence Field: It takes the value from SAP Signavio attribute meta-consequence. In valueMappings we are only considering those values that starts with the word possible. The last expression inside outputExpression defines how to modify the data, which for our example is converting the value to uppercase.


The new Fact Sheet created using the previous configuration is shown bellow. The values for the fields meta_cause and meta_consequence are Admission of candidates and POSSIBLE OUTRAGE respectively.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274f61037a441014a74b924c6029291d_LowRes.png)
