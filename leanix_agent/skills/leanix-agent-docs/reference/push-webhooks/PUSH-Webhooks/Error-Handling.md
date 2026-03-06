##  Error Handling
If event delivery fails, retries occur every 50 seconds until successful. Delivery may fail in the following cases:
  * The target URL is unreachable or is improperly configured.
  * The client returns a non-successful HTTP response code.


To skip events that cannot be delivered to the target URL, select the Ignore errors option in the webhook configuration. With this option enabled, delivery retries do not occur.
