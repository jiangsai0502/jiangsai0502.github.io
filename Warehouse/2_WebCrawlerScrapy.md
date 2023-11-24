# Scrapy入门

#### 1. 安装环境

1. 切换到 `py3` 虚拟环境：`source activate py3`
2. 查看当前环境是否已包含 `Scrapy` 模块：`conda list`
3. 安装 `Scrapy` 模块：`pip install Scrapy`

#### 2. 第一个项目案例

> 开发Scrapy爬虫的步骤

> 创建工程：scrapy startproject xxx（项目名字，不区分大小写）
>
> 明确目标 （编写items.py）：明确你想要抓取的目标
>
> 制作爬虫 （spiders/xxspider.py）：制作爬虫开始爬取网页
>
> 存储内容 （pipelines.py）：设计管道存储爬取内容
>
> 启动程序的py文件（start.py）：等同于此命令（scrapy crawl xxx -o xxx.json）

1. **创建工程 (scrapy startproject)**

   1. 创建项目目录：`mkdir ~/Documents/MyScrapy && cd ~/Documents/MyScrapy`

   2. 创建 `Scrapy` 项目：`scrapy startproject QuotesSpider`

   3. 展示项目的目录树：

      ```bash
      brew install tree
      tree
      ```

      ```python
      MyScrapy
          └── QuotesSpider
              ├── scrapy.cfg
              ├── QuotesSpider/
                     ├── __init__.py
                     ├── __pycache__/
                     ├── items.py
                     ├── middlewares.py
                     ├── pipelines.py
                     ├── settings.py
                     └── spiders/
                         ├── __init__.py
                         └── __pycache__
      ```

      * `scrapy.cfg`：项目的配置文件，一般不用修改

      * `mySpider/`：项目的Python模块，将会从这里引用代码
      * `__init__.py`：该文件指示当前文件夹属于一个python模块
      * `__pycache__/`：该目录用于存储解释器生成的.pyc文件
      * `items.py`：项目的实体类，数据模型，定义爬虫目标的相关属性，例如要爬取 豆瓣Top250 的电影信息，则每部电影就是一个 item，可以理解成强化版的字典类型
      * `middlewares.py`：中间件代码，默认包含下载器中间件和爬虫中间件
      * `pipelines.py`：项目实体管道，用于处理 spider返回的items，包括清洗，验证，持久化(存储到本地)
      * `settings.py`：本爬虫的一些配置信息（比如请求头、多久发送一次请求、ip代理池等）
      * `spiders/`：以后所有的爬虫，都是存放到这个里面

2. **明确目标 (MovieSpider/items.py)**

   1. 分析需求

      > 抓取 `http://quotes.toscrape.com/` 网站里所有名人语录的 "语录", "姓名", "生辰"

   2. 编写项目实体类

      * 打开 `QuotesSpider/items.py` 

        ```python
        import scrapy
        
        class QuotesItem(scrapy.Item):
            words = scrapy.Field()
            name = scrapy.Field()
            birth = scrapy.Field()
        ```
   
3. **制作爬虫（spiders/itcastSpider.py）**

   1. **爬数据**

      1. 进入项目目录：`cd QuotesSpider`

      2. 创建爬虫：`scrapy genspider quotes quotes.toscrape.com`

         * `scrapy` 会自动在 `QuotesSpider/spider` 目录下创建一个名为 `quotes.py` 的爬虫
         *  `quotes.py` 爬取域的范围是 `quotes.toscrape.com`
         * 网址要去掉头部的 `https://` 或 `http://`，以及尾部的 `/`

      3. 修改 `QuotesSpider/QuotesSpider/spiders/quotes.py`

         ```python
         class QuotesSpider(scrapy.Spider):
             name = 'quotes'
             allowed_domains = ['quotes.toscrape.com']
             start_urls = ['http://quotes.toscrape.com/',]
         
             def parse(self, response):
                 pass
         ```

         * `name = 'quotes'`：名称必须是唯一的，不同爬虫必须定义不同的名字

         * `allowed_domains = ['quotes.toscrape.com']`：爬虫搜索的域名范围，即只爬取这个域名下的网页

           > 例如我们要爬取豆瓣上北京地区新上映的电影信息，豆瓣里有很多链接，有的可能就链接到百度百科里去了，如果爬虫就这么无休止的趴下去，那它就永远都回不来了，所以这里我们限定在域名范围内

         * `start_urls = ['http://quotes.toscrape.com/',]`：要爬取的 url 列表

         * parse() 方法 ：解析爬虫获取的网页源码，每个 url 完成下载后将被调用

           > 主要作用
           >
           > 1. 解析返回的网页数据 (response.body)
           > 2. 提取结构化数据 (生成item)
           > 3. 查找指向下一页的链接，将获得的下一页链接再次以同样的方式进行请求处理

           > 1. 因为使用的 yield,而不是 return。parse() 方法将会被当做一个生成器使用。 Scrapy 会逐一获取 parse() 方法生成的结果，并判断结果类型
           > 2. 结果若是 request 类型，则加入爬取队列；若是 item 类型，则使用 pipeline 处理
           > 3. Scrapy 取到第一部分的 request 后会把这个 request 放到队列里，然后从生成器里继续取，直到取尽
           > 4. 取尽第一部分的 request后，就开始获取第二部分的item，但取到的 item 不用等待，取到后就立刻放到对应的 pipeline 里处理
           > 5. parse() 方法作为 callback 回调函数赋值给了 Request，指定 parse() 方法来处理这些请求 scrapy.Request(ur1, callback=self.parse) Request 对象经过调度，执行生成 scrapy.http.response() 的响应对象，并送回给 parse() 方法，直到调度器中没有 Request (递归的思路)
           > 6. 取尽之后，parse() 工作结束，Scrapy 引擎再根据队列和 pipelines 中的内容去执行相应的操作
           > 7. 程序在取得各个页面的 items 前，会先处理完之前所有的 request 队列里的请求，然后再提取 items
           > 8. 这一切的一切, Scrapy 引擎和调度器将负责到底

         * 源码

           ```python
           import scrapy
           from QuotesSpider.items import QuotesItem
           
           class QuotesSpider(scrapy.Spider):
               name = 'quotes'
               allowed_domains = ['quotes.toscrape.com']
               start_urls = [
                   'http://quotes.toscrape.com/',
               ]
           
               def parse(self, response):
                   list_div = response.xpath('//div[@class="col-md-8"]/div')
                   for div in list_div:
                       quote = QuotesItem()
                       quote['words'] = div.xpath('./span[1]/text()').get()
                       auth_href = div.xpath('./span[2]/a/@href').get()
                       if auth_href:
                         yield response.follow(auth_href, meta={'quote': quote}, callback=self.parse_author)
           
                   next_page = response.xpath('//li[@class="next"]/a/@href').get()
                   if next_page:
                       yield response.follow(next_page,self.parse)
           
               def parse_author(self, response):
                   author = response.xpath('//div[@class="author-details"]')
                   quote = response.meta['quote']
                   quote['name'] = author.xpath('./h3/text()').get(),
                   quote['birth'] = author.xpath('./p[1]/span/text()').getall(),
                   yield quote
           ```

           > 1. 无需自己实现 Fetch_Data，爬虫启动后，scrapy 自动抓取数据，这个类里的方法只负责数据解析 Parse_Data
           >
           > 2. `response.follow(auth_href, self.parse_author)`
           >
           >    * scrapy 对 auth_href 链接发起请求
           >    * 请求成功后调用 self.parse_author 方法
           >    * 调用是异步执行的，调用的先后顺序只有调度器 schedule 知道
           >
           > 3. `yield au_request`
           >
           >    * yield 出去的数据会被 scrapy 框架的 item 接收，进行下一步的处理。若没有进一步处理，则会被打印到终端
           >
           > 4. `scrapy.Request`和`response.follow`的区别
           >
           >    ```python
           >    next_page = response.xpath('//span[2]/a/@href').get()
           >    if next_page:
           >        next_page = response.urljoin(next_page)
           >        yield scrapy.Request(next_page, callback=self.parse)
           >    ```
           >
           >    ```python
           >    next_page = response.xpath('//span[2]/a/@href').get()
           >    if next_page:
           >        yield response.follow(next_page, callback=self.parse)
           >    ```
           >
           >    * `scrapy.Request` 需要下一页的绝对 url
           >    * `response.follow` 需要下一页的相对 url
           >
           > 5. 将附加数据传递给回调函数
           >
           >    ```python
           >    def parse_1(self, response):
           >        quote = QuotesItem()
           >        quote['main_url'] = response.url
           >        yield response.follow('author/J-K-Rowling/', meta={'quote': quote}, callback=self.parse_2)
           >       
           >    def parse_2(self, response):
           >        quote = response.meta['quote']
           >        quote['other_url'] = response.url
           >        yield quote
           >    ```
           >
           >    * `meta`是dict类型，用来在不同请求之间传递值
           >    * parse_1 通过 `request的meta属性` 向回调函数parse_2 传递参数，以便接收 parse_2 处理之后的结果

      4. 修改 `MovieSpider/MovieSpider/settings.py`   [参考](https://www.jianshu.com/p/df9c0d1e9087)

         ```python
         USER_AGENT = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.110 Safari/537.36'
         ROBOTSTXT_OBEY = False
         DOWNLOAD_DELAY = 0.5
         HTTPCACHE_ENABLED = True
      ```
         
      * 伪装成浏览器：`USER_AGENT`
         * 遵守爬虫协议：`ROBOTSTXT_OBEY`，默认是 True。我们改成 False。True 是遵守机器协议，即爬虫工作时，scrapy首先去找 robots.txt 文件，如果没有找到，则直接停止爬取
      * 限制爬行速度：`DOWNLOAD_DELAY`，设置从该网站下载连续页面之前的等待时间，单位是秒
         * 启动HTTP请求缓存：`HTTPCACHE_ENABLED`，下次再遇到该url时，不再请求远程服务器，而直接使用缓存，方便调试 

      5. 运行爬虫

         1. 进入项目目录：`MyScrapy/QuotesSpider`
         2. 运行爬虫（结果打印在终端）：`scrapy crawl quotes`
         3. 运行爬虫（结果存入 json 文件）： `scrapy crawl quotes -o quotes.json`
         
      6. 调试 scrapy

         1. 终端调试

            1. 在项目目录下：`MyScrapy/QuotesSpider`

            2. 进入调试控制台

               1. `scrapy shell`
               2. `scrapy shell http://quotes.toscrape.com/`

            3. 进入控制台后可使用如下函数和对象

               | 函数              | 描述                                                         | 示例                                   |
               | ----------------- | ------------------------------------------------------------ | -------------------------------------- |
               | `shelp()`         | 查看帮助                                                     |                                        |
               | `fetch()`         | 请求 url 或 request 对象。请求成功后会将当前作用域内的 request 和 response 对象重新赋值 | `fetch('http://quotes.toscrape.com/')` |
               | `view(response)`  | 将抓取到的网页在浏览器打开                                   |                                        |
               | `scrapy view url` | 用项目配置下载网页，并用浏览器打开                           |                                        |

               调试元素

               ```python
               测试xpath能否取到元素
               response.xpath('//div[@class="col-md-8"]/div/span[2]/small/text()')
               测试items
               from QuotesSpider.items import QuotesItem
               quote = QuotesItem()
               quote.fields
      ```

         2. vscode调试

            1. 编辑项目的配置文件 launch.json中增加scrapy调试配置

               ```js
               {
                   "name": "Python: 调试quotes",
                   "type": "python",
                   "request": "launch",
                   "module": "scrapy",
                   "cwd": "${workspaceRoot}/QuotesSpider", //项目目录
                   "args": [
                       "crawl", //执行命令
                       "quotes" //爬虫名
                   ]
               }
               ```

               1. `"cwd": "${workspaceRoot}/QuotesSpider"`中的`QuotesSpider`改为项目名
               2. `"args"`中的`"quotes"`改为爬虫名

               ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/20200216182913.png)

            2. 调试流程

               ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/20200216183602.png)

         

      **爬数据的流程**

      > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200202203910.png)
      >
      > 1. **Spiders 爬虫** 将 start_urls 中的第一个 url 发送给 **Scrapy Engine 引擎**
      >2. **Scrapy Engine 引擎** 把 url 封装成 *Requests 请求*，然后传递给 **Scheduler 调度器**
      > 3. **Scheduler 调度器** 将 *Requests 请求* 进行排序、入队，然后有序的传递给 **Scrapy Engine 引擎**
      > 4. **Scrapy Engine 引擎** 收到 *Requests 请求* 后通过 *Downloader Middlewares 下载中间件* 传递给 **Downloader 下载器 **
      > 5. **Downloader 下载器** 去互联网下载数据，然后拿到互联网服务器发回的 *Response 应答包*后，通过 *Downloader Middlewares 下载中间件* 发送给 **Scrapy Engine 引擎**
      > 6. **Scrapy Engine 引擎** 接收到 *Response 应答包* 后，通过 *Spider Middlewares 爬虫中间件* 发送给 **Spiders 爬虫**
      > 7. **Spiders 爬虫** 处理 *Response 应答包* 并返回匹配到的 *Item 实体* 和新的 *Request 请求* 给 **Scrapy Engine 引擎**
      > 8. **Scrapy Engine 引擎** 将收到的 *Item 实体* 传递给 **Item Pipeline 实体管道** 做数据处理或入库保存，将收到的 *Request 请求* 传递给 **Scheduler 调度器** 进行排序、入队
      > 9. 从第 3 步重复直到调度器中没有更多的 *request 请求*
      > 
      > > 代码写好，程序开始运行...
      >>
      > > - 1 引擎：Hi！Spider, 你要处理哪一个网站？
      > > - 2 Spider：老大要我处理 movie.douban.com
      > > - 3 引擎：你把第一个需要处理的URL给我吧
      > > - 4 Spider：给你，第一个URL是 movie.douban.com/cinema/later/chengdu
      > > - 5 引擎：Hi！调度器，我这有request请求你帮我排序，入队一下
      > > - 6 调度器：好的，正在处理你等一下
      > > - 7 引擎：Hi！调度器，把你处理好的request请求给我
      > > - 8 调度器：给你，这是我处理好的request
      > > - 9 引擎：Hi！下载器，你按照老大的下载中间件的设置帮我下载一下这个request请求
      > > - 10 下载器：好的！给你，这是下载好的东西。（如果失败：sorry，这个 request 下载失败了。然后引擎告诉调度器，这个request下载失败了，你记录一下，我们待会儿再下载）
      > > - 11 引擎：Hi！Spider，这是下载好的东西，并且已经按照老大的下载中间件处理过了，你自己处理一下（注意！这里 responses 默认是交给 def parse() 这个函数处理的）
      > > - 12 Spider：（处理完毕数据之后），Hi！引擎，我这里有两个结果，这个是我获取到的Item数据，还有这个是我需要跟进的URL
      > > - 13 引擎：Hi ！管道，我这儿有个item，你帮我处理一下！Hi ！调度器！这是需要跟进的URL，你帮我处理一下，然后从第 5 步开始循环，直到获取完老大需要全部信息。
      > > - 14 管道调度器：好的，现在就做！
      > >
      > > **注意！只有当调度器中不存在任何request了，整个程序才会停止，（也就是说，对于下载失败的URL，Scrapy也会重新下载）**

   2. **存数据**

      1. 修改 `tutorial/pipelines.py` 管道

         * `Item` 被 yield 出来之后，会自动被送到 `Item Pipeline` 进行处理
         * `Item Pipeline` 可以用系统生成的 `pipelines.py`  ，也可以删了 `pipelines.py`，自己新建一个，只要实现`process_item()` 方法即可。

         这里我们新建一个 `QuotesPipeline.py`

      2. 























