#!/usr/bin/env python3
"""Cross-account duplicate content clusters in the SPOTAPOD dataset.

Stdlib only. Groups records by exact normalized content and reports
clusters where the same non-placeholder text appears under two or more
distinct author identifiers. Cross-account text reuse is one observable
indicator relevant to coordinated posting analysis. It is an observation
tier fact (VERIFIED within the dataset); interpreting a cluster as
coordination is a separate INFERENCE step the analyst must document.

Usage:
    python3 analysis/duplicate_content.py data.json --min-authors 2 > clusters.csv
"""
import argparse
import collections
import csv
import json
import re
import sys

PLACEHOLDER = {"this post has no content", "postnocontent",
               "cette publication n'a pas de contenu", ""}


def normalize(text):
    return re.sub(r"\s+", " ", text.strip().lower())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--min-authors", type=int, default=2)
    ap.add_argument("--min-length", type=int, default=40,
                    help="ignore very short texts such as single-word reactions")
    args = ap.parse_args()

    with open(args.source, encoding="utf-8") as f:
        posts = json.load(f)["Posts"]

    clusters = collections.defaultdict(set)
    counts = collections.Counter()
    for p in posts:
        key = normalize(p.get("Content", ""))
        if key in PLACEHOLDER or len(key) < args.min_length:
            continue
        counts[key] += 1
        a = p.get("AuthorPublicIdentifier")
        if a:
            clusters[key].add(a)

    writer = csv.writer(sys.stdout)
    writer.writerow(["content_prefix", "record_count", "distinct_authors"])
    emitted = 0
    for key, authors in sorted(clusters.items(),
                               key=lambda kv: -len(kv[1])):
        if len(authors) >= args.min_authors:
            writer.writerow([key[:80], counts[key], len(authors)])
            emitted += 1
    print(f"{emitted} cross-account clusters at min authors "
          f"{args.min_authors}", file=sys.stderr)


if __name__ == "__main__":
    main()
