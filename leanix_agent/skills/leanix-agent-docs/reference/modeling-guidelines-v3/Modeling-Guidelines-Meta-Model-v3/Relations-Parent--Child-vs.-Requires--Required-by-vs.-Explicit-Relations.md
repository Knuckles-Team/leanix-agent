##  Relations: Parent / Child vs. Requires / Required by vs. Explicit Relations
In LeanIX you will find 3 different types of relations between Fact Sheets:
Parent / Child relations allow creating distinct relations between Fact Sheets ("tree structure") within one Fact Sheet type (e.g. User Group). A child can only have one parent Fact Sheet, whereas a parent can have multiple children Fact Sheets. The result is a tree with different levels (top parent = level 1, children of top parent = level 2, children of level 2 parents = level 3, ...). Some examples of modeling in LeanIX:
  * User Groups to build a clear regional structure: Europe / Western Europe / Netherlands (Europe = Level 1, Western Europe = Level 2, Netherlands = Level 3).
  * Tech Category to build a clear Tech Category structure: Database / Relational Database (Database = Level 1, Relational Database = Level 2).


**Note**
Use hierarchies with care. More details always require more maintenance. Start with low granularity and refine only where it makes sense.
Explicit relations are defined between Fact Sheet types based on the LeanIX best practice data model. If available for your use case, we highly recommend using this type of relation. In some cases, these relations include certain attributes to specify the relation (e.g. "total annual costs" on the relation Application - IT Component or "usage" (CRUD) on the relation Application - Data Object).
Requires / Required by relations can be used to create further logical dependencies within one Fact Sheet type or between Fact Sheet types
  * Within the same fact sheet type: For example, a server requires an OS (operating system). These are both IT Components but only the server is directly linked to the Application. Using logical n:m dependencies, however, the "Technology Risk" view allows you to extract the information that the OS is also linked, albeit indirectly through the server. However, you cannot see the indirect connection in the technology risk view of the application matrix report.
  * Between Fact Sheet types: For documentation purposes, it might be helpful to show the dependencies between Fact Sheets of different Fact Sheet types (e.g. Data Object to Process). This relation cannot be visualized in any of the standard reports and is only available on the Fact Sheets and in the table view.


**Note**
Requires / Required by is a powerful concept which should be used carefully. There are use cases (e.g. Technology Risk) where using it will improve the data quality and insights that can be drawn out of LeanIX. In other instances, however, using this relation might create more harm as it overloads the data model. Explicit relations should always be considered before opting for Requires / Required by.
