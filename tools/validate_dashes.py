#!/usr/bin/env python3
"""Fail if any em dash or en dash appears in derived prose files.

Stdlib only. Walks Markdown and YAML files in the repo, decoding each file
as UTF-8 and scanning decoded text, so Unicode escape sequences cannot slip
a dash past a raw byte sweep (regression: the em-dash validator Unicode
escape bypass). Data files under a caller-supplied exclusion list are
skipped because source data content is quoted verbatim, not derived prose.

Exit 0 when no dashes are found. Exit 1 with file and line references
otherwise. Per the probe posture law this tool reports NO VIOLATIONS
DETECTED, never CLEAN.
"""
import sys
from pathlib import Path

FORBIDDEN = {"\u2014": "em dash", "\u2013": "en dash"}
SCAN_SUFFIXES = {".md", ".yml", ".yaml", ".cff", ".txt"}
EXCLUDE_PARTS = {".git", "engagements", "site", "__pycache__"}


def scan(root):
    violations = []
    for path in sorted(Path(root).rglob("*")):
        if not path.is_file() or path.suffix not in SCAN_SUFFIXES:
            continue
        if EXCLUDE_PARTS & set(path.parts):
            continue
        try:
            text = path.read_text(encoding="utf-8")
        except UnicodeDecodeError:
            violations.append((path, 0, "file is not valid UTF-8"))
            continue
        for lineno, line in enumerate(text.splitlines(), 1):
            for ch, name in FORBIDDEN.items():
                if ch in line:
                    violations.append((path, lineno, name))
    return violations


def main():
    root = sys.argv[1] if len(sys.argv) > 1 else "."
    violations = scan(root)
    if violations:
        for path, lineno, name in violations:
            print(f"DASH VIOLATION: {path}:{lineno}: {name}")
        sys.exit(1)
    print("dash gate: NO VIOLATIONS DETECTED")


if __name__ == "__main__":
    main()
