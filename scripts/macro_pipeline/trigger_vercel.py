"""
Vercel Deploy Trigger
====================
觸發Vercel重新編譯靜態頁面

用法:
    python3 trigger_vercel.py
    
環境變數:
    VERCEL_DEPLOY_HOOK - Vercel Deploy Hook URL
"""

import os
import requests
import json
import argparse

def trigger_vercel_rebuild(webhook_url: str = None):
    """
    呼叫 Vercel Deploy Hook，觸發 Astro 專案重新讀取 MDX 並編譯靜態 HTML。
    """
    # 優先使用參數，否則使用環境變數
    url = webhook_url or os.environ.get("VERCEL_DEPLOY_HOOK")
    
    if not url:
        return {
            "status": "error", 
            "message": "VERCEL_DEPLOY_HOOK environment variable not set. Use --webhook or set env var."
        }
    
    try:
        response = requests.post(url, timeout=30)
        
        if response.status_code in [200, 201]:
            return {
                "status": "success", 
                "message": "Vercel rebuild triggered successfully.",
                "deploy_id": response.json().get("uid", "N/A")
            }
        else:
            return {
                "status": "failed", 
                "http_code": response.status_code, 
                "error": response.text[:200]
            }
    except requests.exceptions.Timeout:
        return {"status": "timeout", "message": "Request timed out"}
    except Exception as e:
        return {"status": "system_error", "message": str(e)}

def main():
    parser = argparse.ArgumentParser(description="Vercel Deploy Trigger")
    parser.add_argument("--webhook", help="Vercel Deploy Hook URL")
    parser.add_argument("--env", action="store_true", help="Show environment variable requirement")
    args = parser.parse_args()
    
    if args.env:
        print("📋 Vercel Deploy Trigger 環境變數設定")
        print("   export VERCEL_DEPLOY_HOOK='https://api.vercel.com/v1/integrations/deploy/prj_xxx/xxx'")
        return
    
    result = trigger_vercel_rebuild(args.webhook)
    print(json.dumps(result, indent=2))

if __name__ == "__main__":
    main()
