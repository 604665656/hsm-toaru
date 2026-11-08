# CHANGELOG v0.33

## 主修复：回退毛边 + 扩大载入范围
| | v0.32（否决） | v0.33 |
|---|---|---|
| 显示源 | 补不规则毛边层 21+17+20 帧 | **回到 v0.31 完整贴图，一个像素不改** |
| 角色容器 | 混用 cover/contain | 统一 `contain`，场景板才 cover |
| 缩略图盒 | 82px / 54px | 96px / 64px |
| 舞台安全边 | 90% / top2% | 80% / top3% |
| 边缘观感 | 发红发糊 | 干净 |

## 借鉴落地
- 新增 `fitBox()` 等比矩形 + `classifyFitRole()` + `applyFitRules()` + `MutationObserver` 自动套用分层规则
- 新增 `LAYOUT_RULES` 声明式规则表；`v19ActorLegal` / `v19BoxLegal` / 回弹循环 / 水平钳制 5 处魔数改为读规则
- 小游戏玩家层 `drawImage` 改用 `fitBox`，不再硬编码 `-38,-47,76,95`

## 小游戏输入
- `pointerdown` / `pointermove` / `pointerup` / `pointercancel` + `setPointerCapture`，`pointerType` 无关
- 拖动 lerp 跟手（`dt*18`），去掉 430px/s 限速
- 收集半径 +12px（触屏宽容）
- 「💨 哈气」按钮 + 双击画布哈气；键盘保留（WCAG 2.5.7 单指针替代）
- 说明文案与 `aria-label` 同步更新

## 本轮素材
- 真生成 2 张：`golden_raw.jpg`、`rainbow_seminary_raw.jpg`（Image2Image / 现有场景板基准）
- 接入上轮 2 张：`rainbow_v033.webp`、`moonlit_v033.webp`
- 4 张全部去水印 → 内嵌关于页 + 展柜；`ASSET_SCENES` 29 → **33**

## 验收（Chromium）
| 项 | 结果 |
|---|---|
| 版本 / 启动错误 | v0.33 / 0 |
| chars 逐键一致 v0.31 | 21/21 |
| 390×844 / 820×1180 / 1024×768 / 1170×2532 溢出 | 0 / 0 / 0 / 0 |
| 鼠标拖动 / 触屏 Pointer 拖动 | 5/5 · 5/5 |
| 键盘替代路径 | y 392→307 |
| 最终态背景 / 立绘 | `block` / 全 `contain` |
| 4 张新图 naturalWidth | 720 ×4 |
| 破图 / undefined src / 原稿按钮 | 0 / 0 / 0 |
| HTML | 8.0 MB |
