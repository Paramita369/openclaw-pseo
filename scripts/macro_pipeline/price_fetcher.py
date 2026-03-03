"""
Price Fetcher Pipeline (Enhanced)
================================
支援 Crypto + Stock (US/HK) + Commodity 既價格獲取

Usage:
    python3 price_fetcher.py --update-all      # 更新所有pending記錄
    python3 price_fetcher.py --fetch-symbol SPY  # 獲取特定標的
    python3 price_fetcher.py --dry-run         # 測試模式
"""

import sqlite3
import json
import os
import argparse
import time
import random
from datetime import datetime, timedelta

from pipeline_utils import resolve_project_root

DB_PATH = str(resolve_project_root(None) / "data" / "macro_events.db")

# Try to import APIs
try:
    import yfinance as yf
    YF_AVAILABLE = True
except ImportError:
    YF_AVAILABLE = False
    print("⚠️ yfinance not installed: pip install yfinance")

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

def get_crypto_price(coin_id: str, date: str) -> float:
    """從 CoinGecko 獲取歷史價格"""
    if not REQUESTS_AVAILABLE:
        return None
    
    url = f"https://api.coingecko.com/api/v3/coins/{coin_id}/history"
    params = {"date": date, "localization": "false"}
    
    try:
        response = requests.get(url, params=params, timeout=10)
        if response.status_code == 200:
            data = response.json()
            return data.get("market_data", {}).get("current_price", {}).get("usd")
        elif response.status_code == 429:
            print(f"⚠️ Rate limited")
            time.sleep(60)
    except Exception as e:
        print(f"❌ Error: {e}")
    return None

def get_stock_price(yahoo_code: str, target_date: str = None) -> dict:
    """從 yfinance 獲取股票/指數價格"""
    if not YF_AVAILABLE:
        return None
    
    try:
        stock = yf.Ticker(yahoo_code)
        
        if target_date:
            # Get specific date
            target_dt = datetime.strptime(target_date, '%Y-%m-%d')
            start = (target_dt - timedelta(days=7)).strftime('%Y-%m-%d')
            end = (target_dt + timedelta(days=1)).strftime('%Y-%m-%d')
            hist = stock.history(start=start, end=end)
            
            if hist.empty:
                return None
            
            # Find closest date
            hist['date'] = hist.index.date
            target_date_only = target_dt.date()
            
            if target_date_only in hist['date'].values:
                row = hist[hist['date'] == target_date_only].iloc[0]
            else:
                row = hist.iloc[0]
            
            return {
                "open": float(row['Open']),
                "high": float(row['High']),
                "low": float(row['Low']),
                "close": float(row['Close']),
                "volume": int(row['Volume'])
            }
        else:
            # Get latest
            hist = stock.history(period="1d")
            if hist.empty:
                return None
            
            row = hist.iloc[0]
            return {
                "open": float(row['Open']),
                "high": float(row['High']),
                "low": float(row['Low']),
                "close": float(row['Close']),
                "volume": int(row['Volume'])
            }
    except Exception as e:
        print(f"❌ Error {yahoo_code}: {e}")
        return None

def calculate_impact(price_t0: float, price_tx: float) -> float:
    """計算漲跌幅"""
    if price_t0 is None or price_tx is None:
        return None
    return round(((price_tx - price_t0) / price_t0) * 100, 2)

def get_pending_events(limit: int = 10) -> list:
    """獲取需要更新價格的事件"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    cursor.execute('''
        SELECT 
            e.event_id,
            e.date as event_date,
            i.impact_id,
            i.ticker,
            i.asset_class,
            i.price_t0,
            i.price_t1
        FROM asset_impact i
        JOIN macro_events e ON i.event_id = e.event_id
        WHERE i.price_t0 IS NULL
        ORDER BY e.date DESC
        LIMIT ?
    ''', (limit,))
    
    return [dict(row) for row in cursor.fetchall()]

def get_yahoo_code(ticker: str) -> str:
    """從stock_assets拎yahoo_code"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # First check stock_assets
    cursor.execute("SELECT yahoo_code FROM stock_assets WHERE symbol = ?", (ticker,))
    row = cursor.fetchone()
    
    if row:
        conn.close()
        return row[0]
    
    # Fallback to old mapping
    TICKER_MAP = {
        "BTC": "bitcoin", "ETH": "ethereum", "SOL": "solana",
        "GOLD": "GC=F", "OIL": "CL=F",
    }
    
    conn.close()
    return TICKER_MAP.get(ticker, ticker)

def is_crypto(ticker: str) -> bool:
    """判斷係咪Crypto"""
    crypto_list = ["BTC", "ETH", "SOL", "XRP"]
    return ticker in crypto_list

def update_price(impact_id: int, price_data: dict) -> bool:
    """更新價格記錄"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    if price_data:
        cursor.execute('''
            UPDATE asset_impact 
            SET price_t0 = ?, updated_at = CURRENT_TIMESTAMP
            WHERE impact_id = ?
        ''', (price_data.get('close'), impact_id))
    
    conn.commit()
    conn.close()
    return True

def fetch_latest_prices(symbols: list = None) -> dict:
    """批量獲取最新價格"""
    if symbols is None:
        # Get all active assets
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT symbol, yahoo_code FROM stock_assets WHERE is_active = 1")
        symbols = cursor.fetchall()
        conn.close()
    
    results = {}
    for symbol, yahoo_code in symbols:
        print(f"📊 Fetching {symbol} ({yahoo_code})...")
        
        if is_crypto(symbol):
            # Crypto via CoinGecko
            coin_map = {"BTC": "bitcoin", "ETH": "ethereum", "SOL": "solana"}
            price = get_crypto_price(coin_map.get(symbol, symbol), datetime.now().strftime('%d-%m-%Y'))
        else:
            # Stock via yfinance
            price_data = get_stock_price(yahoo_code)
            price = price_data['close'] if price_data else None
        
        if price:
            results[symbol] = price
            print(f"   ${price}")
        else:
            results[symbol] = None
        
        time.sleep(random.uniform(0.3, 0.8))
    
    return results

def main():
    parser = argparse.ArgumentParser(description="Price Fetcher Pipeline")
    parser.add_argument("--project-root", default=None, help="Repository root")
    parser.add_argument("--db-path", default=None, help="Database path")
    parser.add_argument("--update-all", action="store_true", help="Update all pending")
    parser.add_argument("--fetch-symbol", help="Fetch specific symbol")
    parser.add_argument("--fetch-all", action="store_true", help="Fetch all stock assets")
    parser.add_argument("--dry-run", action="store_true", help="Test mode")
    parser.add_argument("--limit", type=int, default=10, help="Limit pending")
    
    args = parser.parse_args()
    
    root = resolve_project_root(args.project_root)
    db_path = args.db_path or str(root / "data" / "macro_events.db")
    global DB_PATH
    DB_PATH = db_path

    if args.update_all:
        pending = get_pending_events(limit=args.limit)
        print(f"📊 Pending events: {len(pending)}")
        
        for p in pending:
            impact_id = p['impact_id']
            ticker = p['ticker']
            event_date = p['event_date']
            
            yahoo_code = get_yahoo_code(ticker)
            
            if is_crypto(ticker):
                coin_map = {"BTC": "bitcoin", "ETH": "ethereum", "SOL": "solana"}
                price = get_crypto_price(coin_map.get(ticker, ticker), event_date)
            else:
                price_data = get_stock_price(yahoo_code, event_date)
                price = price_data['close'] if price_data else None
            
            if price:
                print(f"   {ticker} @ ${price}")
                if not args.dry_run:
                    update_price(impact_id, {'close': price})
    
    elif args.fetch_symbol:
        yahoo_code = get_yahoo_code(args.fetch_symbol)
        if is_crypto(args.fetch_symbol):
            coin_map = {"BTC": "bitcoin", "ETH": "ethereum", "SOL": "solana"}
            price = get_crypto_price(coin_map.get(args.fetch_symbol, args.fetch_symbol), 
                                   datetime.now().strftime('%d-%m-%Y'))
        else:
            price_data = get_stock_price(yahoo_code)
            price = price_data['close'] if price_data else None
        
        print(f"{args.fetch_symbol}: ${price}" if price else "Failed")
    
    elif args.fetch_all:
        print("📊 Fetching all stock assets...")
        results = fetch_latest_prices()
        print(f"\n✅ Fetched {len(results)} prices")
    
    else:
        pending = get_pending_events(limit=args.limit)
        print(f"📊 {len(pending)} pending events")

if __name__ == "__main__":
    main()
