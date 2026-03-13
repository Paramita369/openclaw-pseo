---
title: "GOLD CPI Win Rate (2026-01-13): Historical T+1/T+7 Probability"
description: "Historical probability profile for GOLD around CPI events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 1
title_template_key: "cpi_1"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2026-01-13"
asof_date: "2026-03-12"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 17.98
robust_score: 11.98
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 100
sample_size: 40
freshness_days: 58
freshness_status: "stale"
index_tier: "B"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 1.49
hub_baseline_median_t7: 1.4
hub_baseline_std_t7: 2.4218
hub_baseline_delta: 2.31
z_score_t7: 0.92
percentile_t7: 84.21
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/gold-after-cpi-2026-01-13"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-13T09:46:21+00:00"
event_direction: "up"
event_actual: 326.588
event_previous: 326.031
event_delta: 0.557
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 10.0
  mdd_t7: -0.82
  volatility: 29.89
  impact_t1_pct: 0.81
  impact_t7_pct: 3.71
probabilities:
  sample_size: 40
  t1:
    up: 55.0
    down: 45.0
    median: 0.32
    mean: 0.27
    sample: 40
  t7:
    up: 78.95
    down: 21.05
    median: 1.4
    mean: 1.49
    sample: 38
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 38
    t1:
      up: 56.41
      down: 43.59
      median: 0.34
      mean: 0.31
      sample: 39
    t7:
      up: 78.95
      down: 21.05
      median: 1.4
      mean: 1.49
      sample: 38
related_events: [{"slug": "gold-after-cpi-2026-01-12", "title": "GOLD After CPI (2026-01-12): Historical T+1/T+7 Probability", "event_date": "2026-01-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 3.37, "sample_size": 0}, {"slug": "gold-after-cpi-2025-12-18", "title": "GOLD After CPI (2025-12-18): Historical T+1/T+7 Probability", "event_date": "2025-12-18", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 4.37, "sample_size": 0}, {"slug": "gold-after-cpi-2025-12-12", "title": "GOLD After CPI (2025-12-12): Historical T+1/T+7 Probability", "event_date": "2025-12-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.43, "sample_size": 0}]
chartData: [{"time": "2026-01-12", "open": 4579.1, "high": 4620.0, "low": 4577.8, "close": 4604.3}, {"time": "2026-01-13", "open": 4578.6, "high": 4617.1, "low": 4578.6, "close": 4589.2}, {"time": "2026-01-14", "open": 4610.3, "high": 4635.0, "low": 4608.2, "close": 4626.3}, {"time": "2026-01-15", "open": 4612.9, "high": 4616.3, "low": 4612.9, "close": 4616.3}, {"time": "2026-01-16", "open": 4608.0, "high": 4608.0, "low": 4588.4, "close": 4588.4}, {"time": "2026-01-20", "open": 4662.2, "high": 4764.0, "low": 4661.8, "close": 4759.6}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **GOLD**
- Event date: **2026-01-13**
- As-of date (T-1): **2026-03-12**
- Freshness age: **58 days**
- Sample size (all-history): **40**

## Event Outcome

- CPI Outcome: **UP** (Actual 326.588, Previous 326.031, Delta +0.5570)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.0% | 45.0% | 0.32% | 0.27% | 40 |
| T+7 | 78.95% | 21.05% | 1.4% | 1.49% | 38 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 56.41% | 43.59% | 0.34% | 0.31% | 39 |
| T+7 | 78.95% | 21.05% | 1.4% | 1.49% | 38 |

## Event Outcome Interpretation

This event should be read as a distribution problem, not a headline-only trade. GOLD around CPI is best framed through how the release landed higher than the previous release. The current observation shows actual value 326.5880 versus previous 326.0310, a delta of +0.5570. Across the full history, GOLD has a T+7 up probability of 78.95% versus 21.05% down, with a median return of 1.40%. When only matching the same event direction, the T+7 up probability shifts to 78.95% across 38 comparable releases, with a same-direction median of 1.40%. The current release therefore reads as constructive and above baseline, but not as a full regime break. The standing hub thesis for this asset-event pair is: Gold's CPI behavior is primarily a real-yield and USD function; directional conviction increases when CPI surprise and Treasury move point the same way.

## Distribution Position

This window is above baseline and reads as constructive, positive but not extreme. The current T+7 move of 3.71% carries a z-score of 0.92 and a percentile rank of 84.21, placing the release in the upper quartile of observed windows. That keeps the interpretation on the stronger side of normal without pushing it into tail language. The right read is that the event behaved better than usual, but not so far beyond baseline that it should be mistaken for a structural break.

## Comparison vs Hub Baseline

This comparison is above baseline, but it remains constructive rather than extreme. Against the hub baseline for this asset-event pair, the current print is measurable rather than anecdotal. The hub baseline median T+7 return is 1.40% and the current gap is +2.31%. Same-direction probability is +0.00% versus all-history, and the same-direction median differs by +0.00%. That is enough to mark the page as positively skewed, while still requiring cross-asset confirmation before upgrading conviction. The current regime context also matters: Safe-haven allocation has become more sensitive to policy-cut expectations.

## Failure Modes

The failure mode here is over-promoting a constructive setup into a false regime break. The main failure mode is confusing distribution evidence with certainty. Conflicting moves between yields and USD can produce range-bound noise. Moderate upside events often fail when secondary markets stop confirming, so the biggest mistake is ignoring the difference between above-baseline behavior and true tail behavior.

## Execution Relevance

Use this page as an educational operating lens, not a trading instruction. The correct stance is to treat this as constructive but not extreme. The checklist is still Read US10Y real yield change alongside DXY.; Prefer breakout only after direction confirms on both metrics.; Set position size by ATR-based risk budget., and confirmation is still required before acting on the signal. Above-baseline pages deserve attention, but they do not eliminate the need for discipline.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
