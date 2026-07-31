# manual 待办清单

> 精简于 2026-07-24
> 采集层已知问题，正文不受影响。

---

## 已解决

### 2026-07-24 — PAK PDF 已补全

从 `D:\Downloads\pak` 手工入库 11 份 PDF：

| 场景 | PDF |
|------|-----|
| factory | pak工业照明.pdf |
| outdoor | pak户外照明.pdf |
| hospital | pak医疗系统.pdf |
| office | pak商业办公.pdf |
| commercial | pak商用基础 + 购物中心 + 超市 |
| estate | pak地产.pdf |
| education | pak学校健康.pdf |
| hotel | pak酒店.pdf |
| transport | pak轨道交通.pdf |

---

## 未解决（正文不缺失，影响极小）

### EEPW 论文配图 — 盗链/广告位

EEPW 文章中的图片链接多为内嵌广告位（`ad.eepw.com.cn`）或头条云 OSS（`p3-sign.toutiaoimg.com`），返回 0～43 bytes。

**涉及场景：** factory/eepw, office/eepw, emergency/eepw, metro/eepw, parking/eepw

**影响：** 正文完整，仅配图缺失

### 人人文库 — 懒加载

`css.renrendoc.com/static/common/images/lazy-load.png` 占位符被下载代替真实图片。

**涉及场景：** office/renrendoc

**影响：** 正文完整，仅配图缺失

### 页面图标类 — 极小 SVG/PNG

`www.tgmtek.com/images/icon/*.png` (330B)、`chinafsl.com/static/images/svg/*.svg` (271B) 等小图标。

**影响：** 装饰性图标，无实际意义

---
### 2026-07-25 15:43

## 雷特 - 朝歌明苑案例 (ltech_case)
- 来源: http://www.ltechonline.com/html/Project-Cases/Chaolisten_Mingyuan.html
manual:PDF缺失
  - URL: http://www.ltechonline.com/catalogue-simple-cn.pdf
  - 说明: 下载失败 (请求失败)

manual:PDF缺失
  - URL: http://www.ltechonline.com/catalogue-smart-home.pdf
  - 说明: 下载失败 (请求失败)


## 雷特 - 碧桂园滨江湾智能家居 (ltech_case)
- 来源: http://www.ltechonline.com/html/Project-Cases/CountryGarden.html
manual:PDF缺失
  - URL: http://www.ltechonline.com/catalogue-simple-cn.pdf
  - 说明: 下载失败 (请求失败)

manual:PDF缺失
  - URL: http://www.ltechonline.com/catalogue-smart-home.pdf
  - 说明: 下载失败 (请求失败)


## 雷特 - DALI金奖案例 (ltech_case)
- 来源: http://www.ltechonline.com/html/Project-Cases/DALI-GoldAward.html
manual:PDF缺失
  - URL: http://www.ltechonline.com/catalogue-simple-cn.pdf
  - 说明: 下载失败 (请求失败)

manual:PDF缺失
  - URL: http://www.ltechonline.com/catalogue-smart-home.pdf
  - 说明: 下载失败 (请求失败)


## 雷特 - 赣州清启案例 (ltech_case)
- 来源: http://www.ltechonline.com/html/Project-Cases/GanzhouQingqi.html
manual:PDF缺失
  - URL: http://www.ltechonline.com/catalogue-simple-cn.pdf
  - 说明: 下载失败 (请求失败)

manual:PDF缺失
  - URL: http://www.ltechonline.com/catalogue-smart-home.pdf
  - 说明: 下载失败 (请求失败)


## 雷特 - HIGOLD案例 (ltech_case)
- 来源: http://www.ltechonline.com/html/Project-Cases/HIGOLD.html
manual:PDF缺失
  - URL: http://www.ltechonline.com/catalogue-simple-cn.pdf
  - 说明: 下载失败 (请求失败)

manual:PDF缺失
  - URL: http://www.ltechonline.com/catalogue-smart-home.pdf
  - 说明: 下载失败 (请求失败)


## 雷特 - 珠海希尔顿酒店 (ltech_case)
- 来源: http://www.ltechonline.com/html/Project-Cases/Hilton_Hotels.html
manual:PDF缺失
  - URL: http://www.ltechonline.com/catalogue-simple-cn.pdf
  - 说明: 下载失败 (请求失败)

manual:PDF缺失
  - URL: http://www.ltechonline.com/catalogue-smart-home.pdf
  - 说明: 下载失败 (请求失败)


## 雷特 - 香港HS案例 (ltech_case)
- 来源: http://www.ltechonline.com/html/Project-Cases/HongKong-HS.html
manual:PDF缺失
  - URL: http://www.ltechonline.com/catalogue-simple-cn.pdf
  - 说明: 下载失败 (请求失败)

manual:PDF缺失
  - URL: http://www.ltechonline.com/catalogue-smart-home.pdf
  - 说明: 下载失败 (请求失败)


## 雷特 - 香港JP超动感世界 (ltech_case)
- 来源: http://www.ltechonline.com/html/Project-Cases/JOYPOLIS-SPORTS.html
manual:图片缺失
  - URL: http://www.ltechonline.com/uploads/news-2025/prodects-case/2025-7-19/10.jpg
  - 说明: 非图片响应 (text/html)

manual:PDF缺失
  - URL: http://www.ltechonline.com/catalogue-simple-cn.pdf
  - 说明: 下载失败 (请求失败)

manual:PDF缺失
  - URL: http://www.ltechonline.com/catalogue-smart-home.pdf
  - 说明: 下载失败 (请求失败)


## 雷特 - 骏地案例 (ltech_case)
- 来源: http://www.ltechonline.com/html/Project-Cases/Jun-Di.html
manual:PDF缺失
  - URL: http://www.ltechonline.com/catalogue-simple-cn.pdf
  - 说明: 下载失败 (请求失败)

manual:PDF缺失
  - URL: http://www.ltechonline.com/catalogue-smart-home.pdf
  - 说明: 下载失败 (请求失败)


## 雷特 - 私人逃逸案例 (ltech_case)
- 来源: http://www.ltechonline.com/html/Project-Cases/private_escape.html
manual:PDF缺失
  - URL: http://www.ltechonline.com/catalogue-simple-cn.pdf
  - 说明: 下载失败 (请求失败)

manual:PDF缺失
  - URL: http://www.ltechonline.com/catalogue-smart-home.pdf
  - 说明: 下载失败 (请求失败)

