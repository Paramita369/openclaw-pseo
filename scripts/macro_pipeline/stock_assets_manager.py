"""
Stock Assets Manager
====================
管理股票資產目錄 (美股 + 港股)

Usage:
    python3 stock_assets_manager.py --add "AAPL,Apple Inc,US,Tech,stock"
    python3 stock_assets_manager.py --list
    python3 stock_assets_manager.py --init-defaults
"""

import sqlite3
import json
import os
import argparse

DB_PATH = os.path.expanduser("~/.openclaw/workspace/data/macro_events.db")

# Default stock assets
DEFAULT_ASSETS = [
    # === US Indices ===
    {"symbol": "SPY", "name": "S&P 500 ETF", "market": "US", "sector": "Index", "asset_type": "index", "yahoo_code": "SPY"},
    {"symbol": "QQQ", "name": "Nasdaq 100 ETF", "market": "US", "sector": "Index", "asset_type": "index", "yahoo_code": "QQQ"},
    {"symbol": "DIA", "name": "Dow Jones ETF", "market": "US", "sector": "Index", "asset_type": "index", "yahoo_code": "DIA"},
    {"symbol": "^IXIC", "name": "Nasdaq Composite", "market": "US", "sector": "Index", "asset_type": "index", "yahoo_code": "^IXIC"},
    {"symbol": "^GSPC", "name": "S&P 500", "market": "US", "sector": "Index", "asset_type": "index", "yahoo_code": "^GSPC"},
    
    # === US Sector ETFs ===
    {"symbol": "XLK", "name": "Tech Sector ETF", "market": "US", "sector": "Tech", "asset_type": "sector", "yahoo_code": "XLK"},
    {"symbol": "XLF", "name": "Financial Sector ETF", "market": "US", "sector": "Finance", "asset_type": "sector", "yahoo_code": "XLF"},
    {"symbol": "XLE", "name": "Energy Sector ETF", "market": "US", "sector": "Energy", "asset_type": "sector", "yahoo_code": "XLE"},
    {"symbol": "XLV", "name": "Healthcare Sector ETF", "market": "US", "sector": "Healthcare", "asset_type": "sector", "yahoo_code": "XLV"},
    {"symbol": "XLY", "name": "Consumer Discretionary ETF", "market": "US", "sector": "Consumer", "asset_type": "sector", "yahoo_code": "XLY"},
    {"symbol": "XLC", "name": "Communication ETF", "market": "US", "sector": "Communication", "asset_type": "sector", "yahoo_code": "XLC"},
    {"symbol": "XLP", "name": "Consumer Staples ETF", "market": "US", "sector": "ConsumerStaples", "asset_type": "sector", "yahoo_code": "XLP"},
    {"symbol": "XLB", "name": "Materials Sector ETF", "market": "US", "sector": "Materials", "asset_type": "sector", "yahoo_code": "XLB"},
    {"symbol": "XLRE", "name": "Real Estate ETF", "market": "US", "sector": "RealEstate", "asset_type": "sector", "yahoo_code": "XLRE"},
    {"symbol": "XLU", "name": "Utilities Sector ETF", "market": "US", "sector": "Utilities", "asset_type": "sector", "yahoo_code": "XLU"},
    
    # === US Stocks - Tech ===
    {"symbol": "AAPL", "name": "Apple Inc", "market": "US", "sector": "Tech", "asset_type": "stock", "yahoo_code": "AAPL"},
    {"symbol": "MSFT", "name": "Microsoft", "market": "US", "sector": "Tech", "asset_type": "stock", "yahoo_code": "MSFT"},
    {"symbol": "NVDA", "name": "NVIDIA", "market": "US", "sector": "Tech", "asset_type": "stock", "yahoo_code": "NVDA"},
    {"symbol": "GOOGL", "name": "Alphabet", "market": "US", "sector": "Tech", "asset_type": "stock", "yahoo_code": "GOOGL"},
    {"symbol": "META", "name": "Meta Platforms", "market": "US", "sector": "Tech", "asset_type": "stock", "yahoo_code": "META"},
    {"symbol": "TSLA", "name": "Tesla", "market": "US", "sector": "Tech", "asset_type": "stock", "yahoo_code": "TSLA"},
    {"symbol": "AMD", "name": "AMD", "market": "US", "sector": "Tech", "asset_type": "stock", "yahoo_code": "AMD"},
    
    # === US Stocks - Finance ===
    {"symbol": "JPM", "name": "JPMorgan Chase", "market": "US", "sector": "Finance", "asset_type": "stock", "yahoo_code": "JPM"},
    {"symbol": "BAC", "name": "Bank of America", "market": "US", "sector": "Finance", "asset_type": "stock", "yahoo_code": "BAC"},
    {"symbol": "GS", "name": "Goldman Sachs", "market": "US", "sector": "Finance", "asset_type": "stock", "yahoo_code": "GS"},
    {"symbol": "MS", "name": "Morgan Stanley", "market": "US", "sector": "Finance", "asset_type": "stock", "yahoo_code": "MS"},
    
    # === US Stocks - Healthcare ===
    {"symbol": "JNJ", "name": "Johnson & Johnson", "market": "US", "sector": "Healthcare", "asset_type": "stock", "yahoo_code": "JNJ"},
    {"symbol": "UNH", "name": "UnitedHealth", "market": "US", "sector": "Healthcare", "asset_type": "stock", "yahoo_code": "UNH"},
    {"symbol": "PFE", "name": "Pfizer", "market": "US", "sector": "Healthcare", "asset_type": "stock", "yahoo_code": "PFE"},
    {"symbol": "LLY", "name": "Eli Lilly", "market": "US", "sector": "Healthcare", "asset_type": "stock", "yahoo_code": "LLY"},
    
    # === US Stocks - Energy ===
    {"symbol": "XOM", "name": "Exxon Mobil", "market": "US", "sector": "Energy", "asset_type": "stock", "yahoo_code": "XOM"},
    {"symbol": "CVX", "name": "Chevron", "market": "US", "sector": "Energy", "asset_type": "stock", "yahoo_code": "CVX"},
    
    # === US Stocks - Consumer ===
    {"symbol": "AMZN", "name": "Amazon", "market": "US", "sector": "Consumer", "asset_type": "stock", "yahoo_code": "AMZN"},
    {"symbol": "WMT", "name": "Walmart", "market": "US", "sector": "Consumer", "asset_type": "stock", "yahoo_code": "WMT"},
    
    # === HK Indices ===
    {"symbol": "^HSI", "name": "Hang Seng Index", "market": "HK", "sector": "Index", "asset_type": "index", "yahoo_code": "^HSI"},
    {"symbol": "^HSCE", "name": "HSCEI", "market": "HK", "sector": "Index", "asset_type": "index", "yahoo_code": "^HSCE"},
    {"symbol": "2828", "name": "Hang Seng金融", "market": "HK", "sector": "Finance", "asset_type": "sector", "yahoo_code": "2828.HK"},
    {"symbol": "2829", "name": "Hang Seng科技", "market": "HK", "sector": "Tech", "asset_type": "sector", "yahoo_code": "2829.HK"},
    
    # === HK Stocks - Tech ===
    {"symbol": "0700", "name": "騰訊控股", "market": "HK", "sector": "Tech", "asset_type": "stock", "yahoo_code": "0700.HK"},
    {"symbol": "9988", "name": "阿里巴巴", "market": "HK", "sector": "Tech", "asset_type": "stock", "yahoo_code": "9988.HK"},
    {"symbol": "3690", "name": "美團", "market": "HK", "sector": "Tech", "asset_type": "stock", "yahoo_code": "3690.HK"},
    {"symbol": "9618", "name": "京東集團", "market": "HK", "sector": "Tech", "asset_type": "stock", "yahoo_code": "9618.HK"},
    {"symbol": "1810", "name": "小米集團", "market": "HK", "sector": "Tech", "asset_type": "stock", "yahoo_code": "1810.HK"},
    
    # === HK Stocks - Finance ===
    {"symbol": "0388", "name": "港交所", "market": "HK", "sector": "Finance", "asset_type": "stock", "yahoo_code": "0388.HK"},
    {"symbol": "0005", "name": "滙豐控股", "market": "HK", "sector": "Finance", "asset_type": "stock", "yahoo_code": "0005.HK"},
    {"symbol": "1398", "name": "工商銀行", "market": "HK", "sector": "Finance", "asset_type": "stock", "yahoo_code": "1398.HK"},
    {"symbol": "0939", "name": "建設銀行", "market": "HK", "sector": "Finance", "asset_type": "stock", "yahoo_code": "0939.HK"},
    {"symbol": "3988", "name": "中國銀行", "market": "HK", "sector": "Finance", "asset_type": "stock", "yahoo_code": "3988.HK"},
    
    # === HK Stocks - Energy ===
    {"symbol": "0883", "name": "中國海洋石油", "market": "HK", "sector": "Energy", "asset_type": "stock", "yahoo_code": "0883.HK"},
    {"symbol": "0857", "name": "中國石油", "market": "HK", "sector": "Energy", "asset_type": "stock", "yahoo_code": "0857.HK"},
    
    # === HK Stocks - Healthcare ===
    {"symbol": "1177", "name": "中國生物製藥", "market": "HK", "sector": "Healthcare", "asset_type": "stock", "yahoo_code": "1177.HK"},
    {"symbol": "2269", "name": "藥明生物", "market": "HK", "sector": "Healthcare", "asset_type": "stock", "yahoo_code": "2269.HK"},
    
    # === HK Stocks - Consumer ===
    {"symbol": "1919", "name": "海底撈", "market": "HK", "sector": "Consumer", "asset_type": "stock", "yahoo_code": "1919.HK"},
    {"symbol": "2319", "name": "蒙牛乳業", "market": "HK", "sector": "Consumer", "asset_type": "stock", "yahoo_code": "2319.HK"},
    
    # === Commodities ===
    {"symbol": "GC=F", "name": "黃金期貨", "market": "COMMODITY", "sector": "PreciousMetal", "asset_type": "commodity", "yahoo_code": "GC=F"},
    {"symbol": "CL=F", "name": "原油期貨", "market": "COMMODITY", "sector": "Energy", "asset_type": "commodity", "yahoo_code": "CL=F"},
    {"symbol": "SI=F", "name": "白銀期貨", "market": "COMMODITY", "sector": "PreciousMetal", "asset_type": "commodity", "yahoo_code": "SI=F"},
]

def init_stock_assets_table():
    """創建stock_assets表"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS stock_assets (
            asset_id INTEGER PRIMARY KEY AUTOINCREMENT,
            symbol VARCHAR(20) NOT NULL UNIQUE,
            name VARCHAR(100),
            market VARCHAR(10) NOT NULL,
            sector VARCHAR(50),
            asset_type VARCHAR(20) NOT NULL,
            yahoo_code VARCHAR(30),
            is_active BOOLEAN DEFAULT 1,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # Create indexes
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_stock_market ON stock_assets(market)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_stock_sector ON stock_assets(sector)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_stock_type ON stock_assets(asset_type)')
    
    conn.commit()
    conn.close()
    print("✅ stock_assets table created")

def add_asset(symbol: str, name: str, market: str, sector: str, asset_type: str) -> dict:
    """添加單一資產"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    yahoo_code = f"{symbol}.HK" if market == "HK" and not symbol.startswith("^") else symbol
    
    try:
        cursor.execute('''
            INSERT INTO stock_assets (symbol, name, market, sector, asset_type, yahoo_code)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (symbol, name, market, sector, asset_type, yahoo_code))
        conn.commit()
        result = {"status": "success", "symbol": symbol}
    except sqlite3.IntegrityError:
        result = {"status": "exists", "symbol": symbol}
    finally:
        conn.close()
    
    return result

def init_default_assets():
    """初始化默認資產列表"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    added = 0
    skipped = 0
    
    for asset in DEFAULT_ASSETS:
        try:
            cursor.execute('''
                INSERT OR IGNORE INTO stock_assets (symbol, name, market, sector, asset_type, yahoo_code)
                VALUES (?, ?, ?, ?, ?, ?)
            ''', (asset['symbol'], asset['name'], asset['market'], 
                  asset['sector'], asset['asset_type'], asset['yahoo_code']))
            if cursor.rowcount > 0:
                added += 1
            else:
                skipped += 1
        except Exception as e:
            print(f"❌ Error adding {asset['symbol']}: {e}")
            skipped += 1
    
    conn.commit()
    conn.close()
    return {"added": added, "skipped": skipped}

def list_assets(market: str = None, sector: str = None, asset_type: str = None) -> list:
    """查詢資產列表"""
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    query = "SELECT * FROM stock_assets WHERE 1=1"
    params = []
    
    if market:
        query += " AND market = ?"
        params.append(market)
    if sector:
        query += " AND sector = ?"
        params.append(sector)
    if asset_type:
        query += " AND asset_type = ?"
        params.append(asset_type)
    
    query += " ORDER BY market, sector, symbol"
    
    cursor.execute(query, params)
    results = [dict(row) for row in cursor.fetchall()]
    conn.close()
    return results

def get_asset_count() -> dict:
    """統計資產數量"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute("SELECT market, COUNT(*) as count FROM stock_assets GROUP BY market")
    by_market = {row[0]: row[1] for row in cursor.fetchall()}
    
    cursor.execute("SELECT asset_type, COUNT(*) as count FROM stock_assets GROUP BY asset_type")
    by_type = {row[0]: row[1] for row in cursor.fetchall()}
    
    cursor.execute("SELECT COUNT(*) FROM stock_assets")
    total = cursor.fetchone()[0]
    
    conn.close()
    return {"total": total, "by_market": by_market, "by_type": by_type}

def main():
    parser = argparse.ArgumentParser(description="Stock Assets Manager")
    parser.add_argument("--init", action="store_true", help="Initialize stock_assets table")
    parser.add_argument("--init-defaults", action="store_true", help="Add default assets")
    parser.add_argument("--list", action="store_true", help="List all assets")
    parser.add_argument("--market", help="Filter by market (US/HK/COMMODITY)")
    parser.add_argument("--sector", help="Filter by sector")
    parser.add_argument("--type", help="Filter by asset_type")
    parser.add_argument("--count", action="store_true", help="Show count stats")
    parser.add_argument("--add", help="Add asset: symbol,name,market,sector,asset_type")
    
    args = parser.parse_args()
    
    if args.init:
        init_stock_assets_table()
    
    if args.init_defaults:
        result = init_default_assets()
        print(f"✅ Added: {result['added']}, Skipped: {result['skipped']}")
    
    if args.list or args.market or args.sector or args.type:
        assets = list_assets(market=args.market, sector=args.sector, asset_type=args.type)
        print(f"📊 Found {len(assets)} assets:")
        for a in assets:
            print(f"   {a['market']:10} {a['sector']:15} {a['symbol']:10} {a['name']}")
    
    if args.count:
        stats = get_asset_count()
        print(f"📈 Total: {stats['total']}")
        print(f"   By Market: {stats['by_market']}")
        print(f"   By Type: {stats['by_type']}")
    
    if args.add:
        parts = args.add.split(",")
        if len(parts) >= 5:
            result = add_asset(parts[0], parts[1], parts[2], parts[3], parts[4])
            print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
