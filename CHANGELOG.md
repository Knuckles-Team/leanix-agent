# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added
- Standardized README.md layout including robust table of contents and dynamic environment setup guides.
- Concept ID traceability tags `[KG-...]` throughout function docstrings and test assertions.

## [0.14.0] - 2026-05-22

### Added
- Real-time custom meta-model discovery via `leanix_discover_meta_model` tool to inspect dynamic custom attributes.
- Comprehensive `.env.example` cataloging all 18 configurable environment variables spanning MTM, Pathfinder, and OTEL options.
- Support for `SSL_VERIFY` and `LEANIX_AGENT_VERIFY` variables to strictly toggle SSL connection warnings.
- Robust test parameterization and isolation of dynamic client test behaviors.

### Changed
- Refactored monolithic `mcp_server.py` into a highly cohesive modular package directory structure under `leanix_agent/mcp/`.
- Consolidated interactive browser authentication workflows to gracefully fall back on OIDC/OAuth SSO tokens when static tokens are missing.

### Fixed
- Silenced standard library `RequestsDependencyWarning` log spam early on server startup.
- Upgraded pre-commit hook configuration definitions for modern Ruff and codespell versions.

[Unreleased]: https://github.com/leanix/leanix-agent/compare/v0.14.0...HEAD
[0.14.0]: https://github.com/leanix/leanix-agent/releases/tag/v0.14.0
