#!/usr/bin/env python3
"""Drift gate: fail if any derived artifact diverges from its recorded hash.

Stdlib only. checksums/derived.json is written only by the generator
(analysis/profile_dataset.py). This gate recomputes the SHA256 of each
derived file and compares it to the manifest. A mismatch means a derived
file was hand edited or the manifest was not regenerated, and CI fails.

Per the probe posture law this gate reports NO DRIFT DETECTED, never CLEAN.
"""
import hashlib
import json
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
MANIFEST = REPO_ROOT / "checksums" / "derived.json"


def main():
    if not MANIFEST.exists():
        sys.exit("drift gate: checksums/derived.json is missing")
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8"))
    failures = []
    for rel, recorded in manifest.get("derived", {}).items():
        path = REPO_ROOT / rel
        if not path.exists():
            failures.append(f"{rel}: file missing")
            continue
        actual = hashlib.sha256(path.read_bytes()).hexdigest()
        if actual != recorded:
            failures.append(f"{rel}: hash mismatch (hand edit suspected)")
    if failures:
        for f in failures:
            print(f"DRIFT: {f}")
        sys.exit(1)
    print("drift gate: NO DRIFT DETECTED")


if __name__ == "__main__":
    main()
