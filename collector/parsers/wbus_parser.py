"""沃思智能方案解析器"""

from typing import Optional
from . import BaseParser


class WbusParser(BaseParser):
    """解析 w-bus.com 的智能照明方案页"""

    def parse(self, html: str) -> Optional[dict]:
        from bs4 import BeautifulSoup

        soup = BeautifulSoup(html, "lxml")
        title = soup.title.string.strip() if soup.title else ""
        body = soup.find("article") or soup.find("main") or soup.find("body")
        text = body.get_text(separator="\n", strip=True) if body else ""

        return {
            "title": title,
            "content": text,
            "tags": ["工厂", "仓库"],
        }
