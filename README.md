# Solution Vault · 方案馆

> 定位：**行业方案知识库 + 智能化改造实践基地**
> 当前聚焦：智能照明改造方案（未来可扩展：汽车等垂直行业方案）

---

## 双项目协作

本项目（`Atlas`）与 [`Forge`](../Forge)（仿真实验室）成对工作：

| | Atlas（本仓） | Forge（仿真仓） |
|---|---|---|
| **运行位置** | 公司电脑（无显卡） | 家用主机（RTX 3060 ×2） |
| **内容** | 方案文档 / 素材 / 场景定义 / 采集工具 | 引擎代码 / 数字孪生 / 仿真 |
| **工作流** | 编辑 → push | pull 场景库 → 跑仿真 → 报告回传 |

协作细节见 [`COLLAB.md`](COLLAB.md)

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
├── collector/          # [工具] 采集器（公司电脑运行）
├── retrofit/           # [实践] 智能化改造（方法论/案例/方案）
├── plan/               # [学习] 学习路径
├── case/               # [案例] 项目案例
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
  3. plan/courses.md → 知识栈学习路径（学什么/课程资料）
  4. scene-library/scenes/ → 场景定义（引擎输入）

跑仿真测试（家用主机）：
  1. git pull
  2. cd ../Forge/engine
  3. python -m src.cli match <bom> --scene-dir ../Atlas/scene-library/scenes
```

---

## 背景

- **创建时间**：2026-07-23（原名"智能照明方案馆"，2026-07-31 重组为 Atlas）
- **素材规模**：277 篇精洗正文 / 20 场景 / 56+ 采集来源
- **定位演进**：常规照明归档 → 智能化改造实践 → 多行业方案库（未来）
