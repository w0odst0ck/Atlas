"""自动发现雷特案例详情页并采集（不下载图片，仅取正文）"""
import sys, os, re
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from pathlib import Path
from datetime import datetime
from urllib.parse import urljoin

import requests
from bs4 import BeautifulSoup
import html2text

BASE_DIR = Path(__file__).resolve().parent.parent
REFS_DIR = BASE_DIR.parent / "refs"
HEADERS = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}

# Step 1: 发现所有案例详情页
print("=== 发现详情页 ===")
resp = requests.get("http://www.ltechonline.com/html/Project-Cases/", headers=HEADERS, timeout=10)
soup = BeautifulSoup(resp.text, "lxml")

# 排除合集页
exclude = {
    "Collection-case.html", "Collection_of_cases.html", "Collection_smart_home.html",
    "case_collection.html", "Business_Case_Collection.html", "2024_Case_Collection.html",
    "home_furnishing_cases.html", "ali.html", "borui.html", "experience-store.html",
    "games_village.html", "huawei-2020.html", "JW-2020.html", "lishui.html",
    "miaore.html", "olympics.html", "putian-show.html", "residence.html",
    "shangying.html", "SIKI-2020.html", "Street.html", "2022-shangfeng.html",
    "beijing-zsc.html", "Andaz_Bali.html", "Angsana.html", "CHIBA.html",
    "hong_Kong_Science_Park.html", "J-Hotel.html", "Kimpton.html",
    "Yongjingwan.html", "zhengzhou-CBD.html",
}

case_links = []
for a in soup.find_all("a", href=True):
    href = a["href"]
    if "/Project-Cases/" in href and href.endswith(".html"):
        fname = href.split("/")[-1]
        if fname not in exclude:
            full_url = urljoin("http://www.ltechonline.com/", href)
            case_links.append((fname.replace(".html", ""), full_url))

case_links.sort(key=lambda x: x[0])
print(f"发现 {len(case_links)} 个案例详情页")

# Step 2: 生成 config 条目
print("\n=== 生成 config 条目 ===")
config_lines = ["\n# --- ltech_all (雷特全部案例) ---"]
for sid, url in case_links:
    config_lines.append(f'[[scene.ltech_all]]')
    config_lines.append(f'  source = "ltech_{sid}"')
    config_lines.append(f'  url = "{url}"')
    config_lines.append(f'  label = "雷特 - {sid}"')
    config_lines.append(f'  type = "static"')
    config_lines.append(f'  priority = 1')
    config_lines.append('')

config_text = "\n".join(config_lines)

# 追加到 config.toml
config_path = BASE_DIR / "config.toml"
with open(config_path, "a", encoding="utf-8") as f:
    f.write(config_text)
print(f"已追加 {len(case_links)} 条到 config.toml")

# Step 3: 采集所有案例（仅正文不下载图片）
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

ok_count = 0
for sid, url in case_links:
    out_dir = REFS_DIR / "ltech_all" / f"ltech_{sid}"
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
    except Exception as e:
        print(f"  [{sid}] 请求失败: {e}")
        continue

    html = resp.text
    with open(out_dir / f"ltech_{sid}_正文.html", "w", encoding="utf-8") as f:
        f.write(html)

    soup = BeautifulSoup(html, "lxml")
    for tag in soup(["script", "style", "nav", "footer", "header"]):
        tag.decompose()

    body = soup.find("article") or soup.find("main") or soup.find("body") or soup

    # 标记图片
    img_count = 0
    for img in body.find_all("img"):
        src = img.get("src", "") or img.get("data-src", "") or img.get("data-original", "")
        if src and not src.startswith("data:"):
            img_count += 1
            ext = os.path.splitext(src.split("?")[0])[1] or ".jpg"
            fname = f"img_{img_count:02d}{ext}"
            img.replace_with(f"\n[manual:图片 {fname}]\n")
        elif img.get("alt"):
            img.replace_with(f"\n[{img['alt']}]\n")

    text = _h.handle(str(body))
    text = re.sub(r"\n{4,}", "\n\n\n", text)
    text = re.sub(r"^[\s_\-=]{15,}$", "", text, flags=re.MULTILINE)
    text = text.strip()

    md = (
        f"# 雷特 - {sid}\n\n"
        f"- 来源: {url}\n"
        f"- 采集时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        f"- 场景: ltech_all\n\n---\n\n{text}"
    )
    with open(out_dir / f"ltech_{sid}_正文.md", "w", encoding="utf-8") as f:
        f.write(md)

    report = (
        f"# 采集报告: 雷特 - {sid}\n\n"
        f"- 来源: {url}\n"
        f"- 场景: ltech_all\n"
        f"- 采集时间: {datetime.now().strftime('%Y-%m-%d %H:%M')}\n"
        f"- 状态: ok\n"
        f"- 正文长度: {len(text)} 字符\n"
        f"- 图片: {img_count} 张（标注 manual）\n"
    )
    with open(out_dir / "_采集报告.md", "w", encoding="utf-8") as f:
        f.write(report)

    ok_count += 1
    if ok_count % 10 == 0:
        print(f"  进度: {ok_count}/{len(case_links)}")

print(f"\n采集完成: {ok_count}/{len(case_links)} 个案例")
