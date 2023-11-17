### XPath 入门

> XPath 是一门在 XML 文档中查找信息的**语言**，通过元素和属性进行导航，是一种路径语言
>
> 用法：网页中按 `F12` 进行元素检查，在源码标签上右键进入 `Copy` 操作，选择里面的 `Copy Xpath` 的选项，即可获得该元素的`Xpath`值
>
> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310101138890.png)

1. **Chrome调试**

   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310081842645.png)
   >
   > 格式：`$x('')`，如`$x('//*[@id="subBtn"]')`

2. **语法**

   > 1. 层级
   >    1. `/`：直接子级
   >    2. `//`：跳级
   > 2. 属性
   >    1. `@`：属性访问
   > 3. 函数
   >    1. contains()：包含
   >    2. not()：不包含
   >    3. text()：文本值
   >    4. starts-with()：以***开头

   **用法**

   > 1. 定位
   >
   >    1. 单一属性定位
   >
   >       `//div/a[@target='_blank']`
   >
   >       > 页面任何位置，所有`div`元素下，所有属性`target='_blank'`的子元素`a`
   >
   >    2. 多属性定位
   >
   >       `//div/a[@target="_blank" and @class="mnav"]`
   >
   >       > 页面任何位置，所有`div`元素下，所有属性`target='_blank'`且属性`class="mnav"`的子元素`a`
   >
   >    3. 借父节点定位
   >
   >       1. 不跳级定位
   >
   >          > `//div[@id="s-top-left"]/a`
   >          >
   >          > > 页面任何位置，所有属性`id="s-top-left"`的`div`元素下，所有子元素`a`（`/`表示仅包含子元素）
   >
   >       2. 跳级定位
   >
   >          > `//div[@id="s-top-left"]//a`
   >          >
   >          > > 页面任何位置，所有属性`id="s-top-left"`的`div`元素下，所有子孙元素`a`（`//`表示包含所有子孙元素）
   >
   >    4. 下标定位
   >
   >       `//div[@id="s-top-left"]/a[2]`
   >
   >       > 页面任何位置，所有属性`id="s-top-left"`的`div`元素下，第2个子元素`a`
   >
   >       `//div[@id="s-top-left"]/a[last()-2]`
   >
   >       > 页面任何位置，所有属性`id="s-top-left"`的`div`元素下，倒数第2个子元素`a`
   >
   >       `//div[@id="s-top-left"]/a[position()<3]`
   >
   >       > 页面任何位置，所有属性`id="s-top-left"`的`div`元素下，前2个子元素`a`
   >
   >    5. 文本定位
   >
   >       `//div/a[text()='hao123']`
   >
   >       > 页面任何位置，所有的`div`元素下，文本值为`hao123`的子元素`a`
   >
   >    6. 模糊定位
   >
   >       1. `contains()`
   >
   >          > `//div/a[contains(@href,'pan')]`
   >          >
   >          > >页面任何位置，所有的`div`元素下，属性`href`值包含`pan`的子元素`a`
   >          >
   >          > `//div/a[contains(text(),"史前")]`
   >          >
   >          > > 页面任何位置，所有的`div`元素下，文本值包含`史前`的子元素`a`
   >
   >       2. `starts-with()`
   >
   >          > `//div/a[starts-with(@data-nid,"news_850")]`
   >          >
   >          > >页面任何位置，所有的`div`元素下，属性`href`值以`news_850`开头的子元素`a`
   >          >
   >          > `//div/a[starts-with(text(),"史前")]`
   >          >
   >          > > 页面任何位置，所有的`div`元素下，文本值以`史前`开头的子元素`a`
   >
   >    7. ~~排除定位（not非常难处理，尽量不用）~~
   >
   >       1. ~~按属性排除~~
   >
   >          ~~`//aside[@class="_2OwGUo"]/*[not(@class="_3Z3nHf")]`~~
   >
   >          > ~~所有属性`class="_2OwGUo"`的元素`aside`下，排除属性`class="_3Z3nHf"`的元素~~
   >
   >       2. ~~按元素排除~~
   >
   >          ~~`//aside[@class="_2OwGUo"]/*[not(name()="div")]`~~
   >
   >          > ~~所有属性`class="_2OwGUo"`的元素`aside`下，排除所有`div`子元素~~
   >
   >          ~~`//aside[@class="_2OwGUo"]/*[not(name()="div" or not(name()="span"))]`~~
   >
   >          > ~~所有属性`class="_2OwGUo"`的元素`aside`下，排除所有`div`子元素和`span`子元素~~
   >
   >    8. 定位合并
   >
   >       `//div/a[text()='hao123'] | //div/a[contains(@href,'pan')]`
   >
   >       > 取并集，先列出`//div/a[text()='hao123']`，再列出`//div/a[contains(@href,'pan')]`
   >
   > 2. 取值
   >
   >    1. 取属性值
   >
   >       `//div/a/@href`
   >
   >       > 所有`div`元素下，所有子元素`a`的属性`href`的值（注意：是`div`元素的`href`属性，此处@后的反斜杠不是上下级关系)，结果如下
   >       >
   >       > ```bash
   >       > http://news.baidu.com
   >       > https://www.hao123.com?src=from_pc_logon
   >       > ```
   >
   >    2. 取元素的文本值
   >
   >       `//div/a/text()`
   >
   >       > 页面任何位置，所有`div`元素下，所有子元素a的文本值，结果如下
   >       >
   >       > ```bash
   >       > 新闻
   >       > hao123
   >       > ```

   **特殊定位案例**

   > 1. 获取具有属性`target`的所有`a`元素
   >
   >    `//a[@target]`
   >
   >    1. 获取定位元素的文本值
   >
   >       `//a[@target]/text()`
   >
   >    2. 获取定位元素的属性值
   >
   >       `//a[@target]/@target`
   >
   >       `//a[@target]/@class`
   >
   >       `//a[@target]/@href`
   >
   > 2. 获取没有属性`target`的所有`a`元素
   >
   >    `//a[not(@target)]`

   **案例**

   ```xml
   <?xml version="1.0" encoding="UTF-8"?>
   <bookstore>
       <book category="cooking">
           <title lang="en">Everyday Italian</title>
           <author>Giada De Laurentiis</author>
           <year>2005</year>
           <price>30.00</price>
       </book>
       <book category="web">
           <title lang="en">XQuery Kick Start</title>
           <author>James McGovern</author>
           <author>Per Bothner</author>
           <year>2003</year>
           <price>49.99</price>
       </book>
   </bookstore>
   ```

   ```python
   # 书店里所有书的作者名
   print(tree.xpath('//bookstore/book/author/text()'))
   # 书店里所有书的语言
   print(tree.xpath('//bookstore/book/title/@lang'))
   # 书店里第一本书的标题
   print(tree.xpath('//bookstore/book[1]/title/text()'))
   # 书店里最后一本书的标题
   print(tree.xpath('//bookstore/book[last()]/title/text()'))
   # 书店里倒数第2本书的标题
   print(tree.xpath('//bookstore/book[last()-1]/title/text()'))
   # 书店里前2本书的标题
   print(tree.xpath('//bookstore/book[position()<3]/title/text()'))
   # 书店所有分类是web的书的标题
   print(tree.xpath('//book[@category="web"]/title/text()'))
   # 书店所有价格大于30的书的价格
   print(tree.xpath('//book[price>35]/price/text()'))
   # 书店所有cover属性包含paper的书的标题
   print(tree.xpath('//book[contains(@cover,"paper")]/title/text()'))
   ```

   ```python
   from lxml import etree
   html = '''
   <div class="article">
       <div class="bd">
           <div id="showing-soon" class="tab-bd">
               <div class="item mod">
                   <a class="thumb" href="https://xxx/34834769/"></a>
                   <div class="intro">
                       <h3>
                           <a href="https://xxx/34834769/" class="">应承</a>
                       </h3>
                       <ul>
                           <li class="dt">02月24日</li>
                           <a class="trailer_icon">预告片</a>
                       </ul>
                   </div>
               </div>
               <div class="item mod odd">
                   <a class="thumb" href="https://xxx/25905044/"></a>
                   <div class="intro">
                       <h3>
                           <a href="https://xxx/25905044/" class="">刺猬索尼克</a>
                       </h3>
                       <ul>
                           <li class="dt">02月28日</li>
                           <a class="trailer_icon">预告片</a>
                       </ul>
                   </div>
               </div>
               <p>
                   <a href="https://xxx/coming">&gt; 查看全部即将上映的影片</a>
               </p>
           </div>
       </div>
   </div>
   '''
   
   tree = etree.HTML(html)
   print(type(tree))                            # <class 'lxml.etree._Element'>
   print(etree.tostring(tree, encoding='utf-8', pretty_print=True, method="html").decode('utf-8'))
   
   print('-'*20, '节点 <div id="showing-soon"> 的内容', '-'*20)
   div_1 = tree.xpath('//div[@id="showing-soon"]')
   print(type(div_1))                       # <class 'list'>
   print(type(div_1[0]))                    # <class 'lxml.etree._Element'>
   print(div_1)
   print(div_1[0])
   print(etree.tostring(div_1[0], encoding='utf-8', pretty_print=True, method="html").decode('utf-8'))
   
   print('-'*20, '节点 <div id="showing-soon"> 的第一个儿子节点 div 的内容', '-'*20)
   div_1_1 = tree.xpath('//div[@id="showing-soon"]/div')
   print(type(div_1_1))                          # <class 'list'>
   print(div_1_1)
   print(div_1_1[0])
   print(etree.tostring(div_1_1[0], encoding='utf-8', pretty_print=True, method="html").decode('utf-8'))
   
   print('-'*20, '节点 <div id="showing-soon"> 的所有儿子节点 div 的内容', '-'*20)
   div_1_1s = tree.xpath('//div[@id="showing-soon"]/div')
   print(div_1_1s)
   for div_1_1 in div_1_1s:
       print(type(div_1_1))                       # <class 'lxml.etree._Element'>
       print(div_1_1)
       print(etree.tostring(div_1_1, encoding='utf-8', pretty_print=True, method="html").decode('utf-8'))
       print('-'*50)
   
   print('-'*30, '综合上面的分析', '-'*30)
   div_1 = tree.xpath('//div[@id="showing-soon"]')
   div_1_1s = tree.xpath('//div[@id="showing-soon"]/div')
   print(div_1)
   print(div_1_1s)
   for div_1_1 in div_1_1s:
       print(div_1_1)
       print(etree.tostring(div_1_1, encoding='utf-8', pretty_print=True, method="html").decode('utf-8'))
   ```

   > 注 1
   >
   > > etree.HTML() 返回的是个 lxml.etree._Element，可以用 etree.tostring() 直接打印
   > > Xpath_Tree.xpath() 返回的是个 list，不可以用 etree.tostring() 直接打印，要用下标取其中的元素才能打印
   > > Xpath_Tree.xpath() 返回的 list 里面的元素是 lxml.etree._Element，可以用 etree.tostring() 直接打印
   >
   > 注 2
   >
   > > Xpath_Tree.xpath('//div[@id="showing-soon"]')返回的 list 只有 1 个元素
   > > Xpath_Tree.xpath('//div[@id="showing-soon"]/div') 返回的 list 有 2 个元素，[div1，div2]
   > > 遍历 [div1，div2] 即可
   >
   > * etree.HTML()：构造一个 XPath 解析对象并对 HTML 文本进行自动修正
   > * etree.tostring()：输出修正后的结果，类型是bytes
   > * xpath_html.xpath()：用于 xpath 定位
   >
   > > xpath 定位后打印 xml 字符串：print(etree.tostring(xpath_html.xpath('//li'), encoding='utf-8', pretty_print=True, method="html").decode('utf-8'))