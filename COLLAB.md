# COLLAB.md · 双机协作手册

> 两个仓库、两台机器、一条工作流。

## 拓扑

```
公司电脑（无显卡）                家用主机（RTX 3060 ×2）
├── solution-vault  ←主仓→  git  ├── solution-vault（只读引用）
└── 内容/采集/方案                 └── sim-lab（主仓，计算）
```

**依赖方向：** sim-lab 读 solution-vault 的场景库；solution-vault 不依赖 sim-lab。

---

## 工作流

### 方向 1：方案/场景编辑（公司电脑 → 家用主机）

```bash
# 公司电脑
cd D:\projects\solution-vault
# 编辑 solutions/、scene-library/、refs/、retrofit/ 等
git add -A
git commit -m "feat: 新增 XX 场景定义"
git push

# 家用主机
cd D:\projects\solution-vault
git pull
```

### 方向 2：仿真测试（家用主机 → 公司电脑）

```bash
# 家用主机
cd D:\projects\sim-lab\engine
python -m src.cli match D:\projects\sim-lab\engine\examples\bom_sample.toml \
  --scene-dir D:\projects\solution-vault\scene-library\scenes \
  --output-dir D:\projects\solution-vault\reports

# 报告进入 solution-vault/reports/，提交回传
cd D:\projects\solution-vault
git add reports/
git commit -m "report: 灯管BOM 场景匹配报告"
git push

# 公司电脑 pull 后即可写方案
```

---

## 机器约定

| 项 | 约定 |
|----|------|
| 两机路径 | 统一 `D:\projects\solution-vault` / `D:\projects\sim-lab` |
| 场景库读取 | `--scene-dir ../solution-vault/scene-library/scenes`（相对 sim-lab） |
| 报告回流 | 一律写入 `solution-vault/reports/` |
| 大文件 | refs 图片/PDF 不入库（gitignore），需要时从公司电脑本地取 |

---

## 仓库清单

| 仓库 | 远端 | 本地目录 | 主要操作机 |
|------|------|----------|-----------|
| Atlas（方案馆） | github.com/w0odst0ck/Atlas | `D:\projects\solution-vault` | 公司电脑 |
| Forge（仿真实验室） | github.com/w0odst0ck/Forge | `D:\projects\sim-lab` | 家用主机 |
