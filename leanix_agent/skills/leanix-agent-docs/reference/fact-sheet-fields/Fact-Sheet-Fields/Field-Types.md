##  Field Types
The following table lists the field types supported in the meta model.
Field Type | Description | Available for Custom Fields
---|---|---
Double | A double-precision floating-point data type is used for numeric values that can include decimal points. It provides a higher precision level than a single-precision floating-point data type. | Yes
Integer | Integer is a data type used for whole numbers, which means it represents non-decimal numeric values. For example, 1, 2, 3, -5, and so on. | Yes
Multiple Select | A multiple-select field enables users to select several options from a given list. It’s suitable when more than one choice is possible. The IDs (keys) of field values must start with a letter. | Yes
Single Select | A single-select field enables users to pick a single option from a list. It's suitable when only one choice is applicable or allowed. The IDs (keys) of field values must start with a letter. | Yes
String |  String is a data type used for text or character-based information. It can encompass letters, numbers, symbols, and other characters, making it useful for various types of textual data. In string fields, you can include URLs using Markdown syntax. For example: [link text](link-url). Multiple links in a single field aren't supported. Make sure to add only one link. | Yes
Base Field | Base field refers to a fundamental or essential field within the database. It is a core element that often serves as a foundation for other fields and data components. Base fields can include fundamental data types like text, numbers, dates, or identifiers. | No
External Id | An external ID field refers to a database field linked or associated with data from an external source or system. It may be used to store data retrieved or integrated from outside the current database or application. External fields are used to import and manage data originating from external systems, files, or sources. | No


**Note**
Some fields may be of a custom type that is not listed in the table, such as Project Status or Lifecycle. You can’t configure these fields.
