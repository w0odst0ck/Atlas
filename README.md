# Solution Vault · 方案馆（A 仓）

> 定位：**知识/设计/学习侧**（D 盘，Obsidian 直接读改）
> 承载：行业方案知识库 + 场景数据（scene-library）+ 项目设计文档 + 项目伴随学习文档
> 2026-08-20 结构变更：与 F 仓（Forge）按"代码/知识"分离——代码在 WSL，知识在此。

---

## A/F 双仓协作（2026-08-20 定）

| | A 仓（本仓，D 盘/Obsidian） | F 仓（Forge，WSL） |
|---|---|---|
| **内容** | 知识/设计/场景数据/学习文档 | 代码/数据/执行/项目日志 |
| **典型文件** | md（方案/学习地图/单元） | py / toml / memory |
| **使用方** | 你（Obsidian 读改）+ 我 | 我 + reasonix |

- **F 读 A**：场景库跨仓引用（`../Atlas/scene-library/scenes`，相对 F 仓根）
- **A 不链 F**：Obsidian 读不到 WSL，本仓文档用路径文字描述 F 文件
- 设计文档/学习文档一律进本仓；代码/实验/日志进 F 仓
- 协作细节见 [`COLLAB.md`](COLLAB.md)

---

## 目录结构

```
Atlas/
├── solutions/          # [知识库] 场景方案摘要（17 场景）
├── refs/               # [知识库] 采集素材（文本入库，图片/PDF 本地保留）
├── scene-library/      # [知识] 场景定义 TOML + 品类 schema（引擎消费）
│   ├── scenes/         #   场景库（车库/教室/仓库/隧道…）
│   ├── schemas/        #   品类 schema（灯管/面板灯）
│   └── matching_rules.toml
├── tech-plans/         # [知识] 技术方案沉淀
│   ├── ROADMAP.md                # 三年技术路线图
│   ├── tech-stack.md             # 技术栈选型
│   ├── 4week-awakening.md        # 4周零硬件唤醒计划
│   ├── bom-scene-engine.md       # BOM 场景匹配引擎方案
│   └── classroom_retrofit.md     # 教室灯智能化改造方案
├── plan/               # [设计] 项目设计文档
│   └── gs-lighting/              # GS-Lighting 技术方案 v1.1（主项目设计）
├── learning/           # [学习] 项目伴随学习文档
│   ├── w1/                       # 嵌入式 W1（历史，完结）
│   └── gs-lighting/              # ⭐ 学习地图 + 学习单元 U1-U6（项目驱动）
├── memory/             # [记忆] 历史记录
├── reports/            # [输出] 仿真报告回流（来自 Forge）
├── COLLAB.md           # 双机协作手册
└── README.md
```

---

## 快速开始

```
查阅常规照明方案：
  1. solutions/{scene}.md → 场景摘要
  2. refs/{scene}/*_clean.md → 精洗正文

做智能化改造方案：
  1. retrofit/README.md → 改造总纲
  2. retrofit/learning-roadmap.md → 学习路线
  3. scene-library/scenes/ → 场景定义（引擎输入）

跑仿真（家用主机 WSL）：
  1. cd projects/Forge/engine
  2. python -m src.cli match <bom> --scene-dir ../Atlas/scene-library/scenes

GS-Lighting 项目（当前主线）：
  1. plan/gs-lighting/技术方案-v1.1.md → 设计
  2. learning/gs-lighting/README.md → 学习地图（项目↔学习闭环）
  3. 代码：projects/Forge/gs-lighting/（WSL）
```

---

## 背景

- **创建时间**：2026-07-23（原名"智能照明方案馆"，2026-07-31 重组为 Atlas）
- **素材规模**：277 篇精洗正文 / 20 场景 / 56+ 采集来源
- **定位演进**：常规照明归档 → 智能化改造实践 → 多行业方案库（未来）
