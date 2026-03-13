---
title: "GOLD NFP Reaction (2026-02-11): T+1/T+7 Up Probability"
description: "Historical probability profile for GOLD around NFP events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 1
title_template_key: "nfp_1"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2026-02-11"
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
quality_score: 90
sample_size: 35
freshness_days: 29
freshness_status: "fresh"
index_tier: "A"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 1.53
hub_baseline_median_t7: 1.31
hub_baseline_std_t7: 1.9626
hub_baseline_delta: -2.99
z_score_t7: -1.64
percentile_t7: 2.86
narrative_trigger: "extreme_underperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "negative"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/gold-after-nfp-2026-02-11"
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
  sharpe_t7: -4.16
  mdd_t7: -3.72
  volatility: 32.81
  impact_t1_pct: -2.92
  impact_t7_pct: -1.68
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
chartData: [{"time": "2026-02-09", "open": 5017.4, "high": 5065.7, "low": 4979.1, "close": 5050.9}, {"time": "2026-02-10", "open": 5013.5, "high": 5029.0, "low": 5002.7, "close": 5003.8}, {"time": "2026-02-11", "open": 5049.9, "high": 5111.3, "low": 5041.3, "close": 5071.6}, {"time": "2026-02-12", "open": 5060.4, "high": 5078.1, "low": 4892.0, "close": 4923.7}, {"time": "2026-02-13", "open": 4953.0, "high": 5043.9, "low": 4946.2, "close": 5022.0}, {"time": "2026-02-17", "open": 5020.0, "high": 5020.0, "low": 4847.8, "close": 4882.9}, {"time": "2026-02-18", "open": 4872.2, "high": 4987.0, "low": 4869.5, "close": 4986.5}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **GOLD**
- Event date: **2026-02-11**
- As-of date (T-1): **2026-03-12**
- Freshness age: **29 days**
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

This event should be read as a distribution problem, not a headline-only trade. GOLD around NFP is best framed through how the release landed lower than the previous release. The current observation shows actual value 158466.0000 versus previous 158558.0000, a delta of -92.0000. Across the full history, GOLD has a T+7 up probability of 77.14% versus 22.86% down, with a median return of 1.31%. When only matching the same event direction, the T+7 up probability shifts to 77.78% across 8 comparable releases, with a same-direction median of 2.07%. The current release therefore belongs to the downside tail and should be treated as materially weak. The standing hub thesis for this asset-event pair is: Gold often reacts inversely to payroll strength via rates repricing, but follow-through depends on whether labor surprise changes Fed expectations materially.

## Distribution Position

This window sits in the weak tail and should be classified as a downside tail event for GOLD after NFP. The current T+7 move of -1.68% carries a z-score of -1.64 and a percentile rank of 2.86, which pushes the release into the weakest decile of observed windows and away from ordinary downside noise. That makes this an extreme negative deviation rather than a routine weak print, so the page should be read with explicit downside-tail caution.

## Comparison vs Hub Baseline

This comparison is materially below baseline and should be treated as a true downside-tail gap. Against the hub baseline for this asset-event pair, the current print is measurable rather than anecdotal. The hub baseline median T+7 return is 1.31% and the current gap is -2.99%. Same-direction probability differs by +0.64% and the same-direction median differs by +0.76%. The baseline gap is now large enough to justify a weak-tail classification and a more defensive interpretation. The current regime context also matters: Macro headline digestion has become faster, shortening reaction windows.

## Failure Modes

The failure mode here is underestimating how far a downside tail can travel before it stabilizes. The main failure mode is confusing distribution evidence with certainty. Revisions and unemployment-rate cross-signals can flip initial direction. Invalidation needs to be tighter because weak-tail conditions can extend farther than a normal weak window.

## Execution Relevance

Use this page as an educational operating lens, not a trading instruction. The operational takeaway is to respect the downside tail and accept a higher invalidation burden before assuming the move is spent. The checklist remains Evaluate headline payroll plus revisions together.; Wait for rate market confirmation before adding size.; Use staggered exits around key session levels.. This is exactly the state where waiting for confirmation matters more than trying to fade weakness too early.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
