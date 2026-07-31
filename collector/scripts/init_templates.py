"""生成 20 个场景方案模板"""
from pathlib import Path

scenes = {
    "office":       ("办公照明方案", "scene:office"),
    "factory":      ("工厂照明方案", "scene:factory"),
    "warehouse":    ("仓储照明方案", "scene:warehouse"),
    "parking":      ("停车场照明方案", "scene:parking"),
    "commercial":   ("商业照明方案", "scene:commercial"),
    "education":    ("教育照明方案", "scene:education"),
    "hospital":     ("医疗照明方案", "scene:hospital"),
    "hotel":        ("酒店照明方案", "scene:hotel"),
    "outdoor":      ("户外照明方案", "scene:outdoor"),
    "emergency":    ("应急照明方案", "scene:emergency"),
    "museum":       ("博物馆照明方案", "scene:museum"),
    "stadium":      ("体育场馆照明方案", "scene:stadium"),
    "airport":      ("机场照明方案", "scene:airport"),
    "metro":        ("地铁照明方案", "scene:metro"),
    "datacenter":   ("数据中心照明方案", "scene:datacenter"),
    "gmp":          ("GMP洁净照明方案", "scene:gmp"),
    "explosion_proof": ("防爆照明方案", "scene:explosion_proof"),
    "marine":       ("船舶/海洋照明方案", "scene:marine"),
    "agriculture":  ("农业/植物照明方案", "scene:agriculture"),
    "landscape":    ("景观亮化照明方案", "scene:landscape"),
}

template = """# {cn} / {tag}

> 状态：待采集
> 采集来源：

---

## 一、场景概述

- **适用场所**：
- **照明需求特点**：
- **相关国标**：

## 二、照明标准

| 指标 | 推荐值 | 参考标准 |
|------|--------|---------|
| 照度标准 | lx | GB 50034 |
| 统一眩光值 UGR | | |
| 显色指数 Ra | | |
| 色温 | K | |
| 照度均匀度 | | |

## 三、推荐产品方案

### 灯具选型

| 区域 | 推荐灯具 | 功率 | 安装方式 | 备注 |
|------|---------|------|---------|------|
| | | | | |

### 控制方式

- [ ] 手动开关
- [ ] 感应控制
- [ ] 定时控制
- [ ] 调光控制
- [ ] 场景控制
- [ ] 集中控制

## 四、方案描述



## 五、参考来源

| 来源 | 内容 | 链接 |
|------|------|------|
| | | |

## 六、商品库关联 SKU

待补充

---

## 采集记录

| 日期 | 动作 |
|------|------|
| | |
"""

solutions_dir = Path(__file__).resolve().parent.parent.parent / "solutions"

for key, (cn, tag) in scenes.items():
    filepath = solutions_dir / key / "README.md"
    content = template.format(cn=cn, tag=tag)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content)

print(f"已生成 {len(scenes)} 个场景模板")
