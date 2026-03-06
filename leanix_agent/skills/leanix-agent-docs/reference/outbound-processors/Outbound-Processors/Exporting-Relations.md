##  Exporting Relations
In case relations need to be available to write information about them to the LDIF, a section "relations" needs to exist. The section contains three parts: "filter", where users will configure the names of the relations they are interested in to export, the fields and the targetFields key to define what fields on the relation and what fields from the target Fact Sheet will be available in the output section. All fields on relations can be configured in the "targetFields" key which is a value within the "relations" key. A processor iterating over the target Fact Sheet types needs to be configured to read all fields.
Example configuration of relations:

```
{
 "relations": {
  "filter": [
   "relToParent",
   "relApplicationToITComponent"
  ],
  "fields": [
   "description"
  ],
  "targetFields": [
   "displayName",
   "externalId"
  ],
  "constrainingRelations": false
 }
}
```



In case relations are found, they are all available as an array in "lx.relations". An example on how to access this information fill follow below. The example above only exports the creation date of all Fact Sheets in scope.
Making information about tags and subscriptions available to be used in the output section works following the same pattern.
