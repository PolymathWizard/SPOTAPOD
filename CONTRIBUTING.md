# Contributing

Contributions that strengthen inspectability are welcome: analysis scripts, data-quality findings, documentation corrections, translations of the docs.

## Ground rules

1. Stdlib-only Python for anything in analysis/ and tools/. No new dependencies without an ADR.
2. Derived artifacts are generated, never hand edited. Regenerate docs/baseline-profile.md via the profiler; the drift gate fails on manual edits.
3. Evidence tiers are mandatory on research claims: VERIFIED, CORROBORATED, STATED, UNCORROBORATED, or INFERENCE, inline.
4. No per-person verdicts. Scripts output observations and statistical flags only. Nothing in this repo declares an account guilty, and nothing declares one clean of manipulation either; absence of anomaly is INCONCLUSIVE.
5. No em dashes or en dashes in prose. Commas or parentheses instead. CI enforces this.
6. New regression tests must name the bug they prevent in their docstring.
7. Conventional commits scoped to the project, for example: spotapod: add ratio percentile flags to anomaly script

## Before opening a PR

Run the full gate locally:

    python3 tools/validate_dashes.py .
    python3 tools/validate_repo.py
    python3 tools/derive_gate.py
    python3 tests/test_validators.py

All four must pass.

## Disputes about the data itself

Use the correction process in docs/corrections.md, not a pull request. Data changes flow through the Dataverse record.
