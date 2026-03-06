---
title: "Fed Decision (2026-01-28) and QQQ: Event-Driven Odds"
description: "Historical probability profile for QQQ around FOMC events (T+1/T+7)."
pubDate: "2026-03-06"
title_variant_id: 2
title_template_key: "fomc_2"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2026-01-28"
asof_date: "2026-03-05"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Bullish"
raw_signal_score: 17.56
robust_score: 13.56
penalties:
  sample: 4.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 60
sample_size: 9
freshness_days: 36
freshness_status: "fresh"
index_tier: "B"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 1.03
hub_baseline_median_t7: 1.16
hub_baseline_std_t7: 2.2487
hub_baseline_delta: -0.13
z_score_t7: 0.0
percentile_t7: 33.33
narrative_trigger: "strict_median_norm"
narrative_rank_band: "median"
narrative_direction_band: "neutral"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/qqq-after-fomc-2026-01-28"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-03T09:55:20.776741+00:00"
event_direction: "flat"
event_actual: 3.75
event_previous: 3.75
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: 1.08
  mdd_t7: 0.0
  volatility: 0.95
  impact_t1_pct: 0.08
  impact_t7_pct: 1.03
probabilities:
  sample_size: 9
  t1:
    up: 55.56
    down: 44.44
    median: 0.43
    mean: 0.08
    sample: 9
  t7:
    up: 77.78
    down: 22.22
    median: 1.16
    mean: 1.03
    sample: 9
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 9
    t1:
      up: 55.56
      down: 44.44
      median: 0.43
      mean: 0.08
      sample: 9
    t7:
      up: 77.78
      down: 22.22
      median: 1.16
      mean: 1.03
      sample: 9
related_events: [{"slug": "qqq-after-fomc-2024-01-30", "title": "Fed Decision (2024-01-30) and QQQ: Event-Driven Odds", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 2.07, "median_t7_pct": 1.16, "sample_size": 9}, {"slug": "qqq-after-fomc-2025-12-10", "title": "QQQ Post-FOMC Reaction (2025-12-10): Quant Backtest Snapshot", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 1.16, "sample_size": 9}, {"slug": "qqq-after-fomc-2025-10-29", "title": "2025-10-29 FOMC Meeting: QQQ T+1/T+7 Probability Profile", "event_date": "2025-10-29", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 1.16, "sample_size": 9}]
chartData: [{"time": "2026-01-26", "open": 623.21, "high": 627.61, "low": 622.12, "close": 625.46}, {"time": "2026-01-27", "open": 628.91, "high": 632.04, "low": 627.34, "close": 631.13}, {"time": "2026-01-28", "open": 635.46, "high": 636.6, "low": 631.81, "close": 633.22}, {"time": "2026-01-29", "open": 632.65, "high": 633.67, "low": 618.27, "close": 629.43}, {"time": "2026-01-30", "open": 625.71, "high": 628.26, "low": 619.3, "close": 621.87}, {"time": "2026-02-02", "open": 618.7, "high": 628.49, "low": 618.66, "close": 626.14}, {"time": "2026-02-03", "open": 628.3, "high": 629.98, "low": 610.96, "close": 616.52}, {"time": "2026-02-04", "open": 615.02, "high": 615.1, "low": 600.47, "close": 605.75}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **QQQ**
- Event date: **2026-01-28**
- As-of date (T-1): **2026-03-05**
- Freshness age: **36 days**
- Sample size (all-history): **9**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 3.75, Previous 3.75, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 0.43% | 0.08% | 9 |
| T+7 | 77.78% | 22.22% | 1.16% | 1.03% | 9 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 55.56% | 44.44% | 0.43% | 0.08% | 9 |
| T+7 | 77.78% | 22.22% | 1.16% | 1.03% | 9 |

## Event Outcome Interpretation

Execution quality here comes from context discipline rather than reacting to the first candle. QQQ around FOMC is best framed through how the release landed unchanged versus the previous release. The current observation shows actual value 3.7500 versus previous 3.7500, a delta of +0.0000. Across the full history, QQQ has a T+7 up probability of 77.78% versus 22.22% down, with a median return of 1.16%. When only matching the same event direction, the T+7 up probability shifts to 77.78% across 9 comparable releases, with a same-direction median of 1.16%. The current release therefore reads as a calibration event inside the median band, not as a high-conviction break. The standing hub thesis for this asset-event pair is: QQQ generally trends with forward-rate expectations, and reactions are magnified when valuation is stretched before the meeting. The highest-quality playbook setup occurs when statement language, dot-plot repricing, and...

## Distribution Position

This window sits in the median band and should be used for calibration rather than conviction. The current T+7 move of 1.03% carries a z-score of 0.00 and a percentile rank of 33.33, which keeps the release inside the central band of observed windows. That is exactly what a strict median norm looks like: neither extreme strength nor extreme weakness, just a normal response range that helps calibrate expectations. The key instruction here is simple: do not overstate what is still a routine macro window.

## Comparison vs Hub Baseline

This comparison stays close to the median band and is best used for calibration. The baseline comparison is what turns the page from observation into a repeatable checklist. The hub baseline median T+7 return is 1.16% and the current gap is -0.13%. Same-direction probability moves by +0.00% and the same-direction median differs by +0.00%. Those numbers matter because they show where normal variation ends, not because they justify an outsized story. The current regime context also matters: Communication tone has become a bigger driver than the headline rate level itself, particularly in periods where terminal-rate uncertainty is lower and policy-path uncertainty is higher. This increases the importance of...

## Failure Modes

The failure mode here is over-reading ordinary data as if it were exceptional. The main failure mode is skipping confirmation steps because the headline feels obvious. A dovish statement can still fail if Q&A tone turns cautious or if long-end yields reprice higher into the close. Mega-cap concentration can mask weak breadth, so index-level strength without broad participation often leads to late-session fade and poor risk-adjusted continuation. Median-band releases often produce the worst decisions when operators insist on finding a dramatic narrative where the distribution is actually telling them to stay measured.

## Execution Relevance

Treat this page as an execution checklist input, not a buy or sell signal. The operational takeaway is calibration, not escalation. The checklist remains Track implied cuts path before and after statement.; Wait for confirmation after Q&A begins.; Size positions based on realized volatility percentile.. When a page is marked strict median norm, the right move is to compare it against the hub, keep sizing conservative, and do not overstate the evidence.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
