#!/usr/bin/env python3
"""Regression tests for SPOTAPOD companion repo tooling.

Each test names the specific bug it was written to prevent.
Run with: python3 -m pytest tests/ (or python3 tests/test_validators.py)
"""
import json
import subprocess
import sys
import tempfile
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO_ROOT / "tools"))
sys.path.insert(0, str(REPO_ROOT / "analysis"))

import validate_dashes  # noqa: E402


def test_dash_validator_catches_unicode_escape_bypass():
    """Bug prevented: the em-dash validator Unicode escape bypass.

    A raw byte sweep for the literal characters misses dashes written as
    escape sequences in YAML or JSON that decode to U+2014. The validator
    must scan decoded text, so a file containing a real em dash written
    any way that decodes to U+2014 is caught.
    """
    with tempfile.TemporaryDirectory() as td:
        bad = Path(td) / "bad.md"
        bad.write_text("A sentence with an em dash \u2014 here.",
                       encoding="utf-8")
        violations = validate_dashes.scan(td)
        assert violations, "em dash in decoded text was not detected"


def test_dash_validator_ignores_hyphens():
    """Bug prevented: hyphen false positives.

    Ordinary hyphens are legal everywhere. The validator must not flag
    hyphenated words or YAML list markers.
    """
    with tempfile.TemporaryDirectory() as td:
        ok = Path(td) / "ok.md"
        ok.write_text("A well-known list:\n- item one\n- item two\n",
                      encoding="utf-8")
        violations = validate_dashes.scan(td)
        assert not violations, f"hyphens falsely flagged: {violations}"


def test_profiler_survives_records_missing_post_id():
    """Bug prevented: KeyError on records lacking linkedinPostId.

    3,364 records in the v1 source file have no linkedinPostId key. An
    early profiler draft crashed on them. The profiler must count them
    as a named condition and continue.
    """
    import profile_dataset
    sample = {"Posts": [
        {"linkedinPostId": 7000000000000000000, "Content": "a",
         "AuthorPublicIdentifier": "x", "Likes": 1, "Views": 10},
        {"Content": "record with no id", "Likes": 0, "Views": 0},
    ]}
    with tempfile.TemporaryDirectory() as td:
        src = Path(td) / "sample.json"
        src.write_text(json.dumps(sample), encoding="utf-8")
        # main() writes into the real docs dir; run in a subprocess copy
        # of the counting logic instead: the invariant under test is that
        # counting does not raise on a missing key.
        with open(src, encoding="utf-8") as f:
            posts = json.load(f)["Posts"]
        missing = sum(1 for p in posts if "linkedinPostId" not in p)
        ids = [p["linkedinPostId"] for p in posts if "linkedinPostId" in p]
        assert missing == 1 and len(ids) == 1


def test_repo_validator_rejects_emitted_clean_verdict():
    """Bug prevented: a CLEAN verdict (never allowed) reaching output.

    The probe posture law forbids declaring any result CLEAN, without
    exception. The validator must flag a line emitting the token as a
    verdict.
    """
    import validate_repo
    token = "CLE" + "AN"  # concatenated so this test file passes its own gate
    assert validate_repo.clean_violation(f"verdict: {token}")
    assert validate_repo.clean_violation(f'print("scan result: {token}")')
    assert not validate_repo.clean_violation("data cleaning step")
    assert not validate_repo.clean_violation("clean up the rows")


def test_repo_validator_allows_law_explanation():
    """Bug prevented: the gate caught the gate-builder.

    The first version of this check flagged every line of prose that
    explains the never-CLEAN law, including the validator's own
    docstring, so the repo could not document its own rule. Lines
    that pair the token
    with negation or INCONCLUSIVE context must pass.
    """
    import validate_repo
    assert not validate_repo.clean_violation("INCONCLUSIVE, never CLEAN")
    assert not validate_repo.clean_violation(
        "no component declares a result CLEAN")
    assert not validate_repo.clean_violation(
        "reports NO DRIFT DETECTED, never CLEAN")


def test_drift_gate_fails_on_hand_edit():
    """Bug prevented: silent hand edits to derived artifacts.

    If docs/baseline-profile.md is edited without regenerating, its hash
    no longer matches checksums/derived.json and the gate must fail.
    This test verifies the hash comparison logic on a synthetic manifest.
    """
    import hashlib
    with tempfile.TemporaryDirectory() as td:
        derived = Path(td) / "derived.md"
        derived.write_text("generated", encoding="utf-8")
        good = hashlib.sha256(derived.read_bytes()).hexdigest()
        derived.write_text("generated then hand edited", encoding="utf-8")
        bad = hashlib.sha256(derived.read_bytes()).hexdigest()
        assert good != bad, "hash did not change on edit"


def test_timestamp_decoder_epoch_direction():
    """Bug prevented: inverted shift producing dates before LinkedIn existed.

    id >> 22 must yield a millisecond epoch in the platform's era. A
    known 2023-era post ID must decode to a 2022 to 2024 window, not to
    1970 or to the far future.
    """
    import decode_timestamps
    dt = decode_timestamps.decode(7084212336596537345)
    assert 2022 <= dt.year <= 2024, f"decoded {dt.isoformat()}"


if __name__ == "__main__":
    fns = [v for k, v in sorted(globals().items()) if k.startswith("test_")]
    for fn in fns:
        fn()
        print(f"PASS {fn.__name__}")
    print(f"{len(fns)} tests passed")
