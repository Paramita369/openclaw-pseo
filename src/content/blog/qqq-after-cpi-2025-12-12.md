---
title: "QQQ Reaction to US CPI (2025-12-12): Quant Probability Breakdown"
description: "Historical probability profile for QQQ around CPI events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 2
title_template_key: "cpi_2"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2025-12-12"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 6.07
robust_score: 0.07
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 70
sample_size: 14
freshness_days: 83
freshness_status: "stale"
index_tier: "B"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.54
hub_baseline_median_t7: 0.6
hub_baseline_std_t7: 2.3774
hub_baseline_delta: -0.06
z_score_t7: -0.0
percentile_t7: 46.15
narrative_trigger: "within_historical_norm"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/qqq-after-cpi-2025-12-12"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "up"
event_actual: 326.031
event_previous: 325.063
event_delta: 0.968
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 2.08
  mdd_t7: 0.0
  volatility: 0.26
  impact_t1_pct: 0.28
  impact_t7_pct: 0.54
probabilities:
  sample_size: 14
  t1:
    up: 57.14
    down: 42.86
    median: 0.35
    mean: 0.28
    sample: 14
  t7:
    up: 53.85
    down: 46.15
    median: 0.6
    mean: 0.54
    sample: 13
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 13
    t1:
      up: 53.85
      down: 46.15
      median: 0.16
      mean: 0.26
      sample: 13
    t7:
      up: 53.85
      down: 46.15
      median: 0.6
      mean: 0.54
      sample: 13
related_events: [{"slug": "qqq-after-cpi-2024-05-15", "title": "2024-05-15 CPI Release: QQQ Directional Probability Snapshot", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 9.6, "median_t7_pct": 0.6, "sample_size": 14}, {"slug": "qqq-after-cpi-2024-09-11", "title": "US CPI (2024-09-11) and QQQ: Event-Driven Return Odds", "event_date": "2024-09-11", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 7.08, "median_t7_pct": 0.6, "sample_size": 14}, {"slug": "qqq-after-cpi-2026-02-12", "title": "QQQ CPI Win Rate (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.6, "sample_size": 14}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **QQQ**
- Event date: **2025-12-12**
- As-of date (T-1): **2026-03-05**
- Freshness age: **83 days**
- Sample size (all-history): **14**

## Event Outcome

- CPI Outcome: **UP** (Actual 326.031, Previous 325.063, Delta +0.9680)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 57.14% | 42.86% | 0.35% | 0.28% | 14 |
| T+7 | 53.85% | 46.15% | 0.6% | 0.54% | 13 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 53.85% | 46.15% | 0.16% | 0.26% | 13 |
| T+7 | 53.85% | 46.15% | 0.6% | 0.54% | 13 |

## Event Outcome Interpretation

The main mistake after macro releases is to treat every surprise as a regime break. QQQ around CPI is best framed through how the release landed higher than the previous release. The current observation shows actual value 326.0310 versus previous 325.0630, a delta of +0.9680. Across the full history, QQQ has a T+7 up probability of 53.85% versus 46.15% down, with a median return of 0.60%. When only matching the same event direction, the T+7 up probability shifts to 53.85% across 13 comparable releases, with a same-direction median of 0.60%. That is the immediate context behind the current neutral classification. The standing hub thesis for this asset-event pair is: QQQ is highly duration-sensitive to CPI shocks. Positive inflation surprise usually pressures multiples first, then recovers if growth narrative stays intact.

## Distribution Position

The current T+7 reaction of 0.54% sits in the middle of its historical distribution for QQQ after CPI. Its z-score is -0.00, which measures distance from the historical mean, and its percentile rank is 46.15, which shows how often prior releases were weaker than this one. That places the observation inside the central band of observed windows, not in an obvious tail bucket. That is the difference between a manageable macro impulse and a tail event that can invalidate prior playbooks. In practice this means the page is useful for calibration, but it does not justify upgrading a routine macro response into a regime-break narrative.

## Comparison vs Hub Baseline

The baseline comparison matters because most false positives come from overreacting to ordinary noise. The hub baseline median T+7 return for QQQ after CPI is 0.60%, while the baseline mean is 0.54% and the baseline standard deviation is 2.3774. The current event is running at -0.06% versus the baseline median. Same-direction probability is +0.00% versus the all-history T+7 up rate, and the same-direction median differs by +0.00%. That distance from baseline is what determines whether this is noise, pressure, or a real outlier worth extra caution. This release is classified as within historical norm rather than handled as a generic macro template. If the current move only differed by a few basis points, the narrative would collapse back toward historical norm. The current regime context also matters: Mega-cap concentration has increased index-level event beta.

## Failure Modes

The main failure mode is assuming the first interpretation of the release will survive cross-asset confirmation. Single-name earnings shocks can mask macro signal quality. This matters because the historical distribution is built on end-of-window outcomes, not the first minute of price discovery. A release can look constructive initially, then fail once rates, the dollar, and sector breadth reprice in a different direction. That is also why low sample environments and mixed reaction functions should be handled as weaker evidence.

## Execution Relevance

Treat this as an educational risk framework, not investment advice. The practical takeaway is to use the current page as a decision filter: read the release, compare it with the hub baseline, then decide whether the event is behaving like a normal CPI setup or a tail observation. For this asset-event pair, the operational checklist is: Track US2Y/US10Y move for duration impulse.; Observe semiconductor breadth for confirmation.; Use staged entries around first-hour range.. When the page is marked within historical norm, the right response is not automatically to trade more aggressively; it is to decide whether confirmation quality is strong enough to justify action.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
