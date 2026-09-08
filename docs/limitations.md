# Limitations

A limitation statement does not weaken research. It defines the boundaries of what the evidence can support. Read this page before drawing any conclusion from the dataset, and especially before drawing any conclusion about an individual account.

## 1. The inclusion criterion is not verifiable from the file

**The central limitation.** The claim that these posts belong to accounts using engagement-pod tooling is STATED by the depositor. The records carry no pod-membership field, no collection log, and no extraction evidence. Within-dataset patterns are reproducible by anyone; the population definition is not. Any downstream work must carry this tier forward rather than silently upgrading "STATED pod users" to "confirmed pod users."

## 2. Metadata discrepancies

- The Dataverse description says 49,000 posts; the file contains 213,491 records. The description most plausibly refers to an earlier or different cut (UNCORROBORATED until the depositor clarifies).
- The description names the platform HyperClapper; the filename says Podawaa. Both are real engagement-pod products, but which population the file covers, or whether it merges several, is unresolved.
- Keyword metadata on the deposit ("Mafia," "Fake Socials") is descriptive framing, not a data field.

These discrepancies are logged in the [corrections queue](corrections.md) for depositor clarification.

## 3. Missing and null fields

- 23,894 records (11.2 percent) have no author identifier. Author-level analyses silently drop them.
- 3,364 records lack `linkedinPostId`, so they cannot be deduplicated by ID, date-decoded, or traced to a live post.
- 44.3 percent of records have zero Views, best treated as "not captured." Ratio analyses restricted to nonzero Views cover only 118,848 records, and that subset is not a random sample of the whole.

## 4. Recapture duplication

9,127 rows duplicate another row's post ID. Post-count statistics that skip deduplication overcount. Conversely, deduplication discards legitimate signal about counter movement between captures.

## 5. No temporal ground truth

The file has no collection timestamps. Post dates are decoded from activity IDs (INFERENCE) and describe when a post was created, not when it was observed or how long engagement had accumulated. Engagement counters from different records are snapshots at unknown, differing moments and are not directly comparable as rates.

## 6. Survivorship and visibility bias

Deleted posts, deleted accounts, private accounts, and LinkedIn visibility rules all shape what could be captured. The dataset over-represents content that stayed public long enough to be observed.

## 7. Language and geography

Roughly three quarters of sampled content contains non-ASCII text; French, Spanish, and other languages are heavily represented. Any English-only analysis covers a biased slice. No geographic fields exist, so regional claims cannot be supported at all.

## 8. Engagement counters cannot prove manipulation per record

High likes, high ratios, and even Likes exceeding Views are anomalies relative to expectations, not per-record proof. Capture artifacts, viral outliers, and platform counting quirks all produce the same surface signal. Manipulation findings require converging evidence: coordination patterns across accounts, timing clusters, text reuse, and ideally external corroboration.

## 9. No control population

The dataset contains only the treated population. Without a matched sample of comparable accounts not flagged as pod users, effect-size questions ("how much does pod usage inflate engagement?") cannot be answered from this file alone. Building a defensible control sample is the highest-value companion project; see [Research questions](research-questions.md).

## 10. Classification error, both directions

If the depositor's collection process had false positives, some accounts in this dataset never used pod tooling. If it had false negatives, the population understates the phenomenon. Neither rate is currently estimable. This is why no per-account verdicts are published, why the correction process exists, and why absence of anomaly is always reported as INCONCLUSIVE, never CLEAN.
