##  Aggregating Obsolescence Risk for Self-Built Software
The aggregated obsolescence risk is calculated based on the lifecycle status of the underlying IT components that support your microservices. The calculation for aggregated obsolescence risk considers both:
  * IT components that are directly linked to the microservice.
  * IT components indirectly linked to the microservice either through parent/child relations between IT components or as required/required by relations between IT components.


Hence, we recommend the following:
  * Link the versioned IT component that is actually in use directly to the microservice.This ensures that the microservice inherits the correct lifecycle and obsolescence risk, since lifecycle information is typically maintained at the version level and not at the product-line level
  * Model product lines as the parent IT component of the versioned IT components.This enables governance, reporting, and grouping at the product-line level. Do not relate the product-line IT component directly to the microservice to avoid incorrectly carrying over aggregated risk.


In the example below, Angular 4, Angular 17, Angular 20, and Angular 21 are versioned IT components having varied lifecycles. Only Angular 21 is actually in use for the microservice, and hence it is directly related to the microservice.
![Modeling Approach to Aggregate Obsolescence Risk for Self-Built Software Discovery](https://help.sap.com/doc/72d375467c1e4dcb872dfa2998b6328d/CLOUD/en-US/loiod8cccc8a1c934107a4f4a9f6e9b68ad6_LowRes.png)
Modeling Approach to Aggregate Obsolescence Risk for Self-Built Software Discovery
Since the microservice is not directly related to the product-line IT component Angular, it does not inherit risk from other versioned IT components under that product line. This avoids incorrect risk status and keeps the inventory factually tied to the technology each microservice is actually running.
### Risk Aggregation at Application Level
For obsolescence risk aggregation at the application level, IT components that are indirectly connected to the application through microservices are also included. This ensures that the appropriate obsolescence risk is correctly surfaced.
For a more detailed guide, see [Obsolescence Risk View Aggregation at the Application Level](https://help.sap.com/docs/leanix/ea/technology-obsolescence-risk-statuses-and-views-in-reports?locale=en-US&state=PRODUCTION&version=CLOUD#loio275db19f7a4410148852ce7f597a5c65__obsolescence_risk_view_aggregation_at_the_application_level).
The precedence logic for vendor and internal lifecycle data applies as usual. For more information, see [Obsolescence Risk Statuses of IT Components](https://help.sap.com/docs/leanix/ea/technology-obsolescence-risk-statuses-and-views-in-reports?locale=en-US&state=PRODUCTION&version=CLOUD#loio275db19f7a4410148852ce7f597a5c65__obsolescence_risk_statuses_of_it_component).
