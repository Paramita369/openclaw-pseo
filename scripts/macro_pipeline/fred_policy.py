from __future__ import annotations

from typing import Dict


def enforce_fred_api_requirement(*, strict: bool, fred_api_key: str, fetch_statuses: Dict[str, str]) -> None:
    if not strict:
        return
    if not fred_api_key.strip():
        raise RuntimeError('FRED_API_KEY missing in strict mode')
    bad = {series: status for series, status in fetch_statuses.items() if status != 'api'}
    if bad:
        raise RuntimeError(f'FRED API requirement failed: {bad}')
