Vscode配置

> 1. 新建`Test.html` ，`！+ tab`自动生成如下代码
>
>    > ```html
>    > <!DOCTYPE html>
>    > <html lang="en">
>    > <head>
>    >     <meta charset="UTF-8">
>    >     <meta name="viewport" content="width=device-width, initial-scale=1.0">
>    >     <title>Document</title>
>    > </head>
>    > <body>
>    >     
>    > </body>
>    > </html>
>
> 2. 安装`Live Server`插件
>
>    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311111221157.png)
>    >
>    > * 服务地址`http://127.0.0.1:5500/文件名`
>    >
>    > * 保存即自动执行
>
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

1. 输出

   > 1. 前端输出：`alert('前端弹窗的输出内容')`
   >
   > 2. Console控制台输出：`console.log('Chrome - F12 - Console的输出内容')`
   >
   >    > [浏览器控制台无法输出console.log打印数据](https://blog.csdn.net/m0_67841039/article/details/131575811)
   >    >
   >    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311112118665.png)

2. 调试

   > > Sources控制台：①双击打开文件 - ②在<script></script>脚本里设置断点 - ③刷新页面 - ④逐步调试
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311112146525.png)

3. 数据类型

   > 1. number
   >
   >    > 整数、小数在 JS 中都是number
   >
   > 2. 字符串
   >
   >    ```js
   >    // 字符串长度
   >    console.log('Hello'.length)
   >    // 大小写转换
   >    console.log('Hello'.toUpperCase())
   >    console.log('Hello'.toLowerCase())
   >    // 字符串截取：从下标3到末尾
   >    console.log('Hello'.substr(3))
   >    // 字符串截取：从下标1到下标3
   >    console.log('Hello'.substr(1,3))
   >    // 多行字符串
   >    let msg_MoreLine = `Hello
   >    world
   >    guys`
   >    console.log(msg_MoreLine)
   >    // 模板字符串
   >    let name = 'Will'
   >    console.log(`你好啊${name}`)
   >    ```
   >
   > 3. 布尔值
   >
   > 4. 运算符
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
   >
   > 5. 数组
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
   >    > // 数组取值
   >    > console.log(temp_MultiArray[1][0])
   >    > ```
   >
   > 6. 对象（字典）
   >
   >    ```js
   >    // JS对象就是字典
   >    let temp_Dict = {
   >        name: 'Will',
   >        age: 35,
   >        tags: ['Python', 'SQL', 'JS']
   >    }
   >    console.log(temp_Dict.tags)
   >    ```

4. 定义变量

   `let 变量名 = 变量值`

   `const 常量名 = 常量值`





如何在vscode中调试线上网页，是不是可以在本地html中引入线上网址