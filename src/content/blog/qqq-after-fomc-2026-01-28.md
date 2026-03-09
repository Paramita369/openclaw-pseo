---
title: "Fed Decision (2026-01-28) and QQQ: Event-Driven Odds"
description: "Historical probability profile for QQQ around FOMC events (T+1/T+7)."
pubDate: "2026-03-09"
title_variant_id: 2
title_template_key: "fomc_2"
event_type: "FOMC"
event_label: "FOMC"
event_slug: "fomc"
event_date: "2026-01-28"
asof_date: "2026-03-08"
source: "verified_targets.csv"
offer_key: "ibkr"
signal: "Neutral"
raw_signal_score: 3.3
robust_score: 3.3
penalties:
  sample: 0.0
  freshness: 0.0
  confidence: 0.0
  outcome: 0.0
confidence_level: "normal"
quality_score: 90
sample_size: 23
freshness_days: 39
freshness_status: "fresh"
index_tier: "A"
is_recent_90d: true
is_core_page: true
core_window_days: 90
body_variant_family: "checklist"
hub_baseline_mean_t7: 0.27
hub_baseline_median_t7: 0.88
hub_baseline_std_t7: 2.891
hub_baseline_delta: -5.22
z_score_t7: -1.6
percentile_t7: 0.0
narrative_trigger: "extreme_underperformance"
narrative_rank_band: "extreme"
narrative_direction_band: "negative"
canonical_target: "self"
canonical_url: "https://quantmacro.vercel.app/blog/qqq-after-fomc-2026-01-28"
robots_directive: "index,follow"
in_blog_sitemap: true
data_last_updated_at: "2026-03-04T01:58:11+00:00"
event_direction: "flat"
event_actual: 3.75
event_previous: 3.75
event_delta: 0.0
direction_basis: "vs_previous"
outcome_status: "ok"
tags: ["qqq", "fomc", "event-probability", "general"]
metrics:
  sharpe_t7: -1.16
  mdd_t7: -4.34
  volatility: 3.74
  impact_t1_pct: -0.6
  impact_t7_pct: -4.34
probabilities:
  sample_size: 23
  t1:
    up: 43.48
    down: 56.52
    median: -0.19
    mean: -0.05
    sample: 23
  t7:
    up: 56.52
    down: 43.48
    median: 0.88
    mean: 0.27
    sample: 23
  conditional:
    basis: "event_direction"
    direction: "flat"
    sample_size: 17
    t1:
      up: 41.18
      down: 58.82
      median: -0.34
      mean: -0.06
      sample: 17
    t7:
      up: 64.71
      down: 35.29
      median: 1.08
      mean: 0.6
      sample: 17
related_events: [{"slug": "qqq-after-fomc-2024-01-30", "title": "Fed Decision (2024-01-30) and QQQ: Event-Driven Odds", "event_date": "2024-01-30", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 2.07, "median_t7_pct": 1.16, "sample_size": 9}, {"slug": "qqq-after-fomc-2025-12-10", "title": "QQQ Post-FOMC Reaction (2025-12-10): Quant Backtest Snapshot", "event_date": "2025-12-10", "event_type": "FOMC", "signal": "Neutral", "sharpe_t7": 0.0, "median_t7_pct": 0.88, "sample_size": 23}, {"slug": "qqq-after-fomc-2025-10-29", "title": "2025-10-29 FOMC Meeting: QQQ T+1/T+7 Probability Profile", "event_date": "2025-10-29", "event_type": "FOMC", "signal": "Bullish", "sharpe_t7": 0.0, "median_t7_pct": 1.16, "sample_size": 9}]
chartData: [{"time": "2026-01-26", "open": 623.21, "high": 627.61, "low": 622.12, "close": 625.46}, {"time": "2026-01-27", "open": 628.91, "high": 632.04, "low": 627.34, "close": 631.13}, {"time": "2026-01-28", "open": 635.46, "high": 636.6, "low": 631.81, "close": 633.22}, {"time": "2026-01-29", "open": 632.65, "high": 633.67, "low": 618.27, "close": 629.43}, {"time": "2026-01-30", "open": 625.71, "high": 628.26, "low": 619.3, "close": 621.87}, {"time": "2026-02-02", "open": 618.7, "high": 628.49, "low": 618.66, "close": 626.14}, {"time": "2026-02-03", "open": 628.3, "high": 629.98, "low": 610.96, "close": 616.52}, {"time": "2026-02-04", "open": 615.02, "high": 615.1, "low": 600.47, "close": 605.75}]
---

## Event Snapshot

- Event: **FOMC**
- Asset: **QQQ**
- Event date: **2026-01-28**
- As-of date (T-1): **2026-03-08**
- Freshness age: **39 days**
- Sample size (all-history): **23**

## Event Outcome

- FOMC Outcome: **FLAT** (Actual 3.75, Previous 3.75, Delta +0.0000)
- Direction basis: **vs_previous**

## Probability Table (All-history)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 43.48% | 56.52% | -0.19% | -0.05% | 23 |
| T+7 | 56.52% | 43.48% | 0.88% | 0.27% | 23 |

## Probability Table (Same-direction)

| Window | P(up) | P(down) | Median return | Mean return | Sample |
| :--- | ---: | ---: | ---: | ---: | ---: |
| T+1 | 41.18% | 58.82% | -0.34% | -0.06% | 17 |
| T+7 | 64.71% | 35.29% | 1.08% | 0.6% | 17 |

## Event Outcome Interpretation

Execution quality here comes from context discipline rather than reacting to the first candle. QQQ around FOMC is best framed through how the release landed unchanged versus the previous release. The current observation shows actual value 3.7500 versus previous 3.7500, a delta of +0.0000. Across the full history, QQQ has a T+7 up probability of 56.52% versus 43.48% down, with a median return of 0.88%. When only matching the same event direction, the T+7 up probability shifts to 64.71% across 17 comparable releases, with a same-direction median of 1.08%. The current release therefore belongs to the downside tail and should be treated as materially weak. The standing hub thesis for this asset-event pair is: QQQ generally trends with forward-rate expectations, and reactions are magnified when valuation is stretched before the meeting. The highest-quality playbook setup occurs when statement language, dot-plot repricing, and...

## Distribution Position

This window sits in the weak tail and should be classified as a downside tail event for QQQ after FOMC. The current T+7 move of -4.34% carries a z-score of -1.60 and a percentile rank of 0.00, which pushes the release into the weakest decile of observed windows and away from ordinary downside noise. That makes this an extreme negative deviation rather than a routine weak print, so the page should be read with explicit downside-tail caution.

## Comparison vs Hub Baseline

This comparison is materially below baseline and should be treated as a true downside-tail gap. The baseline comparison is what turns the page from observation into a repeatable checklist. The hub baseline median T+7 return is 0.88% and the current gap is -5.22%. Same-direction probability differs by +8.19% and the same-direction median differs by +0.20%. The baseline gap is now large enough to justify a weak-tail classification and a more defensive interpretation. The current regime context also matters: Communication tone has become a bigger driver than the headline rate level itself, particularly in periods where terminal-rate uncertainty is lower and policy-path uncertainty is higher. This increases the importance of...

## Failure Modes

The failure mode here is underestimating how far a downside tail can travel before it stabilizes. The main failure mode is skipping confirmation steps because the headline feels obvious. A dovish statement can still fail if Q&A tone turns cautious or if long-end yields reprice higher into the close. Mega-cap concentration can mask weak breadth, so index-level strength without broad participation often leads to late-session fade and poor risk-adjusted continuation. Invalidation needs to be tighter because weak-tail conditions can extend farther than a normal weak window.

## Execution Relevance

Treat this page as an execution checklist input, not a buy or sell signal. The operational takeaway is to respect the downside tail and accept a higher invalidation burden before assuming the move is spent. The checklist remains Track implied cuts path before and after statement.; Wait for confirmation after Q&A begins.; Size positions based on realized volatility percentile.. This is exactly the state where waiting for confirmation matters more than trying to fade weakness too early.

## Methodology

This page aggregates historical windows for the same event type (FOMC) and deduplicates by event date. It reports both all-history probabilities and same-direction probabilities based on event outcome direction (vs previous) for educational use only.
