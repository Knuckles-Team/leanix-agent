##  Case 5: Use Complex Expressions in Value Mappings
Inside valueMappings keyword, each element of the list allows the mapping of the value to a final result given by the keyword outputExpression. In previous examples, we set fixed text values in this keyword, however it is possible to use more complex EL expressions that combine other objects of data.
In the following JSON config, we are combining part (the first 5 characters) of the SAP Signavio name concatenated with the attribute language to obtain the final value for the field processnumber.

```
{
 "inboundMappings": [
  {
   "leanixType": "factSheetField",
   "fields": [
    {
     "leanixFieldName": "processnumber",
     "inboundPropertyPath": "${model.name}",
     "valueMappings": [
      {
       "outputExpression": "${input.substring(0,5)} - ${editordata.model.properties.language}",
       "regexMatch": "^[0-9].*"
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
In outputExpression, the symbol input represents the result obtained after the expression in inboundPropertyPath (the model name: ${model.name}) is resolved. In general, the input keyword is only available in outputExpression and offers a flexible way to modify the inboundPropertyPath value. We are also verifying that only models that have a name that starts with a number are used to obtain the processnumber field, this is guaranteed by the regexMatch "^[0-9].*" .
After the synchronization, an SAP Signavio Diagram named 1.1.3 Summary of objections is synchronized to a Fact Sheet with the value 1.1.3 - English in the field processnumber.
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2748f8567a44101483e5dec413621b4b_LowRes.png)
**Note**
Unknown property handling
It might be that some advanced expressions may contain references to properties on SAP Signavio Processes that exist for some processes but do not exist on others. To avoid error messages, a flag "ignoreUnknownProperty" can be set to true. By using this, the admin can keep the logs clean in cases where such warnings are expected and can be ignored.
Sample usage to ignore missing property warnings

```
{
 "inboundMappings": [
  {
   "leanixType": "factSheetField",
   "fields": [
    {
     "leanixFieldName": "processnumber",
     "inboundPropertyPath": "${model.name}",
     "valueMappings": [
      {
       "outputExpression": "${input.substring(0,5)} - ${editordata.model.properties.language}",
       "regexMatch": "^[0-9].*"
      }
     ],
     "ignoreUnknownProperty": true
    }
   ]
  }
 ]
}

```



