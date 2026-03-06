##  Combining Conditions
Conditions can be combined using OR & AND logics when you want to activate the same attribute with multiple conditions.
  * When activating values come from a single activator then conditions are combined by an OR logic
  * When activating values come from different activators then conditions are combined by an AND logic.


For example:
  * In application fact sheets, you may want to make the Functional Fit Description field visible only when the functional fit is unreasonable or insufficient. Because only in those cases users have the need to provide usage justification in the description field.
In this case you define 2 conditions to activate the Functional Fit Description field using Unreasonable and Insufficient as activating values, since both of them belong to the activator field Functional Fit, OR logic is used. As a result, the Functional Fit Description field is activated if either Unreasonable or Insufficient is selected in the fact sheet.
![Combining Conditions for Conditional Attributes with OR Logic](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2757411f7a441014b072de8e403e9ed0_LowRes.png)
Combining Conditions for Conditional Attributes with OR Logic
  * In an application fact sheet, say if you want to activate the field Provided Interfaces only when the TIME classification is Eliminate and the 6R classification is Retire. In this case, since activating values Eliminate and Retire belong to different activator fields, AND logic is used.
![Combining Conditions for Conditional Attribute with AND Logic](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio27418ca67a4410149788c23066fdf3fd_LowRes.png)
Combining Conditions for Conditional Attribute with AND Logic
**Note**
It is also possible to combine both OR and AND logics to activate a conditional attribute.
