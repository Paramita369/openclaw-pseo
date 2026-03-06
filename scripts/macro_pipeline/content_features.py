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
    narrative_rank_band: str
    narrative_direction_band: str
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


def resolve_narrative_trigger(z_score: float, percentile: float, sample_size: int) -> str:
    if sample_size < 8:
        return "low_context"

    def z_bucket(value: float) -> tuple[int, str]:
        if value >= 1.5:
            return (5, "extreme_outperformance")
        if value <= -1.5:
            return (5, "extreme_underperformance")
        if value >= 0.5:
            return (3, "moderate_outperformance")
        if value <= -0.5:
            return (3, "moderate_underperformance")
        return (1, "strict_median_norm")

    def percentile_bucket(value: float) -> tuple[int, str]:
        if value >= 90.0:
            return (5, "extreme_outperformance")
        if value <= 10.0:
            return (5, "extreme_underperformance")
        if value >= 70.0:
            return (3, "moderate_outperformance")
        if value < 30.0:
            return (3, "moderate_underperformance")
        return (1, "strict_median_norm")

    z_severity, z_trigger = z_bucket(z_score)
    percentile_severity, percentile_trigger = percentile_bucket(percentile)
    return z_trigger if z_severity >= percentile_severity else percentile_trigger


def narrative_rank_band(trigger: str) -> str:
    mapping = {
        "extreme_outperformance": "extreme",
        "extreme_underperformance": "extreme",
        "moderate_outperformance": "moderate",
        "moderate_underperformance": "moderate",
        "strict_median_norm": "median",
        "low_context": "low_context",
    }
    return mapping.get(str(trigger or "").strip(), "unknown")


def narrative_direction_band(trigger: str) -> str:
    mapping = {
        "extreme_outperformance": "positive",
        "moderate_outperformance": "positive",
        "strict_median_norm": "neutral",
        "moderate_underperformance": "negative",
        "extreme_underperformance": "negative",
        "low_context": "unknown",
    }
    return mapping.get(str(trigger or "").strip(), "unknown")


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
            narrative_rank_band='low_context',
            narrative_direction_band='unknown',
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

    narrative = resolve_narrative_trigger(z_score, percentile, len(baseline))

    return StatisticalFeatures(
        baseline_mean_t7=round(mean_value, 2),
        baseline_median_t7=round(median_value, 2),
        baseline_std_t7=round(std_value, 4),
        hub_baseline_delta=round(delta_value, 2),
        z_score_t7=round(z_score, 2),
        percentile_t7=round(percentile, 2),
        narrative_trigger=narrative,
        narrative_rank_band=narrative_rank_band(narrative),
        narrative_direction_band=narrative_direction_band(narrative),
        sample_size=len(baseline),
    )
