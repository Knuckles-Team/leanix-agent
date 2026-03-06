##  Advanced Inbound Mappings (Processes and Glossary Items)
The inboundMappings can be used in both Processes and Glossary Items configurations, it consists of a list of JSON maps as shown.

```
{
 "inboundMappings": [
  {
   "leanixType": "",
   "fields": [
    {
     "leanixFieldName": "",
     "inboundPropertyPath": "",
     "valueMappings": [
      {
       "outputExpression": "",
       "regexMatch": ""
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
Each element inside this list of Inbound Mappings have the following keywords:
  * leanixType: Specify into which SAP LeanIX data type the data is written. Allowed values are:


Type of Descriptor | Allowed Values
---|---
Processes (processSyncDescriptors) | factSheetField, tag, subscription
Glossary Items ( glossaryCategorySyncDescriptors) | factSheetField, tag, subscription


  * fields: A list that describes the incoming data path, how it is transformed and where it is written to.


Each member in fields list has the following properties:
  * leanixFieldName: the Fact Sheet field where data is written into. Depending of the leanixType value, it should contain optional or required Fact Sheets fields. The table bellow shows the expected definitions for each possible value of leanixType:


For Processes:
leanixType | Allowed values | Description
---|---|---
factSheetField | Data model field name | The name of a field defined for the fact sheet type in your SAP LeanIX Data Model. Supported data types: SINGLE_SELECT, STRING, DOUBLE, INTEGER.
tag | required: name. Optional: group | The tag must exist before the synchronization. If group is not specified, Others is used.
subscription | required: email, type, role. Optional: comment | The role must exist before the synchronization.


For Glossary Items:
leanixType | Allowed values | Description
---|---|---
factSheetField | Data model field name | The name of a field defined for the fact sheet type in your SAP LeanIX Data Model. Supported data types: SINGLE_SELECT, STRING, DOUBLE, INTEGER.


  * inboundPropertyPath: Specify path/expression for SAP Signavio endpoints (See section SAP Signavio Endpoints). The symbols that are available are the same as shown in the table below:
for outputExpression except for ${input}.
  * valueMappings: Optional, it allows to specify mappings of the values that have been obtained based on inboundPropertyPath value.


Each member inside valueMappings have the following properties:
  * regexMatch: A regular expression to which the value of the inboundPropertyPath has to match, the simplest case is an static text, but any Java Regular Expression could be used here. The elements in the list of value Mappings are evaluated until the first matched is found.
  * outputExpression: An expression that resolves the final value for the Fact Sheet field. We can use fixed values, like a text, or the combination of multiple fields. The table bellow shows the symbols that are available inside the expressions.


For processes:
Symbol | Meaning | Example
---|---|---
input | The value resolved by inboundPropertyPath expression | ${input}
model | The data taken from model endpoint | ${model.status.publish}
editordata | The data taken from editordata endpoint | ${editordata.model.properties.language}
glossaryItem | A utility object for Glossary Items referenced in SAP Signavio Attributes | ${glossaryItem.get('12423')}


For Glossary Items:
Symbol | Meaning | Example
---|---|---
input | The value resolved by inboundPropertyPath expression | ${input}
glossary | The data coming taken from glossary endpoint | ${glossary.metaDataValues['meta-cause']}


The example expressions in the previous table follow the syntax defined by Expression Language (or just EL). EL expressions allows advanced operations like splitting, concatenating or selection of substrings for any of the symbols available. A description for EL can be found in [https://jcp.org/en/jsr/detail?id=245![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fjcp.org%2Fen%2Fjsr%2Fdetail%3Fid%3D245 "https://jcp.org/en/jsr/detail?id=245").
