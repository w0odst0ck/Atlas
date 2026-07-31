"""快速采集雷特案例（正文仅文本不下载图片）"""
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

case_urls = [
    ('chaolisten', 'http://www.ltechonline.com/html/Project-Cases/Chaolisten_Mingyuan.html', '朝歌明苑'),
    ('country_garden', 'http://www.ltechonline.com/html/Project-Cases/CountryGarden.html', '碧桂园滨江湾'),
    ('dali_gold', 'http://www.ltechonline.com/html/Project-Cases/DALI-GoldAward.html', 'DALI金奖'),
    ('ganzhou', 'http://www.ltechonline.com/html/Project-Cases/GanzhouQingqi.html', '赣州清启'),
    ('higold', 'http://www.ltechonline.com/html/Project-Cases/HIGOLD.html', 'HIGOLD'),
    ('hilton', 'http://www.ltechonline.com/html/Project-Cases/Hilton_Hotels.html', '珠海希尔顿酒店'),
    ('hongkong_hs', 'http://www.ltechonline.com/html/Project-Cases/HongKong-HS.html', '香港HS'),
    ('joypolis', 'http://www.ltechonline.com/html/Project-Cases/JOYPOLIS-SPORTS.html', '香港JP超动感世界'),
    ('jundi', 'http://www.ltechonline.com/html/Project-Cases/Jun-Di.html', '骏地'),
    ('private_escape', 'http://www.ltechonline.com/html/Project-Cases/private_escape.html', '私人逃逸'),
]

for sid, url, name in case_urls:
    print(f'\n[{sid}] 雷特 - {name}')
    out_dir = REFS_DIR / 'ltech_case' / f'ltech_case_{sid}'
    out_dir.mkdir(parents=True, exist_ok=True)

    try:
        resp = requests.get(url, headers=HEADERS, timeout=10)
    except Exception as e:
        print(f'  请求失败: {e}')
        continue

    html = resp.text

    # 保存原始 HTML
    with open(out_dir / f'ltech_case_{sid}_正文.html', 'w', encoding='utf-8') as f:
        f.write(html)

    soup = BeautifulSoup(html, 'lxml')
    for tag in soup(['script', 'style', 'nav', 'footer', 'header']):
        tag.decompose()

    body = soup.find('article') or soup.find('main') or soup.find('body') or soup

    # 提取图片但不下载
    img_index = 0
    for img in body.find_all('img'):
        src = img.get('src', '') or img.get('data-src', '') or img.get('data-original', '')
        if src and not src.startswith('data:'):
            img_index += 1
            ext = os.path.splitext(src.split('?')[0])[1] or '.jpg'
            fname = f'img_{img_index:02d}{ext}'
            img.replace_with(f'\n[manual:图片 {fname} 来源: {src}]\n')

    # 转 markdown
    h = html2text.HTML2Text()
    h.body_width = 0
    h.ignore_links = False
    h.ignore_images = True
    h.ignore_emphasis = False
    h.protect_links = True
    h.unicode_snob = True
    h.single_line_break = True
    h.skip_internal_links = True
    h.ignore_tables = False
    h.mark_code = True

    text = h.handle(str(body))
    text = re.sub(r'\n{4,}', '\n\n\n', text)
    text = re.sub(r'^[\s_\-=]{15,}$', '', text, flags=re.MULTILINE)
    text = text.strip()

    md = (
        f'# 雷特 - {name}\n\n'
        f'- 来源: {url}\n'
        f'- 采集时间: {datetime.now().strftime("%Y-%m-%d %H:%M")}\n'
        f'- 场景: ltech_case\n\n'
        f'---\n\n{text}'
    )

    with open(out_dir / f'ltech_case_{sid}_正文.md', 'w', encoding='utf-8') as f:
        f.write(md)

    report = (
        f'# 采集报告: 雷特 - {name}\n\n'
        f'- 来源: {url}\n'
        f'- 场景: ltech_case\n'
        f'- 采集时间: {datetime.now().strftime("%Y-%m-%d %H:%M")}\n'
        f'- 状态: ok\n'
        f'- 正文长度: {len(text)} 字符\n'
        f'- 图片: {img_index} 张（标注为 manual 未下载）\n'
    )
    with open(out_dir / '_采集报告.md', 'w', encoding='utf-8') as f:
        f.write(report)

    print(f'  OK: {len(text)} 字, {img_index} 张图(manual)')
