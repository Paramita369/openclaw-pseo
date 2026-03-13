---
title: "SPY After CPI (2026-02-13): Up/Down Odds and Median Returns"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 5
title_template_key: "cpi_5"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2026-02-13"
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
quality_score: 100
sample_size: 40
freshness_days: 27
freshness_status: "fresh"
index_tier: "A"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "distribution"
hub_baseline_mean_t7: 0.21
hub_baseline_median_t7: 0.51
hub_baseline_std_t7: 1.714
hub_baseline_delta: 0.62
z_score_t7: 0.54
percentile_t7: 71.05
narrative_trigger: "moderate_outperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "positive"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/spy-after-cpi-2026-02-13"
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
  sharpe_t7: 10.0
  mdd_t7: 0.0
  volatility: 6.69
  impact_t1_pct: 0.16
  impact_t7_pct: 1.13
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
related_events: [{"slug": "spy-after-cpi-2026-02-12", "title": "SPY After CPI (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 0.47, "sample_size": 0}, {"slug": "spy-after-cpi-2025-12-18", "title": "SPY After CPI (2025-12-18): Historical T+1/T+7 Probability", "event_date": "2025-12-18", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.35, "sample_size": 0}, {"slug": "spy-after-cpi-2025-10-12", "title": "SPY After CPI (2025-10-12): Historical T+1/T+7 Probability", "event_date": "2025-10-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.8, "sample_size": 0}]
chartData: [{"time": "2026-02-10", "open": 694.95, "high": 696.54, "low": 691.66, "close": 692.12}, {"time": "2026-02-11", "open": 696.39, "high": 697.14, "low": 689.18, "close": 691.96}, {"time": "2026-02-12", "open": 694.24, "high": 695.35, "low": 680.37, "close": 681.27}, {"time": "2026-02-13", "open": 681.69, "high": 686.28, "low": 677.52, "close": 681.75}, {"time": "2026-02-17", "open": 680.14, "high": 684.94, "low": 675.78, "close": 682.85}, {"time": "2026-02-18", "open": 684.02, "high": 689.15, "low": 682.83, "close": 686.29}, {"time": "2026-02-19", "open": 683.84, "high": 686.18, "low": 681.55, "close": 684.48}, {"time": "2026-02-20", "open": 682.32, "high": 690.06, "low": 681.73, "close": 689.43}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
- Event date: **2026-02-13**
- As-of date (T-1): **2026-03-12**
- Freshness age: **27 days**
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

The useful signal is where this release sits inside the historical range, not the headline in isolation. SPY around CPI is best framed through how the release landed higher than the previous release. The current observation shows actual value 327.4600 versus previous 326.5880, a delta of +0.8720. Across the full history, SPY has a T+7 up probability of 68.42% versus 31.58% down, with a median return of 0.51%. When only matching the same event direction, the T+7 up probability shifts to 68.42% across 38 comparable releases, with a same-direction median of 0.51%. The current release therefore reads as constructive and above baseline, but not as a full regime break. The standing hub thesis for this asset-event pair is: SPY reacts to CPI through broad risk-premium repricing; downside inflation surprises often support index breadth while upside shocks compress valuation multiples.

## Distribution Position

This window is above baseline and reads as constructive, positive but not extreme. The current T+7 move of 1.13% carries a z-score of 0.54 and a percentile rank of 71.05, placing the release in the central band of observed windows. That keeps the interpretation on the stronger side of normal without pushing it into tail language. The right read is that the event behaved better than usual, but not so far beyond baseline that it should be mistaken for a structural break.

## Comparison vs Hub Baseline

This comparison is above baseline, but it remains constructive rather than extreme. Relative to the hub baseline, this release can be located with a concrete distance from normal behavior. The hub baseline median T+7 return is 0.51% and the current gap is +0.62%. Same-direction probability is +0.00% versus all-history, and the same-direction median differs by +0.00%. That is enough to mark the page as positively skewed, while still requiring cross-asset confirmation before upgrading conviction. The current regime context also matters: Sector rotation speed has accelerated in the post-tightening phase.

## Failure Modes

The failure mode here is over-promoting a constructive setup into a false regime break. The main failure mode is forgetting that distributions absorb noise before they change shape. Energy and healthcare moves can offset index-level signal clarity. Moderate upside events often fail when secondary markets stop confirming, so the biggest mistake is ignoring the difference between above-baseline behavior and true tail behavior.

## Execution Relevance

Use this page as a distribution map, not a shortcut to conviction. The correct stance is to treat this as constructive but not extreme. The checklist is still Track breadth (advance/decline) with index move.; Compare rate-sensitive sectors versus defensives.; Use predefined stop distance from event range., and confirmation is still required before acting on the signal. Above-baseline pages deserve attention, but they do not eliminate the need for discipline.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
