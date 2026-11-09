# CHANGELOG v0.31

## 主修复：半身模式 108% 溢出
| | 修复前 | 修复后 |
|---|---|---|
| `.vn.frame-half .vn-char` | `height:100%;top:8%` → 底部 108% | `height:90%;top:2%` → 底部 92% |
| 通用兜底 | 无 | `max-height:92%` |
| 副角色 | `height:50%;top:17%` | `height:44%;top:12%` |
| 全身模式 | `height:100%` | `height:76%` |
| 1024×768 溢出 | 41px | **0** |
| 1170×2532 溢出 | 58px | **0** |

舞台 `.vn` 为 `overflow:hidden`，溢出部分被硬切 → 用户连续三轮看到的「裁切」。
小屏 `@media(max-width:520px)` 把 height 覆盖成 64%，所以之前单视口验收漏掉了。

## 气泡
`:root{--dlgA:.30;--dlgA2:.36}` → `.24/.29`；JS `state.alpha` 默认 30 → 24；滑块与存档逻辑不变。

## 本轮素材
- 生成 2 张：`morning_mist_raw.jpg`、`church_pages_raw.jpg`（均 Image2Image / 现有场景板基准）
- 去水印 → `morning_mist_v031.webp`、`church_pages_v031.webp` → 内嵌关于页 + 登记展柜
- `ASSET_SCENES` 27 → **29**

## 验收矩阵（Chromium）
| 视口 | 第1关 | 第5关 | 第6关 | 最大溢出 |
|---|---|---|---|---|
| 390×844 | 0 | 0 | 0 | 0 |
| 768×1024 | 0 | 0 | 0 | 0 |
| 820×1180 | 0 | 0 | 0 | 0 |
| 1024×768 | 0 | 0 | 0 | 0 |
| 1170×2532 | 0 | 0 | 0 | 0 |

全部 `contain`；启动错误 0 / 破图 0 / 原稿按钮 0 / 两张新图 naturalWidth 720；HTML 7.3 MB。
