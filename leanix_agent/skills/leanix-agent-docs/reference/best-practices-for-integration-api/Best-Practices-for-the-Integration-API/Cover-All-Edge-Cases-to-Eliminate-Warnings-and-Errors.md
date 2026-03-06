##  Cover All Edge Cases to Eliminate Warnings and Errors
Whenever value mapping is defined in the processor, it is highly suggested to add a "catch-all" option at the end of the value mapping list. By doing so, warnings that arise from the processor on not finding any matching value from other value mapping list can be removed.

```
{
 "leanixType": "tag",
 "fields": [
  {
   "leanixFieldName": "group",
   "inboundPropertyPath": "Process Frequency",
   "valueMappings": []
  },
  {
   "leanixFieldName": "name",
   "inboundPropertyPath": "${editordata.model.properties[\"meta-processfrequency\"]}",
   "valueMappings": [
    {
     "outputExpression": "High",
     "regexMatch": "ci1560953961659160925663"
    },
    {
     "outputExpression": "Medium",
     "regexMatch": "ci1560953961659758129772"
    },
    {
     "outputExpression": "Low",
     "regexMatch": "ci1560953961659682886651"
    },
    {
     "outputExpression": "None",
     "regexMatch": "ci1560953961659123251220"
    },
    {
     "outputExpression": "Other value",
     "regexMatch": ".*"
    }
   ]
  }
 ]
}
```



In the example above, by using the last value mapping of "Other Value", the Integration will not output a warning in the sync log when it does not find any of the matching values defined.
