# Interactive Explorer

![SPOTAPOD Explorer](figures/diagram-explorer.svg)

A single-file, offline analysis tool for the SPOTAPOD dataset: [explorer/spotapod-explorer.html](https://github.com/PolymathWizard/SPOTAPOD/blob/main/explorer/spotapod-explorer.html) (download the raw file and open it in a desktop browser).

## How it works

1. Download `podawaa2024_fixed.json` from the Harvard Dataverse SPOTAPOD record.
2. Open the explorer HTML file locally. It works with the network off; nothing is uploaded anywhere.
3. Drop the JSON onto the page. The file is hashed in your browser and compared to the published v1 SHA256 before analysis begins. A mismatch is reported, never silently ignored.

## What it gives you

- Global filters: author identifier and keyword filters that drive every panel; click any author in a table or top-20 bar to focus on them
- Overview: the data-quality picture (null authors, missing IDs, zero-Views share) computed live from the records in view
- Likes against Views scatter: log-log canvas plot with the likes-equal-views impossibility line, the median-ratio line of the current view, and hover detail per record
- Likes distribution in the brand chart register
- Ratio lab: like-to-view anomaly flagging with the threshold and minimum-Views floor as sliders, because thresholds are parameters, not verdicts
- Timeline from decoded post IDs, labeled INFERENCE on the page itself
- Top 20 authors by records in view and top 20 posts by likes in view, as brand-register horizontal bar charts
- Author aggregates with a minimum-records slider
- Cross-account duplicate content clusters with adjustable minimum authors and text length
- Record browser sorted by likes over the current view

## Posture

Every panel carries its evidence tier chip. Flags are statistical anomalies at your chosen thresholds, not findings about people. An empty flag table reports INCONCLUSIVE, never a certification. The population label stays STATED in the status bar for the whole session.

The tool ships with no data inside it, so the repository republishes no personal identifiers; exploration happens on your own downloaded copy under the Dataverse record's terms of use.
