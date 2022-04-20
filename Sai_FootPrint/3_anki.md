##### 快捷键

1. 红色：`option+2`
2. 绿色：`option+3`
3. 挖空：`command+3`

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

            ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200522171342.png)

         2. 遮盖要记忆的部分

            ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200522180649.png)

            > 1. 选择矩形 - 遮挡
            > 2. 按住shift，选择矩形3，4，右键选择Group，则矩形3，4在卡片中同时出现同时消失
            > 3. Hide All, Guess One：学习矩形1时，矩形2，3，4都是遮挡状态（**常用**）
            > 4. Hide One, Guess One：学习矩形1时，矩形2，3，4都是显示状态

      2. `Quick Colour Changing`：修改文本颜色

         1. `Meta`对应`Control键`，`Ctrl`对应`Command键`，`Alt`对应`Option键`

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
      
         ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200522203746.png)

4. 设置卡片的学习/复习节奏

   1. 0/All：不学新卡片，复习所有到期卡片

   2. All/All：学习所有新卡片，复习所有到期卡片

      ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200522205145.png)

5. 填空题挖空

   1. 情况1：1道题挖2个空，分2张卡片展示，`Command+Shift+C`

   2. 情况2：1道题挖2个空，合成1张卡片展示，`Command+Shift+Option+C`

      > 1. BetterTouchTool修改组合快捷键（经常失效）
      >
      >    `control+3`：`Command+Shift+Option+C`
      >
      >    `control+4`：`Command+Shift+C`
   
6. 创建自己的卡片类型

   1. 问答题

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

   2. 填空题

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

   3. 阅读题

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

   ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200522214252.png)

   > 案例
   >
   > 1. 新建问答题类型
   >
   >    ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200522220207.png)
   >
   > 2. 增加字段并设置样式
   >
   >    ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200522221434.png)