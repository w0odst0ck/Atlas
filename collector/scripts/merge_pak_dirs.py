#!/usr/bin/env python3
"""
PAK 目录重组脚本
- 将 pak_all/ + pak_detail_*/ 按场景归入 refs/{scene}/pak*/ 下
- 安全的只搬运操作（不删除源，只复制）
"""

import shutil
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
REFS_DIR = BASE_DIR / "refs"

# 重复场景清单 — pak_all 中与 {scene}/pak/ 内容相同的子目录，跳过
DUPLICATE_SCENES = {"office", "hospital", "hotel", "education", "outdoor", "commercial"}

# pak_all → 场景映射
PAK_ALL_MAP = {
    "pak":        ("catalog",    "pak_index"),     # PAK 首页 → catalog
    "pak_factory": ("factory",   "pak"),            # 工厂方案
    "pak_estate":  ("estate",    "pak"),            # 房地产方案（新场景）
    "pak_transport": ("transport", "pak"),          # 交通方案（新场景）
}

# 不在 duplicate 中的 pak_all 子目录，但源目录名不同时需要显式映射
# 剩下的自动按 pak_{scene} → {scene}/pak 处理
PAK_ALL_AUTO_PREFIX = "pak_"

# pak_detail → 场景映射
PAK_DETAIL_MAP = {
    "pak_detail_office":       "office",
    "pak_detail_factory":      "factory",
    "pak_detail_hospital":     "hospital",
    "pak_detail_hotel":        "hotel",
    "pak_detail_education":    "education",
    "pak_detail_mall":         "commercial",
    "pak_detail_shop":         "commercial",
    "pak_detail_outdoor":      "outdoor",
    "pak_detail_supermarket":  "commercial",
    "pak_detail_transport":    "transport",
    "pak_detail_estate":       "estate",
}


def merge_pak_all():
    """处理 pak_all/ 目录"""
    pak_all_dir = REFS_DIR / "pak_all"
    if not pak_all_dir.exists():
        print("[SKIP] pak_all/ 不存在")
        return

    moved = 0
    skipped = 0

    for subdir in sorted(pak_all_dir.iterdir()):
        if not subdir.is_dir():
            continue

        source_name = subdir.name

        # 检查是否在重复清单中
        for dup_scene in DUPLICATE_SCENES:
            if source_name == dup_scene or source_name == f"pak_{dup_scene}":
                print(f"  [SKIP] {source_name} → 与 {dup_scene}/pak 重复，跳过")
                skipped += 1
                break
        else:
            # 不在重复列表，检查映射
            if source_name in PAK_ALL_MAP:
                scene, sub_source = PAK_ALL_MAP[source_name]
            elif source_name.startswith(PAK_ALL_AUTO_PREFIX):
                scene = source_name[len(PAK_ALL_AUTO_PREFIX):]
                sub_source = "pak"
            else:
                print(f"  [WARN] {source_name} → 无映射，跳过")
                skipped += 1
                continue

            target_dir = REFS_DIR / scene / sub_source
            target_dir.mkdir(parents=True, exist_ok=True)

            # 复制所有文件
            for f in subdir.iterdir():
                if f.is_file():
                    shutil.copy2(f, target_dir / f.name)
                elif f.is_dir():
                    shutil.copytree(f, target_dir / f.name, dirs_exist_ok=True)

            print(f"  [OK]  {source_name} → {scene}/{sub_source} ({len(list(subdir.iterdir()))} files)")
            moved += 1

    print(f"\n  pak_all 处理完毕：{moved} 已搬运, {skipped} 跳过")


def merge_pak_details():
    """处理 pak_detail_*/ 目录"""
    detail_dirs = [d for d in REFS_DIR.iterdir() if d.is_dir() and d.name.startswith("pak_detail_")]
    if not detail_dirs:
        print("[SKIP] 无 pak_detail_* 目录")
        return

    moved = 0
    for d in sorted(detail_dirs):
        scene = PAK_DETAIL_MAP.get(d.name)
        if not scene:
            print(f"  [WARN] {d.name} → 无场景映射，跳过")
            continue

        for subdir in sorted(d.iterdir()):
            if not subdir.is_dir():
                continue

            # 目标：{scene}/pak_detail/{subdir.name}/
            target_dir = REFS_DIR / scene / "pak_detail" / subdir.name
            target_dir.mkdir(parents=True, exist_ok=True)

            for f in subdir.iterdir():
                if f.is_file():
                    shutil.copy2(f, target_dir / f.name)
                elif f.is_dir():
                    shutil.copytree(f, target_dir / f.name, dirs_exist_ok=True)

            print(f"  [OK]  {d.name}/{subdir.name} → {scene}/pak_detail/{subdir.name}")
            moved += 1

    print(f"\n  pak_detail 处理完毕：{moved} 已搬运")


if __name__ == "__main__":
    print("=" * 60)
    print("PAK 目录重组")
    print("=" * 60)

    print("\n--- 处理 pak_all/ ---")
    merge_pak_all()

    print("\n--- 处理 pak_detail_*/ ---")
    merge_pak_details()

    print("\n" + "=" * 60)
    print("完成！原始目录（pak_all/、pak_detail_*/）保留未删除")
    print("确认无误后手动删除：rm -rf refs/pak_all* refs/pak_detail_*")
    print("=" * 60)
