---
title: "2026-01-09 Nonfarm Payrolls: SPY Historical Win Rate"
description: "Historical probability profile for SPY around NFP events (T+1/T+7)."
pubDate: "2026-03-13"
title_variant_id: 2
title_template_key: "nfp_2"
event_type: "NFP"
event_label: "NFP"
event_slug: "nfp"
event_date: "2026-01-09"
asof_date: "2026-03-12"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 4.94
robust_score: -1.06
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
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.81
hub_baseline_median_t7: 0.11
hub_baseline_std_t7: 1.9337
hub_baseline_delta: -0.46
z_score_t7: -0.6
percentile_t7: 32.35
narrative_trigger: "moderate_underperformance"
narrative_rank_band: "moderate"
narrative_direction_band: "negative"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/spy-after-nfp-2026-01-09"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-13T09:46:21+00:00"
event_direction: "up"
event_actual: 158558.0
event_previous: 158432.0
event_delta: 126.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["spy", "nfp", "event-probability", "general"]
metrics:
  sharpe_t7: -6.51
  mdd_t7: -0.5
  volatility: 4.47
  impact_t1_pct: 0.16
  impact_t7_pct: -0.35
probabilities:
  sample_size: 35
  t1:
    up: 50.0
    down: 50.0
    median: 0.02
    mean: -0.05
    sample: 22
  t7:
    up: 55.88
    down: 44.12
    median: 0.11
    mean: 0.81
    sample: 34
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 14
    t1:
      up: 42.86
      down: 57.14
      median: -0.07
      mean: -0.11
      sample: 14
    t7:
      up: 61.54
      down: 38.46
      median: 0.55
      mean: 1.0
      sample: 26
related_events: [{"slug": "spy-after-nfp-2026-01-02", "title": "SPY After NFP (2026-01-02): Historical T+1/T+7 Probability", "event_date": "2026-01-02", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.6, "sample_size": 0}, {"slug": "spy-after-nfp-2025-11-20", "title": "SPY After NFP (2025-11-20): Historical T+1/T+7 Probability", "event_date": "2025-11-20", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 4.73, "sample_size": 0}, {"slug": "spy-after-nfp-2025-09-05", "title": "SPY After NFP (2025-09-05): Historical T+1/T+7 Probability", "event_date": "2025-09-05", "event_type": "NFP", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.57, "sample_size": 0}]
chartData: [{"time": "2026-01-06", "open": 687.93, "high": 692.32, "low": 687.78, "close": 691.81}, {"time": "2026-01-07", "open": 692.19, "high": 693.96, "low": 689.32, "close": 689.58}, {"time": "2026-01-08", "open": 688.82, "high": 690.62, "low": 687.49, "close": 689.51}, {"time": "2026-01-09", "open": 690.63, "high": 695.31, "low": 689.18, "close": 694.07}, {"time": "2026-01-12", "open": 690.68, "high": 696.09, "low": 690.63, "close": 695.16}, {"time": "2026-01-13", "open": 695.49, "high": 696.09, "low": 691.35, "close": 693.77}, {"time": "2026-01-14", "open": 691.0, "high": 691.72, "low": 686.04, "close": 690.36}, {"time": "2026-01-15", "open": 694.57, "high": 695.45, "low": 691.25, "close": 692.24}, {"time": "2026-01-16", "open": 693.66, "high": 694.25, "low": 690.1, "close": 691.66}]
---

## Event Snapshot

- Event: **NFP**
- Asset: **SPY**
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
| T+1 | 50.0% | 50.0% | 0.02% | -0.05% | 22 |
| T+7 | 55.88% | 44.12% | 0.11% | 0.81% | 34 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 42.86% | 57.14% | -0.07% | -0.11% | 14 |
| T+7 | 61.54% | 38.46% | 0.55% | 1.0% | 26 |

## Event Outcome Interpretation

The main mistake after macro releases is to treat every surprise as a regime break. SPY around NFP is best framed through how the release landed higher than the previous release. The current observation shows actual value 158558.0000 versus previous 158432.0000, a delta of +126.0000. Across the full history, SPY has a T+7 up probability of 55.88% versus 44.12% down, with a median return of 0.11%. When only matching the same event direction, the T+7 up probability shifts to 61.54% across 14 comparable releases, with a same-direction median of 0.55%. The current release therefore reads as a below-baseline and fragile response rather than a collapse. The standing hub thesis for this asset-event pair is: SPY's payroll reaction depends on whether labor strength implies growth support or renewed rate pressure; context from wages and revisions is critical.

## Distribution Position

This window is below baseline and looks fragile rather than structurally broken. The current T+7 move of -0.35% carries a z-score of -0.60 and a percentile rank of 32.35, leaving the release in the central band of observed windows. That puts the event on the weak side of normal without forcing it into a full downside tail label. The important distinction is that fragile reactions can still bounce, which is why a mild underperformance should not be confused with regime failure.

## Comparison vs Hub Baseline

This comparison is below baseline, but it is still better read as fragile than catastrophic. The baseline comparison matters because most false positives come from overreacting to ordinary noise. The hub baseline median T+7 return is 0.11% and the current gap is -0.46%. Same-direction probability differs by +5.66% and the same-direction median differs by +0.44%. The baseline gap is large enough to matter, but not large enough to imply that the broader playbook is broken. The current regime context also matters: Market has priced labor resilience with tighter tolerance for inflation reacceleration.

## Failure Modes

The failure mode here is reading a fragile window as proof of permanent weakness. The main failure mode is assuming the first interpretation will survive cross-asset confirmation. False trend starts are common before cash-session participation increases. Moderate underperformance often creates bounce risk, especially if rates or the dollar stop reinforcing the weak read.

## Execution Relevance

Treat this as an educational risk framework, not investment advice. The operational takeaway is to respect the below-baseline read without assuming collapse. The checklist is Read payroll, wages, and revisions as a package.; Wait for cash equity open confirmation.; Scale out into intraday volatility spikes.. Fragile setups demand tighter invalidation and more patience because bounce risk is often highest when traders treat every weak release as a one-way trend.

## Methodology

This page aggregates historical windows for the same event type (NFP) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
