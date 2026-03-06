##  Dot Walking
It is possible to dot walk certain field mappings within the advanced configuration of the Integration. This is especially useful if it is required to pull information of some record from its corresponding referenced field.
In the following example, we know that Schedule & Track is linked to the Business Unit of Australia. To bring this information into SAP LeanIX as a relationship, we will have to -
  * Map the table which the reference field is from to a SAP LeanIX Fact Sheet type. In this case it would be linking the SAP LeanIX User Group Fact Sheet Type to the business_unit table.
  * Create a relationship descriptor of type REFERENCE_FIELD between the Applications and the User Group Fact Sheet Type using the business_unit reference field as seen below in the screenshot.


![3584](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2753faaf7a4410149e53cc97c6db3f31_LowRes.png)
Business Unit field here is a field of type Reference that is connected to the business_unit table.
While the above method works, it is often times too much work just to bring in data from the field. Especially so if it is not required to have as a Relationship. In such a case, dot-walking functionality can be used to bring the name of the Business Unit into SAP LeanIX as a string field.
  * Step 1
Review the field in ServiceNow by clicking on the (i) icon


![3584](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274b98d07a44101491b7cfb1371f6fd6_LowRes.png)
The (i) icon preview shows us the mini-view of the Australia record within the Business Unit table.
  * Step 2
We notice that the name field is the one that stores the actual value of "Australia" in a string field.
  * Step 3
Logically speaking another way to put this would be business_unit.name. Wherein, the first part before the "." is the name of the field within the main table. Subsequently, the second part after the "." is the name of the field within the referenced table where the value is stored. This is known as dot-walking.
  * Step 4
Within SAP LeanIX, this can be modeled within the advanced tab in JSON as follows -



```
"alias": {
  "fieldType": "FOREIGN_FIELD",
  "foreignFieldName": "business_unit.name",
  "useNormalDirection": true
},

```



![3584](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio275347177a441014aef4eff5ab1152d5_LowRes.png)
Configuration example within advanced tab
In the code example above, we are pulling the name of the attached business unit to the Application into the Alias field of SAP LeanIX which for the purposes below we have renamed to "Business Unit".
![3584](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2755f03e7a44101497418566bd768570_LowRes.png)
Business Unit's name coming through to SAP LeanIX through dot-walking.
