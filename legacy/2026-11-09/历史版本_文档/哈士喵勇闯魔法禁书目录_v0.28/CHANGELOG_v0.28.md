# CHANGELOG v0.28

## 本轮素材（3 张生成稿 → 2 件进网页 + 1 张否决留档）
| 生成稿 | 方式 | 结果 |
|---|---|---|
| `card_red_raw.jpg` | Image2Image / 基准=用户图 82 | → `card_red_v028.webp`，进网页 |
| `card_kuroko_raw.jpg` | Image2Image / 基准=用户图 83 | → `card_kuroko_v028.webp`，进网页 |
| `expr_sheet_raw.jpg` | Text2Image 自由发挥 | **用户否决**，留档不进网页 |

处理：右下水印 inpaint；不硬裁，整张 `contain` 放进 800×1000 4:5 卡，底部加中文名条。

## 裁切感修复
1. `.case18-th>img` 由 `height:54px;object-fit:cover` 改为 `height:96px!important;object-fit:contain!important`
2. `.case18-th` 最小高 130px、`.case18-grid` 最大高 264px
3. `.vn-char.sub/.sub2` 宽度 30%/27% + `object-position:bottom center`；`.bf` 同步
4. `.vn-actor.sub/.sub2` 宽 30%/27% 加强制优先级
5. 全站角色图统一 `contain`，只有背景板 `cover`

## 接入
- 关于／版本页新增可见章节，内嵌两张 800×1000 完整卡
- `ART.cardsV28`、`ART.scenes.cardred_h/_v`、`cardkuroko_h/_v`
- `ASSET_SCENES` 20 → **22**，展柜计数 12 → 14

## 验收（Chromium 390×844 DPR2）
| 项 | 结果 |
|---|---|
| 启动错误 / 破图 / 原稿按钮 | 0 / 0 / 0 |
| 缩略图 | `76×96` 0.79:1 / contain / 填充 99·94·99% |
| 舞台主角色 | `304×331` contain，drawn 286×331（94%），完整 |
| 舞台副角色 | `104×178` / `50% 100%` 脚贴底，完整 |
| 两张卡 | `naturalWidth=800`、展柜 22 条 |
| 单文件 | 5.36 MB |

## 过程留痕
首次构建时说明块内用了双引号属性，落在双引号 JS 字符串里导致启动崩溃（`Unexpected identifier 'v28'`）；已从 v0.27 干净重建，说明块内 HTML 属性统一单引号，当前启动错误 0。
