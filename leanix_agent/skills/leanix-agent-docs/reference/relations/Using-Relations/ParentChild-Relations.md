##  Parent/Child Relations
Parent/child relations in SAP LeanIX allow you to create hierarchical structures within a single fact sheet type—such as business capabilities, organizations, or tech categories. These relations form a tree structure, where a child fact sheet can have only one parent, but a parent fact sheet can have multiple children. This results in a multilevel hierarchy, for example:
  * Level 1: Top-level parent
  * Level 2: Children of the top-level parent
  * Level 3: Children of level 2 parents


Hierarchies are used in landscape and matrix reports for the clustering and aggregation of the items. For example, in an application landscape, the applications get clustered by business capabilities (or any other relation that you choose). This gives a structure to navigate your applications in a meaningful way. While hierarchies for representing your organization, your capabilities, or data objects make perfect sense, they don’t work well for things that are long lists, for example, the applications or IT components of your EA repository.
![Example of how applications are rolled-up into the business capabilities, giving a structure to the data that is meaningful to your business.](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274c03797a441014b505fe7c75520924_LowRes.png)
Example of how applications are rolled-up into the business capabilities, giving a structure to the data that is meaningful to your business.
