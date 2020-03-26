# 爬虫前须知



### 前端基础

```html
<html> 声明 这是一个HTML文档
<head> 标签的头部
<body> body包含了N多组标签对
<a> 超链接 如果a标签后面跟着 href="任何链接" 说明<a>一定是链接
<p> 段落
<img> 图像
<input> 输入文本框
<form> 表单（包含多个input，一个button）
<title> 窗口的标题
<iframe> 框架 HTML中的框架
<div> 无名式 代表的是块级元素 div是一个容器 可以包含任意标签
<span> 无名式 代表的是块级元素 span是一个文本容器 可以包含任意标签
```

* HTML中的开始标签和结束标签之间的所有代码都是元素，元素有属性和属性值

```html
demo:
<input id="kw" name="wd" class="s_ipt" value="" maxlength="100" autocomplete="off">
```

> * id 是该元素中的一个属性 属性值是 kw 依此类推
> * 检查属性值的唯一性： f12 -->ctrl + f -->拷贝属性对应的属性值--复制到HTML中的文本框-->enter键查看该属性值是否在整个页面中是否唯一，**如果唯一就可以使用该元素去定位**



### Chrome 调试和抓包

![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200130134426.png)



**针对静态网页的数据**

1. 标记 2 是 **HTML 源码**

   > 每个标签都是 1 个 Dom 节点，所有标签组成 Dom 树

2. 标记 1 是  **元素选择器**

   > 开启元素选择器
   >
   > 1. 鼠标悬浮到左侧网页的指定元素时，Elements 会选中右侧 Dom 树中对应的 Dom 节点
   > 2. 鼠标悬浮到右侧 Dom 树中指定的 Dom 节点时，Elements 会选中左侧网页的对应元素

3. 标记 3 是   **对 Dom 节点的操作**

   > 1. 选择 1 个 Dom 时，左侧网页中的元素就会被阴影覆盖
   > 2. 修改 1 个 Dom 时，左侧网页中的元素就会实时显示
   > 3. 删除 1 个 Dom 时，左侧网页中的元素就会消失
   > 4. 例如 Copy outerHTML :  Copy 网页指定区域的代码块

4. 标记 4 是源码内的**搜索**功能，确认元素的时候用，**使用频率非常高**

5. 标记 5 是   **当前 Dom 节点的路径**

   > 单击路径中任何一个节点，即可以跳转到相应节点内容中去



![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200128205657.png)



**针对动态网页的数据**

1. Network 网络监控功能，即 **抓包**

2. **记录**：打开 **Network** 界面，开启 **记录**，然后 **刷新** 页面，就可以看到所有**发出的请求**，包括数据、JS、CSS、图片、文档等，从请求列表中可以寻找你的目标
3. **搜索**：打开 **搜索** 界面，直接对你的目标内容进行查找
4. **Preseve log** ：选中 **Preseve log** ，页面刷新之后，列表不会清空
5. **Filter **：打开 **Filter** 界面，可以按 **过滤类型** 和 **关键字** 筛选请求
6. **Request Header**：即 **抓包** 要抓的内容，请求头包含 **user-agent**、host、referer、**cookie** 等。其中 **cookie** 是用来识别请求者身份的关键信息，对于需要登录的网站，这个值少不了。而另外几项，也经常会被网站用来识别请求的合法性。同样的请求，浏览器里可以，程序里不行，多半就是 **Request Header** 信息不正确。可以从 Chrome 上把这些信息照搬到程序里，以此绕过对方的限制

**爬取网页之前先搞清楚**

1. 请求方式 Request Method

   > 拉勾网为了反爬，本来应该 **GET** 的地方，它用了 **POST**

2. 常用爬虫请求头 Request Header

   > * **User-Agent**
   > * **Referer**
   > * **Cookie**



### IPython 入门

1. 安装环境

   1. 切换到 `py3` 虚拟环境：`source activate py3`
   2. 查看当前环境是否已包含 `IPython` 模块：`conda list`
   3. 安装 `IPython` 模块：`pip install ipython`

2. 用法示例

   1. 对象内省

      > 对象内省：在变量名或命令的后面加 `?`，可显示该对象的通用信息，如对象类型、文档字符串等

      * 显示通用信息

        > ```
        > In [1]: import os
        >     ...: l = [2, 3, 4 ,5]
        > ```
        >
        > `l?`显示变量`l`的类型，内容
        >
        > ```
        > In [2]: l?
        > Type:        list
        > String form: [2, 3, 4, 5]
        > Length:      4
        > Docstring:
        > Built-in mutable sequence.
        > ```
        >
        > `os.listdir?`显示`os.listdir`的返回值
        >
        > ```
        > In [3]: os.listdir?
        > Signature: os.listdir(path=None)
        > Docstring:
        > Return a list containing the names of the files in the directory.
        > ```

      * 通配符*匹配

        > `os.*dir?`显示`os`模块中所有以`dir`结尾的方法
        >
        > ```
        > In [4]: os.*dir?
        > os.chdir
        > os.curdir
        > os.fchdir
        > os.listdir
        > os.mkdir
        > os.pardir
        > os.rmdir
        > os.scandir
        > ```
        >
        > `os.*dir*?`显示`os`模块中所有包含`dir`的方法
        >
        > ```
        > In [5]: os.*dir*?
        > os.__dir__
        > os.chdir
        > os.curdir
        > os.fchdir
        > os.listdir
        > os.makedirs
        > os.mkdir
        > os.pardir
        > os.removedirs
        > os.rmdir
        > os.scandir
        > os.supports_dir_fd
        > ```



