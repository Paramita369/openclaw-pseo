#!/usr/bin/env python3
"""Sync CPI/NFP/FOMC event calendar from FRED + override file."""

from __future__ import annotations

import argparse
import csv
import json
import os
import sqlite3
from dataclasses import dataclass
from datetime import date, datetime, timedelta
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence, Set, Tuple

from pipeline_utils import ALLOWED_EVENT_TYPES, PRIMARY_ASSETS, cutoff_date, event_filter_sql, resolve_project_root
from fred_policy import enforce_fred_api_requirement

try:
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
except Exception:  # pragma: no cover
    requests = None  # type: ignore
    HTTPAdapter = None  # type: ignore
    Retry = None  # type: ignore
try:
    import yfinance as yf
except Exception:  # pragma: no cover
    yf = None


EVENT_SERIES = {
    "CPI": "CPIAUCSL",
    "NFP": "PAYEMS",
    "FOMC": "DFEDTARU",
}
EVENT_HEADLINES = {
    "CPI": "CPI Release",
    "NFP": "NFP Data Release",
    "FOMC": "FOMC Rate Decision",
}
CALENDAR_START_DATE = "2024-01-01"
DEFAULT_LOOKBACK_DAYS = 90

ASSET_META = {
    "BTC": ("Crypto", "BINANCE", "BTC-USD"),
    "ETH": ("Crypto", "BINANCE", "ETH-USD"),
    "GOLD": ("Commodity", "FX", "GC=F"),
    "QQQ": ("Stock", "NASDAQ", "QQQ"),
    "SPY": ("Stock", "NYSE", "SPY"),
}
FETCH_DIAGNOSTICS: List[Dict[str, str]] = []


@dataclass
class OverrideRow:
    event_type: str
    event_date: str
    status: str
    source: str
    release_ref: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Sync event calendar from FRED + overrides")
    parser.add_argument("--project-root", default=".", help="Repository root")
    parser.add_argument("--db-path", default=None, help="Path to macro_events.db")
    parser.add_argument("--as-of-date", default=date.today().isoformat(), help="Run date (YYYY-MM-DD)")
    parser.add_argument("--provider", default="fred", choices=["fred"], help="Calendar provider")
    parser.add_argument(
        "--override-file",
        default=None,
        help="Override CSV path (default: data/event_overrides.csv)",
    )
    parser.add_argument("--strict", action="store_true", help="Fail when recent event pool is stale")
    parser.add_argument("--lookback-days", type=int, default=DEFAULT_LOOKBACK_DAYS, help="Freshness lookback window")
    return parser.parse_args()


def ensure_schema(conn: sqlite3.Connection) -> None:
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS event_calendar (
          event_type TEXT NOT NULL,
          event_date TEXT NOT NULL,
          source TEXT NOT NULL,
          status TEXT NOT NULL,
          release_ref TEXT,
          created_at TEXT DEFAULT CURRENT_TIMESTAMP,
          updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
          PRIMARY KEY(event_type, event_date)
        )
        """
    )
    cursor.execute(
        "CREATE INDEX IF NOT EXISTS idx_event_calendar_date ON event_calendar(event_date, event_type, status)"
    )
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_macro_events_date ON macro_events(date)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_macro_events_headline ON macro_events(headline, date)")
    cursor.execute("CREATE INDEX IF NOT EXISTS idx_asset_impact_event_ticker ON asset_impact(event_id, ticker)")
    conn.commit()


def valid_iso_date(value: str) -> bool:
    if not isinstance(value, str) or len(value) != 10:
        return False
    try:
        datetime.strptime(value, "%Y-%m-%d")
        return True
    except ValueError:
        return False


def get_fred_session():
    if requests is None:
        return None
    session = requests.Session()
    if Retry is not None and HTTPAdapter is not None:
        retries = Retry(
            total=3,
            connect=3,
            read=3,
            backoff_factor=1,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods={"GET"},
            raise_on_status=False,
        )
        session.mount("https://", HTTPAdapter(max_retries=retries))
    return session


def record_fetch_issue(event: str, series_id: str, code: str, detail: str) -> None:
    FETCH_DIAGNOSTICS.append(
        {
            "event": event,
            "series_id": series_id,
            "code": code,
            "detail": detail[:280],
        }
    )


def fetch_json(url: str) -> Dict[str, object]:
    if requests is None:
        raise RuntimeError("requests_unavailable")
    session = get_fred_session()
    if session is None:
        raise RuntimeError("fred_session_unavailable")
    response = session.get(url, timeout=30)
    response.raise_for_status()
    payload = response.json()
    if not isinstance(payload, dict):
        raise RuntimeError("invalid_json_payload")
    return payload


def fred_api(path: str, params: Dict[str, str], api_key: str) -> Dict[str, object]:
    payload = dict(params)
    payload["file_type"] = "json"
    if api_key:
        payload["api_key"] = api_key
    if requests is None:
        raise RuntimeError("requests_unavailable")
    query = requests.compat.urlencode(payload)
    url = f"https://api.stlouisfed.org{path}?{query}"
    return fetch_json(url)


def parse_fred_csv(series_id: str) -> List[Tuple[str, float]]:
    url = f"https://fred.stlouisfed.org/graph/fredgraph.csv?id={series_id}"
    if requests is None:
        record_fetch_issue("fred_csv", series_id, "requests_unavailable", "requests import failed")
        return []
    session = get_fred_session()
    if session is None:
        record_fetch_issue("fred_csv", series_id, "fred_session_unavailable", "unable to init requests session")
        return []
    try:
        response = session.get(url, timeout=30)
        response.raise_for_status()
        raw = response.text
    except Exception as exc:
        code = "network_error"
        if isinstance(exc, requests.Timeout):
            code = "timeout"
        elif isinstance(exc, requests.HTTPError):
            status = exc.response.status_code if exc.response is not None else "unknown"
            code = f"http_{status}"
        record_fetch_issue("fred_csv", series_id, code, str(exc))
        return []
    rows: List[Tuple[str, float]] = []
    reader = csv.DictReader(raw.splitlines())
    for item in reader:
        obs_date = str(item.get("DATE") or "").strip()
        value_raw = str(item.get(series_id) or "").strip()
        if not valid_iso_date(obs_date) or value_raw in {"", ".", "nan", "NaN"}:
            continue
        try:
            rows.append((obs_date, float(value_raw)))
        except ValueError:
            continue
    return rows


def fetch_series_observations(series_id: str, api_key: str) -> List[Tuple[str, float]]:
    try:
        payload = fred_api(
            "/fred/series/observations",
            {
                "series_id": series_id,
                "sort_order": "asc",
                "observation_start": CALENDAR_START_DATE,
            },
            api_key,
        )
    except Exception as exc:
        code = "network_error"
        if requests is not None and isinstance(exc, requests.Timeout):
            code = "timeout"
        elif requests is not None and isinstance(exc, requests.HTTPError):
            status = exc.response.status_code if exc.response is not None else "unknown"
            code = f"http_{status}"
        record_fetch_issue("fred_api", series_id, code, str(exc))
        return parse_fred_csv(series_id)

    rows: List[Tuple[str, float]] = []
    for item in payload.get("observations", []):
        obs_date = str(item.get("date", "")).strip()
        value_raw = str(item.get("value", "")).strip()
        if not valid_iso_date(obs_date) or value_raw in {"", ".", "nan", "NaN"}:
            continue
        try:
            rows.append((obs_date, float(value_raw)))
        except ValueError:
            continue
    if not rows:
        record_fetch_issue("fred_api", series_id, "empty_payload", "observations payload empty after filtering")
        return parse_fred_csv(series_id)
    return rows


def fetch_release_dates_for_series(series_id: str, api_key: str) -> List[str]:
    try:
        payload = fred_api("/fred/series/release", {"series_id": series_id}, api_key)
    except Exception as exc:
        code = "network_error"
        if requests is not None and isinstance(exc, requests.Timeout):
            code = "timeout"
        elif requests is not None and isinstance(exc, requests.HTTPError):
            status = exc.response.status_code if exc.response is not None else "unknown"
            code = f"http_{status}"
        record_fetch_issue("fred_release", series_id, code, str(exc))
        return []
    releases = payload.get("releases", []) or []
    if not releases:
        record_fetch_issue("fred_release", series_id, "empty_payload", "release payload missing")
        return []
    release_id = releases[0].get("id")
    if release_id is None:
        record_fetch_issue("fred_release", series_id, "missing_release_id", "release id unavailable")
        return []
    try:
        dates_payload = fred_api(
            "/fred/release/dates",
            {
                "release_id": str(release_id),
                "sort_order": "asc",
                "include_release_dates_with_no_data": "true",
            },
            api_key,
        )
    except Exception as exc:
        code = "network_error"
        if requests is not None and isinstance(exc, requests.Timeout):
            code = "timeout"
        elif requests is not None and isinstance(exc, requests.HTTPError):
            status = exc.response.status_code if exc.response is not None else "unknown"
            code = f"http_{status}"
        record_fetch_issue("fred_release_dates", series_id, code, str(exc))
        return []
    dates: List[str] = []
    for row in dates_payload.get("release_dates", []) or []:
        value = str(row.get("date", "")).strip()
        if valid_iso_date(value):
            dates.append(value)
    if not dates:
        record_fetch_issue("fred_release_dates", series_id, "empty_payload", "no valid release dates")
    return dates


def derive_release_dates_from_observations(series_id: str, event_type: str, api_key: str) -> List[str]:
    rows = fetch_series_observations(series_id, api_key)
    lag_days = 42 if event_type == "CPI" else 35
    output: List[str] = []
    for obs_date, _ in rows:
        obs_dt = datetime.strptime(obs_date, "%Y-%m-%d").date()
        release_dt = obs_dt + timedelta(days=lag_days)
        while release_dt.weekday() >= 5:
            release_dt = release_dt + timedelta(days=1)
        output.append(release_dt.isoformat())
    return output


def monthly_fallback_dates(event_type: str, start_date: str, as_of_cutoff: str) -> List[str]:
    start_dt = datetime.strptime(start_date, "%Y-%m-%d").date()
    cutoff_dt = datetime.strptime(as_of_cutoff, "%Y-%m-%d").date()
    year = start_dt.year
    month = start_dt.month
    output: List[str] = []

    def first_friday(y: int, m: int) -> date:
        day = date(y, m, 1)
        while day.weekday() != 4:
            day = day + timedelta(days=1)
        return day

    while True:
        if month == 12:
            next_month_year = year + 1
            next_month = 1
        else:
            next_month_year = year
            next_month = month + 1
        year, month = next_month_year, next_month

        if event_type == "CPI":
            candidate = date(year, month, 12)
        else:
            candidate = first_friday(year, month)

        if candidate > cutoff_dt:
            break
        output.append(candidate.isoformat())

    return output


def fetch_macro_event_dates(conn: sqlite3.Connection, event_type: str, as_of_cutoff: str) -> List[str]:
    cursor = conn.cursor()
    cursor.execute(
        f"""
        SELECT DISTINCT m.date
        FROM macro_events m
        WHERE m.date <= ?
          AND {event_filter_sql(event_type)}
        ORDER BY m.date ASC
        """,
        (as_of_cutoff,),
    )
    return [str(row[0]) for row in cursor.fetchall()]


def load_overrides(path: Path, as_of_cutoff: str) -> List[OverrideRow]:
    if not path.exists():
        return []

    rows: List[OverrideRow] = []
    with path.open("r", encoding="utf-8", newline="") as handle:
        reader = csv.DictReader(handle)
        for item in reader:
            event_type = str(item.get("event_type", "")).strip().upper()
            event_date = str(item.get("event_date", "")).strip()
            if event_type not in ALLOWED_EVENT_TYPES:
                continue
            if not valid_iso_date(event_date):
                continue
            if event_date > as_of_cutoff or event_date < CALENDAR_START_DATE:
                continue
            status = str(item.get("status", "confirmed")).strip().lower() or "confirmed"
            source = str(item.get("source", "override")).strip() or "override"
            release_ref = str(item.get("release_ref", "")).strip()
            rows.append(
                OverrideRow(
                    event_type=event_type,
                    event_date=event_date,
                    status=status,
                    source=source,
                    release_ref=release_ref,
                )
            )
    return rows


def first_close_on_or_after(data, target_day: datetime.date) -> Optional[float]:
    if data.empty:
        return None
    for idx in range(len(data)):
        row = data.iloc[idx]
        day = row["date"]
        if day >= target_day:
            return float(row["Close"])
    return None


def first_close_on_or_before(data, target_day: datetime.date) -> Optional[float]:
    if data.empty:
        return None
    selected: Optional[float] = None
    for idx in range(len(data)):
        row = data.iloc[idx]
        day = row["date"]
        if day <= target_day:
            selected = float(row["Close"])
        else:
            break
    return selected


def fetch_price_windows(ticker: str, event_date: str, as_of_cutoff: str) -> Tuple[Optional[float], Optional[float], Optional[float], Optional[float]]:
    if yf is None:
        return None, None, None, None

    base = datetime.strptime(event_date, "%Y-%m-%d")
    cutoff_dt = datetime.strptime(as_of_cutoff, "%Y-%m-%d")
    end_dt = min(base + timedelta(days=14), cutoff_dt + timedelta(days=1))
    start = (base - timedelta(days=7)).strftime("%Y-%m-%d")
    end = (end_dt + timedelta(days=1)).strftime("%Y-%m-%d")

    try:
        hist = yf.Ticker(ticker).history(start=start, end=end)
    except Exception:
        return None, None, None, None
    if hist.empty:
        return None, None, None, None

    frame = hist.reset_index()
    frame["date"] = frame["Date"].dt.date
    frame = frame[["date", "Close"]].sort_values("date")

    d0 = first_close_on_or_before(frame, base.date()) or first_close_on_or_after(frame, base.date())
    d1 = first_close_on_or_after(frame, (base + timedelta(days=1)).date())
    d3 = first_close_on_or_after(frame, (base + timedelta(days=3)).date())
    d7 = first_close_on_or_after(frame, (base + timedelta(days=7)).date())
    return d0, d1, d3, d7


def percent_change(base: Optional[float], value: Optional[float]) -> Optional[float]:
    if base is None or value is None or base == 0:
        return None
    return round(((value - base) / base) * 100, 4)


def ensure_asset_impact_rows(
    conn: sqlite3.Connection,
    event_id: int,
    event_date: str,
    as_of_cutoff: str,
) -> int:
    cursor = conn.cursor()
    inserted = 0
    for asset in PRIMARY_ASSETS:
        cursor.execute(
            "SELECT 1 FROM asset_impact WHERE event_id = ? AND ticker = ? LIMIT 1",
            (event_id, asset),
        )
        if cursor.fetchone():
            continue

        asset_class, exchange, provider_ticker = ASSET_META.get(asset, ("Unknown", "UNKNOWN", asset))
        p0, p1, p3, p7 = fetch_price_windows(provider_ticker, event_date, as_of_cutoff)
        if p0 is None:
            continue

        cursor.execute(
            """
            INSERT INTO asset_impact (
              event_id, ticker, asset_class, exchange,
              price_t0, price_t1, price_t3, price_t7,
              impact_t1_pct, impact_t3_pct, impact_t7_pct,
              updated_at
            )
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, CURRENT_TIMESTAMP)
            """,
            (
                event_id,
                asset,
                asset_class,
                exchange,
                p0,
                p1,
                p3,
                p7,
                percent_change(p0, p1),
                percent_change(p0, p3),
                percent_change(p0, p7),
            ),
        )
        inserted += 1
    conn.commit()
    return inserted


def upsert_event_calendar(
    conn: sqlite3.Connection,
    event_type: str,
    event_date: str,
    source: str,
    status: str,
    release_ref: str,
) -> None:
    cursor = conn.cursor()
    cursor.execute(
        """
        INSERT INTO event_calendar (
          event_type, event_date, source, status, release_ref, created_at, updated_at
        ) VALUES (?, ?, ?, ?, ?, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP)
        ON CONFLICT(event_type, event_date)
        DO UPDATE SET
          source = excluded.source,
          status = excluded.status,
          release_ref = excluded.release_ref,
          updated_at = CURRENT_TIMESTAMP
        """,
        (event_type, event_date, source, status, release_ref),
    )
    conn.commit()


def ensure_macro_event(conn: sqlite3.Connection, event_type: str, event_date: str) -> Tuple[int, bool]:
    headline = EVENT_HEADLINES[event_type]
    cursor = conn.cursor()
    cursor.execute(
        """
        SELECT event_id
        FROM macro_events
        WHERE date = ? AND headline = ?
        ORDER BY event_id DESC
        LIMIT 1
        """,
        (event_date, headline),
    )
    existing = cursor.fetchone()
    if existing:
        return int(existing[0]), False

    cursor.execute(
        """
        INSERT INTO macro_events (date, domain, headline, summary, sentiment_score, related_assets, metadata)
        VALUES (?, 'Macro', ?, ?, 0.0, ?, ?)
        """,
        (
            event_date,
            headline,
            f"{event_type} scheduled release auto-synced from calendar",
            ",".join(PRIMARY_ASSETS),
            json.dumps({"source": "sync_event_calendar"}),
        ),
    )
    conn.commit()
    return int(cursor.lastrowid), True


def collect_event_dates(
    conn: sqlite3.Connection,
    as_of_cutoff: str,
    api_key: str,
    overrides: Sequence[OverrideRow],
) -> Tuple[Dict[str, Set[str]], Dict[Tuple[str, str], Tuple[str, str, str]]]:
    event_dates: Dict[str, Set[str]] = {event: set() for event in sorted(ALLOWED_EVENT_TYPES)}
    source_map: Dict[Tuple[str, str], Tuple[str, str, str]] = {}

    for event_type in sorted(ALLOWED_EVENT_TYPES):
        for date_value in fetch_macro_event_dates(conn, event_type, as_of_cutoff):
            if date_value < CALENDAR_START_DATE:
                continue
            event_dates[event_type].add(date_value)
            source_map[(event_type, date_value)] = ("macro_events", "confirmed", "")

    for event_type in ("CPI", "NFP"):
        series_id = EVENT_SERIES[event_type]
        try:
            release_dates = fetch_release_dates_for_series(series_id, api_key)
        except Exception:
            release_dates = []
        if not release_dates:
            release_dates = derive_release_dates_from_observations(series_id, event_type, api_key)
        for date_value in release_dates:
            if date_value < CALENDAR_START_DATE or date_value > as_of_cutoff:
                continue
            event_dates[event_type].add(date_value)
            source_map[(event_type, date_value)] = ("fred_release_dates", "confirmed", series_id)

        latest_known = max(event_dates[event_type]) if event_dates[event_type] else ""
        if latest_known:
            for date_value in monthly_fallback_dates(event_type, latest_known, as_of_cutoff):
                if date_value < CALENDAR_START_DATE or date_value > as_of_cutoff:
                    continue
                if date_value in event_dates[event_type]:
                    continue
                event_dates[event_type].add(date_value)
                source_map[(event_type, date_value)] = ("synthetic_monthly_calendar", "estimated", series_id)

    # FOMC fallback from rate-change days (captures only change meetings), override fills the full schedule.
    series_rows = fetch_series_observations(EVENT_SERIES["FOMC"], api_key)
    previous_value: Optional[float] = None
    for obs_date, obs_value in series_rows:
        if obs_date < CALENDAR_START_DATE or obs_date > as_of_cutoff:
            previous_value = obs_value
            continue
        if previous_value is None:
            previous_value = obs_value
            continue
        if obs_value != previous_value:
            event_dates["FOMC"].add(obs_date)
            source_map[("FOMC", obs_date)] = ("fred_rate_change", "confirmed", EVENT_SERIES["FOMC"])
        previous_value = obs_value

    for row in overrides:
        key = (row.event_type, row.event_date)
        if row.status in {"disabled", "skip"}:
            event_dates[row.event_type].discard(row.event_date)
            source_map[key] = (row.source, row.status, row.release_ref)
            continue
        event_dates[row.event_type].add(row.event_date)
        source_map[key] = (row.source, row.status, row.release_ref)

    return event_dates, source_map


def assert_recent_pool(
    event_dates: Dict[str, Set[str]],
    as_of_cutoff: str,
    lookback_days: int,
) -> None:
    cutoff_dt = datetime.strptime(as_of_cutoff, "%Y-%m-%d").date()
    threshold = cutoff_dt - timedelta(days=lookback_days)
    stale: List[str] = []
    for event_type in sorted(ALLOWED_EVENT_TYPES):
        dates = sorted(event_dates.get(event_type, set()))
        if not dates:
            stale.append(f"{event_type}:missing")
            continue
        latest = datetime.strptime(dates[-1], "%Y-%m-%d").date()
        if latest < threshold:
            stale.append(f"{event_type}:{latest.isoformat()}")
    if stale:
        joined = ", ".join(stale)
        raise SystemExit(f"Event pool freshness violation (>{lookback_days} days): {joined}")


def main() -> None:
    args = parse_args()
    root = resolve_project_root(args.project_root)
    db_path = Path(args.db_path).resolve() if args.db_path else root / "data" / "macro_events.db"
    override_path = (
        Path(args.override_file).resolve()
        if args.override_file
        else (root / "data" / "event_overrides.csv")
    )
    as_of_cutoff = cutoff_date(args.as_of_date)
    fred_api_key = os.getenv("FRED_API_KEY", "").strip()
    FETCH_DIAGNOSTICS.clear()

    conn = sqlite3.connect(db_path)
    try:
        ensure_schema(conn)
        overrides = load_overrides(override_path, as_of_cutoff)
        event_dates, source_map = collect_event_dates(conn, as_of_cutoff, fred_api_key, overrides)

        enforce_fred_api_requirement(
            strict=args.strict,
            fred_api_key=fred_api_key,
            fetch_statuses={'calendar': 'api' if not FETCH_DIAGNOSTICS else 'fallback'},
        )

        calendar_upserts = 0
        new_events = 0
        new_impacts = 0
        for event_type in sorted(ALLOWED_EVENT_TYPES):
            for event_date in sorted(event_dates.get(event_type, set())):
                source, status, release_ref = source_map.get((event_type, event_date), ("sync", "confirmed", ""))
                if status in {"disabled", "skip"}:
                    continue

                upsert_event_calendar(conn, event_type, event_date, source, status, release_ref)
                calendar_upserts += 1

                event_id, inserted = ensure_macro_event(conn, event_type, event_date)
                if inserted:
                    new_events += 1
                new_impacts += ensure_asset_impact_rows(conn, event_id, event_date, as_of_cutoff)

        if args.strict:
            assert_recent_pool(event_dates, as_of_cutoff, args.lookback_days)
    finally:
        conn.close()

    summary = {
        "cutoff": as_of_cutoff,
        "calendar_rows": sum(len(values) for values in event_dates.values()),
        "calendar_upserts": calendar_upserts,
        "new_macro_events": new_events,
        "new_asset_impacts": new_impacts,
        "override_file": str(override_path),
        "fetch_diagnostics_count": len(FETCH_DIAGNOSTICS),
        "fetch_diagnostics": FETCH_DIAGNOSTICS[:15],
    }
    print(json.dumps(summary, ensure_ascii=False))


if __name__ == "__main__":
    main()
