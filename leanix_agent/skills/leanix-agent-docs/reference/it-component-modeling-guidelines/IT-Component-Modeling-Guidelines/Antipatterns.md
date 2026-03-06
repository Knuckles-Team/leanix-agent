##  Antipatterns
This section addresses antipatterns involving ineffective or counterproductive ways of modeling IT components in SAP LeanIX.
  * Don’t introduce too fine-granular versions of IT components (e.g., patch level of software).
  * Don’t confuse SaaS as a fact sheet subtype under the IT component with SaaS as an application. Generally, SaaS (the software that end users interact with) is modeled as an application. The IT component fact sheet only describes the hosting aspect of that service.
  * Don’t import all instances of deployments.
  * Don’t import all technologies before linking them to applications. Only import technologies that you really need.
  * Don’t confuse Service with SaaS or microservice fact sheet subtype.
  * If you use IT component data from the reference catalog, don’t aim for 100% coverage of having all items linked to the reference catalog; start off with your most important IT components by filtering on the IT components of critical and important applications.
