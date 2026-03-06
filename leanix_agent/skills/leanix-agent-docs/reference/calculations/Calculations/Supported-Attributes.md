##  Supported Attributes
**Caution**
To prevent infinite loops in calculations, avoid using these fields in the calculation code: rev, updatedAt, and the target field. These fields don't appear in the code editor to prevent errors.
The following attributes are supported in calculations:
Supported Attributes Attribute | Details
---|---
Fact sheet fields | Double |  To reference fact sheet fields, use the notation data.fieldName. Dynamic property access is not supported. Always use direct properties when referencing fields. Do not use notations like data['field'+'Name'] or const key = ‘fieldName’; data[key], or similar variations. Incorrect notations can prevent calculation triggers from being identified properly. As a result, the calculations might not execute correctly. Calculations that read data from at least one Date field (String type) run daily for all target fact sheets at 12:00 AM (midnight) UTC.
Integer
Multiple Select
Single Select
String
External Id
Base Field, except for the field Level **Restriction** You can use Base fields as input and not as target fields.
Lifecycle |  To reference a lifecycle field, use the notation data.lifecycleFieldName.phaseName. For example: data.lifecycle.active. To prevent errors when the lifecycle field is undefined, exclude those cases (for example, by adding if (data.lifecycle != null){...}). Calculations that read data from at least one lifecycle field run daily for all target fact sheets at 12:00 AM (midnight) UTC.
Relations |  To reference relations, use the notation data.relationName. This returns an array of relations on the fact sheet of the specified relation type. You can perform further operations, such as accessing the number of related fact sheets with data.relationName.length. Use the notation data.relationName and avoid reassigning it to variables. Incorrect notations can prevent calculation triggers from being appropriately identified. This may result in the relation content not being read. Dynamic property access is not supported. Always use direct properties when referencing relations.
Fields on relations | To reference fields on relations, use the notation relation.fieldOnRelation of a relation. For example: data.relationName[0].fieldOnRelation. In many cases, it’s useful to loop through relations with for (const relation of data.relationName){ ... relation.fieldOnRelation ... }.
Fields on related fact sheets | To reference fields on related fact sheets, use the notation relation.factsheet of a relation. For example, in a calculation for business capability fact sheets, you can access the functionalSuitability field on related applications with data.relBusinessCapabilityToApplication[0].factsheet.functionalSuitability.


**Note**
For source fields referenced in calculations, you can populate data using any method: manual input or automated population through integrations. Calculations trigger regardless of the method you use.
