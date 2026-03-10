---
title: "QQQ CPI Win Rate (2026-01-12): Historical T+1/T+7 Probability"
description: "Historical probability profile for QQQ around CPI events (T+1/T+7)."
pubDate: "2026-03-10"
title_variant_id: 1
title_template_key: "cpi_1"
event_type: "CPI"
event_label: "CPI"
event_slug: "cpi"
event_date: "2026-01-12"
asof_date: "2026-03-09"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 8.09
robust_score: 2.09
penalties:
  sample: 0.0
  freshness: 6.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 39
freshness_days: 56
freshness_status: "stale"
index_tier: "B"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.2
hub_baseline_median_t7: 0.58
hub_baseline_std_t7: 2.2166
hub_baseline_delta: -3.63
z_score_t7: -1.47
percentile_t7: 5.26
narrative_trigger: "extreme_underperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "negative"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/qqq-after-cpi-2026-01-12"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "up"
event_actual: 326.588
event_previous: 326.031
event_delta: 0.557
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: -1.05
  mdd_t7: -3.05
  volatility: 2.9
  impact_t1_pct: -0.15
  impact_t7_pct: -3.05
probabilities:
  sample_size: 39
  t1:
    up: 61.54
    down: 38.46
    median: 0.21
    mean: 0.23
    sample: 39
  t7:
    up: 55.26
    down: 44.74
    median: 0.58
    mean: 0.2
    sample: 38
  conditional:
    basis: "event_direction"
    direction: "up"
    sample_size: 38
    t1:
      up: 60.53
      down: 39.47
      median: 0.19
      mean: 0.23
      sample: 38
    t7:
      up: 55.26
      down: 44.74
      median: 0.58
      mean: 0.2
      sample: 38
related_events: [{"slug": "qqq-after-cpi-2024-05-15", "title": "2024-05-15 CPI Release: QQQ Directional Probability Snapshot", "event_date": "2024-05-15", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 9.6, "median_t7_pct": 0.58, "sample_size": 39}, {"slug": "qqq-after-cpi-2024-09-11", "title": "US CPI (2024-09-11) and QQQ: Event-Driven Return Odds", "event_date": "2024-09-11", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 7.08, "median_t7_pct": 0.58, "sample_size": 39}, {"slug": "qqq-after-cpi-2026-02-12", "title": "QQQ CPI Win Rate (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 0.58, "sample_size": 39}]
chartData: [{"time": "2026-01-09", "open": 621.41, "high": 627.89, "low": 619.06, "close": 626.65}, {"time": "2026-01-12", "open": 622.31, "high": 628.85, "low": 622.26, "close": 627.17}, {"time": "2026-01-13", "open": 627.27, "high": 629.47, "low": 623.7, "close": 626.24}, {"time": "2026-01-14", "open": 622.24, "high": 623.45, "low": 614.56, "close": 619.55}, {"time": "2026-01-15", "open": 626.6, "high": 630.0, "low": 620.75, "close": 621.78}, {"time": "2026-01-16", "open": 625.5, "high": 626.08, "low": 618.88, "close": 621.26}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **QQQ**
- Event date: **2026-01-12**
- As-of date (T-1): **2026-03-09**
- Freshness age: **56 days**
- Sample size (all-history): **39**

## Event Outcome

- CPI Outcome: **UP** (Actual 326.588, Previous 326.031, Delta +0.5570)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 61.54% | 38.46% | 0.21% | 0.23% | 39 |
| T+7 | 55.26% | 44.74% | 0.58% | 0.2% | 38 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 60.53% | 39.47% | 0.19% | 0.23% | 38 |
| T+7 | 55.26% | 44.74% | 0.58% | 0.2% | 38 |

## Event Outcome Interpretation

The main mistake after macro releases is to treat every surprise as a regime break. QQQ around CPI is best framed through how the release landed higher than the previous release. The current observation shows actual value 326.5880 versus previous 326.0310, a delta of +0.5570. Across the full history, QQQ has a T+7 up probability of 55.26% versus 44.74% down, with a median return of 0.58%. When only matching the same event direction, the T+7 up probability shifts to 55.26% across 38 comparable releases, with a same-direction median of 0.58%. The current release therefore belongs to the downside tail and should be treated as materially weak. The standing hub thesis for this asset-event pair is: QQQ is highly duration-sensitive to CPI shocks. Positive inflation surprise usually pressures multiples first, then recovers if growth narrative stays intact.

## Distribution Position

This window sits in the weak tail and should be classified as a downside tail event for QQQ after CPI. The current T+7 move of -3.05% carries a z-score of -1.47 and a percentile rank of 5.26, which pushes the release into the weakest decile of observed windows and away from ordinary downside noise. That makes this an extreme negative deviation rather than a routine weak print, so the page should be read with explicit downside-tail caution.

## Comparison vs Hub Baseline

This comparison is materially below baseline and should be treated as a true downside-tail gap. The baseline comparison matters because most false positives come from overreacting to ordinary noise. The hub baseline median T+7 return is 0.58% and the current gap is -3.63%. Same-direction probability differs by +0.00% and the same-direction median differs by +0.00%. The baseline gap is now large enough to justify a weak-tail classification and a more defensive interpretation. The current regime context also matters: Mega-cap concentration has increased index-level event beta.

## Failure Modes

The failure mode here is underestimating how far a downside tail can travel before it stabilizes. The main failure mode is assuming the first interpretation will survive cross-asset confirmation. Single-name earnings shocks can mask macro signal quality. Invalidation needs to be tighter because weak-tail conditions can extend farther than a normal weak window.

## Execution Relevance

Treat this as an educational risk framework, not investment advice. The operational takeaway is to respect the downside tail and accept a higher invalidation burden before assuming the move is spent. The checklist remains Track US2Y/US10Y move for duration impulse.; Observe semiconductor breadth for confirmation.; Use staged entries around first-hour range.. This is exactly the state where waiting for confirmation matters more than trying to fade weakness too early.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
