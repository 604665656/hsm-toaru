# CHANGELOG v0.25

## 新增素材（本轮第一件事）
- `kakine_wings.webp`：垣根帝督左右对称双翼差分，以 v0.06 单翼定稿为唯一基准图生图，只改翅膀
- `kakine_wings_raw.png`：品红幕生成原图（含水印版留档）
- `kakine_input_magenta.png`：合成到纯品红底的输入图，左右各留 82px 给新翼
- `双翼对照_v025.jpg`：单翼定稿 vs 双翼差分

## 修复
- 第 9 关「翅膀只有一半」：根因是 CAST_MAP[9] = `hamazura / mugino / kakine`，第三只登场的是垣根帝督，其定稿层只有一片白翼；不是裁切、不是缺块
- 三处素材引用统一：`ART.chars.kakine` 对象键、`ART.expr.kakine` 对象键、后置覆盖赋值
- `.vn-actor.sub2` 宽 20% → 27%，双翼完整露出

## 保留
- v0.24 的 21 张定稿回归、原稿按钮 0、竖屏场景板 `display:block`、朗读默认关、四选项 4/4

## 验收
- 页内错误 0、破图 0、原稿按钮 0
- 第 9 关第三个角色层实测 437×430（新双翼层）
- 单文件 4.38 MB
