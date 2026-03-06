##  Relation Types
Relation Type | Description
---|---
All relations to hardware | Represents the default behavior, reading the entire cmdb_rel_ci table to find connections between applications and hardware instances. It can result in lengthy synchronization times and uncover relations that aren't immediately visible in ServiceNow.
Relations to hardware by types | Similar to All relations to hardware, but allows filtering by one or multiple cmdb_rel_ci relation types.
Relations to hardware by query | Similar to All relations to hardware, but allows filtering by a provided ServiceNow query when reading cmdb_rel_ci relations.
All relations to hardware by hops |  Reads the entire cmdb_rel_ci table to find connections, but allows specifying the maximum number of hops to consider relations between applications and hardware instances. The value must be 2 or greater. Hops are equivalent to relation levels, capturing direct relations and those passing through intermediary items (1 or 2 hops). For example, if you set the hops count to 2, the integration creates relations up to 2 levels deep, capturing:
  * Direct relations
  * Relations that pass through one intermediary item (1 hop)
  * Relations that pass through two intermediary items (2 hops)




