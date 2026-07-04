"""LeanIX Enterprise Architecture ontology contribution (CONCEPT:AU-KG.ontology.package-federation-migration).

Data-only subpackage: it carries ``leanix.ttl`` (the ``owl:Ontology``
``http://knuckles.team/kg/leanix`` module — fact sheets, applications, IT
components and their enterprise-architecture relationships) which the
agent-utilities hub federates in via the ``agent_utilities.ontology_providers``
entry-point. It holds no business logic and no heavy imports so the hub can
resolve it cheaply.
"""
