##  Partial Sync Mode
This is the property that sets how the partials sync should be executed. It has three options: FULL, SKIP and WITHOUT_RELATION
![](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio274cdcf07a4410149a02b8eeb0b0c8e8_LowRes.png)
Options | Description
---|---
FULL | Fact sheet mappings and relation mappings will be processed during a partial change.
SKIP | Partial changes will not trigger a synchronization run.
WITHOUT RELATIONS | Only fact sheet mappings will be processed during a partial change. Relation mappings are skipped.


