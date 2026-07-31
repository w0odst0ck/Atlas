"""采集存储 — 统一写入 refs/ 目录"""

from pathlib import Path
from datetime import datetime
from typing import Optional


BASE_DIR = Path(__file__).resolve().parent.parent / "refs"


def save_text(source_key: str, content: str, tags: list[str] = None) -> Path:
    """保存方案摘要文本"""
    tag = tags[0] if tags else "general"
    output_dir = BASE_DIR / source_key
    output_dir.mkdir(parents=True, exist_ok=True)

    filename = f"{tag}_{datetime.now().strftime('%Y%m%d')}.md"
    filepath = output_dir / filename
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)
    return filepath


def record_source(source_key: str, url: str, status: str, filepath: Optional[Path] = None):
    """记录采集源到 sources.csv"""
    csv_path = BASE_DIR / "sources.csv"
    import csv

    file_exists = csv_path.exists()
    with open(csv_path, "a", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        if not file_exists:
            writer.writerow(["source", "url", "fetch_date", "status", "file_path"])
        writer.writerow([
            source_key,
            url,
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            status,
            str(filepath) if filepath else "",
        ])
