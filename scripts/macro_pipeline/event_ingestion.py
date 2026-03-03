"""
Event Ingestion Pipeline
========================
將每日重大新聞寫入資料庫，並初始化影響力追蹤表。

Usage:
    python3 event_ingestion.py --domain "Crypto" --headline "BTC ETF approved" --summary "..." --sentiment 0.8 --assets "BTC,ETH"
"""

import sqlite3
import json
import os
import argparse
from datetime import datetime

from pipeline_utils import resolve_project_root

DB_PATH = str(resolve_project_root(None) / "data" / "macro_events.db")

# Domain enumeration
DOMAINS = ["AI", "Crypto", "Macro", "Geopolitics", "TechStock", "Commodity"]

# Asset to class mapping
ASSET_CLASS_MAP = {
    "BTC": ("Crypto", "BINANCE"),
    "ETH": ("Crypto", "BINANCE"),
    "SOL": ("Crypto", "BINANCE"),
    "XRP": ("Crypto", "BINANCE"),
    "GOLD": ("Commodity", "FX"),
    "OIL": ("Commodity", "FX"),
    "AAPL": ("Stock", "NASDAQ"),
    "NVDA": ("Stock", "NASDAQ"),
    "MSFT": ("Stock", "NASDAQ"),
    "GOOGL": ("Stock", "NASDAQ"),
    "TSLA": ("Stock", "NASDAQ"),
    "QQQ": ("Stock", "NASDAQ"),
    "SPY": ("Stock", "NYSE"),
    "HK-0700": ("Stock", "HKEX"),
    "HK-9988": ("Stock", "HKEX"),
}

def get_asset_class(ticker: str) -> tuple:
    """返回 (asset_class, exchange)"""
    return ASSET_CLASS_MAP.get(ticker, ("Unknown", "UNKNOWN"))

def log_daily_event(
    domain: str,
    headline: str,
    summary: str,
    sentiment: float,
    assets: list,
    metadata: dict = None
) -> dict:
    """
    將每日重大新聞寫入資料庫，並初始化影響力追蹤表。
    
    Args:
        domain: AI, Crypto, Macro, Geopolitics, TechStock, Commodity
        headline: 新聞標題
        summary: 摘要
        sentiment: -1.0 (極空) to 1.0 (極多)
        assets: 相關資產列表 e.g. ["BTC", "GOLD"]
        metadata: 額外信息 (source, author, etc.)
    
    Returns:
        {"status": "success", "event_id": int, "tracked_assets": list}
    """
    if domain not in DOMAINS:
        raise ValueError(f"Invalid domain. Must be one of: {DOMAINS}")
    
    if not -1.0 <= sentiment <= 1.0:
        raise ValueError("sentiment must be between -1.0 and 1.0")
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    today = datetime.now().strftime('%Y-%m-%d')
    
    # 1. 寫入新聞主表
    cursor.execute('''
        INSERT INTO macro_events (date, domain, headline, summary, sentiment_score, related_assets, metadata)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    ''', (
        today,
        domain,
        headline,
        summary,
        sentiment,
        ",".join(assets),
        json.dumps(metadata) if metadata else None
    ))
    
    event_id = cursor.lastrowid
    
    # 2. 建立資產追蹤記錄 (T+0價格稍後由price_fetcher填補)
    for asset in assets:
        asset_class, exchange = get_asset_class(asset)
        cursor.execute('''
            INSERT INTO asset_impact (event_id, ticker, asset_class, exchange)
            VALUES (?, ?, ?, ?)
        ''', (event_id, asset, asset_class, exchange))
    
    conn.commit()
    conn.close()
    
    return {
        "status": "success",
        "event_id": event_id,
        "tracked_assets": assets,
        "date": today
    }

def get_recent_events(limit: int = 10, domain: str = None) -> list:
    """查詢最近的事件"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    if domain:
        cursor.execute('''
            SELECT * FROM macro_events 
            WHERE domain = ?
            ORDER BY date DESC, event_id DESC
            LIMIT ?
        ''', (domain, limit))
    else:
        cursor.execute('''
            SELECT * FROM macro_events 
            ORDER BY date DESC, event_id DESC
            LIMIT ?
        ''', (limit,))
    
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results

def main():
    parser = argparse.ArgumentParser(description="Event Ingestion Pipeline")
    parser.add_argument("--project-root", default=None, help="Repository root")
    parser.add_argument("--db-path", default=None, help="Database path")
    parser.add_argument("--domain", required=True, choices=DOMAINS, help="Event domain")
    parser.add_argument("--headline", required=True, help="News headline")
    parser.add_argument("--summary", default="", help="News summary")
    parser.add_argument("--sentiment", type=float, default=0.0, 
                        help="Sentiment score (-1.0 to 1.0)")
    parser.add_argument("--assets", required=True, help="Comma-separated assets (e.g., BTC,ETH)")
    parser.add_argument("--source", default="manual", help="News source")
    
    args = parser.parse_args()
    
    root = resolve_project_root(args.project_root)
    db_path = args.db_path or str(root / "data" / "macro_events.db")
    global DB_PATH
    DB_PATH = db_path

    assets = [a.strip() for a in args.assets.split(",")]
    metadata = {"source": args.source}
    
    result = log_daily_event(
        domain=args.domain,
        headline=args.headline,
        summary=args.summary,
        sentiment=args.sentiment,
        assets=assets,
        metadata=metadata
    )
    
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
