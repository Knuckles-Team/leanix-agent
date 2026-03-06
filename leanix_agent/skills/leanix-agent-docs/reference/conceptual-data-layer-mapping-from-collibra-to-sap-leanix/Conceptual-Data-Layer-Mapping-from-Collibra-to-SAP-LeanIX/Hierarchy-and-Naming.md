##  Hierarchy and Naming
In the Hierarchy Mapping list, you can choose whether you want to map the communities and domains from Collibra to SAP LeanIX. If you choose to map the hierarchy, fact sheets are created to match the Collibra hierarchy, establishing parent-child relationships from community, sub-community, and domain down to assets. If you choose not to map the hierarchy by selecting None, then only fact sheets for assets are created.
Based on your configuration, the integration will scan the defined communities for all sub-communities, domains, and assets and will create a data object fact sheet for each of them using the following rules:
  * The Name of the created fact sheet in SAP LeanIX will match the name of the corresponding object in Collibra.
  * The Display Name of the fact sheets will be derived from the following hierarchy:
    * For each sub-community, the corresponding fact sheet is suffixed with "relToParent" relation to its parent community.
    * For each domain, the corresponding fact sheet is suffixed with "relToParent" relation to its community.
    * For each asset, the corresponding fact sheet is suffixed with "relToParent" relation to its domain.
![Hierarchy and Naming Conventions](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274885a67a441014978c8d0ffd1e405f_LowRes.png)
Hierarchy and Naming Conventions
