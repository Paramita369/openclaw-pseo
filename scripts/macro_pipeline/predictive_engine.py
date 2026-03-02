"""
Predictive Engine
=================
當新事件發生時，利用向量檢索找出歷史相似事件，計算期望勝率與平均漲跌幅。

Usage:
    python3 predictive_engine.py --headline "Fed cuts rates" --ticker BTC
    python3 predictive_engine.py --event-id 5 --ticker BTC
"""

import sqlite3
import json
import os
import argparse
from datetime import datetime, timedelta
import math

DB_PATH = os.path.expanduser("~/.openclaw/workspace/data/macro_events.db")

def cosine_similarity(a: list, b: list) -> float:
    """計算兩個向量的cosine相似度"""
    dot_product = sum(x * y for x, y in zip(a, b))
    norm_a = math.sqrt(sum(x * x for x in a))
    norm_b = math.sqrt(sum(x * x for x in b))
    if norm_a == 0 or norm_b == 0:
        return 0
    return dot_product / (norm_a * norm_b)

def simple_text_embedding(text: str) -> list:
    """
    簡易文字向量化 (基於關鍵詞權重)
    實際生產環境應使用sentence-transformers或OpenAI embeddings
    """
    keywords = {
        # Domain weights
        "fed": {"domain": "Macro", "weight": 1.5},
        "rate": {"domain": "Macro", "weight": 1.5},
        "interest": {"domain": "Macro", "weight": 1.5},
        "cpi": {"domain": "Macro", "weight": 1.5},
        "inflation": {"domain": "Macro", "weight": 1.5},
        "etf": {"domain": "Crypto", "weight": 1.5},
        "bitcoin": {"domain": "Crypto", "weight": 2.0},
        "btc": {"domain": "Crypto", "weight": 2.0},
        "ethereum": {"domain": "Crypto", "weight": 2.0},
        "eth": {"domain": "Crypto", "weight": 2.0},
        "war": {"domain": "Geopolitics", "weight": 2.0},
        "iran": {"domain": "Geopolitics", "weight": 2.0},
        "attack": {"domain": "Geopolitics", "weight": 1.5},
        "military": {"domain": "Geopolitics", "weight": 1.5},
        "ai": {"domain": "AI", "weight": 2.0},
        "nvidia": {"domain": "TechStock", "weight": 1.5},
        "openai": {"domain": "AI", "weight": 1.5},
        "chip": {"domain": "TechStock", "weight": 1.5},
        "gold": {"domain": "Commodity", "weight": 2.0},
        "oil": {"domain": "Commodity", "weight": 2.0},
        # Sentiment
        "bullish": {"sentiment": 0.5},
        "up": {"sentiment": 0.3},
        "gain": {"sentiment": 0.3},
        "surge": {"sentiment": 0.5},
        "rally": {"sentiment": 0.4},
        "bearish": {"sentiment": -0.5},
        "down": {"sentiment": -0.3},
        "loss": {"sentiment": -0.3},
        "crash": {"sentiment": -0.5},
        "plunge": {"sentiment": -0.5},
    }
    
    text_lower = text.lower()
    
    domain_scores = {"Macro": 0, "Crypto": 0, "Geopolitics": 0, "AI": 0, "TechStock": 0, "Commodity": 0}
    sentiment_score = 0
    
    for word, info in keywords.items():
        if word in text_lower:
            if "domain" in info:
                domain_scores[info["domain"]] += info.get("weight", 1.0)
            if "sentiment" in info:
                sentiment_score += info["sentiment"]
    
    # Normalize domain scores
    total = sum(domain_scores.values())
    if total > 0:
        domain_vector = [score / total for score in domain_scores.values()]
    else:
        domain_vector = [1/6] * 6
    
    # Cap sentiment
    sentiment_score = max(-1, min(1, sentiment_score))
    
    return domain_vector + [sentiment_score]

def find_similar_events(headline: str = None, event_id: int = None, 
                        domain: str = None, limit: int = 5) -> list:
    """
    找出相似的歷史事件
    實際生產應使用LanceDB向量搜索
    """
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    # Build query
    query = "SELECT * FROM macro_events WHERE 1=1"
    params = []
    
    if event_id:
        query += " AND event_id != ?"
        params.append(event_id)
    
    if domain:
        query += " AND domain = ?"
        params.append(domain)
    
    query += " ORDER BY date DESC LIMIT 50"
    
    cursor.execute(query, params)
    events = cursor.fetchall()
    conn.close()
    
    if not events:
        return []
    
    # Calculate similarity
    if headline:
        query_embedding = simple_text_embedding(headline)
        similarities = []
        
        for event in events:
            event_text = f"{event['headline']} {event['summary'] or ''}"
            event_embedding = simple_text_embedding(event_text)
            sim = cosine_similarity(query_embedding, event_embedding)
            similarities.append((dict(event), sim))
        
        # Sort by similarity and return top N
        similarities.sort(key=lambda x: x[1], reverse=True)
        return [s[0] for s in similarities[:limit]]
    
    # If no headline, return most recent
    return [dict(e) for e in events[:limit]]

def predict_asset_movement(event_ids: list, target_ticker: str, 
                          use_weighted: bool = True,
                          decay_factor: float = 0.9) -> dict:
    """
    基於歷史相似事件，預測目標資產的期望回報
    
    Args:
        event_ids: 歷史事件ID列表
        target_ticker: 目標資產
        use_weighted: 是否使用時效性衰減權重
        decay_factor: 衰減因子 (越接近現在的事件權重越高)
    """
    if not event_ids:
        return {"error": "No historical events provided"}
    
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    
    placeholders = ','.join('?' for _ in event_ids)
    
    # Get price impacts
    cursor.execute(f'''
        SELECT 
            i.event_id,
            i.impact_t1_pct,
            i.impact_t3_pct,
            i.impact_t7_pct,
            e.date,
            e.sentiment_score
        FROM asset_impact i
        JOIN macro_events e ON i.event_id = e.event_id
        WHERE i.ticker = ? AND i.event_id IN ({placeholders})
        AND i.impact_t1_pct IS NOT NULL
    ''', [target_ticker] + event_ids)
    
    results = cursor.fetchall()
    
    # Get event dates for weighting
    cursor.execute(f'''
        SELECT event_id, date FROM macro_events 
        WHERE event_id IN ({placeholders})
    ''', event_ids)
    
    event_dates = {row[0]: row[1] for row in cursor.fetchall()}
    conn.close()
    
    if not results:
        return {"status": "insufficient_data", "ticker": target_ticker}
    
    # Calculate weighted predictions
    t1_impacts = []
    t7_impacts = []
    weights = []
    
    reference_date = datetime.now()
    
    for row in results:
        event_id = row['event_id']
        t1 = row['impact_t1_pct']
        t7 = row['impact_t7_pct']
        sentiment = row['sentiment_score'] or 0
        
        # Calculate time weight
        if use_weighted and event_id in event_dates:
            event_date = datetime.strptime(event_dates[event_id], '%Y-%m-%d')
            days_ago = (reference_date - event_date).days
            weight = decay_factor ** (days_ago / 30)  # Normalize to monthly decay
        else:
            weight = 1.0
        
        if t1 is not None:
            t1_impacts.append((t1, weight, sentiment))
        if t7 is not None:
            t7_impacts.append((t7, weight, sentiment))
        weights.append(weight)
    
    if not t1_impacts and not t7_impacts:
        return {"status": "insufficient_impact_data", "ticker": target_ticker}
    
    # Calculate weighted statistics
    def weighted_stats(impacts):
        if not impacts:
            return {"avg": 0, "win_rate": 0, "std": 0}
        
        total_weight = sum(w for _, w, _ in impacts)
        weighted_return = sum(ret * w for ret, w, _ in impacts) / total_weight
        
        wins = sum(1 for ret, w, _ in impacts if ret > 0)
        win_rate = wins / len(impacts)
        
        # Standard deviation
        mean = weighted_return
        variance = sum(w * (ret - mean) ** 2 for ret, w, _ in impacts) / total_weight
        std = math.sqrt(variance)
        
        return {
            "avg": round(weighted_return, 2),
            "win_rate": round(win_rate * 100, 1),
            "std": round(std, 2),
            "p10": round(weighted_return - 1.65 * std, 2),
            "p90": round(weighted_return + 1.65 * std, 2)
        }
    
    t1_stats = weighted_stats(t1_impacts)
    t7_stats = weighted_stats(t7_impacts)
    
    return {
        "ticker": target_ticker,
        "sample_size": len(results),
        "prediction_t1": t1_stats,
        "prediction_t7": t7_stats,
        "confidence": "high" if len(results) >= 10 else "medium" if len(results) >= 5 else "low"
    }

def save_prediction(query: str, target_ticker: str, similar_ids: list, 
                   prediction: dict) -> bool:
    """保存預測記錄"""
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    
    cursor.execute('''
        INSERT INTO predictions (query_headline, target_ticker, similar_event_ids, 
                                predicted_return_pct, confidence_lower, confidence_upper, 
                                win_rate, sample_size)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        query,
        target_ticker,
        ",".join(map(str, similar_ids)),
        prediction.get("prediction_t7", {}).get("avg"),
        prediction.get("prediction_t7", {}).get("p10"),
        prediction.get("prediction_t7", {}).get("p90"),
        prediction.get("prediction_t7", {}).get("win_rate"),
        prediction.get("sample_size")
    ))
    
    conn.commit()
    conn.close()
    return True

def main():
    parser = argparse.ArgumentParser(description="Predictive Engine")
    parser.add_argument("--headline", help="New event headline")
    parser.add_argument("--event-id", type=int, help="Use existing event as query")
    parser.add_argument("--ticker", required=True, help="Target ticker to predict")
    parser.add_argument("--domain", help="Filter by domain")
    parser.add_argument("--limit", type=int, default=5, help="Number of similar events")
    parser.add_argument("--save", action="store_true", help="Save prediction to database")
    
    args = parser.parse_args()
    
    # Find similar events
    if args.headline:
        similar = find_similar_events(headline=args.headline, domain=args.domain, limit=args.limit)
    elif args.event_id:
        # Get the event details
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        cursor.execute("SELECT headline, domain FROM macro_events WHERE event_id = ?", (args.event_id,))
        row = cursor.fetchone()
        conn.close()
        
        if row:
            similar = find_similar_events(headline=row[0], domain=row[1], limit=args.limit)
        else:
            similar = []
    else:
        print("❌ Must provide --headline or --event-id")
        return
    
    if not similar:
        print(json.dumps({"status": "no_similar_events", "ticker": args.ticker}, indent=2))
        return
    
    similar_ids = [e['event_id'] for e in similar]
    
    print(f"📊 Found {len(similar)} similar events:")
    for e in similar:
        print(f"   - [{e['date']}] {e['domain']}: {e['headline'][:50]}...")
    
    # Get prediction
    prediction = predict_asset_movement(similar_ids, args.ticker)
    
    print(f"\n🎯 Prediction for {args.ticker}:")
    print(json.dumps(prediction, indent=2))
    
    # Save if requested
    if args.save:
        query_text = args.headline or f"Event {args.event_id}"
        save_prediction(query_text, args.ticker, similar_ids, prediction)
        print("💾 Prediction saved to database")

if __name__ == "__main__":
    main()
