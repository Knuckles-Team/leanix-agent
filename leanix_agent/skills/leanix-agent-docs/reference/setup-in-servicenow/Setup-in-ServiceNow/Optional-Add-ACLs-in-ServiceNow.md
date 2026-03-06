##  Optional: Add ACLs in ServiceNow
If you want to limit access of your cmdb_ci's ACLs in a way that only your target tables accept <create> and <write> access, you can add JavaScript code to your ACL. Therefore when creating the record ACL you must check the Advanced checkbox and add additional rules as JavaScript.
The JavaScript example below checks, that only modifications to thecmdb_ci_business_app are allowed. If the variable answer is true the ACL will pass, otherwise, the ACL will reject.

```
// Limits access only to table cmdb_ci_business_app
var targetTableName = current.sys_meta.name;
answer = (targetTableName == 'cmdb_ci_business_app');

```



![3496](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2755c2b87a44101482e5d681adceee45_LowRes.png)
Sample JavaScript, which limits the write access to only the 'cmdb_ci_business_app' table.
**Restriction**
Adding a record ACL to a target table like cmdb_ci_business_app, may change the access behavior. When specifying a record ACL to a table, the new ACL may mask ACLs from base tables. Therefore it is possible that a user has write access by an ACL on cmdb_ci but afterwards this will be denied by the ACLs on cmdb_ci_business_app.
