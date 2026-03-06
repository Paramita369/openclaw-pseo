---
title: "SPY Reaction to US CPI (2026-02-12): Quant Probability Breakdown"
description: "Historical probability profile for SPY around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 2
title_template_key: "cpi_2"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2026-02-12"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 19.75
robust_score: 19.75
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
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.51
hub_baseline_median_t7: 1.08
hub_baseline_std_t7: 1.8429
hub_baseline_delta: -0.57
z_score_t7: 0.0
percentile_t7: 46.15
narrative_trigger: "within_historical_norm"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/spy-after-cpi-2026-02-12"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "up"
event_actual: 326.588
event_previous: 326.031
event_delta: 0.557
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 2.04
  mdd_t7: 0.0
  volatility: 0.25
  impact_t1_pct: 0.26
  impact_t7_pct: 0.51
probabilities:
  sample_size: 14
  t1:
    up: 64.29
    down: 35.71
    median: 0.15
    mean: 0.26
    sample: 14
  t7:
    up: 76.92
    down: 23.08
    median: 1.08
    mean: 0.51
    sample: 13
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 13
    t1:
      up: 61.54
      down: 38.46
      median: 0.09
      mean: 0.26
      sample: 13
    t7:
      up: 76.92
      down: 23.08
      median: 1.08
      mean: 0.51
      sample: 13
related_events: [{"slug": "spy-after-cpi-2024-03-12", "title": "SPY CPI Win Rate (2024-03-12): Historical T+1/T+7 Probability", "event_date": "2024-03-12", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 3.94, "median_t7_pct": 1.08, "sample_size": 14}, {"slug": "spy-after-cpi-2024-11-14", "title": "2024-11-14 CPI Release: SPY Directional Probability Snapshot", "event_date": "2024-11-14", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 0.43, "median_t7_pct": 1.08, "sample_size": 14}, {"slug": "spy-after-cpi-2024-05-15", "title": "2024-05-15 CPI Release: SPY Directional Probability Snapshot", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 0.37, "median_t7_pct": 1.08, "sample_size": 14}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **SPY**
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
| T+1 | 64.29% | 35.71% | 0.15% | 0.26% | 14 |
| T+7 | 76.92% | 23.08% | 1.08% | 0.51% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 61.54% | 38.46% | 0.09% | 0.26% | 13 |
| T+7 | 76.92% | 23.08% | 1.08% | 0.51% | 13 |

## Event Outcome Interpretation

The main mistake after macro releases is to treat every surprise as a regime break. SPY around CPI is best framed through how the release landed higher than the previous release. The current observation shows actual value 326.5880 versus previous 326.0310, a delta of +0.5570. Across the full history, SPY has a T+7 up probability of 76.92% versus 23.08% down, with a median return of 1.08%. When only matching the same event direction, the T+7 up probability shifts to 76.92% across 13 comparable releases, with a same-direction median of 1.08%. That is the immediate context behind the current bullish classification. The standing hub thesis for this asset-event pair is: SPY reacts to CPI through broad risk-premium repricing; downside inflation surprises often support index breadth while upside shocks compress valuation multiples.

## Distribution Position

The current T+7 reaction of 0.51% sits in the middle of its historical distribution for SPY after CPI. Its z-score is 0.00, which measures distance from the historical mean, and its percentile rank is 46.15, which shows how often prior releases were weaker than this one. That places the observation inside the central band of observed windows, not in an obvious tail bucket. That is the difference between a manageable macro impulse and a tail event that can invalidate prior playbooks. In practice this means the page is useful for calibration, but it does not justify upgrading a routine macro response into a regime-break narrative.

## Comparison vs Hub Baseline

The baseline comparison matters because most false positives come from overreacting to ordinary noise. The hub baseline median T+7 return for SPY after CPI is 1.08%, while the baseline mean is 0.51% and the baseline standard deviation is 1.8429. The current event is running at -0.57% versus the baseline median. Same-direction probability is +0.00% versus the all-history T+7 up rate, and the same-direction median differs by +0.00%. That distance from baseline is what determines whether this is noise, pressure, or a real outlier worth extra caution. This release is classified as within historical norm rather than handled as a generic macro template. If the current move only differed by a few basis points, the narrative would collapse back toward historical norm. The current regime context also matters: Sector rotation speed has accelerated in the post-tightening phase.

## Failure Modes

The main failure mode is assuming the first interpretation of the release will survive cross-asset confirmation. Energy and healthcare moves can offset index-level signal clarity. This matters because the historical distribution is built on end-of-window outcomes, not the first minute of price discovery. A release can look constructive initially, then fail once rates, the dollar, and sector breadth reprice in a different direction. That is also why low sample environments and mixed reaction functions should be handled as weaker evidence.

## Execution Relevance

Treat this as an educational risk framework, not investment advice. The practical takeaway is to use the current page as a decision filter: read the release, compare it with the hub baseline, then decide whether the event is behaving like a normal CPI setup or a tail observation. For this asset-event pair, the operational checklist is: Track breadth (advance/decline) with index move.; Compare rate-sensitive sectors versus defensives.; Use predefined stop distance from event range.. When the page is marked within historical norm, the right response is not automatically to trade more aggressively; it is to decide whether confirmation quality is strong enough to justify action.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
