# CHANGELOG v0.29

## 主修复：角色舞台页横宽盒
- `.char-btn img` 由 `height:96px;width:100%` → `height:auto;aspect-ratio:4/5;object-fit:contain;object-position:center center;padding:4px 0;box-sizing:border-box`
- `.char-grid` 手机 3 列 / 桌面 5 列；`.char-btn` 取消 `min-height:150px` 硬撑
- `.case18-th>img` 加 `object-position:center center` 与 5px 安全内边距
- 三种视口实测：96×120 / 134×168 / 202×253，比例全部 **0.80**，21 张 `cover` 数 0，平均填充 81 / 84 / 87%

## 诊断留痕
- 三角色定稿层 + 差分层 alpha 四边全 0，bbox 距边 10px → **源图未裁**
- 全站 `object-fit:cover` 的 img 只有 fullBg / stage-bg / case18-bg（都是背景板）→ **角色未被 CSS 裁**
- 结论：裁切感来自容器比例，不是像素裁切

## 本轮素材
- 生成 2 张：`street_dusk_raw.jpg`（进网页）、`three_cards_raw.jpg`（**否决留档**：漏神裂 / 比例没生效 / 水印）
- 确定性产出：`street_dusk_v029.webp`、`三角色_完整卡_v029.webp`、`三角色_并排基准.png`、3 张 `_safe.webp` + 3 张 `_expr_safe.webp`
- 接入：`ART.scenes.dusk_h/_v`、`threecats_h/_v`、`ART.cardsV29`、`ART.safeLayers`、`ASSET_SCENES` 22 → **24**

## 验收（Chromium 390×844 / 820 / 1280）
| 项 | 结果 |
|---|---|
| 启动错误 / 破图 / 原稿按钮 | 0 / 0 / 0 |
| 角色卡竖比 | 0.80 / 0.80 / 0.80 |
| 角色卡 cover 数 | 0 |
| 关于页 v29 两张图 | 800 / 720 naturalWidth |
| 展柜 | 24 条、`ART.safeLayers` 有值 |
| 单文件 | 5.9 MB |
