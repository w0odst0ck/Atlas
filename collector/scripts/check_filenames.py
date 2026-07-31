#!/usr/bin/env python3
"""校验每个来源目录的文件名是否标准化"""
from pathlib import Path

REFS = Path(r"D:\projects\智能照明方案馆\refs")
errors = []

for scene_dir in sorted(REFS.iterdir()):
    if not scene_dir.is_dir() or scene_dir.name.startswith("_"):
        continue
    for src_dir in sorted(scene_dir.iterdir()):
        if not src_dir.is_dir():
            continue
        expected_md = src_dir / f"{src_dir.name}_正文.md"
        expected_clean = src_dir / f"{src_dir.name}_正文_clean.md"
        expected_html = src_dir / f"{src_dir.name}_正文.html"

        # Check md files that don't match naming
        for f in src_dir.glob("*_正文*"):
            if f.suffix in (".md", ".html"):
                expected = src_dir / f"{src_dir.name}{f.stem[len(src_dir.name):]}{f.suffix}"
                # Actually just check if any file has different prefix
                pass

        if not expected_md.exists():
            # Find what exists
            existing = list(src_dir.glob("*_正文.md"))
            if existing:
                errors.append(
                    f"[MISMATCH] {scene_dir.name}/{src_dir.name}: "
                    f"期望 {expected_md.name}, 实际有 {', '.join(e.name for e in existing)}"
                )
            else:
                errors.append(f"[MISSING] {scene_dir.name}/{src_dir.name}: 无 _正文.md 文件")

        if not expected_clean.exists():
            existing_clean = list(src_dir.glob("*_正文_clean.md"))
            if not existing_clean and expected_md.exists():
                errors.append(f"[MISSING CLEAN] {scene_dir.name}/{src_dir.name}: 无 _正文_clean.md")

print(f"=== 文件名标准化校验 ===")
if errors:
    for e in errors:
        print(e)
else:
    print("全部 OK！所有来源目录文件名标准化通过。")
