# CHANGELOG v0.36

## 本轮：点击台词气泡 + 语音包接口
| 项 | v0.35 | v0.36 |
|---|---|---|
| 点击立绘反馈 | 弹跳 / 震动 / 符号 / 短标签 | **+ 文字气泡 + 真图贴片 + 连击双气泡** |
| 台词池 | 4 类固定短词 | **4×10 性格 + 21 角色专属 + 情境/天气/连击** |
| 语音包 | 仅按角色归户播放 | **`window.HuskyVoice` 完整接口 + 情绪归户** |
| 展柜 | 37 条 | **38 条** |
| 贴片素材 | 无 | **4 个透明层** |
| 设置 | — | **💬 点击台词开关** |

## 素材（先补，不等提醒）
- 真生成 2 张：品红幕 2×2 贴片合页、学园都市夜市 9:16 场景板
- 4 个贴片：色相键控 → 最大连通域 → 填洞 → 去绿溢边 → 去色溢，孔洞 0
- 夜市：去水印 → 405×720 竖版 + 同源 720×405 横版
- 全部进网页；零新画角色，21 张定稿层与 17 个差分一字未动

## 代码（末尾单点注入，同一 script 内）
1. 版本号 2 处
2. `ART.stickers` / `ART.scenes.nightmarket_*` / `ASSET_SCENES.push`
3. `window.HuskyVoice`：register / registerMany / play / has / list / clear / on / off / setVolume / attachFiles / moodOf / roleOf
4. 包装 `#packFiles` 的 onchange：原归户照跑，再按情绪注册接口
5. `TAP_POOL36` / `TAP_ROLE36` / `TAP_CTX36` / `pickTap36()`
6. `.vn-tap-bubble` CSS + 互斥放置（候选位最小重叠、HUD 下界、左右钳制）
7. 包装 `poke18`：原函数照跑，追加 `tap36()`（文字气泡 + 语音钩子 + aria-live）
8. 设置开关 DOM 注入 + `state.tapLines` 持久化
9. 包装 `renderAbout` 追加接口文档与本轮素材预览

## 修过的两个坑
- **气泡压 HUD**：旧算法「重叠就往上抬」在半身构图（角色贴顶）会把气泡顶到 top=10，正好压住 HUD。改成 11 个候选位 + 最小重叠面积择优 + `minTop=HUD底+8`，17 关 guard 全 0。
- **连击跨关继承**：切关会重建 `#vnStage`，加 `_tapStage36` 判定，舞台变了就清空连击计数。

## 验收
3 视口 × 17 关：异常 0 项、越屏 0、压组件 0、气泡互叠 0、TTS 0、破图 0、错误 0；连击 2 条互斥；接口 8 mood 全通过；7.3 MB 单文件。
