---
title: "US CPI (2025-12-12) and SPY: Event-Driven Return Odds"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
pubDate: "2026-03-11"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-12-12"
asof_date: "2026-03-10"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 15.44
robust_score: 9.44
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 39
freshness_days: 88
freshness_status: "stale"
index_tier: "B"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 0.21
hub_baseline_median_t7: 0.51
hub_baseline_std_t7: 1.714
hub_baseline_delta: -0.39
z_score_t7: -0.05
percentile_t7: 42.11
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/spy-after-cpi-2025-12-12"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 326.031
event_previous: 325.063
event_delta: 0.968
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.46
  mdd_t7: -0.15
  volatility: 0.27
  impact_t1_pct: -0.15
  impact_t7_pct: 0.12
probabilities:
  sample_size: 39
  t1:
    up: 64.1
    down: 35.9
    median: 0.16
    mean: 0.21
    sample: 39
  t7:
    up: 68.42
    down: 31.58
    median: 0.51
    mean: 0.21
    sample: 38
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 38
    t1:
      up: 63.16
      down: 36.84
      median: 0.14
      mean: 0.21
      sample: 38
    t7:
      up: 68.42
      down: 31.58
      median: 0.51
      mean: 0.21
      sample: 38
related_events: [{"slug": "spy-after-cpi-2024-03-12", "title": "SPY CPI Win Rate (2024-03-12): Historical T+1/T+7 Probability", "event_date": "2024-03-12", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 3.94, "median_t7_pct": 0.51, "sample_size": 39}, {"slug": "spy-after-cpi-2024-11-14", "title": "2024-11-14 CPI Release: SPY Directional Probability Snapshot", "event_date": "2024-11-14", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 0.43, "median_t7_pct": 0.51, "sample_size": 39}, {"slug": "spy-after-cpi-2024-05-15", "title": "2024-05-15 CPI Release: SPY Directional Probability Snapshot", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 0.37, "median_t7_pct": 0.51, "sample_size": 39}]
chartData: [{"time": "2025-12-09", "open": 681.14, "high": 683.37, "low": 680.58, "close": 681.03}, {"time": "2025-12-10", "open": 680.55, "high": 686.94, "low": 679.3, "close": 685.54}, {"time": "2025-12-11", "open": 683.12, "high": 687.22, "low": 680.16, "close": 687.14}, {"time": "2025-12-12", "open": 686.14, "high": 686.85, "low": 677.17, "close": 679.75}, {"time": "2025-12-15", "open": 683.72, "high": 683.74, "low": 677.25, "close": 678.72}, {"time": "2025-12-16", "open": 677.23, "high": 679.07, "low": 672.99, "close": 676.87}, {"time": "2025-12-17", "open": 677.89, "high": 678.44, "low": 669.22, "close": 669.42}, {"time": "2025-12-18", "open": 675.6, "high": 678.73, "low": 672.91, "close": 674.48}, {"time": "2025-12-19", "open": 676.59, "high": 681.09, "low": 676.47, "close": 680.59}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
- Event date: **2025-12-12**
- As-of date (T-1): **2026-03-10**
- Freshness age: **88 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 326.031, Previous 325.063, Delta +0.9680)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 64.1% | 35.9% | 0.16% | 0.21% | 39 |
| T+7 | 68.42% | 31.58% | 0.51% | 0.21% | 38 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 63.16% | 36.84% | 0.14% | 0.21% | 38 |
| T+7 | 68.42% | 31.58% | 0.51% | 0.21% | 38 |

## Event Outcome Interpretation

Execution quality here comes from context discipline rather than reacting to the first candle. SPY around CPI is best framed through how the release landed higher than the previous release. The current observation shows actual value 326.0310 versus previous 325.0630, a delta of +0.9680. Across the full history, SPY has a T+7 up probability of 68.42% versus 31.58% down, with a median return of 0.51%. When only matching the same event direction, the T+7 up probability shifts to 68.42% across 38 comparable releases, with a same-direction median of 0.51%. The current release therefore reads as a calibration event inside the median band, not as a high-conviction break. The standing hub thesis for this asset-event pair is: SPY reacts to CPI through broad risk-premium repricing; downside inflation surprises often support index breadth while upside shocks compress valuation multiples.

## Distribution Position

This window sits in the median band and should be used for calibration rather than conviction. The current T+7 move of 0.12% carries a z-score of -0.05 and a percentile rank of 42.11, which keeps the release inside the central band of observed windows. That is exactly what a strict median norm looks like: neither extreme strength nor extreme weakness, just a normal response range that helps calibrate expectations. The key instruction here is simple: do not overstate what is still a routine macro window.

## Comparison vs Hub Baseline

This comparison stays close to the median band and is best used for calibration. The baseline comparison is what turns the page from observation into a repeatable checklist. The hub baseline median T+7 return is 0.51% and the current gap is -0.39%. Same-direction probability moves by +0.00% and the same-direction median differs by +0.00%. Those numbers matter because they show where normal variation ends, not because they justify an outsized story. The current regime context also matters: Sector rotation speed has accelerated in the post-tightening phase.

## Failure Modes

The failure mode here is over-reading ordinary data as if it were exceptional. The main failure mode is skipping confirmation steps because the headline feels obvious. Energy and healthcare moves can offset index-level signal clarity. Median-band releases often produce the worst decisions when operators insist on finding a dramatic narrative where the distribution is actually telling them to stay measured.

## Execution Relevance

Treat this page as an execution checklist input, not a buy or sell signal. The operational takeaway is calibration, not escalation. The checklist remains Track breadth (advance/decline) with index move.; Compare rate-sensitive sectors versus defensives.; Use predefined stop distance from event range.. When a page is marked strict median norm, the right move is to compare it against the hub, keep sizing conservative, and do not overstate the evidence.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
