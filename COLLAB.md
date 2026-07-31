# COLLAB.md · 双机协作手册

> 两个仓库、两台机器、一条工作流。

## 拓扑

```
公司电脑（无显卡）                家用主机（RTX 3060）
├── Atlas  ←主仓→  git  ├── Atlas（场景库/报告回流）
└── 内容/方案/素材               └── Forge（主仓，计算）
```

**依赖方向：** Forge 读 Atlas 的场景库；Atlas 不依赖 Forge。
**双写说明：** Atlas 是**双写仓**——公司电脑写方案/场景，家用主机写仿真报告（`reports/`）。两个方向都要遵守「push 前先 pull」约定（见下）。

---

## 路径约定（重要）

| 环境 | 路径 |
|------|------|
| **OpenClaw 实际运行（WSL 内）** | `/home/l/.openclaw/workspace/projects/{Atlas,Forge}` |
| Windows 侧（公司电脑） | `D:\projects\{Atlas,Forge}` |
| 文档/命令示例 | 一律用 **git 根相对路径**（机器无关，见下方命令） |

> 文档里的 `D:\projects\...` 仅是 Windows 侧逻辑路径。实际执行命令时用相对路径：在 Atlas/Forge 仓库根目录内操作，`../Atlas` 表示兄弟仓库。

---

## 工作流

### 方向 1：方案/场景编辑（公司电脑 → 家用主机）

```bash
# 公司电脑（Atlas 仓库根）
git pull --rebase          # 先收家用主机回传的报告，避免冲突
# 编辑 solutions/、scene-library/、refs/、retrofit/ 等
git add -A
git commit -m "feat: 新增 XX 场景定义"
git push

# 家用主机（Atlas 仓库根）
git pull --rebase
```

### 方向 2：仿真测试（家用主机 → 公司电脑）

```bash
# 家用主机（Forge 仓库根）
./scripts/run_match.sh engine/examples/bom_sample.toml
# 脚本内部：pull Atlas → 跑引擎 → 报告写入 Atlas/reports/ → push（含 commit 溯源）

# 公司电脑（Atlas 仓库根）
git pull --rebase          # 拿到报告即可写方案
```

### ⚠️ 冲突处理约定（双写仓必读）

1. **push 前必 pull --rebase**（两个方向都适用）
2. 报告文件与场景文件基本不重叠（`reports/` vs `scene-library/`），冲突概率低；万一冲突，保留双方改动后 commit
3. 不要 `git push --force`，除非明确知道在做什么

---

## 大文件通道

refs 图片/PDF 不入库（见 Atlas/.gitignore），需要时从公司电脑本地取：

```bash
# 公司电脑 → 家用主机（示例，按实际 IP 改）
scp -r user@company-ip:/d/projects/Atlas/refs /home/l/refs-backup/
```

| 通道 | 适用 | 说明 |
|------|------|------|
| git | 文本类（md/toml/代码） | 正常流程 |
| scp/rsync | 图片/PDF 批量 | 按需手动，不入库 |
| 网盘/共享盘 | 一次性大包 | 备选 |

---

## 脚本清单

| 脚本 | 位置 | 作用 |
|------|------|------|
| `run_match.sh` | Forge/scripts/ | 一键仿真：pull Atlas → 跑引擎 → 报告回传 push |
| `verify_engine.sh` | Forge/scripts/ | 本地引擎自检（无 Atlas 也跑，用内置示例） |
| `sync_atlas.sh` | Atlas/scripts/ | 公司电脑拉取最新（含报告回流） |

---

## 仓库清单

| 仓库 | 远端 | 主要操作机 | 角色 |
|------|------|-----------|------|
| Atlas（方案馆） | github.com/w0odst0ck/Atlas | 公司电脑（写）+ 家用主机（写 reports） | 场景库/方案/素材/报告 |
| Forge（仿真实验室） | github.com/w0odst0ck/Forge | 家用主机 | 引擎/仿真/测试 |

---

## CI

Forge 有 GitHub Actions：`engine` 变更自动跑 BOM 引擎验证（含真实场景库快照）。绿了才可合入。

---

## 机器速查

| 项 | 公司电脑 | 家用主机 |
|----|---------|---------|
| 系统 | Windows | Windows + WSL2（OpenClaw 运行处） |
| GPU | 无 | RTX 3060 12GB（WSL 内 CUDA 可用） |
| Python | - | `/home/l/venvs/gputest/`（torch 2.13+cu130） |
