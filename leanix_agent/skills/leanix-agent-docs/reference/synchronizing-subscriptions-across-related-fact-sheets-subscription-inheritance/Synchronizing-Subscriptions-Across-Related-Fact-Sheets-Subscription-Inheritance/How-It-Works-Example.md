##  How It Works: Example
If an IT component is related to multiple applications, it will inherit subscriptions from all related applications. For example:
  * Application A has owner 1 and owner 2
  * Application B has owner 2 and owner 3
  * Shared IT component will have owner 1, owner 2, and owner 3


When a relation is removed:
  * If application A is unlinked, owner 1 will be removed from the IT component (assuming no other applications have owner 1).
  * Owner 2 will remain because application B still has owner 2.
