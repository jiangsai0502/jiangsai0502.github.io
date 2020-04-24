

### Requests + XPath

**爬取豆瓣电影信息源码**

```python
import requests
from lxml import etree

def GetXpathTree(url):
    fake_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
    }
    response = requests.get(url, headers=fake_headers)
    html = response.content.decode('utf-8')
    XpathTree = etree.HTML(html)
    # print(XpathTree.xpath('//*[@id="showing-soon"]/div[1]/div/h3/a/text()'))
    return XpathTree

def GetBigData(XpathTree):

    div_id_showing_soon = XpathTree.xpath('//*[@id="showing-soon"]')[0]
    bigData = []
    # 用 try except 是因为有的节点不存在，直接匹配会报异常
    for div_class_item_mod in div_id_showing_soon:
        try:
            data = {}
            data['影名'] = div_class_item_mod.xpath('./div/h3/a/text()')[0]
            data['日期'] = div_class_item_mod.xpath('./div/ul/li[1]/text()')[0]
            data['类型'] = div_class_item_mod.xpath('./div/ul/li[2]/text()')[0]
            data['地区'] = div_class_item_mod.xpath('./div/ul/li[3]/text()')[0]
            data['热度'] = div_class_item_mod.xpath('./div/ul/li[4]/span/text()')[0]
            bigData.append(data)
        except:
            pass
    return bigData

if __name__ == "__main__":
    url = "https://movie.douban.com/cinema/later/chengdu/"
    XpathTree = GetXpathTree(url)
    bigData = GetBigData(XpathTree)
    print(bigData)
```

> > 所有的 xpath 都是网页中按 `F12` 进行元素检查，在源码标签上右键进入 `Copy` 操作，选择里面的 `Copy Xpath` 的选项
>
> 1. 囊括所有电影的父节点的 xpath 是 //\*[@id="showing-soon"]
>
> 2. 每部电影的节点的 xpath
>
>   3. 影名的 xpath 是 //\*[@id="showing-soon"]/div[1]/div/h3/a
>   4. 日期 的 xpath 是 //\*[@id="showing-soon"]/div[1]/div/ul/li[1]
>   5. 类型的 xpath 是 //\*[@id="showing-soon"]/div[1]/div/ul/li[2]
>   6. 地区 的 xpath 是 //\*[@id="showing-soon"]/div[1]/div/ul/li[3]
>   7. 热度的 xpath 是 //\*[@id="showing-soon"]/div[1]/div/ul/li[4]/span
>
> 8. 按层级获取节点
>
>   > 层级关系：div_id_showing_soon -> div_class_item_mod -> div_class_intro -> h3 -> a
>   >
>   > 
>   >
>   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200202013058.png)
>   >
>   > 
>   >
>   > **对应程序中的变量**
>   >
>   > **div_id_showing_soon 就是 \<div id="showing-soon" class="tab-bd">**
>   >
>   > **div_class_item_mod 就是 \<div class="item mod ">**
>
>     1. div_id_showing_soon = XpathTree.xpath('//*[@id="showing-soon"]')[0]
>     2. div_class_item_mod = div_id_showing_soon.xpath('./div')[0]
>     3. div_class_intro = div_class_item_mod.xpath('./div')[0]
>     4. h3 = div_class_intro.xpath('./h3')[0]
>     5. a = h3.xpath('./a')[0]
>     6. a_text = h3.xpath('./a/text()')[0]
>
> > 打印节点的两种方式
> >
> > print(div_id_showing_soon)
> >
> > print(etree.tostring(div_id_showing_soon, encoding='utf-8', pretty_print=True, method="html").decode('utf-8'))



**爬站长之家的美女图片**

```python
from lxml import etree
import time, os, requests

def GetXpathTree(url, url_er, page):
    if page == 1:
        url = url
    else:
        url = url_er.format(page)

    fake_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
    }

    response = requests.get(url, headers=fake_headers)
    html = response.content.decode('utf-8')
    XpathTree = etree.HTML(html)
    return XpathTree

def GetImgData(XpathTree):

    ImgData = {}
    # 获取所有的图片的 img地址 和 alt名称
    image_src_list = XpathTree.xpath('//div[@id="container"]//img/@src2')
    image_alt_list = XpathTree.xpath('//div[@id="container"]//img/@alt')
    ImgData['image_src_list'] = image_src_list
    ImgData['image_alt_list']= image_alt_list
    return ImgData

def DownLoadImg(ImgData):

    image_src_list = ImgData['image_src_list']
    image_alt_list = ImgData['image_alt_list']

    for each_image_src in image_src_list:

        Img_Folder_Name = 'DownLoadImgFolder'
        if not os.path.exists(Img_Folder_Name):
            os.mkdir(Img_Folder_Name)
        Img_Name = image_alt_list[image_src_list.index(each_image_src)]

        Img_Suffix = each_image_src.split('.')[-1]
        Img_Name = Img_Name + '.' + Img_Suffix
        relative_file_path = os.path.join(Img_Folder_Name, Img_Name)
        
        print('正在下载%s。。。。。。' % Img_Name)

        img_byte = requests.get(each_image_src)
        with open(relative_file_path, 'wb') as img_file:
            img_file.write(img_byte.content)
        
        print('结束下载%s' % Img_Name)
        time.sleep(2)

if __name__ == '__main__':
    start_page = 2
    end_page = 2
    url = 'http://sc.chinaz.com/tag_tupian/YaZhouMeiNv.html'
    url_er = 'http://sc.chinaz.com/tag_tupian/yazhoumeinv_{}.html'
    for page in range(start_page, end_page + 1):
        print('正在下载第%s页。。。。。。' % page)
        XpathTree = GetXpathTree(url, url_er, page)
        ImgData = GetImgData(XpathTree)
        DownLoadImg(ImgData)
        print('结束下载第%s页' % page)
        time.sleep(2)
```

> **问题：爬取页面和审查元素获取的内容不一致** 
>
> * 右键`检查` -> `copy`  -> `copy XPath` 得到图片的 XPath 路径是 //\*[@id="container"]/div[7]/div/a/img
>
> * 打印图片地址，即属性 `src` 的值看下
>
>   * `src_attr = XpathTree.xpath('//*[@id="container"]/div[7]/div/a/img/@src')`
>
>   * `print(src_attr)`
>
>   * `print(etree.tostring(src_attr[0], encoding='utf-8', pretty_print=True, method="html").decode('utf-8'))`
>
>     > 第 1 个 print 是列表为空，说明没找到元素
>
> *问题排查*
>
> 1. 打印 `src` 属性所在 `img` 标签的全部内容看看
>
>    * `img_tag = XpathTree.xpath('//*[@id="container"]/div[7]/div/a/img')`
>    * `print(img_tag)`
>
>    * `print(etree.tostring(img_tag[0], encoding='utf-8', pretty_print=True, method="html").decode('utf-8'))`
>
> 2. 发现 `img` 标签是
>
>    `<img src2="http://pic1.sc.chinaz.com/Files/pic/pic9/201912/zzpic21744_s.jpg" alt="亚洲高清美女写真图片">`
>
> 3. `img` 标签里居然没有 `src` 属性，而是 `src2`
>
> 4. 网页上右键，审查网页源代码发现，图片的属性果然是 `src2`，难怪抓取不到
>
> *原因分析*
>
> 1. 右键“审查网页源代码” 看到的是服务端最初发给浏览器的
> 2. HTML 代码右键“检查” 看到的是最初的 HTML 代码 + JavaScript 动态生成的代码
> 3. 若最初的 HTML 代码 被 JavaScript 改变了，则 右键“审查网页源代码” 和 右键“检查” 就不一致了
> 4. 现在的情况是， ，copy XPath 拿到的是 JavaScript 改变后的代码，因此就解析不到 src2 了
>
> 未来如何避免
>
> > 凡是右键`检查` -> `copy`  -> `copy XPath` 得到的 XPath 路径使用代码找不到这个元素
>
> 1. 查它的父节点
>    1. 使用 `etree.tostring()` 打印它的父节点的 XML 源码
>    2. 排查这个节点在父节点中的信息有何不同
>    3. 若父节点也找不到，则查父节点的父节点，依次类推
> 2. 右键“审查网页源代码” ，因为requests 获取的是网页源码跟这个是一致的





### Requests + BeautifulSoup

**爬取豆瓣电影信息**

> **目的**：获取[豆瓣电影](https://movie.douban.com/cinema/later/chengdu/)页面电影列表的名字、详情链接、上映时间、影片类型、地区、关注者数量
>
> [原教程](https://www.jianshu.com/p/c64fe2a20bc9)

#### 思路

##### 1. 分析网页

> 这一步非常重要，直接影响了我们能不能提取到我们想要的内容。

![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200116103822.png)

* 找到网页中的第一个电影的名字，**鼠标指向该名字**，点击右键，选择"检查"，页面上会打开"开发者工具"窗口，焦点会定位到电影名字
* 当鼠标划到图片中的\<ul>...\</ul>标签的时候，"复仇者联盟"的详细信息被选中了。
* 当鼠标划到下一个\<div class="item mod odd">...\</div>的时候，下一个影片"战犬瑞克斯"的所有信息被选中了。
* 当鼠标划到图片上方的\<div id="showing-soon" class="tab-bd">的时候，整个网页中我们需要采集的影片信息都被选中了。

***这几个动作说明***

> 1.我们需要的内容全都在\<div id="showing-soon" class="tab-bd">...\</div>里面。  
> 2.每个影片的信息，都在一个\<div class="item mod odd">...\</div>或者\<div class="item mod">...\</div>里面。画面左边的影片没有odd属性，右边的有odd属性(这好像对于我们采集信息没啥用)。

##### 2. 制订提取策略

1. 先找到囊括了所有的影片的最大的div
2. 再从最大的div里找到每一个影片的div
3. 最后从每个影片的div里面解析出来我们需要的名字、链接等等信息

![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200116124725.png)

从上图得知目标位置

| 电影属性   | 源码中的位置                               |
| ---------- | ------------------------------------------ |
| 电影名     | 在第 2 个\<a>标签里面                      |
| 链接       | 在第 1 个和第 2 个\<a>标签的 href 属性里面 |
| 上映日期   | 在第 1 个\<li>标签里面                     |
| 类型       | 在第 2 个\<li>标签里面                     |
| 地区       | 在第 3 个\<li>标签里面                     |
| 关注者数量 | 在第 4 个\<li>标签里面                     |

##### 3. 获取目标内容方式

1. 电影名：先获取所有的\<a>标签，再取第二个\<a>标签的 text
2. 链接：利用上一步获取的所有标签，取第二个\<a>标签的href属性
3. 其他信息：先获取所有的\<li>标签，再依次取出里面的text的值就是我们所需要的目标，上映日期，类型，地区等等



#### 最终源码及分析

```python
import requests
from bs4 import BeautifulSoup
import csv

from pyecharts import options as opts
from pyecharts.charts import Bar
from pyecharts.commons.utils import JsCode

# 空类的作用是存数据
class Data():
    pass

def GetSoup(url):
    # 伪装成浏览器的header
    fake_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
    }
    response = requests.get(url, headers=fake_headers)
    html = response.content.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def GetBigData(soup):
    # 先找到最大的 div
    all_movies = soup.find('div', id="showing-soon", class_="tab-bd")
    bigData = []
    # 逐个取出每一个电影的 div
    for each_movie in all_movies.find_all('div', class_="item", limit = 2):
        # 定义一个存放每一个电影信息的空类
        data = Data()
        
        # 先获取所有的<a>标签
        all_a_tag = each_movie.find_all('a')
        # 再取第二个<a>标签的 text，即电影名
        data.movie_name = all_a_tag[1].text
        # 再取第二个<a>标签的 'href'属性，即电影链接
        data.moive_href = all_a_tag[1]['href']

        # 先获取所有的<li>标签
        all_li_tag = each_movie.find_all('li')
        # 再取第二个<li>标签的 text，即日期
        data.movie_date = all_li_tag[0].text
        data.movie_type = all_li_tag[1].text
        data.movie_area = all_li_tag[2].text
        data.movie_lovers = all_li_tag[3].text.replace('人想看', '')
        
        bigData.append(data)
    return bigData

def PrintBigData(bigData):
    for data in bigData:
        print(f'名字：{data.movie_name}\n 链接：{data.moive_href}\n 日期：{data.movie_date}\n 类型：{data.movie_type}\n 地区：{data.movie_area}\n 关注者：{data.movie_lovers}\n')

def WriteToTxt(bigData):
    with open('/Users/jiangsai02/Documents/Temp/WebCrawler.txt', 'w') as OpenTxt:
        for data in bigData:
            for each_key,each_value in data.__dict__.items():
                OpenTxt.write(f'{each_key}:{each_value}\n')
            OpenTxt.write('\n')

def WriteToHtml(bigData):
    html_begin = ("""
                <!DOCTYPE html>
                <html>
                <head>
                    <meta charset="UTF-8">
                    <title>豆瓣电影即将上映影片信息</title>
                    <link href="https://cdn.bootcss.com/bootstrap/4.0.0/css/bootstrap.min.css" rel="stylesheet">
                </head>
                <body>
                <h2 class="text-center">豆瓣电影即将上映影片信息</h2>
                <table class="table table-striped table-hover mx-auto text-center">
                    <thead>
                        <tr>
                            <th>影片名</th>
                            <th>上映日期</th>
                            <th>影片类型</th>
                            <th>地区</th>
                            <th>关注者数量</th>
                        </tr>
                    </thead>
                    <tbody>
                """)
    html_end = ("""
                    </tbody>
                </table>
                </body>
                </html>
                """)
    def each_movie_info(data):
        movie_info = (f"""
                        <tr>
                            <td><a href="{data.moive_href}">{data.movie_name}</a></td>
                            <td>{data.movie_date}</td>
                            <td>{data.movie_type}</td>
                            <td>{data.movie_area}</td>
                            <td>{data.movie_lovers}</td>
                        </tr>
                    """)
        return movie_info
    with open('/Users/jiangsai02/Documents/Temp/WebCrawler.html', 'w') as OpenHtml:
        OpenHtml.write(html_begin)
        for data in bigData:
            html_movie_info = each_movie_info(data)
            OpenHtml.write(html_movie_info)
        OpenHtml.write(html_end)

def WriteToCSV(bigData):
    with open('/Users/jiangsai02/Documents/Temp/WebCrawler.csv', 'w', encoding="gbk", newline='') as OpenCSV:
        CSVwriter = csv.writer(OpenCSV)
        CSVwriter.writerow(["影片名", "链接", "上映日期", "影片类型", "地区", "关注者"])
        for data in bigData:
            CSVwriter.writerow([data.movie_name, data.moive_href, data.movie_date, data.movie_type, data.movie_area, data.movie_lovers])

def WriteToExcel(bigData):
    MyWB = Workbook()
    MyWS = MyWB.active
    MyWS.title = "TempData"
    # 将 bigData 的第一个 data 字典的键设置为 Excel 第 1 行的表头
    MyWS.append(list(bigData[0].keys()))
    for data in bigData:
        MyWS.append(list(data.values()))
    MyWB.save('/Users/jiangsai02/Documents/Temp/test.xlsx')
            
def TransToChart(bigData):
    sorted_bigData = sorted(bigData, key = lambda data: int(data.movie_lovers))
    all_names = [i.movie_name for i in sorted_bigData]
    all_lovers = [i.movie_lovers for i in sorted_bigData]
    
    def bar_base() -> Bar:
        c = (
            Bar()
            .add_xaxis(all_names)
            .add_yaxis("受欢迎度", all_lovers)
            .set_global_opts(title_opts=opts.TitleOpts(title="电影关注者排行榜"))
        )
        return c
    bar_base().render('Chart_Bar1.html')

    def bar_border_radius():
        c = (
            Bar()
            .add_xaxis(all_names)
            .add_yaxis("受欢迎度", all_lovers, category_gap="60%")
            .set_series_opts(itemstyle_opts={
                "normal": {
                    "color": JsCode("""new echarts.graphic.LinearGradient(0, 0, 0, 1, [{
                        offset: 0,
                        color: 'rgba(0, 244, 255, 1)'
                    }, {
                        offset: 1,
                        color: 'rgba(0, 77, 167, 1)'
                    }], false)"""),
                    "barBorderRadius": [30, 30, 30, 30],
                    "shadowColor": 'rgb(0, 160, 221)',
                }})
            .set_global_opts(title_opts=opts.TitleOpts(title="电影关注者排行榜"))
        )
        return c
    bar_border_radius().render('Chart_Bar2.html')            

if __name__ == "__main__":
    url = "https://movie.douban.com/cinema/later/chengdu/"
    soup = GetSoup(url)
    bigData = GetBigData(soup)
    PrintBigData(bigData)
    WriteToTxt(bigdata)
    WriteToHtml(bigdata)
    WriteToCSV(bigData)
    TransToChart(bigData)
```

> 1. GetSoup(url)：网页转换成 BeautifulSoup 对象
>
>    > 这是个通用方法，以后直接用即可
>
> 2. GetBigData(soup)：从 BeautifulSoup 对象中获取目的数据
>
>    > 这是整个程序的关键，具体分析可往上翻分析策略
>    >
>    > 创建一个空类，作用是存数据，python是动态语言，可以定义空类后，用的时候再临时增加字段，炒鸡好用
>    >
>    > ```python
>    > class Data():
>    > pass
>    > ```
>
> 3. PrintBigData(bigData)：打印目的数据，判断是否遗漏
>
> 4. WriteToTxt(bigdata)：用法见下方 **读写 TXT**
>
> 5. WriteToHtml(bigdata)：写入html
>
>    > html 是拼接的
>
> 6. WriteToCSV(bigData)：用法见下方 **读写 CSV**
>
> 7. TransToChar(bigData)：将数据转成图表
>
>    > 1. 安装pyecharts：pip install pyecharts （不能pip3 install pyecharts，否则出错）
>    >
>    > 2. 用法参照 [pyecharts图表](https://pyecharts.org/#/zh-cn/intro)
>    >
>    > 3. 引入相关模块
>    >
>    >    ```python
>    >    from pyecharts import options as opts
>    >    from pyecharts.charts import Bar
>    >    from pyecharts.commons.utils import JsCode
>    >    ```
>    >
>    > 4. 使用 sorted(iterable, cmp=None, key=None, reverse=False) 按照 movie_lovers 排序，得到一个有序的bigdata
>    >
>    >    ```python
>    >    sorted_bigData = sorted(bigData, key = lambda data: int(data.movie_lovers))
>    >    ```
>    >
>    >    > 1. bigData 必须是可迭代对象
>    >    > 2. data 是迭代对象的元素
>    >
>    > 5. 图表的简单用法
>    >
>    >    **官网Demo**
>    >
>    >    ```python
>    >    def bar_base() -> Bar:
>    >        c = (
>    >            Bar()
>    >            .add_xaxis(Faker.choose())
>    >            .add_yaxis("商家A", Faker.values())
>    >            .add_yaxis("商家B", Faker.values())
>    >            .set_global_opts(title_opts=opts.TitleOpts(title="Bar-基本示例", subtitle="我是副标题"))
>    >        )
>    >        return c
>    >    ```
>    >
>    >    **我的修改**
>    >
>    >    ```python
>    >    def bar_base() -> Bar:
>    >        c = (
>    >            Bar()
>    >            .add_xaxis(all_names)
>    >            .add_yaxis("受欢迎度", all_lovers)
>    >            .set_global_opts(title_opts=opts.TitleOpts(title="电影关注者排行榜"))
>    >        )
>    >        return c
>    >    bar_base().render('Chart_Bar.html')
>    >    ```
>    >
>    >    > 1. A().b().c() 这种写法是链式调用
>    >    >
>    >    > 2. add_xaxis(Faker.choose())
>    >    >
>    >    >    > add_xaxis 表示 x 轴，Faker.choose() 是个 list，表示 x 轴上的值
>    >    >
>    >    > 3. add_yaxis("商家A", Faker.values())
>    >    >
>    >    >    > add_yaxis 表示 y 轴，"商家A" "商家B" 表示有两组数据，Faker.values() 是个 list，表示 y 轴上的值
>    >    >
>    >    > 4. set_global_opts(title_opts=opts.TitleOpts(title="电影关注者排行榜"))
>    >    >
>    >    >    >  设置表名
>    >    >
>    >    > 5. bar_base().render('Chart_Bar1.html')
>    >    >
>    >    >    >  <类名>.render('路径及文件名.html')



**豆瓣电影 Top 250**

1. 探索网页获取规则**

   * 每页25部电影，共10页，因此要分析每一页的地址规则

     ```html
     第1页：https://movie.douban.com/top250
     第2页：https://movie.douban.com/top250?start=25&filter=
     第3页：https://movie.douban.com/top250?start=50&filter=
     第4页：https://movie.douban.com/top250?start=75&filter=
     ```

   * start 的参数是0, 25, 50, 75 . . . 225，可用 range(0, 250, 25) 

     

2. **探索每个页面的信息获取规则**

   * 鼠标悬停在某个电影名称上，右键 '检查' ，发现该电影的相关信息在一个 **\<div class="info"> ... \</div>** 中，而 **\<div class="info"> ... \</div>** 在一个 **\<div class="item"> ... \</div>** 中，每一部电影占据唯一一个  **\<div class="info"> ... \</div>** ，而一个 **\<div class="info"> ... \</div>** 占据唯一一个  **\<div class="item"> ... \</div>** ，所有电影的外面一层是  **\<ol class="grid_view"> ... \</ol>** 

     **整理思路**

   * 所有电影都在 **ol** 标签中，**ol** 的子标签是每部电影所在的 **li** 标签

   * 每个 **li** 中只有一个 **div**，每个 **div** 中有2个 **div**，其中第 2 个 **div**，即 **\<div class="info">** 才有目的信息

   * **\<div class="info">** 中有 2 个 div：**\<div class="hd">** 和 **\<div class="bd">**

   * **\<div class="hd">** 包含 片名，别名；**\<div class="bd">** 包含 人员，评分，短简介

     > ```html
     > <ol class="grid_view">
     > 	<div class="item">
     > 		<div class="info">
     > 		...
     > 		</div>
     > 	</div>
     > 	<div class="item">
     > 		<div class="info">
     > 		...
     > 		</div>
     > 	</div>
     > </ol>
     > ```

     > ```html
     > <div class="item">
     > 	<div class="info">
     > 		<div class="hd">
     > 			<a href="https://movie.douban.com/subject/3008247/" class="">
     > 			<span class="title">穿条纹睡衣的男孩</span>
     > 			<span class="title">&nbsp;/&nbsp;The Boy in the Striped Pajamas</span>
     > 			<span class="other">&nbsp;/&nbsp;穿条纹衣服的男孩  /  穿条纹衣的男孩</span>
     > 			</a>
     > 			<span class="playable">[可播放]</span>
     > 		</div>
     > 		<div class="bd">
     > 			<p class=""> 导演: 马克·赫尔曼 Mark Herman&nbsp;&nbsp;&nbsp;主演: 阿萨·巴特菲尔德 
     > 				<br> 2008&nbsp;/&nbsp;英国 美国&nbsp;/&nbsp;剧情 战争
     > 			</p>
     > 			<div class="star">
     > 				<span class="rating45-t"></span>
     > 				<span class="rating_num" property="v:average">9.1</span>
     > 				<span property="v:best" content="10.0"></span>
     > 				<span>303601人评价</span>
     > 			</div>
     > 			<p class="quote">
     > 				<span class="inq">尽管有些不切实际的幻想，这部电影依旧是一部感人肺腑的佳作。</span>
     > 			</p>
     > 		</div>
     > 	</div>
     > </div>
     > ```

   

3. **源码**

   * 先从一个网页开始爬取，将思路落实成代码，跑通后再扩展到更多页面

     ```python
     import requests
     from bs4 import BeautifulSoup
     
     def GetSoup(url):
         fake_headers = {
         'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
         }
         response = requests.get(url, headers=fake_headers)
         html = response.content.decode('utf-8')
         soup = BeautifulSoup(html, 'html.parser')
         return soup
     
     def GetBigData(soup):
         
         # 先找到 ol 标签
         all_movies = soup.find('ol', class_="grid_view")
         # 每部电影都是一个 Data 类，所有电影都放在 bigData 列表中
         bigData = []
     
         # 逐个取出每一个电影的 div
         for each_movie in all_movies.find_all('div', class_="info", limit = 20):
     
             # 声明一个存放每一个电影信息的空字典
             data = {}
     
             # 按标签层级搜索的第 1 种方式
             hd_tag = each_movie.find('div', class_="hd")
             data['电影名'] = hd_tag.find('a').find_all('span', class_="title")[0].text
             data['电影别名'] = hd_tag.find('a').find('span', class_="other").text
     
             bd_tag = each_movie.find('div', class_="bd")
             data['相关人员'] = bd_tag.find('p').text.replace(" ","").replace("\n", "")
             data['评分'] = bd_tag.find('div', class_="star").find('span', class_="rating_num", property="v:average").text
             data['评分人'] = bd_tag.find('div', class_="star").find_all('span')[3].text
             data['短简介'] = bd_tag.find('p', class_="quote").find('span', class_="inq").text
     
             bigData.append(data)
         return bigData
     
     def PrintBigData(bigData):
         for data in bigData:
             for each_key,each_value in data.items():
                 print(f'{each_key}:{each_value}')
             print('-'*30)
                 
     def JoinUrl(url):
         urls = []
         for start in range(0, 25, 25):
             new_url = f'{url}{start}'
             urls.append(new_url)
         return urls
     
     if __name__ == "__main__":
         Original_Url = "https://movie.douban.com/top250?start="
         Join_Urls = JoinUrl(Original_Url)
         for each_url in Join_Urls:
             soup = GetSoup(each_url)
             bigData = GetBigData(soup)
             PrintBigData(bigData)
     ```

4. **GetBigData(soup) 方法的改进**

   > BeautifulSoup 标签取值的优化

   ```python
   # 按标签层级搜索的第 1 种方式
   hd_tag = each_movie.find('div', class_="hd")
   data.movie_name = hd_tag.find('a').find_all('span', class_="title")[0].text
   data.movie_other_name = hd_tag.find('a').find('span', class_="other").text
   
   bd_tag = each_movie.find('div', class_="bd")
   data.staff = bd_tag.find('p').text.replace(" ","").replace("\n", "")
   data.score = bd_tag.find('div', class_="star").find('span', class_="rating_num", property="v:average").text
   data.score_rater = bd_tag.find('div', class_="star").find_all('span')[3].text
   data.intro = bd_tag.find('p', class_="quote").find('span', class_="inq").text
   
   # 按标签层级搜索的第 2 种方式
   hd_tag = each_movie.find('div', class_="hd")
   data.movie_name = hd_tag.a.find('span', class_="title").text
   data.movie_other_name = hd_tag.a.find('span', class_="other").text
   
   bd_tag = each_movie.find('div', class_="bd")
   data.staff = bd_tag.p.text.replace(" ","").replace("\n", "")
   data.score = bd_tag.div.find('span', class_="rating_num", property="v:average").text
   data.score_rater = bd_tag.div.find_all('span')[3].text
   data.intro = bd_tag.find('p', class_="quote").span.text
   
   # 因为 Beautifulsoup 是从当前标签一层一层往下搜索，因此只要目的标签是唯一的，不必拘泥于一定要按部就班地，第一层.第二层.第三层，完全可以跳着来，也完全不必把属性信息都写上
   data.movie_name = hd_tag.span.text
   data.movie_name = hd_tag.find_all('span')[0].text
   data.movie_name = each_movie.find('span', class_="title").text
   
   data.movie_other_name = hd_tag.find('span', class_="other").text
   data.movie_other_name = each_movie.find('span', class_="other").text
   
   bd_tag = each_movie.find('div', class_="bd")
   
   data.staff = bd_tag.p.text
   data.staff = bd_tag.find('p').text
   data.staff = each_movie.p.text
   data.staff = each_movie.find('p').text
   
   data.score = bd_tag.find('span', class_="rating_num").text
   data.score_rater = bd_tag.find_all('span')[3].text
   data.score = each_movie.find('span', class_="rating_num").text
   
   data.intro = bd_tag.find('p', class_="quote").span.text
   data.intro = bd_tag.find_all('span')[4].text
   data.intro = bd_tag.find('span', class_="inq").text
   data.intro = each_movie.find('span', class_="inq").text
   ```



### 2018年北京房价均价

1. **源码**

   ```python
   def GetBigData(soup):
       items = soup.find('table', class_="house-table").tbody
       bigData = []
       # for each_item in items.find_all('tr'):
       for each_item in items.find_all('tr', limit = 2):
           data = {}
           data['月份'] = each_item.find_all('td')[0].text
           data['价格'] = int(each_item.find_all('td')[1].text.replace('元/㎡',''))
           rate = each_item.span.text.replace('↓','').replace('↑','').replace('%','')
           expr_Decision_Making = lambda rate : '跌' if '-' in rate else '涨'
           data['涨跌'] = expr_Decision_Making(rate)
           data['百分比'] = float(rate.replace('-',''))
           bigData.append(data)
       return bigData
   
   Url = "https://zhinan.qianzhan.com/fangjia/2018_1_1096_0_0.html"
   ```

   > 1. 字符串替换最好用replace()，因为写下来就是为了将来忘记时翻看，因此可读性是最先考虑的，正则效率高，可读性低
   > 2. lambda 表达式使用一行代码构造一个函数方法，最好用于 if ... else 判断
   > 3. 涨跌比率的格式是，'0.45%↑'  ,  '-0.45%↓'  ，因此，用 lambda 表达式去掉负号，并将 '↑' ''↓' 替换成  '涨' ''跌'



### B站搜索结果

1. **源码**

   ```python
   def GetBigData(soup):
       items = soup.find('ul', class_="video-list clearfix")
       bigData = []
       # for each_item in items.find_all('tr'):
       for each_item in items.find_all('li', limit = 5):
           data = {}
           data['视频名'] = each_item.find('div',class_="headline clearfix").a.text
           data['观看次数'] = each_item.find('span',class_="so-icon watch-num").text.replace('\n', '').replace(' ', '')
           data['弹幕数量'] = each_item.find('span',class_="so-icon hide").text.replace('\n', '').replace(' ', '')
           data['上传时间'] = each_item.find('span',class_="so-icon time").text.replace('\n', '').replace(' ', '')
           data['up主'] = each_item.find('a',class_="up-name").text.replace('\n', '').replace(' ', '')
           bigData.append(data)
       return bigData
     
   Url = "https://search.bilibili.com/all?keyword=css&from_source=nav_search_new&order=click&duration=0&tids_1=0&page=1"
   ```

   > 网页规则
   >
   > 1. 翻页，Url 结尾的page= 递增，最大到 50
   > 2. 综合排序：order=totalrank
   > 3. 最多点击：order=click
   > 4. 最新发布：order=pubdate
   > 5. 最多弹幕：order=dm
   > 6. 最多收藏：order=stow

   

### 访问要登录的网页

1. ~~模拟登录~~

   > ~~**模拟登陆总是失败，且意义很小，因为即便模拟登陆成功，得到的网页大多是js 加载过的，依旧拿不到想要的数据**，不如直接用`selenium`~~
   >
   > 1. ~~豆瓣的登录网址是~~
   >
   >    ~~`https://accounts.douban.com/passport/login`~~
   >
   > 2. ~~但进入 "检查"，查看post表单发现请求的网址是~~
   >
   >    ~~`Request URL: https://accounts.douban.com/j/mobile/login/basic`~~
   >
   > 3. ~~思路：直接post这个网址，拿到session，然后用session访问主页~~

2. 利用 `Cookie` 访问Hipda

   ```python
   import requests
   from lxml import etree
   
   def GetBuySell(url):
       fake_headers = {
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
       'Cookie': 'cdb_sid=gz22lD; __utma=128828693.216731137.1581256554.1581256554.1581256554.1; __utmc=128828693; __utmz=128828693.1581256554.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); __utmt=1; cdb_auth=804d%2FygXeOz%2F3XOb%2FBdGgKtgINSEqL3h4EMQ3zstKDHz3K%2FTydHZ4TUuNgl7hVZjq3ZWsLH3cpVsx6ZTXErVM%2BX7LD5J; __utmb=128828693.3.10.1581256554'
       }
       response = requests.get(url, headers=fake_headers)
       html = response.content.decode('gbk')   # 其他网站都是utf-8，Hipda很奇葩
       XpathTree = etree.HTML(html)
       BuySell = XpathTree.xpath('//*[@id="forum6"]/tr/th/div/h2/a/text()')
       print(BuySell)
   
   if __name__ == "__main__":
       url = "https://www.hi-pda.com/forum/"
       XpathTree = GetBuySell(url)
   ```

   > <img src="https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/20200209221042.png" style="zoom:30%;" />

   

### 爬取App Store评分

```python
import urllib.request
import json
import xlsxwriter
page=1
# appid=input("请输入应用id号:")
appid=1142989247
workbook = xlsxwriter.Workbook('app评论.xlsx')
worksheet = workbook.add_worksheet()
format=workbook.add_format()
title=['评分','昵称','标题','评论内容']
worksheet.write_row('A1',title)
row=1
col=0
count=0

#默认循环10次  
while page<11:
    myurl="https://itunes.apple.com/rss/customerreviews/page="+str(page)+"/id="+str(appid)+"/sortby=mostrecent/json?l=en&&cc=cn"
    response = urllib.request.urlopen(myurl)
    myjson = json.loads(response.read().decode())
    print("正在生成数据文件，请稍后......"+str(page*10)+"%")
    if "entry" in myjson["feed"]:
        count+=len(myjson["feed"]["entry"])

        #循环写入第0列：评分
        for i in myjson["feed"]["entry"]:
            worksheet.write(row,col,i["im:rating"]["label"],format)
            row+=1
        #循环写入第1列：昵称
        row=1+(page-1)*50
        for i in myjson["feed"]["entry"]:
            worksheet.write(row,col+1,i["author"]["name"]["label"],format)
            row+=1
        #循环写入第2列：标题    
        row=1+(page-1)*50
        for i in myjson["feed"]["entry"]:
            worksheet.write(row,col+2,i["title"]["label"],format)
            row+=1
        #循环写入第3列：内容
        row=1+(page-1)*50
        for i in myjson["feed"]["entry"]:
            worksheet.write(row,col+3,i["content"]["label"],format)
            row+=1
            
        page=page+1
        row=(page-1)*50+1
    else:
        print("正在生成数据文件，请稍后......100%")
        break
if count==0:
    print("运行完毕，未获取到任何数据。请检查是否输入正确！")
else:
    print("生成完毕，请查阅相关文件,共获取到"+str(count)+"条数据")
workbook.close()
```



