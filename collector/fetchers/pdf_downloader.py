"""PDF 下载器 — requests 流式写入"""

from pathlib import Path
from typing import Optional


def download(url: str, output_dir: Path, filename: str) -> Optional[Path]:
    """下载 PDF 到本地"""
    import requests

    output_dir.mkdir(parents=True, exist_ok=True)
    save_path = output_dir / filename

    try:
        resp = requests.get(url, stream=True, timeout=30)
        resp.raise_for_status()
        with open(save_path, "wb") as f:
            for chunk in resp.iter_content(chunk_size=8192):
                f.write(chunk)
        return save_path
    except Exception as e:
        print(f"  [ERROR] PDF 下载失败: {url} — {e}")
        return None
