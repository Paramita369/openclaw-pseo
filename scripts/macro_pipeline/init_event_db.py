"""
Macro Events Database Initialization
=====================================
建立三張核心關聯表：記錄新聞、記錄資產價格、記錄事件引發的後續波動。

Usage:
    python3 init_event_db.py
"""

import sqlite3
import os
from datetime import datetime

DB_PATH = os.path.expanduser("~/.openclaw/workspace/data/macro_events.db")

def init_event_database():
    """初始化數據庫與所有Table"""
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
    
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    # 1. 重大事件與新聞表 (包含 LLM 情感評分 + 向量ID)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS macro_events (
            event_id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT NOT NULL,
            domain TEXT NOT NULL,
            headline TEXT NOT NULL,
            summary TEXT,
            sentiment_score REAL,
            related_assets TEXT,
            embedding_id TEXT,
            metadata JSON,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # 2. 資產報價切片表 (儲存事件發生後的價格變化)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS asset_impact (
            impact_id INTEGER PRIMARY KEY AUTOINCREMENT,
            event_id INTEGER NOT NULL,
            ticker TEXT NOT NULL,
            asset_class TEXT NOT NULL,
            exchange TEXT,
            price_t0 REAL,
            price_t1 REAL,
            price_t3 REAL,
            price_t7 REAL,
            impact_t1_pct REAL,
            impact_t3_pct REAL,
            impact_t7_pct REAL,
            compound_return_pct REAL,
            volatility REAL,
            sharpe_t7 REAL,
            mdd_t7 REAL,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(event_id) REFERENCES macro_events(event_id)
        )
    ''')
    
    # 3. 向量索引表 (LanceDB mapping)
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS vector_index (
            vector_id TEXT PRIMARY KEY,
            event_id INTEGER NOT NULL,
            vector_type TEXT,
            model_name TEXT,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY(event_id) REFERENCES macro_events(event_id)
        )
    ''')
    
    # 4. 預測歷史記錄
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS predictions (
            pred_id INTEGER PRIMARY KEY AUTOINCREMENT,
            query_event_id INTEGER,
            query_headline TEXT,
            target_ticker TEXT,
            similar_event_ids TEXT,
            predicted_return_pct REAL,
            confidence_lower REAL,
            confidence_upper REAL,
            win_rate REAL,
            sample_size INTEGER,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    ''')
    
    # 5. 創建Index提升查詢效率
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_events_date ON macro_events(date)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_events_domain ON macro_events(domain)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_impact_event ON asset_impact(event_id)')
    cursor.execute('CREATE INDEX IF NOT EXISTS idx_impact_ticker ON asset_impact(ticker)')
    
    conn.commit()
    conn.close()
    
    print(f"✅ Database initialized: {DB_PATH}")
    print("   Tables: macro_events, asset_impact, vector_index, predictions")
    print("   Indexes created for date, domain, event_id, ticker")

if __name__ == "__main__":
    init_event_database()
