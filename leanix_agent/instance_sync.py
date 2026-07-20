"""Bounded, privacy-safe LeanIX synchronization through ChangeEnvelope."""

from __future__ import annotations

import hashlib
import inspect
import json
import re
from collections.abc import Iterable, Iterator
from typing import Any

from agent_utilities.security.persistence_privacy import (
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
    from graphql import (
        is_enum_type,
        is_interface_type,
        is_object_type,
        is_scalar_type,
        is_union_type,
    )

    named = _named_graphql_type(field.type)
    if is_scalar_type(named) or is_enum_type(named):
        return name
    type_name = str(getattr(named, "name", ""))
    if not _GRAPHQL_NAME.fullmatch(type_name):
        return None
    if is_union_type(named):
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
    if not (is_object_type(named) or is_interface_type(named)):
        return None
    if type_name in seen:
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

    def _selection(self, fact_sheet_type: str) -> tuple[list[str], list[str]]:
        if not _GRAPHQL_NAME.fullmatch(fact_sheet_type):
            raise ValueError("FactSheet type is not a valid GraphQL name")
        definition = _definitions(self.meta_model()).get(fact_sheet_type)
        if definition is None:
            raise ValueError("FactSheet type is not present in the live data model")
        relations = _relation_names(definition)
        schema = getattr(getattr(self.graphql_client, "client", None), "schema", None)
        if schema is None:
            schema = self.graphql_client.ensure_schema()
        gql_type = schema.get_type(fact_sheet_type)
        if gql_type is None:
            raise RuntimeError("LeanIX GraphQL schema is missing a data-model type")
        fields = getattr(gql_type, "fields", {})
        if len(fields) > _MAX_FIELDS_PER_TYPE:
            raise RuntimeError("LeanIX field selection exceeds the safety limit")
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
        return data_fields, relations

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
            edges = connection.get("edges") or []
            if not isinstance(edges, list) or len(edges) > self.page_size:
                raise RuntimeError("LeanIX GraphQL returned an invalid page")
            for edge in edges:
                node = edge.get("node") if isinstance(edge, dict) else None
                if not isinstance(node, dict) or not node.get("id"):
                    continue
                seen_records += 1
                if seen_records > _MAX_RECORDS_PER_TYPE:
                    raise RuntimeError("LeanIX record count exceeds the safety limit")
                if wanted_ids is not None and str(node["id"]) not in wanted_ids:
                    continue
                if since and str(node.get("updatedAt") or "") <= since:
                    continue
                node.setdefault("type", fact_sheet_type)
                self._seen_by_type[fact_sheet_type] = (
                    self._seen_by_type.get(fact_sheet_type, 0) + 1
                )
                yield node
            page = connection.get("pageInfo") or {}
            if not isinstance(page, dict):
                raise RuntimeError("LeanIX GraphQL returned invalid pageInfo")
            if not page.get("hasNextPage"):
                return
            cursor = page.get("endCursor")
            if (
                not isinstance(cursor, str)
                or not cursor
                or len(cursor.encode("utf-8")) > _MAX_CURSOR_BYTES
                or cursor in seen_cursors
            ):
                raise RuntimeError("LeanIX returned an invalid pagination cursor")
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
            data = self._execute_page(query, variables=variables)
            connection = data.get("allFactSheets") if isinstance(data, dict) else None
            if not isinstance(connection, dict):
                raise RuntimeError("LeanIX GraphQL returned no FactSheet connection")
            edges = connection.get("edges") or []
            if not isinstance(edges, list) or len(edges) > self.page_size:
                raise RuntimeError("LeanIX GraphQL returned an invalid ID page")
            for edge in edges:
                node = edge.get("node") if isinstance(edge, dict) else None
                if isinstance(node, dict) and node.get("id"):
                    live_ids.add(str(node["id"]))
                    if len(live_ids) > _MAX_RECORDS_PER_TYPE:
                        raise RuntimeError(
                            "LeanIX live-id set exceeds the safety limit"
                        )
            page = connection.get("pageInfo") or {}
            if not page.get("hasNextPage"):
                return live_ids
            cursor = page.get("endCursor")
            if (
                not isinstance(cursor, str)
                or not cursor
                or len(cursor.encode("utf-8")) > _MAX_CURSOR_BYTES
                or cursor in seen_cursors
            ):
                raise RuntimeError("LeanIX returned an invalid pagination cursor")
            seen_cursors.add(cursor)
            variables["after"] = cursor
        raise RuntimeError("LeanIX pagination exceeded the page safety limit")

    def expected_records(self) -> int:
        """Return authoritative per-type totals for a full run."""
        return sum(self._expected_by_type.values())


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
    properties = {
        name: value
        for name, value in clean.items()
        if isinstance(name, str)
        and name not in {"id", "name", "type", "tags"}
        and not name.startswith("rel")
        and _privacy_safe_property(name)
    }
    entity: dict[str, Any] = {
        "id": node_id,
        "node_type": mapped_type,
        "name": clean.get("name"),
        "externalToolId": node_id,
        "updatedAt": clean.get("updatedAt"),
        "domain": "leanix",
        "metamodelDigest": artifact.schema_digest,
        "sourceProperties": properties,
    }
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
    from agent_utilities.knowledge_graph.ingestion.change_envelope import (
        ChangeEnvelope,
    )
    from agent_utilities.knowledge_graph.ingestion.envelope_ingest import (
        ingest_envelope,
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
    if retention is not None:
        retention = str(retention).strip() or None
        if retention is not None:
            clean_retention, retention_report = PersistencePrivacyGuard().sanitize_text(
                retention
            )
            if (
                retention_report.changed
                or clean_retention != retention
                or len(retention.encode("utf-8")) > 256
            ):
                raise ValueError("retention policy reference is invalid")
    adapter = LeanixSourceAdapter(api_client, graphql_client, page_size=page_size)
    artifact = compile_instance_ontology(adapter.meta_model())
    ontology_result = load_instance_ontology(artifact, engine)
    if ontology_result.get("status") != "ok":
        raise RuntimeError("Generated LeanIX ontology was rejected")

    cursor = read_change_cursor(engine, "leanix", source_instance=source_instance)
    if mode == "reconcile":
        raw_ids = adapter.fact_sheet_ids()
        live_ids = {
            _private_id("leanix_object", value, source_instance) for value in raw_ids
        }
        snapshot_digest = hashlib.sha256(
            json.dumps(sorted(live_ids), separators=(",", ":")).encode("utf-8")
        ).hexdigest()
        envelope = ChangeEnvelope.snapshot_complete(
            connector="leanix",
            tenant=resolved_session.tenant,
            source_instance=source_instance,
            checkpoint=cursor,
            live_ids=live_ids,
            source_version=snapshot_digest,
            retention=retention,
            ontology_mapping_version=artifact.schema_digest,
            provenance={
                "generated_by": "leanix-agent",
                "metamodel_digest": artifact.schema_digest,
            },
        )
        result = ingest_envelope(engine, envelope)
        status = "ok" if _result_ok(result) else "failed"
        return InstanceSyncReport(
            status=status,
            mode=mode,
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

    since = None if mode == "full" else cursor
    factsheets_seen = 0
    payload_nodes = 0
    payload_relations = 0
    payload_batches = 0
    privacy_redactions = 0
    personal_records_skipped = 0
    max_checkpoint = cursor
    pending: dict[str, Any] | None = None
    pending_counts = (0, 0)

    def commit(record: dict[str, Any], checkpoint: str | None) -> dict[str, Any]:
        envelope = ChangeEnvelope.from_connector_record(
            record,
            connector="leanix",
            tenant=resolved_session.tenant,
            source_instance=source_instance,
            id_field="id",
            version_field="updatedAt",
            checkpoint=checkpoint,
            retention=retention,
            ontology_mapping_version=artifact.schema_digest,
            session=resolved_session,
            provenance={
                "generated_by": "leanix-agent",
                "metamodel_digest": artifact.schema_digest,
            },
        )
        return ingest_envelope(engine, envelope)

    for fact_sheet_type in sorted(_definitions(adapter.meta_model())):
        for raw_record in adapter.iter_factsheets(
            fact_sheet_type, since=since, ids=ids
        ):
            factsheets_seen += 1
            updated_at = str(raw_record.get("updatedAt") or "")
            if updated_at and (max_checkpoint is None or updated_at > max_checkpoint):
                max_checkpoint = updated_at
            prepared, nodes, relations, redactions = _prepare_record(
                raw_record, artifact, source_instance=source_instance
            )
            privacy_redactions += redactions
            if prepared is None:
                personal_records_skipped += 1
                continue
            if pending is not None:
                result = commit(pending, None)
                payload_batches += 1
                if not _result_ok(result):
                    return _failure_report(
                        mode=mode,
                        artifact=artifact,
                        ontology_result=ontology_result,
                        reason="native ChangeEnvelope commit failed",
                        factsheets_seen=factsheets_seen,
                        payload_nodes=payload_nodes,
                        payload_relations=payload_relations,
                        payload_batches=payload_batches,
                        expected_factsheets=None,
                        privacy_redactions=privacy_redactions,
                        personal_records_skipped=personal_records_skipped,
                        partial_graphql_pages=adapter.partial_graphql_pages,
                        minimal_fallback_pages=adapter.minimal_fallback_pages,
                    )
                payload_nodes += pending_counts[0]
                payload_relations += pending_counts[1]
            pending = prepared
            pending_counts = (nodes, relations)

    expected_factsheets = (
        adapter.expected_records() if mode == "full" and ids is None else None
    )
    if expected_factsheets is not None and factsheets_seen != expected_factsheets:
        return _failure_report(
            mode=mode,
            artifact=artifact,
            ontology_result=ontology_result,
            reason="LeanIX full-sync count verification failed",
            factsheets_seen=factsheets_seen,
            payload_nodes=payload_nodes,
            payload_relations=payload_relations,
            payload_batches=payload_batches,
            expected_factsheets=expected_factsheets,
            privacy_redactions=privacy_redactions,
            personal_records_skipped=personal_records_skipped,
            partial_graphql_pages=adapter.partial_graphql_pages,
            minimal_fallback_pages=adapter.minimal_fallback_pages,
        )
    final_result: dict[str, Any] = {
        "status": "skipped",
        "reason": "no privacy-safe changes",
        "native_atomic": True,
    }
    if pending is not None:
        final_result = commit(pending, max_checkpoint)
        payload_batches += 1
        if not _result_ok(final_result):
            return _failure_report(
                mode=mode,
                artifact=artifact,
                ontology_result=ontology_result,
                reason="native ChangeEnvelope commit failed",
                factsheets_seen=factsheets_seen,
                payload_nodes=payload_nodes,
                payload_relations=payload_relations,
                payload_batches=payload_batches,
                expected_factsheets=expected_factsheets,
                privacy_redactions=privacy_redactions,
                personal_records_skipped=personal_records_skipped,
                partial_graphql_pages=adapter.partial_graphql_pages,
                minimal_fallback_pages=adapter.minimal_fallback_pages,
            )
        payload_nodes += pending_counts[0]
        payload_relations += pending_counts[1]

    return InstanceSyncReport(
        status="ok",
        mode=mode,
        schema_digest=artifact.schema_digest,
        ontology=ontology_result,
        source_sync=final_result,
        factsheets_seen=factsheets_seen,
        payload_nodes=payload_nodes,
        payload_relations=payload_relations,
        payload_batches=payload_batches,
        expected_factsheets=expected_factsheets,
        privacy_redactions=privacy_redactions,
        personal_records_skipped=personal_records_skipped,
        partial_graphql_pages=adapter.partial_graphql_pages,
        minimal_fallback_pages=adapter.minimal_fallback_pages,
        complete=True,
    )
