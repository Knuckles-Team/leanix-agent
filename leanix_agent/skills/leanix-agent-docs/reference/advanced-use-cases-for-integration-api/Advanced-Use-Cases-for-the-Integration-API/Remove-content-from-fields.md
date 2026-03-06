##  Remove content from fields
The integration API can be used to remove content. In case Values array contains "null" values after evaluating all configured elements in the Values Array, the Integration API will try to reset the configured field to an initial "not filled" state. This is specifically helpful for Single or multi select fields. String fields can simply be cleaned by passing an empty String. Numbers may rather be set to 0.
To avoid a warning, that no value could be found, ensure the "optional" field is used.
**Note**
variableProcessor
Is used to only write values to internal variables. This will be used for aggregation use cases where the LDIF content needs to be used to only collect values without directly writing anything to SAP LeanIX.
