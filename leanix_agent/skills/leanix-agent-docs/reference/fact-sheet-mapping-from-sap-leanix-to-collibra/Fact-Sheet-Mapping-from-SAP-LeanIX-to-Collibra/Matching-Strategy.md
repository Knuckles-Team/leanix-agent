##  Matching Strategy
When the integration maps fact sheets to Collibra, there might already be an existing asset with the same name. To handle such situations, you can select one of the following options:
  * No Matching: The integration always attempts to create a new asset, regardless of existing entities. If a conflict arises, a warning appears in the synchronization log. This is the default option.
  * Match By Name: Before creating a new asset, the integration checks for an existing asset with the same name. If the asset type and inbox domain match, the integration uses the existing asset as the target for mapping. Instead of creating a new asset, the integration updates the matched asset.
