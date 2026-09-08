#!/usr/bin/env python3
"""Flag engagement-ratio anomalies in the SPOTAPOD dataset.

Stdlib only. Emits a CSV of records whose like-to-view ratio exceeds a
user-chosen threshold, restricted to records with nonzero Views.

Every output row is an observation, not an accusation. A high ratio is a
statistical anomaly relative to the dataset's own distribution. Whether a
given anomaly reflects pod activity, a Views capture gap, or an organic
outlier is a provenance question this script cannot answer. Per the probe
posture law, the script classifies transport-level facts only. It never
emits a CLEAN verdict for any record or author, never.

Usage:
    python3 analysis/engagement_anomalies.py data.json --threshold 0.5 > anomalies.csv
"""
import argparse
import csv
import json
import sys


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("source")
    ap.add_argument("--threshold", type=float, default=0.5,
                    help="like-to-view ratio above which a record is flagged")
    ap.add_argument("--min-views", type=int, default=100,
                    help="ignore records below this view count")
    args = ap.parse_args()

    with open(args.source, encoding="utf-8") as f:
        posts = json.load(f)["Posts"]

    writer = csv.writer(sys.stdout)
    writer.writerow(["linkedinPostId", "author", "likes", "views",
                     "ratio", "flag"])
    flagged = 0
    for p in posts:
        views = p.get("Views", 0)
        if views < args.min_views:
            continue
        likes = p.get("Likes", 0)
        ratio = likes / views
        if ratio > args.threshold:
            flag = "LIKES_EXCEED_VIEWS" if likes > views else "RATIO_ANOMALY"
            writer.writerow([p.get("linkedinPostId", ""),
                             p.get("AuthorPublicIdentifier", ""),
                             likes, views, f"{ratio:.4f}", flag])
            flagged += 1
    print(f"flagged {flagged} records at threshold {args.threshold}, "
          f"min views {args.min_views}", file=sys.stderr)


if __name__ == "__main__":
    main()
