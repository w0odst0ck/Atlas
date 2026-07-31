"""解析器基类"""

from abc import ABC, abstractmethod
from typing import Optional


class BaseParser(ABC):
    """所有解析器的基类"""

    @abstractmethod
    def parse(self, html: str) -> Optional[dict]:
        """
        解析 HTML，返回结构化数据：
        {
            "title": str,
            "content": str,
            "tags": list[str],
            "key_points": dict,
        }
        """
        ...
