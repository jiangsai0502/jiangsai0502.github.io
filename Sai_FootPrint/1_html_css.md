

> 网页三大件：Html是结构，Css是外观，Js是动作
>
> ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200430201456.png)



### HTML

1. vscode自动生成标准html代码（文件后缀html）

   > 1. 自动生成头文件：输入`!`，按下`Tab`
   > 2. 自动补齐
   >    1. 输入`a`，按下`Tab`
   >    2. 输入`img`，按下`Tab`
   >    3. 输入`input`，按下`Tab`
   >    4. 输入`div`，按下`Tab`

2. 常用标签

   >标签属性
   >1. class：为html元素定义一个或多个类名
   >2. id：定义元素的唯一id

   ```html
   <br> break换行
   
   <hr>分割线
   
   <p>paragraph一个段落</p>
   
   <!-- 这是一个注释 -->
   
   a标签
   1. anchor定义一个超链接，target="_blank"，点击链接新开一个标签页
   2. 相对路径，"./baidu.html"即当前html文件同目录下的baidu.html
      相对路径，"../serach/google.html"即当前html文件上层目录下的serach目录下的google.html
       <a href="https://www.runoob.com/" target="_blank">菜鸟教程</a>
       <a href="./baidu.html" target="_blank">baidu</a>
       <a href="../serach/google.html">google</a>
   3. 锚点，id属性用于设置当前页面的锚点，实现页面内跳转
       <a href="#c2">第2章</a>
       <a id="c1">第1章：贾雨村风尘怀闺秀</a>
       <a id="c2">第2章：冷子兴演说荣国府</a>
   4. 下载文件，href给出绝对或相对文件路径
       <a href="https://itsycal.s3.amazonaws.com/Itsycal.zip">google</a>
       <a href="../store/Itsycal.zip">google</a>
   
   img标签
   1. 在浏览器无法载入图像时，裂掉的图片会显示alt属性值
   2. 相对路径，"./img/pic.jpg"即当前html文件同目录下的img目录下的pic.jpg
      相对路径，"../img/pic.jpg"即当前html文件上层目录下的img目录下的pic.jpg
       <img src="https://xxx.jpg" alt="我裂了">
       <img src="./img/pic.jpg" alt="">
       <img src="../pic/tmp.jpg" alt="">
   3. 把img用做超链接，点击"./img/pic.jpg"，跳转到"./baidu.html"
       <a href="./baidu.html" target="_blank"><img src="./img/pic.jpg" alt=""></a>
       <a href="https://www.runoob.com/" target="_blank"><img src="./img/pic.jpg" alt=""></a>
   
   ul标签
   1. unorder list无序列表，
   2. li：list列表项，是个容器，可以存放任何元素，如a，，img，table等待
       <ul>
           <li>Coffee</li>
           <li>Milk</li>
       </ul>
   
   ol标签
   1. order list有序列表
   2. li：list列表项，是个容器，可以存放任何元素，如a，，img，table等待
       <ol>
           <li>Coffee</li>
           <li>Milk</li>
       </ol>
   
   dl标签
   1. define list自定义列表，用于名词解释，项目说明
   2. dt：项目名
   3. dd：项目描述
       <dl>
           <dt>项目名</dt>
           <dd>项目描述1</dd>
           <dd>项目描述2</dd>
       </dl>
   
   table标签
   1. thead：表格的头部区域，用于存放表头
       1. tr：table row表格的行
       2. th：table head表格的表头单元格，是特殊的td
   2. tbody：表格的主体区域，用户存放数据
       1. tr：table row表格的行
       2. td：table data表格的单元格
   3. 合并单元格：rowspan属性，跨行合并(合并第2，3行)；colspan属性，跨列合并(合并第2，3列)
   4. 表格常用属性：width：表格宽度；border：单元格边框厚度，默认是0px；cellpadding：单元格边缘与内容的距离，默认是1px；cellspacing：单元格之间的距离，默认是2px（px即像素）
       <table border="1">
           <thead>
               <tr>
                   <th>姓名</th>
                   <th>房产</th>
               </tr>
           </thead>
           <tbody>
               <tr>
                   <td>老王</td>
                   <td>2套</td>
               </tr>
               <tr>
                   <td rowspan='2'>老张</td>
                   <td>3套</td>
               </tr>
               <tr>
                   <td>2套</td>
               </tr>
           </tbody>
       </table>
   
   form表单
   1. action 属性，是个url，接收表单提交数据。只有含name属性的元素 才会被提交(MyName不会被提交)
   2. 可以是相对路径 action="example.html"，也可以是绝对路径action="http://www.example.com/example.html"
   3. radio 和 checkbox 必须有相同的name，默认选中checked
   4. submit在form的任何位置都会提交整个form表单域内的数据
   5. label绑定表单元素，点击label标签内的文本时，鼠标会focus到对应元素上，提升用户体验
   6. label用法for属性值与绑定元素的id属性值相同
       <form name="Sai的表单" action="./example.html" method="GET">
           Your name: <input type="text" name="name_文本域">
         
           <label for="psw">Password: </label>
           <input type="password" name="psw_密码字段" id='psw'>
   
           <input type="radio" name="sex_单选按钮" value="male" checked='checked'>Male
           <input type="radio" name="sex_单选按钮" value="female">Female
   
           <input type="checkbox" name="vehicle_复选框" value="Bike" checked='checked'>I have a bike
           <input type="checkbox" name="vehicle_复选框" value="Car">I have a car
   
           <input type="file" name="pic_上传文件">
   
           <textarea name="comment_多行文本" id="" cols="30" rows="3"></textarea>
   
           <select name='favorite'>
               <option value="1">Volvo</option>
               <option value="2" selected='selected'>Saab</option>
           </select>
   
           <input type="submit" name="sbm_提交按钮" value="提交">
       </form>
   
   div块
   1. 是用于文档布局的容器，可以组合其他 HTML 元素
   2. 1行只能放1个div
       <body>
           <div id="container" style="width:500px">
               <div id="header" style="background-color:#FFA500;">
                   <h1 style="margin-bottom:0;">主要的网页标题</h1>
               </div>
               <div id="menu" style="background-color:#FFD700;height:200px;width:100px;float:left;">
                   <b>菜单</b><br>
                   JavaScript</div>
               <div id="content" style="background-color:#EEEEEE;height:200px;width:400px;float:left;">
                   内容在这里</div>
               <div id="footer" style="background-color:#FFA500;clear:both;text-align:center;">
                   版权 © runoob.com</div>
           </div>
       </body>
   
   span 
   1. 是用于文档布局的容器，可以组合其他 HTML 元素
   2. 1行能放多个span
   
   
   
   
   frame框架，能在同一个浏览器窗口中显示不止一个页面
   
   ```

   案例

   ```html
   <h1>青春不再</h1>
   <table border="1">
     <thead>
       <tr><th>类别</th><th>选项</th></tr>
     </thead>
     <tbody>
       <tr>
         <td>性别</td>
         <td>
           <input type="radio" name='sex' id="male"><label for="male">男</label>
           <input type="radio" name='sex' id="female"><label for="female">女</label>
         </td>
       </tr>
       <tr>
         <td>生日</td>
         <td>
           <select name="" id="">
             <option value="1">--年--</option>
             <option value="1">1988</option>
             <option value="2">1989</option>
           </select>
           <select name="" id="">
             <option value="1">--月--</option>
             <option value="1">1988</option>
             <option value="2">1989</option>
           </select>
           <select name="" id="">
             <option value="1">--日--</option>
             <option value="1">1988</option>
             <option value="2">1989</option>
           </select>
         </td>
       </tr>
       <tr>
         <td>住址</td>
         <td>
           <input type="text" name="" id="">
         </td>
       </tr>
       <tr>
         <td>喜好</td>
         <td>
           <input type="checkbox" name="favo" id="">可爱型
           <input type="checkbox" name="favo" id="">霸道型
         </td>
       </tr>
       <tr>
         <td>自介</td>
         <td>
           <textarea name="" id="" cols="30" rows="2"></textarea>
         </td>
       </tr>
       <tr>
         <td></td>
         <td>
           <a href="#">我是会员，立即登录</a>
         </td>
       </tr>
       <tr>
         <td></td>
         <td>
           <h4>承诺</h4>
           <ul>
             <li>我年满18</li>
             <li>真诚寻爱</li>
           </ul>
         </td>
       </tr>
     </tbody>
   </table>
   ```

   ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200430200805.png)

### css

#### css基础篇

1. 原生css

   1. 位置： `<head></head>` 中的` <style></style>`

   2. css引入方式1：css写在html中

      ```html
      <head>
          <style>
              ul{
                  color: magenta;
              }
              ol{
                  font-size: 30px;
              }
          </style>
      </head>
      ```

   3. css引入方式2：css单独一个文件，html外部引用该文件

      `index.html`

      ```html
      <head>
          <link rel="stylesheet" href="../css/index_style.css">
      </head>
      ```

      `index_style.css`

      ```css
      ul {
          color: magenta;
      }
      ol {
          font-size: 30px;
      }
      ```

2. 基础选择器

   1. label选择器：修改指定标签的样式

      `label_name`无任何修饰

      ```html
      <style>
          label_name {
              样式属性：值
          }
      </style>
      ```

   2. class选择器（**最常用**）：修改指定class类的标签的样式

      `.`修饰`class_name`

      ```html
      <style>
          .class_name {
              样式属性：值
          }
      </style>
      ```

   3. id选择器：修改指定id的标签的样式

      `#`修饰`id_name`

      ```html
      <style>
          #id_name {
              样式属性：值
          }
      </style>
      ```

   4. 通配符选择器：修改所有标签的样式（性能太差，一般不用）

      ```html
      <style>
          * {
              样式属性：值
          }
      </style>
      ```

   | 选择器       | 作用             | 特点                         | 使用情况     |
   | ------------ | ---------------- | ---------------------------- | ------------ |
   | label选择器  | 选择所有相同标签 | 不能差异化选择               | 常用         |
   | class选择器  | 选择1类标签      | 能根据需求选择               | 最常用       |
   | id选择器     | 选择1个标签      | 1个id在1个html文件中是唯一的 | 与js一起用   |
   | 通配符选择器 | 选择全部标签     | 遍历所有标签，性能太差       | 特殊情况采用 |

   **案例**：label选择器 &&class选择器 &&  id选择器

   * css文件

     ```css
     <style>
         li {
             color: olivedrab;
         }
         .color {
             color: orchid;
         }
         #lisi {
             color: red;
         }
         .sai_font {
             font-size: 50px;
         }
         .sai_bg_color {
             background-color:grey;
         }
     </style>
     ```

   * html文件

     ```html
     <body>
         <li>陈大</li>
         <li class="color">刘二</li>
         <li class="color sai_bg_color">张三</li>
         <li class="color sai_font sai_bg_color">陈六</li>
         <li id='lisi'>李四</li>
         <div class="color">王五</div>
     </body>
     ```

   > 影响范围差别
   >
   > 1. label选择器：影响范围大
   > 2. class选择器：影响范围可大可小，可以定义相同label相同的类，也可以定义不同label相同的类
   >    1. 1个标签可以有多个class修饰，如陈六
   >    2. 可以抽象出字体类，背景色类，等等
   > 3. id选择器：只能影响一个标签，因为html的id属性必须是唯一的

3. 字体

   1. 字体单一属性

      ```css
      <style>
          body {
              /* 字体类型 */
              font-family: 'Times New Roman', Times, serif;
              /* 字体大小 */
              font-size: 16px;
              /* 字体粗细 */
              font-weight: 900;
              /* 字体样式（不常用） */
              font-style: italic;
          }
      </style>
      ```

      > 1. 字体类型：浏览器查看系统本地有无第1个`Times New Roman字体`，如没有就查看有无第2个`Times字体`，直至找到
      > 2. 字体大小：单位是`px`，即像素
      > 3. 字体粗细：无单位，数字范围100~900
      > 4. 文字样式：不常用

   2. 字体复合属性

      > 1. 必须遵守属性的顺序，即`font: font-style font-weight font-size/line-height font-family`
      > 2. `font-style font-weight`可以省略，不做设置，即`font: font-size/line-height font-family`

      ```css
      <style>
          body {
              font: italic 400 28px Times;
          }
          div {
              font: 15px serif;
          }
      </style>
      ```

4. 文本

   1. 3

      ```css
      <style>
          body {
              /* 文本颜色 */
              color: #ff0000;
              /* 文本水平对齐 */
              text-align: center;
              /* 装饰文本 */
              text-decoration: underline;
              /* 文本缩进 */
              text-indent: 20em;
              /* 行间距 */
              line-height: 26px;
          }
      </style>
      ```

      > 1. 文本缩进：em 表示文字块，2em 表示缩进2个字
      >
      > 2. 行间距：包括上间距，文字高度，下间距，若行间距是26px，文字是16px，则上下间距各5px
      >
      >    ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200501151758.png)

   

   

#### css高级篇

1. Emmet语法

   1. 快速生成html结构

      | 目的                                    | 操作                                       | 结果                                                         |
      | --------------------------------------- | ------------------------------------------ | ------------------------------------------------------------ |
      | 生成1个标签                             | `标签名`+Tab，如`div`                      | `<div></div>`                                                |
      | 生成n个相同标签                         | `标签名*n`+Tab，如`div*2`                  | `<div></div>`<br/>`<div></div>`                              |
      | 生成有父子级关系的标签                  | `父标签名>子标签名`+Tab，如`ul>li`         | `<ul>`<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<li></li>`<br/>`</ul>` |
      |                                         | `父标签名>子标签名*n`+Tab，如`ul>li*2`     | `<ul>`<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<li></li>`<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<li></li>`<br/>`</ul>` |
      | 生成兄弟级标签                          | `兄标签名+弟标签名`+Tab，如`div+p`         | `<div></div>`<br/>`<p></p>`                                  |
      |                                         | `兄标签名*n+弟标签名*n`+Tab，如`div*1+p*2` | `<div></div>`<br/>`<p></p>`<br/>`<p></p>`                    |
      | 生成带有class**值**和id**值**的标签     | `标签名.class值`+Tab，如`div.test`         | `<div class="test"></div>`                                   |
      |                                         | `标签名#id值`+Tab，如`p#123`               | `<p id="123"></p>`                                           |
      |                                         | 如`div.test*2`                             | `<div class="test"></div>`<br/>`<div class="test"></div>`    |
      |                                         | 如`p#123*2`                                | `<p id="123"></p>`<br/>`<p id="123"></p>`                    |
      |                                         | 如`ul>li#321*2`                            | `<ul>`<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<li id="321"></li>`<br/>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`<li id="321"></li>`<br/>`</ul>` |
      | 生成带有顺序class**值**和id**值**的标签 | `标签名.class值$*n`+Tab，如`div.test$*2`   | `<div class="test1"></div>`<br/>`<div class="test2"></div>`  |
      |                                         | `标签名#id值$*n`+Tab，如`div#demo$*2`      | `<div id="demo1"></div>`<br/>`<div id="demo2"></div>`        |
      | 生成带标签文字的标签                    | `标签名{$}`+Tab，如`div{case}`             | `<div>case</div>`                                            |
      |                                         | `标签名{$}*2`+Tab，如`div{case$}*2`        | `<div>case1</div>`<br/>`<div>case2</div>`                    |
      | 组合                                    | `div{case$}*.test$*#demo$*2`               | `<div class="test1" id="demo1">case1</div>`<br/>`<div class="test2" id="demo2">case2</div>` |

   2. 快速生成css样式

      

   3. 2































