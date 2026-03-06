---
title: "US CPI (2026-02-12) and GOLD: Event-Driven Return Odds"
description: "Historical probability profile for GOLD around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2026-02-12"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 15.46
robust_score: 15.46
penalties:
  sample: 0.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 70
sample_size: 14
freshness_days: 21
freshness_status: "fresh"
index_tier: "B"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "analyst"
hub_baseline_mean_t7: 1.07
hub_baseline_median_t7: 1.52
hub_baseline_std_t7: 1.8614
hub_baseline_delta: -0.45
z_score_t7: 0.0
percentile_t7: 46.15
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/gold-after-cpi-2026-02-12"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "up"
event_actual: 326.588
event_previous: 326.031
event_delta: 0.557
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["gold", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 1.26
  mdd_t7: 0.0
  volatility: 0.85
  impact_t1_pct: 0.22
  impact_t7_pct: 1.07
probabilities:
  sample_size: 14
  t1:
    up: 50.0
    down: 50.0
    median: 0.27
    mean: 0.22
    sample: 14
  t7:
    up: 76.92
    down: 23.08
    median: 1.52
    mean: 1.07
    sample: 13
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 13
    t1:
      up: 53.85
      down: 46.15
      median: 0.56
      mean: 0.36
      sample: 13
    t7:
      up: 76.92
      down: 23.08
      median: 1.52
      mean: 1.07
      sample: 13
related_events: [{"slug": "gold-after-cpi-2025-02-12", "title": "US CPI (2025-02-12) and GOLD: Event-Driven Return Odds", "event_date": "2025-02-12", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 7.09, "median_t7_pct": 1.52, "sample_size": 14}, {"slug": "gold-after-cpi-2024-02-20", "title": "US CPI (2024-02-20) and GOLD: Event-Driven Return Odds", "event_date": "2024-02-20", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 6.12, "median_t7_pct": 1.52, "sample_size": 14}, {"slug": "gold-after-cpi-2024-05-15", "title": "US CPI (2024-05-15) and GOLD: Event-Driven Return Odds", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 0.47, "median_t7_pct": 1.52, "sample_size": 14}]
chartData: [{"time": "2026-02-09", "open": 5017.4, "high": 5065.7, "low": 4979.1, "close": 5050.9}, {"time": "2026-02-10", "open": 5013.5, "high": 5029.0, "low": 5002.7, "close": 5003.8}, {"time": "2026-02-11", "open": 5049.9, "high": 5111.3, "low": 5041.3, "close": 5071.6}, {"time": "2026-02-12", "open": 5060.4, "high": 5078.1, "low": 4892.0, "close": 4923.7}, {"time": "2026-02-13", "open": 4953.0, "high": 5043.9, "low": 4946.2, "close": 5022.0}, {"time": "2026-02-17", "open": 5020.0, "high": 5020.0, "low": 4847.8, "close": 4882.9}, {"time": "2026-02-18", "open": 4872.2, "high": 4987.0, "low": 4869.5, "close": 4986.5}, {"time": "2026-02-19", "open": 5014.7, "high": 5014.7, "low": 4975.9, "close": 4975.9}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **GOLD**
- Event date: **2026-02-12**
- As-of date (T-1): **2026-03-05**
- Freshness age: **21 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 326.588, Previous 326.031, Delta +0.5570)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 50.0% | 50.0% | 0.27% | 0.22% | 14 |
| T+7 | 76.92% | 23.08% | 1.52% | 1.07% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 53.85% | 46.15% | 0.56% | 0.36% | 13 |
| T+7 | 76.92% | 23.08% | 1.52% | 1.07% | 13 |

## Event Outcome Interpretation

This event should be read as a distribution problem, not a headline-only trade. GOLD around CPI is best framed through how the release landed higher than the previous release. The current observation shows actual value 326.5880 versus previous 326.0310, a delta of +0.5570. Across the full history, GOLD has a T+7 up probability of 76.92% versus 23.08% down, with a median return of 1.52%. When only matching the same event direction, the T+7 up probability shifts to 76.92% across 13 comparable releases, with a same-direction median of 1.52%. The current release therefore reads as a calibration event inside the median band, not as a high-conviction break. The standing hub thesis for this asset-event pair is: Gold's CPI behavior is primarily a real-yield and USD function; directional conviction increases when CPI surprise and Treasury move point the same way.

## Distribution Position

This window sits in the median band and should be used for calibration rather than conviction. The current T+7 move of 1.07% carries a z-score of 0.00 and a percentile rank of 46.15, which keeps the release inside the central band of observed windows. That is exactly what a strict median norm looks like: neither extreme strength nor extreme weakness, just a normal response range that helps calibrate expectations. The key instruction here is simple: do not overstate what is still a routine macro window.

## Comparison vs Hub Baseline

This comparison stays close to the median band and is best used for calibration. Against the hub baseline for this asset-event pair, the current print is measurable rather than anecdotal. The hub baseline median T+7 return is 1.52% and the current gap is -0.45%. Same-direction probability moves by +0.00% and the same-direction median differs by +0.00%. Those numbers matter because they show where normal variation ends, not because they justify an outsized story. The current regime context also matters: Safe-haven allocation has become more sensitive to policy-cut expectations.

## Failure Modes

The failure mode here is over-reading ordinary data as if it were exceptional. The main failure mode is confusing distribution evidence with certainty. Conflicting moves between yields and USD can produce range-bound noise. Median-band releases often produce the worst decisions when operators insist on finding a dramatic narrative where the distribution is actually telling them to stay measured.

## Execution Relevance

Use this page as an educational operating lens, not a trading instruction. The operational takeaway is calibration, not escalation. The checklist remains Read US10Y real yield change alongside DXY.; Prefer breakout only after direction confirms on both metrics.; Set position size by ATR-based risk budget.. When a page is marked strict median norm, the right move is to compare it against the hub, keep sizing conservative, and do not overstate the evidence.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
