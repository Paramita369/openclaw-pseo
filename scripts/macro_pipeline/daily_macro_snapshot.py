"""
Daily Macro Snapshot Generator
=============================
抓取每日Macro數據並生成JSON俾Astro使用

數據:
- DXY (美元指數)
- BTC (比特幣)
- GOLD (黃金)
- 10年期美國國債收益率
- VIX (波動率指數)

用法:
    python3 daily_macro_snapshot.py
"""

import os
import json
import requests
import time
from datetime import datetime

try:
    import yfinance as yf
    YF_AVAILABLE = True
except ImportError:
    YF_AVAILABLE = False
    print("⚠️ yfinance not installed")

OUTPUT_PATH = os.path.expanduser("~/.openclaw/workspace/astro_project/public/daily_snapshot.json")

def get_market_data():
    """獲取每日市場數據"""
    data = {
        "timestamp": datetime.now().isoformat(),
        "markets": {},
        "macro": {}
    }
    
    if not YF_AVAILABLE:
        return data
    
    # Market Data
    tickers = {
        "BTC": "BTC-USD",      # Bitcoin
        "GOLD": "GC=F",        # Gold Futures
        "SPY": "SPY",          # S&P 500
        "QQQ": "QQQ",          # Nasdaq
        "DXY": "DX-Y.NYB",     # US Dollar Index
        "VIX": "^VIX",         # Volatility Index
        "TNX": "^TNX",         # 10-Year Treasury Yield
    }
    
    for name, ticker in tickers.items():
        try:
            stock = yf.Ticker(ticker)
            hist = stock.history(period="2d")
            
            if not hist.empty:
                latest = hist.iloc[-1]
                prev = hist.iloc[-2] if len(hist) > 1 else latest
                
                change = ((latest['Close'] - prev['Close']) / prev['Close']) * 100 if prev['Close'] else 0
                
                data["markets"][name] = {
                    "price": round(latest['Close'], 2),
                    "change": round(change, 2),
                    "volume": int(latest['Volume']) if 'Volume' in latest else 0,
                    "high": round(latest['High'], 2),
                    "low": round(latest['Low'], 2)
                }
                print(f"✅ {name}: ${latest['Close']} ({change:+.2f}%)")
            
            time.sleep(0.3)  # Rate limiting
        except Exception as e:
            print(f"⚠️ {name}: {e}")
    
    # Calculate BTC halving countdown (estimated next halving)
    # Next halving: April 2028 approximately
    # For now, just add a placeholder
    data["events"] = {
        "btc_halving": {
            "estimate": "April 2028",
            "days_remaining": "~730 days"
        }
    }
    
    return data

def save_snapshot(data):
    """儲存為JSON"""
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"\n✅ Snapshot saved: {OUTPUT_PATH}")

def main():
    print("📊 Generating Daily Macro Snapshot...")
    print(f"⏰ {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
    
    data = get_market_data()
    save_snapshot(data)
    
    print("\n📈 Market Summary:")
    for name, info in data["markets"].items():
        change_emoji = "📈" if info["change"] > 0 else "📉"
        print(f"   {name}: ${info['price']} {change_emoji} {info['change']:+.2f}%")

if __name__ == "__main__":
    main()
