##### CSS定位

> > css调试技巧：F12开发者工具 - 进入Elements面板 - 按`Esc`键后下方打开Console面板
> >
> > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311091848566.png)
>
> 
>
> > 1. `>`：即直接子节点
> >
> >    |        | `Son`                                                        | `.Son`                                                       | `#Son`                                                       |
> >    | ------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
> >    | `Dad`  | `Dad>Son`<br />标签名为`Dad`，直接子标签名为`Son`的所有节点  | `Dad>.Son`<br />标签名为`Dad`，直接子标签的`class="Son"`的所有节点 | `Dad>#Son`<br />标签名为`Dad`，直接子标签的`id="Son"`的所有节点 |
> >    | `.Dad` | `.Dad>Son`<br />标签的`class="Dad"`，直接子标签名为`Son`的所有节点 | `.Dad>.Son`<br />标签的为`class="Dad"`，直接子标签的`class="Son"`的所有节点 | `.Dad>#Son`<br />标签的为`class="Dad"`，直接子标签的`id="Son"`的所有节点 |
> >    | `#Dad` | `#Dad>Son`<br />标签的`id="Dad"`，直接子标签名为`Son`的所有节点 | `#Dad>.Son`<br />标签的`id="Dad"`，直接子标签的`class="Son"`的所有节点 | `#Dad>#Son`<br />标签的`id="Dad"`，直接子标签的`id="Son"`的所有节点 |
> >
> > 2. 
>
> **单节点定位**
>
> 1. `Element`：标签名定位，无需符号标记
>
>    `document.querySelectorAll('div')`
>
>    >取所有 `div` 节点
>
> 2. `#id`：id属性定位，用符号 `#` 标记
>
>    `document.querySelectorAll('#Hello')`
>
>    >取所有 `id="Hello"` 的节点
>
> 3. `.class`：类属性定位，用符号 `.` 标记
>
>    `document.querySelectorAll('.world')`
>
>    >取所有 `class="world"` 的节点
>
> 4. 其他属性定位，用`属性名`标记
>
>    `document.querySelectorAll('[type="text"]')`
>
>    >取所有 `type="text"` 的节点
>
> 5. 组合定位
>
>    1. 精确匹配
>
>       > 1. `document.querySelectorAll('div#Hello')`
>       >
>       >    > 取所有 `id="Hello"` 的 `div` 节点
>       >
>       > 2. `document.querySelectorAll('#Hello.world')`
>       >
>       >    >取所有 `id="Hello"` 且`class="world"` 的节点
>       >
>       > 3. `document.querySelectorAll('.world[href]')`
>       >
>       >    >取所有 `class="world"` 且包含属性`href`的节点
>       >
>       > 4. `document.querySelectorAll('[href][type="text"]')`
>       >
>       >    >取所有包含属性`href`且 `type="text"` 的节点
>
>    2. 模糊匹配
>
>       > 1. `*=`：前后模糊匹配
>       >
>       >    `document.querySelectorAll('[href="163"]')` 
>       >
>       >    > 可匹配`href="163.com"`、`href="mail.163.com"`
>       >
>       > 2. `^=`：以指定字符串开头的后模糊匹配
>       >
>       >    `document.querySelectorAll('[href^="163"]')` 
>       >
>       >    > 可匹配`href="163.com"`，不可匹配`href="mail.163.com"`
>       >
>       > 3. `$=`：以指定字符串结尾的前模糊匹配
>       >
>       >    `document.querySelectorAll('[src$=".png"]')` 
>       >
>       >    > 可匹配`src="xxx.png"`、不可匹配`src="xxx.png/5435435"`、`src="xxx.jpg"`、
>
> 多节点组合定位
>
> 1. `，`：如`Element,Element`，即并集
>
>    >1. `document.querySelectorAll('div,#Hello')`
>    >
>    >   > 取所有`div` 节点和所有 `id="Hello"` 的节点的并集
>    >
>    >2. `document.querySelectorAll('#Hello,.world')`
>    >
>    >   >取所有 `id="Hello"` 的节点和所有`class="world"` 的节点的并集
>    >
>    >3. `document.querySelectorAll('.world,[href]')`
>    >
>    >   >取所有 `class="world"` 的节点和所有包含属性`href`的节点的并集
>    >
>    >4. `document.querySelectorAll('[href],[type="text"]')`
>    >
>    >   >取所有包含属性`href`的节点和所有 `type="text"` 的节点的并集
>
> 2. `>`：如`FatherElement>SonElement`，即直接子节点，只包含儿子，不包含孙子，重孙子
>
>    >1. `document.querySelectorAll('div>#Hello')`
>    >
>    >   > 取其父节点的标签名为 `div` 的所有 `id="Hello"` 的 节点
>    >
>    >2. `document.querySelectorAll('#Hello>.world')`
>    >
>    >   >取其父节点的 `id="Hello"` 的所有`class="world"` 的节点
>    >
>    >3. `document.querySelectorAll('.world>[href]')`
>    >
>    >   >取其父节点的 `class="world"` 的所有包含属性`href`的节点
>    >
>    >4. `document.querySelectorAll('[href]>[type="text"]')`
>    >
>    >   >取其父节点包含属性`href`的所有 `type="text"` 的节点
>
> 3. `空格`：如`FatherElement SonElement`，即子孙节点，既包含儿子，又包含孙子，重孙子
>
>    >1. `document.querySelectorAll('div #Hello')`
>    >
>    >   > 取 `div` 节点下的所有 `id="Hello"` 的 节点
>    >
>    >2. `document.querySelectorAll('#Hello .world')`
>    >
>    >   >取 `id="Hello"` 的节点下所有`class="world"` 的节点
>    >
>    >3. `document.querySelectorAll('.world [href]')`
>    >
>    >   >取 `class="world"` 的节点下所有包含属性`href`的节点
>    >
>    >4. `document.querySelectorAll('[href] [type="text"]')`
>    >
>    >   >取包含属性`href`的节点下所有 `type="text"` 的节点
>
> 4. 

##### css基础篇

1. 基础选择器

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

   2. 字体复合写法

      > 1. 必须遵守属性的顺序，即`font: font-style font-weight font-size/line-height font-family`
      > 2. `font-style font-weight`可以省略，不做设置，即`font: font-size/line-height font-family`

      ```css
      body {
          font: italic 400 28px Times;
      }
      div {
          font: 15px serif;
      }
      ```
   
4. 文本

   ```css
   p {
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
   ```
   
   > 1. 文本缩进：em 表示文字块，2em 表示缩进2个字
>
   > 2. 行间距：包括上间距，文字高度，下间距，若行间距是26px，文字是16px，则上下间距各5px
   >
   >    ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200501151758.png)

   * 文本垂直居中的技巧

     > 设置文字行高等于盒子高度，即 height = line-height，若`height: 40px`，则`line-height: 40px`

   

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

   2. 复合选择器

      > 由多个基础选择器组成

      1. 后代选择器

         > 1. 格式：`父 子` 或 `父 子 孙` 或 `父 孙`（尽量把层级写完整，即不要用`父 孙`）
         > 2. 父、子、孙元素都可以是任意label选择器、class选择器、id选择器

         ```css
         /* 三个儿子是红色 */
         ol li {
             color: red;
         }
         /* 熊二是绿色 */
         ol li ul li {
             color: green;
         }
         /* 熊大是蓝色 */
         ol .temp div {
             color: blue;
         }
         /* 光头强是粉色 */
         ol li #test {
             color: pink;
         }
         ```

         ```html
         <ol>
             <li class="temp">大儿子
                 <div>熊大</div>
             </li>
             <li>二儿子
                 <ul>
                     <li>熊二</li>
                 </ul>
             </li>
             <li>三儿子
                 <a id='test' href="#">光头强</a>
             </li>
         </ol>
         ```
         
      2. 子选择器

         > 1. 格式：`父>子`，子元素必须是**儿子**
   > 2. 父、子元素都可以是任意label选择器、class选择器、id选择器
   
         ```css
   /* 只有儿子是红色 */
         div>a {
             color: red;
         }
         ```
   
         ```html
   <div class="nav">
             <a href="">儿子</a>
             <p>
                 <a href="">孙子</a>
             </p>
         </div>
         ```
   
      3. 并集选择器
      
         > 1. 格式：`标签元素1,标签元素2`

         ```css
         /* 熊大、熊二、小猪一家都是粉色 */
         div,
         p,
         .pig li {
             color: pink;
         }
         ```
      
         ```html
         <div>熊大</div>
         <p>熊二</p>
         <span>光头强</span>
         <ul class="pig">
             <li>佩奇</li>
             <li>猪爸爸</li>
             <li>猪妈妈</li>
         </ul>
         ```
         
      4. 伪类选择器
      
         1. 链接伪类选择器
         
            | 格式                       | 含义                     |
         | -------------------------- | ------------------------ |
            | `a:link`/`.pig:link`       | 选择所有未访问过的链接   |
         | `a:visited`/`.pig:visited` | 选择所有已访问过的链接   |
            | `a:hover`/`.pig:hover`     | 选择鼠标悬停的链接       |
         | `a:active`/`.pig:active`   | 选择鼠标按下未弹起的链接 |
         
            ```css
            /* 未访问过的链接显示黑色，去掉下划线 */
            a:link {
                color: black;
                text-decoration: none;
         }
            /* 已访问过的链接显示屎黄色 */
            a:visited {
                color: orange;
            }
            /* 鼠标悬停的链接显示天蓝色 */
            a:hover {
                color: skyblue;
            }
            /* 鼠标按下未弹起的链接显示荧光色 */
            a:active {
                color: chartreuse;
            }
            ```
         
            ```html
            <a class="pig" href="#1">佩奇</a>
            <a class="pig" href="#2">熊大</a>
            <a class="pig" href="#3">光头强</a>
            ```
         
         2. 光标伪类选择器
         
            > 1. 作用：选取光标所在的**表单**元素
         
            ```css
            /* 光标所在的表单元素背景色是粉红色 */
            input:focus {
             background-color: pink;
            }
      ```
         
      ```html
         <input type="text">输入框1
            <input type="text">输入框2
      ```
   
2. 元素显示模式

   1. 元素种类

      1. 块元素：`<div>`、`<h1>~<h6>`、`<p>`、`<ul>`、`<ol>`、`<li>`，其中`<div>`最典型
      2. 行内元素：`span`、`a`、`strong`、`b`、`em`、`i`、`del`、`s`、`ins`、`u`，其中`span`最典型
      3. 行内块元素：`img`、`input`、`td`

      | 种类       | 元素排列      | 样式           | 默认宽度   | 包含                         |
      | ---------- | ------------- | -------------- | ---------- | ---------------------------- |
      | 块元素     | 1行只能放一个 | 可设置宽、高   | 容器的宽度 | 可包含文本，行内元素，块元素 |
      | 行内元素   | 1行可放多个   | 不可设置宽、高 | 内容的宽度 | 可包含文本，行内元素         |
      | 行内块元素 | 1行可放多个   | 可设置宽、高   | 内容的宽度 |                              |

   2. 元素转换显示模式

      1. 行内元素转换为块元素：`display: block;` 如a标签，增加链接的触发范围

         ```css
         .line_to_block1 {
             width: 150px;
             height: 50px;
             background-color: salmon;
         }
         .line_to_block2 {
             width: 150px;
             height: 50px;
             background-color: salmon;
             /* 行内元素转换为块元素 */
             display: block;
         }
         ```

         ```html
         <a class='line_to_block1' href="#1">行内元素转换为块元素1</a>
         <a class='line_to_block2' href="#2">行内元素转换为块元素2</a>
         ```
         
      2. 行内元素转换为行内块元素：`display: inline-block;`

         ```css
         #line_to_lineblock1 {
             width: 350px;
             height: 50px;
             background-color: salmon;
         }
         #line_to_lineblock2 {
             width: 350px;
             height: 50px;
             background-color: salmon;
             /* 行内元素转换为行内块元素 */
             display: inline-block;
         }
         ```
      
         ```html
         <span id='line_to_lineblock1'>行内元素转换为行内块元素1</span>
         <span id='line_to_lineblock2'>行内元素转换为行内块元素2</span>
         ```
   
3. css背景

   1. 普通写法

      ```css
      .demo {
          height: 500px;
          /* 元素背景色，默认是透明 transparent */
          background-color: pink;
          /* 元素背景图片，默认是无图 none; */
          background-image: url(./img/baidu.jpg);
          /* 元素背景图片平铺，默认是平铺 repeat; */
          background-repeat: no-repeat;
          /* 元素背景图片位置，x y坐标可为方位词，如top bottom center right left */
          background-position: bottom center;
          /* 元素背景图片位置，x y坐标也可为数字，只写1个数字时，另1个默认居中 */
          background-position: 15px 30px;
          /* 元素背景图片位置，x y坐标也可为方位词+数字 */
          background-position: center 40px;
          /* 元素背景图片固定，默认是scroll */
          background-attachment: fixed;
      }
      ```

      ```html
      <div class="demo">
          <p>这是个透明控件</p>
          <p>这是个透明控件</p>
          <p>这是个透明控件</p>
      </div>
      ```
      
   2. 复合写法：

      > 背景色 背景图片 背景图片平铺 背景图片位置 背景图片固定（没顺序要求，这不像font复合写法）

      ```css
   .demo {
          /* 背景图片复合写法 */
          background: pink url(./img/baidu.jpg) no-repeat center 40px fixed;
      }
      ```
   
   3. 背景色透明度

      ```css
      .demo {
          /* 盒子背景透明图，前3位是RGB色值，第4位是透明度，0-1之间 */
          background: rgba(255, 192, 203, 0.5);
      }
      ```
   
4. css三大特性

   > 层叠性，继承性，优先级

   1. 层叠性

      ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200505203427.png)

      > **样式冲突时，就近原则，执行离得近的样式**
      >
      > 上图实际执行的是
      >
      > ```css
      > div {
      >     font-size: 18px;
      >     color: green;
      > }
      > ```

   2. 继承性

      ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200505203950.png)

      * 行高继承的另一种写法

        ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200505205618.png)

        > 父元素行高1.5的意思是，所有子元素的行高都是其字号的1.5倍

      

   3. 优先级

      | 选择器               | 权重                                       |
      | -------------------- | ------------------------------------------ |
      | 继承，通配符*        | 0,0,0,0                                    |
      | 元素选择器           | 0,0,0,1                                    |
      | 类选择器，伪类选择器 | 0,0,1,0                                    |
      | ID选择器             | 0,1,0,0                                    |
      | 行内样式style=""     | 1,0,0,0                                    |
      | !important           | 无视规则，可把任何选择器的优先级提升到最高 |

      1. 案例

         1. **行内样式style > ID选择器 > 类选择器，伪类选择器 > 元素选择器 > 继承，通配符**

            ```css
            div {
                color: blue;
            }
            .test {
                color: brown;
            }
            #demo {
                color: darkcyan;
            }
            * {
                color: fuchsia !important;
            }
            ```

            ```html
            <div>元素选择器优先级：0,0,0,1</div>
            <div class='test'>类选择器优先级：0,0,1,0</div>
            <div class='test' id='demo'>ID选择器优先级：0,1,0,0</div>
            <div class='test' id='demo' style="color: darkorange;">行内样式style优先级：1,0,0,0</div>
            ```

         2. **不管父标签的权重多高，子标签继承来的权重都是0**

            ```css
            .fatherDiv {
                color: fuchsia;
            }
            .sonP {
                color: green;
            }
            #sonId {
                color: turquoise;
            }
            ```

            ```html
            <div class="fatherDiv">
                <p class="sonP">继承的优先级为0</p>
                <p>继承的优先级为0</p>
                <a href="#">a标签有自己的样式（蓝色+下划线）</a><br>
                <a href="#" id='sonId'>a标签要单独修改样式</a>
            </div>
            ```

      2. 复合选择器权重叠加

         ```css
         /* 权重：0,0,0,1 */
         li {
             color: pink;
         }
         /* 权重：0,0,0,1 + 0,0,0,1 = 0,0,0,2  */
         ul li {
             color: green;
         }
         /* 权重：0,0,1,0 + 0,0,0,1 = 0,0,1,1  */
         /* 权重无论累加少，都不会进位，如 0,0,1,0 > 0,0,0,15 */
         .fatherUl li {
             color: magenta;
         }
         /* 虽然类选择器权重高，但是被继承后，权重为0 */
         .fatherUl {
             color: red;
         }
         ```

         ```html
         <ul class="fatherUl">
             <li>熊大</li>
             <li>熊二</li>
             <li>光头强</li>
         </ul>
         ```




#### css盒子布局

1. 本质：封装html元素的容器

   ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200508122912.png)

2. border边框

   1. 边框组成：宽度，样式，颜色

      ```css
      div {
          width: 250px;
          height: 150px;
          border-width: 5px;
          /* solid 实线；dashed 虚线；dotted 点线*/
          border-style: dotted;
          border-color: salmon;
      }
      ```

      ```html
      <div>这是个盒子</div>
      ```

   2. 边框复合写法

      ```css
      div {
          width: 250px;
          height: 150px;
          border: 5px dotted pink;
      }
      ```

   3. 修改上下左右边框

      ```css
      div {
          width: 250px;
          height: 150px;
          border: 5px dotted pink;
          border-top: 10px solid powderblue;
      }
      ```

   4. 边框影响盒子大小

      > 盒子实际大小 = 盒子尺寸 + 边框尺寸

      ```css
      /* 若要求盒子高为150px，则内容高度为140px，上边框5px，下边框5px，共150px */
      div {
          width: 250px;
          height: 140px;
          border: 5px dotted pink;
      }
      ```

   5. 表格细线边框

      ```css
      table {
          width: 150px;
          height: 200px;
      }
      table, td, th {
          border: 1px dotted pink;
          /* 合并重叠的边框 */
          border-collapse: collapse;
          font-size: 25px;
          text-align: center;
      }
      ```

      ```html
      <table>
          <thead>
              <tr><th>姓名</th><th>房产</th></tr>
          </thead>
          <tbody>
              <tr><td>老王</td><td>2套</td></tr>
              <tr><td rowspan='2'>老张</td><td>3套</td></tr>
              <tr>                        <td>2套</td></tr>
          </tbody>
      </table>
      ```

3. 内边距padding

   ```css
   div {
       height: 50px;
       width: 180px;
       border: 1px solid #000;
       padding: 2px;
       padding-left: 10px;
       padding-right: 20px;
       padding-bottom: 30px;
   }
   ```

   ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200508160941.png)

   1. 内边距复合写法

      | 值的个数                     | 意思                                          |
      | ---------------------------- | --------------------------------------------- |
      | padding: 5px;                | 上下左右都是5像素                             |
      | padding: 5px 10px;           | 上下5像素，左右10像素                         |
      | padding: 5px 10px 20px;      | 上5像素，左右10像素，下20像素                 |
      | padding: 5px 10px 20px 30px; | 上5像素，右10像素，下20像素，左30像素，顺时针 |

   2. 内边距影响盒子大小

      > 盒子实际大小 = 盒子尺寸 + 边框尺寸 + 内边距

      ```css
      /* 若要求盒子高为150px，则内容高度为120px，上边框5px，下边框5px，上内边距10px，下内边距10px，共150px */
      div {
          width: 250px;
          height: 120px;
          border: 5px dotted pink;
          padding: 10px;
      }
      ```

4. 外边距margin

   ```css
   div {
       height: 50px;
       width: 180px;
       border: 1px solid #000;
       margin: 2px;
       margin-left: 10px;
       margin-right: 20px;
       margin-bottom: 30px;
   }
   ```

   ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200508170707.png)

   1. 外边距复合写法

      | 值的个数                    | 意思                                          |
      | --------------------------- | --------------------------------------------- |
      | margin: 5px;                | 上下左右都是5像素                             |
      | margin: 5px 10px;           | 上下5像素，左右10像素                         |
      | margin: 5px 10px 20px;      | 上5像素，左右10像素，下20像素                 |
      | margin: 5px 10px 20px 30px; | 上5像素，右10像素，下20像素，左30像素，顺时针 |

   2. 外边距影响盒子大小

      > 盒子实际大小 = 盒子尺寸 + 边框尺寸 + 内边距 + 外边距

      ```css
      /* 若要求盒子高为150px，则内容高度为80px，上边框5px，下边框5px，上内边距10px，下内边距10px，上外边距20px，下外边距20px，共150px */
      div {
          width: 250px;
          height: 120px;
          border: 5px dotted pink;
          padding: 10px;
          margin: 20px;
      }
      ```

   3. **块级元素**水平居中

      > 盒子左右外边距设为auto即可

      ```css
      div {
          width: 250px;
          height: 120px;
          border: 5px dotted pink;
          margin: 0 auto;
      }
      ```

   4. **行内元素、行内块元素**水平居中

      > 给其父元素添加text-align: center;

      ```css
      div {
          width: 250px;
          height: 120px;
          border: 5px dotted pink;
          margin: 0 auto;
          text-align: center;
      }
      ```

      ```html
      <div>
          盒子内容Content
          <p>p元素</p>
      </div>
      ```

   5. 嵌套块元素垂直外边距的塌陷问题

      > 问题：子块元素的上边距 > 父块元素的上边距时，子元素不会下移，父元素会下移
      >
      > 方案：
      >
      > 1. 父元素定义上边框
      > 2. 父元素定义上内边距
      > 3. 父元素添加属性

      ```css
      .father {
          width: 250px;
          height: 100px;
          background-color: powderblue;
          margin-top: 10px;
          /* 方案1：父元素定义上边框 */
          border-top: 1px solid transparent;
          /* 方案2：父元素定义上内边距 */
          padding-top: 1px;
          /* 方案3：父元素添加属性 */
          overflow: hidden;
      }
      .son {
          width: 100px;
          height: 50px;
          background-color: salmon;
          margin-top: 20px;
      }
      ```

      ```html
      <div class='father'>
          <div class="son"></div>
      </div>
      ```

5. 清除内外边距

   一些元素**默认自带**内外边距，且不同浏览器的内外边距**值**不同

   ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200508181404.png)

   ```css
   /* css第一个样式，先清除边距 */
   * {
       margin: 0;
       padding: 0;
   }
   ```

6. 圆角边框

   ```css
   .rectangle {
       width: 100px;
       height: 50px;
       background-color: salmon;
       /* 圆角矩形，半径设为高度的1/2 */
       border-radius: 25px;
   }
   .square {
       width: 100px;
       height: 100px;
       background-color: green;
       /* 圆形，半径设为边长的1/2，可精确写成px，也可写成50% */
       border-radius: 50px;
   }
   .fulArgs {
       width: 100px;
       height: 100px;
       background-color: red;
       /* 四个角弧度不同，顺时针，左上，右上，右下，左下 */
       border-radius: 10px 20px 30px 40px;
   }
   ```

   ```html
   <div class="rectangle"></div>
   <div class="square"></div>
   <div class="fulArgs"></div>
   ```

7. 盒子阴影

   > box-shadow: h-shadow v-shadow blur spread color;
   >
   > > h-shadow：水平阴影，可为负值    v-shadow：垂直阴影，可为负值
   > >
   > > blur：模糊距离    spread：阴影尺寸    color：阴影颜色

   ```css
   .rectangle {
       width: 100px;
       height: 50px;
       background-color: salmon;
   }
   .rectangle:hover {
       box-shadow: 5px 10px 15px 20px lightblue;
   }
   ```

   ```html
   <div class="rectangle"></div>
   ```

##### 小tips

> * ps工具
>   1. 开启标尺：视图 - 标尺
>   2. 修改标尺单位：双击标尺，改为像素
>
> 
>
> 去掉ul li前面的无序小圆点
>
> 1. list-style: none;
>
>    ```
>    ul li {
>        list-style: none;
>    }
>    ```



#### css浮动

1. 常见网页布局

   > 标准流，浮动，定位

   1. 标准流：块元素、行内元素，按照规定好的默认方式排列

      1. 块元素：独占一行，自上而下顺序排列
         * 如：div、hr、p、h1~h6、ul、ol、dl、form、table
      2. 行内元素：一行多个，自左至右顺序排列，遇到父元素边缘则自动换行
         * 如：span、a、i、em

   2. 浮动

      > 应用：多个块元素在一行内排列显示
      >
      > * 多个块元素纵向排列用标准流
      > * 多个块元素横向排列用浮动

      1. float属性创建浮动框，将元素向左侧或右侧移动，直到碰到**父边框**或另一个**浮动框**

         ```css
         div {
             width: 100px;
             height: 50px;
         }
         .left {
             background-color: salmon;
             float: left;
         }
         .right {
             background-color: green;
             float: right;
         }
         ```

         ```html
         <a href="#">小飞机</a>
         <div class="left">青龙</div>
         <div class="right">白虎</div>
         ```

      2. 浮动的特性

         1. 浮动元素会脱标（脱离标准流）

            > 1. 脱离标准流的控制，移动到指定位置
            > 2. 移走的元素不再保留原来的位置
            > 3. 浮动元素只会影响后面的标准流，不会影响前面的标准流
            >
            > ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200509115609.png)

            ```css
            .top {
                width: 100px;
                height: 50px;
                background-color: salmon;
            }
            .center {
                float: left;
                width: 150px;
                height: 75px;
                background-color: red;
            }
            .bottom {
                width: 200px;
                height: 100px;
                background-color: green;
            }
            ```

            > 不要这么写，一个元素浮动，其兄弟元素也要浮动，就不会出各种奇葩问题

            ```html
            <div class="top">标准流</div>
            <div class="center">浮动</div>
            <div class="bottom">标准流</div>
            ```

         2. 浮动元素会在一行内显示，且顶部对齐

            > 1. 浮动元素无缝隙靠在一起
            > 2. 父元素一行放不下时，则自动换行
            >
            > ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200509120755.png)

            ```css
            div {
                float: left;
                width: 200px;
            }
            .No1 {
                height: 50px;
                background-color: salmon;
                float: left;
            }
            .No2 {
                height: 100px;
                background-color: green;
            }
            .No3 {
                height: 150px;
                background-color: red;
            }
            ```

            ```html
            <div class="No1"></div>
            <div class="No2"></div>
            <div class="No3"></div>
            ```

         3. 浮动元素有行内块元素的特性

            > 1. 任何元素都可以添加浮动属性，块元素，行内元素添加浮动后都有行内块特性
            >
            > ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200509121739.png)

            ```css
            span {
                width: 200px;
                height: 150px;
                background-color: salmon;
            }
            .floatSpan {
                float: right;
            }
            ```

            ```html
            <span>原生span是行内元素，无法设置宽高</span>
            <span class="floatSpan">floatSpan添加了float属性后具备行内块特性，可设置宽高</span>
            ```

      3. **浮动元素**常与**标准流父元素**配合使用

         > 1. 先用标准流父元素排列上下位置
         > 2. 再给子元素设置float属性排列左右位置
         >
         > ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200509122317.png)

         ```css
         .father {
             width: 300px;
             height: 100px;
             background-color: salmon;
             margin: 100px auto;
         }
         .sonLeft {
             float: left;
             width: 100px;
             height: 50px;
             background-color: skyblue;
         }
         .sonRight {
             float: right;
             width: 100px;
             height: 50px;
             background-color: skyblue;
         }
         ```

         ```html
         <div class="father">
             <div class="sonLeft"></div>
             <div class="sonRight"></div>
         </div>
         ```

2. 清除浮动

   > 1. 父元素没有高度：浮动的子元素数量可变时，不能写死父元素的行高
   > 2. 子元素不占位置：浮动的子元素不占有位置，会对后面的排版产生影响
   >
   > ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200509135545.png)
   >
   > * 清除浮动的本质：消除浮动元素造成的恶劣影响，让父元素自动检测高度

   1. 方法1：额外标签法（不常用）

      > 在浮动元素末尾添加一个空标签`<div style="clear: both;"></div>`

   2. 方法2：父元素添加`overflow`属性

      > `overflow: hidden;`
      >
      > 缺点：无法显示溢出部分

      ```css
      .father {
          /* 方法2：父元素添加overflow属性 */
          overflow: hidden;
          width: 350px;
          background-color: salmon;
          margin: 0 auto;
      }
      .son {
          float: left;
          width: 100px;
          height: 50px;
          background-color: skyblue;
      }
      .foot {
          width: 100%;
          height: 150px;
          background-color: yellowgreen;
      }
      ```

      ```html
      <div class="father">
          <div class="son"></div>
          <div class="son"></div>
          <!-- 方法1：在浮动元素末尾添加一个空标签 -->
          <div style="clear: both;"></div>
      </div>
      <div class="foot"></div>
      ```

   3. 方法3：父元素添加`:after`伪元素

      ```css
      .clearfix::after {
          content: "";
          display: block;
          height: 0;
          clear: both;
          visibility: hidden;
      }
      
      .father {
          width: 350px;
          background-color: salmon;
          margin: 0 auto;
      }
      .son {
          float: left;
          width: 100px;
          height: 50px;
          background-color: skyblue;
      }
      .foot {
          width: 100%;
          height: 150px;
          background-color: yellowgreen;
      }
      ```

      ```html
      <!-- 父元素有2个类名 -->
      <div class="father clearfix">
          <div class="son"></div>
          <div class="son"></div>
      </div>
      <div class="foot"></div>
      ```

   4. 方法4：父元素添加双伪属性

      ```css
      .clearfix::before,
      .clearfix:after {
          content: "";
          display: table;
      }
      .clearfix:after {
          clear: both;
      }
      
      .father {
          width: 350px;
          background-color: salmon;
          margin: 0 auto;
      }
      .son {
          float: left;
          width: 100px;
          height: 50px;
          background-color: skyblue;
      }
      .foot {
          width: 100%;
          height: 150px;
          background-color: yellowgreen;
      }
      ```

      ```html
      <!-- 父元素有2个类名 -->
      <div class="father clearfix">
          <div class="son"></div>
          <div class="son"></div>
      </div>
      <div class="foot"></div>
      ```

3. PS切片



#### css定位

1. 定位：将盒子固定在某个位置

   * 定位 = 定位模式 + 边偏移

     1. 定位模式

        | 模式                     | 是否脱标 | 移动位置                           | 备注     |
        | ------------------------ | -------- | ---------------------------------- | -------- |
        | `static`：静态定位       | 否       | 不用边偏移                         |          |
        | **`relative`：相对定位** | **否**   | **相对自身位置边偏移**             | **常用** |
        | **`absolute`：绝对定位** | **是**   | **相对带有定位的父元素位置边偏移** | **常用** |
        | **`fixed`：固定定位**    | **是**   | **相对浏览器可视区边偏移**         | **常用** |
        | `sticky`：粘性定位       | 否       | 相对浏览器可视区边偏移             |          |

     2. 边偏移

        | 属性   | 示例         | 描述                               |
        | ------ | ------------ | ---------------------------------- |
        | top    | top: 80px    | 顶端偏移，元素距父元素上边线的距离 |
        | bottom | bottom: 80px | 底部偏移，元素距父元素下边线的距离 |
        | left   | left: 80px   | 左侧偏移，元素距父元素左边线的距离 |
        | right  | right: 80px  | 右侧偏移，元素距父元素右边线的距离 |

2. `relative`：相对定位

   * 即元素移动位置是相对于自己原来的位置来说的

     `选择器 {position: relative; }`	

     ```css
     .head {
         position: relative;
         left: 200px;
         top: 200px;
       
         width: 100px;
         height: 50px;
         background-color: skyblue;
     }
     .foot {
         width: 100px;
         height: 50px;
         background-color: pink;
     }
     ```

     ```html
     <div class="head"></div>
     <div class="foot"></div>
     ```

3. `absolute`：绝对定位

   * 即元素移动位置是相对于祖先元素的位置来说的

     `选择器 {position: absolute; }`

     1. 若没有祖先元素或祖先元素没有定位，则以浏览器的边缘为参考点来定位

     2. 绝对定位的元素不占有原来的位置

     3. 若祖先元素有（相对，绝对，固定）定位，则以最近一级有定位的祖先元素为参考点来定位

        ```css
        .father {
            /* 若祖先元素有（相对，绝对，固定）定位，则以最近一级有定位的祖先元素为参考点来定位 */
            position: relative;
            width: 200px;
            height: 100px;
            background-color: pink;
        }
        
        .boy {
            /* 若没有祖先元素或祖先元素没有定位，则以浏览器的边缘为准来定位 */
            position: absolute;
            right: 50px;
            top: 50px;
          
            width: 100px;
            height: 50px;
            background-color: skyblue;
        }
        
        /* 绝对定位脱标的元素不占有原来的位置，girl盒子会上移 */
        .girl {
            width: 100px;
            height: 50px;
            background-color: red;
        }
        ```

        ```html
        <div class="father">
            <div class="boy"></div>
            <div class="girl"></div>
        </div>
        ```

4. `fixed`：固定定位

   * 即固定在浏览器的某个位置，不随页面滚动而滚动

     `选择器 {position: fixed; }`

     1. 以**浏览器可视区**为参考点来定位，与父元素没关系

     2. 绝对定位的元素不占有原来的位置

        ```css
        .demo {
            position: fixed;
            right: 50px;
            top: 50px;
        
            width: 200px;
            height: 100px;
            background-color: pink;
        }
        ```

        ```html
        <div class="demo"></div>
        ```

5. `sticky`：粘性定位

   `选择器 {position: sticky; top: 10px }`

   1. 以**浏览器可视区**为参考点来定位（fixed 特点）

   2. 占有原本的位置（relative 特点）

      ```css
      body {
          height: 3000px;
      }
      .demo {
          position: sticky;
          top: 10px;
          width: 800px;
          height: 50px;
          background-color: pink;
          margin: 100px auto;
      }
      ```

      ```html
      <div class="demo"></div>
      <div class="w"></div>
      ```

6. 定位叠放次序

   `选择器 {z-index: num; }`

   1. num默认是auto，可改为正数，负数或0，越大盒子越靠上

   2. num相同时，按照书写顺序，后来者居上

      ```css
      .demo {
          position: absolute;
          top: 10px;
          width: 200px;
          height: 100px;
      }
      .red {
          background-color: red;
          z-index: 0;
      }
      .blue {
          background-color: blue;
          left: 50px;
          top: 50px;
      }
      .pink {
          background-color: pink;
          left: 100px;
          top: 100px;
      }
      ```

      ```html
      <div class="demo red"></div>
      <div class="demo blue"></div>
      <div class="demo pink"></div>
      ```

7. 小技巧

   1. 将盒子固定在版心右侧

      > 以**浏览器版心**为参考点来定位
      >
      > 1. 先让固定定位的盒子`left: 50%`，走到浏览器可视区的一半左侧（也是版心的一半左侧）
      > 2. 再让固定定位的盒子`margin-left: 版心宽度的一半`

      ```css
      .w {
          width: 500px;
          height: 1400px;
          background-color: greenyellow;
          margin: 0 auto;
      }
      .demo {
          position: fixed;
          /* 先右移浏览器可视区的一半距离，到垂直中线右侧 */
          left: 50%;
          /* 再右移版心的一半距离，到版心的右侧 */
          margin-left: 250px;
          top: 50px;
      
          width: 100px;
          height: 100px;
          background-color: pink;
      }
      ```

      ```html
      <div class="demo"></div>
      <div class="w"></div>
      ```

   2. 将盒子固定在版心中央

      > 1. 先让固定定位的盒子`left: 50%`，走到浏览器可视区的一半左侧（也是版心的一半左侧）
      > 2. 再让固定定位的盒子`margin-right: 盒子宽度的一半`

      ```css
      .w {
          width: 500px;
          height: 1400px;
          background-color: greenyellow;
          margin: 0 auto;
      }
      .demo {
          position: fixed;
          /* 先右移浏览器可视区的一半距离，到垂直中线右侧 */
          left: 50%;
          /* 再左移盒子自身的一半距离，到版心的垂直中央 */
          margin-left: -50px;
          /* 先下移浏览器可视区的一半距离，到水平中线下侧 */
          top: 50%;
          /* 再上移盒子自身的一半距离，到版心的水平中央 */
          margin-top: -50px;
          width: 100px;
          height: 100px;
          background-color: pink;
      }
      ```

      ```html
      <div class="demo"></div>
      <div class="w"></div>
      ```

   3. 1

##### Css 网页布局总结

1. 标准流：让多个块级盒子垂直显示
2. 浮动：让多个块级盒子一行显示
3. 定位：让多个块级盒子层叠显示

![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200510160826.png)



##### 显示隐藏元素

1. display

   1. `display: none; `：隐藏后，元素不再占有位置

   2. `display: block; `：显示

      ```css
      .w {
          width: 100px;
          height: 100px;
          margin: 10px;
      }
      .a {
          display: none;
          background-color: goldenrod;
      }
      .b {
          background-color: pink;
      }
      ```

      ```html
      <div class="w a"></div>
      <div class="w b"></div>
      ```

2. visibility

   1. `visibility: hidden;`：隐藏后，元素继续占有位置

   2. `visibility: visible;`：显示

      ```css
      .w {
          width: 100px;
          height: 100px;
          margin: 10px;
      }
      .c {
          visibility: hidden;
          background-color: red;
      }
      .d {
          background-color: royalblue;
      }
      ```

      ```html
      <div class="w c"></div>
      <div class="w d"></div>
      ```

3. overflow

   1. `overflow: hidden;`：溢出部分不显示

   2. `overflow: auto;`：溢出时显示滚动条

   3. `overflow: scroll;`：溢出不溢出都显示滚动条

      ```css
      .w {
          width: 100px;
          height: 100px;
          margin: 10px;
          background-color: salmon;
      }
      .e {
          overflow: hidden;
      }
      ```

      ```html
      <div class="w e">
          《富爸爸·穷爸爸》是以提倡“财务智商”的教育成为畅销书。
      </div>
      ```

      

#### css高级技巧

1. 精灵图

   * 应用：结构复杂的小图片

   * 坐标都是负值

     ```css
     .box {
         width: 23px;
         height: 30px;
         margin: 0 auto;
         background: url(./img/a.png) -157px -102px;
     }
     ```

     ```html
     <div class="box"></div>
     ```

2. 字体图标

   * 应用：结构简单的小图标
   * 看起来像图标，本质是字体

3. css三角

   > 设置宽高为0的矩形

   ```css
   .box1 {
       width: 0;
       height: 0;
       border-top: 50px solid red;
       border-right: 50px solid green;
       border-bottom: 50px solid blue;
       border-left: 50px solid pink;
   }
   .box2 {
       position: relative;
       width: 200px;
       height: 200px;
       background-color: salmon;
   }
   .box3 {
       position: absolute;
       left: 150px;
       top: -50px;
       width: 0;
       height: 0;
       border: 25px solid rgba(0, 0, 0, 0);
       border-bottom: 25px solid pink;
   }
   ```

   ```html
   <div class="box1"></div>
   <div class="box2">
       <div class="box3"></div>
   </div>
   ```

4. css用户界面样式

   1. 修改鼠标样式

      | 属性        | 形状描述 |
      | ----------- | -------- |
      | default     | 箭头     |
      | pointer     | 小手     |
      | move        | 移动     |
      | text        | 文本选择 |
      | not-allowed | 禁止     |

      ```html
      <ul>
          <li style="cursor: pointer;">鼠标样式：小手</li>
          <li style="cursor: move;">鼠标样式：移动</li>
          <li style="cursor: text;">鼠标样式：文本</li>
          <li style="cursor: not-allowed ;">鼠标样式：禁止</li>
      </ul>
      ```

   2. 消除输入框的轮廓线

      > `outline: none`

      ```html
      <input type="text">
      <input type="text" style="outline: none">
      ```

   3. 禁止文本域拖拽

      > `resize:none`

      ```html
      <textarea name="" id="" cols="30" rows="10"></textarea>
      <textarea name="" id="" cols="30" rows="10" style="resize:none"></textarea>
      ```

   4. 图片、表单、文字垂直对齐

      > 只用于行内块元素

      ```css
      img, textarea {
          border: 1px solid pink;
          vertical-align: middle;
      }
      ```

      ```html
      <img src="./img/baidu.jpg" alt="">大百度<br>
      <textarea name="" id="" cols="30" rows="10"></textarea>文本域
      ```

   5. 溢出文字显示省略号

      1. 单行文字显示省略号

         > 1. 先强制一行内显示文字：`white-space: nowrap;`
         > 2. 再隐藏超出部分：`overflow: hidden;`
         > 3. 最后省略号代替超出部分：`text-overflow: ellipsis;`

         ```css
         div {
             width: 150px;
             height: 20px;
             border: 1px solid pink;
             white-space: nowrap;
             overflow: hidden;
             text-overflow: ellipsis;
         }
         ```

         ```html
         <div class="box">省略一万字，啥都别说了</div>
         ```

      2. 多行文字显示省略号（兼容性问题）

5. 常见布局技巧

   1. margin负值

      1. 消除边框叠加

         > 原理：每个盒子都左移一个边框的距离，用第2个box的左边框盖住第1个box的右边框

         ```css
         .original li {
             list-style: none;
             float: left;
             width: 150px;
             height: 20px;
             border: 5px solid pink;
         }
         .new li {
             margin-left: -5px;
         }
         ```

         ```html
         <ul class="original">
             <li></li>
             <li></li>
             <li></li>
         </ul>
         <hr>
         <ul class="original new">
             <li></li>
             <li></li>
             <li></li>
         </ul>
         ```

      2. 鼠标悬浮边框变色

         > 问题：因box左移，右边框都被盖住，会看不到变色
         >
         > 原理：鼠标悬浮时，提高盒子的层级。有定位的box加z-index，没定位的加相对定位(relative)来保留位置

         ```css
         .original li {
             position: relative;
             list-style: none;
             float: left;
             width: 150px;
             height: 20px;
             border: 5px solid pink;
             margin-left: -5px;
         }
         .original li:hover {
             z-index: 1;
             border-color: green;
         }
         ```

         ```html
         <ul class="original">
             <li></li>
             <li></li>
             <li></li>
         </ul>
         ```

   2. 文字围绕浮动元素

   3. 行内块的技巧

   4. css三角强化

6. 



