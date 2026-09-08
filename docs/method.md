# Method

How the SPOTAPOD research record works: what was collected, how it is classified, and how the publication layers fit together.

## The public data trust stack

There is rarely one perfect place to publish research data. Different platforms solve different parts of the problem, so SPOTAPOD splits the project into layers with distinct jobs.

| Layer | Purpose | Platform |
|---|---|---|
| Research record | Permanent, citable publication with a DOI | Harvard Dataverse (SPOTAPOD collection) |
| Research method | Methodology, schemas, analysis code, change history | This GitHub repository |
| Evidence archive | Original observations, timestamps, verification hashes | BHIL internal, controlled access |

The published dataset is the research artifact. The evidence archive is the source record. This repository is the methodology that explains the connection between them. A reader should never need access to the evidence archive to evaluate the published claims; the archive exists so disputed findings can be checked against original records.

## What a record is

Each record in `podawaa2024_fixed.json` represents one LinkedIn post attributed to an account observed in connection with engagement-pod tooling. The record carries the post's platform identifier, its text content, the author's public identifier, and two engagement counters (Likes and Views) as captured at observation time.

## How accounts entered the dataset

**Evidence tier: STATED.** The depositor describes the collection as posts from accounts using an engagement-pod platform. The records themselves contain no pod-membership field, no collection timestamp, and no extraction log, so the inclusion criterion cannot be re-derived from the published file. This is the single most important thing to understand about the dataset. Analyses of within-dataset patterns (concentration, duplication, engagement distributions) are reproducible; the claim that the population is "pod users" rests on the depositor's collection process.

Two names appear in the project's own metadata: the deposit description references the platform HyperClapper, while the source filename references Podawaa. Both are commercial engagement-pod products. Whether the dataset covers one platform, both, or a merged collection is an open provenance question tracked in [Limitations](limitations.md).

## Observed fact versus research classification

The method enforces a hard line between two kinds of statement:

- **Observation**: "This record shows 88,028 Likes and 0 Views." Anyone can verify this against the file.
- **Classification**: "This account participated in coordinated engagement." This is an interpretation that requires evidence beyond the published fields.

The published dataset contains observations only. It contains no per-account classification field, no confidence score, and no verdict. Every analysis script in this repository outputs statistical flags (ratio anomalies, cross-account duplicate clusters, concentration measures) and explicitly does not output judgments about individuals. Turning a flag into a classification is an analyst's step, and it must be documented with its own evidence tier when anyone takes it.

## Analysis methodology

Four stdlib-only scripts regenerate every figure this project publishes:

| Script | What it computes | Evidence tier of output |
|---|---|---|
| `profile_dataset.py` | Full baseline profile: counts, completeness, distributions, checksum | VERIFIED |
| `engagement_anomalies.py` | Records whose like-to-view ratio exceeds a chosen threshold | VERIFIED (the ratio), INFERENCE (any interpretation) |
| `author_concentration.py` | Per-author volume, engagement, and internal duplication aggregates | VERIFIED |
| `duplicate_content.py` | Exact-text clusters spanning two or more author identifiers | VERIFIED (the cluster), INFERENCE (coordination) |
| `decode_timestamps.py` | Approximate post dates decoded from LinkedIn activity IDs | INFERENCE |

Threshold choices are parameters, not baked-in conclusions. One analyst can flag ratios above 0.5, another above 0.9. Both work from the same file and the same code, which is the point: a skeptical researcher should be able to disagree with the original analysis without rebuilding the research environment from scratch.

## Timestamp decoding

LinkedIn activity IDs encode a millisecond Unix timestamp in the upper 41 bits (`id >> 22`). This is a widely documented community technique, not a platform guarantee, so all decoded dates carry the INFERENCE tier. Decoded dates for this dataset span July 2018 to November 2024, with more than 95 percent of records falling in 2021 through 2024.

## Verification trail

- The source file's SHA256 is recorded in [checksums/CHECKSUMS.txt](https://github.com/PolymathWizard/SPOTAPOD/blob/main/checksums/CHECKSUMS.txt). Download the file from Dataverse, hash it, and compare before running anything.
- The baseline profile is a generated artifact. Its generation-time hash is recorded in `checksums/derived.json`, and CI fails if the committed profile diverges from that hash (the drift gate). Derived artifacts are generated, never hand edited.
- The BHIL evidence archive assigns each original observation a source identifier and a SHA256 hash. Published findings can point back to those identifiers without releasing the source material. If a finding is challenged, the original record is compared against the recorded hash.

## Versioning

Dataset versions live on Dataverse with DOI-level version history. Companion versions live in this repository's [CHANGELOG](https://github.com/PolymathWizard/SPOTAPOD/blob/main/CHANGELOG.md) and git history. Corrections flow through the process in [Corrections](corrections.md) and appear in both histories.
