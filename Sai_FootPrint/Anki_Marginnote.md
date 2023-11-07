#### 快捷键

> 1. 红色：`option+2`
> 2. 绿色：`option+3`
> 3. 挖空：`command+3`

#### 设置

> **软件设置**
>
> > 1. 新的一天始于 `4` 时
> > 2. `混合新卡片和复习卡` 改为 `先复习，后学新`
>
> **牌组设置**
>
> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311030956501.png)
>
> > * Daily Limits 每日上限
> >
> >   > New cards/day 9999 每天新卡的学习上限
> >   > Maximum reviews/day 9999 每天旧卡的复习上限
> >
> > * New Cards 新卡
> >
> >   > Learning steps 1m 19m 选【重来】的间隔1m，【良好】20m
> >   > Graduating interval 1 选择【一般】的间隔1day
> >   > Easy interval 7 选择【简单】的间隔7day
> >
> > * Lapses 错误次数
> >
> >   > Relearning steps 19m 选【重来】的间隔
> >   > Minimum interval 2
> >   > Leech threshold 4 连续错4天则将卡片执行Leech action
> >   > Leech action
>
> **插件**
>
> > 工具 - 插件 - 获取插件 - 插件官网
> >
> > 1. `Image Occlusion Enhanced`：图形填空插件
> >
> >    > 1. 选择该卡片类型 - 他处截图 - 点击右侧图形icon
> >    >
> >    >    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220723212138.png)
> >    >
> >    > 2. 遮盖要记忆的部分
> >    >
> >    >    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220723212224.png)
> >    >
> >    >    > 1. 选择矩形 - 遮挡
> >    >    > 2. 按住shift，选择矩形3，4，右键选择Group，则矩形3，4在卡片中同时出现同时消失
> >    >    > 3. Hide All, Guess One：学习矩形1时，矩形2，3，4都是遮挡状态（**常用**）
> >    >    > 4. Hide One, Guess One：学习矩形1时，矩形2，3，4都是显示状态
> >
> > 2. `Quick Colour Changing`：修改文本颜色
> >
> >    > `Meta`对应`Control键`，`Ctrl`对应`Command键`，`Alt`对应`fn + Option键`
> >    >
> >    > ```bash
> >    > "keys": [
> >    >     [ "#FF0000", "Meta+1" ],
> >    >     [ "#008080", "Meta+2" ],
> >    > ]
> >    > "keys": [
> >    >  [ "#FF0000", "Alt+1" ],
> >    >     [ "#008080", "Alt+2" ],
> >    > ]
> >    > "keys": [
> >    >     [ "#FF0000", "Ctrl+1" ],
> >    >     [ "#008080", "Ctrl+2" ],
> >    > ]
> >    > ```
> >
> > 3. `Mini Format Pack`：增加格式选项
> >
> >    >![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220723212300.png)
> >
> > 4. `Customize Keyboard Shortcuts`：自定义anki的快捷键
> >
> > 5. `Auto Sync`：自动同步

#### 自制模版

> * 自制带书名号的问答题模板
>
>   >1. 添加个新的系统模板「添加：问答题」，然后修改此模版
>   >
>   >   ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311031120189.png)
>   >
>   >2. 新建字段
>   >
>   >   ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311031030197.png)
>   >
>   >   > Step2设置为输入时固定不变，方便录入
>   >
>   >3. 设置卡片格式
>   >
>   >   ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311031057282.png)
>   >
>   >   > 正面内容模版
>   >   >
>   >   > ```css
>   >   > {{Front}}
>   >   > <br><br>
>   >   > <div style='font-family: Arial; font-size: 12px;float:left;color:#D3D3D3'>《{{《》}}》
>   >   > </div>
>   >   > ```
>   >
>   >   > 背面内容模版
>   >   >
>   >   > ```css
>   >   > {{FrontSide}}
>   >   > <br>
>   >   > <hr>
>   >   > {{Back}}
>   >   > ```
>   >
>   >   > 样式
>   >   >
>   >   > ```css
>   >   > .card {
>   >   >  font-family: arial;
>   >   >  font-size: 20px;
>   >   >  text-align: left;
>   >   >  color: black;
>   >   >  background-color: white;
>   >   > }
>   >   > 
>   >   > .kbd {
>   >   >     box-shadow: inset 0px 1px 0px 0px #ffffff;
>   >   >     background: -webkit-gradient(linear, left top, left bottom, color-stop(0.05, #f9f9f9)stop(1, #e9e9e9) );
>   >   >     background-color: #f9f9f9;
>   >   >     border-radius: 5px;
>   >   >     border: 1px solid #dcdcdc;
>   >   >     display: inline-block;
>   >   >     font-size: 0.8em;
>   >   >     height: 30px;
>   >   >     line-height: 30px;
>   >   >     padding: 0px 10px;
>   >   >     text-align: center;
>   >   >     text-shadow: 1px 1px 0px #ffffff;
>   >   > }
>   >   > ```
>
> * 自制带书名号的填空题模版（操作步骤见「自制带书名号的问答题模板」）
>
>   1. 添加个新的系统模板「添加：填空题」，然后修改此模版
>
>   2. 新建字段
>
>      ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311031111954.png)
>
>      > * 字段名称`Front`改为`Question`
>      > * 新建书名号字段，其他字段删除
>
>   3. 设置卡片格式
>
>      >正面内容模版
>      >
>      >```css
>      >{{cloze:Question}}
>      ><br>
>      ><div style='font-family: Arial; font-size: 12px;float:left;color:	#D3D3D3'>《{{《》}}》
>      ></div>
>      >```
>
>      > 背面内容模版
>      >
>      > ```css
>      > {{cloze:Question}}
>      > <br>
>      > <div style='font-family: Arial; font-size: 12px;float:left;color:	#D3D3D3'>《{{《》}}》
>      > </div>
>      > ```
>
>      > 样式
>      >
>      > ```css
>      > .card {
>      >  font-family: arial;
>      >  font-size: 20px;
>      >  text-align: left;
>      >  color: black;
>      >  background-color: white;
>      > }
>      > 
>      > .cloze {
>      >  font-weight: bold;
>      >  color: red;
>      > }
>      > ```
>
> * 自制带书名号的浏览题模板（操作步骤见「自制带书名号的问答题模板」）
>
>   1. 添加个新的系统模板「添加：问答题」，然后修改此模版
>
>   2. 新建字段
>
>      ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311031132769.png)
>
>      > * 字段名称`Front`改为`Text`
>      > * 新建书名号字段，其他字段删除
>
>   3. 设置卡片格式
>
>      > 正面内容模版
>      >
>      > ```
>      > {{Text}}
>      > <br>
>      > <br>
>      > <div style='font-family: Arial; font-size: 12px;float:left;color:	#D3D3D3'>《{{《》}}》
>      > </div>
>      > ```
>
>      > 背面内容模版
>      >
>      > ```
>      > {{FrontSide}}
>      > ```
>
>      > 样式
>      >
>      > ```css
>      > .card {
>      >  font-family: arial;
>      >  font-size: 20px;
>      >  text-align: left;
>      >  color: black;
>      >  background-color: white;
>      > }
>      > ```

#### 小技巧

> * [长时间没复习，面对海量的review怎么办](https://zhuanlan.zhihu.com/p/442081874?utm_id=0)
>
>   >![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311031009864.png)
>   >
>   >创建一个最近12天内到期的卡片牌组：`deck:整合记忆 is:due prop:due>-12`
>   >
>   >> 这个「逐步蚕食」牌组会从「整合记忆」牌组中抽出符合条件的卡，剩下的都是12后到期的卡
>
> * 只想复习特点主题的卡片怎么办
>
>   > 根据书名号创建想要复习的章节
>
> * 调节每日学习/复习节奏
>
>   >1. 0/All：不学新卡片，复习所有到期卡片
>   >
>   >2. All/All：学习所有新卡片，复习所有到期卡片
>   >
>   >   ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220723212327.png)
>
> * 填空题挖空
>
>   > 1. 1道题挖2个空，分2张卡片展示，`Command+Shift+C`
>   >
>   > 2. 1道题挖2个空，合成1张卡片展示，`Command+Shift+Option+C`

#### Anki+快捷指令

> * ##### anki随手记
>
>   > 链接：https://www.icloud.com/shortcuts/ab54c4a723de4698ad3432aa4bf63262
>   >
>   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311021619753.png)
>   >
>   > 1. 安装快捷指令：复制到该平台的safari
>   >
>   > 2. 账户重命名
>   >
>   >    > * Mac、iPad、iPhone三个平台的账户名好像是不互通的，使用哪个平台的快捷指令就改哪个平台的账户名
>   >    >
>   >    >   > 1. 新建一个临时账户「Will」
>   >    >   > 2. 切换到临时账户「Will」
>   >    >   > 3. 左滑原账户重命名为「Sai」
>   >    >   > 4. 切换到原账户「Sai」
>   >    >   > 5. 删除临时账户
>   >
>   > 3. 链接修改注意事项
>   >
>   >    > ①Sai、②Basic、③整合记忆::摘录、④Front前后没有空格，尤其是④，fld跟Front之间没有空格
>   >    >
>   >    > 任何一个空格都会报错，有报错首先检查是否有空行
>   >    >
>   >    > > 案例
>   >    > >
>   >    > > 1. `Sai` 前/后有空格，提示「Error requested profile not active」
>   >    > > 2. `Basic` 前/后有空格，提示「数据库存在不一致问题，请使用“检查数据库”操作」
>   >    > > 3. `整合记忆::摘录` 前/后有空格，可以正常工作
>   >    > > 4. `Front` 前/后有空格，提示「Error field Front does not exist」
>
> * ##### anki复制摘录
>
>   > 链接：https://www.icloud.com/shortcuts/e396d4755b3b443c824efbf25eeaeda2
>
> * ##### anki滑词翻译
>
>   > 链接：https://shimo.im/docs/X3gyCqd9rrTYKtxJ/read

#### Marginnote读书方式

> [主参考](https://www.bilibili.com/video/BV1NE411u7jZ)，[参考]()
>
> 1. 文档区功能
>
>    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311050058814.png)
>
> 2. 脑图区功能
>
>    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311050059054.png)

> **快速略读：第1遍**
>
> > 文档模式：随手勾画、涂鸦，如下图
> >
> > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311050106038.png)
>
> **通读：第2遍**
>
> > 学习模式：导图目录 + 摘录卡片，如下图
> >
> > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311042314698.png)
> >
> > > 制作**浏览题**、**简答题**、**填空题**
>
> 1. 切入学习模式
>
>    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311042113680.png)
>
> 2. 制作单面卡片**「浏览题」**
>
>    1. 手型工具
>
>       > 1. 文字选择：`学习模式 - 文档区` ①长按选中文字 -> ②长按已选中的文字，拖到`脑图区`，自动生成卡片
>       >
>       >    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311042054166.png)
>       >
>       > 2. 区域选择：`学习模式 - 文档区` ①长按框选区域 -> ②长按已选中的区域，拖到`脑图区`，自动生成卡片
>       >
>       >    > 若未提前开启`设置 - 自动转换矩形/ 多边形摘录为文字`，则卡片为图片卡片
>       >    >
>       >    > 若提前开启，则卡片自动OCR成文字
>       >
>       >    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311061556465.png)
>       >
>       >    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311050011283.png)
>
>    2. 文字选择工具
>
>       > * 文字选择：`学习模式 - 文档区` 提前开启①`设置 - 自动添加到脑图` -> ②滑动选中文字，`脑图区` 自动生成卡片
>       >
>       >   ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311061546876.png)
>       
>    3. 矩形框选工具（同手型工具）
>
>       > * 区域选择：`学习模式 - 文档区`提前开启`设置 - 自动添加到脑图`  -> ①框选区域，`脑图区` 自动生成卡片
>       >
>       >   > 若未提前开启`设置 - 自动转换矩形/ 多边形摘录为文字`，则卡片为图片卡片
>       >   >
>       >   > 若提前开启，则卡片自动OCR成文字
>       
>    4. 自由框选工具
>
>       > * 区域选择：`学习模式 - 文档区`提前开启`设置 - 自动添加到脑图`  -> ①框选区域，`脑图区` 自动生成卡片
>       >
>       >   > 若未提前开启`设置 - 自动转换矩形/ 多边形摘录为文字`，则卡片为图片卡片
>       >   >
>       >   > 若提前开启，则卡片自动OCR成文字
>       >
>       > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311042059629.png)
>
> 3. 制作双面卡片**「问答题」**
>
>    1. 为已存在的单面卡片「添加评论」「添加标题」
>
>       > > **手型工具模式**下 -> ①`文档区`，选中要处理卡片 -> ②pencil长按，滑动选择文字，选完后弹窗选择将所选文字设为标题即卡片正面，或评论即卡片背面
>       >
>       > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311042155045.png)
>
>    2. 将2个单面卡片合并成1个双面卡片
>
>       > > ①`脑图区`，选中要设为评论的卡片 -> ②拖到要设为标题的卡片身上 -> ③ 成为其子节点后，再次将子节点卡片拖到父节点卡片身上，随即2张卡片合成1个
>       >
>       > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311042231549.png)
>
> 4. 制作**「填空题」**
>
>    1. 荧光笔涂鸦
>
>       1. 非卡片涂鸦
>
>          >1. 涂鸦：`文档区` 任意位置「荧光笔涂鸦」①
>          >2. 文档区复习：`文档区` 打开设置「回忆模式②」
>          >
>          >![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311050124471.png)
>
>       2. 卡片涂鸦
>
>          > 1. 涂鸦：`文档区` 在单面卡片上用「荧光笔涂鸦②」
>          > 2. Anki复习：筛选出「目标颜色卡片③」导入「目标卡片组⑦」，勾选「遮挡文档上的荧光笔⑨」，勾选「导出到 MarginNote 的链接⑪」，Anki沉浸式复习
>          >
>          > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311061136985.png)
>
>    2. 文字挖空
>
>       1. 挖空方式
>
>          > 1. 文档区挖空：`学习模式 -> 文档区`打开设置「划重点①」
>          >    1. `手型工具`挖空：在一个「单面卡片」上，长按划动选择「挖空文字」
>          >    2. `文字选择`挖空：在一个「单面卡片」上，划动选择「挖空文字」
>          > 2. 卡片组挖空：`复习模式`点击填空，在卡片上，划动选择「挖空文字」
>
>       2. 复习方式
>
>          > 1. 文档区复习：`学习模式 -> 文档区`打开设置「回忆模式②」，`文档区` 边阅读边复习
>          > 2. Anki复习
>
>       ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311061417711.png)
>
> 5. 脑图效果
>
>    > > 章节设为灰色；知识点设为绿色
>    >
>    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311042314698.png)
>
> 6. 导入卡片组
>
>    > > 排除章节卡片，筛选出知识点卡片，导入到卡片组
>    >
>    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311042338989.png)
>
> 7. 导入Anki
>
>    > > 导出时勾选「导出到 MarginNote 的链接」，Anki中点击卡片链接自动跳转到卡片在文档中的位置
>    > >
>    > > > 技巧：iPad记忆时，开分屏，左MarginNote右Anki
>    >
>    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311052148508.png)
>
> **MarginNote导出的卡片改为自制卡片模版**
>
> > 
>
> **双面卡制作技巧**
>
> 1. 问题与答案在同一文件，但相距较远
>
>    >![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311060016950.png)
>
> 2. 问题与答案在不同文件
>
>    >![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311060046340.png)
>
> **英文原著阅读**
>
> 1. MarginNote + Eudic
>
>    > 1. Eudic：`账号` - `设置` - 开启`查词后加入生词本`
>    > 2. MarginNote：`•••` - `插件` - 开启`Search in Eudic+`
>    > 3. 分屏开启Eudic、MarginNote，`手形工具`/`文字工具`下选中某个单词（只能是单词不能是句子）
>
>    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311061828564.png)
>
> 2. MarginNote + OhmyMN
>
>    > 1. OhmyMN数据库安装
>    >
>    >    > [链接](https://pan.baidu.com/s/1iw2cahlRI9WX4MbKgU-RXw?pwd=gwmg)  提取码: gwmg
>    >    >
>    >    > AirDrop到iPad，使用MarginNote打开即完成安装
>    >
>    > 2. 

> * 制作选择题
>   * https://www.bilibili.com/video/BV1yW41117PU
> * 制作填空题
>   * https://www.bilibili.com/video/BV1h7411v7ou
>   * https://www.bilibili.com/video/BV1JK411P7VA
> * 制作问答题
>   * https://www.bilibili.com/video/BV1NE411u7jZ
> * 背单词
>   * https://www.bilibili.com/video/BV1jL4y1471g
> * MN教程
>   * https://www.bilibili.com/video/BV1qB4y1b7R9
> * 看漫画背单词
>   * https://www.bilibili.com/video/BV1fb411m77g
> * 跑步背单词
>   * https://www.bilibili.com/video/BV1TE41157qH

-----

### 高级教程

* 三合一模板

  > 1. Fields 删改
  >
  >    1. 标题：改为《问题》，并设置为Sort by this field
  >    2. 正面：改为《原文/填空》
  >    3. 《》：新增书名号
  >    4. 挖空率：不变
  >    5. 反面、笔记、Remarks、MNLink、MNMindMap：删除
  >
  > 2. 新增书名号部分
  >
  >    1. Card - Front template中`<div style="text-align:center">`前增加
  >
  >       ```
  >       <br>
  >       <div style='font-family: Arial; font-size: 12px;float:left;color:#D3D3D3'>《{{《》}}》</div><br>
  >       ```
  >
  >    2. Card - Back template中`<div style="text-align:center">`前增加
  >
  >       ```
  >       <br>
  >       <div style='font-family: Arial; font-size: 12px;float:left;color:#D3D3D3'>《{{《》}}》</div><br>
  >       ```
  >
  > 3. 修改卡片按钮名称
  >
  >    1. Card - Back template
  >
  >       ```
  >       <button class="button1" onclick="text()" style=margin-right:6px>摘 录</button>
  >       ```
  >
  >       “摘 录”改为“原 文”
  >
  >    2. Card - Front template
  >
  >       ```
  >       <button class="button4" onclick="addnote()" style=margin-right:6px>笔 记</button>
  >       ```
  >
  >       “笔 记”改为“原 文”
  >
  > 4. Card - Front template删除没用的部分
  >
  >    ```
  >    <div class=bg><div class=bg2>
  >       
  >    <div style="margin:-5px 0 0 0"></div>
  >    <div style="text-align:right;font-size:0.75em;max-width:828px;margin:0 auto;color:#808080">➵ {{Subdeck}}</div>
  >    ```
  >
  >    ```
  >    <div class="footer">
  >    <ul style=float:left;left:0>
  >    <li><a href="javascript:void(0)" onselectstart="return false;" onclick="prevv()">← Prev</a></li></ul>
  >    <ul style=float:right;right:0>
  >    <li><a href= "javascript:void(0)" class="active" onselectstart="return false;" onclick="nextt()">Next →</a></li></ul>
  >    </div>
  >    ```
  >
  >    ```
  >    function prevv()
  >    {
  >    	for (var i = sum -1; i >0; i = i - 2)
  >    	{
  >    		var n = i;
  >    		idd = "keyy" + String(n);
  >       
  >    		if (document.getElementById(idd).getAttribute("class") == "cloze")
  >    		{
  >    			idd = "keyy" + String(n);
  >    			$("#" + idd)[0];
  >    			switchh(idd);
  >    			break;
  >    		}
  >    	}
  >    }
  >       
  >    function nextt()
  >    {
  >    	for (var i = 2; i < sum; i = i + 2)
  >    	{
  >    		var n = i;
  >    		idd = "keyy" + String(n);
  >       
  >    		if (document.getElementById(idd).getAttribute("class") == "hidden")
  >    		{
  >       
  >    			idd = "keyy" + String(n - 1);
  >    			$("#" + idd)[0];
  >    			switchh(idd);
  >    			break;
  >    		}
  >    	}
  >    }
  >    ```
  >
  > 
  >
  > 5. Card - Back template 删除一下没用的部分
  >
  >    ```
  >    <div class=bg><div class=bg2>
  >    
  >    <div style="margin:-5px 0 0 0"></div>
  >    <div style="text-align:right;font-size:0.75em;max-width:828px;margin:0 auto;color:#808080">➵ {{Subdeck}}</div>
  >    ```
  >
  >    ```
  >    <div style="margin:16px 0 0 0"></div>
  >    <div id="div2" style="display:block">
  >    <div id="blank" class="section2">
  >    <div class="mbooks-highlight-txt"></div></div></div>
  >    ```
  >
  >    ```
  >    <div style="margin:16px 0 0 0"></div>
  >    <div id=question class=section3 style=display:none;>
  >    <div id=div3 class="mbooks-highlight-txt"></div></div>
  >    
  >    <div style="margin:16px 0 0 0"></div>
  >    <div id=question class=section3 style=display:none;>
  >    <div id=div3 class="mbooks-highlight-txt">{{原文/填空}}</div></div>
  >    ```
  >
  >    ```
  >    <div style="margin:16px 0 0 0"></div>
  >    <div class="notes">
  >    <div style="margin:10px 5px 10px 12px;font-weight:bold;font-size:0.92em;letter-spacing:0.02em">Notes :</div>
  >    <div id=note class="notes-txt" style="font-family:kt"></div></div>
  >    
  >    <div style="margin:16px 0 0 0"></div>
  >    <div class="notes">
  >    <div style="margin:10px 12px 5px; font-size:0.75em;text-align:left"></div></div>
  >    ```
  >
  >    ```
  >    <audio id=player src=""></audio>
  >    <button class="btn3" onclick="playAudio()">播放</button>
  >    <button class="btn4" onclick="pauseAudio()">暂停</button>
  >    <script type="text/javascript">
  >    document.querySelector("audio").setAttribute('src', 'https://fanyi.baidu.com/gettts?lan=zh&text=' + "{{text:原文/填空}}".replace(/\{\{c1\:\:/g,"").replace(/\}\}/g,"") + '&spd=6');
  >    function playAudio() {player.play()};
  >    function pauseAudio() {player.pause()};
  >    </script>
  >    ```
  >
  > 6. Card - Front template 修改默认板块
  >
  >    1. 修改卡片一上来就展示填空板块
  >       1. 找到`<div id="div2" style="display:none">`
  >       2. 改为`<div id="div2" style="display:block">`
  >
  > 7. 挖空方式修改挖空率（Card - Front template）
  >
  >    1. 找到rate = 80，改为目标数字
  >
  > 8. 录入
  >
  >    * 问题栏：卡片的问题
  >    * 原文/填空栏：做题时点**填空**按钮，填空栏里的加粗文字会隐藏，点击每个隐藏部分则逐个展示；点
  >    * 挖空率：不填则默认挖空率80%，做题时点**随机**按钮，按照挖空率对填空栏的内容进行80%的隐藏。2种挖空方式
  >
  > 9. 2种挖空方式
  >
  >    1. 固定挖空率：卡片录入时，输入60，即可指定挖空60%的内容
  >
  >    2. 固定挖空位置：卡片录入时，输入7/5/6/7，即以7个字为一组，挖空第5、6、7个字，适合背诗（标点不算字数）
  >
  >       * 如“朝辞白帝彩云间，千里江陵一日还”，会被挖成“朝辞白帝 _ _ _，千里江陵 _ _ _”
  >
  >    3. 指定为一格一挖孔，模拟《背了个X》：
  >
  >       1. Card - Front template找到如下代码
  >
  >          ```
  >          {{^挖空率}}
  >          <script type="text/javascript">
  >              var isFix = false;
  >              var rate = 80;
  >          </script>
  >          {{/挖空率}}
  >          ```
  >
  >          改为
  >
  >          ```
  >          {{^挖空率}}
  >          <script type="text/javascript">
  >              var isFix = true;
  >              var src = "2/1";
  >              var arr_num =[];
  >              src.split(/[/,;-]/).map(function(ele) {
  >                  var num = parseInt(ele);
  >                  if (!isNaN(num)) {
  >                      arr_num.push(num);
  >                  }
  >              });
  >          </script>
  >          {{/挖空率}}
  >          ```
  >
  >          其中 “ var src = "2/1"; ”，是指以2个字为一组，挖空第1个字，也可以替换为别的，如 “ var src = "5/2/4"; ”，是指以5个字为一组，挖空第2、4个字
  >
  >       2. 卡片录入的挖空率栏要清空
  >
  >    4. 英文“一个字母一个挖空”改为“一个单词一个挖空”
  >
  >       ```
  >       element.innerHTML = Array(element.innerHTML.length + 1).join(char_mask);
  >       ```
  >
  >       改为
  >
  >       ```
  >       element.innerHTML = char_mask;
  >       ```
