# Changelog

All notable changes to the SPOTAPOD companion repository. Dataset version history lives on the Harvard Dataverse record.

## 1.3.1, 2026-09-08

- README: Interactive Explorer section with description and a new authored graphic in the BHIL diagram register (docs/figures/diagram-explorer.svg), mirrored on the docs site and the explorer guide

## 1.3.0, 2026-09-08

- Explorer v2: global author and keyword filters applied to every panel, with click-to-focus on any author identifier in tables and charts
- Likes against Views scatter on log-log axes (canvas): likes-equal-views impossibility line, median-ratio line of the current view, per-record hover detail, deterministic sampling above 14,000 points
- Top 20 authors by records and top 20 posts by likes, horizontal bar charts recomputed over the filtered view
- Record browser replaces plain content search (filters now cover keyword search globally)
- Filter logic verified against the Python baselines: unfiltered counts match exactly, single-author counts match known values

## 1.2.0, 2026-09-08

- Interactive explorer: single-file offline HTML tool (explorer/spotapod-explorer.html) with in-browser SHA256 verification against the v1 checksum before analysis
- Panels: overview, likes distribution, ratio lab with threshold and minimum-Views sliders, decoded timeline, author aggregates with search, cross-account duplicate clusters, content search
- Posture carried into the UI: per-panel evidence tier chips, STATED population label pinned in the status bar, empty flag results report INCONCLUSIVE
- Ships with no data inside; loads the user's own Dataverse download locally, nothing leaves the machine
- Explorer JS logic verified against the Python baselines (record, author, ratio-subset, and year counts match exactly)
- Dash gate extended to scan .html files

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
