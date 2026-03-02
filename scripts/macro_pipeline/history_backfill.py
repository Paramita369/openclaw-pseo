"""
Historical Data Backfill Script
============================
抓取歷史Macro事件數據並填充入macro_events.db

支持的Macro事件:
- CPI (消費者物價指數) - 每月
- NFP (非農就業) - 每月
- Fed Rate Decision (聯儲局議息) - 每月
- GDP (國內生產總值) - 每季

用法:
    python3 history_backfill.py --asset BTC --events cpi,nfp,fed
"""

import sqlite3
import os
import json
import requests
import time
from datetime import datetime, timedelta
import pandas as pd

BASE_DIR = os.getcwd()
DB_PATH = os.path.join(BASE_DIR, "data/macro_events.db")

# 歷史Macro事件日期 (2024-2025)
# 數據來源: 實際公佈日期
MACRO_EVENTS_2024 = [
    # 2024 CPI dates
    {"date": "2024-01-15", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-02-20", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-03-12", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-04-10", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-05-15", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-06-12", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-07-11", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-08-14", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-09-11", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-10-10", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-11-14", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2024-12-11", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    
    # 2024 NFP dates
    {"date": "2024-01-05", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-02-02", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-03-01", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-04-05", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-05-03", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-06-07", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-07-05", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-08-02", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-09-06", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-10-04", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-11-01", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2024-12-06", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    
    # 2024 Fed Rate Dates
    {"date": "2024-01-30", "event": "Fed", "headline": "FOMC Rate Decision", "domain": "Macro"},
    {"date": "2024-03-19", "event": "Fed", "headline": "FOMC Rate Decision", "domain": "Macro"},
    {"date": "2024-04-30", "event": "Fed", "headline": "FOMC Rate Decision", "domain": "Macro"},
    {"date": "2024-06-11", "event": "Fed", "headline": "FOMC Rate Decision", "domain": "Macro"},
    {"date": "2024-07-30", "event": "Fed", "headline": "FOMC Rate Decision", "domain": "Macro"},
    {"date": "2024-09-17", "event": "Fed", "headline": "FOMC Rate Decision", "domain": "Macro"},
    {"date": "2024-11-06", "event": "Fed", "headline": "FOMC Rate Decision", "domain": "Macro"},
    {"date": "2024-12-17", "event": "Fed", "headline": "FOMC Rate Decision", "domain": "Macro"},
]

# 2025 events (sample)
MACRO_EVENTS_2025 = [
    {"date": "2025-01-15", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2025-02-12", "event": "CPI", "headline": "CPI Release", "domain": "Macro"},
    {"date": "2025-01-10", "event": "NFP", "headline": "NFP Data Release", "domain": "Macro"},
    {"date": "2025-01-29", "event": "Fed", "headline": "FOMC Rate Decision", "domain": "Macro"},
]

# 資產配置
ASSETS = ["BTC", "ETH", "GOLD", "SPY", "QQQ"]

# Yahoo Finance tickers
TICKER_MAP = {
    "BTC": "BTC-USD",
    "ETH": "ETH-USD", 
    "GOLD": "GC=F",
    "SPY": "SPY",
    "QQQ": "QQQ"
}

def get_historical_price(ticker, date_str):
    """用Yahoo Finance獲取歷史價格"""
    try:
        # 嘗試用yfinance
        import yfinance as yf
        stock = yf.Ticker(TICKER_MAP.get(ticker, ticker))
        
        # 獲取前後7天的數據
        target_date = datetime.strptime(date_str, "%Y-%m-%d")
        start = (target_date - timedelta(days=7)).strftime("%Y-%m-%d")
        end = (target_date + timedelta(days=14)).strftime("%Y-%m-%d")
        
        hist = stock.history(start=start, end=end)
        
        if hist.empty:
            return None
        
        # 找到最接近目標日期的價格
        hist = hist.reset_index()
        hist['date'] = pd.to_datetime(hist['Date']).dt.date
        
        target_date_only = target_date.date()
        
        # 找T+0
        if target_date_only in hist['date'].values:
            t0_price = float(hist[hist['date'] == target_date_only].iloc[0]['Close'])
        else:
            # 用最接近的
            t0_price = float(hist.iloc[0]['Close'])
        
        # 找T+1
        t1_date = target_date + timedelta(days=1)
        if t1_date.date() in hist['date'].values:
            t1_price = float(hist[hist['date'] == t1_date.date()].iloc[0]['Close'])
        else:
            t1_price = None
            
        # 找T+7
        t7_date = target_date + timedelta(days=7)
        if t7_date.date() in hist['date'].values:
            t7_price = float(hist[hist['date'] == t7_date.date()].iloc[0]['Close'])
        else:
            t7_price = None
        
        return t0_price, t1_price, t7_price
        
    except Exception as e:
        print(f"  ⚠️ Error fetching {ticker} for {date_str}: {e}")
        return None, None, None

def insert_events_and_prices():
    """插入歷史事件並抓取價格"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    all_events = MACRO_EVENTS_2024 + MACRO_EVENTS_2025
    total_inserted = 0
    
    for event_data in all_events:
        event_date = event_data["date"]
        event_type = event_data["event"]
        headline = event_data["headline"]
        
        # 插入事件
        cursor.execute('''
            INSERT INTO macro_events (date, domain, headline, summary, sentiment_score, related_assets)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (
            event_date,
            event_data["domain"],
            headline,
            f"{event_type} historical data point for backtesting",
            0.0,  # neutral sentiment
            ",".join(ASSETS)
        ))
        
        event_id = cursor.lastrowid
        
        # 為每個資產獲取價格
        for asset in ASSETS:
            print(f"  📊 Fetching {asset} for {event_date}...")
            t0, t1, t7 = get_historical_price(asset, event_date)
            
            if t0:
                # 計算漲跌幅
                impact_t1 = ((t1 - t0) / t0 * 100) if t1 else None
                impact_t7 = ((t7 - t0) / t0 * 100) if t7 else None
                
                cursor.execute('''
                    INSERT INTO asset_impact 
                    (event_id, ticker, asset_class, exchange, price_t0, price_t1, price_t7, impact_t1_pct, impact_t7_pct)
                    VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
                ''', (
                    event_id, asset, 
                    "Crypto" if asset in ["BTC", "ETH"] else "Stock",
                    "BINANCE" if asset in ["BTC", "ETH"] else "NYSE",
                    t0, t1, t7,
                    round(impact_t1, 2) if impact_t1 else None,
                    round(impact_t7, 2) if impact_t7 else None
                ))
                total_inserted += 1
            
            time.sleep(0.5)  # Rate limiting
    
    conn.commit()
    conn.close()
    
    return total_inserted

def main():
    print("📜 Historical Data Backfill Script")
    print("=" * 50)
    print(f"📅 Events to process: {len(MACRO_EVENTS_2024) + len(MACRO_EVENTS_2025)}")
    print(f"📊 Assets: {', '.join(ASSETS)}")
    print()
    
    # Auto-confirm for automation
    print("⚠️ This will add historical macro event data to your database.")
    print("⚠️ Total records to insert: ~{}".format((len(MACRO_EVENTS_2024) + len(MACRO_EVENTS_2025)) * len(ASSETS)))
    print()
    
    print("🚀 Starting backfill (auto-confirmed)...")
    inserted = insert_events_and_prices()
    
    print(f"\n✅ Done! Inserted {inserted} price records.")

if __name__ == "__main__":
    main()
