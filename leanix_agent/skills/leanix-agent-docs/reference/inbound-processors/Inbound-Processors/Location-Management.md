##  Location Management
Writing to fields of type "location" will require a single string as input. The string will be sent to the location service (open street map). In case a single result was returned, the location will be written to the field with all meta data returned by "open street map". Providing latitudes and longitude works by simply passing the coordinates in that order, separated by comma: "50.11, 8.682".
In case of no or multiple locations returned, the field will not be populated and an error shown in the log for this field. Other updates by the data processor may still be valid and pass.
**Note**
When writing locations, the used open street map service may return multiple results. Default behaviour is to not set any location. In case the value provided to the Location starts with a # character, the first result from open street map will be used (same logic as we see when providing coordinates)
