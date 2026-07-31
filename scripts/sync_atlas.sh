#!/usr/bin/env bash
# sync_atlas.sh — 公司电脑侧：拉取最新 Atlas（含家用主机回传的报告）
# 用法: ./scripts/sync_atlas.sh

set -euo pipefail

ATLAS_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"

echo "=== pull Atlas（含 reports 回流）==="
git -C "$ATLAS_ROOT" pull --rebase
echo "=== 最近报告 ==="
ls -t "$ATLAS_ROOT"/reports/*_match_report.md 2>/dev/null | head -5 || echo "（暂无报告）"
echo "✅ 同步完成"
