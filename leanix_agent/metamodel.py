"""Live LeanIX metamodel discovery and instance ontology generation."""

from __future__ import annotations

import hashlib
import json
import re
from types import SimpleNamespace
from typing import Any
from urllib.parse import quote

from agent_utilities.security.persistence_privacy import PersistencePrivacyGuard
from pydantic import BaseModel, ConfigDict, Field

_GRAPH_NAME = re.compile(r"^[_A-Za-z][_0-9A-Za-z]*$")
_PERSON_TYPE = re.compile(
    r"(?:^|[_-])(?:person|user|employee|contact)(?:$|[_-])", re.IGNORECASE
)
_MAX_METAMODEL_BYTES = 4 * 1024 * 1024
_MAX_FACTSHEET_TYPES = 1_024
_MAX_MEMBERS_PER_TYPE = 2_048
_MAX_TAXONOMY_ITEMS = 100_000


class InstanceOntology(BaseModel):
    """Deterministic ontology artifact compiled from one live LeanIX workspace."""

    model_config = ConfigDict(arbitrary_types_allowed=True)

    schema_digest: str
    ontology_iri: str
    class_count: int = Field(ge=0)
    object_property_count: int = Field(ge=0)
    datatype_property_count: int = Field(ge=0)
    taxonomy_concept_count: int = Field(ge=0)
    node_shape_count: int = Field(ge=0)
    type_map: dict[str, tuple[str, str]]
    relation_map: dict[str, tuple[str, str]]
    turtle: str
    meta_model: dict[str, Any]


def _payload_data(value: Any) -> Any:
    """Unwrap the universal transport and ordinary Pathfinder response envelopes."""
    current = value
    for _ in range(4):
        if not isinstance(current, dict) or "data" not in current:
            break
        candidate = current["data"]
        if not isinstance(candidate, dict):
            break
        if "factSheets" in current:
            break
        current = candidate
    return current


def _has_fact_sheet_types(value: Any) -> bool:
    if not isinstance(value, dict):
        return False
    fact_sheets = value.get("factSheets")
    return isinstance(fact_sheets, (dict, list)) and bool(fact_sheets)


def _named_item_row(fallback: Any, item: Any) -> tuple[str, str, dict[str, Any]]:
    """Derive one stable id/label/payload row for a taxonomy member."""
    payload = item if isinstance(item, dict) else {"value": item}
    identifier = (
        payload.get("id") or payload.get("key") or payload.get("name") or fallback
    )
    label = (
        payload.get("label")
        or payload.get("displayName")
        or payload.get("name")
        or identifier
    )
    return str(identifier), str(label), payload


def _named_items(value: Any) -> list[tuple[str, str, dict[str, Any]]]:
    """Normalize LeanIX list/dict taxonomies into stable id, label, payload rows."""
    if isinstance(value, dict):
        iterable = value.items()
    elif isinstance(value, list):
        iterable = enumerate(value)
    else:
        return []
    return [_named_item_row(fallback, item) for fallback, item in iterable]


def _privacy_safe_field(name: str) -> bool:
    """Return whether a schema field name may cross the persistence boundary."""
    clean, report = PersistencePrivacyGuard().sanitize({name: "present"})
    return not report.changed and clean.get(name) == "present"


def _normalized_fact_sheet_members(
    normalized: dict[str, Any], key: str
) -> dict[str, Any]:
    """Return one fact-sheet's fields/relations, filtered to safe member names."""
    members = _named_items(normalized.get(key) or {})
    if len(members) > _MAX_MEMBERS_PER_TYPE:
        raise ValueError("LeanIX metamodel member count exceeds the limit")
    return {
        member_id: payload
        for member_id, _member_label, payload in members
        if _GRAPH_NAME.fullmatch(member_id)
        and (key == "relations" or _privacy_safe_field(member_id))
    }


def _normalized_fact_sheet(definition: dict[str, Any]) -> dict[str, Any]:
    """Normalize one fact-sheet definition's field and relation member sets."""
    normalized = dict(definition)
    for key in ("fields", "relations"):
        normalized[key] = _normalized_fact_sheet_members(normalized, key)
    return normalized


def _filtered_fact_sheets(
    rows: list[tuple[str, str, dict[str, Any]]],
) -> dict[str, Any]:
    """Return privacy-safe, GraphQL-named fact-sheet definitions keyed by type."""
    filtered: dict[str, Any] = {}
    for type_id, _label, definition in rows:
        if not _GRAPH_NAME.fullmatch(type_id) or _PERSON_TYPE.search(type_id):
            continue
        filtered[type_id] = _normalized_fact_sheet(definition)
    return filtered


def _taxonomy_item_count(clean: dict[str, Any]) -> int:
    """Return the total normalized taxonomy row count across known taxonomy keys."""
    return sum(
        len(_named_items(value))
        for key, value in clean.items()
        if key in {"tags", "taxonomies", "tagGroups"}
    )


def _bounded_meta_model(meta_model: dict[str, Any]) -> dict[str, Any]:
    """Sanitize the live model and reject inputs that could exhaust compilation."""
    canonical = json.dumps(
        meta_model, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    )
    if len(canonical.encode("utf-8")) > _MAX_METAMODEL_BYTES:
        raise ValueError("LeanIX metamodel exceeds the compilation size limit")
    clean, _report = PersistencePrivacyGuard().sanitize(meta_model)
    if not isinstance(clean, dict):
        raise ValueError("LeanIX metamodel is not an object")
    definitions = clean.get("factSheets")
    if not isinstance(definitions, (dict, list)):
        raise ValueError("LeanIX metamodel has no factSheets definition")
    rows = _named_items(definitions)
    if not rows or len(rows) > _MAX_FACTSHEET_TYPES:
        raise ValueError("LeanIX metamodel fact-sheet type count is invalid")

    filtered = _filtered_fact_sheets(rows)
    if not filtered:
        raise ValueError("LeanIX metamodel has no privacy-safe fact-sheet types")
    clean["factSheets"] = filtered

    if _taxonomy_item_count(clean) > _MAX_TAXONOMY_ITEMS:
        raise ValueError("LeanIX metamodel taxonomy exceeds the limit")
    return clean


def _tag_group_collections(meta_model: dict[str, Any]) -> list[tuple[str, str, Any]]:
    """Return one taxonomy collection per non-empty tag group."""
    collections: list[tuple[str, str, Any]] = []
    for group_id, group_label, group in _named_items(meta_model.get("tagGroups")):
        values = group.get("tags") or group.get("values") or group.get("options")
        if values:
            collections.append((f"tag-group-{group_id}", group_label, values))
    return collections


def _fact_sheet_field_collections(
    type_id: str, definition: dict[str, Any]
) -> list[tuple[str, str, Any]]:
    """Return one taxonomy collection per enumerated field on a fact-sheet type."""
    collections: list[tuple[str, str, Any]] = []
    fields = definition.get("fields") or {}
    for field_id, field_label, field in _named_items(fields):
        values = (
            field.get("values") or field.get("options") or field.get("allowedValues")
        )
        if values:
            collections.append((f"{type_id}-{field_id}", f"{type_id} {field_label}", values))
    return collections


def _fact_sheet_taxonomy_collections(
    meta_model: dict[str, Any],
) -> list[tuple[str, str, Any]]:
    """Return the subtype and enumerated-field taxonomy collections for every type."""
    collections: list[tuple[str, str, Any]] = []
    fact_sheets = meta_model.get("factSheets") or {}
    for type_id, _, definition in _named_items(fact_sheets):
        if definition.get("subtypes"):
            collections.append(
                (f"{type_id}-subtypes", f"{type_id} subtypes", definition["subtypes"])
            )
        collections.extend(_fact_sheet_field_collections(type_id, definition))
    return collections


def _taxonomy_collections(meta_model: dict[str, Any]) -> list[tuple[str, str, Any]]:
    """Return every discovered taxonomy collection across the live metamodel."""
    collections: list[tuple[str, str, Any]] = [
        (key, key, meta_model[key])
        for key in ("tags", "taxonomies")
        if meta_model.get(key)
    ]
    collections.extend(_tag_group_collections(meta_model))
    collections.extend(_fact_sheet_taxonomy_collections(meta_model))
    return collections


def _skos_concept_lines(
    collection_id: str, values: Any, scheme: str, base: str
) -> tuple[list[str], int]:
    """Render the sorted SKOS Concept lines for one taxonomy collection."""
    lines: list[str] = []
    count = 0
    for identifier, concept_label, _ in sorted(
        _named_items(values), key=lambda item: item[0]
    ):
        concept = (
            base + "concept:" + quote(collection_id, safe="") + ":" + quote(identifier, safe="")
        )
        lines.append(
            f"<{concept}> a <http://www.w3.org/2004/02/skos/core#Concept> ;\n"
            f"    <http://www.w3.org/2000/01/rdf-schema#label> "
            f"{json.dumps(concept_label, ensure_ascii=False)} ;\n"
            f"    <http://www.w3.org/2004/02/skos/core#inScheme> <{scheme}> ."
        )
        count += 1
    return lines, count


def _taxonomy_turtle(meta_model: dict[str, Any], digest: str) -> tuple[str, int]:
    """Compile tag groups, subtypes, and enumerated field values as SKOS concepts."""
    collections = _taxonomy_collections(meta_model)
    base = f"urn:leanix:taxonomy:{digest}:"
    lines: list[str] = []
    count = 0
    for collection_id, label, values in sorted(collections, key=lambda item: item[0]):
        scheme = base + "scheme:" + quote(collection_id, safe="")
        lines.append(
            f"<{scheme}> a <http://www.w3.org/2004/02/skos/core#ConceptScheme> ;\n"
            f"    <http://www.w3.org/2000/01/rdf-schema#label> "
            f"{json.dumps(label, ensure_ascii=False)} ."
        )
        concept_lines, concept_count = _skos_concept_lines(
            collection_id, values, scheme, base
        )
        lines.extend(concept_lines)
        count += concept_count
    return ("\n\n".join(lines) + ("\n" if lines else ""), count)


_SHACL_DATATYPES = {
    "BOOLEAN": "http://www.w3.org/2001/XMLSchema#boolean",
    "DATE": "http://www.w3.org/2001/XMLSchema#date",
    "DATE_TIME": "http://www.w3.org/2001/XMLSchema#dateTime",
    "DECIMAL": "http://www.w3.org/2001/XMLSchema#decimal",
    "DOUBLE": "http://www.w3.org/2001/XMLSchema#double",
    "INTEGER": "http://www.w3.org/2001/XMLSchema#integer",
    "LONG": "http://www.w3.org/2001/XMLSchema#long",
}


def _truthy(value: Any) -> bool:
    return value is True or str(value).lower() in {"1", "true", "required", "mandatory"}


def _cardinality(payload: dict[str, Any], key: str) -> int | None:
    value = payload.get(key)
    if isinstance(value, int) and value >= 0:
        return value
    if isinstance(value, str) and value.isdigit():
        return int(value)
    return None


def _field_cardinality_constraints(field: dict[str, Any]) -> list[str]:
    """Return the minCount/maxCount constraints declared for one field."""
    constraints: list[str] = []
    minimum = _cardinality(field, "minCardinality")
    maximum = _cardinality(field, "maxCardinality")
    if minimum is not None:
        constraints.append(f"<http://www.w3.org/ns/shacl#minCount> {minimum}")
    if maximum is not None:
        constraints.append(f"<http://www.w3.org/ns/shacl#maxCount> {maximum}")
    return constraints


def _field_enumeration_constraint(field: dict[str, Any]) -> list[str]:
    """Return the sh:in enumeration constraint for one field, if it has values."""
    values = field.get("values") or field.get("options") or field.get("allowedValues")
    literals = [
        json.dumps(label, ensure_ascii=False) for _, label, _ in _named_items(values)
    ]
    if not literals:
        return []
    return ["<http://www.w3.org/ns/shacl#in> (" + " ".join(literals) + ")"]


def _field_shacl_constraints(field_id: str, field: dict[str, Any]) -> list[str]:
    """Return the SHACL property constraints for one fact-sheet field."""
    constraints = [
        f"<http://www.w3.org/ns/shacl#path> <http://knuckles.team/kg#{field_id}>"
    ]
    if _truthy(field.get("required") or field.get("mandatory")):
        constraints.append("<http://www.w3.org/ns/shacl#minCount> 1")
    constraints.extend(_field_cardinality_constraints(field))
    datatype = _SHACL_DATATYPES.get(str(field.get("type") or ""))
    if datatype:
        constraints.append(f"<http://www.w3.org/ns/shacl#datatype> <{datatype}>")
    constraints.extend(_field_enumeration_constraint(field))
    return constraints


def _fact_sheet_field_properties(definition: dict[str, Any]) -> list[str]:
    """Return one SHACL property block per GraphQL-named fact-sheet field."""
    properties: list[str] = []
    for field_id, _, field in sorted(
        _named_items(definition.get("fields") or {}), key=lambda item: item[0]
    ):
        if not _GRAPH_NAME.fullmatch(field_id):
            continue
        constraints = _field_shacl_constraints(field_id, field)
        properties.append("[ " + " ; ".join(constraints) + " ]")
    return properties


def _relation_shacl_constraints(
    relation_id: str, relation: dict[str, Any]
) -> list[str]:
    """Return the SHACL property constraints for one fact-sheet relation."""
    constraints = [
        f"<http://www.w3.org/ns/shacl#path> <http://knuckles.team/kg#{relation_id}>"
    ]
    target = (
        relation.get("targetFactSheetType")
        or relation.get("targetType")
        or relation.get("target")
    )
    if isinstance(target, str) and _GRAPH_NAME.fullmatch(target):
        constraints.append(
            f"<http://www.w3.org/ns/shacl#class> <http://knuckles.team/kg#{target}>"
        )
    for source_key, predicate in (
        ("minCardinality", "minCount"),
        ("maxCardinality", "maxCount"),
    ):
        cardinality = _cardinality(relation, source_key)
        if cardinality is not None:
            constraints.append(
                f"<http://www.w3.org/ns/shacl#{predicate}> {cardinality}"
            )
    return constraints


def _fact_sheet_relation_properties(definition: dict[str, Any]) -> list[str]:
    """Return one SHACL property block per GraphQL-named ``rel*`` relation."""
    properties: list[str] = []
    for relation_id, _, relation in sorted(
        _named_items(definition.get("relations") or {}), key=lambda item: item[0]
    ):
        if not relation_id.startswith("rel") or not _GRAPH_NAME.fullmatch(
            relation_id
        ):
            continue
        constraints = _relation_shacl_constraints(relation_id, relation)
        properties.append("[ " + " ; ".join(constraints) + " ]")
    return properties


def _fact_sheet_shacl_properties(definition: dict[str, Any]) -> list[str]:
    """Return every SHACL property block for one fact-sheet type's shape."""
    return _fact_sheet_field_properties(definition) + _fact_sheet_relation_properties(
        definition
    )


def _fact_sheet_shape_statement(
    type_id: str, digest: str, properties: list[str]
) -> str:
    """Render one fact-sheet type's complete SHACL NodeShape statement."""
    shape = f"urn:leanix:shape:{digest}:{quote(type_id, safe='')}"
    statement = (
        f"<{shape}> a <http://www.w3.org/ns/shacl#NodeShape> ;\n"
        f"    <http://www.w3.org/ns/shacl#targetClass> "
        f"<http://knuckles.team/kg#{type_id}>"
    )
    if properties:
        statement += " ;\n    <http://www.w3.org/ns/shacl#property> " + (
            " ,\n        ".join(properties)
        )
    return statement + " ."


def _shacl_turtle(meta_model: dict[str, Any], digest: str) -> tuple[str, int]:
    """Compile tolerant field/relation constraints into SHACL node shapes."""
    lines: list[str] = []
    count = 0
    fact_sheets = meta_model.get("factSheets") or {}
    for type_id, _, definition in sorted(
        _named_items(fact_sheets), key=lambda item: item[0]
    ):
        if not _GRAPH_NAME.fullmatch(type_id):
            continue
        properties = _fact_sheet_shacl_properties(definition)
        lines.append(_fact_sheet_shape_statement(type_id, digest, properties))
        count += 1
    return ("\n\n".join(lines) + ("\n" if lines else ""), count)


def discover_meta_model(client: Any) -> dict[str, Any]:
    """Read the current authoritative workspace data model."""
    response = client.request_api(
        "GET", "models/dataModel", service="pathfinder", version="v1"
    )
    model = _payload_data(response)
    if not _has_fact_sheet_types(model):
        raise RuntimeError("LeanIX returned no usable fact-sheet data model")
    return _bounded_meta_model(model)


def compile_instance_ontology(meta_model: dict[str, Any]) -> InstanceOntology:
    """Compile every discovered type, field, and relation into deterministic OWL."""
    try:
        from agent_utilities.knowledge_graph.ontology.leanix_metamodel import (
            compile_leanix_metamodel,
            export_leanix_ttl,
        )
    except ImportError as exc:  # pragma: no cover - dependency floor guards this
        raise RuntimeError(
            "LeanIX ontology generation requires agent-utilities"
        ) from exc

    meta_model = _bounded_meta_model(meta_model)
    canonical = json.dumps(
        meta_model, sort_keys=True, separators=(",", ":"), ensure_ascii=False
    )
    digest = hashlib.sha256(canonical.encode("utf-8")).hexdigest()
    ontology_iri = f"urn:leanix:metamodel:{digest}"
    spec = compile_leanix_metamodel(meta_model)
    turtle = export_leanix_ttl(spec).replace(
        "<http://knuckles.team/kg/leanix>", f"<{ontology_iri}>", 1
    )
    taxonomy_turtle, taxonomy_count = _taxonomy_turtle(meta_model, digest)
    shacl_turtle, node_shape_count = _shacl_turtle(meta_model, digest)
    turtle += "\n" + taxonomy_turtle + "\n" + shacl_turtle
    return InstanceOntology(
        schema_digest=digest,
        ontology_iri=ontology_iri,
        class_count=len(spec.classes),
        object_property_count=len(spec.object_properties),
        datatype_property_count=len(spec.datatype_properties),
        taxonomy_concept_count=taxonomy_count,
        node_shape_count=node_shape_count,
        type_map=spec.type_map,
        relation_map=spec.relation_map,
        turtle=turtle,
        meta_model=meta_model,
    )


def load_instance_ontology(
    artifact: InstanceOntology, engine: Any, *, activate: bool = True
) -> dict[str, Any]:
    """Load the generated ontology into the live epistemic-graph RDF surface."""
    try:
        from agent_utilities.knowledge_graph.core.owl_bridge import (
            register_promotable_node_types,
        )
        from agent_utilities.knowledge_graph.ontology.lifecycle import OntologyLifecycle
    except ImportError as exc:  # pragma: no cover - dependency floor guards this
        raise RuntimeError("Ontology hosting requires agent-utilities") from exc

    register_promotable_node_types(
        mapped_type for mapped_type, _prefix in artifact.type_map.values()
    )
    authority = (
        engine
        if getattr(engine, "graph_compute", None) is not None
        else SimpleNamespace(graph_compute=engine)
    )
    result = OntologyLifecycle(authority).load(
        artifact.turtle,
        source_type="text",
        version=artifact.schema_digest,
        iri=artifact.ontology_iri,
        activate=activate,
    )
    engine_result = (result.get("ontology") or {}).get("engine") or {}
    if (
        activate
        and result.get("status") == "ok"
        and not engine_result.get("loaded_to_engine")
    ):
        raise RuntimeError(
            "LeanIX ontology was validated but not loaded into the graph reasoner"
        )
    return result
