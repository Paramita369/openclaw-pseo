#!/usr/bin/env python3
"""Generate daily KPI report from GA4 and Search Console."""

from __future__ import annotations

import argparse
import json
import os
from datetime import date, datetime, timedelta, timezone
from pathlib import Path
from typing import Dict, Optional

from pipeline_utils import resolve_project_root


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Generate KPI report")
    parser.add_argument("--project-root", default=None, help="Repository root")
    parser.add_argument("--report-date", default=(date.today() - timedelta(days=1)).isoformat(), help="Report date")
    parser.add_argument("--output", default=None, help="Output json path")
    return parser.parse_args()


def fetch_ga4(report_date: str) -> Dict[str, object]:
    property_id = os.getenv("GA4_PROPERTY_ID", "").strip()
    if not property_id:
        return {"status": "skipped", "reason": "GA4_PROPERTY_ID missing"}

    try:
        from google.analytics.data_v1beta import BetaAnalyticsDataClient
        from google.analytics.data_v1beta.types import DateRange, Dimension, Metric, RunReportRequest
    except Exception:
        return {"status": "skipped", "reason": "google-analytics-data package unavailable"}

    try:
        client = BetaAnalyticsDataClient()
        request = RunReportRequest(
            property=f"properties/{property_id}",
            dimensions=[Dimension(name="eventName")],
            metrics=[Metric(name="eventCount")],
            date_ranges=[DateRange(start_date=report_date, end_date=report_date)],
            dimension_filter={
                "filter": {
                    "field_name": "eventName",
                    "string_filter": {"match_type": "EXACT", "value": "affiliate_click"},
                }
            },
        )
        response = client.run_report(request=request)
        clicks = 0
        for row in response.rows:
            if row.dimension_values and row.dimension_values[0].value == "affiliate_click":
                clicks = int(row.metric_values[0].value)
        return {"status": "ok", "affiliate_clicks": clicks}
    except Exception as exc:
        return {"status": "error", "reason": str(exc)}


def fetch_gsc(report_date: str) -> Dict[str, object]:
    site_url = os.getenv("GSC_SITE_URL", "https://quantmacro.vercel.app/").strip()
    try:
        from googleapiclient.discovery import build
        from google.oauth2 import service_account
    except Exception:
        return {"status": "skipped", "reason": "google-api-python-client unavailable"}

    credentials_path = os.getenv("GOOGLE_APPLICATION_CREDENTIALS", "").strip()
    if not credentials_path:
        return {"status": "skipped", "reason": "GOOGLE_APPLICATION_CREDENTIALS missing"}

    try:
        credentials = service_account.Credentials.from_service_account_file(
            credentials_path,
            scopes=["https://www.googleapis.com/auth/webmasters.readonly"],
        )
        service = build("searchconsole", "v1", credentials=credentials, cache_discovery=False)
        body = {
            "startDate": report_date,
            "endDate": report_date,
            "dimensions": ["date"],
            "rowLimit": 1,
        }
        response = service.searchanalytics().query(siteUrl=site_url, body=body).execute()
        rows = response.get("rows", [])
        if not rows:
            organic = {"organic_clicks": 0, "organic_impressions": 0, "ctr": 0.0, "position": None}
        else:
            row = rows[0]
            organic = {
                "organic_clicks": int(row.get("clicks", 0)),
                "organic_impressions": int(row.get("impressions", 0)),
                "ctr": float(row.get("ctr", 0.0)),
                "position": float(row.get("position", 0.0)),
            }

        index_coverage = fetch_index_coverage(service=service, site_url=site_url)
        return {"status": "ok", **organic, "index_coverage": index_coverage}
    except Exception as exc:
        return {"status": "error", "reason": str(exc)}


def fetch_index_coverage(service: object, site_url: str) -> Dict[str, object]:
    try:
        response = service.sitemaps().list(siteUrl=site_url).execute()
        items = response.get("sitemap", []) or []
        if not items:
            return {"status": "skipped", "reason": "no_sitemaps"}

        selected: Optional[dict] = None
        for item in items:
            path = str(item.get("path", ""))
            if "sitemap.xml" in path:
                selected = item
                break
        if selected is None:
            selected = items[0]

        contents = selected.get("contents", []) or []
        submitted = 0
        indexed = 0
        for entry in contents:
            submitted += int(entry.get("submitted", 0) or 0)
            indexed += int(entry.get("indexed", 0) or 0)

        if submitted == 0 and indexed == 0:
            return {"status": "ok", "submitted": 0, "indexed": 0, "coverage_pct": 0.0}

        coverage = round((indexed / submitted) * 100, 4) if submitted else 0.0
        return {"status": "ok", "submitted": submitted, "indexed": indexed, "coverage_pct": coverage}
    except Exception as exc:
        return {"status": "error", "reason": str(exc)}


def main() -> None:
    args = parse_args()
    root = resolve_project_root(args.project_root)
    output = Path(args.output).resolve() if args.output else root / "reports" / "kpi" / f"{args.report_date}.json"

    ga4 = fetch_ga4(args.report_date)
    gsc = fetch_gsc(args.report_date)

    report = {
        "date": args.report_date,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "northstar": "affiliate_ctr",
        "ga4": ga4,
        "gsc": gsc,
    }

    clicks = ga4.get("affiliate_clicks", 0) if isinstance(ga4, dict) else 0
    organic_clicks = gsc.get("organic_clicks", 0) if isinstance(gsc, dict) else 0
    report["derived"] = {
        "affiliate_clicks": clicks,
        "organic_clicks": organic_clicks,
        "affiliate_ctr_proxy": round((clicks / organic_clicks) * 100, 4) if organic_clicks else 0.0,
    }

    output.parent.mkdir(parents=True, exist_ok=True)
    output.write_text(json.dumps(report, indent=2, ensure_ascii=False), encoding="utf-8")

    print(json.dumps({"date": args.report_date, "output": str(output), "derived": report["derived"]}, ensure_ascii=False))


if __name__ == "__main__":
    main()
