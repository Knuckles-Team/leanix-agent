##  CMDB_REL_CI
You can add an optional query to relation mappings in foreignRelationMapping to enhance integration performance. Here's an example of a query that reads only from relations where the parent class is a business capability and the child class is a business application.
JSON Example:

```
"foreignRelationMapping": {
   "type": "CMDB_REL_CI",
   "relationName": "Provided By::Provides",
   "query": "parent.sys_class_name=cmdb_ci_business_capability^child.sys_class_name=cmdb_ci_business_app^typeISNOTEMPTY"
 }

```



