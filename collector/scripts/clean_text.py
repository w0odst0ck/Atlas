#!/usr/bin/env python3
"""
正文精洗工具
- 按来源适配清洗规则
- 先 preview 预览效果，确认后批量跑
- 产出 {source}_正文_clean.md
"""

import re
import sys
from pathlib import Path
from datetime import datetime

BASE_DIR = Path(__file__).resolve().parent.parent.parent
REFS_DIR = BASE_DIR / "refs"

# ── 清洗规则库 ──

RULES = {
    "default": [
        # 面包屑导航（首页 > 产品 > 方案）
        (r'^首页\s*[>＞·▪▶].*$', '', "面包屑"),
        # 纯分隔线
        (r'^[\s_\-=*]{15,}$', '', "分隔线"),
        # 翻页/返回
        (r'^\[?下一页|上一页|返回|首页\]?.*$', '', "翻页"),
        # 客服/在线/咨询浮窗
        (r'.*?(?:客服|在线|咨询|订阅).*?(?:热线|电话|邮箱|微信).*?$', '', "客服"),
        # 底部版权
        (r'^©.*?(?:All\s*Rights|Reserved|版权所有|备案|ICP).*$', '', "版权"),
        # 尾部相关文章
        (r'(?:相关文章|热门推荐|猜你喜欢|延伸阅读|你可能还喜欢|推荐文章).*', '===TAIL_CUT===', "相关推荐"),
        # 尾部标签/分享按钮
        (r'分享到：|分享至|微博|微信|QQ空间|Facebook|Twitter.*$', '', "分享"),
        # 连续空行归并
        (r'\n{4,}', '\n\n\n', "空行"),
    ],
    "pak": [
        (r'^首页\s*[>＞·▪▶].*$', '', "面包屑"),
        (r'^解决方案$', '', "导航标题"),
        (r'^办公照明|教育照明|医疗照明|市政交通|酒店照明|店铺照明|超市照明|购物中心|工业照明|房地产|户外照明$', '', "导航"),
        (r'^关于三雄|公司简介|品牌历程|社会责任|荣誉资质|工程案例|合作伙伴|联系我们', '', "导航"),
        (r'^产品中心|商用照明|家居照明|铂刻|金品系列|常规灯具', '', "导航"),
        (r'^照明学院|学院介绍|设计有光|空间大师|照明知识', '', "导航"),
        (r'^新闻中心|公司新闻|媒体聚焦|投资者关系', '', "导航"),
        (r'^服务中心|设计软件|产品目录|招贤纳士|供应商合作', '', "导航"),
        (r'^天猫旗舰店|京东旗舰店|家居照明微商城|中文版|English', '', "导航"),
        (r'^确认$', '', "确认按钮"),
        (r'^\d+$', '', "页码"),
        (r'^©.*?(?:All\s*Rights|Reserved|版权所有|备案|ICP).*$', '', "版权"),
        # 导航链接块
        (r'^\s*\*\s*\[[^]]+\]\(<[^)]+>\)', '===RM_LINE===', "导航菜单"),
        (r'全国服务热线：.*$', '', "热线"),
        (r'^@2023 All Rights.*', '', "年份版权"),
        (r'\[SEO标签\]\(</[^>]+>\)', '', "SEO标签"),
        (r'\[粤ICP备[^\]]+\]\(<[^>]+>\)', '', "备案号"),
        (r'\n{4,}', '\n\n\n', "空行"),
    ],
    "pak_batch": [
        # 继承基础 PAK 规则 + 批量页特有
        (r'^首页\s*[>＞·▪▶].*$', '', "面包屑"),
        (r'^解决方案$', '', "导航标题"),
        (r'^办公照明|教育照明|医疗照明|市政交通|酒店照明|店铺照明|超市照明|购物中心|工业照明|房地产|户外照明$', '', "导航"),
        (r'^关于三雄|公司简介|品牌历程|社会责任|荣誉资质|工程案例|合作伙伴|联系我们', '', "导航"),
        (r'^产品中心|商用照明|家居照明|铂刻|金品系列|常规灯具', '', "导航"),
        (r'^确认$', '', "确认按钮"),
        (r'^\d+$', '', "页码"),
        # 批量页专用
        (r'^©.*?(?:All\s*Rights|Reserved|版权所有|备案|ICP).*$', '', "版权"),
        (r'\[small\].*?\[/small\]', '', "small标签"),
        (r'<video[^>]*>.*?</video>', '', "video标签", re.DOTALL),
        (r'<source[^>]*>', '', "source标签"),
        (r'^\d+/\d+$', '', "轮播指示"),
        (r'^扫一扫.?手机.*', '', "二维码"),
        (r'^\\[详细\\].*', '', "详情链接"),
        # 导航链接块
        (r'^\s*\*\s*\[[^]]+\]\(<[^)]+>\)', '===RM_LINE===', "导航菜单"),
        (r'全国服务热线：.*$', '', "热线"),
        (r'^@2023 All Rights.*', '', "年份版权"),
        (r'\[SEO标签\]\(</[^>]+>\)', '', "SEO标签"),
        (r'\[粤ICP备[^\]]+\]\(<[^>]+>\)', '', "备案号"),
        (r'\n{4,}', '\n\n\n', "空行"),
    ],
    "pak_detail": [
        # PAK 详情页规则
        (r'^首页\s*[>＞·▪▶].*$', '', "面包屑"),
        (r'^解决方案$', '', "导航标题"),
        (r'^\d+$', '', "页码"),
        (r'^确认$', '', "确认按钮"),
        (r'^\[small\].*?\[/small\]', '', "small标签"),
        (r'^©.*?(?:All\s*Rights|Reserved|版权所有|备案|ICP).*$', '', "版权"),
        # 导航链接块（三雄极光特有：带 [导航名](</...>) 格式的菜单列表）
        (r'^\s*\*\s*\[\s*\]?\(</[^)]+>\)', '', "导航链接"),
        (r'^\s*\*\s*\[[^]]+\]\(<[^)]+>\)', '===RM_LINE===', "导航菜单"),
        (r'全国服务热线：.*$', '', "热线"),
        (r'^\[\!\[.*?\]\(.*?\)\s*\]', '', "导航图链"),
        (r'^@2023 All Rights.*', '', "年份版权"),
        (r'\[SEO标签\]\(</[^>]+>\)', '', "SEO标签"),
        (r'\[粤ICP备[^\]]+\]\(<[^>]+>\)', '', "备案号"),
        (r'\n{4,}', '\n\n\n', "空行"),
    ],
    "eepw": [
        (r'^EEPW首页.*?>.*', '', "面包屑"),
        (r'^<a href="https?://ad\.eepw', '===RM_LINE===', "广告"),
        (r'^发布人：.*?时间：.*', '', "元信息"),
        (r'.*加入技术交流群.*', '', "加群"),
        (r'.*技术大咖面对面.*', '', "加群文案"),
        (r'.*海量资料库查询.*', '', "加群文案"),
        (r'.*扫码加入.*', '', "加群二维码"),
        (r'^\[发布文章\].*', '', "发布入口"),
        (r'^专栏中心$', '', "导航标题"),
        (r'^\[?查看更多\]?.*', '', "查看更多"),
        (r'^相关文章.*|^### .*相关文章.*|^\[?相关文章\]?.*', '===TAIL_CUT===', "相关推荐"),
        (r'^上一篇：|^下一篇：', '', "翻页"),
        (r'^分享到：.*', '', "分享"),
        (r'^\[EEPW首页\].*', '', "面包屑链接"),
        (r'^\[?投稿\]?.*?\[?订阅\]?', '', "投稿订阅"),
        (r'^\d{4}-\d{2}-\d{2}\s+\d{2}:\d{2}.*来源：', '', "时间戳"),
        (r'^\[?加入收藏\]?.*', '', "收藏"),
        (r'^\)\;\s*\/\/\s*\-\-\>', '', "JS残留"),
        (r'^[\.\w]+\.com\.cn.*\bck\.php.*', '', "广告链接残留"),
        (r'^<\/?(?:a|div|span|br|p)[^>]*>', '', "HTML标签"),
        (r'^©.*?(?:All\s*Rights|Reserved|版权所有|备案|ICP).*$', '', "版权"),
        (r'\n{4,}', '\n\n\n', "空行"),
    ],
    "wbus": [
        (r'^首页\s*[>＞·▪▶].*$', '', "面包屑"),
        (r'^‹\s*上一篇文章|下一篇\s*›', '', "翻页"),
        (r'^分享到：.*', '', "分享"),
        (r'^扫描.*?微信.*?二维码.*', '', "二维码"),
        (r'^关注我们|联系我们|产品中心|关于我们', '', "导航"),
        (r'^©.*?(?:All\s*Rights|Reserved|版权所有|备案|ICP).*$', '', "版权"),
        (r'\n{4,}', '\n\n\n', "空行"),
    ],
}

# ── 来源关键词 → 规则映射 ──
SOURCE_KEYWORDS = [
    ("pak_detail", "pak_detail"),
    ("pak_batch", "pak_batch"),
    ("pak_", "pak_batch"),
    ("pak$", "pak_batch"),
]


def detect_rules(source_key: str) -> str:
    """根据来源名返回规则键名"""
    sk = source_key.lower()
    # 精确匹配（仅限有专用规则的）
    if sk in RULES:
        return sk
    # 若包含 'detail' 用 detail 规则
    if "pak_detail" in sk or ("pak" in sk and "detail" in sk):
        return "pak_detail"
    # 若来源是 pak 且非详情页 → 批量规则
    if sk == "pak" or (sk.startswith("pak_") and "detail" not in sk):
        return "pak_batch"
    # 关键词匹配
    for keyword, rule in [("eepw", "eepw"), ("wbus", "wbus")]:
        if keyword in sk:
            return rule
    return "default"


def clean_text(text: str, rules: list) -> tuple[str, list]:
    """应用清洗规则，返回 (清洗后文本, 操作日志)"""
    log = []
    tail_cut = False

    for rule in rules:
        if len(rule) == 4:
            pattern, replacement, rule_name, extra_flag = rule
            flag = re.MULTILINE | re.IGNORECASE | extra_flag
        else:
            pattern, replacement, rule_name = rule
            flag = re.MULTILINE | re.IGNORECASE
        if replacement == "===TAIL_CUT===":
            match = re.search(pattern, text, flag)
            if match:
                text = text[:match.start()].rstrip()
                log.append(f"  [CUT] {rule_name}")
                tail_cut = True
        elif replacement == "===RM_LINE===":
            new_text = re.sub(pattern, '', text, flags=flag)
            if new_text != text:
                log.append(f"  [RM]  {rule_name}")
            text = new_text
        else:
            new_text = re.sub(pattern, replacement, text, flags=flag)
            if new_text != text:
                log.append(f"  [RM]  {rule_name}")
            text = new_text

    text = text.strip()
    return text, log


def preview(source_key: str, text_before: str, text_after: str, log: list):
    """打印清洗前后对比预览"""
    lines_before = len(text_before.split("\n"))
    lines_after = len(text_after.split("\n"))
    chars_before = len(text_before)
    chars_after = len(text_after)

    print(f"\n{'='*60}")
    print(f"来源: {source_key}")
    print(f"{'='*60}")
    print(f"清洗前: {chars_before} 字 / {lines_before} 行")
    print(f"清洗后: {chars_after} 字 / {lines_after} 行")
    print(f"移除:   {chars_before - chars_after} 字 / {lines_before - lines_after} 行")
    print(f"\n操作日志:")
    for l in log:
        print(l)

    print(f"\n--- 清洗后正文 (前 1500 字) ---")
    print(text_after[:1500])
    print("...")
    print(f"\n--- 清洗后正文 (后 500 字) ---")
    print(text_after[-500:])


def clean_file(md_path: Path, source_key: str, dry_run: bool = False) -> bool:
    """清洗单个文件"""
    if not md_path.exists():
        print(f"  [SKIP] 文件不存在: {md_path}")
        return False

    text = md_path.read_text(encoding="utf-8")
    if len(text) < 500:
        print(f"  [SKIP] 内容过短 ({len(text)} 字)，跳过清洗")
        return False

    rule_key = detect_rules(source_key)
    rules = RULES.get(rule_key, RULES["default"])
    text_clean, log = clean_text(text, rules)

    # ── 质量门禁 ──
    quality = []
    if len(text_clean) < 100:
        quality.append(f"[WARN] 清洗后过短 ({len(text_clean)} 字)")
    if len(text_clean) < 200:
        quality.append(f"[WARN] 清洗后很短 ({len(text_clean)} 字)，检查规则")
    shrink_ratio = 1 - len(text_clean) / max(len(text), 1)
    if shrink_ratio > 0.5:
        quality.append(f"[WARN] 压缩率 {shrink_ratio:.0%}>50%，可能过度删除")

    for q in quality:
        print(f"  {q}")
    if quality and len(quality) >= 2:
        print(f"  [SKIP] 质量问题较多，跳过（可用 --preview 检查）")
        return False

    if dry_run:
        preview(source_key, text, text_clean, log)
        return True

    # 写 _clean.md
    clean_path = md_path.with_name(md_path.stem + "_clean.md")
    clean_path.write_text(text_clean, encoding="utf-8")
    removed = len(text) - len(text_clean)
    print(f"  [OK]  {clean_path.name}  ({len(text_clean)} 字, 移除 {removed} 字)")
    return True


def batch_clean(scene: str = "", dry_run: bool = False):
    """批量清洗指定场景或全部（递归查找所有含 _正文.md 的目录）"""
    scenes = [scene] if scene else [d.name for d in REFS_DIR.iterdir() if d.is_dir() and not d.name.startswith("_")]
    total = 0
    ok = 0
    skip = 0

    for s in scenes:
        scene_dir = REFS_DIR / s
        if not scene_dir.is_dir():
            continue
        # 递归查找所有 {name}_正文.md 文件
        for md_path in sorted(scene_dir.rglob("*_正文.md")):
            source_dir = md_path.parent
            source_key = source_dir.name
            if source_key.startswith("_"):
                continue
            total += 1
            if clean_file(md_path, source_key, dry_run):
                ok += 1
            else:
                skip += 1

    return total, ok, skip


def generate_report(output_path: str = None):
    """生成归档快照 refs/_inventory.md"""
    scenes = sorted(d.name for d in REFS_DIR.iterdir() if d.is_dir() and not d.name.startswith("_"))
    rows = []
    total_raw = total_clean = 0

    for scene in scenes:
        scene_dir = REFS_DIR / scene
        for src_dir in sorted(scene_dir.iterdir()):
            if not src_dir.is_dir():
                continue
            raw_path = src_dir / f"{src_dir.name}_正文.md"
            raw_wc = len(raw_path.read_text(encoding="utf-8")) if raw_path.exists() else 0
            html_path = src_dir / f"{src_dir.name}_正文.html"
            html_exist = html_path.exists()
            clean_path = src_dir / f"{src_dir.name}_正文_clean.md"
            clean_wc = len(clean_path.read_text(encoding="utf-8")) if clean_path.exists() else 0
            img_dir = src_dir / "images"
            img_count = len(list(img_dir.glob("*"))) if img_dir.exists() else 0
            pdf_dir = src_dir / "pdfs"
            pdf_count = len(list(pdf_dir.glob("*"))) if pdf_dir.exists() else 0
            report_path = src_dir / "_采集报告.md"
            report_exist = report_path.exists()

            status = "OK" if clean_wc > 0 else ("RAW" if raw_wc > 0 else "EMPTY")
            shrink = f"{(1 - clean_wc/max(raw_wc,1))*100:.0f}%" if clean_wc > 0 else "-"

            total_raw += raw_wc
            total_clean += clean_wc

            rows.append((scene, src_dir.name, raw_wc, clean_wc, shrink, img_count, pdf_count,
                        "Y" if report_exist else "-", status))

    lines = [
        "# 方案馆 · 归档快照",
        "",
        f"> 生成时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        f"> 场景数: {len(scenes)}",
        f"> 来源数: {len(rows)}",
        f"> 总字数 (raw): {total_raw:,}",
        f"> 总字数 (clean): {total_clean:,}",
        f"> 压缩率: {(1 - total_clean/max(total_raw,1))*100:.1f}%",
        "",
        "---",
        "",
        "## 来源清单",
        "",
        "| 场景 | 来源 | raw字 | clean字 | 压缩率 | 图片 | PDF | 报告 | 状态 |",
        "|------|------|-------|--------|--------|------|-----|------|------|",
    ]
    for scene, src, rw, cw, shrink, img, pdf, rpt, st in rows:
        lines.append(f"| {scene} | {src} | {rw:,} | {cw:,} | {shrink} | {img} | {pdf} | {rpt} | {st} |")

    out = "\n".join(lines)
    if output_path:
        Path(output_path).write_text(out, encoding="utf-8")
        print(f"[OK] 快照已写入: {output_path}")
    else:
        print(out)


def pipeline_all():
    """全流程：清洗 → 摘要 → 报告"""
    print("=" * 60)
    print("Pipeline: 全量清洗 → 场景摘要 → 归档快照")
    print("=" * 60)

    print("\n>>> Step 1: 全量清洗")
    t, o, s = batch_clean()
    print(f">>> 清洗: {t} 总, {o} 成功, {s} 跳过")

    print("\n>>> Step 2: 生成清单 (manifest)")
    try:
        import generate_manifest
        m = generate_manifest.scan_sources()
        generate_manifest.write_manifest(m)
        generate_manifest.write_inventory(m)
        print(">>> 清单: 完成")
    except Exception as e:
        import traceback
        print(f">>> 清单生成失败: {e}")
        traceback.print_exc()

    print("\n>>> Step 3: 场景摘要")
    try:
        import generate_summary
        generate_summary.main(m)
        print(">>> 摘要: 完成")
    except Exception as e:
        import traceback
        print(f">>> 摘要生成失败: {e}")
        traceback.print_exc()

    print("\n" + "=" * 60)
    print("Pipeline 完成")
    print("=" * 60)


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="正文精洗工具")
    parser.add_argument("--preview", type=str, help="预览: scene/source_key")
    parser.add_argument("--run", type=str, default="", nargs="?", help="批量清洗场景 (空=全部)")
    parser.add_argument("--dry-run", action="store_true", help="仅预览不写文件")
    parser.add_argument("--all", action="store_true", help="全流程: 清洗→摘要→快照")
    parser.add_argument("--report", action="store_true", help="仅生成归档快照")
    args = parser.parse_args()

    if args.all:
        pipeline_all()
    elif args.report:
        generate_report(str(REFS_DIR / "_inventory.md"))
    elif args.preview:
        parts = args.preview.split("/")
        source_key = parts[1] if len(parts) > 1 else parts[0]
        scene = parts[0] if len(parts) > 1 else parts[0]
        md_path = REFS_DIR / scene / source_key / f"{source_key}_正文.md"
        if len(parts) == 1:
            for d in REFS_DIR.rglob(f"{source_key}_正文.md"):
                md_path = d
                break
        clean_file(md_path, source_key, dry_run=True)
    elif args.dry_run:
        t, o, s = batch_clean(dry_run=True)
        print(f"\n{'='*60}")
        print(f"预览完成: {t} 个文件, {o} 可清洗, {s} 跳过")
    else:
        t, o, s = batch_clean(args.run or "")
        print(f"\n{'='*60}")
        print(f"清洗完成: {t} 个文件, {o} 成功, {s} 跳过/失败")
