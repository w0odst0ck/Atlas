"""静态页面采集器 — requests + beautifulsoup4"""

from typing import Optional


def fetch(url: str) -> Optional[str]:
    """抓取静态页面，返回 HTML 文本"""
    import requests

    try:
        resp = requests.get(url, timeout=15)
        resp.encoding = resp.apparent_encoding
        return resp.text
    except Exception as e:
        print(f"  [ERROR] 抓取失败: {url} — {e}")
        return None
