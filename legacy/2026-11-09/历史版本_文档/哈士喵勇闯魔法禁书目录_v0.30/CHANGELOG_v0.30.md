# CHANGELOG v0.30

## 本轮素材（3 张真生成稿 → 全部进网页）
| 生成稿 | 基准 | 结果 |
|---|---|---|
| `index_card_raw.jpg` | 单角色定稿合成品红幕 | `index_card_v030.webp` 进网页 |
| `kuroko_card_raw.jpg` | 单角色定稿合成品红幕 | `kuroko_card_v030.webp` 进网页 |
| `kanzaki_card_raw.jpg` | 单角色定稿合成品红幕 | `kanzaki_card_v030.webp` 进网页 |

全部 Image2Image、单主体基准、无否决；去水印 + `contain` 放进 800×1000 卡片，不硬裁。

## 主修复：末尾覆盖层
- 发现文件末尾「覆盖层」IIFE 在最后把 `ART.expr` 三键写回旧层，导致前两轮所有前置修改失效
- 覆盖层三键 + `ART.chars` 三键 + `ART.expr` 三键 + `ART.breath`（index 替换 / kuroko·kanzaki 新增）四处统一换安全留白层
- 安全留白：定稿层四周 20%×14% 透明画布，实测距边 67–94px；表情差分与呼吸双帧都保留
- 呼吸 b 帧为确定性纵向 +2.2% 缩放，不用 AI，零漂移
- CSS：`.vn-actor .bf / .vn-char` 统一 `object-position:center bottom`

## 接入
- 关于页新增三卡可见章节 `.v30-cards`
- `ART.cardsV30` / `ART.scenes.card30_*` / `ASSET_SCENES` 24 → **27**

## 验收（Chromium 390×844 DPR2）
| 项 | 结果 |
|---|---|
| 启动错误 / 破图 / undefined src / 原稿按钮 | 0 / 0 / 0 / 0 |
| 第 1 关 | `482×539` 安全层 |
| 第 5 关 | `514×541`（茵蒂克丝）/ `522×520`（神裂） |
| 第 6 关 | `589×561`（白井） |
| 三卡 / 展柜 | 800 naturalWidth / 27 条 |
| 单文件 | 6.9 MB |

## 诊断留痕（如实记录）
排查中曾两次误判：把 `expr` 段的键当成 `breath`、把正则窗口截断的 16 键当成 `chars` 缺 `kanzaki`。
最终以全量花括号计数 + 浏览器实测为准：**根因是末尾覆盖层**，不是缺键、不是源图被裁。
