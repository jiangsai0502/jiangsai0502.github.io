Vscode配置

> 1. 调试本地页面
>
>    1. 新建`Test.html` ，`！+ tab`自动生成如下代码
>
>       > ```js
>       > <!DOCTYPE html>
>       > <html lang="en">
>       > <head>
>       >  <meta charset="UTF-8">
>       >  <meta name="viewport" content="width=device-width, initial-scale=1.0">
>       >  <title>Document</title>
>       > </head>
>       > <body>
>       > 
>       > </body>
>       > </html>
>       > ```
>
>    2. 安装`Live Server`插件
>
>       >![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311111221157.png)
>       >
>       >* 服务地址`http://127.0.0.1:5500/文件名`
>       >
>       >* 保存即自动执行
>
> 2. 调试在线页面
>
>    1. 安装VScode插件`JavaScript Debugger`
>
>    2. `推荐`新建一个空项目 - 进入调试视图 -「创建lauch.json文件」- Web应用(Chrome) - 编辑json文件
>
>       > ```json
>       > {
>       >     "version": "0.2.0",
>       >     "configurations": [
>       >         {
>       >             "type": "chrome",
>       >             "request": "launch",
>       >             "name": "Sai用Chrome调试在线网页",
>       >             "url": "https://www.zhihu.com/question/23498580",
>       >             "webRoot": "${workspaceFolder}"
>       >         }
>       >     ]
>       > }
>       > ```
>
>    3. 调试视图 - 运行和调试刚新建的lauch.json文件
>
>    4. Chrome 中设置断点，代码执行到断点时，VS Code将暂停执行并显示调试器界面
>
>    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311131126610.png)
>
>    > 调试在线网页的最佳方式：将网页下载到本地
>

引入js

1. 内部引入

   > ```html
   > <body>
   >     <script>
   >         alert('前端弹窗的输出内容')
   >         console.log('Chrome - F12 - Console的输出内容')
   >     </script>
   > </body>

2. 外部引入

   > `Sai.js`
   >
   > ```js
   > alert('前端弹窗的输出内容')
   > console.log('Chrome - F12 - Console的输出内容')
   > ```
   >
   > `test.html`
   >
   > ```html
   > <body>
   >     <script src="Sai.js"></script>
   > </body>

基础语法

1. 输入

   > 前端输入：`prompt("输入一个字符串")`

2. 输出

   > 1. 前端输出：`alert('前端弹窗的输出内容')`
   >
   > 2. Console控制台输出：`console.log('Chrome - F12 - Console的输出内容')`
   >
   >    > [浏览器控制台无法输出console.log打印数据](https://blog.csdn.net/m0_67841039/article/details/131575811)
   >    >
   >    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311112118665.png)

3. 调试

   > > Sources控制台：①双击打开文件 - ②在<script></script>脚本里设置断点 - ③刷新页面 - ④逐步调试
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311112146525.png)

4. 数据类型

   > 1. 定义变量
   >
   >    >`let 变量名 = 变量值`
   >    >
   >    >`const 常量名 = 常量值`
   >
   > 2. 数值
   >
   >    > 整数、小数在 JS 中都是number
   >    >
   >    > ```js
   >    > console.log(typeof 1)  // 类型判断：number
   >    > console.log(typeof 1.1)  // 类型判断：number
   >
   > 3. 字符串
   >
   >    > ```js
   >    > console.log(typeof 'Hello')  // 类型判断：string
   >    > console.log('Hello'.length)  // 字符串长度：5
   >    > console.log('Hello'.toUpperCase())  // 大写转换HELLO
   >    > console.log('Hello'.toLowerCase())  // 小写转换hello
   >    > console.log('Hello'.substr(3))  // 字符串截取：从下标3到末尾：lo
   >    > console.log('Hello'.substr(1,3))  // 字符串截取：从下标1到下标3：ell
   >    > console.log('Hello, world'.split(", "))  // 字符串分割：['Hello', 'world']
   >    > 
   >    > // 多行字符串
   >    > let name = 'Will'
   >    > let msg_MoreLine = `Hello
   >    > world
   >    > guys`
   >    > console.log(msg_MoreLine)
   >    > console.log(`你好啊 ${name}`)  // 模板字符串：你好啊 Will
   >    > ```
   >
   > 4. 布尔值
   >
   > 5. 运算符
   >
   >    > &&：与
   >    >
   >    > ||：或
   >    >
   >    > !：非
   >    >
   >    > =：赋值
   >    >
   >    > ===：绝对等于
   >    >
   >    > !==：绝对不等于
   >
   > 6. 数组
   >
   >    > JS数组中可以容纳任何值
   >    >
   >    > ```js
   >    > let temp_Array = [1, 2, 'Hi', "Jiang Sai", null, true]
   >    > console.log(typeof temp_Array)  // 类型判断：object
   >    > console.log(Array.isArray(temp_Array))  // 判断是否为数组类型：true
   >    > console.log(temp_Array[3])  // 数组取值：Jiang Sai
   >    > console.log(temp_Array.length)  // 数组长度：6
   >    > // 数组增加元素：splice(index, 0 , let) 在下标index处增加元素let
   >    > temp_Array.splice(2, 0, 'will');
   >    > console.log(temp_Array)
   >    > // 数组删除元素：splice(index, n) 从下标index处删除n个元素
   >    > temp_Array.splice(2, 1);
   >    > console.log(temp_Array)
   >    > // 遍历数组
   >    > temp_Array.forEach(function (element) {
   >    >     console.log(element);
   >    > })
   >    > for (let element of temp_Array) {
   >    >     console.log(element);
   >    > }
   >    > 
   >    > //以下不常用
   >    > console.log(temp_Array.slice(3))  // 数组截取：从下标3到末尾
   >    > console.log(temp_Array.slice(1, 3))  // 数组截取：从下标1到下标3
   >    > temp_Array.unshift(520, 123)  // 数组增加元素：头部增加多个元素
   >    > console.log(temp_Array)
   >    > // 数组增加元素：尾部增加多个元素
   >    > temp_Array.push(250, 321)
   >    > console.log(temp_Array)
   >    > // 数组删除元素：头部删除第1个元素
   >    > temp_Array.shift()
   >    > console.log(temp_Array)
   >    > // 数组删除元素：尾部删除第1个元素
   >    > temp_Array.pop()
   >    > console.log(temp_Array)
   >    > // 多维数组
   >    > let temp_MultiArray = [[1, 2], ['Hi', "Jiang Sai"], [null, true]]
   >    > // 多维数组取值
   >    > console.log(temp_MultiArray[1][0])
   >    > ```
   >
   > 7. 对象（字典）
   >
   >    > ```js
   >    > // JS对象就是字典
   >    > let temp_Dict = {
   >    >     name: 'Will',
   >    >     age: 35,
   >    >     tags: ['Python', 'SQL', 'JS']
   >    > }
   >    > console.log(typeof temp_Dict)  // 类型判断：object
   >    > // 遍历对象
   >    > for (const [key, value] of Object.entries(temp_Dict)) {
   >    >     console.log(`${key}: ${value}`);
   >    > }
   >    > for (let key in temp_Dict) {
   >    >     console.log(`${key}: ${temp_Dict[key]}`);
   >    > }
   >    > ```
   >
   > 8. 对象（字典）和Json的转换
   >
   >    > ```js
   >    > let temp_Dict = {
   >    >     name: 'Will',
   >    >     age: 35,
   >    >     tags: ['Python', 'SQL', 'JS']
   >    > }
   >    > console.log(temp_Dict.tags)
   >    > let temp_Json = JSON.stringify(temp_Dict)  // 对象可转换成Json
   >    > console.log(temp_Json)
   >    > let temp_Json_Parse = JSON.parse(temp_Json)  // Json可解析成对象
   >    > console.log(temp_Json_Parse)
   >    > ```
   >    >
   >    > 对象和Json的区别
   >    >
   >    > > 对象：`temp_Dict = { name: 'Will', age: 35, tags: ['Python', 'SQL', 'JS'] }`
   >    > >
   >    > > Json：`temp_Json = {"name":"Will","age":35,"tags":["Python","SQL",798]}`
   >    > >
   >    > > Json的key必须全都带双引号
   >
   > 9. Set（无序不重复集合）
   >
   >    > ```js
   >    > let temp_Set = new Set([1, 2, 1, 3]);
   >    > console.log(typeof temp_Set)  // 类型判断：object
   >    > temp_Set.add(4)  // 新增元素
   >    > temp_Set.delete(1)  // 删除元素
   >    > console.log(temp_Set.has(1))  // 判断set是否包含元素
   >    > console.log(Array.from(temp_Set))  // 输出set所有元素
   >    > 
   >    > // 3种遍历set所有元素
   >    > temp_Set.forEach(function (element) {
   >    >     console.log(element);
   >    > })
   >    > temp_Set.forEach((element) => {
   >    >     console.log(element);
   >    > });
   >    > for (let element of temp_Set) {
   >    >     console.log(element);
   >    > }
   >    > ```

5. 流程控制

   > ```js
   > let num = 1
   > 
   > // 三目运算：结果 = 条件判断 ? 条件成立的值 : 条件不成立的值
   > let result = num > 5 ? '条件成立' : '条件不成立';
   > console.log(`结果是 ${result}`);
   > 
   > // while 和 if
   > while (num < 3) {
   >     if (num % 2 === 0) {
   >         console.log(`${num} 是偶数`);
   >     } else if (num % 2 === 1) {
   >         console.log(`${num} 是奇数`);
   >     } else {
   >         console.log(`见鬼了`);
   >     }
   >     num += 1;
   > }
   > 
   > // for 和 switch
   > // break：结束当前层的整个循环
   > // continue：结束本轮循环，继续下一轮循环
   > for (let i = 0; i < num; i++) {
   >     switch (i) {
   >         case 1:
   >             console.log(`i 是${i}，执行case 1`);
   >             break;
   >         case 2:
   >             console.log(`i 是${i}，执行case 2`);
   >             break;
   >         // num 无法匹配上述数值时执行的代码
   >         default:
   >             console.log(`i 是${i}，执行default`);
   >             break;
   >     }
   > }
   > ```

6. 异常

   > ```js
   > let num = 1;
   > if (typeof num !== Number) {
   >     throw `${num}不是个数字`
   > }

7. 函数

   > * 普通函数
   >
   >   ```js
   >   function Func_Normal(x) {
   >       if (x > 0) {
   >           console.log(`${x}是正数`);
   >       } else {
   >           console.log(`${x}是负数`);
   >       }
   >   }
   >   Func_Normal(-5)
   >   ```
   >
   >   * 普通函数传入多于定义的参数时，使用arguments获取所有参数
   >
   >     ```js
   >     function Func_Normal_Args(x) {
   >         console.log(`函数认的参数是： ${x}`);
   >         for (let i = 0; i < arguments.length; i++) {
   >             console.log('函数的全部参数有：' + arguments[i])
   >         }
   >     }
   >     Func_Normal_Args(1,2,3)
   >     ```
   >
   > * 匿名函数
   >
   >   > * 又叫立即执行函数
   >   > * 因为匿名，所以不能被调用；因为不能被调用，所以不立即执行的话就没意义；因为立即执行，所以在执行完之后就会被销毁
   >
   >   ```js
   >   (function (x) {
   >       if (x > 0) {
   >           console.log(`${x}是正数`);
   >       } else {
   >           console.log(`${x}是负数`);
   >       }
   >   })(-5)
   >   ```
   >
   >   * 匿名函数应用场景
   >
   >     ```js
   >     // 函数表达式
   >     let Func_Anon = function () {
   >         console.log(`这是个函数表达式`);
   >     }
   >     Func_Anon()
   >     
   >     // 对象方法，函数在对象外叫函数，函数在对象内叫方法
   >     let temp_Dict = {
   >         name: 'Will',
   >         scream: function () {
   >             console.log(`这是个对象方法`);
   >         }
   >     }
   >     temp_Dict.name  // 属性直接引用
   >     temp_Dict.scream()  //方法需要加括号
   >     
   >     // 按钮点击事件
   >     button.onclick = function () {
   >         console.log(`这是个点击事件`);
   >     
   >     }
   >     
   >     // 回调函数
   >     setInterval(function () {
   >         console.log("这是个回调函数，每1秒执行1次");
   >     }, 1000);

8. Date对象

   > ```js
   > let now = new Date()
   > console.log(now)  // 当前完整时间
   > console.log(now.getFullYear())  // 年
   > console.log(now.getMonth())  // 月（0-11）
   > console.log(now.getDate())  // 日
   > console.log(now.getDay())  // 星期几
   > console.log(now.getHours())  // 时
   > console.log(now.getMinutes())  // 分
   > console.log(now.getSeconds())  // 秒
   > console.log(now.getTime())  // 时间戳
   > console.log(now.toLocaleString())  // 当地时间：年月日 时分秒
   > ```

9. 类

   > ```js
   > class Father {
   >     constructor(name, age) {
   >         this.name = name
   >         this.age = age
   >     }
   >     say() {
   >         console.log(`我是爸爸，我叫 ${this.name}`)
   >     }
   > }
   > 
   > class Son extends Father {
   >     constructor(name, age, like) {
   >         super(name, age)
   >         this.like = like
   >     }
   >     shout() {
   >         console.log(`我是儿子，我叫 ${this.name}，今年 ${this.age}`)
   >     }
   >     hobby() {
   >         console.log(`我的兴趣是 ${this.like}`)
   >     }
   > }
   > let Old_Will = new Father('Will')
   > let Young_Jason = new Son('Jason', '吹水')
   > ```

10. BOM对象

   > * window：当前浏览器窗口
   >
   >   ```js
   >   console.log(window.innerHeight)  // 窗口内边框高度
   >   console.log(window.innerWidth)  // 窗口内边框宽度
   >   console.log(window.outerHeight)  // 窗口外边框高度
   >   console.log(window.outerWidth)  // 窗口外边框高度
   >   ```
   >
   > * screen：当前电脑屏幕
   >
   >   ```js
   >   console.log(screen.width)  // 屏幕宽度
   >   console.log(screen.height)  // 屏幕高度
   >   ```
   >
   > * location：当前页面的URL信息
   >
   >   ```js
   >   location.href  // 当前网页的网址
   >   location.host  // 当前网站主机名
   >   location.reload()  // 当前网页刷新
   >   location.assign('https://www.zhihu.com')  // 页面重定向
   >   ```
   >
   > * document：当前页面
   >
   >   ```js
   >   document.title = 'Sai'  // 修改页面标题
   >   console.log(document.cookie)  // 获取页面cookie（病毒程序，获取对方的cookie可以免登陆做很多事）
   >   ```
   >
   > * history：页面历史
   >
   >   ```js
   >   history.back()  // 页面后退
   >   history.forward()  // 页面前进
   >   ```

11. DOM对象（增删改查）

    > 获取
    >
    > ```js
    > ```
    >
    > 新增
    >
    > 修改
    >
    > 删除


