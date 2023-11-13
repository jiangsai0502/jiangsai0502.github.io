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
   >    > // 类型判断
   >    > console.log(typeof 1)  // number
   >    > console.log(typeof 1.1)  // number
   >
   > 3. 字符串
   >
   >    > ```js
   >    > // 类型判断
   >    > console.log(typeof 'Hello')  // string
   >    > // 字符串长度
   >    > console.log('Hello'.length)  // 5
   >    > // 大小写转换
   >    > console.log('Hello'.toUpperCase())  // HELLO
   >    > console.log('Hello'.toLowerCase())  // hello
   >    > // 字符串截取：从下标3到末尾
   >    > console.log('Hello'.substr(3))  // lo
   >    > // 字符串截取：从下标1到下标3
   >    > console.log('Hello'.substr(1,3))  // ell
   >    > // 多行字符串
   >    > let msg_MoreLine = `Hello
   >    > world
   >    > guys`
   >    > console.log(msg_MoreLine)
   >    > // 模板字符串
   >    > let name = 'Will'
   >    > console.log(`你好啊${name}`)  // 你好啊Will
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
   >    > // 数组取值
   >    > console.log(temp_Array[3])
   >    > // 数组长度
   >    > console.log(temp_Array.length)
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
   >    > // 数组截取：从下标3到末尾
   >    > console.log(temp_Array.slice(3))
   >    > // 数组截取：从下标1到下标3
   >    > console.log(temp_Array.slice(1, 3))
   >    > // 数组增加元素：头部增加多个元素
   >    > temp_Array.unshift(520, 123)
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
   >    > // 遍历对象
   >    > for (const [key, value] of Object.entries(temp_Dict)) {
   >    >     console.log(`${key}: ${value}`);
   >    > }
   >    > for (let key in temp_Dict) {
   >    >     console.log(`${key}: ${temp_Dict[key]}`);
   >    > }
   >    > ```
   >
   > 8. Set（无序不重复集合）
   >
   >    > ```js
   >    > let temp = new Set([1, 2, 1, 3]);
   >    > // 新增元素
   >    > temp.add(4)
   >    > // 删除元素
   >    > temp.delete(1)
   >    > // 判断set是否包含元素
   >    > console.log(temp.has(1));
   >    > // 输出set所有元素
   >    > console.log(Array.from(temp));
   >    > // 3种遍历set所有元素
   >    > temp.forEach(function (element) {
   >    >     console.log(element);
   >    > })
   >    > temp.forEach((element) => {
   >    >     console.log(element);
   >    > });
   >    > for (let element of temp) {
   >    >     console.log(element);
   >    > }
   >    > ```

5. 流程控制

   > ```js
   > let num = 1
   > 
   > // 三目运算：结果 = 条件判断 ？ 条件成立的值 : 条件不成立的值
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

   > > 对象外叫函数，对象内叫方法
   >
   > ```js
   > // 普通函数
   > function Func_Normal(x) {
   >     if (x > 0) {
   >         console.log(`${x}是正数`);
   >     } else {
   >         console.log(`${x}是负数`);
   >     }
   > }
   > Func_Normal(-5)
   > // 普通函数超标传参
   > function Func_Normal_Args(x) {
   >     console.log(`函数认的参数是： ${x}`);
   >     for (let i = 0; i < arguments.length; i++) {
   >         console.log('函数的全部参数有：' + arguments[i])
   >     }
   > }
   > Func_Normal_Args(1,2,3)
   > ```
   >
   > >匿名函数又叫立即执行函数；因为匿名，所以不能被调用；因为不能被调用，所以不立即执行的话就没意义；因为立即执行，所以在执行完之后就会被销毁
   >
   > ```js
   > // 匿名函数
   > (function (x) {
   >     if (x > 0) {
   >         console.log(`${x}是正数`);
   >     } else {
   >         console.log(`${x}是负数`);
   >     }
   > }
   > )(-5)
   > // 匿名函数应用场景
   > // 函数表达式
   > let Func_Anon = function () {
   >     console.log(`这是个函数表达式`);
   > }
   > Func_Anon()
   > // 对象方法
   > let temp_Dict = {
   >     name: 'Will',
   >     scream: function () {
   >         console.log(`这是个对象方法`);
   >     }
   > }
   > temp_Dict.scream()
   > // 按钮点击事件
   > button.onclick = function () {
   >     console.log(`这是个点击事件`);
   > 
   > }
   > // 回调函数
   > setInterval(function () {
   >     console.log("这是个回调函数，每1秒执行1次");
   > }, 1000);
   > ```

8. BOM

   > ```js
   > // window：当前浏览器窗口
   > // 窗口内边框高度
   > console.log(window.innerHeight)
   > // 窗口内边框宽度
   > console.log(window.innerWidth)
   > // 窗口外边框高度
   > console.log(window.outerHeight)
   > // 窗口外边框高度
   > console.log(window.outerWidth)
   > 
   > // screen：当前电脑屏幕
   > // 屏幕宽度
   > console.log(screen.width)
   > // 屏幕高度
   > console.log(screen.height)
   > 
   > // location：当前页面的URL信息
   > // 页面重定向
   > // location.assign('https://www.zhihu.com/question/23498580')
   > ```

9. DOM

   > ```js
   > ```
   >
   > 


