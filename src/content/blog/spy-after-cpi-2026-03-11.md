---
title: "US CPI (2026-03-11) and SPY: Event-Driven Return Odds"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 3
title_template_key: "cpi_3"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2026-03-11"
asof_date: "2026-03-12"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 14.96
robust_score: 14.96
penalties:
  sample: 0.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 80
sample_size: 40
freshness_days: 1
freshness_status: "fresh"
index_tier: "A"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 0.21
hub_baseline_median_t7: 0.51
hub_baseline_std_t7: 1.714
hub_baseline_delta: -0.3
z_score_t7: 0.0
percentile_t7: 44.74
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/spy-after-cpi-2026-03-11"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-13T09:46:21+00:00"
event_direction: "up"
event_actual: 327.46
event_previous: 326.588
event_delta: 0.872
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 0.12
  mdd_t7: -1.52
  volatility: 1.73
  impact_t1_pct: -1.52
  impact_t7_pct: 0.21
probabilities:
  sample_size: 40
  t1:
    up: 62.5
    down: 37.5
    median: 0.14
    mean: 0.16
    sample: 40
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
      up: 61.54
      down: 38.46
      median: 0.13
      mean: 0.16
      sample: 39
    t7:
      up: 68.42
      down: 31.58
      median: 0.51
      mean: 0.21
      sample: 38
related_events: [{"slug": "spy-after-cpi-2026-02-13", "title": "SPY After CPI (2026-02-13): Historical T+1/T+7 Probability", "event_date": "2026-02-13", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.13, "sample_size": 0}, {"slug": "spy-after-cpi-2026-02-12", "title": "SPY After CPI (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 0.47, "sample_size": 0}, {"slug": "spy-after-cpi-2025-12-18", "title": "SPY After CPI (2025-12-18): Historical T+1/T+7 Probability", "event_date": "2025-12-18", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.35, "sample_size": 0}]
chartData: [{"time": "2026-03-09", "open": 666.39, "high": 679.92, "low": 662.39, "close": 678.27}, {"time": "2026-03-10", "open": 677.72, "high": 683.36, "low": 674.76, "close": 677.18}, {"time": "2026-03-11", "open": 677.58, "high": 680.08, "low": 673.34, "close": 676.33}, {"time": "2026-03-12", "open": 671.16, "high": 671.65, "low": 665.88, "close": 666.06}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
- Event date: **2026-03-11**
- As-of date (T-1): **2026-03-12**
- Freshness age: **1 days**
- Sample size (all-history): **40**

## Event Outcome

- CPI Outcome: **UP** (Actual 327.46, Previous 326.588, Delta +0.8720)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 62.5% | 37.5% | 0.14% | 0.16% | 40 |
| T+7 | 68.42% | 31.58% | 0.51% | 0.21% | 38 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 61.54% | 38.46% | 0.13% | 0.16% | 39 |
| T+7 | 68.42% | 31.58% | 0.51% | 0.21% | 38 |

## Event Outcome Interpretation

Execution quality here comes from context discipline rather than reacting to the first candle. SPY around CPI is best framed through how the release landed higher than the previous release. The current observation shows actual value 327.4600 versus previous 326.5880, a delta of +0.8720. Across the full history, SPY has a T+7 up probability of 68.42% versus 31.58% down, with a median return of 0.51%. When only matching the same event direction, the T+7 up probability shifts to 68.42% across 38 comparable releases, with a same-direction median of 0.51%. The current release therefore reads as a calibration event inside the median band, not as a high-conviction break. The standing hub thesis for this asset-event pair is: SPY reacts to CPI through broad risk-premium repricing; downside inflation surprises often support index breadth while upside shocks compress valuation multiples.

## Distribution Position

This window sits in the median band and should be used for calibration rather than conviction. The current T+7 move of 0.21% carries a z-score of 0.00 and a percentile rank of 44.74, which keeps the release inside the central band of observed windows. That is exactly what a strict median norm looks like: neither extreme strength nor extreme weakness, just a normal response range that helps calibrate expectations. The key instruction here is simple: do not overstate what is still a routine macro window.

## Comparison vs Hub Baseline

This comparison stays close to the median band and is best used for calibration. The baseline comparison is what turns the page from observation into a repeatable checklist. The hub baseline median T+7 return is 0.51% and the current gap is -0.30%. Same-direction probability moves by +0.00% and the same-direction median differs by +0.00%. Those numbers matter because they show where normal variation ends, not because they justify an outsized story. The current regime context also matters: Sector rotation speed has accelerated in the post-tightening phase.

## Failure Modes

The failure mode here is over-reading ordinary data as if it were exceptional. The main failure mode is skipping confirmation steps because the headline feels obvious. Energy and healthcare moves can offset index-level signal clarity. Median-band releases often produce the worst decisions when operators insist on finding a dramatic narrative where the distribution is actually telling them to stay measured.

## Execution Relevance

Treat this page as an execution checklist input, not a buy or sell signal. The operational takeaway is calibration, not escalation. The checklist remains Track breadth (advance/decline) with index move.; Compare rate-sensitive sectors versus defensives.; Use predefined stop distance from event range.. When a page is marked strict median norm, the right move is to compare it against the hub, keep sizing conservative, and do not overstate the evidence.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
