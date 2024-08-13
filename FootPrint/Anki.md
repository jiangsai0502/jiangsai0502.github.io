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
>   > 4. 设置模版代码，见[Anki卡片模版样式代码](Storage/Anki_template.md)
>
> * 自制带书名号的填空题模版（操作步骤见「自制带书名号的问答题模板」）
>
>   >1. 添加个新的系统模板「添加：填空题」，然后修改此模版
> >
>   >2. 新建字段
> >
>   >   ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311031111954.png)
> >
>   >   > * 字段名称`Front`改为`Question`
>   >   > * 新建书名号字段，其他字段删除
> >
>   >3. 设置模版代码，见[Anki卡片模版样式代码](Storage/Anki_template.md)
>
> * 自制带书名号的浏览题模板（操作步骤见「自制带书名号的问答题模板」）
>
>   >1. 添加个新的系统模板「添加：问答题」，然后修改此模版
>   >
>   >2. 新建字段
>   >
>   >   ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311031132769.png)
>   >
>   >   > * 字段名称`Front`改为`Text`
>   >   > * 新建书名号字段，其他字段删除
>   >
>   >3. 设置模版代码，见[Anki卡片模版样式代码](Storage/Anki_template.md)
>   
> * 自制图片阅读卡片
>
>   > 1. 使用Basic模板，进入「卡片」属性，修改「样式」
>   >
>   >    ```js
>   >    /* 设置图片自动适应设备宽度，且保持比例 */
>   >    img {
>   >        width: 100%; /* 图片宽度为设备宽度 */
>   >        height: auto; /* 保持图片比例 */
>   >        max-width: 100%; /* 防止图片超出容器 */
>   >        display: block;
>   >        margin: 0 auto; /* 图片居中 */
>   >        object-fit: contain; /* 保持内容不变形，适应容器 */
>   >    }
>   >    ```
>   >
>   >    ![image-20240813181638325](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202408131816853.png)

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

-----

### 高级教程

* 高级自制：阅读/填空题（加粗挖空）

  > 效果
  >
  > 1. 阅读题：正反面一样；2个换行之间自动增加MarkDown分割线
  > 2. 填空题
  >    1. 正面，加粗部分被挖空，点击挖空部分显示文字
  >    2. 背面，显示完整信息
  >    3. 2个换行之间自动增加MarkDown分割线
  >
  > 设置
  >
  > 1. 新建一个**问答题**模版，取名`Sai阅读/填空`
  >    1. 字段1：名称`阅读/填空正文`，本字段既是正面又是背面
  >    2. 字段2：名称`《》`，为书名号/MN位置链接
  > 2. 设置模版代码，见[Anki卡片模版样式代码](Storage/Anki_template.md)

* 高级自制：问答题

  > 效果
  >
  > 1. 正面，问题加粗
  > 2. 背面，显示完整信息；2个换行之间自动增加MarkDown分割线
  >
  > 设置
  >
  > 1. 新建一个**问答题**模版，取名`Sai问答`
  >    1. 字段1：名称`问题`，为正面
  >    2. 字段2：名称`答案`，为背面
  >    3. 字段3：名称`《》`，为书名号/MN位置链接
  > 2. 设置模版代码，见[Anki卡片模版样式代码](Storage/Anki_template.md)
