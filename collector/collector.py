#!/usr/bin/env python3
"""
智能照明方案馆 · 采集引擎 v3
全量采集：正文 + 原始 HTML + 图片 + PDF + 采集报告
"""

import tomllib
import csv
import re
from pathlib import Path
from datetime import datetime
from typing import Optional
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
import html2text

BASE_DIR = Path(__file__).resolve().parent
REFS_DIR = BASE_DIR.parent / "refs"
SOURCES_CSV = REFS_DIR / "sources.csv"
MANUAL_TODO = REFS_DIR / "_manual_todo.md"

HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"
}


# ══════════════════════════════════════════════════════════
#  网络请求
# ══════════════════════════════════════════════════════════

def fetch_page(url: str) -> Optional[requests.Response]:
    try:
        resp = requests.get(url, headers=HEADERS, timeout=20)
        resp.encoding = resp.apparent_encoding
        return resp
    except Exception as e:
        print(f"    [FAIL] 请求失败: {e}")
        return None


def download_file(url: str, save_path: Path, expected_type: str = None) -> bool:
    try:
        resp = requests.get(url, headers=HEADERS, stream=True, timeout=15)
        resp.raise_for_status()
        if expected_type:
            ct = resp.headers.get("Content-Type", "").lower()
            if expected_type not in ct:
                return False
        save_path.parent.mkdir(parents=True, exist_ok=True)
        total = 0
        for chunk in resp.iter_content(65536):
            total += len(chunk)
            if total > 5 * 1024 * 1024:  # 单文件超过 5MB 截断
                print(f"    [SKIP] 文件过大(>{5}MB)，跳过: {save_path.name}")
                return False
            save_path.parent.mkdir(parents=True, exist_ok=True)
            with open(save_path, "ab") as f:
                f.write(chunk)
        return save_path.exists() and save_path.stat().st_size > 500
    except requests.Timeout:
        print(f"    [SKIP] 下载超时: {save_path.name}")
        return False
    except Exception as e:
        print(f"    [FAIL] 下载失败: {e}")
        return False


# ══════════════════════════════════════════════════════════
#  采集核心
# ══════════════════════════════════════════════════════════

class CollectResult:
    """单个来源的采集结果"""
    def __init__(self, source_key: str, url: str, scene: str, label: str):
        self.source_key = source_key
        self.url = url
        self.scene = scene
        self.label = label
        self.status = "pending"
        self.text_length = 0
        self.images_ok: list[str] = []
        self.images_fail: list[str] = []
        self.pdfs_ok: list[str] = []
        self.pdfs_fail: list[str] = []
        self.manual_notes: list[str] = []

    def add_manual(self, category: str, url: str, reason: str):
        note = f"manual:{category}\n  - URL: {url}\n  - 说明: {reason}\n"
        self.manual_notes.append(note)

    @property
    def has_failures(self) -> bool:
        return bool(self.images_fail) or bool(self.pdfs_fail) or bool(self.manual_notes)

    def report_text(self) -> str:
        lines = [
            f"# 采集报告: {self.label}",
            f"",
            f"- 来源: {self.url}",
            f"- 场景: {self.scene}",
            f"- 采集时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}",
            f"- 状态: {self.status}",
            f"- 正文长度: {self.text_length} 字符",
            f"",
            f"## 图片",
            f"- 成功: {len(self.images_ok)} 张",
            f"- 失败: {len(self.images_fail)} 张",
        ]
        for u in self.images_fail:
            lines.append(f"  - {u}")
        lines += [
            f"",
            f"## PDF",
            f"- 成功: {len(self.pdfs_ok)} 个",
            f"- 失败: {len(self.pdfs_fail)} 个",
        ]
        for u in self.pdfs_fail:
            lines.append(f"  - {u}")
        if self.manual_notes:
            lines += ["", "## 手动标注清单"]
            lines += self.manual_notes
        return "\n".join(lines)


def collect_source(
    source_key: str, url: str, scene: str, label: str, page_type: str,
    selector: str = "",
) -> Optional[CollectResult]:
    """全量采集一个来源"""
    result = CollectResult(source_key, url, scene, label)
    scene_dir = REFS_DIR / scene
    out_dir = scene_dir / source_key
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"\n  [{source_key}] {label}")
    print(f"    URL: {url}")

    # ── 动态页先用 playwright 尝试 ──
    if page_type == "dynamic":
        from fetchers.dynamic_fetcher import fetch as dynamic_fetch
        print(f"    [PLAYWRIGHT] 尝试渲染...")
        html = dynamic_fetch(url)
        if html and len(html) > 1000:
            result.status = "ok"
            print(f"    [OK] playwright 渲染成功 ({len(html)} chars)")
        else:
            result.status = "skipped_dynamic"
            result.add_manual("正文缺失", url, "动态渲染页，playwright 无法获取完整内容")
            _save_report(result, out_dir)
            _record_csv(result)
            print(f"    [SKIP] 动态页渲染不完整，标 manual")
            return result

    # ── PDF 走二进制下载 ──
    if page_type == "pdf":
        result.status = "pdf_pending"
        pdf_dir = out_dir / "pdfs"
        pdf_name = Path(url.split("?")[0]).name or f"{source_key}.pdf"
        save_path = pdf_dir / pdf_name
        ok = download_file(url, save_path, expected_type="application/pdf")
        if ok and save_path.stat().st_size > 1000:
            result.pdfs_ok.append(url)
            result.status = "ok"
            print(f"    [OK] PDF 下载完成 ({save_path.stat().st_size} bytes)")
        else:
            result.pdfs_fail.append(url)
            result.status = "pdf_fail"
            result.add_manual("PDF缺失", url, "content-type 不匹配或文件过小")
            print(f"    [SKIP] PDF 下载失败，已标注 manual")
        _save_report(result, out_dir)
        _record_csv(result)
        return result

    # ── 请求页面 ──
    resp = fetch_page(url)
    if resp is None:
        result.status = "fetch_fail"
        result.add_manual("正文缺失", url, "页面请求失败")
        _save_report(result, out_dir)
        _record_csv(result)
        return result

    html = resp.text
    result.status = "ok"

    # ── 1. 保存原始 HTML ──
    html_path = out_dir / f"{source_key}_正文.html"
    with open(html_path, "w", encoding="utf-8") as f:
        f.write(html)

    # ── 2. 先解析，构建图片映射 ──
    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    # 优先使用 config 指定的 CSS selector
    body = None
    if selector:
        body = soup.select_one(selector)
    if not body:
        body = soup.find("article") or soup.find("main") or soup.find("body")
    if not body:
        body = soup

    # ── 图片提取（5 种来源）+ 下载 ──
    img_dir = out_dir / "images"
    seen_urls = set()
    img_map = {}
    img_index = 0

    def extract_img_src(element, attr, base_url):
        """从元素属性提取图片 URL"""
        nonlocal img_index
        src = element.get(attr, "")
        if not src or src.startswith("data:"):
            return
        abs_url = urljoin(base_url, src)
        if abs_url in seen_urls:
            return
        seen_urls.add(abs_url)
        img_index += 1

        ext = Path(abs_url.split("?")[0]).suffix or ".jpg"
        fname = f"img_{img_index:02d}{ext}"
        img_id = f"__IMG__{img_index}__"
        save_path = img_dir / fname

        # 下载：先无 Referer，再试有 Referer
        ok, msg = _download_img(abs_url, save_path)
        if not ok:
            # 加页面 Referer 重试
            site = "/".join(url.split("/")[:3])
            ok, msg = _download_img(abs_url, save_path, referer=site)

        if ok:
            result.images_ok.append(abs_url)
            img_map[img_id] = (fname, abs_url, "ok")
            print(f"    [OK] 图片 {fname}")
        else:
            result.images_fail.append(abs_url)
            img_map[img_id] = (fname, abs_url, "fail")
            result.add_manual("图片缺失", abs_url, msg)

        # 替换标签为占位符（仅 img 标签）
        if element.name == "img":
            element.replace_with(f"\n[{img_id}]\n")

    def _download_img(img_url: str, save_path: Path, referer: str = "") -> tuple[bool, str]:
        """带 Referer 的图片下载"""
        hdrs = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36",
        }
        if referer:
            hdrs["Referer"] = referer
        try:
            resp = requests.get(img_url, headers=hdrs, timeout=15, stream=True)
            ct = resp.headers.get("Content-Type", "")
            if "image" not in ct and resp.status_code != 200:
                return False, f"非图片响应 ({ct})"
            resp.raise_for_status()
            save_path.parent.mkdir(parents=True, exist_ok=True)
            total = 0
            with open(save_path, "wb") as f:
                for chunk in resp.iter_content(65536):
                    total += len(chunk)
                    if total > 5 * 1024 * 1024:
                        return False, "超过 5MB"
                    f.write(chunk)
            if total < 500:
                return False, f"文件过小 ({total} bytes)"
            # 根据 Content-Type 修正后缀
            ext_map = {"image/png": ".png", "image/jpeg": ".jpg",
                       "image/gif": ".gif", "image/webp": ".webp",
                       "image/svg+xml": ".svg"}
            correct_ext = ext_map.get(ct.split(";")[0].strip())
            if correct_ext and save_path.suffix != correct_ext:
                new_path = save_path.with_suffix(correct_ext)
                save_path.rename(new_path)
            return True, "ok"
        except requests.Timeout:
            return False, "超时"
        except Exception as e:
            return False, str(e)[:60]

    # 1. 标准 img src
    for img in body.find_all("img", src=True):
        extract_img_src(img, "src", url)

    # 2. 懒加载 data-src
    for img in body.find_all("img", attrs={"data-src": True}):
        extract_img_src(img, "data-src", url)

    # 3. 懒加载 data-original
    for img in body.find_all("img", attrs={"data-original": True}):
        extract_img_src(img, "data-original", url)

    # 4. CSS background-image
    for tag in body.find_all(style=re.compile(r"background-image")):
        urls = re.findall(r"url\(['\"]?(.*?)['\"]?\)", tag["style"])
        for u in urls:
            if u.startswith("data:"):
                continue
            abs_url = urljoin(url, u)
            if abs_url in seen_urls:
                continue
            seen_urls.add(abs_url)
            img_index += 1
            ext = ".png"
            fname = f"img_{img_index:02d}{ext}"
            save_path = img_dir / fname
            ok, _ = _download_img(abs_url, save_path, referer="/".join(url.split("/")[:3]))
            if ok:
                result.images_ok.append(abs_url)
                print(f"    [OK] 图片 {fname} (css)")
            else:
                result.images_fail.append(abs_url)

    # 5. picture > source srcset
    for source in body.find_all("source", srcset=True):
        first = source["srcset"].split(",")[0].strip().split(" ")[0]
        if first.startswith("data:"):
            continue
        abs_url = urljoin(url, first)
        if abs_url in seen_urls:
            continue
        seen_urls.add(abs_url)
        img_index += 1
        ext = Path(abs_url.split("?")[0]).suffix or ".jpg"
        fname = f"img_{img_index:02d}{ext}"
        save_path = img_dir / fname
        ok, _ = _download_img(abs_url, save_path)
        if ok:
            result.images_ok.append(abs_url)
            print(f"    [OK] 图片 {fname} (srcset)")
        else:
            result.images_fail.append(abs_url)

    # ── 3. html2text 提取结构化 markdown ──
    _h = html2text.HTML2Text()
    _h.body_width = 0
    _h.ignore_links = False
    _h.ignore_images = True         # 图片由 img_map 统一处理
    _h.ignore_emphasis = False
    _h.protect_links = True
    _h.unicode_snob = True
    _h.single_line_break = True
    _h.skip_internal_links = True
    _h.ignore_tables = False
    _h.mark_code = True

    text = _h.handle(str(body))

    # ── 后处理：正则清洗 ──
    text = re.sub(r'\n{4,}', '\n\n\n', text)                  # 连续空行归并
    text = re.sub(r'^[\s_\-=]{15,}$', '', text, flags=re.MULTILINE)  # 纯分隔线
    text = re.sub(r'^首页\s*[>＞·].*$', '', text, flags=re.MULTILINE) # 面包屑导航
    text = re.sub(r'^\[(?:下一页|上一页|返回|首页).*?\]$', '', text, flags=re.MULTILINE)  # 翻页/返回
    text = re.sub(r'\|\s*__(?:客服|在线|咨询|服务).*?$', '', text, flags=re.MULTILINE | re.IGNORECASE)
    text = text.strip()

    # ── 图片占位符替换 ──
    for img_id, (fname, abs_url, status) in img_map.items():
        if status == "ok":
            text = text.replace(img_id, f"![{fname}](images/{fname})")
        else:
            text = text.replace(img_id, f"[image: {fname} — manual:图片缺失]")

    result.text_length = len(text)
    md_content = (
        f"# {label}\n\n"
        f"- 来源: {url}\n"
        f"- 采集时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        f"- 场景: {scene}\n\n"
        f"---\n\n{text}"
    )
    md_path = out_dir / f"{source_key}_正文.md"
    with open(md_path, "w", encoding="utf-8") as f:
        f.write(md_content)
    print(f"    [OK] 正文 ({result.text_length} 字符, {len(img_map)} 张图标记)")

    # ── 4. 提取 PDF 链接并下载 ──
    pdf_dir = out_dir / "pdfs"
    for a in soup.find_all("a", href=True):
        href = a["href"]
        if not href.lower().endswith(".pdf"):
            continue
        abs_pdf = urljoin(url, href)
        pdf_name = Path(abs_pdf.split("?")[0]).name
        save_path = pdf_dir / pdf_name
        ok = download_file(abs_pdf, save_path)
        if ok and save_path.stat().st_size > 1000:
            result.pdfs_ok.append(abs_pdf)
            print(f"    [OK] PDF {pdf_name}")
        else:
            result.pdfs_fail.append(abs_pdf)
            result.add_manual("PDF缺失", abs_pdf, f"下载失败 ({'文件过小' if ok else '请求失败'})")

    # ── 5. 保存采集报告 ──
    _save_report(result, out_dir)
    _record_csv(result)
    return result


def _save_report(result: CollectResult, out_dir: Path):
    report_path = out_dir / "_采集报告.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.write(result.report_text())
    print(f"    [OK] 采集报告")


def _record_csv(result: CollectResult):
    exists = SOURCES_CSV.exists()
    with open(SOURCES_CSV, "a", newline="", encoding="utf-8") as f:
        w = csv.writer(f)
        if not exists:
            w.writerow(["scene", "source", "url", "fetch_time", "status",
                        "text_len", "img_ok", "img_fail", "pdf_ok", "pdf_fail"])
        w.writerow([
            result.scene, result.source_key, result.url,
            datetime.now().strftime("%Y-%m-%d %H:%M"),
            result.status, result.text_length,
            len(result.images_ok), len(result.images_fail),
            len(result.pdfs_ok), len(result.pdfs_fail),
        ])


def append_manual_todo(results: list[CollectResult]):
    """将所有 manual 标注追加到全局待处理清单"""
    notes = []
    for r in results:
        if r.manual_notes:
            notes.append(f"## {r.label} ({r.scene})")
            notes.append(f"- 来源: {r.url}")
            notes.extend(r.manual_notes)
            notes.append("")

    if not notes:
        return

    with open(MANUAL_TODO, "a", encoding="utf-8") as f:
        f.write(f"\n---\n### {datetime.now().strftime('%Y-%m-%d %H:%M')}\n\n")
        f.write("\n".join(notes))
    print(f"\n  manual 标注已追加到 {MANUAL_TODO}")


# ══════════════════════════════════════════════════════════
#  主入口
# ══════════════════════════════════════════════════════════

def load_config() -> dict:
    config_path = BASE_DIR / "config.toml"
    with open(config_path, "rb") as f:
        return tomllib.load(f)


def collect_single_scene(scene_name: str):
    """采集指定场景的全部来源"""
    config = load_config()
    scene_cfg = config.get("scene", {})
    items = scene_cfg.get(scene_name, [])
    if not items:
        print(f"场景 '{scene_name}' 在 config.toml 中未找到")
        return

    results = []
    for it in items:
        r = collect_source(
            source_key=it.get("source", ""),
            url=it.get("url", ""),
            scene=scene_name,
            label=it.get("label", ""),
            page_type=it.get("type", "static"),
            selector=it.get("selector", ""),
        )
        if r:
            results.append(r)
            print(f"    状态: {r.status} 正文:{r.text_length}字 图片:{len(r.images_ok)}/{len(r.images_fail)} PDF:{len(r.pdfs_ok)}/{len(r.pdfs_fail)}")

    append_manual_todo(results)
    print(f"\n  {scene_name} 完成，共 {len(results)} 个来源")


def print_status(config: dict):
    scene_cfg = config.get("scene", {})
    scenes = sorted(scene_cfg.keys())
    scene_collected = {}
    if SOURCES_CSV.exists():
        with open(SOURCES_CSV, "r", encoding="utf-8") as f:
            for row in csv.DictReader(f):
                s = row.get("scene", "")
                if s:
                    scene_collected.setdefault(s, {"ok": 0, "total": 0})
                    scene_collected[s]["total"] += 1
                    if row.get("status") == "ok":
                        scene_collected[s]["ok"] += 1

    print("\n" + "=" * 60)
    print("20 场景采集状态总览")
    print("=" * 60)
    for name in scenes:
        items = scene_cfg[name]
        stats = scene_collected.get(name, {"ok": 0})
        total = len(items)
        pct = f"{stats['ok']}/{total}"
        print(f"  {name:20s}  {pct}")


if __name__ == "__main__":
    import sys

    config = load_config()

    if len(sys.argv) < 2:
        print("用法:")
        print("  python collector.py status             查看进度")
        print("  python collector.py precheck           预检所有 URL")
        print("  python collector.py run <scene>       采集指定场景")
        print("  python collector.py run-all            采集全部场景")
        sys.exit(0)

    cmd = sys.argv[1]

    if cmd == "status":
        print_status(config)

    elif cmd == "precheck":
        """预检查所有 URL 可用性"""
        scene_cfg = config.get("scene", {})
        print("\n" + "=" * 60)
        print("URL 健康预检查")
        print("=" * 60)
        for name in sorted(scene_cfg.keys()):
            items = scene_cfg[name]
            for it in items:
                url = it.get("url", "")
                label = it.get("label", "")
                ptype = it.get("type", "static")
                if ptype == "dynamic":
                    print(f"  [SKIP] {name:15s} {label:30s} 动态页(跳过)")
                    continue
                if ptype == "pdf":
                    resp = fetch_page(url)
                    ct = ""
                    if resp:
                        ct = resp.headers.get("Content-Type", "")
                    status = f"PDF({ct})" if resp else "FAIL"
                    print(f"  [{status:10s}] {name:15s} {label:30s}")
                    continue
                resp = fetch_page(url)
                if resp and len(resp.text) > 200:
                    print(f"  [OK        ] {name:15s} {label:30s} ({len(resp.text)} chars)")
                elif resp:
                    print(f"  [SHORT({len(resp.text)})] {name:15s} {label:30s} 内容过短，可能是动态页")
                else:
                    print(f"  [FAIL      ] {name:15s} {label:30s}")
        print()

    elif cmd == "run":
        if len(sys.argv) < 3:
            print("需要指定场景名，如: python collector.py run factory")
        else:
            collect_single_scene(sys.argv[2])

    elif cmd == "run-all":
        scene_cfg = config.get("scene", {})
        names = sorted(scene_cfg.keys())
        total = len(names)
        for i, name in enumerate(names, 1):
            print(f"\n{'='*60}")
            print(f"[{i:02d}/{total:02d}] {name}")
            print(f"{'='*60}")
            collect_single_scene(name)
        print(f"\n{'='*60}")
        print(f"全部完成：{total} 个场景")
        print(f"{'='*60}")

    else:
        print(f"未知命令: {cmd}")
