#!/usr/bin/env python3
"""
refs/ 目录扫描 → _manifest.json + _inventory.md
不依赖 sources.csv，直接从目录结构生成。
递归查找所有包含 {name}_正文.md 的真正来源目录。
"""

import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent.parent
REFS_DIR = BASE_DIR / "refs"
MANIFEST_PATH = REFS_DIR / "_manifest.json"
INVENTORY_PATH = REFS_DIR / "_inventory.md"


def scan_sources() -> dict:
    """递归扫描 refs/{scene}/ 下所有包含正文文件的目录"""
    manifest = {}

    for scene_dir in sorted(REFS_DIR.iterdir()):
        if not scene_dir.is_dir() or scene_dir.name.startswith("_"):
            continue
        scene = scene_dir.name
        sources = []

        # 递归查找所有包含 {name}_正文.md 的目录作为来源
        for src_dir in sorted(scene_dir.rglob("*_正文.md")):
            src_dir = src_dir.parent
            src_name = src_dir.relative_to(scene_dir).as_posix()
            if src_name.startswith("_"):
                continue

            body_md = src_dir / f"{src_dir.name}_正文.md"
            body_html = src_dir / f"{src_dir.name}_正文.html"
            clean_md = src_dir / f"{src_dir.name}_正文_clean.md"
            report = src_dir / "_采集报告.md"
            img_dir = src_dir / "images"
            pdf_dir = src_dir / "pdfs"

            raw_len = len(body_md.read_text(encoding="utf-8")) if body_md.exists() else 0
            clean_len = len(clean_md.read_text(encoding="utf-8")) if clean_md.exists() else 0

            source = {
                "name": src_name,
                "has_raw": body_md.exists(),
                "has_html": body_html.exists(),
                "has_clean": clean_md.exists(),
                "has_report": report.exists(),
                "raw_chars": raw_len,
                "clean_chars": clean_len,
                "images": len(list(img_dir.glob("*"))) if img_dir.exists() else 0,
                "pdfs": len(list(pdf_dir.glob("*"))) if pdf_dir.exists() else 0,
            }

            if clean_len > 0:
                source["status"] = "OK"
            elif raw_len > 0:
                source["status"] = "RAW"
            else:
                source["status"] = "EMPTY"

            if clean_len > 0:
                source["shrink"] = f"{int((1 - clean_len / max(raw_len, 1)) * 100)}%"
            else:
                source["shrink"] = "-"

            sources.append(source)

        if sources:
            manifest[scene] = sources

    return manifest


def write_manifest(manifest: dict):
    data = {
        "updated_at": datetime.now().strftime("%Y-%m-%d %H:%M"),
        "scene_count": len(manifest),
        "source_count": sum(len(v) for v in manifest.values()),
        "scenes": manifest,
    }
    MANIFEST_PATH.write_text(
        json.dumps(data, ensure_ascii=False, indent=2), encoding="utf-8"
    )
    print(f"[OK] _manifest.json — {data['scene_count']} 场景, {data['source_count']} 来源")


def write_inventory(manifest: dict):
    total_raw = total_clean = 0
    for scene in manifest:
        for s in manifest[scene]:
            total_raw += s["raw_chars"]
            total_clean += s["clean_chars"]

    stat_lines = [
        f"> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"> 场景数: {len(manifest)}",
        f"> 来源数: {sum(len(v) for v in manifest.values())}",
        f"> 总字 (raw): {total_raw:,}",
        f"> 总字 (clean): {total_clean:,}",
        f"> 压缩率: {(1 - total_clean/max(total_raw,1))*100:.1f}%",
    ]

    lines = [
        "# 方案馆 · 归档快照",
        "",
    ] + stat_lines + [
        "",
        "| 场景 | 来源 | raw字 | clean字 | 压缩率 | 图片 | PDF | 报告 | 状态 |",
        "|------|------|-------|--------|--------|------|-----|------|------|",
    ]
    for scene in sorted(manifest):
        for s in manifest[scene]:
            lines.append(
                f"| {scene} | {s['name']} | {s['raw_chars']:,} | {s['clean_chars']:,} | "
                f"{s['shrink']} | {s['images']} | {s['pdfs']} | "
                f"{'Y' if s['has_report'] else '-'} | {s['status']} |"
            )

    INVENTORY_PATH.write_text("\n".join(lines), encoding="utf-8")
    print(f"[OK] _inventory.md")


if __name__ == "__main__":
    m = scan_sources()
    write_manifest(m)
    write_inventory(m)
    print("完成")
