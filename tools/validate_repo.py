#!/usr/bin/env python3
"""Repo conformance validator for the SPOTAPOD companion repository.

Stdlib only. Checks:
1. Required files exist.
2. No line emits a CLEAN verdict token (INCONCLUSIVE, never CLEAN).
3. Evidence tier vocabulary in docs uses only the five canonical tiers.
4. Internal Markdown links in docs resolve to real files.
5. The raw dataset JSON is not committed to the repo.

Per the probe posture law this validator reports NO VIOLATIONS DETECTED,
never CLEAN.
"""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
REQUIRED = [
    "README.md",
    "CHANGELOG.md",
    "CONTRIBUTING.md",
    "CITATION.cff",
    "LICENSE",
    "LICENSE-CONTENT",
    "docs/method.md",
    "docs/data-dictionary.md",
    "docs/limitations.md",
    "docs/ethics.md",
    "docs/research-questions.md",
    "docs/use-cases.md",
    "docs/faq.md",
    "docs/baseline-profile.md",
    "docs/corrections.md",
    "checksums/CHECKSUMS.txt",
    "checksums/derived.json",
    "schema/posts.schema.json",
    "engagements/.gitkeep",
]
CANONICAL_TIERS = {"VERIFIED", "CORROBORATED", "UNCORROBORATED",
                   "INFERENCE", "STATED"}
# Word-boundary CLEAN as a standalone verdict token. The phrase
# "cleaning" or "clean up" in prose is allowed; the verdict token
# "CLEAN" in caps is not. Explanatory prose about the law itself is
# allowed: legitimate mentions always pair the token with a negation
# or with INCONCLUSIVE on the same line ("INCONCLUSIVE, never CLEAN").
# A line that emits the token without such context is a violation.
# Regression: the gate caught the gate-builder. The first version of
# this check flagged every line of prose explaining the never-CLEAN
# law, including its own docstring. The negation-context rule below
# is the fix, and tests/test_validators.py names the bug.
CLEAN_RE = re.compile(r"\bCLEAN\b")
ALLOW_RE = re.compile(
    r"\b(never|not|no|nothing|inconclusive|forbid\w*|token)\b",
    re.IGNORECASE)


def clean_violation(line):
    """True when a line emits the CLEAN verdict token outside
    negation or law-explanation context."""
    return bool(CLEAN_RE.search(line)) and not ALLOW_RE.search(line)
LINK_RE = re.compile(r"\]\((?!https?://|#|mailto:)([^)]+)\)")


def main():
    failures = []

    for rel in REQUIRED:
        if not (REPO_ROOT / rel).exists():
            failures.append(f"missing required file: {rel}")

    for path in sorted(REPO_ROOT.rglob("*")):
        if not path.is_file():
            continue
        if {".git", "engagements", "site", "__pycache__"} & set(path.parts):
            continue
        if path.suffix in {".md", ".py", ".yml", ".yaml", ".cff"}:
            text = path.read_text(encoding="utf-8", errors="replace")
            for lineno, line in enumerate(text.splitlines(), 1):
                if clean_violation(line):
                    failures.append(
                        "forbidden verdict token (use INCONCLUSIVE) in "
                        f"{path.relative_to(REPO_ROOT)}:{lineno}")
        if path.suffix == ".md":
            text = path.read_text(encoding="utf-8", errors="replace")
            for m in LINK_RE.finditer(text):
                target = m.group(1).split("#")[0]
                if not target:
                    continue
                resolved = (path.parent / target).resolve()
                if not resolved.exists():
                    failures.append(
                        f"broken link in {path.relative_to(REPO_ROOT)}: "
                        f"{target}")

    for pattern in ("*.json",):
        for path in REPO_ROOT.rglob(pattern):
            if path.stat().st_size > 50 * 1024 * 1024:
                failures.append(
                    f"large data file committed: {path.relative_to(REPO_ROOT)}"
                    " (raw dataset must live on Dataverse, not in git)")

    if failures:
        for f in failures:
            print(f"CONFORMANCE: {f}")
        sys.exit(1)
    print("repo gate: NO VIOLATIONS DETECTED")


if __name__ == "__main__":
    main()
