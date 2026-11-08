# -*- coding: utf-8 -*-
from pathlib import Path
import base64,re
V='v0.38'
s=Path('哈士喵勇闯魔法禁书目录_v0.37.html').read_text(encoding='utf-8')
P=Path('build/art_v038')
def U(f):return 'data:image/webp;base64,'+base64.b64encode((P/f).read_bytes()).decode()
POSE={k:U(f'pose_{k}_v038.webp') for k in ['touma','alice','shangli','sakuyo']}
FX={k:U(f'fx_{k}_v038.webp') for k in ['coin','redsnow','arc','rune']}
R=[]
s=s.replace('<title>哈士喵勇闯魔法禁书目录 · v0.37</title>','<title>哈士喵勇闯魔法禁书目录 · '+V+'</title>',1)
s=s.replace('const DATA={"version":"v0.37"','const DATA={"version":"'+V+'"',1)
R.append('版本号 v0.37 → v0.38')

anchor='</script>\n</body>\n</html>'
assert anchor in s
code = r'''
/* ============ v0.38 · 大画布合页素材 + 18–23 关解锁 ============ */
/* ① 本轮先补的素材：2 张 1536×1536 大合页 → 8 个透明层（全部 85px 安全边） */
ART.pose38={
 touma:'__P_TOUMA__',alice:'__P_ALICE__',shangli:'__P_SHANGLI__',sakuyo:'__P_SAKUYO__'
};
ART.fx38={
 coin:'__F_COIN__',redsnow:'__F_REDSNOW__',arc:'__F_ARC__',rune:'__F_RUNE__'
};
/* 18–23 登场角色 → 本轮姿态差分（其余角色沿用已入库 ART.expr） */
var QPOSE38={
 18:{shangli:ART.pose38.shangli,sakuyo:ART.pose38.sakuyo},
 19:{touma:ART.pose38.touma},
 21:{touma:ART.pose38.touma},
 22:{alice:ART.pose38.alice,touma:ART.pose38.touma},
 23:{alice:ART.pose38.alice,touma:ART.pose38.touma}
};
var QFX38={18:'rune',19:'coin',20:'coin',21:'redsnow',22:'coin',23:'rune'};

/* ② 解锁 18–23 关（场景板 cheap/gold/redsnow 早已入库） */
PERF_READY.push(18,19,20,21,22,23);
EXPR_QUESTS.push(18,19,20,21,22,23);
Object.assign(QUEST_FRAME,{18:'half',19:'half',20:'full',21:'half',22:'half',23:'full'});
var _pn38=window.perfNeed;
window.perfNeed=function(id){var n=Number(id);return (n>=18&&n<=23)?[]:_pn38.apply(this,arguments)};

/* ③ 姿态差分在原 applyExpr 之后叠加（不动 1–17 关已有差分） */
function applyQPose38(){
 var st=document.querySelector('#vnStage');if(!st)return;
 var map=QPOSE38[curId()];if(!map)return;
 var ids=questCast(Q(state.active)||currentQuest());
 var els=[].slice.call(st.querySelectorAll('.vn-actor, .vn-char'));
 ids.forEach(function(id,i){
  var src=map[id],el=els[i];if(!src||!el)return;
  el.classList.add('expr-static');
  var imgs=el.querySelectorAll('img');
  if(imgs.length)imgs.forEach(function(im,k){im.src=src;if(k>0)im.style.display='none'});
  else if(el.tagName==='IMG')el.src=src;
  el.setAttribute('aria-label',(el.getAttribute('aria-label')||'').replace(/（v0\.38 姿态差分）/g,'')+'（v0.38 姿态差分）');
 });
}
var _ae38=window.applyExpr;
window.applyExpr=function(){var r=_ae38.apply(this,arguments);try{applyQPose38()}catch(e){}return r};

/* ④ 特效贴片层：环境层，在角色之后、暗角之前，不吃点击 */
(function(){
 var css=document.createElement('style');css.id='fx38css';
 css.textContent='.vn-fx-deco38{position:absolute;inset:0;width:100%;height:100%;object-fit:contain;'+
  'pointer-events:none;z-index:4;opacity:.38;filter:drop-shadow(0 4px 14px #0005);'+
  'transition:opacity .5s ease}.vn.peek-scene .vn-fx-deco38{opacity:.12}'+
  '.stage .vn-fx-deco38{opacity:.38}';
 (document.head||document.body).appendChild(css);
 window.syncFx38=function(){
  var st=document.querySelector('#vnStage');if(!st)return;
  var el=st.querySelector('.vn-fx-deco38');
  if(!el){el=document.createElement('img');el.className='vn-fx-deco38';el.alt='本关特效贴片';el.decoding='async';st.appendChild(el)}
  var k=QFX38[curId()],src=k&&ART.fx38[k];
  if(src){el.src=src;el.style.display=''}else el.style.display='none';
 };
 var _rq38=window.renderQuest,_vr38=window.vnRender;
 window.renderQuest=function(){var r=_rq38.apply(this,arguments);try{syncFx38()}catch(e){}return r};
 window.vnRender=function(){var r=_vr38.apply(this,arguments);try{syncFx38();applyQPose38()}catch(e){}return r};
 try{syncFx38()}catch(e){}
})();

/* ⑤ 关于页登记：画布诊断、两条生成路线、解锁 */
var ABOUT38=`<details class="card" id="v038Reg"><summary>🖼 v0.38 · 大画布合页 / 18–23 关解锁</summary>
<p class="muted">本轮第一件事仍是先补素材：<b>2 张 1536×1536 大合页 → 8 个透明层</b>，全部 85px 安全边、零触边、全部进网页。</p>
<div class="voice-grid">
 <div><b>「生成的还是有裁剪」查清了</b><span>上一张 4:5 单角色稿是 <b>1408×1664</b>，角色左右只剩 <b>27–40px（≈2%）</b>：严格说像素没触边，但视觉上就是快被切掉。根因是<b>画布相对角色太小</b>，不是羽化、不是载入裁切、不是 CSS。这轮换 1536² 大画布、每格 768²，角色只占格 10–12%，四边留白 <b>205–272px</b>，抠图后再统一 pad 到 85px 安全边。</span></div>
 <div><b>是图生图吗？两条都试了</b><span>上一张 4:5 单角色是图生图。这轮按「一次性生成多个角色」改回 2×2 大合页：<b>纯文生图合页</b>画风漂成平涂描边细长站立版（正是之前被否掉的那批）→ <b>否决留档</b>；<b>以定稿 4 层拼成的大合页做图生图</b>，保留全部服装道具与厚涂画风，只微调表情 → <b>采用</b>。所以用大画布合页＋图生图，既一次画 4 只，也不漂移。</span></div>
 <div><b>角色层仍是定稿唯一基准</b><span>21 张定稿一字未动；本轮 4 个是<b>姿态／表情差分</b>，按关卡查表叠加，不覆盖 1–17 关已有差分。上条校服绷带、爱丽丝卷发蓝白裙扑克、上里黑制服、去鸣银发破布锁链全部保留，没有脱衣、没有漏角色。</span></div>
 <div><b>4 个特效贴片</b><span>斜落金币 / 绯红雪花 / 淡青电弧 / 淡金魔法阵，独立透明层，作为环境层叠在角色之后、不吃点击。19–20、22 关金币雨，21 关红雪，18、23 关术式环；「🖼 看全场景」时自动淡出。</span></div>
 <div><b>18–23 关解锁</b><span>场景板 cheap / gold / redsnow 早已入库，6 个登场角色的表情差分也已覆盖，本轮补齐姿态差分与特效层后解锁，锁关 13 → <b>7</b>。第 24 关起继续「敬请期待」。</span></div>
</div>
<div class='v35-cards'>
 <figure><img class='gallery-img' src='__P_TOUMA__' alt='上条姿态差分'><figcaption>大合页抠出的姿态差分</figcaption></figure>
 <figure><img class='gallery-img' src='__P_ALICE__' alt='爱丽丝姿态差分'><figcaption>眨眼坏笑 · 服装道具保留</figcaption></figure>
 <figure><img class='gallery-img' src='__F_COIN__' alt='金币雨特效贴片'><figcaption>金币雨特效层</figcaption></figure>
 <figure><img class='gallery-img' src='__F_REDSNOW__' alt='红雪特效贴片'><figcaption>绯红雪花特效层</figcaption></figure>
</div>
<div><b>如实说</b><span>纯文生图那张 4 角色合页只在包内留档、不进网页，不补同款；特效贴片是原创装饰，不对应原作镜头。答案重排、🎤 录音 / 📁 导入、点击台词气泡、Pointer 拖动、fitBox、LAYOUT_RULES 全部保留。</span></div>
</details>`;
(function(){
 var _ra=window.renderAbout;
 window.renderAbout=function(){_ra.apply(this,arguments);var a=$('#about');if(a&&!a.querySelector('#v038Reg'))a.insertAdjacentHTML('beforeend',ABOUT38)};
 try{if($('#about'))renderAbout()}catch(e){}
})();
'''
for k,v in POSE.items():code=code.replace('__P_'+k.upper()+'__',v)
for k,v in FX.items():code=code.replace('__F_'+k.upper()+'__',v)
s=s.replace(anchor,code+'\n'+anchor,1)
R.append('末尾注入：4 姿态差分 + 4 特效层 + QPOSE38/QFX38 + 18–23 解锁 + 关于页登记')

for pat,label in [('function fitBox(cw,ch,iw,ih,mode)','fitBox'),
                 ('window.LAYOUT_RULES=LAYOUT_RULES','LAYOUT_RULES'),
                 ('window.HuskyVoice.record=function','录音接口'),
                 ('function tap36Bubble(stage,el,pick,ord)','点击台词气泡'),
                 ("c.addEventListener('pointerdown'","小游戏 Pointer"),
                 ('.vn .vn-bg,.vn-bg{object-fit:cover!important','竖屏 cover'),
                 ('const PERF_READY=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17]','17 关基准'),
                 ('DATA.quests.forEach(function(q)','答案确定性重排')]:
    assert pat in s,label+' 丢失'
R.append('既有能力断言通过：fitBox / LAYOUT_RULES / 录音 / 点击台词 / Pointer / cover / 17 关 / 答案重排')

out=Path(f'哈士喵勇闯魔法禁书目录_{V}.html');out.write_text(s,encoding='utf-8')
print('已应用',len(R),'项');[print('  ✓',x) for x in R]
print('大小',round(out.stat().st_size/1024/1024,2),'MB')
