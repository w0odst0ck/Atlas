"""佛山照明全量采集（正文+图片）"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pathlib import Path
from datetime import datetime

import requests
from bs4 import BeautifulSoup
import html2text

BASE_DIR = Path(__file__).resolve().parent.parent
REFS_DIR = BASE_DIR.parent / "refs"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# 发现所有 solution/ 和 application/ 页
base = "https://www.chinafsl.com"
all_urls = []

print("=== 发现方案页 ===")
for i in range(1, 51):
    url = f"{base}/solution/{i}.html"
    try:
        r = requests.get(url, headers=HEADERS, timeout=5)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, "lxml")
            title_tag = soup.find("title")
            title = title_tag.get_text(strip=True) if title_tag else ""
            # 排除404页面（可能返回200但title显示404）
            if "404" not in title and "未找到" not in title:
                all_urls.append(("solution", i, url, title))
                print(f"  solution/{i}.html → {title[:50]}")
    except:
        pass

print(f"\n=== 发现案例页 ===")
for i in range(1, 21):
    url = f"{base}/application/{i}.html"
    try:
        r = requests.get(url, headers=HEADERS, timeout=5)
        if r.status_code == 200:
            soup = BeautifulSoup(r.text, "lxml")
            title_tag = soup.find("title")
            title = title_tag.get_text(strip=True) if title_tag else ""
            if "404" not in title and "未找到" not in title:
                all_urls.append(("application", i, url, title))
                print(f"  application/{i}.html → {title[:50]}")
    except:
        pass

print(f"\n共 {len(all_urls)} 个页面")

# 加到 config.toml
config_path = BASE_DIR / "config.toml"
config_lines = ["\n# --- fsl_all (佛山照明全部方案+案例) ---"]
for ptype, pid, url, title in all_urls:
    sid = f"fsl_{ptype}_{pid}"
    label = f"佛山照明 - {ptype}{pid}"
    if title:
        label += f" - {title[:30]}"
    config_lines.append(f'[[scene.fsl_all]]')
    config_lines.append(f'  source = "{sid}"')
    config_lines.append(f'  url = "{url}"')
    config_lines.append(f'  label = "{label}"')
    config_lines.append(f'  type = "static"')
    config_lines.append(f'  priority = 1')
    config_lines.append('')

with open(config_path, "a", encoding="utf-8") as f:
    f.write("\n".join(config_lines))
print(f"已追加 {len(all_urls)} 条到 config.toml")

# 采集
print("\n=== 开始采集 ===")
_h = html2text.HTML2Text()
_h.body_width = 0
_h.ignore_links = False
_h.ignore_images = True
_h.ignore_emphasis = False
_h.protect_links = True
_h.unicode_snob = True
_h.single_line_break = True
_h.skip_internal_links = True
_h.ignore_tables = False
_h.mark_code = True

out_scene = "fsl_all"
ok = 0
for ptype, pid, url, title in all_urls:
    sid = f"fsl_{ptype}_{pid}"
    out_dir = REFS_DIR / out_scene / sid
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
    except Exception as e:
        print(f"  [{sid}] 请求失败: {e}")
        continue

    html = resp.text
    with open(out_dir / f"{sid}_正文.html", "w", encoding="utf-8") as f:
        f.write(html)

    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    body = soup.find("article") or soup.find("main") or soup.find("body") or soup.find("div", class_="content") or soup

    img_count = 0
    for img in body.find_all("img"):
        src = img.get("src", "") or img.get("data-src", "") or img.get("data-original", "")
        if src and not src.startswith("data:"):
            img_count += 1
            ext = os.path.splitext(src.split("?")[0])[1] or ".jpg"
            fname = f"img_{img_count:02d}{ext}"
            img.replace_with(f"\n[manual:图片 {fname}]\n")

    text = _h.handle(str(body))
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    text = re.sub(r"^[\s_\-=]{15,}$", "", text, flags=re.MULTILINE)
    text = text.strip()

    label = f"佛山照明 - {ptype}{pid}"
    md = (
        f"# {label}\n\n"
        f"- 来源: {url}\n"
        f"- 采集时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        f"- 场景: {out_scene}\n\n---\n\n{text}"
    )
    with open(out_dir / f"{sid}_正文.md", "w", encoding="utf-8") as f:
        f.write(md)

    report = (
        f"# 采集报告: {label}\n\n"
        f"- 来源: {url}\n"
        f"- 场景: {out_scene}\n"
        f"- 采集时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        f"- 状态: ok\n"
        f"- 正文长度: {len(text)} 字符\n"
        f"- 图片: {img_count} 张（标注 manual）\n"
    )
    with open(out_dir / "_采集报告.md", "w", encoding="utf-8") as f:
        f.write(report)

    ok += 1
    if ok % 10 == 0:
        print(f"  进度: {ok}/{len(all_urls)}")

print(f"\n采集完成: {ok}/{len(all_urls)} 个页面")
