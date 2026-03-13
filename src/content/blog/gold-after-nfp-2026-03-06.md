---
title: "2026-03-06 Nonfarm Payrolls: GOLD Historical Win Rate"
description: "Historical probability profile for GOLD around NFP events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 2
title_template_key: "nfp_2"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2026-03-06"
asof_date: "2026-03-12"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 19.66
robust_score: 19.66
penalties:
  sample: 0.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 80
sample_size: 35
freshness_days: 6
freshness_status: "fresh"
index_tier: "A"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 1.53
hub_baseline_median_t7: 1.31
hub_baseline_std_t7: 1.9626
hub_baseline_delta: -2.25
z_score_t7: -1.26
percentile_t7: 14.29
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/gold-after-nfp-2026-03-06"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-13T09:46:21+00:00"
event_direction: "down"
event_actual: 158466.0
event_previous: 158558.0
event_delta: -92.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -7.87
  mdd_t7: -1.06
  volatility: 0.12
  impact_t1_pct: -1.06
  impact_t7_pct: -0.94
probabilities:
  sample_size: 35
  t1:
    up: 63.64
    down: 36.36
    median: 0.39
    mean: 0.5
    sample: 22
  t7:
    up: 77.14
    down: 22.86
    median: 1.31
    mean: 1.53
    sample: 35
  conditional:
    basis: "event_direction"
    direction: "down"
    sample_size: 8
    t1:
      up: 62.5
      down: 37.5
      median: 0.54
      mean: 0.16
      sample: 8
    t7:
      up: 77.78
      down: 22.22
      median: 2.07
      mean: 1.64
      sample: 9
related_events: [{"slug": "gold-after-nfp-2026-01-02", "title": "GOLD After NFP (2026-01-02): Historical T+1/T+7 Probability", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 4.08, "sample_size": 0}, {"slug": "gold-after-nfp-2025-12-16", "title": "GOLD After NFP (2025-12-16): Historical T+1/T+7 Probability", "event_date": "2025-12-16", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 4.14, "sample_size": 0}, {"slug": "gold-after-nfp-2025-11-20", "title": "GOLD After NFP (2025-11-20): Historical T+1/T+7 Probability", "event_date": "2025-11-20", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 3.99, "sample_size": 0}]
chartData: [{"time": "2026-03-03", "open": 5298.7, "high": 5303.8, "low": 5023.0, "close": 5107.4}, {"time": "2026-03-04", "open": 5130.7, "high": 5180.2, "low": 5117.2, "close": 5120.2}, {"time": "2026-03-05", "open": 5169.5, "high": 5169.5, "low": 5054.7, "close": 5065.3}, {"time": "2026-03-06", "open": 5121.0, "high": 5146.1, "low": 5076.1, "close": 5146.1}, {"time": "2026-03-09", "open": 5155.0, "high": 5160.6, "low": 5077.7, "close": 5091.5}, {"time": "2026-03-10", "open": 5138.2, "high": 5229.7, "low": 5137.6, "close": 5229.7}, {"time": "2026-03-11", "open": 5190.8, "high": 5191.3, "low": 5167.4, "close": 5167.4}, {"time": "2026-03-12", "open": 5137.2, "high": 5137.2, "low": 5115.8, "close": 5115.8}, {"time": "2026-03-13", "open": 5084.0, "high": 5132.4, "low": 5066.0, "close": 5093.9}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **GOLD**
- Event date: **2026-03-06**
- As-of date (T-1): **2026-03-12**
- Freshness age: **6 days**
- Sample size (all-history): **35**

## Event Outcome

- NFP Outcome: **DOWN** (Actual 158466.0, Previous 158558.0, Delta -92.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 63.64% | 36.36% | 0.39% | 0.5% | 22 |
| T+7 | 77.14% | 22.86% | 1.31% | 1.53% | 35 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 62.5% | 37.5% | 0.54% | 0.16% | 8 |
| T+7 | 77.78% | 22.22% | 2.07% | 1.64% | 9 |

## Event Outcome Interpretation

The main mistake after macro releases is to treat every surprise as a regime break. GOLD around NFP is best framed through how the release landed lower than the previous release. The current observation shows actual value 158466.0000 versus previous 158558.0000, a delta of -92.0000. Across the full history, GOLD has a T+7 up probability of 77.14% versus 22.86% down, with a median return of 1.31%. When only matching the same event direction, the T+7 up probability shifts to 77.78% across 8 comparable releases, with a same-direction median of 2.07%. The current release therefore reads as a below-baseline and fragile response rather than a collapse. The standing hub thesis for this asset-event pair is: Gold often reacts inversely to payroll strength via rates repricing, but follow-through depends on whether labor surprise changes Fed expectations materially.

## Distribution Position

This window is below baseline and looks fragile rather than structurally broken. The current T+7 move of -0.94% carries a z-score of -1.26 and a percentile rank of 14.29, leaving the release in the lower quartile of observed windows. That puts the event on the weak side of normal without forcing it into a full downside tail label. The important distinction is that fragile reactions can still bounce, which is why a mild underperformance should not be confused with regime failure.

## Comparison vs Hub Baseline

This comparison is below baseline, but it is still better read as fragile than catastrophic. The baseline comparison matters because most false positives come from overreacting to ordinary noise. The hub baseline median T+7 return is 1.31% and the current gap is -2.25%. Same-direction probability differs by +0.64% and the same-direction median differs by +0.76%. The baseline gap is large enough to matter, but not large enough to imply that the broader playbook is broken. The current regime context also matters: Macro headline digestion has become faster, shortening reaction windows.

## Failure Modes

The failure mode here is reading a fragile window as proof of permanent weakness. The main failure mode is assuming the first interpretation will survive cross-asset confirmation. Revisions and unemployment-rate cross-signals can flip initial direction. Moderate underperformance often creates bounce risk, especially if rates or the dollar stop reinforcing the weak read.

## Execution Relevance

Treat this as an educational risk framework, not investment advice. The operational takeaway is to respect the below-baseline read without assuming collapse. The checklist is Evaluate headline payroll plus revisions together.; Wait for rate market confirmation before adding size.; Use staggered exits around key session levels.. Fragile setups demand tighter invalidation and more patience because bounce risk is often highest when traders treat every weak release as a one-way trend.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
