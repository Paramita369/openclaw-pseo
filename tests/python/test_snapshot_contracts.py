from __future__ import annotations

from datetime import datetime, timezone
from pathlib import Path

from fetch_daily_snapshot import fallback_entry
from quality_gates import validate_snapshot_single_source_contract

ROOT = Path(__file__).resolve().parents[2]


def test_fallback_entry_marks_snapshot_as_fallback() -> None:
    now = datetime(2026, 3, 6, 12, 0, tzinfo=timezone.utc)
    entry = fallback_entry(
        {
            'price': 123.45,
            'change': 1.2,
            'high': 125.0,
            'low': 120.0,
            'as_of_ts': '2026-03-05T20:00:00+00:00',
            'as_of_date': '2026-03-05',
        },
        now,
        asset_type='us_session',
    )
    assert entry is not None
    assert entry['source'] == 'fallback_cache'
    assert entry['source_quality'] == 'fallback'
    assert entry['display_mode'] == 'fallback'


def test_snapshot_single_source_contract_passes() -> None:
    result = validate_snapshot_single_source_contract(ROOT)
    assert result['count'] == 0, result['violations']
