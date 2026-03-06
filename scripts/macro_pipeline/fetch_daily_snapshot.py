#!/usr/bin/env python3
"""Fetch daily market snapshot for homepage widgets."""

from __future__ import annotations

import argparse
import json
from datetime import datetime, timedelta, timezone
from pathlib import Path
from typing import Any, Dict, Optional, Tuple

try:
    from zoneinfo import ZoneInfo
except Exception:  # pragma: no cover
    ZoneInfo = None  # type: ignore

from pipeline_utils import ensure_dir, resolve_project_root

try:
    import yfinance as yf
except ImportError:  # pragma: no cover
    yf = None
try:
    import pandas_market_calendars as mcal
except Exception:  # pragma: no cover
    mcal = None


ASSETS: Dict[str, Dict[str, str]] = {
    "BTC": {"ticker": "BTC-USD", "asset_type": "crypto"},
    "ETH": {"ticker": "ETH-USD", "asset_type": "crypto"},
    "SOL": {"ticker": "SOL-USD", "asset_type": "crypto"},
    "GOLD": {"ticker": "GC=F", "asset_type": "us_session"},
    "SPY": {"ticker": "SPY", "asset_type": "us_session"},
    "QQQ": {"ticker": "QQQ", "asset_type": "us_session"},
    "DXY": {"ticker": "DX-Y.NYB", "asset_type": "us_session"},
    "VIX": {"ticker": "^VIX", "asset_type": "us_session"},
    "TNX": {"ticker": "^TNX", "asset_type": "us_session"},
}

CRYPTO_STALE_HOURS = 6.0
US_SESSION_CLOSE_GRACE_HOURS = 4.0


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Fetch daily snapshot")
    parser.add_argument("--project-root", default=None, help="Repository root")
    parser.add_argument("--output", default=None, help="Deprecated output json path (use --output-path)")
    parser.add_argument("--output-path", default=None, help="Override output json path")
    return parser.parse_args()


def to_utc_iso(value: Any) -> Optional[str]:
    if value is None:
        return None
    try:
        if hasattr(value, "to_pydatetime"):
            dt = value.to_pydatetime()
        elif isinstance(value, datetime):
            dt = value
        else:
            return None
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc).isoformat()
    except Exception:
        return None


def parse_iso_datetime(value: Any) -> Optional[datetime]:
    text = str(value or "").strip()
    if not text:
        return None
    try:
        dt = datetime.fromisoformat(text.replace("Z", "+00:00"))
        if dt.tzinfo is None:
            dt = dt.replace(tzinfo=timezone.utc)
        return dt.astimezone(timezone.utc)
    except Exception:
        return None


def fallback_entry(previous_entry: object, now_utc: datetime, *, asset_type: str) -> Optional[Dict[str, Any]]:
    if not isinstance(previous_entry, dict):
        return None
    entry = dict(previous_entry)
    entry["asset_type"] = asset_type
    entry["source"] = "fallback_cache"
    entry["freshness_status"] = "fallback"
    entry["source_quality"] = "fallback"
    entry["display_mode"] = "fallback"
    as_of_ts = parse_iso_datetime(entry.get("as_of_ts"))
    if as_of_ts:
        entry["data_age_hours"] = round((now_utc - as_of_ts).total_seconds() / 3600.0, 2)
        entry["as_of_date"] = as_of_ts.date().isoformat()
        entry["as_of_ts"] = as_of_ts.isoformat()
    else:
        entry["data_age_hours"] = None
        fallback_date = str(entry.get("as_of_date") or "").strip()
        fallback_ts = str(entry.get("as_of_ts") or "").strip()
        entry["as_of_date"] = fallback_date or now_utc.date().isoformat()
        entry["as_of_ts"] = fallback_ts or now_utc.isoformat()
    return entry


def fetch_history(ticker: str, *, period: str, interval: str):
    if yf is None:
        return None
    try:
        data = yf.Ticker(ticker).history(period=period, interval=interval, auto_adjust=False)
    except Exception:
        return None
    if data is None or data.empty:
        return None
    return data


def latest_close_timestamp(index_value: Any, *, fallback_hour: int = 0) -> Optional[datetime]:
    if hasattr(index_value, "to_pydatetime"):
        dt = index_value.to_pydatetime()
    elif isinstance(index_value, datetime):
        dt = index_value
    else:
        return None
    if dt.tzinfo is None:
        dt = dt.replace(hour=fallback_hour, minute=0, second=0, microsecond=0, tzinfo=timezone.utc)
    return dt.astimezone(timezone.utc)


def build_crypto_snapshot(name: str, ticker: str, now_utc: datetime, previous_entry: object) -> Optional[Dict[str, Any]]:
    history = fetch_history(ticker, period="2d", interval="1h")
    if history is None or len(history) == 0:
        return fallback_entry(previous_entry, now_utc, asset_type="crypto")

    latest = history.iloc[-1]
    prev = history.iloc[-2] if len(history) > 1 else latest
    latest_ts = latest_close_timestamp(history.index[-1], fallback_hour=0)
    if latest_ts is None:
        return fallback_entry(previous_entry, now_utc, asset_type="crypto")

    prev_close = float(prev["Close"]) if float(prev["Close"]) != 0 else 1.0
    pct_change = ((float(latest["Close"]) - prev_close) / prev_close) * 100
    age_hours = round((now_utc - latest_ts).total_seconds() / 3600.0, 2)

    return {
        "price": round(float(latest["Close"]), 2),
        "change": round(pct_change, 2),
        "volume": int(latest.get("Volume", 0)),
        "high": round(float(latest["High"]), 2),
        "low": round(float(latest["Low"]), 2),
        "asset_type": "crypto",
        "as_of_date": latest_ts.date().isoformat(),
        "as_of_ts": latest_ts.isoformat(),
        "data_age_hours": age_hours,
        "freshness_status": "stale" if age_hours > CRYPTO_STALE_HOURS else "fresh",
        "source": "yfinance",
        "source_quality": "live",
        "display_mode": "delayed" if age_hours > 1.0 else "live",
    }


def load_us_schedule(now_utc: datetime):
    if mcal is None:
        return None
    try:
        now_et = now_utc.astimezone(ZoneInfo("America/New_York")) if ZoneInfo else now_utc
        start = (now_et.date() - timedelta(days=21)).isoformat()
        end = (now_et.date() + timedelta(days=2)).isoformat()
        calendar = mcal.get_calendar("NYSE")
        schedule = calendar.schedule(start_date=start, end_date=end)
        return schedule
    except Exception:
        return None


def expected_us_session(schedule, now_utc: datetime) -> Tuple[Optional[str], Optional[datetime]]:
    if schedule is None or len(schedule) == 0:
        return None, None
    now_et = now_utc.astimezone(ZoneInfo("America/New_York")) if ZoneInfo else now_utc
    past = schedule[schedule.index.date <= now_et.date()]
    if len(past) == 0:
        return None, None
    session_date = past.index[-1].date().isoformat()
    close_ts = to_utc_iso(past.iloc[-1].get("market_close"))
    return session_date, parse_iso_datetime(close_ts)


def session_close_for_day(schedule, day_iso: str) -> Optional[datetime]:
    if schedule is None:
        return None
    for idx in range(len(schedule)):
        row = schedule.iloc[idx]
        session_date = schedule.index[idx].date().isoformat()
        if session_date == day_iso:
            return parse_iso_datetime(to_utc_iso(row.get("market_close")))
    return None


def build_us_session_snapshot(
    name: str,
    ticker: str,
    now_utc: datetime,
    schedule,
    previous_entry: object,
) -> Optional[Dict[str, Any]]:
    history = fetch_history(ticker, period="15d", interval="1d")
    if history is None or len(history) == 0:
        return fallback_entry(previous_entry, now_utc, asset_type="us_session")

    latest = history.iloc[-1]
    prev = history.iloc[-2] if len(history) > 1 else latest
    latest_ts = latest_close_timestamp(history.index[-1], fallback_hour=0)
    if latest_ts is None:
        return fallback_entry(previous_entry, now_utc, asset_type="us_session")

    last_bar_date = latest_ts.date().isoformat()
    expected_session_date, expected_close_ts = expected_us_session(schedule, now_utc)
    last_bar_close_ts = session_close_for_day(schedule, last_bar_date) or latest_ts

    prev_close = float(prev["Close"]) if float(prev["Close"]) != 0 else 1.0
    pct_change = ((float(latest["Close"]) - prev_close) / prev_close) * 100

    freshness_status = "calendar_unknown"
    if expected_session_date and expected_close_ts:
        stale_trigger = expected_close_ts + timedelta(hours=US_SESSION_CLOSE_GRACE_HOURS)
        is_stale = last_bar_date < expected_session_date and now_utc > stale_trigger
        freshness_status = "stale" if is_stale else "fresh"

    age_hours = round((now_utc - last_bar_close_ts).total_seconds() / 3600.0, 2)

    return {
        "price": round(float(latest["Close"]), 2),
        "change": round(pct_change, 2),
        "volume": int(latest.get("Volume", 0)),
        "high": round(float(latest["High"]), 2),
        "low": round(float(latest["Low"]), 2),
        "asset_type": "us_session",
        "as_of_date": last_bar_close_ts.date().isoformat(),
        "as_of_ts": last_bar_close_ts.isoformat(),
        "data_age_hours": age_hours,
        "freshness_status": freshness_status,
        "source": "yfinance",
        "source_quality": "calendar_unknown" if freshness_status == "calendar_unknown" else "live",
        "display_mode": "calendar_unknown" if freshness_status == "calendar_unknown" else ("delayed" if freshness_status == "stale" else "live"),
    }


def fetch_snapshot(previous: Dict[str, object] | None = None) -> Dict[str, object]:
    now_utc = datetime.now(timezone.utc)
    previous_markets = (previous or {}).get("markets", {})
    previous_markets = previous_markets if isinstance(previous_markets, dict) else {}
    results: Dict[str, Dict[str, Any]] = {}

    if yf is None:
        fallback_markets: Dict[str, Dict[str, Any]] = {}
        for name, cfg in ASSETS.items():
            previous_entry = previous_markets.get(name)
            item = fallback_entry(previous_entry, now_utc, asset_type=cfg["asset_type"])
            if item is not None:
                fallback_markets[name] = item
        return {
            "timestamp": now_utc.isoformat(),
            "markets": fallback_markets,
            "macro": {},
        }

    schedule = load_us_schedule(now_utc)
    for name, cfg in ASSETS.items():
        ticker = cfg["ticker"]
        asset_type = cfg["asset_type"]
        previous_entry = previous_markets.get(name)
        if asset_type == "crypto":
            snapshot = build_crypto_snapshot(name, ticker, now_utc, previous_entry)
        else:
            snapshot = build_us_session_snapshot(name, ticker, now_utc, schedule, previous_entry)
        if snapshot is None:
            snapshot = fallback_entry(previous_entry, now_utc, asset_type=asset_type)
        if snapshot is not None:
            results[name] = snapshot

    return {
        "timestamp": now_utc.isoformat(),
        "markets": results,
        "macro": {},
    }


def main() -> None:
    args = parse_args()
    root = resolve_project_root(args.project_root)
    output_override = args.output_path or args.output
    output = Path(output_override).resolve() if output_override else root / "src" / "daily_snapshot.json"

    previous = None
    if output.exists():
        try:
            previous = json.loads(output.read_text(encoding="utf-8"))
        except Exception:
            previous = None

    snapshot = fetch_snapshot(previous=previous)
    ensure_dir(output.parent)
    output.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"✅ Daily snapshot saved: {output}")


if __name__ == "__main__":
    main()
