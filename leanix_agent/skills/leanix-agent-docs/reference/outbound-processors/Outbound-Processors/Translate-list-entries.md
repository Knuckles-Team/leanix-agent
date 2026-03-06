##  Translate list entries
A first use case covers the need to translate all entries of a list of values read from a Fact Sheet. Combining the option to iterate over a list of values in the output section and being able to configure this multiple times to collect results to output and on top of this filter by specific entries of the list.
We iterate over the list of entries multiple times. One time for each known option we want to translate. And we skip all other entries of the list. As a result, we collected a list of translated values.
The solution can be used for inbound and outbound processors both.
Example of translating all entries of a list to be exported:

```
{
 "key": {
  "expr": "myGermanValues"
 },
 "mode": "list",
 "values": [
  {
   "forEach": {
    "elementOf": "${myList}",
    "filter": "${integration.output.valueOfForEach==’english value 1’}"
   },
   "expr": "Deutscher Wert 1"
  },
  {
   "forEach": {
    "elementOf": "${myList}",
    "filter": "${integration.output.valueOfForEach==’english value 2’}"
   },
   "expr": "Deutscher Wert 2"
  }
 ]
}
```



