# Code Enhancement: leanix-agent

> Automated code enhancement review for leanix-agent. Covers 17 analysis domains.

## User Stories

- As a **developer**, I want to **address Project Analysis findings (grade: C, score: 74)**, so that **improve project project analysis from C to at least B (80+)**.
- As a **developer**, I want to **address Codebase Optimization findings (grade: C, score: 73)**, so that **improve project codebase optimization from C to at least B (80+)**.
- As a **developer**, I want to **address Test Coverage findings (grade: C, score: 75)**, so that **improve project test coverage from C to at least B (80+)**.
- As a **developer**, I want to **address Architecture & Design Patterns findings (grade: D, score: 65)**, so that **improve project architecture & design patterns from D to at least B (80+)**.
- As a **developer**, I want to **address Concept Traceability findings (grade: F, score: 24)**, so that **improve project concept traceability from F to at least B (80+)**.
- As a **developer**, I want to **address Test Execution findings (grade: F, score: 25)**, so that **improve project test execution from F to at least B (80+)**.
- As a **developer**, I want to **address Changelog Audit findings (grade: C, score: 75)**, so that **improve project changelog audit from C to at least B (80+)**.
- As a **developer**, I want to **address Pytest Quality findings (grade: C, score: 75)**, so that **improve project pytest quality from C to at least B (80+)**.
- As a **developer**, I want to **address Environment Variables findings (grade: F, score: 55)**, so that **improve project environment variables from F to at least B (80+)**.
- As a **developer**, I want to **address analyze_xdg_kg findings (grade: F, score: 0)**, so that **improve project analyze_xdg_kg from F to at least B (80+)**.

## Functional Requirements

- **FR-001**: Minor update: agent-utilities 0.2.40 (installed) -> 0.16.0
- **FR-002**: Minor update: pytest-xdist 3.6.0 (constraint — not installed) -> 3.8.0
- **FR-003**: 2 functions exceed 200 lines (actionable refactoring targets): register_leanix_mtm_tools (331L), leanix_leanix_mtm (329L)
- **FR-004**: Needs attention: api_client_pathfinder.py (779L) — God class: Api (71 methods) — consider mixins/composition
- **FR-005**: Needs attention: api_client_reference_data.py (671L) — God class: Api (56 methods) — consider mixins/composition
- **FR-006**: Needs attention: api_client_mtm.py (1595L) — God class: Api (155 methods) — consider mixins/composition
- **FR-007**: 2 flat directories with >15 Python files: leanix_agent/mcp, leanix_agent/api
- **FR-008**: Test suite lacks intent diversity (only one type)
- **FR-009**: 11 potential doc-test drift items
- **FR-010**: README.md missing sections: usage|quick start
- **FR-011**: 2 broken internal links in README.md
- **FR-012**: README missing: Has usage examples with code blocks
- **FR-013**: SRP: 6 modules exceed 500 lines (god modules)
- **FR-014**: SRP: 19 classes have >15 methods
- **FR-015**: No discernible layer architecture (no domain/service/adapter separation)
- **FR-016**: 22 Python files at top level — consider package organization
- **FR-017**: Low traceability ratio: 5% concepts fully traced
- **FR-018**: 39 orphaned concepts (only in one source)
- **FR-019**: 204 test functions missing concept markers
- **FR-020**: 583 significant functions (>10 lines) missing concept markers in docstrings
- **FR-021**: Total lint findings: 0 (high/error: 0, medium/warning: 0, low: 0)
- **FR-022**: 1 hook(s) may be outdated: ruff-pre-commit
- **FR-023**: 2 directories with >20 files: leanix_agent/mcp, leanix_agent/api
- **FR-024**: CHANGELOG.md exists but could not be parsed — check format compliance
- **FR-025**: No changelog entries within the last 30 days
- **FR-026**: keepachangelog not installed — pip install 'universal-skills[code-enhancer]'
- **FR-027**: 3 test files exceed 500 lines — split into focused modules
- **FR-028**: 2 test files have >30 tests — too dense
- **FR-029**: Test directory lacks subdirectory organization (consider unit/, integration/, e2e/)
- **FR-030**: 2 tests have no assertions
- **FR-031**: 19 tests use weak assertions (assert result is not None, assert True, etc.)
- **FR-032**: Only 14% of env vars documented in README.md
- **FR-033**: Undocumented env vars: AUDIENCE, AUTH_TYPE, DEFAULT_AGENT_NAME, DELEGATED_SCOPES, EUNOMIA_POLICY_FILE, EUNOMIA_TYPE, GRAPHQLTOOL, LEANIX_AGENT_VERIFY, LEANIX_AI_INVENTORY_BUILDERTOOL, LEANIX_APPTIO_CONNECTORTOOL
- **FR-034**: 13 Python env vars not in .env.example: AUDIENCE, DEFAULT_AGENT_NAME, DELEGATED_SCOPES, LEANIX_API_TOKEN, LEANIX_BROWSER_LOGIN
- **FR-035**: 7 env vars have no default value in code
- **FR-036**: Analysis error: No module named 'agent_utilities.knowledge_graph'

## Success Criteria

- Overall GPA: 2.24 → 3.0
- Domains at B or above: 7 → 17
- Actionable findings: 36 → 0
