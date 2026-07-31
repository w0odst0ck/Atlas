#!/usr/bin/env python3
"""
场景摘要生成器
读取 _manifest.json，为每个场景生成 00_场景摘要.md
"""

import json
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent.parent
REFS_DIR = BASE_DIR / "refs"
MANIFEST_PATH = REFS_DIR / "_manifest.json"


def load_manifest() -> dict:
    """从 _manifest.json 读取清单"""
    if not MANIFEST_PATH.exists():
        print("[WARN] _manifest.json 不存在，请先运行 generate_manifest.py")
        return {}
    return json.loads(MANIFEST_PATH.read_text(encoding="utf-8"))


def generate_summary(scene: str, sources: list) -> str:
    """生成单个场景的摘要 markdown"""
    total_raw = sum(s.get("raw_chars", 0) for s in sources)
    total_clean = sum(s.get("clean_chars", 0) for s in sources)
    total_imgs = sum(s.get("images", 0) for s in sources)

    lines = [
        f"# {scene} · 采集摘要",
        "",
        f"> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"> 来源数量: {len(sources)}",
        f"> 总字 (raw): {total_raw:,} | 总字 (clean): {total_clean:,} | 图片: {total_imgs}",
        "",
        "---",
        "",
        "## 来源清单",
        "",
        "| 来源 | raw字 | clean字 | 压缩率 | 图片 | PDF | 报告 | 状态 |",
        "|------|-------|--------|--------|------|-----|------|------|",
    ]

    for s in sources:
        lines.append(
            f"| {s['name']:20s} | {s['raw_chars']:>6,} | {s['clean_chars']:>6,} | "
            f"{s['shrink']:>6s} | {s['images']:>3} | {s['pdfs']:>3} | "
            f"{'Y' if s['has_report'] else '-':>4s} | {s['status']} |"
        )

    lines += [
        "",
        f"**总计**: {len(sources)} 来源, {total_raw:,} 字 (raw), {total_clean:,} 字 (clean)",
        "",
    ]

    return "\n".join(lines)


def main(manifest: dict = None):
    """如果传入了 manifest 则直接使用，否则从文件读取"""
    if manifest is None:
        data = load_manifest()
        scenes_data = data.get("scenes", {})
    else:
        scenes_data = manifest

    if not scenes_data:
        print("[WARN] 无场景数据，跳过")
        return

    scenes = sorted(scenes_data.keys())
    print(f"共 {len(scenes)} 个场景")
    for scene in scenes:
        sources = scenes_data[scene]
        summary = generate_summary(scene, sources)
        scene_dir = REFS_DIR / scene
        scene_dir.mkdir(parents=True, exist_ok=True)
        out_path = scene_dir / "00_场景摘要.md"
        out_path.write_text(summary, encoding="utf-8")
        ok_count = sum(1 for s in sources if s.get("status") == "OK")
        print(f"  [OK] {scene:20s} ({ok_count}/{len(sources)} OK)")

    print(f"\n完成: {len(scenes)} 个场景摘要")


if __name__ == "__main__":
    main()
