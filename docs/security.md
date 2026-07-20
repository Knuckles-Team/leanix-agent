# Security and release privacy

LeanIX Agent treats connection details, credentials, tenant data, schemas, and
generated mappings as deployment-owned configuration. None of those values are
required in the source tree or distribution wheel.

## Repository security contract

The bounded contract in `security/security-contract.json` declares the only
permitted fuzz and authenticated-negative hooks and the fail-closed SPDX license
policy. Hook commands are argument arrays, never shell strings. The runner
removes credential-like environment variables, bounds execution time and output,
and requires structured passing evidence.

Run the source checks from the repository root:

```bash
python3 scripts/security_contract.py \
  --contract security/security-contract.json validate
python3 scripts/security_contract.py \
  --contract security/security-contract.json \
  run-hook --kind fuzz --result-root security-results
python3 scripts/security_contract.py \
  --contract security/security-contract.json \
  run-hook --kind authenticated_negative --result-root security-results
```

The authenticated-negative hook also rejects mutable third-party workflow
references, broad token permissions, privileged pull-request triggers, and
secret interpolation into shell commands.

## Wheel privacy gate

Every release wheel must pass:

```bash
python3 scripts/check_wheel_privacy.py path/to/leanix_agent.whl
```

The gate rejects local machine paths, email-like content, bytecode, test trees,
documentation trees, scripts, and unsafe archive member paths. It reports only
stable finding categories and never echoes matched content.

TLS verification remains enabled. Trust stores, client certificates, endpoint
URLs, and credentials are referenced through deployment configuration and are
not embedded in source, documentation examples, evidence, or release artifacts.
