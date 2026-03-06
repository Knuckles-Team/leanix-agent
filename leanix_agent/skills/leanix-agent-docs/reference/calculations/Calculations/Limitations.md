##  Limitations
  * You can have only one active calculation for a specific target field.
  * You can use Base fields as source fields, but not as target fields. This means you can read data from these fields, but you can't write data to them.
  * Reading a target field as a source field isn't supported. You can't select a target field and then use the same field within a calculation to update it. This creates an infinite loop because an update to the target field triggers the calculation again.
