# Code Enhancement: leanix-agent

> Automated code enhancement review for leanix-agent. Covers 17 analysis domains.

## User Stories

- As a **developer**, I want to **address Project Analysis findings (grade: C, score: 74)**, so that **improve project project analysis from C to at least B (80+)**.
- As a **developer**, I want to **address Codebase Optimization findings (grade: D, score: 68)**, so that **improve project codebase optimization from D to at least B (80+)**.
- As a **developer**, I want to **address Security Analysis findings (grade: C, score: 75)**, so that **improve project security analysis from C to at least B (80+)**.
- As a **developer**, I want to **address Test Coverage findings (grade: D, score: 65)**, so that **improve project test coverage from D to at least B (80+)**.
- As a **developer**, I want to **address Documentation & Governance findings (grade: C, score: 70)**, so that **improve project documentation & governance from C to at least B (80+)**.
- As a **developer**, I want to **address Architecture & Design Patterns findings (grade: D, score: 65)**, so that **improve project architecture & design patterns from D to at least B (80+)**.
- As a **developer**, I want to **address Concept Traceability findings (grade: F, score: 30)**, so that **improve project concept traceability from F to at least B (80+)**.
- As a **developer**, I want to **address Linting & Formatting findings (grade: F, score: 0)**, so that **improve project linting & formatting from F to at least B (80+)**.
- As a **developer**, I want to **address Test Execution findings (grade: F, score: 20)**, so that **improve project test execution from F to at least B (80+)**.
- As a **developer**, I want to **address Directory Organization findings (grade: C, score: 75)**, so that **improve project directory organization from C to at least B (80+)**.
- As a **developer**, I want to **address Changelog Audit findings (grade: C, score: 75)**, so that **improve project changelog audit from C to at least B (80+)**.
- As a **developer**, I want to **address Pytest Quality findings (grade: D, score: 64)**, so that **improve project pytest quality from D to at least B (80+)**.

## Functional Requirements

- **FR-001**: 2 functions exceed 200 lines (actionable refactoring targets): generate (250L), get_mcp_instance (245L)
- **FR-002**: Monolithic: mcp_server.py (516L) — 1 functions with high complexity (worst: get_mcp_instance at 245L, CC=34); Low cohesion: 10 distinct concepts in one file
- **FR-003**: Needs attention: reference_data_api.py (671L) — God class: Api (56 methods) — consider mixins/composition
- **FR-004**: Needs attention: pathfinder_api.py (779L) — God class: Api (71 methods) — consider mixins/composition
- **FR-005**: Needs attention: mtm_api.py (1595L) — God class: Api (155 methods) — consider mixins/composition
- **FR-006**: 7 functions with nesting depth >4
- **FR-007**: 1 flat directories with >15 Python files: leanix_agent
- **FR-008**: 1 HIGH severity vulnerabilities found
- **FR-009**: eval/exec usage detected: 1 instances
- **FR-010**: 6 tests without assertions
- **FR-011**: Test suite lacks intent diversity (only one type)
- **FR-012**: 16 potential doc-test drift items
- **FR-013**: README.md missing sections: installation, usage|quick start
- **FR-014**: README missing: MCP tools mapping table with descriptions
- **FR-015**: README missing: Has a Table of Contents
- **FR-016**: README missing: Has usage examples with code blocks
- **FR-017**: README missing: References /docs directory material
- **FR-018**: README missing: Has MCP tools mapping table with descriptions
- **FR-019**: SRP: 7 modules exceed 500 lines (god modules)
- **FR-020**: SRP: 20 classes have >15 methods
- **FR-021**: No discernible layer architecture (no domain/service/adapter separation)
- **FR-022**: 51 Python files at top level — consider package organization
- **FR-023**: Low traceability ratio: 0% concepts fully traced
- **FR-024**: 176 test functions missing concept markers
- **FR-025**: 524 significant functions (>10 lines) missing concept markers in docstrings
- **FR-026**: Total lint findings: 25 (high/error: 25, medium/warning: 0, low: 0)
- **FR-027**: 1 hook(s) may be outdated: ruff-pre-commit
- **FR-028**: 1 test execution error(s)
- **FR-029**: 1 directories with >40 files: leanix_agent
- **FR-030**: Monolithic directory: leanix_agent contains 60.0% of all files (42/70)
- **FR-031**: CHANGELOG.md is missing — create one following Keep a Changelog format
- **FR-032**: CHANGELOG.md is missing
- **FR-033**: 3 test files exceed 500 lines — split into focused modules
- **FR-034**: 2 test files have >30 tests — too dense
- **FR-035**: Test directory lacks subdirectory organization (consider unit/, integration/, e2e/)
- **FR-036**: No @pytest.mark.parametrize usage — consider data-driven tests
- **FR-037**: 6 tests have no assertions
- **FR-038**: 19 tests use weak assertions (assert result is not None, assert True, etc.)
- **FR-039**: Undocumented env vars: ALLOWED_CLIENT_REDIRECT_URIS, AUTH_TYPE, ENABLE_OTEL, EUNOMIA_POLICY_FILE, EUNOMIA_REMOTE_URL, EUNOMIA_TYPE, LEANIX_API_KEY, LLM_API_KEY, LLM_BASE_URL, OAUTH_BASE_URL
- **FR-040**: 37 Python env vars not in .env.example: DEFAULT_AGENT_NAME, GRAPHQLTOOL, LEANIX_AGENT_VERIFY, LEANIX_AI_INVENTORY_BUILDERTOOL, LEANIX_APPTIO_CONNECTORTOOL

## Success Criteria

- Overall GPA: 1.94 → 3.0
- Domains at B or above: 5 → 17
- Actionable findings: 40 → 0
