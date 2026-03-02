"""
pSEO Keyword Matrix Generator
============================
生成標準化既長尾詞清單與對應既 URL Slug

用法:
    python3 keyword_generator.py
"""

import itertools
import pandas as pd
import os
import argparse

# 1. 定義 pSEO 變數矩陣
ASSETS = ["btc", "ethereum", "gold", "spy", "tsla", "nvda", "sol"]
INTENTS = ["price impact", "historical performance", "volatility", "correlation"]
MACRO_EVENTS = ["cpi release", "fed rate cut", "nfp data", "inflation rate", "gdp report"]
TIMEFRAMES = ["1-day", "7-day"]
COMPARISONS = ["", "vs sp500", "vs gold"]

OUTPUT_PATH = os.path.expanduser("~/.openclaw/workspace/data/pseo_keywords.csv")

def generate_pseo_matrix(assets=None, intents=None, macro_events=None, timeframes=None, comparisons=None):
    """將維度交叉組合，生成 pSEO 關鍵詞與 URL Slug 矩陣"""
    
    # Use defaults if not provided
    assets = assets or ASSETS
    intents = intents or INTENTS
    macro_events = macro_events or MACRO_EVENTS
    timeframes = timeframes or TIMEFRAMES
    comparisons = comparisons or COMPARISONS
    
    combinations = list(itertools.product(assets, intents, macro_events, timeframes, comparisons))
    
    data = []
    for asset, intent, event, timeframe, comp in combinations:
        # 組合自然語言關鍵詞 (Search Query)
        keyword_parts = [asset, intent, "after", event]
        if timeframe:
            keyword_parts.append(f"({timeframe})")
        if comp:
            keyword_parts.append(comp)
        keyword = " ".join(keyword_parts)
        
        # 組合 URL Slug (必須小寫、無特殊符號、以連字符分隔)
        slug = keyword.replace(" ", "-").replace("(", "").replace(")", "").lower()
        
        # 建立頁面 Title 模板 (Frontmatter 預備)
        title = f"Historical {intent.title()} of {asset.upper()} After {event.title()}"
        if timeframe:
            title += f" ({timeframe})"
        if comp:
            title += f" {comp.title()}"
        
        # 提取事件類型 (用於數據庫匹配)
        event_type = event.lower().replace(" ", "_")
        
        data.append({
            "keyword": keyword,
            "url_slug": slug,
            "h1_title": title,
            "asset": asset,
            "macro_event": event,
            "macro_event_type": event_type,
            "timeframe": timeframe,
            "comparison": comp if comp else "",
            "intent": intent
        })
    
    df = pd.DataFrame(data)
    
    # 匯出 CSV
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    df.to_csv(OUTPUT_PATH, index=False)
    
    return f"✅ 成功生成 {len(df)} 筆 pSEO 頁面組合，已儲存至 {OUTPUT_PATH}"

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="pSEO Keyword Matrix Generator")
    parser.add_argument("--assets", nargs="+", help="Custom assets list")
    parser.add_argument("--intents", nargs="+", help="Custom intents list")
    parser.add_argument("--events", nargs="+", help="Custom macro events list")
    args = parser.parse_args()
    
    result = generate_pseo_matrix(
        assets=args.assets,
        intents=args.intents,
        macro_events=args.events
    )
    print(result)
    
    # Print summary
    df = pd.read_csv(OUTPUT_PATH)
    print(f"\n📊 Summary:")
    print(f"   Total combinations: {len(df)}")
    print(f"   Unique assets: {df['asset'].nunique()}")
    print(f"   Unique events: {df['macro_event'].nunique()}")
    print(f"\n📋 Sample keywords:")
    for _, row in df.head(5).iterrows():
        print(f"   - {row['keyword']}")
