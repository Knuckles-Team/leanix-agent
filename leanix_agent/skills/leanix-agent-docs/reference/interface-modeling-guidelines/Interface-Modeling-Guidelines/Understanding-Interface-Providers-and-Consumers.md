##  Understanding Interface Providers and Consumers
The terms “provider” and “consumer” relate to ownership and change management, not to the direction of data flow.
  * Provider : Owns the interface and is responsible for its change management. Each interface can only have one provider.
  * Consumer: Owns the interface but doesn’t manage its changes. A single interface can have multiple consumers.


In most cases the role of provider and consumer can be clearly defined. However, there are situations where this isn’t as straightforward. For example, you might not be aware of all of the consumers for public APIs. If this is the case, you can leave the consumer field empty in the fact sheet.
For technologies like FTP (File Transfer Protocol), it can be more challenging to identify which system is the provider or consumer. To manage this ambiguity, it’s best to establish clear guidelines or conventions to consistently determine providers and consumers.
