#!/usr/bin/env python3
"""Decode approximate post timestamps from LinkedIn activity IDs.

Stdlib only. LinkedIn activity IDs encode a millisecond Unix timestamp in
the upper 41 bits (id >> 22). This is a widely documented community
technique, not a platform guarantee, so decoded dates carry the INFERENCE
evidence tier in all downstream use.

Usage:
    python3 analysis/decode_timestamps.py data.json > timestamps.csv
"""
import csv
import datetime
import json
import sys


def decode(post_id):
    return datetime.datetime.fromtimestamp(
        (post_id >> 22) / 1000, datetime.timezone.utc)


def main(source):
    with open(source, encoding="utf-8") as f:
        posts = json.load(f)["Posts"]
    writer = csv.writer(sys.stdout)
    writer.writerow(["linkedinPostId", "decoded_utc"])
    skipped = 0
    for p in posts:
        pid = p.get("linkedinPostId")
        if not pid:
            skipped += 1
            continue
        writer.writerow([pid, decode(pid).isoformat()])
    print(f"skipped {skipped} records without a post ID", file=sys.stderr)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: decode_timestamps.py /path/to/data.json")
    main(sys.argv[1])
