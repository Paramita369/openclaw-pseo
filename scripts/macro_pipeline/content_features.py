from __future__ import annotations

import math
import statistics
from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Iterable, List, Optional, Sequence

CORE_WINDOW_DAYS = 90
FEATURE_EPSILON = 1e-8


@dataclass(frozen=True)
class StatisticalFeatures:
    baseline_mean_t7: float
    baseline_median_t7: float
    baseline_std_t7: float
    hub_baseline_delta: float
    z_score_t7: float
    percentile_t7: float
    narrative_trigger: str
    sample_size: int


def _parse_iso_date(value: str) -> Optional[datetime]:
    text = str(value or '').strip()
    if not text:
        return None
    try:
        return datetime.strptime(text[:10], '%Y-%m-%d')
    except ValueError:
        return None


def coerce_finite_float(value: object) -> Optional[float]:
    try:
        number = float(value)
    except Exception:
        return None
    return number if math.isfinite(number) else None


def finite_values(values: Iterable[object]) -> List[float]:
    output: List[float] = []
    for value in values:
        number = coerce_finite_float(value)
        if number is not None:
            output.append(number)
    return output


def compute_recent_cutoff(as_of_date: str, window_days: int = CORE_WINDOW_DAYS) -> Optional[str]:
    parsed = _parse_iso_date(as_of_date)
    if parsed is None:
        return None
    return (parsed - timedelta(days=window_days)).date().isoformat()


def is_core_page_for_window(
    *,
    event_date: str,
    as_of_date: str,
    canonical_target: str,
    robots_directive: str,
    in_blog_sitemap: bool,
    window_days: int = CORE_WINDOW_DAYS,
) -> bool:
    if canonical_target != 'self':
        return False
    if robots_directive != 'index,follow':
        return False
    if not bool(in_blog_sitemap):
        return False

    event_dt = _parse_iso_date(event_date)
    as_of_dt = _parse_iso_date(as_of_date)
    if event_dt is None or as_of_dt is None:
        return False

    age_days = (as_of_dt.date() - event_dt.date()).days
    if age_days < 0:
        return False
    return age_days <= window_days


def compute_statistical_features(
    current_value: object,
    baseline_values: Sequence[object],
    *,
    epsilon: float = FEATURE_EPSILON,
) -> StatisticalFeatures:
    baseline = finite_values(baseline_values)
    current = coerce_finite_float(current_value)
    if current is None or len(baseline) < 8:
        return StatisticalFeatures(
            baseline_mean_t7=0.0,
            baseline_median_t7=0.0,
            baseline_std_t7=0.0,
            hub_baseline_delta=0.0,
            z_score_t7=0.0,
            percentile_t7=0.0,
            narrative_trigger='low_context',
            sample_size=len(baseline),
        )

    mean_value = float(statistics.mean(baseline))
    median_value = float(statistics.median(baseline))
    std_value = float(statistics.pstdev(baseline)) if len(baseline) > 1 else 0.0
    delta_value = float(current - median_value)
    if std_value < epsilon:
        z_score = 0.0
    else:
        z_score = float((current - mean_value) / std_value)

    percentile = float(sum(1 for value in baseline if value <= current) / len(baseline) * 100.0)
    if not math.isfinite(z_score):
        z_score = 0.0
    if not math.isfinite(percentile):
        percentile = 0.0

    if z_score >= 1.25 or percentile >= 85.0:
        narrative = 'significant_outperformance'
    elif z_score <= -1.25 or percentile <= 15.0:
        narrative = 'significant_underperformance'
    else:
        narrative = 'within_historical_norm'

    return StatisticalFeatures(
        baseline_mean_t7=round(mean_value, 2),
        baseline_median_t7=round(median_value, 2),
        baseline_std_t7=round(std_value, 4),
        hub_baseline_delta=round(delta_value, 2),
        z_score_t7=round(z_score, 2),
        percentile_t7=round(percentile, 2),
        narrative_trigger=narrative,
        sample_size=len(baseline),
    )
