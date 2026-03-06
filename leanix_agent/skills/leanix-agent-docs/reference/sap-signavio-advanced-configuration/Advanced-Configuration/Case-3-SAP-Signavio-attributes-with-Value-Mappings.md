##  Case 3: SAP Signavio attributes with Value Mappings
In this case the SAP Signavio attribute language in mapped into a custom Fact Sheet field language. Additionally, the value is mapped from their common name into the international two-letter code:
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2751d9e37a44101493a18fb8f986bae7_LowRes.png)
The JSON data structure shows the list of value mappings as maps inside the valueMappings keyword.

```
{
 "inboundMappings": [
  {
   "leanixType": "factSheetField",
   "fields": [
    {
     "leanixFieldName": "language",
     "inboundPropertyPath": "${editordata.model.properties.language}",
     "valueMappings": [
      {
       "outputExpression": "EN",
       "regexMatch": "English"
      },
      {
       "outputExpression": "DE",
       "regexMatch": "German"
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
The regexMatch keyword allows to define a Regular Expression. In this example it is a fixed string and the value retrieved from the inboundPropertyPath editordata.model.properties.language will be compared to this string. The first matching mapping will be used and the outputexpression will be written into the field specified in leanixFieldName.
It is easily possible to define a default avlue that is used if none of the defined (regEx) options match.
This functionality is only available in the JSON (advanced) configuration. In the below example all other languages or empty input will result in "Other"
Example for default values to be mapped

```
{
 "inboundMappings": [
  {
   "leanixType": "factSheetField",
   "fields": [
    {
     "leanixFieldName": "language",
     "inboundPropertyPath": "${editordata.model.properties.language}",
     "valueMappings": [
      {
       "outputExpression": "EN",
       "regexMatch": "English"
      },
      {
       "outputExpression": "DE",
       "regexMatch": "German"
      }
     ],
     "defaultValue": "Other"
    }
   ]
  }
 ]
}

```



