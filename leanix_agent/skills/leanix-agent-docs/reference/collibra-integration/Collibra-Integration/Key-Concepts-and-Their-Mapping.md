##  Key Concepts and Their Mapping
The following are some terms and their definitions that help enterprise architects understand Collibra’s operating model:
Collibra Term | Description | Representation in SAP LeanIX
---|---|---
Community | A community is a grouping of subcommunities and domains, typically reflecting functional divisions within a company. It is most effective when aligned with the organization's governance structure. | Can be synced as a data object with a parent-child relation with its respective domains.
Domain | A domain is a logical grouping of assets that belongs to exactly one community. | Can be synced as a data object with a parent community and the underlying assets as parent-child relations.
Asset/Asset Types | An asset is a fundamental building block used to capture information. It belongs to exactly one domain and has a unique name within that domain. Each asset is an instance of a single asset type—such as a business asset, data asset, governance asset, issue, or technology asset. To learn more, see [Overview of Packaged Asset Types![Information published on non-SAP site](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/themes/sap-light/img/3rd_link.png)](https://help.sap.com/docs/link-disclaimer?site=https%3A%2F%2Fproductresources.collibra.com%2Fdocs%2Fcollibra%2Flatest%2FContent%2FAssets%2FAssetTypes%2Fref_ootb-asset-types.htm "https://productresources.collibra.com/docs/collibra/latest/Content/Assets/AssetTypes/ref_ootb-asset-types.htm"). | Assets are imported from Collibra into SAP LeanIX as data objects. Currently, the integration supports two asset types: business assets and data assets. Business assets are particularly relevant for this integration.
Attribute | An attribute is a specific piece of information that describes an asset. Each asset can have multiple attributes to capture its key details. | Synced as fields, such as name or description.
Relation | A relation connects exactly two assets and defines how they are related. An asset can have multiple relations, each representing a specific type of connection. | 'Groups' relations from Collibra are represented as relations between data objects.


