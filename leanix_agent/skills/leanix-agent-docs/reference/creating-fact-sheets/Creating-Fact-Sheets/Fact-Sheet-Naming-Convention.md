##  Fact Sheet Naming Convention
Fact sheets have 3 different name values to ensure structured and consistent identification:
Name: This is the user-provided identifier for the fact sheet. It doesn't have to be unique by itself but is used to form the full name. If the provided name doesn't result in a unique full name, the user is prompted to provide a different name.
Full Name: The system automatically generates the full name using the fact sheet's name and it may include prefixes (such as provider information) and suffixes (like release details), which vary based on the specific fact sheet type.
Display Name: The display name is the complete name shown in the fact sheet header, incorporating parent-child relationships. Display names are important for accurately referencing fact sheets when importing relations via Excel files.
Fact Sheet Type | Full Name | Display Name
---|---|---
Application | [name] [Release] | [Parent 1] / [Parent n] / [Full Name]
Business Capability | [name] | [Parent 1] / [Parent n] / [Full Name]
Business Context | [name] | [Parent 1] / [Parent n] / [Full Name]
Data Object | [name] | [Parent 1] / [Parent n] / [Full Name]
Initiative | [name] | [Parent 1] / [Parent n] / [Full Name]
Interface | [name] [Release] | [Parent 1] / [Parent n] / [Full Name]
IT Component | [Provider] [Name] [Release] | [Parent 1] / [Parent n] / [Full Name]
Platform | [name] | [Parent 1] / [Parent n] / [Full Name]
Objective | [name] | [Parent 1] / [Parent n] / [Full Name]
Organization | [name] | [Parent 1] / [Parent n] / [Full Name]
Provider | [name] | [Parent 1] / [Parent n] / [Full Name]
Tech Category | [name] | [Parent 1] / [Parent n] / [Full Name]


**Note**
Using Forward Slashes in Fact Sheet Names: If you need to use a forwarded slash /in the name of a fact sheet itself, you can use the / without a space before and after.
