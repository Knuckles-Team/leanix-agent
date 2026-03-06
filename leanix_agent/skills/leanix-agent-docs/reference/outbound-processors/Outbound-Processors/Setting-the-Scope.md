##  Setting the Scope
The outbound configuration needs to contain a scope. The scope defines the set of Fact Sheets that will be looked at when iterating over the configured outbound processors and creating content in the resulting LDIF. However, while the scope section needs to exist, it can be left completely empty as the example above shows, this means that it will look at all Fact Sheets.
The scope defined in the below example will iterate over all Fact Sheets. The UI provides a visual interface (accessible via the Set Scope button) which allows for the selection of the Fact Sheet data required and sets this data as in "scope" into the configuration. The default scope used for all processors will be defined in the global section. Each processor may contain a scope section to overwrite the global scope settings.
Scope configuration:

```
{
 "scope": {},
 "processors": [
  {
   "processorType": "outboundFactSheet",
   "processorName": "Export to LDIF",
   "processorDescription": "This is an example how to use the processor",
   "scope": {
    "ids": [],
    "facetFilters": [
     {
      "keys": [
       "Application"
      ],
      "facetKey": "FactSheetTypes",
      "operator": "OR"
     }
    ]
   }
  }
 ]
}
```



