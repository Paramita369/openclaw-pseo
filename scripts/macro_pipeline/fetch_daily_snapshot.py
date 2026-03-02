"""
Daily Macro Snapshot Fetcher
===========================
Fetches real-time prices for key macro assets using yfinance
Output: src/data/daily_snapshot.json
"""

import yfinance as yf
import json
import os
from datetime import datetime

# Configuration
BASE_DIR = os.getcwd()
DATA_DIR = os.path.join(BASE_DIR, "src/data")
os.makedirs(DATA_DIR, exist_ok=True)
JSON_PATH = os.path.join(DATA_DIR, "daily_snapshot.json")

# Target assets (yfinance Tickers)
assets = {
    "BTC": "BTC-USD",
    "GOLD": "GC=F",
    "SPY": "SPY",
    "NVDA": "NVDA",
    "TSLA": "TSLA",
    "SOL": "SOL-USD",
    "ETH": "ETH-USD"
}

results = {}

for name, ticker in assets.items():
    try:
        # Fetch last 5 days to ensure we have previous close
        data = yf.Ticker(ticker).history(period="5d")
        
        if len(data) >= 2:
            latest_price = data['Close'].iloc[-1]
            prev_price = data['Close'].iloc[-2]
            pct_change = ((latest_price - prev_price) / prev_price) * 100
            
            results[name] = {
                "price": float(latest_price),
                "change": round(pct_change, 2)
            }
            print(f"✅ {name}: ${latest_price:.2f} ({pct_change:+.2f}%)")
        else:
            print(f"⚠️ {name}: Insufficient data")
            
    except Exception as e:
        print(f"❌ Error fetching {name}: {e}")

# Save as JSON for Astro
output = {
    "timestamp": datetime.utcnow().isoformat() + "Z",
    "markets": results
}

with open(JSON_PATH, "w") as f:
    json.dump(output, f, indent=2)

print(f"✅ Daily snapshot saved to {JSON_PATH}")
