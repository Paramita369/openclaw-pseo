"""Common helpers for the local daily pSEO pipeline."""

from __future__ import annotations

import hashlib
import json
import math
import os
from datetime import datetime, timedelta
from pathlib import Path
from typing import Any, Dict, Optional

ALLOWED_EVENT_TYPES = {"CPI", "NFP", "FOMC"}
PRIMARY_ASSETS = ("BTC", "ETH", "GOLD", "QQQ", "SPY")


def event_filter_sql(event_type: str) -> str:
    normalized = (event_type or "").strip().upper()
    if normalized == "CPI":
        return "UPPER(m.headline) LIKE '%CPI%'"
    if normalized == "NFP":
        return "UPPER(m.headline) LIKE '%NFP%'"
    if normalized == "FOMC":
        return "UPPER(m.headline) LIKE '%FOMC%'"
    return "1=0"


def resolve_project_root(project_root: Optional[str] = None) -> Path:
    """Resolve the repository root for all pipeline scripts."""
    if project_root:
        return Path(project_root).expanduser().resolve()

    env_root = os.getenv("PROJECT_ROOT", "").strip()
    if env_root:
        return Path(env_root).expanduser().resolve()

    return Path(__file__).resolve().parents[2]


def ensure_dir(path: Path) -> None:
    path.mkdir(parents=True, exist_ok=True)


def parse_float(value: Any, default: Optional[float] = None) -> Optional[float]:
    if value is None:
        return default
    if isinstance(value, float):
        if math.isnan(value) or math.isinf(value):
            return default
        return value
    text = str(value).strip()
    if not text:
        return default
    lowered = text.lower()
    if lowered in {"nan", "none", "null"}:
        return default
    try:
        number = float(text)
        if math.isnan(number) or math.isinf(number):
            return default
        return number
    except ValueError:
        return default


def stable_hash(payload: Dict[str, Any]) -> str:
    serialized = json.dumps(payload, sort_keys=True, ensure_ascii=False)
    return hashlib.sha256(serialized.encode("utf-8")).hexdigest()


def load_manifest(path: Path) -> Dict[str, Any]:
    if not path.exists():
        return {"version": 2, "pages": {}, "slug_redirects": {}, "legacy_slugs": {}}
    try:
        data = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError:
        return {"version": 2, "pages": {}, "slug_redirects": {}, "legacy_slugs": {}}

    if "pages" not in data or not isinstance(data["pages"], dict):
        data["pages"] = {}
    if "slug_redirects" not in data or not isinstance(data["slug_redirects"], dict):
        data["slug_redirects"] = {}
    if "legacy_slugs" not in data or not isinstance(data["legacy_slugs"], dict):
        data["legacy_slugs"] = {}
    data["version"] = 2
    return data


def save_manifest(path: Path, manifest: Dict[str, Any]) -> None:
    ensure_dir(path.parent)
    path.write_text(json.dumps(manifest, indent=2, ensure_ascii=False), encoding="utf-8")


def load_config(path: Path) -> Dict[str, Any]:
    raw = path.read_text(encoding="utf-8")

    try:
        import yaml  # type: ignore

        data = yaml.safe_load(raw)
        if isinstance(data, dict):
            return data
    except Exception:
        pass

    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError(f"Invalid config structure in {path}")
    return data


def normalize_event_type(event_type: str, event_date: str) -> str:
    text = (event_type or "").strip().upper()
    if text in ALLOWED_EVENT_TYPES:
        return text

    cpi_dates = {
        "2024-03-12",
        "2024-04-10",
        "2024-05-15",
        "2024-06-12",
        "2024-07-11",
        "2024-08-14",
        "2024-09-11",
        "2024-10-10",
        "2024-11-14",
        "2024-12-11",
        "2025-01-15",
        "2025-02-12",
        "2024-02-20",
        "2024-01-15",
    }
    nfp_dates = {
        "2024-01-05",
        "2024-02-02",
        "2024-03-01",
        "2024-04-05",
        "2024-05-03",
        "2024-06-07",
        "2024-07-05",
        "2024-08-02",
        "2024-09-06",
        "2024-10-04",
        "2024-11-01",
        "2024-12-06",
        "2025-01-10",
    }
    fomc_dates = {
        "2024-01-30",
        "2024-03-19",
        "2024-04-30",
        "2024-06-11",
        "2024-07-30",
        "2024-09-17",
        "2024-11-06",
        "2024-12-17",
        "2025-01-29",
    }

    if event_date in cpi_dates:
        return "CPI"
    if event_date in nfp_dates:
        return "NFP"
    if event_date in fomc_dates:
        return "FOMC"
    return ""


def to_offer_key(asset: str, offers_config: Dict[str, Any]) -> str:
    asset_upper = asset.upper()
    keys_map = offers_config.get("asset_offer_keys", {})
    keys = keys_map.get(asset_upper) or keys_map.get("DEFAULT") or []
    if not keys:
        return "ibkr"
    return str(keys[0])


def canonical_slug(asset: str, event_type: str, event_date: str) -> str:
    return f"{asset.lower()}-after-{event_type.lower()}-{event_date}"


def cutoff_date(run_date: str) -> str:
    dt = datetime.strptime(run_date, "%Y-%m-%d")
    return (dt - timedelta(days=1)).strftime("%Y-%m-%d")
