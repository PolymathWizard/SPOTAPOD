# Data Dictionary

Formal definitions for every field in `podawaa2024_fixed.json`. Without this page, two researchers can read the same field and mean different things.

## File structure

A single JSON object with one top-level key, `Posts`, holding an array of 213,491 record objects. UTF-8 encoded, CRLF line endings, approximately 221 MB uncompressed. A machine-readable JSON Schema is in [schema/posts.schema.json](https://github.com/PolymathWizard/SPOTAPOD/blob/main/schema/posts.schema.json).

## Fields

| Field | Type | Meaning | Null behavior |
|---|---|---|---|
| `linkedinPostId` | Integer (64-bit) | LinkedIn activity identifier for the post. Encodes an approximate creation timestamp in its upper 41 bits (see below). | Key absent in 3,364 records. Never null when present. |
| `Content` | String | Post text as captured, up to 3,000 characters. Multilingual: roughly 74 percent of a 50,000-record sample contains non-ASCII characters. | Present in all records, but 2,692 records carry platform placeholder strings or empty text (see below). |
| `AuthorPublicIdentifier` | String or null | The public URL slug of the posting account (the part after `linkedin.com/in/`). Identifies a real person's public profile. | Null in 23,894 records (11.2 percent). |
| `Likes` | Integer | Reaction count captured at observation time. Zero in 24,273 records. | Always present. |
| `Views` | Integer | View count captured at observation time. Zero in 94,643 records (44.3 percent). A zero here more often means "not captured" than "nobody saw it"; see interpretation notes. | Always present. |

## Interpretation notes

**Views is unevenly populated.** LinkedIn exposes view counts inconsistently across post types, account types, and collection paths. Treat `Views == 0` as missing data unless corroborated, not as an observed zero audience. Analyses that use like-to-view ratios must restrict to `Views > 0` and should state a minimum-views floor.

**Likes exceeding Views.** 2,500 records show more Likes than Views, which is organically impossible if both counters were captured accurately at the same moment. Evidence tier for the fact: VERIFIED. Evidence tier for any explanation: INFERENCE. The most plausible reading is a Views capture artifact (counters captured at different times or through different endpoints), not per-record proof of manipulation. Do not cite these 2,500 records as individually fraudulent.

**Placeholder content.** Known placeholder strings observed in the file: `This post has no content` (2,156 records), `Cette publication n'a pas de contenu` (502), `postNoContent` (160), plus 536 empty strings. These indicate reposts, media-only posts, or capture failures. Exclude them from text analysis.

**Duplicate post IDs.** 9,127 rows share a `linkedinPostId` with another row. These are near-certain recapture duplicates of the same post at different observation moments (Likes and Views may differ between copies). Deduplicate on `linkedinPostId` before counting posts; keep all rows when studying counter drift between captures.

**Author identifiers are personal data.** The slug resolves to an identifiable person's public profile. Handling rules are in [Ethics](ethics.md). Aggregate before publishing; do not build public per-person accusation lists from this field.

## What the file does not contain

No collection timestamps, no comment counts, no share counts, no follower counts, no pod-membership evidence, no account metadata (industry, location, employer), no media, no classification or confidence fields. Every one of these absences constrains what the data can support; see [Limitations](limitations.md).

## Units, ranges, observed values

- `Likes`: 0 to 215,818. Median 57. p90 499, p99 2,190.
- `Views`: 0 to 14,771,715 (maximum observed).
- `Content` length: median 667 characters, p90 1,765, hard ceiling 3,000 (LinkedIn's post limit).
- Decoded post dates (INFERENCE): 2018-07-15 to 2024-11-01.

All figures above are VERIFIED against source file SHA256 `2d64e4b274c1b238399a6b1d578b951cac9d5035a980ab70d4c3d66efffb4214` and regenerate via `analysis/profile_dataset.py`.
