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
         
      4. Customize Keyboard Shortcuts：自定义anki的快捷方式

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

  > 1. Fields 删改
  >
  >    1. 标题：改为《问题》
  >    2. 正面：改为《原文/填空》
  >    3. 挖空率：不变
  >    4. 反面、笔记、Remarks、MNLink、MNMindMap：删除
  >
  > 2. 删除没用的
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
  > 3. Card - Back template 删除一下没用的部分Notes、audio
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
  > 4. Card - Front template 修改默认板块
  >
  >    1. 改为默认显示填空板块
  >       1. 找到`<div id="div0" style="display:none">`
  >       2. 改为`<div id="div0" style="display:block">`
  >    2. 改为默认显示随机板块
  >       1. 找到`<div id="question" class=section style=display:none></div>`
  >       2. 改为`<div id="question" class=section style=display:block></div>`
  >    3. 修改挖空率（card - Front template）
  >       1. 找到rate = 80，改为目标数字
  >
  > 5. 修改卡片按钮名称
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
  > 6. 录入
  >
  >    * 问题栏：卡片的问题
  >    * 原文/填空栏：做题时点**填空**按钮，填空栏里的加粗文字会隐藏，点击每个隐藏部分则逐个展示；点
  >    * 挖空率：不填则默认挖空率80%，做题时点**随机**按钮，按照挖空率对填空栏的内容进行80%的隐藏