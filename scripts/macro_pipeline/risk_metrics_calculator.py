"""
Risk Metrics Calculator
====================
Calculates Sharpe Ratio and Max Drawdown from historical price data

Adds to asset_impact table:
- sharpe_t7: Sharpe Ratio (T+7 returns)
- mdd_t7: Maximum Drawdown (T+7 period)
"""

import sqlite3
import os
import numpy as np

# Configuration
BASE_DIR = os.getcwd()
DB_PATH = os.path.join(BASE_DIR, "data/macro_events.db")

def calculate_metrics():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # Check if columns exist, add if not
    cursor.execute("PRAGMA table_info(asset_impact)")
    columns = [col[1] for col in cursor.fetchall()]
    
    if 'sharpe_t7' not in columns:
        cursor.execute("ALTER TABLE asset_impact ADD COLUMN sharpe_t7 REAL")
        print("✅ Added sharpe_t7 column")
    
    if 'mdd_t7' not in columns:
        cursor.execute("ALTER TABLE asset_impact ADD COLUMN mdd_t7 REAL")
        print("✅ Added mdd_t7 column")
    
    # Get all impact records with price data
    cursor.execute("""
        SELECT impact_id, ticker, price_t0, price_t1, price_t3, price_t7 
        FROM asset_impact 
        WHERE price_t0 IS NOT NULL 
        AND price_t1 IS NOT NULL
    """)
    
    records = cursor.fetchall()
    print(f"📊 Processing {len(records)} records...")
    
    for record in records:
        impact_id, ticker, p0, p1, p3, p7 = record
        
        # Calculate daily returns (assuming equal spacing)
        # For T+7, we have 7 days of returns
        returns = []
        prices = [p0]
        if p1: prices.append(p1)
        if p3: prices.append(p3)
        if p7: prices.append(p7)
        
        if len(prices) >= 2:
            # Calculate daily returns
            for i in range(1, len(prices)):
                daily_ret = (prices[i] - prices[i-1]) / prices[i-1]
                returns.append(daily_ret)
        
        if returns:
            returns = np.array(returns)
            
            # Calculate Sharpe Ratio (annualized, assuming 252 trading days)
            if np.std(returns) > 0:
                sharpe = (np.mean(returns) / np.std(returns)) * np.sqrt(252)
            else:
                sharpe = 0
            
            # Calculate Max Drawdown
            cumulative = (1 + returns).cumprod()
            running_max = np.maximum.accumulate(cumulative)
            drawdowns = (cumulative - running_max) / running_max
            mdd = np.min(drawdowns) * 100  # As percentage
            
            # Update database
            cursor.execute("""
                UPDATE asset_impact 
                SET sharpe_t7 = ?, mdd_t7 = ?
                WHERE impact_id = ?
            """, (round(sharpe, 2), round(mdd, 2), impact_id))
    
    conn.commit()
    
    # Show sample results
    cursor.execute("SELECT ticker, sharpe_t7, mdd_t7 FROM asset_impact WHERE sharpe_t7 IS NOT NULL LIMIT 5")
    results = cursor.fetchall()
    print("\n📈 Sample Risk Metrics:")
    for r in results:
        print(f"  {r[0]}: Sharpe={r[1]:.2f}, MDD={r[2]:.2f}%")
    
    conn.close()
    print("✅ Risk metrics calculation complete!")

if __name__ == "__main__":
    calculate_metrics()
