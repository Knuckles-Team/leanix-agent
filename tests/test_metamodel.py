"""Dynamic LeanIX metamodel and ontology generation coverage."""

from __future__ import annotations

from unittest.mock import MagicMock

import pytest
import rdflib

from leanix_agent.metamodel import compile_instance_ontology, discover_meta_model


def _custom_model():
    return {
        "tagGroups": [
            {
                "id": "criticality",
                "name": "Criticality",
                "tags": [
                    {"id": "high", "name": "High"},
                    {"id": "low", "name": "Low"},
                ],
            }
        ],
        "factSheets": {
            "CustomPlatform": {
                "subtypes": [{"id": "internal", "name": "Internal"}],
                "fields": {
                    "hostingModel": {
                        "type": "SINGLE_SELECT",
                        "values": [
                            {"id": "cloud", "name": "Cloud"},
                            {"id": "onprem", "name": "On Premises"},
                        ],
                    }
                },
                "relations": {
                    "relCustomPlatformToApplication": {
                        "targetFactSheetType": "Application"
                    }
                },
            },
            "Application": {"fields": {}, "relations": {}},
        },
    }


def test_custom_metamodel_compiles_types_relations_fields_and_taxonomy():
    artifact = compile_instance_ontology(_custom_model())

    assert artifact.class_count == 2
    assert artifact.object_property_count == 1
    assert artifact.taxonomy_concept_count == 5
    assert artifact.node_shape_count == 2
    assert artifact.type_map["CustomPlatform"][0] == "CustomPlatform"
    assert artifact.relation_map["relCustomPlatformToApplication"][1] == "Application"
    assert ":CustomPlatform a owl:Class" in artifact.turtle
    assert ":hostingModel a owl:DatatypeProperty" in artifact.turtle
    assert "skos/core#Concept" in artifact.turtle
    assert "shacl#NodeShape" in artifact.turtle
    rdflib.Graph().parse(data=artifact.turtle, format="turtle")


def test_ontology_is_deterministic_across_mapping_order():
    first = _custom_model()
    second = {
        "factSheets": dict(reversed(list(first["factSheets"].items()))),
        "tagGroups": first["tagGroups"],
    }

    left = compile_instance_ontology(first)
    right = compile_instance_ontology(second)

    assert left.schema_digest == right.schema_digest
    assert left.turtle == right.turtle


def test_discover_meta_model_prefers_rich_data_model():
    client = MagicMock()
    client.request_api.return_value = {"status": 200, "data": _custom_model()}

    result = discover_meta_model(client)

    assert result == _custom_model()
    client.request_api.assert_called_once_with(
        "GET", "models/dataModel", service="pathfinder", version="v1"
    )


def test_discovery_has_no_deprecated_endpoint_fallback():
    client = MagicMock()
    client.request_api.return_value = {"status": 200, "data": {}}

    with pytest.raises(RuntimeError, match="data model"):
        discover_meta_model(client)

    client.request_api.assert_called_once_with(
        "GET", "models/dataModel", service="pathfinder", version="v1"
    )


def test_compiler_excludes_person_entities_and_personal_fields():
    model = _custom_model()
    model["factSheets"]["Person"] = {
        "fields": {"email": {"type": "STRING"}},
        "relations": {},
    }
    model["factSheets"]["Application"]["fields"] = {
        "owner": {"type": "STRING"},
        "description": {"type": "STRING"},
    }

    artifact = compile_instance_ontology(model)

    assert "Person" not in artifact.type_map
    assert "owner" not in artifact.meta_model["factSheets"]["Application"]["fields"]
    assert "description" in artifact.meta_model["factSheets"]["Application"]["fields"]
    assert ":Person a owl:Class" not in artifact.turtle


def test_compiler_rejects_unbounded_type_count():
    model = {
        "factSheets": {
            f"Type{number}": {"fields": {}, "relations": {}} for number in range(1_025)
        }
    }

    with pytest.raises(ValueError, match="type count"):
        compile_instance_ontology(model)
