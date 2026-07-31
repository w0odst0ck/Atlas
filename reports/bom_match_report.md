> 溯源: Atlas scene-library @ `3bd86ea`（run_match.sh 自动生成）

# BOM 场景匹配报告

**产品**: 智能IoT雷达感应灯管
**生成时间**: 2026-07-31 23:00

---

## 📊 摘要

| 指标 | 值 |
|------|-----|
| 评估场景数 | 8 |
| 通过硬约束 | 7 |
| 平均匹配分 | 83.75% |

## 🏆 最佳匹配

**冷库/冷链** — 100.0%
> ✅ 强烈推荐用于此场景

## 📋 场景匹配详情

### 1. 冷库/冷链

**✅ 推荐** — 匹配分: **100.0%**

**维度评分:**

| 维度 | 得分 | 权重 | 加权分 |
|------|------|------|--------|
| temp_margin | 100.00% | 30% | 30.00% |
| ip_match | 100.00% | 25% | 25.00% |
| sensor_match | 100.00% | 20% | 20.00% |
| communication_match | 100.00% | 15% | 15.00% |
| power_match | 100.00% | 10% | 10.00% |

- **temp_margin**: -40.0 在理想区间 [-999, -30]
- **ip_match**: IP ['IP30', 'IP40', 'IP67'] ≥ IP66, 得分 1.00
- **sensor_match**: 值 'radar_5.8G' → 映射得分 1.0
- **communication_match**: 交集得分 1.0 (值: ['rs-485', 'rs-232', 'lora', 'zigbee', 'ethernet'], 理想: ['lora', 'rs-485', 'ethernet'])
- **power_match**: 12.0 在理想区间 [10, 15]

---

### 2. 长走廊/通道

**✅ 推荐** — 匹配分: **100.0%**

**维度评分:**

| 维度 | 得分 | 权重 | 加权分 |
|------|------|------|--------|
| neighbor_notify_match | 100.00% | 30% | 30.00% |
| fade_match | 100.00% | 25% | 25.00% |
| sensor_match | 100.00% | 20% | 20.00% |
| hold_time_match | 100.00% | 15% | 15.00% |
| power_match | 100.00% | 10% | 10.00% |

- **neighbor_notify_match**: 全部特性匹配 1/1
- **fade_match**: 全部特性匹配 2/2
- **sensor_match**: 值 'radar_5.8G' → 映射得分 1.0
- **hold_time_match**: 全部特性匹配 1/1
- **power_match**: 12.0 在理想区间 [8, 16]

---

### 3. 工业厂房/车间

**✅ 推荐** — 匹配分: **100.0%**

**维度评分:**

| 维度 | 得分 | 权重 | 加权分 |
|------|------|------|--------|
| protocol_match | 100.00% | 25% | 25.00% |
| efficacy_match | 100.00% | 20% | 20.00% |
| communication_match | 100.00% | 20% | 20.00% |
| sensor_match | 100.00% | 15% | 15.00% |
| zone_control_match | 100.00% | 10% | 10.00% |
| environment_match | 100.00% | 10% | 10.00% |

- **protocol_match**: 多协议匹配得分 1.00
- **efficacy_match**: 180.0 在理想区间 [160, 999]
- **communication_match**: 交集得分 1.0 (值: ['rs-485', 'rs-232', 'lora', 'zigbee', 'ethernet'], 理想: ['rs-485', 'ethernet'])
- **sensor_match**: 值 'radar_5.8G' → 映射得分 1.0
- **zone_control_match**: 全部特性匹配 2/2
- **environment_match**: IP ['IP30', 'IP40', 'IP67'] ≥ IP54, 得分 1.00

---

### 4. 物流仓储

**✅ 推荐** — 匹配分: **100.0%**

**维度评分:**

| 维度 | 得分 | 权重 | 加权分 |
|------|------|------|--------|
| communication_range_match | 100.00% | 25% | 25.00% |
| efficacy_match | 100.00% | 20% | 20.00% |
| environment_match | 100.00% | 20% | 20.00% |
| sensor_match | 100.00% | 15% | 15.00% |
| communication_downlink | 100.00% | 10% | 10.00% |
| protocol_match | 100.00% | 10% | 10.00% |

- **communication_range_match**: 200.0 在理想区间 [150, 999]
- **efficacy_match**: 180.0 在理想区间 [170, 999]
- **environment_match**: IP ['IP30', 'IP40', 'IP67'] ≥ IP54, 得分 1.00
- **sensor_match**: 值 'radar_5.8G' → 映射得分 1.0
- **communication_downlink**: 交集得分 1.0 (值: ['rs-485', 'rs-232', 'lora', 'zigbee', 'ethernet'], 理想: ['lora', 'zigbee'])
- **protocol_match**: 交集得分 1.0 (值: ['modbus', 'opc_ua', 'siemens_plc', 'mitsubishi_plc'], 理想: ['modbus'])

---

### 5. 隧道照明

**✅ 推荐** — 匹配分: **100.0%**

**维度评分:**

| 维度 | 得分 | 权重 | 加权分 |
|------|------|------|--------|
| efficacy_match | 100.00% | 25% | 25.00% |
| ip_match | 100.00% | 20% | 20.00% |
| communication_match | 100.00% | 20% | 20.00% |
| protocol_match | 100.00% | 15% | 15.00% |
| sensor_match | 100.00% | 10% | 10.00% |
| temp_margin | 100.00% | 10% | 10.00% |

- **efficacy_match**: 180.0 在理想区间 [170, 999]
- **ip_match**: IP ['IP30', 'IP40', 'IP67'] ≥ IP65, 得分 1.00
- **communication_match**: 交集得分 1.0 (值: ['rs-485', 'rs-232', 'lora', 'zigbee', 'ethernet'], 理想: ['lora', 'rs-485', 'ethernet'])
- **protocol_match**: 交集得分 1.0 (值: ['modbus', 'opc_ua', 'siemens_plc', 'mitsubishi_plc'], 理想: ['modbus', 'opc_ua'])
- **sensor_match**: 值 'radar_5.8G' → 映射得分 1.0
- **temp_margin**: -40.0 在理想区间 [-999, -25]

---

### 6. 地下车库

**✅ 推荐** — 匹配分: **100.0%**

**维度评分:**

| 维度 | 得分 | 权重 | 加权分 |
|------|------|------|--------|
| sensor_match | 100.00% | 25% | 25.00% |
| communication_match | 100.00% | 20% | 20.00% |
| power_match | 100.00% | 15% | 15.00% |
| installation_match | 100.00% | 15% | 15.00% |
| environment_match | 100.00% | 15% | 15.00% |
| protocol_match | 100.00% | 10% | 10.00% |

- **sensor_match**: 值 'radar_5.8G' → 映射得分 1.0
- **communication_match**: 交集得分 1.0 (值: ['rs-485', 'rs-232', 'lora', 'zigbee', 'ethernet'], 理想: ['lora', 'zigbee'])
- **power_match**: 12.0 在理想区间 [10, 20]
- **installation_match**: 布尔字段匹配 1/1
- **environment_match**: IP ['IP30', 'IP40', 'IP67'] ≥ IP40, 得分 1.00
- **protocol_match**: 交集得分 1.0 (值: ['modbus', 'opc_ua', 'siemens_plc', 'mitsubishi_plc'], 理想: ['modbus'])

---

### 7. 洁净车间/洁净室

**⚠️ 条件适配** — 匹配分: **70.0%**

**维度评分:**

| 维度 | 得分 | 权重 | 加权分 |
|------|------|------|--------|
| ra_match | 0.00% | 30% | 0.00% |
| ip_match | 100.00% | 20% | 20.00% |
| efficacy_match | 100.00% | 15% | 15.00% |
| sensor_match | 100.00% | 15% | 15.00% |
| communication_match | 100.00% | 10% | 10.00% |
| installation_match | 100.00% | 10% | 10.00% |

- **ra_match**: 0 < 80, 偏差 80, 得分 0.00
- **ip_match**: IP ['IP30', 'IP40', 'IP67'] ≥ IP54, 得分 1.00
- **efficacy_match**: 180.0 在理想区间 [150, 999]
- **sensor_match**: 值 'radar_5.8G' → 映射得分 1.0
- **communication_match**: 交集得分 1.0 (值: ['rs-485', 'rs-232', 'lora', 'zigbee', 'ethernet'], 理想: ['rs-485', 'ethernet'])
- **installation_match**: 布尔字段匹配 1/1

**Gap 分析:**

  - 🟡 **ra_match**: 值 0 低于理想最小值 80，偏差 80
    当前: `0` | 需求: `≥80`

---

### 8. 学校教室

**❌ 未通过硬约束** — 此场景不推荐
- `certification.ccc` 要求 `eq True`，BOM 不满足
  - ▲ 必须通过国家强制性 CCC 认证
- `product_specs.ra` 要求 `gte 90`，BOM 不满足
  - 显色指数 Ra ≥ 90
- `product_specs.r9` 要求 `gte 90`，BOM 不满足
  - R9 ≥ 90
- `certification.blue_light_rating` 要求 `eq RG0`，BOM 不满足
  - 蓝光认证：无危险类 RG0
- `certification.flicker_rating` 要求 `in ['无显著影响', '无危害类']`，BOM 不满足
  - 频闪认证：无显著影响或无危害类
- `product_specs.redundancy_ratio` 要求 `gte 3.5`，BOM 不满足
  - LED模块总功率与额定功率之比 ≥ 3.5
- `product_specs.upward_flux_ratio` 要求 `gte 10`，BOM 不满足
  - ▲ 上射光通量占总光通量 ≥ 10%（视觉舒适度）
- `product_specs.up_down_cct_diff` 要求 `lte 50`，BOM 不满足
  - ▲ 上下色温差 ≤ 50K
- `product_specs.luminance_uniformity` 要求 `gte 0.8`，BOM 不满足
  - 发光面亮度均匀度 ≥ 0.8
- `product_specs.cct.max` 要求 `lte 5200`，BOM 不满足
  - 色温 5000K ±200K（上限）
