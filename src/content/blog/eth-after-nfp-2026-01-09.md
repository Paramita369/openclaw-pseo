---
title: "ETH After NFP (2026-01-09): Event Probability and Median Return"
description: "Historical probability profile for ETH around NFP events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 3
title_template_key: "nfp_3"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2026-01-09"
asof_date: "2026-03-12"
source: "verified_targets.csv"
offer_key: "binance"
signal: "Neutral"
raw_signal_score: 5.14
robust_score: -0.86
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 100
sample_size: 35
freshness_days: 62
freshness_status: "stale"
index_tier: "B"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 2.74
hub_baseline_median_t7: 1.98
hub_baseline_std_t7: 9.6006
hub_baseline_delta: 4.91
z_score_t7: 0.43
percentile_t7: 68.57
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/eth-after-nfp-2026-01-09"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-13T09:46:21+00:00"
event_direction: "up"
event_actual: 158558.0
event_previous: 158432.0
event_delta: 126.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["eth", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: -0.02
  volatility: 57.87
  impact_t1_pct: -0.02
  impact_t7_pct: 6.89
probabilities:
  sample_size: 35
  t1:
    up: 48.57
    down: 51.43
    median: -0.02
    mean: -0.16
    sample: 35
  t7:
    up: 57.14
    down: 42.86
    median: 1.98
    mean: 2.74
    sample: 35
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 26
    t1:
      up: 46.15
      down: 53.85
      median: -0.05
      mean: -0.07
      sample: 26
    t7:
      up: 53.85
      down: 46.15
      median: 2.43
      mean: 2.98
      sample: 26
related_events: [{"slug": "eth-after-nfp-2025-11-20", "title": "ETH After NFP (2025-11-20): Historical T+1/T+7 Probability", "event_date": "2025-11-20", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 6.45, "sample_size": 0}, {"slug": "eth-after-nfp-2025-09-05", "title": "ETH After NFP (2025-09-05): Historical T+1/T+7 Probability", "event_date": "2025-09-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 9.48, "sample_size": 0}, {"slug": "eth-after-nfp-2025-08-01", "title": "ETH After NFP (2025-08-01): Historical T+1/T+7 Probability", "event_date": "2025-08-01", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 14.95, "sample_size": 0}]
chartData: [{"time": "2026-01-06", "open": 3226.12, "high": 3303.56, "low": 3184.01, "close": 3295.95}, {"time": "2026-01-07", "open": 3295.91, "high": 3296.39, "low": 3126.55, "close": 3166.84}, {"time": "2026-01-08", "open": 3166.92, "high": 3179.87, "low": 3052.51, "close": 3104.38}, {"time": "2026-01-09", "open": 3104.33, "high": 3140.71, "low": 3058.1, "close": 3083.05}, {"time": "2026-01-10", "open": 3083.17, "high": 3099.17, "low": 3075.14, "close": 3082.4}, {"time": "2026-01-11", "open": 3082.41, "high": 3141.96, "low": 3080.75, "close": 3118.89}, {"time": "2026-01-12", "open": 3118.83, "high": 3166.22, "low": 3068.07, "close": 3092.33}, {"time": "2026-01-13", "open": 3092.01, "high": 3352.58, "low": 3088.51, "close": 3322.1}, {"time": "2026-01-14", "open": 3322.19, "high": 3397.9, "low": 3280.38, "close": 3354.72}, {"time": "2026-01-15", "open": 3354.77, "high": 3382.45, "low": 3276.82, "close": 3317.1}, {"time": "2026-01-16", "open": 3317.34, "high": 3325.25, "low": 3251.81, "close": 3295.48}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **ETH**
- Event date: **2026-01-09**
- As-of date (T-1): **2026-03-12**
- Freshness age: **62 days**
- Sample size (all-history): **35**

## Event Outcome

- NFP Outcome: **UP** (Actual 158558.0, Previous 158432.0, Delta +126.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 48.57% | 51.43% | -0.02% | -0.16% | 35 |
| T+7 | 57.14% | 42.86% | 1.98% | 2.74% | 35 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 46.15% | 53.85% | -0.05% | -0.07% | 26 |
| T+7 | 53.85% | 46.15% | 2.43% | 2.98% | 26 |

## Event Outcome Interpretation

This event should be read as a distribution problem, not a headline-only trade. ETH around NFP is best framed through how the release landed higher than the previous release. The current observation shows actual value 158558.0000 versus previous 158432.0000, a delta of +126.0000. Across the full history, ETH has a T+7 up probability of 57.14% versus 42.86% down, with a median return of 1.98%. When only matching the same event direction, the T+7 up probability shifts to 53.85% across 26 comparable releases, with a same-direction median of 2.43%. The current release therefore reads as a calibration event inside the median band, not as a high-conviction break. The standing hub thesis for this asset-event pair is: ETH has historically shown mixed first-day response to payroll shocks, but directional follow-through improves when dollar trend aligns with crypto market breadth.

## Distribution Position

This window sits in the median band and should be used for calibration rather than conviction. The current T+7 move of 6.89% carries a z-score of 0.43 and a percentile rank of 68.57, which keeps the release inside the central band of observed windows. That is exactly what a strict median norm looks like: neither extreme strength nor extreme weakness, just a normal response range that helps calibrate expectations. The key instruction here is simple: do not overstate what is still a routine macro window.

## Comparison vs Hub Baseline

This comparison stays close to the median band and is best used for calibration. Against the hub baseline for this asset-event pair, the current print is measurable rather than anecdotal. The hub baseline median T+7 return is 1.98% and the current gap is +4.91%. Same-direction probability moves by -3.29% and the same-direction median differs by +0.45%. Those numbers matter because they show where normal variation ends, not because they justify an outsized story. The current regime context also matters: Cross-exchange depth has improved, reducing single-venue distortion.

## Failure Modes

The failure mode here is over-reading ordinary data as if it were exceptional. The main failure mode is confusing distribution evidence with certainty. Thin weekend-adjacent liquidity can produce false breaks. Median-band releases often produce the worst decisions when operators insist on finding a dramatic narrative where the distribution is actually telling them to stay measured.

## Execution Relevance

Use this page as an educational operating lens, not a trading instruction. The operational takeaway is calibration, not escalation. The checklist remains Validate move with ETH perp funding and open interest.; Use smaller first entry and add on confirmation.; Monitor ETH/BTC and TOTAL3 for breadth confirmation.. When a page is marked strict median norm, the right move is to compare it against the hub, keep sizing conservative, and do not overstate the evidence.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
