##  Case 2: SAP Signavio Attributes to Fields
The configuration that synchronizes a SAP Signavio attribute into a Fact Sheet Field is shown:
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2751c73f7a441014b430e81791832931_LowRes.png)
The corresponding JSON structure is:
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
     "valueMappings": []
    }
   ]
  }
 ]
}

```



New Fact Sheets created will have the field language with the same value taken from the SAP Signavio endopoint editordata, the value for the path given in inboundPropertyPath is explained in [Endpoints](https://help.sap.com/docs/leanix/ea/sap-signavio-advanced-configuration?locale=en-US&state=PRODUCTION&version=CLOUD#loio275c5e6b7a441014bb7791de014f5feb__endpoints). The expression ${...} is part of EL (Expression Language) used by the integration to offer a flexible way to work with data from SAP Signavio Endpoints.
**Note**
For the properties with names in the format, meta-xxx use the inboundPropertyPath as below.
"inboundPropertyPath": "${editordata.model.properties use the inb}"
