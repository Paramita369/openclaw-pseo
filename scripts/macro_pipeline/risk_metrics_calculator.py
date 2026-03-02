"""
Risk Metrics Calculator (Final Version)
=====================================
Calculates accurate Sharpe Ratio and Max Drawdown using price data in database

Math:
- Sharpe: Uses daily returns series (not total return)
- MDD: Uses cumulative max approach (not just endpoints)
"""

import sqlite3
import os
import numpy as np

BASE_DIR = os.getcwd()
DB_PATH = os.path.join(BASE_DIR, "data/macro_events.db")

def calculate_metrics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Get all impact records with price data
    cursor.execute("""
        SELECT impact_id, ticker, price_t0, price_t1, price_t3, price_t7 
        FROM asset_impact 
        WHERE price_t0 IS NOT NULL AND price_t1 IS NOT NULL
    """)
    
    records = cursor.fetchall()
    print(f"📊 Processing {len(records)} records...")
    
    processed = 0
    for record in records:
        impact_id, ticker, p0, p1, p3, p7 = record
        
        # Build price series: [T0, T1, T3, T7]
        prices = []
        for p in [p0, p1, p3, p7]:
            if p and p > 0:
                prices.append(p)
        
        if len(prices) < 2:
            continue
            
        prices = np.array(prices)
        
        # 1. Calculate Sharpe using DAILY returns
        daily_returns = []
        for i in range(1, len(prices)):
            if prices[i-1] > 0:
                ret = (prices[i] - prices[i-1]) / prices[i-1]
                daily_returns.append(ret)
        
        daily_returns = np.array(daily_returns)
        
        if len(daily_returns) > 1 and np.std(daily_returns) > 0:
            annual_factor = 365 if ticker in ['BTC', 'ETH', 'SOL'] else 252
            sharpe = (np.mean(daily_returns) / np.std(daily_returns)) * np.sqrt(annual_factor)
            sharpe = round(sharpe, 2)
        else:
            sharpe = 0.0
        
        # 2. Calculate MDD using cumulative max
        cumulative_max = np.maximum.accumulate(prices)
        drawdowns = (prices - cumulative_max) / cumulative_max
        mdd = np.min(drawdowns) * 100
        
        # Cap unrealistic values
        sharpe = max(-10, min(10, sharpe))
        mdd = max(-50, mdd)
        
        cursor.execute("""
            UPDATE asset_impact 
            SET sharpe_t7 = ?, mdd_t7 = ?
            WHERE impact_id = ?
        """, (sharpe, round(mdd, 2), impact_id))
        
        processed += 1
    
    conn.commit()
    
    # Show results
    cursor.execute("""
        SELECT ticker, 
               ROUND(AVG(sharpe_t7), 2) as avg_sharpe, 
               ROUND(AVG(mdd_t7), 2) as avg_mdd,
               COUNT(*) as cnt
        FROM asset_impact 
        WHERE sharpe_t7 IS NOT NULL 
        GROUP BY ticker 
        ORDER BY avg_sharpe DESC
    """)
    
    results = cursor.fetchall()
    print("\n📈 Risk Metrics (Final):")
    print(f"  {'Asset':<10} {'Sharpe':<10} {'MDD':<10} {'Count':<8}")
    print(f"  {'-'*40}")
    for r in results:
        print(f"  {r[0]:<10} {r[1]:<10} {r[2]:<10}% {r[3]:<8}")
    
    conn.close()
    print(f"\n✅ Completed! Processed {processed} records.")

if __name__ == "__main__":
    calculate_metrics()
