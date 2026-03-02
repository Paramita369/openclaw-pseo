"""
Astro Page Builder
=================
將 verified_targets.csv 與 macro_events.db 結合，生成 Astro MDX 頁面

用法:
    python3 astro_page_builder.py
"""

import os
import pandas as pd
import sqlite3
import json
import requests
from datetime import datetime

# ================= 配置區 =================
BASE_DIR = os.getcwd()
DB_PATH = os.path.join(BASE_DIR, "data/macro_events.db")
CSV_PATH = os.path.join(BASE_DIR, "data/verified_targets.csv")
OUTPUT_DIR = os.path.join(BASE_DIR, "src/content/blog/")
FALLBACK_CSV = os.path.join(BASE_DIR, "data/pseo_keywords.csv")
PUBLIC_DIR = os.path.join(BASE_DIR, "public/")
DOMAIN = "https://quantmacro.vercel.app"

# LLM Configuration (MiniMax)
LLM_API_KEY = os.environ.get("MINIMAX_API_KEY", "")
LLM_ENABLED = bool(LLM_API_KEY)

# Referral Links Configuration
REFERRAL_LINKS = {
    "BINANCE": {
        "url": "https://www.binance.com/referral/earn-together/refer2earn-usdc/claim?hl=zh-TC&ref=GRO_28502_NXG80",
        "text": "Trade {asset} on Binance with reduced fees"
    },
    "FUTU": {
        "url": "https://invest.futuhk.com/invite-centre_share?lang=zh-hk&invite_code=MQHETN7N",
        "text": "Trade {asset} stocks with Futu"
    },
    "IB": {
        "url": "https://www.ibkr.com/referral/siohong248",
        "text": "Trade {asset} on Interactive Brokers"
    }
}

# Asset to Platform Mapping
ASSET_PLATFORM_MAP = {
    "BTC": "BINANCE",
    "ETH": "BINANCE",
    "SOL": "BINANCE",
    "GOLD": "IB",
    "OIL": "IB",
    # Default to Futu for stocks
}
# ==========================================

# ================= LLM Content Generator =================
def generate_llm_analysis(asset: str, event: str, data: dict = None) -> str:
    """
    使用 MiniMax LLM 生成獨特既200-300字分析文本
    """
    if not LLM_ENABLED:
        return None
    
    # 構建prompt
    data_info = ""
    if data:
        data_info = f"""
Current quantitative data for {asset} following {event}:
- Sample size: {data.get('sample_size', 0)} events
- Average T+1 impact: {data.get('avg_t1', 0)}%
- Average T+7 impact: {data.get('avg_t7', 0)}%
- Win rate: {data.get('win_rate', 0)}%
"""
    
    prompt = f"""Write a 200-300 word unique quantitative analysis about how {asset} typically reacted to {event} macroeconomic events. 

{data_info}

Requirements:
- Write in English
- Focus on historical patterns and trading implications
- Include specific numbers when available
- Keep it professional and data-driven
- No speculation about future prices
- Do not repeat the same analysis for different assets

Output ONLY the analysis text, no introductions or conclusions needed."""

    try:
        # Try MiniMax API
        url = "https://api.minimax.chat/v1/text/chatcompletion_pro"
        headers = {
            "Authorization": f"Bearer {LLM_API_KEY}",
            "Content-Type": "application/json"
        }
        payload = {
            "model": "abab6.5s-chat",
            "messages": [
                {"role": "user", "content": prompt}
            ],
            "max_tokens": 500
        }
        
        response = requests.post(url, headers=headers, json=payload, timeout=30)
        
        if response.status_code == 200:
            result = response.json()
            return result.get("choices", [{}])[0].get("message", {}).get("content", "")
        else:
            # Print error for debugging
            print(f"   ⚠️ LLM API error: {response.status_code} - {response.text[:100]}")
            return None
            
    except Exception as e:
        print(f"   ⚠️ LLM generation error: {e}")
        return None

# Fallback: Generate basic analysis without LLM
def generate_fallback_analysis(asset: str, event: str, data: dict = None) -> str:
    """當LLM不可用時既fallback分析"""
    if data:
        trend = "positive" if data.get('avg_t7', 0) > 0 else "negative"
        win_rate = data.get('win_rate', 0)
        avg_t7 = data.get('avg_t7', 0)
        sample = data.get('sample_size', 0)
        
        return f"""Based on historical analysis of {sample} {event} events, {asset} has demonstrated a {trend} correlation with average T+7 returns of {avg_t7}%. The win rate stands at {win_rate}%, suggesting {'a potential bullish bias' if win_rate > 50 else 'a cautious approach recommended'} when trading {asset} around {event} releases.

Traders often monitor these macroeconomic indicators for volatility clustering effects, where increased trading volume and price swings are commonly observed in the 24-48 hours following {event} announcements."""
    else:
        return f"""Quantitative analysis for {asset} following {event} events is currently being compiled. Check back for detailed historical performance metrics, win rates, and average price impacts."""

# ===============================================

def fetch_historical_data(ticker: str, event_domain: str):
    """從 SQLite 提取特定資產與事件的歷史勝率與平均漲跌幅"""
    try:
        if not os.path.exists(DB_PATH):
            return None
        
        conn = sqlite3.connect(DB_PATH)
        cursor = conn.cursor()
        
        # 模糊匹配事件名稱提取 T+1, T+7 漲跌幅
        query = '''
            SELECT impact_t1_pct, impact_t7_pct 
            FROM asset_impact a 
            JOIN macro_events m ON a.event_id = m.event_id 
            WHERE a.ticker = ? AND LOWER(m.headline) LIKE ?
        '''
        
        cursor.execute(query, (ticker.upper(), f"%{event_domain.lower()}%"))
        results = cursor.fetchall()
        conn.close()
        
        if not results:
            return None
        
        t1_impacts = [r[0] for r in results if r[0] is not None]
        t7_impacts = [r[1] for r in results if r[1] is not None]
        
        if not t1_impacts:
            return None
        
        win_rate_t1 = sum(1 for x in t1_impacts if x > 0) / len(t1_impacts)
        
        return {
            "sample_size": len(results),
            "avg_t1": round(sum(t1_impacts) / len(t1_impacts), 2),
            "avg_t7": round(sum(t7_impacts) / len(t7_impacts), 2) if t7_impacts else 0,
            "win_rate": round(win_rate_t1 * 100, 2)
        }
    except Exception as e:
        print(f"⚠️ DB Error for {ticker}: {e}")
        return None

def generate_mdx(row):
    """生成單一 Astro MDX 頁面"""
    asset = row['asset'].upper()
    event = row.get('macro_event', row.get('macro_event_type', 'general')).title()
    slug = row['url_slug']
    title = row.get('h1_title', row.get('title', slug))
    
    # 1. 獲取量化數據
    data = fetch_historical_data(asset, event)
    
    # 1.5 獲取圖表數據
    chart_data = []
    try:
        event_date = row.get('date', datetime.now().strftime('%Y-%m-%d'))
        chart_data = fetch_chart_data(asset.lower(), event_date)
    except Exception as e:
        pass
    
    # 2. 生成 LLM 分析文本 (如果啟用)
    llm_analysis = ""
    if LLM_ENABLED:
        print(f"   🤖 Generating LLM analysis for {asset} + {event}...")
        llm_analysis = generate_llm_analysis(asset, event, data)
        if not llm_analysis:
            print(f"   ⚠️ LLM failed, using fallback...")
            llm_analysis = generate_fallback_analysis(asset, event, data)
    else:
        # Use fallback when LLM is not enabled
        llm_analysis = generate_fallback_analysis(asset, event, data)
    
    # 3. 構建動態數據區塊 (Data-Led SEO)
    if data:
        trend = "bullish 📈" if data['avg_t7'] > 0 else "bearish 📉"
        data_section = f"""
## Historical Performance Data

Historically, based on **{data['sample_size']}** recorded events, **{asset}** shows a **{trend}** trend.

| Metric | T+1 (24h) | T+7 (1 Week) |
| :--- | :--- | :--- |
| Win Rate (Positive Returns) | {data['win_rate']}% | N/A |
| Average Impact | {data['avg_t1']}% | {data['avg_t7']}% |
"""
        faq_answer = f"Based on our quant database of {data['sample_size']} events, {asset} has an average T+7 impact of {data['avg_t7']}%, indicating a {trend.replace('📈', 'positive').replace('📉', 'negative')} historical reaction."
    else:
        data_section = f"""
## Historical Performance Data

> ⏳ *Our models are currently gathering historical data for {asset} during {event} events. Check back soon.*

This page will be automatically updated when sufficient data is collected.
"""
        faq_answer = f"Historical data for {asset} following {event} is currently being compiled by our quantitative tracking system."
    
    # 3. 構建 Google FAQ Schema (Rich Snippets 武器)
    faq_schema = {
        "@context": "https://schema.org",
        "@type": "FAQPage",
        "mainEntity": [{
            "@type": "Question",
            "name": f"How does {asset} react to {event}?",
            "acceptedAnswer": {
                "@type": "Answer",
                "text": faq_answer
            }
        }]
    }
    
    # 4. Generate CTA based on asset type (HTML with Tailwind classes)
    # Support multiple platforms for stocks and commodities
    platforms = []
    
    if asset in ["BTC", "ETH", "SOL"]:
        platforms = ["BINANCE"]  # Crypto only
    else:
        # Stocks, gold, oil - show both IBKR and FUTU
        platforms = ["IB", "FUTU"]  # IB on top, FUTU below
    
    # Build CTA HTML
    cta_buttons = ""
    for platform in platforms:
        ref_info = REFERRAL_LINKS[platform]
        cta_text = ref_info["text"].format(asset=asset)
        ref_url = ref_info["url"]
        
        btn_class = "bg-blue-600 hover:bg-blue-700" if platform == "BINANCE" else \
                   "bg-emerald-600 hover:bg-emerald-700" if platform == "IB" else \
                   "bg-purple-600 hover:bg-purple-700"
        
        cta_buttons += f'''
    <div class="mb-3">
        <p class="text-blue-800 text-sm mb-2">{cta_text}</p>
        <a href="{ref_url}" target="_blank" class="inline-block {btn_class} text-white font-bold py-3 px-6 rounded-lg transition-colors shadow-md">
            Open {platform} Account →
        </a>
    </div>'''
    
    cta_section = f"""
<div class="mt-8 p-6 bg-gradient-to-r from-blue-50 to-indigo-50 border-l-4 border-blue-600 rounded-r-lg">
    <h3 class="text-lg font-bold text-blue-900 mb-4">💡 Actionable Insight</h3>
    <p class="text-blue-800 mb-4">Ready to trade **{asset}**?</p>
    {cta_buttons}
    <p class="text-xs text-gray-500 mt-3">*Trading involves risk. This is for educational purposes.</p>
</div>
"""

    # 5. 組合 MDX 內容 (包含 Frontmatter)
    mdx_content = f"""---
title: "{title}"
description: "Quantitative analysis and historical performance of {asset} following {event} releases."
pubDate: "{datetime.now().strftime('%Y-%m-%d')}"
slug: "{slug}"
tags: ["{asset.lower()}", "macro", "backtest", "{row.get('intent', 'analysis').replace(' ', '-').lower()}"]
metrics:
  sharpe_t7: {float(row.get('sharpe_t7', 0)) if row.get('sharpe_t7') else 0}
  mdd_t7: {float(row.get('mdd_t7', 0)) if row.get('mdd_t7') else 0}
  volatility: {float(row.get('volatility', 0)) if row.get('volatility') else 0}
{('chartData: ' + json.dumps(chart_data)) if chart_data else ''}
---

# {title}

Welcome to the OpenClaw quantitative analysis report for **{asset}** reacting to **{event}**. We track historical price actions to provide data-driven trading insights.

{data_section}

## Quantitative Analysis

{llm_analysis if llm_analysis else "*Our quantitative analysis is being updated with the latest data.*"}

## Market Context

*Macroeconomic indicators like **{event}** often trigger high algorithmic trading volume. This page is automatically updated by our backend when new data is released.*

{cta_section}

<script type="application/ld+json">
{json.dumps(faq_schema, indent=2)}
</script>
"""
    
    # 5. 寫入檔案
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    output_file = os.path.join(OUTPUT_DIR, f"{slug}.md")
    
    with open(output_file, "w", encoding="utf-8") as f:
        f.write(mdx_content)
    
    return output_file

def main():
    # 優先使用 verified_targets.csv，如果唔存在就用 pseo_keywords.csv
    csv_to_use = CSV_PATH if os.path.exists(CSV_PATH) else FALLBACK_CSV
    
    if not os.path.exists(csv_to_use):
        print(f"❌ 找不到 {csv_to_use}！")
        print(f"   請先執行 keyword_generator.py 並將驗證後既檔案命名為 verified_targets.csv")
        return
    
    df = pd.read_csv(csv_to_use)
    print(f"🚀 開始生成 {len(df)} 個 Astro MDX 頁面...")
    print(f"📂 Output: {OUTPUT_DIR}")
    
    success = 0
    for idx, (_, row) in enumerate(df.iterrows()):
        try:
            output_file = generate_mdx(row)
            success += 1
            if (idx + 1) % 100 == 0:
                print(f"   Progress: {idx + 1}/{len(df)}")
        except Exception as e:
            print(f"   ⚠️ Error generating {row.get('url_slug', 'unknown')}: {e}")
    
    print(f"\n✅ 完成！成功產出 {success} 頁面至 {OUTPUT_DIR}")
    
    # Generate sitemap
    build_sitemap()

# ================= Sitemap Generator =================
def build_sitemap():
    """掃描生成的 .md 檔案並產出標準 sitemap.xml"""
    public_dir = os.path.expanduser("~/.openclaw/workspace/astro_project/public/")
    os.makedirs(public_dir, exist_ok=True)
    
    xml_lines = [
        '<?xml version="1.0" encoding="UTF-8"?>',
        '<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9">',
        f'  <url>\n    <loc>{DOMAIN}/</loc>\n    <priority>1.0</priority>\n  </url>'
    ]
    
    for filename in os.listdir(OUTPUT_DIR):
        if filename.endswith(".md"):
            slug = filename[:-3]
            xml_lines.append(f'  <url>\n    <loc>{DOMAIN}/blog/{slug}</loc>\n    <priority>0.8</priority>\n  </url>')
    
    xml_lines.append('</urlset>')
    
    sitemap_path = os.path.join(public_dir, "sitemap.xml")
    with open(sitemap_path, "w", encoding="utf-8") as f:
        f.write("\n".join(xml_lines))
    
    print(f"✅ Sitemap 已生成: {sitemap_path}")

if __name__ == "__main__":
    main()

# ================= Chart Data Fetcher =================
def fetch_chart_data(ticker, event_date, days=10):
    """Fetch OHLC data for chart visualization"""
    try:
        import yfinance as yf
        from datetime import timedelta
        
        start = (pd.to_datetime(event_date) - timedelta(days=3)).strftime('%Y-%m-%d')
        end = (pd.to_datetime(event_date) + timedelta(days=7)).strftime('%Y-%m-%d')
        
        # Handle ticker format
        yf_ticker = f"{ticker}-USD" if ticker in ['BTC', 'ETH', 'SOL'] else ticker
        
        data = yf.Ticker(yf_ticker).history(start=start, end=end)
        
        if len(data) > 0:
            chart_data = []
            for idx, row in data.iterrows():
                chart_data.append({
                    "time": idx.strftime('%Y-%m-%d'),
                    "open": round(row['Open'], 2),
                    "high": round(row['High'], 2),
                    "low": round(row['Low'], 2),
                    "close": round(row['Close'], 2)
                })
            return chart_data
    except Exception as e:
        print(f"Chart data error for {ticker}: {e}")
    return []

# ================================================
