#### 调试

1. 调试本地页面

   1. 新建`Test.html` ，`！+ tab`自动生成如下代码

      ```html
      <!DOCTYPE html>
      <html lang="en">
      <head>
      <meta charset="UTF-8">
      <meta name="viewport" content="width=device-width, initial-scale=1.0">
      <title>Document</title>
      </head>
      <body>
      
      </body>
      </html>
      ```

   2. 配合VSCode的 `Live Server` 插件

2. 调试线上页面

   1. 在线上页面调试自己的js代码

      > 都不用vscode，用`Snippets`  写代码族裔

      1. 进入`Snippets` ：开发者工具 - `Sources` - 左侧导航中的找到`Snippets`
      2. 编写代码：`New Snippet` - 命名 - 编辑器中粘贴我的 JavaScript 代码
      3. 设置断点：编辑器行号旁边的空白处来设置断点
      4. 运行`Snippets` 
      5. 运行代码：编辑器右下角“Run”执行Snippet；左侧导航的Snippet 文件上右击“Run”

   2. 在线上页面调试页面上的js代码

      1. 进入`Page` ：开发者工具 - `Sources` - 左侧导航中的找到`Page`，选择js文件
      2. 设置断点：编辑器行号旁边的空白处来设置断点
      3. 刷新页面

   ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311151554165.png)

3. [调试技巧](https://www.bilibili.com/video/BV1zu4y127mu)

   1. 普通断点

   2. 条件断点

      > 断点上右键 - Edit breakpoint - 设置i === 5，即只在i的值是5时，暂停
      >
      > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311151859540.png)

   3. 调试方式

      ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311151830074.png)

      1. `① 恢复 (Resume）`：执行，直到下一个断点

      2. `② 跨步(step over）`：运行下一条指令，不会进入函数

      3. `③ 步入(step into）`：运行下一条指令，会进入函数；

      4. `④ 步出 (step out）`：执行完当前函数，回到③步入之前的代码

         > 使用`③步入`偶然进入到一个函数，但是又想中途跳出，可使用 `④步出`

      5. `⑤ 单步 (step）`：同`③ 步入`

         > 同步代码中与`③步入` 类似，异步上有区别


#### 引入js

1. 内部引入

   ```html
   <body>
       <script>
           alert('前端弹窗的输出内容')
           console.log('Chrome - F12 - Console的输出内容')
       </script>
   </body>
   ```

2. 外部引入

   * `Sai.js`

     ```js
     alert('前端弹窗的输出内容')
     console.log('Chrome - F12 - Console的输出内容')
     ```

   * `test.html`

     ```html
     <body>
      <script src="Sai.js"></script>
     </body>

#### 基础语法

1. 用户输入 `prompt`  `confirm`

   ```js
   let temp_prompt = prompt("输入一个字符串")
   console.log(`用户输入的是：${temp_prompt}`)
   // 确定：true，取消：false
   let temp_confirm = confirm('今天心情好么')
   console.log(`用户输入的是：${temp_confirm}`)
   ```

2. 程序输出 `alert`

   ```js
   alert('前端弹窗的输出内容')
   console.log('Chrome - F12 - Console的输出内容')
   ```

   >[浏览器控制台无法输出console.log打印数据](https://blog.csdn.net/m0_67841039/article/details/131575811)
   >
   >![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311112118665.png)

3. 数据类型

   1. 定义变量

      * `let 变量名 = 变量值`
      * `const 常量名 = 常量值`

   2. 数值

      >整数、小数在 JavaScript 中都是number

      ```js
      console.log(typeof 1)  // 类型判断：number
      console.log(typeof 1.1)  // 类型判断：number
      ```

   3. 字符串

      ```js
      console.log(typeof 'Hello')  // 类型判断：string
      console.log('Hello'.length)  // 字符串长度：5
      console.log('Hello'.toUpperCase())  // 大写转换HELLO
      console.log('Hello'.toLowerCase())  // 小写转换hello
      console.log('Hello'.substr(3))  // 字符串截取：从下标3到末尾：lo
      console.log('Hello'.substr(1,3))  // 字符串截取：从下标1到下标3：ell
      console.log('Hello, world'.split(", "))  // 字符串分割：['Hello', 'world']
      
      // 多行字符串
      let name = 'Will'
      let msg_MoreLine = `Hello
      world
      guys`
      console.log(msg_MoreLine)
      console.log(`你好啊 ${name}`)  // 模板字符串：你好啊 Will
      ```

   4. 运算符

      ```js
      let temp1 = (2>1 && 3>4) ? "全部为真" : "任意一方为假"
      console.log(`&&的结果时：${temp1}`)
      let temp2 = (2>1 || 3>4) ? "任意一方为真" : "全部为假"
      console.log(`||的结果时：${temp2}`)
      let temp3 = (! 2>1) ? "非真" : "非假"
      console.log(`!的结果时：${temp3}`)
      let temp4 = (2 === "2") ? "绝对等于" : "不绝对等于"
      console.log(`===的结果时：${temp4}`)
      let temp5 = (2 !== "2") ? "绝对不等于" : "不绝对不等于"
      console.log(`!==的结果时：${temp5}`)
      ```

   5. 数组

      > JavaScript数组中可以容纳任何值

      ```js
      let temp_Array = [1, 2, 'Hi', "Jiang Sai", null, true]
      console.log(typeof temp_Array)  // 类型判断：object
      console.log(Array.isArray(temp_Array))  // 判断是否为数组类型：true
      console.log(temp_Array[3])  // 数组取值：Jiang Sai
      console.log(temp_Array.length)  // 数组长度：6
      // 数组增加元素：splice(index, 0 , let) 在下标index处增加元素let
      temp_Array.splice(2, 0, 'will');
      console.log(temp_Array)
      // 数组删除元素：splice(index, n) 从下标index处删除n个元素
      temp_Array.splice(2, 1);
      console.log(temp_Array)
      // 遍历数组
      temp_Array.forEach(function (element) {
       console.log(element);
      })
      for (let element of temp_Array) {
       console.log(element);
      }
      
      //以下不常用
      console.log(temp_Array.slice(3))  // 数组截取：从下标3到末尾
      console.log(temp_Array.slice(1, 3))  // 数组截取：从下标1到下标3
      temp_Array.unshift(520, 123)  // 数组增加元素：头部增加多个元素
      console.log(temp_Array)
      // 数组增加元素：尾部增加多个元素
      temp_Array.push(250, 321)
      console.log(temp_Array)
      // 数组删除元素：头部删除第1个元素
      temp_Array.shift()
      console.log(temp_Array)
      // 数组删除元素：尾部删除第1个元素
      temp_Array.pop()
      console.log(temp_Array)
      // 多维数组
      let temp_MultiArray = [[1, 2], ['Hi', "Jiang Sai"], [null, true]]
      // 多维数组取值
      console.log(temp_MultiArray[1][0])

   6. 对象（即字典）

      ```js
      // JS对象就是字典
      let temp_Dict = {
       name: 'Will',
       age: 35,
       tags: ['Python', 'SQL', 'JS']
      }
      console.log(typeof temp_Dict)  // 类型判断：object
      // 遍历对象
      for (const [key, value] of Object.entries(temp_Dict)) {
       console.log(`${key}: ${value}`);
      }
      for (let key in temp_Dict) {
       console.log(`${key}: ${temp_Dict[key]}`);
      }
      ```

   7. 对象和Json的转换

      ```js
      let temp_Dict = {
       name: 'Will',
       age: 35,
       tags: ['Python', 'SQL', 'JS']
      }
      console.log(temp_Dict.tags)
      let temp_Json = JSON.stringify(temp_Dict)  // 对象可转换成Json
      console.log(temp_Json)
      let temp_Json_Parse = JSON.parse(temp_Json)  // Json可解析成对象
      console.log(temp_Json_Parse)
      ```

      >对象和Json的区别
      >
      >> 对象：`temp_Dict = { name: 'Will', age: 35, tags: ['Python', 'SQL', 'JS'] }`
      >>
      >> Json：`temp_Json = {"name":"Will","age":35,"tags":["Python","SQL",798]}`
      >>
      >> Json的key必须全都带双引号

   8. Set（无序不重复集合）

      ```js
      let temp_Set = new Set([1, 2, 1, 3]);
      console.log(typeof temp_Set)  // 类型判断：object
      temp_Set.add(4)  // 新增元素
      temp_Set.delete(1)  // 删除元素
      console.log(temp_Set.has(1))  // 判断set是否包含元素
      console.log(Array.from(temp_Set))  // 输出set所有元素
      
      // 3种遍历set所有元素
      temp_Set.forEach(function (element) {
       console.log(element);
      })
      temp_Set.forEach((element) => {
       console.log(element);
      });
      for (let element of temp_Set) {
       console.log(element);
      }
      ```

4. 流程控制

   ```js
   let num = 1
   
   // 三目运算：结果 = 条件判断 ? 条件成立的值 : 条件不成立的值
   let result = num > 5 ? '条件成立' : '条件不成立';
   console.log(`结果是 ${result}`);
   
   // while 和 if
   while (num < 3) {
    if (num % 2 === 0) {
        console.log(`${num} 是偶数`);
    } else if (num % 2 === 1) {
        console.log(`${num} 是奇数`);
    } else {
        console.log(`见鬼了`);
    }
    num += 1;
   }
   
   // for 和 switch
   // break：结束当前层的整个循环
   // continue：结束本轮循环，继续下一轮循环
   for (let i = 0; i < num; i++) {
    switch (i) {
        case 1:
            console.log(`i 是${i}，执行case 1`);
            break;
        case 2:
            console.log(`i 是${i}，执行case 2`);
            break;
        // num 无法匹配上述数值时执行的代码
        default:
            console.log(`i 是${i}，执行default`);
            break;
    }
   }
   ```

5. 异常

   ```js
   let num = 1;
   if (typeof num !== Number) {
    throw `${num}不是个数字`
   }
   ```

6. 函数

   | 原始形式                                                     | 箭头形式                                                     |
   | ------------------------------------------------------------ | ------------------------------------------------------------ |
   | 带名函数<br />function Func_Name(x) {<br/>    console.log(`x 是${x}`);<br/>}<br/>Func_Name(-5) | 带名 - 箭头函数<br />const fun_name = (x) => {<br/>    console.log(`x 是${x}`);<br/>}<br/>Func_Name(-5) |
   | 匿名函数<br />// 声明时不赋值，仅用于立即执行<br/>(function (x, y) {<br/>    return x*(y+1);<br/>})(-5, 5) | 匿名函数<br />// 声明时不赋值，仅用于立即执行<br/>((x, y) => {<br/>    return x*(y+1);<br/>})(-5, 5) |
   | 匿名函数<br />// 声明时赋值，用法同带名函数<br/>let temp = function (x, y) {<br/>    return x*(y+1);<br/>}<br/>temp(-5, 5) | 匿名函数<br />// 声明时赋值，用法同带名函数<br/>let temp = (x, y) => {<br/>    return x*(y+1);<br/>}<br/>temp(-5, 5) |
   | // 事件监听<br />// click发生时，执行function(e) {} <br/>sai.addEventListener('click', function(e) {<br/>    console.log('「监听事件」点了我一下')<br/>}) | // 事件监听<br />// click发生时，执行function(e) {} <br/>sai.addEventListener('click', (e) => {<br/>    console.log('「监听事件」点了我一下')<br/>}) |

   * 带名函数

     ```js
     function Func_Name(x) {
         console.log(`x 是${x}`);
     }
     setInterval(Func_Name(1), 1000)
     ```

   * 匿名函数

     > * 又叫立即执行函数；因为没有函数名，因此不能被调用，故而不立即执行就没意义
     > * 用途：如果一个函数仅使用一次，即用即弃，就没必要给它命名

     ```js
     // 声明时不赋值，仅用于立即执行
     (function (x, y) {
         return x*(y+1);
     })(-5, 5)
     ```

     ```js
     // 声明时赋值，用法同带名函数，不知意义何在
     let temp = function (x, y) {
         return x*(y+1);
     }
     temp(-5, 5)

   * 箭头函数

     ```js
     // 声明时不赋值，仅用于立即执行
     ((x, y) => {
         return x*(y+1);
     })(-5,5)
     ```

     ```js
     // 声明时赋值，用法同带名函数，不知意义何在
     let temp = ((x, y) => {
         return x*(y+1);
     })(-5,5)
     temp(-5, 5)
     ```

     * 当箭头函数只有一个参数时

       * 正常的写法

         ```js
         ((x) => {
             return x;
         })(5)

       * 省略参数括号的写法

         ```js
         (x => {
             return x;
         })(5)
         ```

     * 当箭头函数的函数体只有一个return时

       * 正常的写法

         ```js
         ((x, y) => {
             return x*(y+1);
         })(-5, 6)
         ```

       * 省略 `return` 关键字，省略函数体花括号的写法

         ```js
         ((x, y) => x*(y+1))(-5, 6)
         ```

     * 当箭头函数只有一个参数，且函数体只有一个return时

       * 正常的写法

         ```js
         ((x) => {
             return x*(x+1);
         })(5)

       * 省略参数括号，省略 `return` 关键字，省略函数体花括号的写法

         ```js
         (x => x*(x+1))(5)

7. Date对象

   ```js
   let now = new Date()
   console.log(now)  // 当前完整时间
   console.log(now.getFullYear())  // 年
   console.log(now.getMonth())  // 月（0-11）
   console.log(now.getDate())  // 日
   console.log(now.getDay())  // 星期几
   console.log(now.getHours())  // 时
   console.log(now.getMinutes())  // 分
   console.log(now.getSeconds())  // 秒
   console.log(now.getTime())  // 时间戳
   console.log(now.toLocaleString())  // 当地时间：年月日 时分秒
   ```

8. 定时器

   1. `setInterval(目标函数, 间隔时间)` ：每隔一段时间执行1次目标函数

      ```js
      let timing = setInterval(function() {
          // 打印当前时间
          console.log(new Date().toLocaleString())
          // 秒数为30时，结束定时器 timing
          if (new Date().getSeconds() === 30) {
              clearInterval(timing)
          }
      }, 1000)
      ```

   2. 

9. 类

   ```js
   class Person {
       // 构造函数
       constructor(name, age) {
           this.name = name;
           this.age = age;
       }
   
       greet() {
           console.log(`This's ${this.name}, I'm ${this.age}`);
       }
   }
   // 继承
   class Student extends Person {
       constructor(name, age, course) {
           super(name, age);
           this.course = course;
       }
   
       study() {
           console.log(`I'm studying ${this.course}.`);
       }
   }
   let person1 = new Person('Alice', 30);
   person1.greet();
   
   let student1 = new Student('Bob', 20, 'JavaScript');
   student1.greet();
   student1.study();
   ```

10. BOM对象

   * window：当前浏览器窗口，**以下 `window.` 均可省略**

     ```js
     window.innerHeight  // 窗口内边框高度
     window.innerWidth  // 窗口内边框宽度
     window.outerHeight  // 窗口外边框高度
     window.outerWidth  // 窗口外边框高度
     // 判断浏览器当前是否有temp_url标签，若没有则新建temp_url标签，并打开https://www.baidu.com/
     window.open('https://www.baidu.com/','temp_url')  
     ```

   * screen：当前电脑屏幕

     ```js
     screen.width  // 屏幕宽度
     screen.height  // 屏幕高度

   * location：当前页面的URL信息

     ```js
     location.href  // 当前网页的网址：'https://baidu.rudon.cn/'
     location.host  // 当前网站主机名：'baidu.rudon.cn'
     location.reload()  // 当前网页刷新
     location.assign('https://www.zhihu.com')  // 页面重定向

   * document：当前页面

     ```js
     document.title = 'Sai'  // 修改页面标题
     document.cookie  // 获取页面cookie（病毒程序，获取对方的cookie可以免登陆做很多事）

   * history：页面历史

     ```js
     history.back()  // 页面后退
     history.forward()  // 页面前进

11. DOM节点（增删改查）

    > ```js
    > let htmlString = '<div class="bili"><span id="will">你好啊Will</span><span id="jason">你好啊Jason</span></div>'
    > // 创建一个新的 DOMParser 实例
    > let parser = new DOMParser();
    > // 使用 parseFromString 方法将字符串转换为 DOM
    > let doc = parser.parseFromString(htmlString, 'text/html');
    > // 获取 DOM 中的第一个元素
    > let Temp = doc.body.firstChild;
    > ```

    * Dom获取

      * 通过 `css` 获取

        ```js
        Temp.querySelector('[id]')  // 用CSS获取Temp节点下第一个匹配的节点
        Temp.querySelectorAll('[id]')  // 用CSS获取Temp节点下所有匹配的节点

      * 通过 `Xpath` 获取

        * Chrome - Console中调试：`$x(xpath，Temp)[0]`，注意`[0]`

          ```js
          $x('//*[@id="jason"]')[0]  // 用xpath获取document下第一个匹配的节点
          $x('.//*[@id="jason"]'，Temp)[0]  // 用xpath获取Temp节点下第一个匹配的节点
          $x('.//*[@id="jason"]'，Temp)[0]  // 用xpath获取Temp节点下所有匹配的节点

        * 脚本执行

          ```js
          document.evaluate(xpath, Temp, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue  // 用xpath获取Temp节点下第一个匹配的节点
          document.evaluate(xpath, Temp, null, XPathResult.ORDERED_NODE_SNAPSHOT_TYPE, null)  //用xpath获取Temp节点下所有匹配的节点
          ```

      * 通过关系获取

        ```js
        Temp.parentNode  // 获取Temp节点的父节点
        Temp.children  // 获取Temp节点的所有子节点
        Temp.children[1]  // 获取Temp节点的第1个子节点
        ```

    * Dom新增

      * 尾部追加子元素

        ```js
        let b1 = document.createElement('button')  // 新增一个button元素b1
        b1.setAttribute('id','tail')  // 设置b1的属性值
        b1.textContent='我插在尾上'  // 设置b1的文本值
        Temp.appendChild(b1)  // 将b1追加到temp的子元素的尾部

      * 任意位置插入子元素

        ```js
        b2 = document.createElement('button')  // 新增一个button元素b2
        b2.setAttribute('id','head')  // 设置b2的属性值
        b2.textContent='我插在头上'  // 设置b2的文本值
        Temp.insertBefore(b2, Temp.children[0])  // 将b1插入到temp的第1个子元素的前面
        ```

    * Dom删除

      ```js
      let head = Temp.querySelector('[id=head]')
      head.remove()  // 移除head节点

    * Dom内容操作

      ```js
      Temp.textContent  // 获取Temp节点的文本内容，包括脚本和样式
      Temp.textContent = "修改内容"  // 修改Temp节点的文本内容，修改会删除所有子元素
      Temp.outerHTML  //  获取Temp节点的HTML内容（包含Temp节点自身）
      Temp.innerHTML  //  获取Temp节点的HTML内容（不包含Temp节点自身）
      ```

    * Dom属性操作

      ```js
      Temp.hasAttribute('id')  // 检查Temp节点自身是否具有id属性  // false
      Temp.getAttribute('class')  // 获取Temp节点自身的class属性值  // 'bili'
      Temp.setAttribute('src', 'wula')  // 首先判断Temp节点是否有src属性，若没有则新增，若有则将src属性值设为wula
      Temp.removeAttribute('src')  // 删除Temp节点的src属性
      ```



#### 事件注册方式

```js
// 当前temp为：<img src="/img/bd.png"">，要为其添加点击事件
let node_img = document.querySelector("img")
```

* 方法一：添加 onclick 事件属性

  * 带名函数

    ```js
    // 带名函数
    node_img.setAttribute('onclick',"fun_name()")
    function fun_name(){
      console.log('「带名函数」点了')
    }
    // 带名 - 箭头函数
    node_img.setAttribute('onclick', "fun_name()");
    const fun_name = () => {
      console.log('「带名函数」点了');
    };
    ```

    > `function fun_name()` 替换成 `const fun_name = () => `

  * 匿名函数

    ```js
    // 匿名函数
    node_img.onclick = function (){
      console.log('「匿名函数1」点了')
    }
    // 匿名 - 箭头函数
    node_img.onclick = () => {
      console.log('「匿名函数1」点了');
    };
    ```

    >`function ()` 替换成 `() => `

    ```js
    匿名函数 - 简写
    node_img.setAttribute('onclick',"console.log('「匿名函数2」点了')")

* 方法二：添加 click 事件监听

  ```js
  // click 是事件，function(event) {} 是事件发生时执行的函数
  node_img.addEventListener('click', function(event) {
      console.log('「监听事件」点了我一下')
  })
  // click 是事件，event => {} 是事件发生时执行的箭头函数
  node_img.addEventListener('click', (event) => {
    console.log('「监听事件」点了我一下');
  })
  ```

  > 同上匿名函数： `function(event)` 替换成 `(event) => `

1. 添加节点事件属性：`内联模式绑定事件`

   > JavaScript代码混入HTML中，不利于维护

   * `onclick`： **单击节点** 时触发

   * `ondblclick`： **双击节点** 时触发

   * `onfocus`：节点 **获得焦点** 时触发

   * `onblur`：节点 **失去焦点** 时触发

   *  `onkeydown` ：节点上，任一键 **按下** 时触发

   * `onkeyup` ：节点上，任一键 **弹起** 时触发

   * `onchange`：节点的 **值发生变化** 时触发。用于`<input>`、`<select>`和`<textarea>`）

   * `onmouseover` ：节点上方 **有鼠标经过** 时触发

   * `onmouseout`：节点上方 **有鼠标移出** 时触发

   * `onload` ：节点加载完成时触发。一般手工增加节点时能用到

     ```js
     let node_input = document.querySelector("input")
     node_input.setAttribute('onclick',"console.log('input 点击')")
     node_input.setAttribute('ondblclick',"console.log('input 双击')")
     node_input.setAttribute('onfocus',"console.log('input 获得焦点')")
     node_input.setAttribute('onblur',"console.log('input 失去焦点')")
     node_input.setAttribute('onkeydown',"console.log('input 按键被按下')")
     node_input.setAttribute('onkeyup',"console.log('input 按键释放')")
     node_input.setAttribute('onchange',"console.log('input 值改变了')")
     node_input.setAttribute('onmouseover',"this.style.backgroundColor='red'")
     node_input.setAttribute('onmouseout',"this.style.backgroundColor=''")
     node_input.setAttribute('onload',"console.log('input 加载完毕')")
     ```

2. 添加事件监听：`外联模式绑定事件`

   1.  鼠标事件

      * **`click`**：**单击节点** 时触发
      * **`dblclick`**：**双击节点** 时触发
      * **`mousedown`**：节点上 **按下鼠标** 时触发
      * **`mouseup`**：节点上 **释放鼠标** 时触发
      * **`mousemove`**：节点上 **鼠标移动** 时触发
      * **`mouseover`**：节点上方 **有鼠标经过** 时触发
      * **`mouseout`**：节点上方 **有鼠标移出** 时触发

      ```js
      node_img = document.querySelector("img")
      // Temp节点被鼠标单击时触发
      node_img.addEventListener('click', function() {
          console.log('元素被点击');
      });
      // Temp节点被鼠标双击时触发
      node_img.addEventListener('dblclick', function() {
          console.log('元素被双击');
      });
      // Temp节点上有鼠标按下时触发
      node_img.addEventListener('mousedown', function() {
          console.log('鼠标按下');
      });
      // Temp节点上有鼠标释放时触发
      node_img.addEventListener('mouseup', function() {
          console.log('鼠标释放');
      });
      // Temp节点上有鼠标移动时触发，event就是监听的事件mousemove
      node_img.addEventListener('mousemove', function(event) {
          console.log('鼠标坐标：', event.clientX, event.clientY);
      });
      // Temp节点上鼠标进入时触发
      node_img.addEventListener('mouseover', function() {
          console.log('鼠标悬停在元素上方');
      });
      // Temp节点上鼠标离开时触发
      node_img.addEventListener('mouseout', function() {
          console.log('鼠标离开元素');
      });
      ```

      * 实战案例：在屏幕上，鼠标右下方，实时展示鼠标的坐标

        ```js
        // 创建用于显示坐标的元素（如果已经存在则跳过此步骤）
        var mouse_XY = document.createElement('div');
        mouse_XY.id = 'mouse_XY';
        mouse_XY.style.position = 'absolute';
        mouse_XY.style.backgroundColor = 'lightgrey';
        mouse_XY.style.padding = '5px';
        mouse_XY.style.border = '1px solid black';
        document.body.appendChild(mouse_XY);
        
        // 鼠标在页面上移动时触发，mousemove 事件发生时，调用function (event) {}
        document.addEventListener('mousemove', function (event) {
            // 更新坐标显示元素的内容 
            mouse_XY.textContent = '鼠标坐标：' + event.clientX + ', ' + event.clientY;
            // 更新坐标显示元素的位置
            mouse_XY.style.left = (event.clientX + 10) + 'px';
            mouse_XY.style.top = (event.clientY + 10) + 'px';
        });
        ```

        > `event.clientX` ，`event.clientY `：以当前可视窗口的左上角为原点
        >
        > `event.pageX` ，`event.pageY `：以当前整个页面的左上角为原点
        >
        > `event.screenX` ，`event.screenY `：以当前屏幕的左上角为原点

      * 实战案例：废弃掉，某个节点的点击跳转

        ```js
        let node_temp = document.querySelector('div[class="beian-wrapper"]').children[0]
        node_temp.addEventListener('click', function (event) {
            event.preventDefault(); // 这会阻止默认行为
        });
        ```

   2. 键盘事件

      * **`keydown`** ：任一键「被按下」时触发

        ```js
        // 为「页面document」添加键盘事件：Escape 和 m 键被按下时触发
        document.addEventListener('keydown', function(event) {
            if (event.key === 'Escape') {
                document.querySelector("img").style.visibility = 'hidden';
                console.log('Esc键被按下，消息隐藏');
            }else if (event.key === 'm') {
                document.querySelector("#subBtn").value = '小样';
                console.log('Esc键被按下，消息隐藏');
            }
        });
        // 为「某个div」添加键盘事件
        node_img = document.querySelector("img")
        node_img.addEventListener('keydown', function(event){
        }
        ```

      * **`keyup`** ：任一键「弹起」时触发

        ```js
        // 为「页面document」添加键盘事件：Escape 和 m 键弹起时触发
        document.addEventListener('keyup', function(event) {
            if (event.key === 'Escape') {
                document.querySelector("img").style.visibility = 'visible';
                console.log('Esc键被按下，消息隐藏');
            }else if (event.key === 'm') {
                document.querySelector("#subBtn").value = '百度一下';
                console.log('Esc键被按下，消息隐藏');
            }
        });
        // 为「某个div」添加键盘事件
        node_img = document.querySelector("img")
        node_img.addEventListener('keyup', function(event){
        }
        ```

        * 实战案例：若当前网页的URL 以https://www.baidu.com/开头，则组织某些快捷键

          ```js
          // 判断当前网址
          if (window.location.href.startsWith("https://www.baidu.com/")) {
              // 监听键盘事件 keydown
              document.addEventListener('keydown', function(event) {
                  // 检查是否按下了 Command + S
                  if (event.metaKey && event.key === 's') {
                      // 阻止默认的保存行为
                      event.preventDefault();
                      console.log('执行自定义操作');
                  }
              });
          }
          ```

          >`control` ：对应 `e.ctrlKey` 
          >`shift` ：对应 `e.shiftKey` ，使用 `shift + 某个按键` 时需将`event.key === 'S'`设为大写，因为shift会影响大小写
          >
          >`command` ：对应  `e.metaKey` ，一般不单独使用`command`与其他键的组合，因为`command`+其他键的常规组合太多，会冲突
          >
          >`option` ：对应 `e.altKey` ，一般不单独使用`option`与其他键的组合，因为`option`+其他键会输出特殊字符

   3. 删除事件

      >只能删除普通函数的事件监听器，匿名函数的事件监听器无法删除

      ```js
      // 添加事件
      head.addEventListener('click', SaiFun);
      function SaiFun() {
          alert('增加响应click事件');
      }
      // 移除事件
      head.removeEventListener("click", SaiFun)
      ```

----

##### 爬虫案例

1. 爬取页面中单个节点下的元素

   > 定位一个合适的父节点，然后在该父节点下进行定位取值

   ```js
   // 1. 定位父节点
   var xpath_Parent = '//*[@class="video-list row"]/div[1]'
   var node_Parent = document.evaluate(xpath_Parent, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
   
   if (node_Parent) {
       // 2. 取属性值：在父节点下定位到「标题」节点
       var xpath_Title = '//*[@class="bili-video-card__info--tit"]'
       var node_Title = document.evaluate(xpath_Title, node_Parent, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
       var Title = node_Title ? node_Title.getAttribute('title') : null;
   
       // 3. 取节点正文：在父节点下定位到「上传日期」节点
       var xpath_LoadTime = '//*[@class="bili-video-card__info--date"]'
       var node_LoadTime = document.evaluate(xpath_LoadTime, node_Parent, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
       var LoadTime = node_LoadTime ? node_LoadTime.textContent : null;
   
       console.log("标题是:", Title);
       console.log("上传时间是:", LoadTime);
   } else {
       console.log("未找到指定的父节点");
   }
   ```

2. 爬取页面中列表节点下的元素

   >定位列表的父节点，然后在该父节点下取子节点，在该子节点下进行定位取值

   ```js
   // 1. 定位父节点
   let xpath_Parent = '//*[@class="video-list row"]'
   let node_Parent = document.evaluate(xpath_Parent, document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
   let Sons = node_Parent.children
   
   // 2. 遍历每个子节点
   Array.from(Sons).forEach(function(son) {
       // 3. 子节点内取属性值：在父节点下定位到「标题」节点；使用相对 XPath 路径
       let xpath_Title = './/*[@class="bili-video-card__info--tit"]'
       let node_Title = document.evaluate(xpath_Title, son, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
       let Title = node_Title ? node_Title.getAttribute('title') : null;
   
       // 4. 子节点内取节点正文：在父节点下定位到「上传日期」节点；使用相对 XPath 路径
       let xpath_LoadTime = './/*[@class="bili-video-card__info--date"]'
       let node_LoadTime = document.evaluate(xpath_LoadTime, son, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue;
       let LoadTime = node_LoadTime ? node_LoadTime.textContent : null;
   
       console.log("标题是:", Title);
       console.log("上传时间是:", LoadTime);
   })
   ```

3. 爬取（暂时用不到）

   ```js
   fetch('https://scrape.center/')
     .then(response => response.text())
     .then(html => {
       // 解析HTML内容
       const parser = new DOMParser();
       const doc = parser.parseFromString(html, 'text/html');
       
       // 提取标题文本
       const title = doc.querySelector('title').textContent;
       
       // 打印标题文本
       console.log('网页标题：', title);
     })
     .catch(error => {
       console.error('发生错误：', error);
     });
   ```

   

