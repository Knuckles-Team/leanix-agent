"""Bounded, privacy-safe LeanIX synchronization through ChangeEnvelope."""

from __future__ import annotations

import hashlib
import inspect
import json
import re
from collections.abc import Iterable, Iterator
from dataclasses import dataclass
from typing import Any

from leanix_agent._persistence_privacy_compat import (
    PersistencePrivacyGuard,
    persistence_reference,
)
from pydantic import BaseModel, Field

from leanix_agent.metamodel import (
    InstanceOntology,
    compile_instance_ontology,
    discover_meta_model,
    load_instance_ontology,
)

_GRAPHQL_NAME = re.compile(r"^[_A-Za-z][_0-9A-Za-z]{0,127}$")
_PERSON_TYPE = re.compile(
    r"(?:^|[_-])(?:person|user|employee|contact)(?:$|[_-])", re.IGNORECASE
)
_MAX_SELECTION_DEPTH = 5
_MAX_FIELDS_PER_TYPE = 512
_MAX_QUERY_BYTES = 128 * 1024
_MAX_PAGES_PER_TYPE = 10_000
_MAX_RECORDS_PER_TYPE = 1_000_000
_MAX_CURSOR_BYTES = 4_096
_MAX_IDS_FILTER = 1_000


class InstanceSyncReport(BaseModel):
    """Auditable result of a governed LeanIX synchronization."""

    status: str
    mode: str
    schema_digest: str
    ontology: dict[str, Any]
    source_sync: dict[str, Any]
    factsheets_seen: int = Field(ge=0)
    payload_nodes: int = Field(ge=0)
    payload_relations: int = Field(ge=0)
    payload_batches: int = Field(ge=0)
    expected_factsheets: int | None = Field(default=None, ge=0)
    privacy_redactions: int = Field(default=0, ge=0)
    personal_records_skipped: int = Field(default=0, ge=0)
    partial_graphql_pages: int = Field(default=0, ge=0)
    minimal_fallback_pages: int = Field(default=0, ge=0)
    native_atomic: bool = True
    complete: bool


def _definitions(meta_model: dict[str, Any]) -> dict[str, dict[str, Any]]:
    raw = meta_model.get("factSheets")
    if isinstance(raw, dict):
        return {
            str(key): value for key, value in raw.items() if isinstance(value, dict)
        }
    return {}


def _relation_names(definition: dict[str, Any]) -> list[str]:
    raw = definition.get("relations")
    if not isinstance(raw, dict):
        return []
    names = [
        str(name)
        for name in raw
        if str(name).startswith("rel") and _GRAPHQL_NAME.fullmatch(str(name))
    ]
    if len(names) > _MAX_FIELDS_PER_TYPE:
        raise RuntimeError("LeanIX relation selection exceeds the safety limit")
    return sorted(names)


def _named_graphql_type(value: Any) -> Any:
    current = value
    while getattr(current, "of_type", None) is not None:
        current = current.of_type
    return current


def _has_required_arguments(field: Any) -> bool:
    try:
        from graphql import is_required_argument

        return any(is_required_argument(argument) for argument in field.args.values())
    except ImportError as exc:  # pragma: no cover - dependency floor guards this
        raise RuntimeError("GraphQL schema support is not installed") from exc


def _union_type_selection(
    name: str,
    named: Any,
    type_name: str,
    *,
    seen: frozenset[str],
    depth: int,
) -> str | None:
    """Build the inline-fragment selection for a GraphQL union field."""
    fragments: list[str] = []
    for possible in sorted(named.types, key=lambda item: item.name)[
        :_MAX_FIELDS_PER_TYPE
    ]:
        children = [
            selected
            for child_name, child in sorted(possible.fields.items())[
                :_MAX_FIELDS_PER_TYPE
            ]
            if _GRAPHQL_NAME.fullmatch(child_name)
            and (
                selected := _field_selection(
                    child_name,
                    child,
                    seen=seen | {type_name, possible.name},
                    depth=depth + 1,
                )
            )
        ]
        if children:
            fragments.append(f"... on {possible.name}{{{' '.join(children)}}}")
    return f"{name}{{__typename {' '.join(fragments)}}}" if fragments else None


def _cyclic_object_selection(name: str, named: Any) -> str | None:
    """Build a leaf-only selection once a type has already been visited on this path."""
    from graphql import is_enum_type, is_scalar_type

    leaves = [
        child_name
        for child_name, child in sorted(named.fields.items())[:_MAX_FIELDS_PER_TYPE]
        if _GRAPHQL_NAME.fullmatch(child_name)
        and not _has_required_arguments(child)
        and (
            is_scalar_type(_named_graphql_type(child.type))
            or is_enum_type(_named_graphql_type(child.type))
        )
    ]
    return f"{name}{{{' '.join(leaves)}}}" if leaves else None


def _object_type_selection(
    name: str,
    named: Any,
    type_name: str,
    *,
    seen: frozenset[str],
    depth: int,
) -> str | None:
    """Recursively build the field selection for a freshly visited object/interface."""
    children = [
        selected
        for child_name, child in sorted(named.fields.items())[:_MAX_FIELDS_PER_TYPE]
        if _GRAPHQL_NAME.fullmatch(child_name)
        and (
            selected := _field_selection(
                child_name,
                child,
                seen=seen | {type_name},
                depth=depth + 1,
            )
        )
    ]
    return f"{name}{{{' '.join(children)}}}" if children else None


def _named_type_selection(
    name: str, named: Any, *, seen: frozenset[str], depth: int
) -> str | None:
    """Dispatch selection-building by the field's resolved named GraphQL type."""
    from graphql import (
        is_enum_type,
        is_interface_type,
        is_object_type,
        is_scalar_type,
        is_union_type,
    )

    if is_scalar_type(named) or is_enum_type(named):
        return name
    type_name = str(getattr(named, "name", ""))
    if not _GRAPHQL_NAME.fullmatch(type_name):
        return None
    if is_union_type(named):
        return _union_type_selection(name, named, type_name, seen=seen, depth=depth)
    if not (is_object_type(named) or is_interface_type(named)):
        return None
    if type_name in seen:
        return _cyclic_object_selection(name, named)
    return _object_type_selection(name, named, type_name, seen=seen, depth=depth)


def _field_selection(
    name: str,
    field: Any,
    *,
    seen: frozenset[str] = frozenset(),
    depth: int = 0,
) -> str | None:
    """Build a finite, no-argument GraphQL selection."""
    if depth > _MAX_SELECTION_DEPTH or _has_required_arguments(field):
        return None
    named = _named_graphql_type(field.type)
    return _named_type_selection(name, named, seen=seen, depth=depth)


def _scalar_data_fields(fields: dict[str, Any]) -> list[str]:
    """Return the bounded, no-argument selections for a type's non-reserved fields."""
    data_fields: list[str] = []
    for name, field in sorted(fields.items()):
        if (
            not _GRAPHQL_NAME.fullmatch(name)
            or name in {"id", "name", "type", "updatedAt"}
            or name.startswith("rel")
        ):
            continue
        selected = _field_selection(name, field)
        if selected:
            data_fields.append(selected)
    return data_fields


def _has_usable_id(node: Any) -> bool:
    """Return whether an edge's node has the minimum shape to be counted."""
    return isinstance(node, dict) and bool(node.get("id"))


def _passes_record_filters(
    node: dict[str, Any], *, wanted_ids: set[str] | None, since: str | None
) -> bool:
    """Return whether a counted node also passes the id/since selection filters."""
    if wanted_ids is not None and str(node["id"]) not in wanted_ids:
        return False
    if since and str(node.get("updatedAt") or "") <= since:
        return False
    return True


class LeanixSourceAdapter:
    """Authenticated source adapter with bounded cursor pagination."""

    def __init__(self, api_client: Any, graphql_client: Any, *, page_size: int = 500):
        if not 1 <= page_size <= 1_000:
            raise ValueError("page_size must be between 1 and 1000")
        self.api_client = api_client
        self.graphql_client = graphql_client
        self.page_size = page_size
        self._meta_model: dict[str, Any] | None = None
        self._expected_by_type: dict[str, int] = {}
        self._seen_by_type: dict[str, int] = {}
        self.partial_graphql_pages = 0
        self.minimal_fallback_pages = 0

    def meta_model(self, *, refresh: bool = False) -> dict[str, Any]:
        """Return the live current data model, cached for this synchronization."""
        if self._meta_model is None or refresh:
            self._meta_model = discover_meta_model(self.api_client)
        return self._meta_model

    def _schema_type(self, fact_sheet_type: str) -> Any:
        """Return the live GraphQL type definition for one FactSheet type."""
        schema = getattr(getattr(self.graphql_client, "client", None), "schema", None)
        if schema is None:
            schema = self.graphql_client.ensure_schema()
        gql_type = schema.get_type(fact_sheet_type)
        if gql_type is None:
            raise RuntimeError("LeanIX GraphQL schema is missing a data-model type")
        return gql_type

    def _selection(self, fact_sheet_type: str) -> tuple[list[str], list[str]]:
        if not _GRAPHQL_NAME.fullmatch(fact_sheet_type):
            raise ValueError("FactSheet type is not a valid GraphQL name")
        definition = _definitions(self.meta_model()).get(fact_sheet_type)
        if definition is None:
            raise ValueError("FactSheet type is not present in the live data model")
        relations = _relation_names(definition)
        gql_type = self._schema_type(fact_sheet_type)
        fields = getattr(gql_type, "fields", {})
        if len(fields) > _MAX_FIELDS_PER_TYPE:
            raise RuntimeError("LeanIX field selection exceeds the safety limit")
        return _scalar_data_fields(fields), relations

    def _query_for_type(self, fact_sheet_type: str, *, minimal: bool = False) -> str:
        fragment = ""
        if not minimal:
            scalar_fields, relations = self._selection(fact_sheet_type)
            relation_fields = " ".join(
                f"{name}{{edges{{node{{factSheet{{id type}}}}}}}}" for name in relations
            )
            fragment_fields = " ".join([*scalar_fields, relation_fields]).strip()
            fragment = (
                f"... on {fact_sheet_type}{{{fragment_fields}}}"
                if fragment_fields
                else ""
            )
        query = (
            "query LeanixInstanceSync($first:Int!,$after:String,$filter:FilterInput){"
            "allFactSheets(first:$first,after:$after,filter:$filter){"
            "totalCount pageInfo{hasNextPage endCursor} "
            "edges{node{id name type updatedAt " + fragment + "}}}}"
        )
        if len(query.encode("utf-8")) > _MAX_QUERY_BYTES:
            raise RuntimeError("Generated LeanIX query exceeds the safety limit")
        return query

    def _execute_page(self, query: str, *, variables: dict[str, Any]) -> dict[str, Any]:
        """Execute one page and request partial data when the client supports it."""
        execute = self.graphql_client.execute_gql
        try:
            parameters = inspect.signature(execute).parameters.values()
            supports_partial = any(
                parameter.kind == inspect.Parameter.VAR_KEYWORD
                or parameter.name == "allow_partial"
                for parameter in parameters
            )
        except (TypeError, ValueError):
            supports_partial = True
        if supports_partial:
            data = execute(query, variables=variables, allow_partial=True)
        else:  # adapter compatibility for a bounded injected source test double
            data = execute(query, variables=variables)
        if int(getattr(self.graphql_client, "last_partial_error_count", 0) or 0):
            self.partial_graphql_pages += 1
        if not isinstance(data, dict):
            raise RuntimeError("LeanIX GraphQL returned an invalid response")
        return data

    def _fetch_connection(
        self, query: str, minimal_query: str, variables: dict[str, Any]
    ) -> dict[str, Any]:
        """Execute one page, falling back to the minimal query, and return its connection."""
        try:
            data = self._execute_page(query, variables=variables)
        except Exception:
            if query == minimal_query:
                raise
            self.minimal_fallback_pages += 1
            data = self._execute_page(minimal_query, variables=variables)
        connection = data.get("allFactSheets") if isinstance(data, dict) else None
        if not isinstance(connection, dict) and query != minimal_query:
            self.minimal_fallback_pages += 1
            data = self._execute_page(minimal_query, variables=variables)
            connection = data.get("allFactSheets")
        if not isinstance(connection, dict):
            raise RuntimeError("LeanIX GraphQL returned no FactSheet connection")
        return connection

    def _checked_total_count(
        self, fact_sheet_type: str, connection: dict[str, Any]
    ) -> int:
        """Validate and reconcile one page's totalCount against prior pages."""
        total_count = connection.get("totalCount")
        if (
            isinstance(total_count, bool)
            or not isinstance(total_count, int)
            or not 0 <= total_count <= _MAX_RECORDS_PER_TYPE
        ):
            raise RuntimeError("LeanIX GraphQL returned an invalid totalCount")
        expected = self._expected_by_type.setdefault(fact_sheet_type, total_count)
        if expected != total_count:
            raise RuntimeError("LeanIX totalCount changed during pagination")
        return total_count

    def _page_edges(self, connection: dict[str, Any]) -> list[Any]:
        """Return one page's edge list, bounded to the configured page size."""
        edges = connection.get("edges") or []
        if not isinstance(edges, list) or len(edges) > self.page_size:
            raise RuntimeError("LeanIX GraphQL returned an invalid page")
        return edges

    def _iter_page_nodes(
        self,
        fact_sheet_type: str,
        edges: list[Any],
        *,
        wanted_ids: set[str] | None,
        since: str | None,
        seen_records: int,
    ) -> Iterator[tuple[dict[str, Any], int]]:
        """Yield each accepted node from one page alongside the running seen count."""
        for edge in edges:
            node = edge.get("node") if isinstance(edge, dict) else None
            if not _has_usable_id(node):
                continue
            seen_records += 1
            if seen_records > _MAX_RECORDS_PER_TYPE:
                raise RuntimeError("LeanIX record count exceeds the safety limit")
            if not _passes_record_filters(node, wanted_ids=wanted_ids, since=since):
                continue
            node.setdefault("type", fact_sheet_type)
            self._seen_by_type[fact_sheet_type] = (
                self._seen_by_type.get(fact_sheet_type, 0) + 1
            )
            yield node, seen_records

    def _checked_next_cursor(
        self, page: dict[str, Any], seen_cursors: set[str]
    ) -> str | None:
        """Return the next page cursor, or None when pagination is finished."""
        if not page.get("hasNextPage"):
            return None
        cursor = page.get("endCursor")
        if (
            not isinstance(cursor, str)
            or not cursor
            or len(cursor.encode("utf-8")) > _MAX_CURSOR_BYTES
            or cursor in seen_cursors
        ):
            raise RuntimeError("LeanIX returned an invalid pagination cursor")
        return cursor

    def _checked_page_cursor(
        self, connection: dict[str, Any], seen_cursors: set[str]
    ) -> str | None:
        """Validate one page's pageInfo shape and return its next cursor, if any."""
        page = connection.get("pageInfo") or {}
        if not isinstance(page, dict):
            raise RuntimeError("LeanIX GraphQL returned invalid pageInfo")
        return self._checked_next_cursor(page, seen_cursors)

    def iter_factsheets(
        self,
        fact_sheet_type: str,
        *,
        since: str | None = None,
        ids: list[str] | None = None,
    ) -> Iterator[dict[str, Any]]:
        """Yield matching records while retaining only one upstream page."""
        if ids is not None and len(ids) > _MAX_IDS_FILTER:
            raise ValueError("ids exceeds the bounded webhook filter limit")
        wanted_ids = set(ids or []) or None
        variables: dict[str, Any] = {
            "first": self.page_size,
            "after": None,
            "filter": {
                "facetFilters": [
                    {"facetKey": "FactSheetTypes", "keys": [fact_sheet_type]}
                ]
            },
        }
        query = self._query_for_type(fact_sheet_type)
        minimal_query = self._query_for_type(fact_sheet_type, minimal=True)
        seen_cursors: set[str] = set()
        seen_records = 0
        for _page_number in range(_MAX_PAGES_PER_TYPE):
            connection = self._fetch_connection(query, minimal_query, variables)
            self._checked_total_count(fact_sheet_type, connection)
            edges = self._page_edges(connection)
            for node, seen_records in self._iter_page_nodes(
                fact_sheet_type,
                edges,
                wanted_ids=wanted_ids,
                since=since,
                seen_records=seen_records,
            ):
                yield node
            cursor = self._checked_page_cursor(connection, seen_cursors)
            if cursor is None:
                return
            seen_cursors.add(cursor)
            variables["after"] = cursor
        raise RuntimeError("LeanIX pagination exceeded the page safety limit")

    def factsheets(
        self,
        type: str,  # noqa: A002 - source adapter protocol
        *,
        since: str | None = None,
        ids: list[str] | None = None,
    ) -> list[dict[str, Any]]:
        """Return a bounded type slice for adapter consumers."""
        return list(self.iter_factsheets(type, since=since, ids=ids))

    def _fetch_id_connection(
        self, query: str, variables: dict[str, Any]
    ) -> dict[str, Any]:
        """Execute one id-sync page and return its validated connection."""
        data = self._execute_page(query, variables=variables)
        connection = data.get("allFactSheets") if isinstance(data, dict) else None
        if not isinstance(connection, dict):
            raise RuntimeError("LeanIX GraphQL returned no FactSheet connection")
        return connection

    def _add_live_ids(self, connection: dict[str, Any], live_ids: set[str]) -> None:
        """Add every valid node id from one page's edges into the live-id set."""
        edges = connection.get("edges") or []
        if not isinstance(edges, list) or len(edges) > self.page_size:
            raise RuntimeError("LeanIX GraphQL returned an invalid ID page")
        for edge in edges:
            node = edge.get("node") if isinstance(edge, dict) else None
            if isinstance(node, dict) and node.get("id"):
                live_ids.add(str(node["id"]))
                if len(live_ids) > _MAX_RECORDS_PER_TYPE:
                    raise RuntimeError("LeanIX live-id set exceeds the safety limit")

    def fact_sheet_ids(self) -> set[str]:
        """Read the authoritative live-id set for a reconcile marker."""
        query = (
            "query LeanixIdSync($first:Int!,$after:String){"
            "allFactSheets(first:$first,after:$after){"
            "pageInfo{hasNextPage endCursor} edges{node{id}}}}"
        )
        variables: dict[str, Any] = {"first": self.page_size, "after": None}
        live_ids: set[str] = set()
        seen_cursors: set[str] = set()
        for _page_number in range(_MAX_PAGES_PER_TYPE):
            connection = self._fetch_id_connection(query, variables)
            self._add_live_ids(connection, live_ids)
            page = connection.get("pageInfo") or {}
            cursor = self._checked_next_cursor(page, seen_cursors)
            if cursor is None:
                return live_ids
            seen_cursors.add(cursor)
            variables["after"] = cursor
        raise RuntimeError("LeanIX pagination exceeded the page safety limit")

    def expected_records(self) -> int:
        """Return authoritative per-type totals for a full run."""
        return sum(self._expected_by_type.values())


def _iter_dict_targets(value: dict[str, Any]) -> Iterable[tuple[str, str | None]]:
    """Yield targets nested inside one FactSheet-relation dict shape."""
    if isinstance(value.get("edges"), list):
        yield from _iter_targets(value["edges"])
        return
    if "node" in value:
        yield from _iter_targets(value["node"])
        return
    for nested_key in ("factSheet", "target"):
        if isinstance(value.get(nested_key), dict):
            yield from _iter_targets(value[nested_key])
            return
    target_id = value.get("factSheetId") or value.get("targetId") or value.get("id")
    if target_id:
        yield str(target_id), value.get("type")


def _iter_targets(value: Any) -> Iterable[tuple[str, str | None]]:
    if value is None:
        return
    if isinstance(value, str):
        yield value, None
        return
    if isinstance(value, list):
        for item in value:
            yield from _iter_targets(item)
        return
    if not isinstance(value, dict):
        return
    yield from _iter_dict_targets(value)


def _iter_tags(value: Any) -> Iterable[dict[str, Any]]:
    if isinstance(value, list):
        for item in value:
            yield from _iter_tags(item)
    elif isinstance(value, dict):
        if isinstance(value.get("edges"), list):
            for edge in value["edges"]:
                yield from _iter_tags(edge)
        elif isinstance(value.get("node"), dict):
            yield from _iter_tags(value["node"])
        elif value.get("id") or value.get("name"):
            yield value


def _private_id(kind: str, value: Any, source_instance: str) -> str:
    return persistence_reference(kind, value, namespace=source_instance or "leanix")


def _privacy_safe_property(name: str) -> bool:
    clean, report = PersistencePrivacyGuard().sanitize({name: "present"})
    return not report.changed and clean.get(name) == "present"


def _sanitized_source_properties(clean: dict[str, Any]) -> dict[str, Any]:
    """Return privacy-safe, non-reserved scalar properties for one clean record."""
    return {
        name: value
        for name, value in clean.items()
        if isinstance(name, str)
        and name not in {"id", "name", "type", "tags"}
        and not name.startswith("rel")
        and _privacy_safe_property(name)
    }


def _tag_nodes_and_links(
    record: dict[str, Any],
    node_id: str,
    artifact: InstanceOntology,
    source_instance: str,
) -> tuple[list[dict[str, Any]], list[dict[str, Any]]]:
    """Return the deduplicated taxonomy nodes and TAGGED_WITH links for one record."""
    auxiliary: list[dict[str, Any]] = []
    links: list[dict[str, Any]] = []
    seen_tags: set[str] = set()
    for tag in _iter_tags(record.get("tags")):
        tag_key = str(tag.get("id") or tag.get("name") or "")
        if not tag_key:
            continue
        tag_id = _private_id("leanix_tag", tag_key, source_instance)
        if tag_id not in seen_tags:
            seen_tags.add(tag_id)
            auxiliary.append(
                {
                    "id": tag_id,
                    "node_type": "TaxonomyConcept",
                    "domain": "leanix-taxonomy",
                    "metamodelDigest": artifact.schema_digest,
                }
            )
        links.append(
            {"source": node_id, "target": tag_id, "relationship": "TAGGED_WITH"}
        )
    return auxiliary, links


def _relation_links(
    record: dict[str, Any],
    node_id: str,
    artifact: InstanceOntology,
    source_instance: str,
) -> list[dict[str, Any]]:
    """Return the typed edges for every ``rel*`` field on one record."""
    links: list[dict[str, Any]] = []
    for field_name, value in record.items():
        if not isinstance(field_name, str) or not field_name.startswith("rel"):
            continue
        relation_type, declared_target = artifact.relation_map.get(
            field_name, (field_name, "")
        )
        for target_id, observed_type in _iter_targets(value):
            target_type = str(observed_type or declared_target or "FactSheet")
            if _PERSON_TYPE.search(target_type):
                continue
            links.append(
                {
                    "source": node_id,
                    "target": _private_id("leanix_object", target_id, source_instance),
                    "relationship": relation_type,
                }
            )
    return links


def _prepare_record(
    record: dict[str, Any],
    artifact: InstanceOntology,
    *,
    source_instance: str,
) -> tuple[dict[str, Any] | None, int, int, int]:
    """Prepare one sanitized entity and its atomic auxiliary graph material."""
    raw_id = str(record.get("id") or "")
    fact_sheet_type = str(record.get("type") or "FactSheet")
    if not raw_id:
        return None, 0, 0, 0
    if _PERSON_TYPE.search(fact_sheet_type):
        return None, 0, 0, 1
    clean, privacy = PersistencePrivacyGuard().sanitize(record)
    if not isinstance(clean, dict):
        raise RuntimeError("LeanIX record failed the persistence privacy gate")
    node_id = _private_id("leanix_object", raw_id, source_instance)
    mapped_type = artifact.type_map.get(
        fact_sheet_type, (fact_sheet_type, fact_sheet_type.lower())
    )[0]
    entity: dict[str, Any] = {
        "id": node_id,
        "node_type": mapped_type,
        "name": clean.get("name"),
        "externalToolId": node_id,
        "updatedAt": clean.get("updatedAt"),
        "domain": "leanix",
        "metamodelDigest": artifact.schema_digest,
        "sourceProperties": _sanitized_source_properties(clean),
    }
    auxiliary, tag_links = _tag_nodes_and_links(
        record, node_id, artifact, source_instance
    )
    links = tag_links + _relation_links(record, node_id, artifact, source_instance)
    if auxiliary:
        entity["_nodes"] = auxiliary
    if links:
        entity["_links"] = links
    return entity, len(auxiliary) + 1, len(links), privacy.redactions


def _result_ok(result: dict[str, Any]) -> bool:
    return str(result.get("status", "")).lower() in {"success", "skipped"}


def _failure_report(
    *,
    mode: str,
    artifact: InstanceOntology,
    ontology_result: dict[str, Any],
    reason: str,
    factsheets_seen: int,
    payload_nodes: int,
    payload_relations: int,
    payload_batches: int,
    expected_factsheets: int | None,
    privacy_redactions: int,
    personal_records_skipped: int,
    partial_graphql_pages: int = 0,
    minimal_fallback_pages: int = 0,
) -> InstanceSyncReport:
    return InstanceSyncReport(
        status="failed",
        mode=mode,
        schema_digest=artifact.schema_digest,
        ontology=ontology_result,
        source_sync={"status": "failed", "reason": reason},
        factsheets_seen=factsheets_seen,
        payload_nodes=payload_nodes,
        payload_relations=payload_relations,
        payload_batches=payload_batches,
        expected_factsheets=expected_factsheets,
        privacy_redactions=privacy_redactions,
        personal_records_skipped=personal_records_skipped,
        partial_graphql_pages=partial_graphql_pages,
        minimal_fallback_pages=minimal_fallback_pages,
        complete=False,
    )


def _source_instance_reference(
    api_client: Any,
    graphql_client: Any,
    *,
    requested: str | None,
) -> str:
    """Return an opaque stable source identity without persisting its endpoint."""
    source = (
        requested
        or getattr(graphql_client, "url", None)
        or getattr(api_client, "base_url", None)
        or "configured-leanix-source"
    )
    return persistence_reference("leanix_source", source, namespace="leanix")


def _cleaned_retention(retention: str | None) -> str | None:
    """Return a privacy-safe, size-bounded retention reference, or None."""
    if retention is None:
        return None
    retention = str(retention).strip() or None
    if retention is None:
        return None
    clean_retention, retention_report = PersistencePrivacyGuard().sanitize_text(
        retention
    )
    if (
        retention_report.changed
        or clean_retention != retention
        or len(retention.encode("utf-8")) > 256
    ):
        raise ValueError("retention policy reference is invalid")
    return retention


@dataclass
class _SyncAuthority:
    """Session-scoped write authority and run parameters shared by every commit."""

    engine: Any
    resolved_session: Any
    source_instance: str
    retention: str | None
    mode: str


def _reconcile_sync(
    adapter: LeanixSourceAdapter,
    artifact: InstanceOntology,
    ontology_result: dict[str, Any],
    cursor: str | None,
    authority: _SyncAuthority,
) -> InstanceSyncReport:
    """Commit one native snapshot-complete marker of the live FactSheet id set."""
    from agent_utilities.knowledge_graph.ingestion.change_envelope import (
        ChangeEnvelope,
    )
    from agent_utilities.knowledge_graph.ingestion.envelope_ingest import (
        ingest_envelope,
    )

    raw_ids = adapter.fact_sheet_ids()
    live_ids = {
        _private_id("leanix_object", value, authority.source_instance)
        for value in raw_ids
    }
    snapshot_digest = hashlib.sha256(
        json.dumps(sorted(live_ids), separators=(",", ":")).encode("utf-8")
    ).hexdigest()
    envelope = ChangeEnvelope.snapshot_complete(
        connector="leanix",
        tenant=authority.resolved_session.tenant,
        source_instance=authority.source_instance,
        checkpoint=cursor,
        live_ids=live_ids,
        source_version=snapshot_digest,
        retention=authority.retention,
        ontology_mapping_version=artifact.schema_digest,
        provenance={
            "generated_by": "leanix-agent",
            "metamodel_digest": artifact.schema_digest,
        },
    )
    result = ingest_envelope(authority.engine, envelope)
    status = "ok" if _result_ok(result) else "failed"
    return InstanceSyncReport(
        status=status,
        mode=authority.mode,
        schema_digest=artifact.schema_digest,
        ontology=ontology_result,
        source_sync=result,
        factsheets_seen=len(raw_ids),
        payload_nodes=0,
        payload_relations=0,
        payload_batches=1,
        expected_factsheets=len(raw_ids),
        partial_graphql_pages=adapter.partial_graphql_pages,
        minimal_fallback_pages=adapter.minimal_fallback_pages,
        complete=status == "ok",
    )


@dataclass
class _IncrementalSyncState:
    """Mutable running totals for one incremental (full/delta) sync pass."""

    factsheets_seen: int = 0
    payload_nodes: int = 0
    payload_relations: int = 0
    payload_batches: int = 0
    privacy_redactions: int = 0
    personal_records_skipped: int = 0
    max_checkpoint: str | None = None
    pending: dict[str, Any] | None = None
    pending_counts: tuple[int, int] = (0, 0)


@dataclass
class _IncrementalSyncContext:
    """Immutable context shared across every staged record in one sync pass."""

    artifact: InstanceOntology
    ontology_result: dict[str, Any]
    adapter: LeanixSourceAdapter
    authority: _SyncAuthority


def _commit_record(
    context: _IncrementalSyncContext, record: dict[str, Any], checkpoint: str | None
) -> dict[str, Any]:
    """Commit one prepared record as a native ChangeEnvelope."""
    from agent_utilities.knowledge_graph.ingestion.change_envelope import (
        ChangeEnvelope,
    )
    from agent_utilities.knowledge_graph.ingestion.envelope_ingest import (
        ingest_envelope,
    )

    envelope = ChangeEnvelope.from_connector_record(
        record,
        connector="leanix",
        tenant=context.authority.resolved_session.tenant,
        source_instance=context.authority.source_instance,
        id_field="id",
        version_field="updatedAt",
        checkpoint=checkpoint,
        retention=context.authority.retention,
        ontology_mapping_version=context.artifact.schema_digest,
        session=context.authority.resolved_session,
        provenance={
            "generated_by": "leanix-agent",
            "metamodel_digest": context.artifact.schema_digest,
        },
    )
    return ingest_envelope(context.authority.engine, envelope)


def _incremental_failure_report(
    state: _IncrementalSyncState,
    context: _IncrementalSyncContext,
    *,
    reason: str,
    expected_factsheets: int | None,
) -> InstanceSyncReport:
    """Build a failure report from the current incremental sync state."""
    return _failure_report(
        mode=context.authority.mode,
        artifact=context.artifact,
        ontology_result=context.ontology_result,
        reason=reason,
        factsheets_seen=state.factsheets_seen,
        payload_nodes=state.payload_nodes,
        payload_relations=state.payload_relations,
        payload_batches=state.payload_batches,
        expected_factsheets=expected_factsheets,
        privacy_redactions=state.privacy_redactions,
        personal_records_skipped=state.personal_records_skipped,
        partial_graphql_pages=context.adapter.partial_graphql_pages,
        minimal_fallback_pages=context.adapter.minimal_fallback_pages,
    )


def _stage_record(
    state: _IncrementalSyncState,
    context: _IncrementalSyncContext,
    raw_record: dict[str, Any],
) -> InstanceSyncReport | None:
    """Prepare and stage one record, committing the previously staged one.

    Returns a failure report when the previously staged commit fails; the
    final staged record is only committed once the whole pass completes.
    """
    state.factsheets_seen += 1
    updated_at = str(raw_record.get("updatedAt") or "")
    if updated_at and (
        state.max_checkpoint is None or updated_at > state.max_checkpoint
    ):
        state.max_checkpoint = updated_at
    prepared, nodes, relations, redactions = _prepare_record(
        raw_record, context.artifact, source_instance=context.authority.source_instance
    )
    state.privacy_redactions += redactions
    if prepared is None:
        state.personal_records_skipped += 1
        return None
    if state.pending is not None:
        result = _commit_record(context, state.pending, None)
        state.payload_batches += 1
        if not _result_ok(result):
            return _incremental_failure_report(
                state,
                context,
                reason="native ChangeEnvelope commit failed",
                expected_factsheets=None,
            )
        state.payload_nodes += state.pending_counts[0]
        state.payload_relations += state.pending_counts[1]
    state.pending = prepared
    state.pending_counts = (nodes, relations)
    return None


def _stage_all_records(
    state: _IncrementalSyncState,
    context: _IncrementalSyncContext,
    since: str | None,
    ids: list[str] | None,
) -> InstanceSyncReport | None:
    """Stage every discovered fact-sheet record, or return an early failure."""
    for fact_sheet_type in sorted(_definitions(context.adapter.meta_model())):
        for raw_record in context.adapter.iter_factsheets(
            fact_sheet_type, since=since, ids=ids
        ):
            failure = _stage_record(state, context, raw_record)
            if failure is not None:
                return failure
    return None


def _finalize_incremental_sync(
    state: _IncrementalSyncState,
    context: _IncrementalSyncContext,
    ids: list[str] | None,
) -> InstanceSyncReport:
    """Verify the full-sync count (if applicable), commit the tail record, and report."""
    expected_factsheets = (
        context.adapter.expected_records()
        if context.authority.mode == "full" and ids is None
        else None
    )
    if expected_factsheets is not None and state.factsheets_seen != expected_factsheets:
        return _incremental_failure_report(
            state,
            context,
            reason="LeanIX full-sync count verification failed",
            expected_factsheets=expected_factsheets,
        )
    final_result: dict[str, Any] = {
        "status": "skipped",
        "reason": "no privacy-safe changes",
        "native_atomic": True,
    }
    if state.pending is not None:
        final_result = _commit_record(context, state.pending, state.max_checkpoint)
        state.payload_batches += 1
        if not _result_ok(final_result):
            return _incremental_failure_report(
                state,
                context,
                reason="native ChangeEnvelope commit failed",
                expected_factsheets=expected_factsheets,
            )
        state.payload_nodes += state.pending_counts[0]
        state.payload_relations += state.pending_counts[1]

    return InstanceSyncReport(
        status="ok",
        mode=context.authority.mode,
        schema_digest=context.artifact.schema_digest,
        ontology=context.ontology_result,
        source_sync=final_result,
        factsheets_seen=state.factsheets_seen,
        payload_nodes=state.payload_nodes,
        payload_relations=state.payload_relations,
        payload_batches=state.payload_batches,
        expected_factsheets=expected_factsheets,
        privacy_redactions=state.privacy_redactions,
        personal_records_skipped=state.personal_records_skipped,
        partial_graphql_pages=context.adapter.partial_graphql_pages,
        minimal_fallback_pages=context.adapter.minimal_fallback_pages,
        complete=True,
    )


def _incremental_sync(
    adapter: LeanixSourceAdapter,
    artifact: InstanceOntology,
    ontology_result: dict[str, Any],
    cursor: str | None,
    authority: _SyncAuthority,
    ids: list[str] | None,
) -> InstanceSyncReport:
    """Stream every full/delta record through the staggered-commit pattern."""
    since = None if authority.mode == "full" else cursor
    context = _IncrementalSyncContext(
        artifact=artifact,
        ontology_result=ontology_result,
        adapter=adapter,
        authority=authority,
    )
    state = _IncrementalSyncState(max_checkpoint=cursor)
    failure = _stage_all_records(state, context, since, ids)
    if failure is not None:
        return failure
    return _finalize_incremental_sync(state, context, ids)


def sync_instance(
    api_client: Any,
    graphql_client: Any,
    *,
    mode: str = "full",
    ids: list[str] | None = None,
    engine: Any = None,
    session: Any = None,
    page_size: int = 500,
    source_instance: str | None = None,
    retention: str | None = None,
) -> InstanceSyncReport:
    """Compile the live ontology and stream records under verified authority."""
    if mode not in {"full", "delta", "reconcile"}:
        raise ValueError("mode must be full, delta, or reconcile")
    if ids is not None and len(ids) > _MAX_IDS_FILTER:
        raise ValueError("ids exceeds the bounded webhook filter limit")
    from agent_utilities.knowledge_graph.core.session import resolve_session
    from agent_utilities.knowledge_graph.ingestion.envelope_ingest import (
        read_change_cursor,
    )
    from agent_utilities.knowledge_graph.ontology.connector_manifest_gate import (
        precheck_source,
    )

    resolved_session = resolve_session(session, required_scope="kg:write")
    if engine is None:
        from agent_utilities.knowledge_graph.memory.native_ingest import (
            native_authority,
        )

        engine = native_authority()

    gate = precheck_source("leanix")
    if not gate.get("checked") or not gate.get("ok"):
        raise RuntimeError("LeanIX connector manifest precheck failed")

    source_instance = _source_instance_reference(
        api_client,
        graphql_client,
        requested=source_instance,
    )
    retention = _cleaned_retention(retention)
    adapter = LeanixSourceAdapter(api_client, graphql_client, page_size=page_size)
    artifact = compile_instance_ontology(adapter.meta_model())
    ontology_result = load_instance_ontology(artifact, engine)
    if ontology_result.get("status") != "ok":
        raise RuntimeError("Generated LeanIX ontology was rejected")

    cursor = read_change_cursor(engine, "leanix", source_instance=source_instance)
    authority = _SyncAuthority(
        engine=engine,
        resolved_session=resolved_session,
        source_instance=source_instance,
        retention=retention,
        mode=mode,
    )
    if mode == "reconcile":
        return _reconcile_sync(adapter, artifact, ontology_result, cursor, authority)
    return _incremental_sync(adapter, artifact, ontology_result, cursor, authority, ids)
