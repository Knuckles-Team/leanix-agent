##  Best Practices
Before diving into best practices, let's consider an example: a webshop with three microservices—a login micro-frontend, a payment processing backend, and a recommender service. Each microservice provides a unique business capability:
  * Payment processing backend: Ensures successful and fast payment checkout.
  * Recommender service: Offers tailored suggestions for additional purchases.
  * Login micro-frontend: Provides a quick introduction to the webshop.


In these scenarios, both the ingestion and best-practice meta model allow you to analyze this product-oriented setup natively. For instance:
  * Which teams power my webshop product?
  * If the payment engine is down, what products are affected? What is the business impact (by knowing the affected business capabilities)?
  * If I want to make changes or launch a new product, which existing capabilities or microservices can be used? What's the impact if we deprecate the payment engine? Who's affected if we update the API?
  * Which technologies power our business (for example, SAP LeanIX's tech stack)?


In summary, this default best practice enables native analysis from the following perspectives:
  * API management: By modeling microservices as applications and using providing and consuming relations to bind interfaces (for example, REST API or Async), you can leverage interface circle reports to discern dependencies between core product elements. This is helpful for planning migrations or transformations and understanding the cost of changes to existing product IT elements.
  * Clear distinction between product and technology: Distinguish logical product building product / business blocks (microservices) from the technology used (IT components and third-party libraries via SBOM).
  * Ownership: By using the dedicated team relation and status as a business artifact (rather than technology), understanding microservice ownership becomes a core element of maintenance.
  * Technology standards: Analyze used technologies in the context of their product role to drive technology standardization.


![Best-Practice, Product-Centric Microservice Modeling](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loio2742a5ed7a4410149266a12371333983_LowRes.png)
Best-Practice, Product-Centric Microservice Modeling
