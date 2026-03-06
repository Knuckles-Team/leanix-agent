##  Fields on Relation
To update fields on a relation, you must include the _field on relation display name_ column along with the _fields on relation_ columns you want to update. This ensures the target relation is correctly identified when there are multiple relations.
![Field on Relation Display Name Column](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loioec1efc038ac34c0a8f5394f25f314c6f_LowRes.png)
Field on Relation Display Name Column
The overwrite principle does not apply to the field on relation display name columns, meaning existing relations not mentioned in these columns will not be deleted.
In the example above, even though AC Management has relations to both Corporate Services and Finance business capabilities, you can mention only one business capability in each row without removing the other existing relations from the AC Management fact sheet.
**Caution**
The general overwrite principle still applies to values in all other columns. See [Overwrite Principle](https://help.sap.com/docs/leanix/ea/importing-fact-sheet-data-through-excel-file?locale=en-US&state=PRODUCTION&version=CLOUD#loio275a86917a441014872eecad909f5e9e__overwrite_principle).
You can also update the field on relation for multiple relations by including several target fact sheets in one cell of the <field on relation display name> column. Target fact sheet names should be separated by semicolons.
![Including Several Target Fact Sheets in One Cell](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274efe2b7a441014b17da5dde8861c68_LowRes.png)
Including Several Target Fact Sheets in One Cell
**Tip**
Adding or Removing Relations: Since the overwrite principle does not apply to the _field on relation display name_ columns, deleting a row does not delete a relationship. To remove or update relations, include the _Relations_ column instead. This column lists all related fact sheets in a single cell, separated by semicolons. Any additions or deletions in this cell will be reflected in the inventory when you upload the file. ![Relations Column](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loioab567219459c49e78c44134477e80f36_LowRes.png)
