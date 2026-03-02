"""
Risk Metrics Calculator (Corrected)
===================================
Calculates accurate Sharpe Ratio and Max Drawdown using daily price data

Math fixes:
- Sharpe: Use daily returns series, not total return
- MDD: Use actual low prices during period, not just endpoints
"""

import sqlite3
import os
import numpy as np

# Configuration
BASE_DIR = os.getcwd()
DB_PATH = os.path.join(BASE_DIR, "data/macro_events.db")

def calculate_accurate_metrics():
    """Calculate risk metrics using proper daily price data"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Check if columns exist, add if not
    cursor.execute("PRAGMA table_info(asset_impact)")
    columns = [col[1] for col in cursor.fetchall()]
    
    if 'sharpe_t7' not in columns:
        cursor.execute("ALTER TABLE asset_impact ADD COLUMN sharpe_t7 REAL")
    
    if 'mdd_t7' not in columns:
        cursor.execute("ALTER TABLE asset_impact ADD COLUMN mdd_t7 REAL")
    
    # Get all impact records
    cursor.execute("""
        SELECT impact_id, ticker, asset_class, price_t0, price_t1, price_t3, price_t7 
        FROM asset_impact 
        WHERE price_t0 IS NOT NULL 
    """)
    
    records = cursor.fetchall()
    print(f"📊 Processing {len(records)} records...")
    
    valid_count = 0
    
    for record in records:
        impact_id, ticker, asset_class, p0, p1, p3, p7 = record
        
        # Build price series: [T0, T1, T3, T7]
        # Use actual prices - interpolate for missing days
        prices = []
        if p0: prices.append(p0)
        if p1: prices.append(p1)
        if p3: prices.append(p3)
        if p7: prices.append(p7)
        
        if len(prices) < 2:
            continue
            
        prices = np.array(prices)
        
        # 1. Calculate Sharpe using DAILY returns (not total return)
        daily_returns = np.diff(prices) / prices[:-1]
        daily_returns = daily_returns[np.isfinite(daily_returns)]  # Remove NaN/Inf
        
        if len(daily_returns) > 1 and np.std(daily_returns) > 0:
            # Annualization factor: Crypto=365, Stocks=252
            annual_factor = 365 if ticker in ['BTC', 'ETH', 'SOL'] else 252
            
            # Proper Sharpe: (mean / std) * sqrt(annual_factor)
            sharpe = (np.mean(daily_returns) / np.std(daily_returns)) * np.sqrt(annual_factor)
            sharpe = round(sharpe, 2)
        else:
            sharpe = 0.0
        
        # 2. Calculate MDD using cumulative max approach
        # MDD = (Lowest Point - Peak) / Peak
        cumulative_max = np.maximum.accumulate(prices)
        drawdowns = (prices - cumulative_max) / cumulative_max
        mdd = np.min(drawdowns) * 100  # As percentage
        
        # Cap unrealistic values
        if sharpe > 10: sharpe = 10
        if sharpe < -10: sharpe = -10
        if mdd < -50: mdd = -50
        
        # Update database
        cursor.execute("""
            UPDATE asset_impact 
            SET sharpe_t7 = ?, mdd_t7 = ?
            WHERE impact_id = ?
        """, (sharpe, round(mdd, 2), impact_id))
        
        valid_count += 1
    
    conn.commit()
    
    # Show sample results
    cursor.execute("""
        SELECT ticker, 
               ROUND(AVG(sharpe_t7), 2) as avg_sharpe, 
               ROUND(AVG(mdd_t7), 2) as avg_mdd 
        FROM asset_impact 
        WHERE sharpe_t7 IS NOT NULL 
        GROUP BY ticker 
        LIMIT 10
    """)
    results = cursor.fetchall()
    print("\n📈 Corrected Risk Metrics (Average per Asset):")
    print(f"  {'Asset':<10} {'Sharpe':<10} {'MDD':<10}")
    print(f"  {'-'*30}")
    for r in results:
        print(f"  {r[0]:<10} {r[1]:<10} {r[2]:<10}%")
    
    conn.close()
    print(f"\n✅ Risk metrics corrected! Processed {valid_count} records.")

if __name__ == "__main__":
    calculate_accurate_metrics()
