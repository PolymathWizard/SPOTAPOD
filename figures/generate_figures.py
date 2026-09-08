#!/usr/bin/env python3
"""Generate BHIL brand-palette figures from the SPOTAPOD source JSON.

Requires matplotlib (the one permitted non-stdlib dependency, per the BHIL
brand chart convention). Headless Agg backend. IBM Plex fonts when present
in ~/.fonts, silent fallback otherwise. Brand tokens: COBALT #1B4FD8,
COBALT_DARK #0F2F8A, COBALT_LIGHT #E8EEFF, NAVY #1C1C2E, ACCENT #6B9EFF.
Style: hairlines not boxes, square corners, no box frames, Plex Mono tick
labels.

Figures are derived artifacts. This script merges their SHA256 hashes into
checksums/derived.json so the drift gate covers them; hand edits fail CI.

Usage:
    python3 figures/generate_figures.py /path/to/podawaa2024_fixed.json
"""
import collections
import datetime
import hashlib
import json
import os
import sys
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.font_manager as fm  # noqa: E402
import matplotlib.pyplot as plt  # noqa: E402

REPO_ROOT = Path(__file__).resolve().parent.parent
FIG_DIR = REPO_ROOT / "docs" / "figures"
MANIFEST = REPO_ROOT / "checksums" / "derived.json"

COBALT = "#1B4FD8"
COBALT_DARK = "#0F2F8A"
COBALT_LIGHT = "#E8EEFF"
NAVY = "#1C1C2E"
ACCENT = "#6B9EFF"
HAIR = "#D8DCE6"
STONE = "#6B7280"
PAPER = "#FFFFFF"

for fdir in (os.path.expanduser("~/.fonts"), "/root/.fonts"):
    if os.path.isdir(fdir):
        for f in os.listdir(fdir):
            if f.endswith(".ttf"):
                try:
                    fm.fontManager.addfont(os.path.join(fdir, f))
                except Exception:
                    pass

SANS = "IBM Plex Sans" if any(
    "IBM Plex Sans" in f.name for f in fm.fontManager.ttflist) else "DejaVu Sans"
MONO = "IBM Plex Mono" if any(
    "IBM Plex Mono" in f.name for f in fm.fontManager.ttflist) else "DejaVu Sans Mono"

plt.rcParams.update({
    "font.family": SANS,
    "text.color": NAVY,
    "axes.labelcolor": STONE,
    "xtick.color": STONE,
    "ytick.color": NAVY,
    "figure.facecolor": PAPER,
    "axes.facecolor": PAPER,
    "axes.grid": False,
    "savefig.dpi": 200,
})

FOOTER = "BHIL SPOTAPOD  |  Human-Directed. AI-Enabled. Commercially Tested."


def strip_axes(ax, keep_bottom=True, keep_left=False):
    for s in ("top", "right"):
        ax.spines[s].set_visible(False)
    ax.spines["left"].set_visible(keep_left)
    ax.spines["bottom"].set_visible(keep_bottom)
    for s in ("bottom", "left"):
        ax.spines[s].set_linewidth(0.8)
        ax.spines[s].set_color(NAVY)
    ax.tick_params(length=0)
    for lbl in ax.get_xticklabels() + ax.get_yticklabels():
        lbl.set_fontfamily(MONO)
        lbl.set_fontsize(9)


def finish(fig, name, tier_note):
    fig.text(0.01, 0.012, FOOTER, fontsize=7.5, family=MONO, color=STONE)
    fig.text(0.99, 0.012, tier_note, fontsize=7.5, family=MONO,
             color=COBALT_DARK, ha="right")
    out = FIG_DIR / name
    fig.savefig(out, metadata={})
    plt.close(fig)
    print(f"wrote {out}")
    return name


def main(source):
    FIG_DIR.mkdir(parents=True, exist_ok=True)
    with open(source, encoding="utf-8") as f:
        posts = json.load(f)["Posts"]
    n = len(posts)
    written = []

    # FIG 1: Likes distribution, log-x histogram
    likes = [p.get("Likes", 0) for p in posts]
    fig, ax = plt.subplots(figsize=(10.9, 5.2))
    bins = [0, 1, 3, 10, 30, 100, 300, 1000, 3000, 10000, 30000, 100000, 300000]
    # stdlib-friendly binning to avoid a numpy dependency
    counts = [0] * (len(bins) - 1)
    for v in likes:
        for i in range(len(bins) - 1):
            if bins[i] <= v < bins[i + 1]:
                counts[i] += 1
                break
        else:
            counts[-1] += 1
    labels = ["0", "1-2", "3-9", "10-29", "30-99", "100-299", "300-999",
              "1K-3K", "3K-10K", "10K-30K", "30K-100K", "100K+"]
    bars = ax.bar(range(len(counts)), counts, color=COBALT, width=0.62)
    bars[0].set_color(COBALT_LIGHT)
    bars[0].set_edgecolor(COBALT)
    for i, c in enumerate(counts):
        ax.text(i, c + max(counts) * 0.012, f"{c:,}", ha="center",
                fontsize=8, family=MONO, color=NAVY)
    ax.set_xticks(range(len(labels)))
    ax.set_xticklabels(labels)
    ax.set_yticks([])
    strip_axes(ax)
    ax.set_title("Likes per record: heavy tail, modest middle",
                 fontsize=15, color=NAVY, loc="left", pad=14)
    ax.text(0, 1.015, f"median 57 likes  |  p99 2,190  |  max 215,818  |  n = {n:,}",
            transform=ax.transAxes, fontsize=9.5, family=MONO, color=STONE)
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    written.append(finish(fig, "fig1-likes-distribution.png", "VERIFIED"))

    # FIG 2: Author concentration curve
    authors = collections.Counter(
        p.get("AuthorPublicIdentifier") for p in posts
        if p.get("AuthorPublicIdentifier"))
    counts_sorted = sorted(authors.values(), reverse=True)
    total_attr = sum(counts_sorted)
    xs, ys, cum = [], [], 0
    for i, c in enumerate(counts_sorted, 1):
        cum += c
        if i <= 200 or i % 25 == 0 or i == len(counts_sorted):
            xs.append(i)
            ys.append(100 * cum / total_attr)
    fig, ax = plt.subplots(figsize=(10.9, 5.2))
    ax.plot(xs, ys, color=COBALT, linewidth=2.2)
    ax.fill_between(xs, ys, color=COBALT_LIGHT)
    for topn in (10, 100, 438):
        share = 100 * sum(counts_sorted[:topn]) / total_attr
        ax.plot([topn], [share], "o", color=COBALT_DARK, markersize=5)
        label = f"top {topn}: {share:.0f}%" if topn != 438 else \
            f"438 authors (100+ records): {share:.0f}%"
        ax.annotate(label, (topn, share), textcoords="offset points",
                    xytext=(10, -4), fontsize=9, family=MONO, color=NAVY)
    ax.set_xscale("log")
    ax.set_xlabel("authors, ranked by record count (log scale)")
    ax.set_ylabel("cumulative share of attributed records")
    ax.grid(True, axis="y", color=HAIR, linewidth=0.7)
    strip_axes(ax, keep_left=True)
    ax.set_title("Volume concentration across 7,033 author identifiers",
                 fontsize=15, color=NAVY, loc="left", pad=14)
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    written.append(finish(fig, "fig2-author-concentration.png", "VERIFIED"))

    # FIG 3: Posts by decoded year
    years = collections.Counter(
        datetime.datetime.fromtimestamp(
            (p["linkedinPostId"] >> 22) / 1000,
            datetime.timezone.utc).year
        for p in posts if p.get("linkedinPostId", 0) > 0)
    ys_sorted = sorted(y for y in years if y >= 2019)
    fig, ax = plt.subplots(figsize=(10.9, 5.2))
    vals = [years[y] for y in ys_sorted]
    ax.bar([str(y) for y in ys_sorted], vals, color=COBALT, width=0.55)
    for i, v in enumerate(vals):
        ax.text(i, v + max(vals) * 0.012, f"{v:,}", ha="center",
                fontsize=9, family=MONO, color=NAVY)
    ax.set_yticks([])
    strip_axes(ax)
    ax.set_title("Records by decoded post year",
                 fontsize=15, color=NAVY, loc="left", pad=14)
    ax.text(0, 1.015,
            "dates decoded from LinkedIn activity IDs, id >> 22  |  "
            "growth confounds phenomenon with collection effort",
            transform=ax.transAxes, fontsize=9.5, family=MONO, color=STONE)
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    written.append(finish(fig, "fig3-posts-by-year.png", "INFERENCE"))

    # FIG 4: Like-to-view ratio, Views > 0 subset
    ratios = sorted(p["Likes"] / p["Views"] for p in posts
                    if p.get("Views", 0) > 0)
    edges = [0, .01, .02, .05, .1, .2, .5, 1.0, float("inf")]
    labels4 = ["<1%", "1-2%", "2-5%", "5-10%", "10-20%", "20-50%",
               "50-100%", "100%+"]
    counts4 = [0] * (len(edges) - 1)
    for r in ratios:
        for i in range(len(edges) - 1):
            if edges[i] <= r < edges[i + 1]:
                counts4[i] += 1
                break
    fig, ax = plt.subplots(figsize=(10.9, 5.2))
    colors = [COBALT] * 6 + [ACCENT, COBALT_DARK]
    bars = ax.bar(range(len(counts4)), counts4, color=colors, width=0.62)
    for i, c in enumerate(counts4):
        ax.text(i, c + max(counts4) * 0.012, f"{c:,}", ha="center",
                fontsize=8.5, family=MONO, color=NAVY)
    ax.set_xticks(range(len(labels4)))
    ax.set_xticklabels(labels4)
    ax.set_yticks([])
    strip_axes(ax)
    ax.set_title("Like-to-view ratio, records with Views > 0",
                 fontsize=15, color=NAVY, loc="left", pad=14)
    ax.text(0, 1.015,
            f"n = {len(ratios):,}  |  median 5.8%  |  the 100%+ band holds "
            "2,619 records (2,500 with likes above views): capture anomaly, "
            "not per-record proof",
            transform=ax.transAxes, fontsize=9.5, family=MONO, color=STONE)
    fig.tight_layout(rect=(0, 0.05, 1, 1))
    written.append(finish(fig, "fig4-ratio-distribution.png",
                          "VERIFIED / anomaly reading INFERENCE"))

    # FIG 5: Field completeness
    fields = [
        ("linkedinPostId", n - 3364),
        ("Content (usable text)", n - 3354),
        ("AuthorPublicIdentifier", n - 23894),
        ("Likes (nonzero)", n - 24273),
        ("Views (nonzero)", n - 94643),
    ]
    fig, ax = plt.subplots(figsize=(10.9, 4.6))
    names = [f[0] for f in fields][::-1]
    vals5 = [100 * f[1] / n for f in fields][::-1]
    ax.barh(range(len(names)), [100] * len(names), color=COBALT_LIGHT,
            height=0.55)
    ax.barh(range(len(names)), vals5, color=COBALT, height=0.55)
    for i, v in enumerate(vals5):
        ax.text(v - 1.2, i, f"{v:.1f}%", va="center", ha="right",
                fontsize=9, family=MONO, color=PAPER)
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels(names)
    ax.set_xticks([])
    strip_axes(ax, keep_bottom=False)
    ax.set_title("Field population: what each record actually carries",
                 fontsize=15, color=NAVY, loc="left", pad=14)
    ax.text(0, 1.02, "zero Views is treated as not captured, "
            "not as an observed zero audience",
            transform=ax.transAxes, fontsize=9.5, family=MONO, color=STONE)
    fig.tight_layout(rect=(0, 0.06, 1, 1))
    written.append(finish(fig, "fig5-field-completeness.png", "VERIFIED"))

    # Merge figure hashes into the derived manifest
    manifest = json.loads(MANIFEST.read_text(encoding="utf-8")) \
        if MANIFEST.exists() else {"derived": {}}
    for name in written:
        rel = f"docs/figures/{name}"
        manifest.setdefault("derived", {})[rel] = hashlib.sha256(
            (FIG_DIR / name).read_bytes()).hexdigest()
    MANIFEST.write_text(json.dumps(manifest, indent=2) + "\n",
                        encoding="utf-8")
    print(f"manifest updated with {len(written)} figures")


if __name__ == "__main__":
    if len(sys.argv) != 2:
        sys.exit("usage: generate_figures.py /path/to/podawaa2024_fixed.json")
    main(sys.argv[1])
