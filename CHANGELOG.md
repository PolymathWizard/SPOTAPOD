# Changelog

All notable changes to the SPOTAPOD companion repository. Dataset version history lives on the Harvard Dataverse record.

## 1.1.0, 2026-09-08

- BHIL brand visual layer: five drift-gated matplotlib charts generated from the source file (likes distribution, author concentration, posts by decoded year, like-to-view ratio, field completeness)
- Two authored SVG schema diagrams in the BHIL diagram register (publication architecture, observation versus classification evidence flow)
- Figure generator merges figure hashes into the derived manifest; hand edits to any chart fail CI
- Caption correction caught in QA: the 100 percent plus ratio band holds 2,619 records (2,500 with likes strictly above views plus 119 equal), and the figure now states both numbers

## 1.0.0, 2026-09-08

- Initial public release of the companion repository
- Baseline profile generated from dataset v1 (source SHA256 2d64e4b2...)
- Method, data dictionary, limitations, ethics, research questions, use cases, FAQ, correction process
- Stdlib-only analysis suite: profiler, engagement anomalies, author concentration, duplicate content, timestamp decoder
- Gates: dash validator, drift gate, repo conformance validator, six named-bug regression tests
- Open correction items C-001 (49K versus 213K count discrepancy), C-002 (HyperClapper versus Podawaa naming), C-003 (3,364 records missing post IDs)
