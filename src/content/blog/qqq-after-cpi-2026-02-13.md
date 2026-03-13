---
title: "QQQ After CPI (2026-02-13): Up/Down Odds and Median Returns"
description: "Historical probability profile for QQQ around CPI events (T+1/T+7)."
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
signal: "Neutral"
raw_signal_score: 7.63
robust_score: 7.63
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
body_variant_family: "risk-first"
hub_baseline_mean_t7: 0.2
hub_baseline_median_t7: 0.58
hub_baseline_std_t7: 2.2166
hub_baseline_delta: 0.56
z_score_t7: 0.42
percentile_t7: 65.79
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/qqq-after-cpi-2026-02-13"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-13T09:46:21+00:00"
event_direction: "up"
event_actual: 327.46
event_previous: 326.588
event_delta: 0.872
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "cpi", "event-probability", "general"]
metrics:
  sharpe_t7: 9.87
  mdd_t7: -0.1
  volatility: 9.75
  impact_t1_pct: -0.1
  impact_t7_pct: 1.14
probabilities:
  sample_size: 40
  t1:
    up: 60.0
    down: 40.0
    median: 0.19
    mean: 0.19
    sample: 40
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
      up: 58.97
      down: 41.03
      median: 0.16
      mean: 0.18
      sample: 39
    t7:
      up: 55.26
      down: 44.74
      median: 0.58
      mean: 0.2
      sample: 38
related_events: [{"slug": "qqq-after-cpi-2026-02-12", "title": "QQQ After CPI (2026-02-12): Historical T+1/T+7 Probability", "event_date": "2026-02-12", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 0.47, "sample_size": 0}, {"slug": "qqq-after-cpi-2025-12-18", "title": "QQQ After CPI (2025-12-18): Historical T+1/T+7 Probability", "event_date": "2025-12-18", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 2.56, "sample_size": 0}, {"slug": "qqq-after-cpi-2025-10-24", "title": "QQQ After CPI (2025-10-24): Historical T+1/T+7 Probability", "event_date": "2025-10-24", "event_type": "CPI", "signal": "Neutral", "sharpe_t7": 10.0, "median_t7_pct": 1.94, "sample_size": 0}]
chartData: [{"time": "2026-02-10", "open": 615.31, "high": 617.02, "low": 611.01, "close": 611.47}, {"time": "2026-02-11", "open": 616.38, "high": 617.52, "low": 607.69, "close": 613.11}, {"time": "2026-02-12", "open": 614.71, "high": 615.81, "low": 599.57, "close": 600.64}, {"time": "2026-02-13", "open": 600.43, "high": 606.48, "low": 596.42, "close": 601.92}, {"time": "2026-02-17", "open": 598.38, "high": 603.95, "low": 593.34, "close": 601.3}, {"time": "2026-02-18", "open": 602.11, "high": 609.77, "low": 600.72, "close": 605.79}, {"time": "2026-02-19", "open": 602.81, "high": 605.82, "low": 600.75, "close": 603.47}, {"time": "2026-02-20", "open": 600.12, "high": 610.35, "low": 599.23, "close": 608.81}]
---

## Event Snapshot

- Event: **CPI**
- Asset: **QQQ**
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
| T+1 | 60.0% | 40.0% | 0.19% | 0.19% | 40 |
| T+7 | 55.26% | 44.74% | 0.58% | 0.2% | 38 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 58.97% | 41.03% | 0.16% | 0.18% | 39 |
| T+7 | 55.26% | 44.74% | 0.58% | 0.2% | 38 |

## Event Outcome Interpretation

The main mistake after macro releases is to treat every surprise as a regime break. QQQ around CPI is best framed through how the release landed higher than the previous release. The current observation shows actual value 327.4600 versus previous 326.5880, a delta of +0.8720. Across the full history, QQQ has a T+7 up probability of 55.26% versus 44.74% down, with a median return of 0.58%. When only matching the same event direction, the T+7 up probability shifts to 55.26% across 38 comparable releases, with a same-direction median of 0.58%. The current release therefore reads as a calibration event inside the median band, not as a high-conviction break. The standing hub thesis for this asset-event pair is: QQQ is highly duration-sensitive to CPI shocks. Positive inflation surprise usually pressures multiples first, then recovers if growth narrative stays intact.

## Distribution Position

This window sits in the median band and should be used for calibration rather than conviction. The current T+7 move of 1.14% carries a z-score of 0.42 and a percentile rank of 65.79, which keeps the release inside the central band of observed windows. That is exactly what a strict median norm looks like: neither extreme strength nor extreme weakness, just a normal response range that helps calibrate expectations. The key instruction here is simple: do not overstate what is still a routine macro window.

## Comparison vs Hub Baseline

This comparison stays close to the median band and is best used for calibration. The baseline comparison matters because most false positives come from overreacting to ordinary noise. The hub baseline median T+7 return is 0.58% and the current gap is +0.56%. Same-direction probability moves by +0.00% and the same-direction median differs by +0.00%. Those numbers matter because they show where normal variation ends, not because they justify an outsized story. The current regime context also matters: Mega-cap concentration has increased index-level event beta.

## Failure Modes

The failure mode here is over-reading ordinary data as if it were exceptional. The main failure mode is assuming the first interpretation will survive cross-asset confirmation. Single-name earnings shocks can mask macro signal quality. Median-band releases often produce the worst decisions when operators insist on finding a dramatic narrative where the distribution is actually telling them to stay measured.

## Execution Relevance

Treat this as an educational risk framework, not investment advice. The operational takeaway is calibration, not escalation. The checklist remains Track US2Y/US10Y move for duration impulse.; Observe semiconductor breadth for confirmation.; Use staged entries around first-hour range.. When a page is marked strict median norm, the right move is to compare it against the hub, keep sizing conservative, and do not overstate the evidence.

## Methodology

This page aggregates historical windows for the same event type (CPI) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
