"""动态页面采集器 — playwright（同步 API + 系统 Chrome）

使用系统已安装的 Chrome/Edge，不下载额外浏览器。
失败时返回 None，由调用方处理 fallback。
"""

from typing import Optional

PLAYWRIGHT_AVAILABLE = False
try:
    from playwright.sync_api import sync_playwright
    PLAYWRIGHT_AVAILABLE = True
except ImportError:
    pass


def fetch(url: str, timeout_ms: int = 30000) -> Optional[str]:
    """使用无头浏览器渲染动态页，返回 HTML 文本"""
    if not PLAYWRIGHT_AVAILABLE:
        print("    [SKIP] playwright 未安装")
        return None

    try:
        with sync_playwright() as p:
            browser = p.chromium.launch(
                headless=True,
                channel="chrome",
                args=[
                    "--no-sandbox",
                    "--disable-blink-features=AutomationControlled",
                ],
            )
            ctx = browser.new_context(
                user_agent=(
                    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                    "AppleWebKit/537.36 Chrome/149.0.0.0 Safari/537.36"
                )
            )
            page = ctx.new_page()
            page.goto(url, wait_until="domcontentloaded", timeout=timeout_ms)
            page.wait_for_timeout(5000)  # 额外等 5s 让 JS 渲染
            html = page.content()
            browser.close()
            return html
    except Exception as e:
        print(f"    [SKIP] playwright 渲染失败: {e}")
        return None
