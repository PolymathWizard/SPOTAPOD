# Research Questions

Questions this dataset can support, questions it can only partially support, and questions it cannot answer no matter how hard it is squeezed. Each question notes the fields involved, the method, and the evidence ceiling (the strongest tier an answer can carry).

## Fully answerable from the file (ceiling: VERIFIED)

**Q1. What does the engagement distribution of pod-associated posts look like?**
Fields: Likes, Views. Method: distribution analysis on the full corpus and the Views > 0 subset. The heavy tail (median 57 likes, p99 2,190, max 215,818) is itself a finding: most pod-associated posts still perform modestly.

**Q2. How concentrated is posting volume?**
Fields: AuthorPublicIdentifier. Method: `author_concentration.py`. Baseline: 438 authors have 100 or more records, the top 100 authors account for 20.9 percent of all records, and 1,409 authors appear exactly once. Concentration curves distinguish habitual heavy users from incidental captures.

**Q3. How much exact text reuse crosses account boundaries?**
Fields: Content, AuthorPublicIdentifier. Method: `duplicate_content.py`. 26,098 records share identical non-empty text with another record. Clusters spanning many distinct authors are candidates for template or coordination analysis.

**Q4. What are the linguistic characteristics of pod-associated content?**
Fields: Content. Method: language identification, hashtag density, length distributions, emoji usage, call-to-action phrasing ("Agree?", "Hit the bell"). The corpus is strongly multilingual, which itself challenges the assumption that engagement manipulation is an anglophone phenomenon.

**Q5. How do engagement ratios distribute, and where are the anomalies?**
Fields: Likes, Views (Views > 0 subset, 118,848 records). Method: `engagement_anomalies.py` at analyst-chosen thresholds. Median ratio 0.058; 5,655 records exceed 0.5; 2,500 exceed 1.0. Publish thresholds and let readers pick their own.

## Answerable with inference steps (ceiling: INFERENCE)

**Q6. How did pod-associated posting volume change over time?**
Method: decode dates from post IDs. The 2020 to 2024 growth curve (4,396 to 62,906 records per year) is decodable, but it confounds phenomenon growth with collection-effort growth. State both readings.

**Q7. Do heavy posters show different engagement signatures than light posters?**
Method: join Q2 aggregates with Q5 ratios. Differences are computable; attributing them to pod mechanics rather than account maturity or audience size is inference.

**Q8. Are there temporal bursts consistent with coordinated campaigns?**
Method: decoded dates plus duplicate clusters. Same-text posts with tightly clustered decoded timestamps across many accounts are the strongest coordination signal available inside this file.

**Q9. What share of records look like recapture artifacts versus distinct posts?**
Method: duplicate post-ID analysis, counter-drift comparison between copies. Useful for anyone building cleaning pipelines on top of the file.

## Not answerable from this file alone (requires external data)

**Q10. Does pod usage actually inflate engagement, and by how much?**
Requires a control population of comparable non-pod accounts. The single most valuable companion dataset anyone could build.

**Q11. Which specific accounts violated 16 CFR Part 465?**
A legal determination requiring intent, commercial context, and adjudication. Out of scope for any dataset.

**Q12. Are these accounts still active, and did behavior change after the FTC rule took effect in October 2024?**
Requires fresh observation. The file's decoded dates end November 2024, offering only a one-month post-rule window, too thin for before-and-after claims.

**Q13. What did the pods themselves look like (membership, pricing, mechanics)?**
The file contains outputs, not the coordination layer. Platform-side research is a separate project with its own ethics review.

**Q14. How representative is this sample of pod usage overall?**
Unanswerable without knowing the collection method's coverage and error rates. See [Limitations](limitations.md), items 1 and 10.

## Questions to ask before trusting any analysis built on this data

1. Did the analysis deduplicate on post ID, and does it say so?
2. Did it treat zero Views as missing or as observed zero?
3. Did it carry the STATED tier on the population definition, or silently upgrade it?
4. Did it publish thresholds as parameters or bake them into conclusions?
5. Did it name individuals, and if so, on what evidence beyond inclusion in the file?
6. Can you regenerate its headline numbers from the scripts in [analysis/](https://github.com/PolymathWizard/SPOTAPOD/tree/main/analysis)?

An analysis that fails question 6 is asking for trust. This project's standard is inspection.
