#!/usr/bin/env python3
"""Author concentration and volume analysis for the SPOTAPOD dataset.

Stdlib only. Emits per-author aggregates: record count, total likes, mean
likes, share of records with zero views, and duplicate-content count within
the author's own records. Aggregates support pattern analysis without
requiring any judgment about individual authors.

Usage:
    python3 analysis/author_concentration.py data.json --min-posts 20 > authors.csv
"""
import argparse
import collections
import csv
import json
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--min-posts", type=int, default=20)
    args = ap.parse_args()

    with open(args.source, encoding="utf-8") as f:
        posts = json.load(f)["Posts"]

    by_author = collections.defaultdict(list)
    for p in posts:
        a = p.get("AuthorPublicIdentifier")
        if a:
            by_author[a].append(p)

    writer = csv.writer(sys.stdout)
    writer.writerow(["author", "records", "total_likes", "mean_likes",
                     "zero_view_share", "internal_duplicate_content"])
    for author, rows in sorted(by_author.items(),
                               key=lambda kv: -len(kv[1])):
        if len(rows) < args.min_posts:
            continue
        likes = [r.get("Likes", 0) for r in rows]
        zero_views = sum(1 for r in rows if r.get("Views", 0) == 0)
        texts = collections.Counter(
            r.get("Content", "").strip() for r in rows)
        internal_dupes = sum(c for t, c in texts.items() if c > 1 and t)
        writer.writerow([author, len(rows), sum(likes),
                         f"{sum(likes)/len(likes):.1f}",
                         f"{zero_views/len(rows):.3f}", internal_dupes])
    print(f"authors with {args.min_posts}+ records written to stdout",
          file=sys.stderr)


if __name__ == "__main__":
    main()
