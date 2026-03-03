#!/usr/bin/env python3
"""Crawler access contract check for production URLs."""

from __future__ import annotations

import argparse
import json
import re
from datetime import datetime, timezone
from urllib.error import HTTPError, URLError
from urllib.request import Request, urlopen
from typing import Dict, List

BLOCKED_X_ROBOTS_TOKENS = {"noindex", "noai", "nosnippet", "none"}
USER_AGENTS = {
    "googlebot": "Googlebot/2.1 (+http://www.google.com/bot.html)",
    "google_extended": "Google-Extended",
}
CHECK_PATHS = ["/", "/robots.txt", "/sitemap.xml", "/sitemap-index.xml"]


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate crawler accessibility for production URLs")
    parser.add_argument("--base-url", default="https://quantmacro.vercel.app", help="Base site URL")
    parser.add_argument("--timeout", type=int, default=20, help="Request timeout seconds")
    parser.add_argument("--strict", action="store_true", help="Exit non-zero on any violation")
    parser.add_argument("--report", default=None, help="Optional JSON output file")
    return parser.parse_args()


def normalize_base_url(value: str) -> str:
    text = str(value or "").strip().rstrip("/")
    if not text:
        return "https://quantmacro.vercel.app"
    if not text.startswith("http://") and not text.startswith("https://"):
        return f"https://{text}"
    return text


def has_blocked_x_robots(value: str) -> bool:
    tokens = {part.strip().lower() for part in value.split(",") if part.strip()}
    return any(token in BLOCKED_X_ROBOTS_TOKENS for token in tokens)


def fetch_url(url: str, user_agent: str, timeout: int) -> Dict[str, object]:
    request = Request(url=url, headers={"User-Agent": user_agent}, method="GET")
    try:
        with urlopen(request, timeout=timeout) as response:
            body = response.read().decode("utf-8", errors="replace")
            headers = {key.lower(): value for key, value in response.headers.items()}
            return {
                "status": int(getattr(response, "status", 200)),
                "body": body,
                "headers": headers,
                "error": "",
            }
    except HTTPError as exc:
        return {
            "status": int(exc.code),
            "body": "",
            "headers": {key.lower(): value for key, value in exc.headers.items()} if exc.headers else {},
            "error": str(exc),
        }
    except URLError as exc:
        return {"status": None, "body": "", "headers": {}, "error": str(exc)}
    except Exception as exc:  # pragma: no cover
        return {"status": None, "body": "", "headers": {}, "error": str(exc)}


def check_urls(base_url: str, timeout: int) -> Dict[str, object]:
    violations: List[str] = []
    checks: List[Dict[str, object]] = []

    for agent_name, agent_value in USER_AGENTS.items():
        headers = {"User-Agent": agent_value}
        for path in CHECK_PATHS:
            url = f"{base_url}{path}"
            status = None
            x_robots_tag = ""
            error = ""
            response = fetch_url(url=url, user_agent=agent_value, timeout=timeout)
            status = response["status"]
            x_robots_tag = str(response["headers"].get("x-robots-tag", "")).strip()
            error = str(response["error"] or "")
            if status != 200:
                violations.append(f"status_not_200:{agent_name}:{path}:{status}")
            if x_robots_tag and has_blocked_x_robots(x_robots_tag):
                violations.append(f"blocked_x_robots:{agent_name}:{path}:{x_robots_tag}")
            if error:
                violations.append(f"request_failed:{agent_name}:{path}:{error}")

            checks.append(
                {
                    "agent": agent_name,
                    "path": path,
                    "url": url,
                    "status": status,
                    "x_robots_tag": x_robots_tag,
                    "error": error,
                }
            )

    robots_url = f"{base_url}/robots.txt"
    robots_text = ""
    robots_error = ""
    robots_response = fetch_url(robots_url, USER_AGENTS["googlebot"], timeout=timeout)
    if robots_response["status"] == 200:
        robots_text = str(robots_response["body"] or "")
    else:
        robots_error = str(robots_response["error"] or f"status={robots_response['status']}")
        violations.append(f"robots_fetch_failed:{robots_error}")

    if robots_text:
        lowered = robots_text.lower()
        if "user-agent: google-extended" in lowered:
            blocked_google_extended = re.search(
                r"user-agent:\s*google-extended[\s\S]*?disallow:\s*/",
                lowered,
            )
            if blocked_google_extended:
                violations.append("robots_disallow_google_extended")

    return {
        "base_url": base_url,
        "generated_at": datetime.now(timezone.utc).isoformat(),
        "checks": checks,
        "robots_url": robots_url,
        "robots_error": robots_error,
        "violations": sorted(set(violations)),
        "total_violations": len(set(violations)),
    }


def main() -> None:
    args = parse_args()
    base_url = normalize_base_url(args.base_url)
    result = check_urls(base_url=base_url, timeout=args.timeout)

    if args.report:
        with open(args.report, "w", encoding="utf-8") as handle:
            json.dump(result, handle, indent=2, ensure_ascii=False)

    print(json.dumps({"base_url": result["base_url"], "total_violations": result["total_violations"]}, ensure_ascii=False))

    if args.strict and int(result["total_violations"]) > 0:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
