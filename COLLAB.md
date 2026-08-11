# COLLAB.md · 双仓协作手册（单机版）

> 两个仓库、一台机器（家用主机）、一条工作流。
> 2026-08-05：公司电脑编辑线已砍，全部编辑在本机；双机同步负担移除。

## 拓扑

```
家用主机（本机）
├── Atlas  D:\ZZZ\NOTES\Atlas   （轻文档：计划/课纲/方案/场景库/报告）
└── Forge  D:\ZZZ\NOTES\Forge   （工程：训练包/引擎/仿真/进度/架构）
```

**依赖方向：** Forge 读 Atlas（场景库/计划）；Atlas 不依赖 Forge。
**vault 关系：** 两仓同在 Obsidian vault `D:\ZZZ\NOTES`，Obsidian 内可直接互链互跳。

---

## 路径约定

| 环境 | 路径 |
|------|------|
| Obsidian / Windows | `D:\ZZZ\NOTES\{Atlas,Forge}`（真实目录） |
| OpenClaw（WSL） | `/home/l/.openclaw/workspace/projects/{Atlas,Forge}`（symlink → D 盘） |
| 文档/命令示例 | 一律用 **git 根相对路径**（如 `../Atlas` = 兄弟仓，机器无关） |

> WSL 侧 `projects/Atlas`、`projects/Forge` 是 symlink，git 走 symlink 路径即可；D 盘仓库已设 `core.fileMode false`（DrvFS 权限位全 777，不设会误报全量 M）。

---

## 双仓定位

| | Atlas（文档仓） | Forge（工程仓） |
|---|---|---|
| 内容 | 方案/计划/课纲/场景库/学习材料（`learning/`） | 引擎/实验代码（`labs/`）/脚本/仿真 |
| 性质 | **文档域**：学习看板动态 + 基线稳定 | **工程域**：代码/仿真动态 |
| 变更 | 学习域看板随进度更新；计划仅纠错回流 + 里程碑 | 一切工程动态 |

## 学习模式（互动式陪伴学习）

> 机制见 OpenClaw skill `pair-learning` v2（2026-08-11 整合 interactive-learning 后统一维护；先讲→检验→点评→沉淀）
> ⚠️ W1 过渡期：复习本仍用 notes.md 单文件（旧体系），**W2 起切 pair-learning 三文件体系**（手册/quiz/review + checklist）

- **互动循环**：一个知识点 → 先讲（一句话本质→详细→类比）→ 检验（开放问题）→ 点评（肯定→精确化→纠正→记忆点）→ 沉淀
- **复习本**：`learning/w{N}/notes.md` 单文件聚合（`<details>` 折叠自测 + 📌 易错点冲刺区 + 概念回链 + 自评），每 W 一文件
- **概念卡**：`study-cards.md`（标准定义通道，复习本 = 自测通道，职责分离）
- **看板**：掌握度看板 `learning/w{N}/README.md`，每 D 完成时 Agent 更新

---

## 双仓同步协议

### 回流规则（按域）

```
纠错回流（回 A）：F 发现基线技术细节不成立（如 BME280→MPU6050）→ 当日修 A 计划文档
状态回流（按域）：学习域进度（看板/掌握度）在 A `learning/w1/README.md`；工程域状态在 F
```

### 同步触发（三种）

1. **每完成一个 D**（用户确认）→ A 看板更新 + 概念卡进 `learning/w1/study-cards.md`
2. **技术决策变更** → A 记 ADR（`learning/w1/architecture/ADR.md`，含「影响文件」字段）+ 当日纠错回流
3. **里程碑/周复盘**（D7、W1 完成）→ 双向核对一致性

### 互链清单（只链接，不复制内容）

| A 侧 | F 侧 | 关系 |
|------|------|------|
| `tech-plans/4week-awakening.md` | `learning/w1/README.md`（A 内互链） | 计划 ↔ 学习看板 |
| `learning/w1/D*/README.md` | `labs/w1/D*/` | 学习指引 ↔ 实验代码 |
| `plan/courses.md`（A 层） | `learning/w1/architecture/`（A 内互链） | 课纲 ↔ 架构认知 |
| `COLLAB.md` | `../Atlas/COLLAB.md` | 协作手册（A 为源） |
| `scene-library/` | `engine/` | 场景定义（F 只读） |
| `reports/` | `scripts/run_match.sh` | 仿真报告回传 |

### 一致性自查（每 D 完成时）

- [ ] A 计划技术细节 = 学习域实现？（变更即查）
- [ ] 互链路径有效 + 文档/代码对称？（跑 `Forge/scripts/verify-links.sh`）

---

## git 约定

1. push 前 `git pull --rebase`（单机也保持习惯，防远端漂移）
2. 报告文件与场景文件不重叠（`reports/` vs `scene-library/`），冲突概率低
3. 不 `git push --force`

---

## 脚本清单

| 脚本 | 位置 | 作用 |
|------|------|------|
| `run_match.sh` | Forge/scripts/ | 一键仿真：pull Atlas → 跑引擎 → 报告回传 push |
| `verify_engine.sh` | Forge/scripts/ | 本地引擎自检（无 Atlas 也跑，用内置示例） |
| `verify-links.sh` | Forge/scripts/ | 双仓互链验证（A↔F 相对路径全有效） |

---

## 仓库清单

| 仓库 | 远端 | 角色 |
|------|------|------|
| Atlas（方案馆） | github.com/w0odst0ck/Atlas | 场景库/方案/计划/报告 |
| Forge（仿真实验室） | github.com/w0odst0ck/Forge | 引擎/仿真/训练包 |

---

## CI

Forge 有 GitHub Actions：`engine` 变更自动跑 BOM 引擎验证（含真实场景库快照）。绿了才可合入。
