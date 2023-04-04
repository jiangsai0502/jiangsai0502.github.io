#### 快捷键

1. 红色：`option+2`
2. 绿色：`option+3`
3. 挖空：`command+3`

#### 设置说明

##### Daily Limits 每日上限
New cards/day 9999 每天新卡的学习上限
Maximum reviews/day 9999 每天旧卡的复习上限

##### New Cards 新卡
Learning steps 1m 19m 选【重来】的间隔1m，【良好】20m
Graduating interval 1 选择【一般】的间隔1day
Easy interval 7 选择【简单】的间隔7day

##### Lapses 错误次数
Relearning steps 19m 选【重来】的间隔
Minimum interval 2
Leech threshold 4 连续错4天则将卡片执行Leech action
Leech action

#### 基础设置

1. 偏好设置

   1. 将`混合新卡片和复习`改为`在复习后显示新卡片`
   2. 下一天开始，改为`4`点

2. 工具 - 创建筛选的牌组

   1. 根据书名号创建想要复习的章节

3. 工具 - 添加组件

   1. 在线安装插件：获取插件 - 浏览插件

   2. 常用插件

      1. `Image Occlusion Enhanced`：图形填空插件

         1. 选择该卡片类型 - 他处截图 - 点击右侧图形icon

            ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220723212138.png)

         2. 遮盖要记忆的部分

            ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220723212224.png)

            > 1. 选择矩形 - 遮挡
            > 2. 按住shift，选择矩形3，4，右键选择Group，则矩形3，4在卡片中同时出现同时消失
            > 3. Hide All, Guess One：学习矩形1时，矩形2，3，4都是遮挡状态（**常用**）
            > 4. Hide One, Guess One：学习矩形1时，矩形2，3，4都是显示状态

      2. `Quick Colour Changing`：修改文本颜色

         1. `Meta`对应`Control键`，`Ctrl`对应`Command键`，`Alt`对应`fn + Option键`

            修改后，保存，退出App
            
            ```bash
            "keys": [
                [ "#FF0000", "Meta+1" ],
                [ "#008080", "Meta+2" ],
            ]
            "keys": [
             [ "#FF0000", "Alt+1" ],
                [ "#008080", "Alt+2" ],
            ]
            "keys": [
                [ "#FF0000", "Ctrl+1" ],
                [ "#008080", "Ctrl+2" ],
            ]
            ```
      
      3. `Mini Format Pack`：增加格式选项
      
         ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220723212300.png)

4. 设置卡片的学习/复习节奏

   1. 0/All：不学新卡片，复习所有到期卡片

   2. All/All：学习所有新卡片，复习所有到期卡片

      ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220723212327.png)

5. 填空题挖空

   1. 情况1：1道题挖2个空，分2张卡片展示，`Command+Shift+C`

   2. 情况2：1道题挖2个空，合成1张卡片展示，`Command+Shift+Option+C`

      > 1. BetterTouchTool修改组合快捷键（经常失效）
      >
      >    `control+3`：`Command+Shift+Option+C`
      >
      >    `control+4`：`Command+Shift+C`
   
6. 创建自己的卡片类型

   1. 新建字段：Fields，新建一个书名号字段《》并将至设置为输入时固定不变
      ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202303031404194.png)
   
   2. 问答题
   
      正面模板
   
      ```bash
      {{问题}} <br>
      <div style='font-family: Arial; font-size: 12px;float:left;color:#D3D3D3'>《{{《》}}》</div>
      ```
   
      格式
   
      ```css
      .card {
       font-family: arial;
       font-size: 20px;
       text-align: left;
       color: black;
       background-color: white;
      }
      
      .kbd {
          box-shadow: inset 0px 1px 0px 0px #ffffff;
          background: -webkit-gradient(linear, left top, left bottom, color-stop(0.05, #f9f9f9)stop(1, #e9e9e9) );
          background-color: #f9f9f9;
          border-radius: 5px;
          border: 1px solid #dcdcdc;
          display: inline-block;
          font-size: 0.8em;
          height: 30px;
          line-height: 30px;
          padding: 0px 10px;
          text-align: center;
          text-shadow: 1px 1px 0px #ffffff;
      }
      ```
   
      背面模板
   
      ```bash
      {{FrontSide}}<br>
      <hr id=answer>
      
      {{答案}}<br>
      <br>
      <div style='font-family: Arial; font-size: 18px;'><div style="float:left"> {{hint:编码}}</div></div><br>
      <div style='font-family: Arial; font-size: 18px;float:left'>{{hint:例子}}</div>
      <br>
      <div style='font-family: Arial; font-size: 18px;'>{{hint:拓展}}</div><br>
      ```
   
   3. 填空题
   
      正面模板
   
      ```bash
      {{cloze:文字}}<br>
      <div style='font-family: Arial; font-size: 12px;float:left;color:	#D3D3D3'>《{{《》}}》</div>
      ```
   
      格式
   
      ```css
      .card {
       font-family: arial;
       font-size: 20px;
       text-align: left;
       color: black;
       background-color: white;
      }
      
      .cloze {
       font-weight: bold;
       color: red;
      }
      ```
   
      背面模板
   
      ```html
      {{cloze:文字}}<br>
      <div style='font-family: Arial; font-size: 12px;float:left;color:	#D3D3D3'>《{{《》}}》</div>
      <br>
      <br>
      <div style='font-family: Arial; font-size: 18px;'><div style="float:left"> {{hint:编码}}</div></div><br>
      <div style='font-family: Arial; font-size: 18px;float:left'>{{hint:例子}}</div><br>
      <div style='font-family: Arial; font-size: 18px;'>{{hint:拓展}}</div><br>
      ```
   
   4. 阅读题
   
      正面模板
   
      ```html
      {{Text}}
       <br>
      <div style='font-family: Arial; font-size: 12px;float:left;color:	#D3D3D3'>《{{《》}}》</div>
      ```
   
      格式
   
      ```css
      .card {
       font-family: arial;
       font-size: 20px;
       text-align: left;
       color: black;
       background-color: white;
      }
      ```
   
      背面模板
   
      ```html
      啥时候想再瞟一眼
      ```
   
   ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220723212407.png)
   
   > 案例
   >
   > 1. 新建问答题类型
   >
   >    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220723212455.png)
   >
   > 2. 增加字段并设置样式
   >
   >    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220723212526.png)

* 三合一模板

  > 1. 用法
  >
  >    * 标题：题目
  >    * 正面：加粗部分会在做填空题时隐藏，点击每个隐藏部分则逐个展示
  >    * 反面：完全copy正面即可
  >    * 挖空率：
  >
  > 2. 删除一下没用的部分Notes、MNMindMap、MNLink（card - Back template）
  >
  >    ```
  >    <div id=addnote style=display:none>
  >    
  >    {{#Notes}}
  >    <p><div class="notes">
  >    <div style="margin:5px 5px -3px 12px;font-weight:bold;font-size:0.92em;letter-spacing:0.02em">Notes :</div>
  >    <div id=note class="notes-txt" style="font-family:kt">{{Notes}}</div></div>
  >    {{/Notes}}
  >    
  >     {{#MNMindMap}}
  >    <p><div class="section">
  >    <div style="margin:5px 5px 8px; font-size:0.75em">{{MNMindMap}}</div></div>
  >    {{/MNMindMap}}
  >    
  >    </div>
  >    
  >    {{#MNLink}}
  >    <p><div style="text-align:center;max-width:828px;margin:0 auto;font-size:1.23em">{{MNLink}}</div>
  >    {{/MNLink}}
  >    
  >    <p><br>
  >    ```
  >
  > 3. 修改默认板块（card - Front template）
  >
  >    1. 改为默认显示填空板块
  >       1. 找到`<div id="div0" style="display:none">`
  >       2. 改为`<div id="div0" style="display:block">`
  >    2. 改为默认显示随机板块
  >       1. 找到`<div id="question" class=section style=display:none></div>`
  >       2. 改为`<div id="question" class=section style=display:block></div>`
  >    3. 修改挖空率（card - Front template）
  >       1. 找到rate = 80，改为目标数字
  >    4. 