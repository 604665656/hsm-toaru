# CHANGELOG v0.26

## 修复
1. **通关链路**：两套 `choose` 里的 `confirm` 分支删除，答对直接 `finishQuest(q.id)`；`showClear` 增加 `playShards(id)` 可选小游戏入口
2. **回弹**：`v19ActorLegal` 阈值 `.55/.40`（HUD/ctl/clear 全判）→ `.34/.55`（只判舞台 + 对白气泡）；`end18` 弹回改 14 步 ×0.84 就近回缩；`ensureVisible19` 去掉 14 步强挪；停用 `endActorPointer` 的二次 transform 写入
3. **裁切**：新增 `.vn-actor.sub.expr-static .bf{object-position:bottom center!important}`

## 新增素材
- `q4_angel_fall_v026.webp`（405×720，41.8 KB）→ `ART.scenes.angelfall_h/_v`，`ASSET_SCENES` 增至 19 条，展柜计数 10 → 11
- `q4_angel_fall_raw.jpg`：AI 生成漂移稿，否决留档
- 21 张定稿层 + v0.25 双翼差分整包留存

## 验收（Chromium 390×844）
| 项 | 结果 |
|---|---|
| 限时开 + 对话框自动确定 | confirm 0 次、vnClear 出现、cleared 加 4 |
| 点「▶ 下一话 · 第 5 关」 | state.active = 5、HUD 显示第 5 关 |
| 第 4 关副角色 object-position | `50% 100%`（脚贴底，完整） |
| 大幅拖出画面松手 | 可见面积 93%，就地弹回不再乱跳 |
| 展柜新场景 | `ASSET_SCENES.length=19`、`angelfall_h` 有图 |
| 页内错误 / 破图 / 原稿按钮 | 0 / 0 / 0 |

单文件 4.49 MB。
