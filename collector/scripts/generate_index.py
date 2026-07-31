# -*- coding: utf-8 -*-
"""Generate scene index files + update STATUS.md"""
import json, re
from pathlib import Path
from datetime import datetime

REFS_DIR = Path(__file__).resolve().parent.parent.parent / "refs"

FSL_SCENE_MAP = {
    2: "catalog", 4: "catalog", 5: "catalog",
    7: "factory", 8: "office", 9: "commercial",
    10: "hotel", 11: "estate", 12: "hospital", 13: "transport",
    15: "outdoor", 17: "outdoor", 18: "education",
    19: "catalog", 20: "catalog",
    21: "hotel", 22: "catalog", 23: "catalog",
    24: "stadium", 25: "stadium",
    26: "catalog", 27: "catalog", 28: "catalog", 29: "catalog",
    32: "outdoor", 34: "outdoor",
}

KINGSUB_CASE_MAP = {
    "indoor": "outdoor",
    "landscape": "outdoor",
    "large_space": "factory",
    "interior": "office",
}

LTECH_KEYWORDS = [
    (r"(?i)hotel|hilton|sheraton|w酒店|merprle|radisson|vinpearl|regis|renaissance|diamond|autumn_fruit|saigon|shangri|conrad|mgm", "hotel"),
    (r"(?i)museum|anhui_museum|suzhou_museum|shanghai_museum|sanxingdui|chengdu_nature", "museum"),
    (r"(?i)huawei|office|ptsc|taikooli|cbd|beijing_huawei|nanjing_huawei|shenzhen_bantian", "office"),
    (r"(?i)shop|store|brompton|meatguy|restaurant|roasted|duravit|porsche|benz|mercedes", "commercial"),
    (r"(?i)sport|gym|joypolis|asian_games|college", "stadium"),
    (r"(?i)school|college|university|education", "education"),
    (r"(?i)park|garden|landscape|street|green_brick", "outdoor"),
    (r"(?i)factory|bwm|dmx|warehouse", "factory"),
    (r"(?i)home|villa|countrygarden|cuijingju|residence|碧桂园", "catalog"),
    (r"(?i)cafe|restaurant|bakery|bar|green_brick|hello_sunday", "commercial"),
    (r"(?i)metro|transport|station|train", "transport"),
    (r"(?i)hospital|medical|clinic", "hospital"),
]

def get_title_summary(md_path):
    try:
        text = md_path.read_text(encoding="utf-8")
        title = ""
        for line in text.split("\n"):
            if line.startswith("# ") and "采集" not in line[:20]:
                title = line[2:].strip()
                break
        body_parts = []
        in_header = False
        for line in text.split("\n"):
            if line.strip() == "---":
                in_header = not in_header
                continue
            if in_header:
                continue
            stripped = line.strip()
            if stripped and not stripped.startswith("[") and not stripped.startswith("!") and not stripped.startswith("http"):
                body_parts.append(stripped)
        summary = " ".join(body_parts)[:200]
        return title or md_path.stem, summary
    except:
        return md_path.stem, ""

def scan_source(scene_dir, source_name):
    clean_md = scene_dir / source_name / f"{source_name}_正文_clean.md"
    raw_md = scene_dir / source_name / f"{source_name}_正文.md"
    md_file = clean_md if clean_md.exists() else raw_md
    if not md_file.exists():
        return None
    title, summary = get_title_summary(md_file)
    imgs_dir = scene_dir / source_name / "images"
    img_count = len(list(imgs_dir.iterdir())) if imgs_dir.exists() else 0
    word_count = len(md_file.read_text(encoding="utf-8"))
    has_manual = False
    report = scene_dir / source_name / "_采集报告.md"
    if report.exists():
        if "manual" in report.read_text(encoding="utf-8").lower():
            has_manual = True
    return {
        "title": title, "summary": summary[:200],
        "word_count": word_count, "img_count": img_count,
        "has_manual": has_manual, "source_key": source_name,
    }

def tag_ltech(name):
    matched = set()
    for pat, scene in LTECH_KEYWORDS:
        if re.search(pat, name):
            matched.add(scene)
    return matched or {"commercial"}

def main():
    manifest = json.loads((REFS_DIR / "_manifest.json").read_text(encoding="utf-8"))
    scenes_data = manifest.get("scenes", {})
    
    # 1. collect per-scene materials
    scene_materials = {}
    for scene, sources in scenes_data.items():
        scene_materials.setdefault(scene, [])
        for entry in sources:
            name = entry["name"]
            info = scan_source(REFS_DIR / scene, name)
            if info:
                info["source_label"] = name
                scene_materials[scene].append(info)
    
    # 2. kingsun_case -> scenes
    for entry in scenes_data.get("kingsun_case", []):
        name = entry["name"]
        for prefix, target in KINGSUB_CASE_MAP.items():
            if name.startswith(f"kingsun_case_{prefix}"):
                info = scan_source(REFS_DIR / "kingsun_case", name)
                if info:
                    info["source_label"] = "kingsun"
                    scene_materials.setdefault(target, []).append(info)
                break
    
    # 3. fsl_all -> scenes
    for entry in scenes_data.get("fsl_all", []):
        name = entry["name"]
        m = re.match(r"fsl_solution_(\d+)", name)
        if m:
            sid = int(m.group(1))
            target = FSL_SCENE_MAP.get(sid)
            if target:
                info = scan_source(REFS_DIR / "fsl_all", name)
                if info:
                    info["source_label"] = "fsl"
                    scene_materials.setdefault(target, []).append(info)
    
    # 4. ltech_all -> scenes
    for entry in scenes_data.get("ltech_all", []):
        name = entry["name"]
        tags = tag_ltech(name)
        for tag in tags:
            info = scan_source(REFS_DIR / "ltech_all", name)
            if info:
                info["source_label"] = "ltech"
                scene_materials.setdefault(tag, []).append(info)
    
    # 5. Write index files
    scene_stats = {}
    for scene in sorted(scene_materials.keys()):
        items = scene_materials[scene]
        seen = set()
        unique = []
        for item in items:
            key = item["source_key"]
            if key not in seen:
                seen.add(key)
                unique.append(item)
        
        lines = [
            f"# {scene} \xb7 \xe7\xb4\xa0\xe6\x9d\x90\xe7\xb4\xa2\xe5\xbc\x95",
            "",
            "## \xe6\x9c\xac\xe5\x9c\xba\xe6\x99\xaf\xe7\xb4\xa0\xe6\x9d\x90",
            "",
            "| # | \xe6\x9d\xa5\xe6\xba\x90 | \xe7\xb4\xa0\xe6\x9d\x90 | \xe5\xad\x97\xe6\x95\xb0 | \xe5\x9b\xbe\xe7\x89\x87 | \xe6\x91\x98\xe8\xa6\x81 |",
            "|---|------|------|------|------|------|",
        ]
        img_total = 0
        manual_count = 0
        for i, item in enumerate(unique, 1):
            wc = f"{item['word_count']//1000}K" if item['word_count'] > 1000 else f"{item['word_count']}"
            img_str = f"{item['img_count']}\xe5\xbc\xa0" + ("(\xe6\x9c\xaa\xe4\xb8\x8b\xe8\xbd\xbd)" if item.get("has_manual") else "")
            lines.append(f"| {i} | {item.get('source_label','?')[:15]} | {item['title'][:30]} | {wc} | {img_str} | {item['summary'][:50]} |")
            img_total += item['img_count']
            if item.get("has_manual"):
                manual_count += 1
        lines.extend(["", "---", f"*Generated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*"])
        
        (REFS_DIR / scene / "_素材索引.md").write_text("\n".join(lines), encoding="utf-8")
        scene_stats[scene] = (len(unique), img_total, manual_count)
        print(f"  {scene}: {len(unique)} items, {img_total} images")
    
    # 6. Update STATUS.md
    print("\n=== STATUS.md ===")
    status = [
        "# Lighting Solution Library - Status Dashboard",
        "",
        f"> Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"> {len(scene_stats)} scenes, ~{sum(s[0] for s in scene_stats.values())} materials",
        "",
        "---",
        "",
        "## Scene Progress",
        "",
        "| Scene | Materials | Images | Status |",
        "|-------|-----------|--------|--------|",
    ]
    priority = ["office","factory","warehouse","parking","commercial","education",
                "hospital","hotel","outdoor","emergency","museum","stadium","metro",
                "transport","estate","catalog","reference"]
    
    all_scenes = priority + [s for s in sorted(scene_stats.keys()) if s not in priority and s not in ("kingsun_case","ltech_all","fsl_all")]
    for scene in all_scenes:
        if scene in scene_stats:
            cnt, img, manual = scene_stats[scene]
            s = "ok" if cnt >= 3 else ("warn" if cnt >= 1 else "missing")
            status.append(f"| {scene} | {cnt} | {img} | {s} |")
    
    (REFS_DIR.parent / "STATUS.md").write_text("\n".join(status), encoding="utf-8")
    print("  Done")
    print(f"\nTotal: {sum(s[0] for s in scene_stats.values())} materials, {sum(s[1] for s in scene_stats.values())} images")

if __name__ == "__main__":
    main()
