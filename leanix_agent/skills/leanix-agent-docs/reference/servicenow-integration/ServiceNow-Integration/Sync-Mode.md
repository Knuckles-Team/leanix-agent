##  Sync Mode
A sync mode for integration configuration can be defined in three ways, depending on the specific requirements of preserving/ deleting the items from the target system.
  * Additive Sync: This Sync Mode only creates and updates items and never deletes anything. This is the safest Sync Mode, but it can lead to duplicate data if not used carefully.
  * Conservative Sync: This sync mode only deletes items created in the target system and are no longer linked to any source object. This Sync Mode preserves manually created items and items that are linked to sources controlled by other integrations. Items that were created by a different integration (e.g. Collibra) will be preserved as well as part of this sync.
  * Overwrite Sync: This Sync Mode deletes any items that are not linked to a source object, or that are linked to a source object that no longer exists. This Sync Mode is the most likely to lead to data loss, but it is also the most likely to ensure that your data is consistent with the source system.


![Selecting a Sync Mode for a Mapping](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2742e3367a44101491d8e1ccc188fb24_LowRes.png)
Selecting a Sync Mode for a Mapping
Sync Mode behavior:
Direction | Additive Sync | Conservative Sync | Overwrite Sync
---|---|---|---
Foreign → LeanIX (SAP LeanIX is the target) | No deletion will happen | Every Fact Sheet will be deleted that has an externalId of the running configuration but the corresponding item on the source is missing AND no further externalId is specified on the Fact Sheet. | Every Fact Sheet will be deleted, that has NO externalId of the running configuration or this externalId links an object that does not exist.
LeanIX → Foreign (Foreign is the target) | No deletion will happen | Every Foreign item from the target will be deleted if no Fact Sheet is found that is linked to this item, considering the configuration externalId. This will happen if a previous linked FactSheet is archived or the item in the foreign system is manually created. | Every foreign item from the target will be deleted that has no valid link to a FactSheet when considering the configuration externalId.


