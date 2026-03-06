from __future__ import annotations

from pathlib import Path

from quality_gates import HUB_ASSETS, HUB_EVENTS, hub_content_depth_passes, load_hub_briefs_payload

ROOT = Path(__file__).resolve().parents[2]


def test_approved_index_hubs_meet_depth_contract() -> None:
    payload = load_hub_briefs_payload(ROOT / 'data' / 'hub_briefs.yaml')
    assert isinstance(payload, dict)
    failing = []
    for asset in HUB_ASSETS:
        for event in HUB_EVENTS:
            key = f'{asset}_{event}'
            item = payload.get(key, {})
            status = str(item.get('status', '')).lower() if isinstance(item, dict) else 'draft'
            indexing = str(item.get('indexing', '')).lower() if isinstance(item, dict) else 'noindex'
            if status == 'approved' and indexing == 'index' and not hub_content_depth_passes(item):
                failing.append(key)
    assert not failing, failing


def test_short_approved_hub_fails_depth_contract() -> None:
    item = {
        'thesis': 'too short',
        'what_changed_recently': 'also too short',
        'risk_watchouts': 'short',
        'execution_checklist': ['first item is long enough', 'second item long enough', 'third item long enough'],
    }
    assert hub_content_depth_passes(item) is False
