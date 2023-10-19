##### 虚拟环境检查、配置，使用

1. 查看当前系统下的虚拟环境，安装路径
   > `conda info --envs`
2. 创建名为 py3 的python3的虚拟环境
   > `conda create -n py3 python=3.10`
3. 激活虚拟环境py3
   
   > `conda activate py3`

4. py3中Python的位置
   
   > `which python`

5. 查看当前的虚拟环境的所有安装包
   > `conda list`
   

##### Playwright安装、配置，使用

1. 为当前的虚拟环境安装playwright包
   
    > - 查看此时要用的pip在哪个环境
    >   
    >   > 详见[Python 周边环境](Sai_FootPrint/1_PythonEnvironment.md)
    >   > 
    >   > `pip3 -V`
    >   > 
    >   > `conda install pip3`
    > 
    > - `pip3 install pytest-playwright`

2. 为playwright安装浏览器
   
    > `playwright install`
    
3. 第一个录制脚本

    > `playwright codegen`
    > 
    > [教程](https://www.bilibili.com/video/BV1H24y1G745)

##### VScode配置，使用

* 执行环境切换为的安装环境py3
  
  ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310011347291.png)

##### 网页爬虫实操

* 录制脚本
  
  > `playwright codegen`
  > 
  > [教程](https://www.bilibili.com/video/BV1H24y1G745)

* 常用功能
  
  ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310061535560.png)
  
  > ```
  > import re, os, random
  > from numbers import Integral
  > from playwright.sync_api import Playwright, sync_playwright, expect
  > from bs4 import BeautifulSoup
  > ```
  > 
  > * `def run(playwright: Playwright) -> None:`
  >   
  >   > 浏览器环境
  >   > 
  >   > * 方式一：Chrome本地浏览器（模拟完全真实场景）
  >   >   
  >   >   > terminal操作部分
  >   >   > 
  >   >   > 1. 查看9222端口是否被占用
  >   >   >    `lsof -i:9222`
  >   >   > 
  >   >   > 2. 若结果如下，表示端口已被占用
  >   >   >    
  >   >   >    | COMMAND | PID   | USER     | FD  | TYPE | DEVICE            | SIZE/OFF | NODE | NAME                             |
  >   >   >    | ------- | ----- | -------- | --- | ---- | ----------------- | -------- | ---- | -------------------------------- |
  >   >   >    | Google  | 93266 | jiangsai | 97u | IPv4 | 0xf8edc13e875fe59 | 0t0      | TCP  | localhost:teamcoherence (LISTEN) |
  >   >   > 
  >   >   > > 即9222端口被「Google进程」占用，PID为「93266」
  >   >   > 
  >   >   > 3. 杀掉进程释放端口
  >   >   >    
  >   >   >    `sudo kill -9 PID`
  >   >   > 
  >   >   > 4. 关闭当前所有Chrome浏览器
  >   >   > 
  >   >   > 5. debug模式启动Chrome浏览器
  >   >   >    `/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222`
  >   >   > 
  >   >   > 代码部分
  >   >   > 
  >   >   > ```
  >   >   > # 启动上述本地debug模式Chrome
  >   >   > SaiBrowser = playwright.chromium.connect_over_cdp('http://localhost:9222')
  >   >   > SaiContext = SaiBrowser.contexts[0]
  >   >   > SaiContext.route(re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.webp.*)"), lambda route: route.abort())
  >   >   > SaiPage = SaiContext.new_page()
  >   >   > ```
  >   > 
  >   > * 方式二：Playwright无头浏览器（反爬网站能识别）
  >   >   
  >   >   ```python
  >   >   # # 初始化一个浏览器（headless = False 有头浏览器；slow_mo = 3000 每个操作停3秒）
  >   >   # SaiBrowser = playwright.chromium.launch(headless = False, slow_mo = 3000)
  >   >             
  >   >   # # 加载本地cookie
  >   >   # # 若本地有cookie，则在SaiBrowser中创建一个context（网页管理器），并加载该cookie，实现免登陆；若本地没有，则在SaiBrowser中创建一个空的context
  >   >   # # 每个context是一个独立会话，用于环境隔离，每个context可使用1套代理，登录1套账号
  >   >   # os.chdir('/Users/jiangsai/Desktop')
  >   >   # if os.path.exists('state.json'):
  >   >   #     SaiContext = SaiBrowser.new_context(storage_state="state.json")
  >   >   # else:
  >   >   #     SaiContext = SaiBrowser.new_context()
  >   >             
  >   >   # 拦截SaiContext下所有页面的图片请求（凡含.png的链接，都当做是png图片）
  >   >   # SaiContext.route(re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.webp.*)"), lambda route: route.abort())
  >   >             
  >   >   # 初始化一个网页
  >   >   # SaiPage = SaiContext.new_page()
  >   >             
  >   >   # 拦截SaiPage这个页面的图片请求
  >   >   # SaiPage.route(re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.webp.*)"), lambda route: route.abort())
  >   >   ```
  >   >   
  >   >   > `SaiContext.route()`和 `SaiPage.route()`的区别：前者应用于 `SaiContext`下的所有页面，后者只应用于 `SaiPage`这一个页面
  >   > 
  >   > 页面交互
  >   > 
  >   > * 打开一个网址
  >   >   
  >   >   `SaiPage.goto("https://www.zhihu.com/question/22543815")`
  >   > 
  >   > * 等待页面加载，直至加载完成
  >   >   
  >   >   `SaiPage.wait_for_load_state("networkidle")`
  >   > 
  >   > * 将这个tab页置于顶部
  >   >   
  >   >   `SaiPage.bring_to_front()`
  >   > 
  >   > * 页面刷新
  >   >   
  >   >   `SaiPage.reload()`
  >   > 
  >   > * 页面后退
  >   >   
  >   >   `SaiPage.go_back()`
  >   > 
  >   > * 页面前进
  >   >   
  >   >   `SaiPage.go_forward()`
  >   > 
  >   > * 鼠标悬停
  >   >   
  >   >   > 所有 `//`开头的表达式都会默认为 XPath
  >   >   
  >   >   `SaiPage.locator('//div[@class="Question"]').hover()`
  >   > 
  >   > * 键盘输入
  >   >   
  >   >   1. 模拟字符串输入
  >   >      
  >   >      `SaiPage.locator('//*[@id="Popover2"]').type('technical')`
  >   >   
  >   >   2. 模拟按键输入
  >   >      
  >   >      > `F(1-12)`,`数字(0-9)`,`Key(a-z、A-Z)大小写敏感`,`Backspace(向左删除)`,`Delete(向右删除)`,`Tab`,`Escape`,`End`,`Enter`,`Home`,`Insert`,`PageUp、PageDown`,`ArrowUp、ArrowDown、ArrowLeft、ArrowRight`
  >   >      
  >   >      `SaiPage.locator('//*[@id="Popover2"]').press("Z")`
  >   >      
  >   >      `SaiPage.locator('//*[@id="Popover2"]').press("Delete")`
  >   >      
  >   >      `SaiPage.keyboard.press('Enter')`
  >   >   
  >   >   3. 模拟组合键输入
  >   >      
  >   >      > `Shift`, `Control`,` Alt`, `Meta(Meta = Win/Cmd 键)`
  >   >      > [其他的按键参考这里](https://playwright.dev/python/docs/api/class-keyboard)
  >   >      
  >   >      全选 `Command+A`：`SaiPage.keyboard.press("Meta+A") `
  >   > 
  >   > * 鼠标点击
  >   > 
  >   > `SaiPage.locator('//button[@class="SearchBar"]').click()`
  >   > 
  >   > * 页面滚动
  >   >   
  >   >   1. 滚动指定高度
  >   >      
  >   >      > `page.mouse.wheel(向右滚动长度,向下滚动长度)`
  >   >      
  >   >      `page.mouse.wheel(0,7000)`
  >   >   
  >   >   2. 滚动到页面底部
  >   >      
  >   >      `page.evaluate("() => window.scrollTo(0,document.body.scrollHeight)")`
  >   >   
  >   >   ```python
  >   >   # 滚动加载更多内容，直到不再加载
  >   >   NotEnd = True
  >   >   while NotEnd:
  >   >       # 滚动前的页面高度
  >   >       BeforeScrollHeight = SaiPage.evaluate("() => document.body.scrollHeight")
  >   >       # 滚动到页面底部
  >   >       SaiPage.evaluate("() => window.scrollTo(0,document.body.scrollHeight)")
  >   >       # 等待网络加载，单位是毫秒
  >   >       SaiPage.wait_for_timeout(random.randint(1000,3000))
  >   >       # 滚动后的页面高度
  >   >       AfterScrollHeight = SaiPage.evaluate("() => document.body.scrollHeight")
  >   >       if BeforeScrollHeight == AfterScrollHeight:
  >   >           # 知乎加载到一定程度，加载速度会变慢，但实际还没加载完
  >   >           SaiPage.wait_for_timeout(random.randint(1000,3000))
  >   >           # SaiPage.mouse.wheel(0, 20000)
  >   >           SaiPage.evaluate("() => window.scrollTo(0,document.body.scrollHeight)")
  >   >           AfterScrollHeight = SaiPage.evaluate("() => document.body.scrollHeight")
  >   >           # 两次等待，两次加载后依然页面高度不变，则判断为加载完了
  >   >           if BeforeScrollHeight == AfterScrollHeight:
  >   >               NotEnd = False
  >   >   ```
  >   > 
  >   > * frame弹窗
  >   >   
  >   >   `SaiPage.frame_locator('//*[@id="iframe"]').locator('//div/input').click()`
  >   > 
  >   > 页面数据提取
  >   > 
  >   > * 截取页面当前可见部分
  >   >   
  >   >   `SaiPage.screenshot(path = "FullScreen.png")`
  >   > 
  >   > * 截取页面指定部分
  >   >   
  >   >   `SaiPage.locator('//table[3]').screenshot(path = "PartPage.png")`
  >   > 
  >   > * 截取整个页面
  >   >   
  >   >   `SaiPage.screenshot(path = "FullPage.png", full_page = True)`
  >   > 
  >   > * 获取页面网址
  >   >   
  >   >   `PageURL = SaiPage.url`
  >   > 
  >   > * 获取页面标题
  >   >   
  >   >   `PageTitle = SaiPage.title()`
  >   > 
  >   > * 获取页面完整Html源代码
  >   >   
  >   >   `PageHtml = SaiPage.content()`
  >   > 
  >   > * 获取页面某个节点的Html源代码
  >   >   
  >   >   `ElementHtml = SaiPage.locator('//div[@class="Question"]').inner_html()`
  >   >   
  >   >   `BSHtml = BeautifulSoup(ElementHtml).prettify()`
  >   > 
  >   > * 获取页面完整文字
  >   >   
  >   >   `PageTextContent = SaiPage.text_content()`
  >   > 
  >   > * 获取页面某个节点的完整文字内容
  >   >   
  >   >   > `text_content()`：返回代码内容；一股脑全部获取，包括隐藏内容
  >   >   > `inner_text()`：返回页面显示内容；按照元素获取，元素间以换行分割
  >   >   
  >   >   `ElementTextContent = SaiPage.locator('//div[@class="HaHa"]').text_content()`
  >   >   
  >   >   `ElementInnerText = SaiPage.locator('//div[@class="HaHa"]').inner_text()`
  >   > 
  >   > * 获取页面的列表元素
  >   >   
  >   >   ```python
  >   >   Elements = SaiPage.query_selector_all('//div[@class="Question"]/div')
  >   >   # 枚举列表元素所有目标值
  >   >   for element in Elements:
  >   >       # 每个元素的文本值 text_content
  >   >       print(element.text_content())
  >   >       # 每个元素的链接
  >   >       print(element.query_selector('//a[@id="Link"]').get_attribute('href'))
  >   >   ```
  >   >   
  >   >   ```python
  >   >   # 枚举列表中每个元素的每个属性值
  >   >   for element in Elements:
  >   >       # 提取每个元素的所有属性 evaluate
  >   >       el_attrs = element.evaluate("el => el.getAttributeNames()")
  >   >       # 枚举所有的属性名称和值 get_attribute
  >   >       for attr in el_attrs:
  >   >           print(attr, ":", element.get_attribute(attr))
  >   >   ```
  >   > 
  >   > * 下载页面所有图片
  >   >   
  >   >   ```python
  >   >   Pic_folder = SaiPage.title()
  >   >   if not os.path.exists(Pic_folder):
  >   >       # 创建文件夹
  >   >       os.mkdir(Pic_folder)
  >   >       # 进入文件夹
  >   >       os.chdir(Pic_folder) 
  >   >   # 找到所有图片节点
  >   >   All_Pic = SaiPage.query_selector_all('//img')
  >   >   Pic_num = 1
  >   >   for Pic in All_Pic:
  >   >       # 提取所有图片链接
  >   >       Pic_url = Pic.get_attribute('src')
  >   >       if Pic_url != '':
  >   >           # 将图片写入文件
  >   >           with open(f'{Pic_num}.jpg', 'wb') as file:
  >   >               file.write(requests.get(Pic_url).content)
  >   >               Pic_num += 1
  >   >           print(Pic_url)
  >   >   ```
  >   > 
  >   > * 将页面部分内容转化为 `markdown`后下载到本地
  >   >   
  >   >   ```python
  >   >   # 切换目录
  >   >   os.chdir('/Users/jiangsai/Desktop')
  >   >   MarkDownMaker = html2text.HTML2Text()
  >   >   MarkDownMaker.ignore_links = True
  >   >   TargetHtml = SaiPage.locator('//div[@class="article"]').inner_html()
  >   >   MarkDownContent = MarkDownMaker.handle(TargetHtml)
  >   >   with open('test.md', mode='w', encoding='utf-8') as f:
  >   >       f.write(MarkDownContent)
  >   >   ```
  >   > 
  >   > 元素存在性判断[参考](https://www.cnblogs.com/yoyoketang/p/17214493.html)
  >   > 
  >   > * `locator()`判断页面中是否存在某个元素
  >   >   
  >   >   > `locator()`定位页面上的元素，不管元素存不存在，都返回一个 `locator`对象，可用 `count() `方法统计元素个数，个数是 0则元素不存在
  >   >   
  >   >   ```python
  >   >   # 直接使用locator()和click()进行定位点击，若当前页面没有该元素则程序会一直等待，直到报错TimeoutError
  >   >   SaiPage.locator(xpath).click()
  >   >   # 因此要先判断一下，元素是否存在
  >   >   if SaiPage.locator(xpath).count() != 0:
  >   >       SaiPage.locator(xpath).click()
  >   >   ```
  >   > 
  >   > * `query_selector()`判断页面中是否存在某个元素
  >   >   
  >   >   > `query_selector()`和 `query_selector_all()`定位页面上的Dom，若元素不存在则返回None
  >   >   
  >   >   ```python
  >   >   # 直接使用query_selector()和click()进行定位点击，若当前页面没有该元素则程序立刻报错AttributeError：'NoneType' object has no attribute 'click'
  >   >   SaiPage.query_selector(xpath).click()
  >   >   # 因此要先判断一下，元素是否存在
  >   >   if SaiPage.query_selector(xpath) is not None:
  >   >       SaiPage.query_selector(xpath).click()
  >   >   ```
  >   > 
  >   > 点击二级页链接
  >   > 
  >   > * 情况一：二级页在老标签加载
  >   >   
  >   >   ```python
  >   >   SaiPage.locator(xpath).click()
  >   >   SaiPage.wait_for_timeout(random.randint(1000,3000))
  >   >   # SaiPage是在打开二级页后，标签没有增加，一级页被二级页取代，未来只能操作二级页，但可以用SaiPage.go_back()在本标签回到一级页
  >   >   ```
  >   > 
  >   > * 情况二：二级页在新标签加载
  >   >   
  >   >   ```python
  >   >   with SaiContext.expect_page() as SonPageInfo:
  >   >       SaiPage.locator(xpath).click()
  >   >   SonPage = SonPageInfo.value
  >   >   SonPage.wait_for_load_state()
  >   >   SonPage.bring_to_front()
  >   >   # SaiPage是一级页的标签页，还在，SonPage是二级页的标签页，可以分别操作2个标签页
  >   >   ```
  >   > 
  >   > 存储Cookie
  >   > 
  >   > > 将 `cookie`保存到 `state.json`，方便方式二Playwright无头浏览器进行免登录
  >   > 
  >   > `storage = SaiContext.storage_state(path="state.json")`
  >   > 
  >   > 收尾工作
  >   > 
  >   > ```python
  >   > SaiPage.pause()
  >   > SaiContext.close()
  >   > SaiBrowser.close()
  >   > ```
  > 
  > ```python
  > with sync_playwright() as playwright:
  >     run(playwright)
  > ```

##### 网页爬虫案例

1. 向ChatGPT循环提交请求并获取请求结果
   
   > ```python
   > from numbers import Integral
   > import re, os, random
   > from playwright.sync_api import Playwright, sync_playwright, expect
   > from bs4 import BeautifulSoup
   > 
   > WebSite = 'https://chat.openai.com/'
   > Xpath_Answer = '//div[@class="flex flex-col text-sm dark:bg-gray-800"]/div'
   > 
   > def Initialize(WebSite):
   >     SaiBrowser = playwright.chromium.connect_over_cdp('http://localhost:9222')
   >     SaiContext = SaiBrowser.contexts[0]
   >     SaiPage = SaiContext.new_page()
   >     SaiPage.goto(WebSite)
   >     SaiPage.wait_for_load_state("networkidle")
   >     SaiPage.bring_to_front()
   >     SaiPage.wait_for_timeout(10000)
   >     return SaiBrowser, SaiContext, SaiPage
   > 
   > def run(playwright: Playwright) -> None:
   >     SaiBrowser, SaiContext, SaiPage = Initialize(WebSite)
   >     question_list=['python','sql','oracle','mysql']
   >     for qst in question_list:
   >         SaiPage.get_by_role("textbox").fill(qst)
   >         SaiPage.get_by_role("textbox").press("Enter")
   >         SaiPage.wait_for_timeout(random.randint(1500, 2500))
   >         text1 = "1"
   >         text2 = "2"
   >         while(text1 != text2):
   >             t1_list = SaiPage.query_selector_all(Xpath_Answer)
   >             if(len(t1_list)>0):
   >                 text1 = t1_list[-2].inner_text()
   >             SaiPage.wait_for_timeout(random.randint(1000,3000))
   >             t2_list = SaiPage.query_selector_all(Xpath_Answer)
   >             if(len(t2_list)>0):
   >                 text2 = t2_list[-2].inner_text()
   >             print(text1)
   > 
   >     SaiContext.close()
   >     SaiBrowser.close()
   > # ---------------------收尾工作---------------------
   > 
   > with sync_playwright() as playwright:
   >     run(playwright)
   > ```

##### 爬虫实操

* #### 爬取接口json数据
  
  [参考](https://3yya.com/lesson/61)

> 打开开发者工具 -> 切到 `Network`  -> 刷新页面 -> 点击 `XHR`过滤请求 -> 逐个查看每个请求的 `Response`
> 
> 案例1：[B站个人空间](https://space.bilibili.com/107861587/video)
> 
> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310071930814.png)
> 
> > 通过观察和测试发现
> > 
> > 1. 接口API：https://api.bilibili.com/x/space/wbi/arc/search?mid=107861587&ps=30&tid=0&pn=1&keyword=&order=pubdate&platform=web&web_location=1550101&order_avoided=true&w_rid=ae73d64fedd5ef027f2a7309c3fa27c5&wts=1696676696
> > 2. 接口API通过pn=1、2的方式进行翻页请求
> > 3. 所有 `XHR`中请求中，接口API的特征为以 `https://api.bilibili.com/x/space/wbi/arc/search?`开头
> 
> ```python
> import json
> from playwright.sync_api import Playwright, sync_playwright, expect
> 
> def handle_json(json):
>     for p in json['data']['list']['vlist']:
>         title = p['title']
>         comment = p['comment']
>         print('title: ', title, ' comment: ', comment)
> 
> def handle(response):
>     if response is not None:
>         if response.url.startswith("https://api.bilibili.com/x/space/wbi/arc/search?"):
>             print(response.request.url)
>             print(response.request.post_data)
>             handle_json(response.json())
> 
> def run(playwright: Playwright) -> None:
>     SaiBrowser = playwright.chromium.connect_over_cdp('http://localhost:9222')
>     SaiContext = SaiBrowser.contexts[0]
>     SaiPage = SaiContext.new_page()
>     SaiPage.on("response", lambda response: handle(response=response))
>     SaiPage.goto('https://space.bilibili.com/107861587/video?pn=2')
> 
>     SaiContext.close()
>     SaiBrowser.close()
> 
> with sync_playwright() as playwright:
>     run(playwright)
> ```

* #### 场景一：滚动加载 + 爬取一级页信息

> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310171701388.png)
>

```python
import os, html2text, re, random
from playwright.sync_api import Playwright, sync_playwright

# MarkDown文件目录
MDdir = "/Users/jiangsai/Desktop"
os.chdir(MDdir)
MarkDownMaker = html2text.HTML2Text()
MarkDownMaker.ignore_links = True
# 待爬的页面
WebSite = "https://zhuanlan.zhihu.com/p/607194926"
# 类型一：问答型
# 问题
Xpath_Answer = '//h1[@class="QuestionHeader-title"]'
# 问题描述
Xpath_Answer_Desc = '//div[@class="css-eew49z"]'
# 整个答案块
Xpath_Questions_Block = '//div[@role="list"]/div'
# 答案块中的答案list
Xpath_Questions = '//div[@role="list"]/*[not(@role="listitem")]'
# 答案块中的每个答案的作者
Xpath_Author = '//div[@class="AuthorInfo-head"]'
# 答案块中的每个答案的内容
Xpath_Question = (
    '//span[@class="RichText ztext CopyrightRichText-richText css-117anjg"]'
)
# 类型二：专题型
Xpath_Article_Title = "//article/header/h1"
Xpath_Article_Content = '//article/div[@class="Post-RichTextContainer"]'


def Initialize(WebSite):
    SaiBrowser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    SaiContext = SaiBrowser.contexts[0]
    # SaiContext.route(re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.webp.*)"), lambda route: route.abort())
    SaiPage = SaiContext.new_page()
    SaiPage.goto(WebSite)
    SaiPage.wait_for_load_state("networkidle")
    SaiPage.bring_to_front()
    return SaiBrowser, SaiContext, SaiPage


def SaiScroll(ScrollPage, ScrollTimes):
    # 滚动加载更多内容，直到不再加载或者滚动了10次
    NotEnd = True
    ScrollTime = 1
    while NotEnd and ScrollTime < ScrollTimes:
        # 滚动前的页面高度
        BeforeScrollHeight = ScrollPage.evaluate("() => document.body.scrollHeight")
        ScrollTime += 1
        for i in range(3):
            # 滚动到页面底部
            ScrollPage.evaluate("() => window.scrollTo(0,document.body.scrollHeight)")
            # 微上划一下模拟人类
            ScrollPage.keyboard.press("PageUp")
            ScrollPage.wait_for_timeout(random.randint(1000, 3000))
        # 滚动后的页面高度
        AfterScrollHeight = ScrollPage.evaluate("() => document.body.scrollHeight")
        if BeforeScrollHeight == AfterScrollHeight or ScrollTime >= ScrollTimes:
            NotEnd = False

def ExtractQAInfo(WritePage):
    # 问题部分
    Answer = WritePage.query_selector(Xpath_Answer).text_content()
    Answer_Desc = ""
    # 判断问题描述是否存在，有些问题没有描述
    if WritePage.locator(Xpath_Answer_Desc).count() != 0:
        # 判断问题描述是否被收起
        if WritePage.locator(Xpath_Answer_Desc + "//button").count() != 0:
            WritePage.locator(Xpath_Answer_Desc + "//button").click()
        # 因问题描述可能包含图片，故此处使用HTML2Text提取富文本
        Answer_Content_Html = WritePage.query_selector(Xpath_Answer_Desc).inner_html()
        Answer_Desc = MarkDownMaker.handle(Answer_Content_Html)
    with open("test.md", mode="a", encoding="utf-8") as f:
        f.write("### " + Answer + "\n" + "> " + Answer_Desc + "\n\n" + "----" + "\n")
    # 答案部分
    # 判断答案是否存在，有些问题没有答案
    if WritePage.locator(Xpath_Questions_Block).count() != 0:
        # 获取所有答案块
        Elements = WritePage.query_selector_all(Xpath_Questions)
        for element in Elements:
            Author = element.query_selector(Xpath_Author).text_content()
            # 因答案内容可能包含图片，故此处使用HTML2Text提取富文本
            QuestionHtml = element.query_selector(Xpath_Question).inner_html()
            Question = MarkDownMaker.handle(QuestionHtml)
            with open("test.md", mode="a", encoding="utf-8") as f:
                f.write("##### " + Author + "\n" + Question + "----" + "\n")

def ExtractZLInfo(WritePage):
    # 因答案内容可能包含图片，故此处使用HTML2Text提取富文本
    Article_Title_Html = WritePage.query_selector(Xpath_Article_Title).inner_html()
    Article_Title = MarkDownMaker.handle(Article_Title_Html)
    Article_Content_Html = WritePage.query_selector(Xpath_Article_Content).inner_html()
    Article_Content = MarkDownMaker.handle(Article_Content_Html)
    with open("test.md", mode="a", encoding="utf-8") as f:
        f.write(
            "### " + Article_Title + "\n" + Article_Content + "\n\n" + "----" + "\n"
        )

def run(playwright: Playwright) -> None:
    SaiBrowser, SaiContext, SaiPage = Initialize(WebSite)
    if "zhuanlan" in SaiPage.url:
        # 专栏页面
        ExtractZLInfo(SaiPage)
    elif "zvideo" in SaiPage.url:
        # 视频页面不抓取
        pass
    else:
        # 问答页面
        # 滚动搜索页获取更多数据
        SaiScroll(SaiPage, 1)
        # 写入MarkDown
        ExtractQAInfo(SaiPage)
    # 收尾
    SaiPage.close()
    SaiContext.close()
    SaiBrowser.close()


with sync_playwright() as playwright:
    run(playwright)
```

* #### 场景二：滚动加载 + 爬取二级页信息

> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310171659341.png)
> 
> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310181706425.png)
> 

```
import os, html2text, re, random
from playwright.sync_api import Playwright, sync_playwright

# MarkDown文件目录
MDdir = "/Users/jiangsai/Desktop"
os.chdir(MDdir)
MarkDownMaker = html2text.HTML2Text()
MarkDownMaker.ignore_links = True
# 待爬的第一个页面
WebSite = "https://www.zhihu.com/search?q=%E4%B8%93%E9%A2%98"
# 搜索页结果list
Xpath_Search_Results = (
    '//div[@class="List"]/div/*[not(@class="Card SearchResult-Card")]'
)
# 搜索页每个结果标题的url
Xpath_Search_Result_url = '//h2[@class="ContentItem-title"]//div/a'
# 类型一：问答型
# 二级页「查看全部回答」（从搜索页点击进入问答页，哪怕只有1个答案，也会展示这个按钮）
Xpath_Check_All = '//div[@class="Card ViewAll"][1]/a'
# 二级页问题
Xpath_Answer = '//h1[@class="QuestionHeader-title"]'
# 二级页问题描述
Xpath_Answer_Desc = '//div[@class="css-eew49z"]'
# 二级页整个答案块
Xpath_Questions_Block = '//div[@role="list"]/div'
# 二级页答案块中的答案list
Xpath_Questions = '//div[@role="list"]/*[not(@role="listitem")]'
# 二级页答案块中的每个答案的作者
Xpath_Author = '//div[@class="AuthorInfo-head"]'
# 二级页答案块中的每个答案的内容
Xpath_Question = (
    '//span[@class="RichText ztext CopyrightRichText-richText css-117anjg"]'
)
# 类型二：专题型
Xpath_Article_Title = "//article/header/h1"
Xpath_Article_Content = '//article/div[@class="Post-RichTextContainer"]'


def Initialize(WebSite):
    SaiBrowser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    SaiContext = SaiBrowser.contexts[0]
    SaiContext.route(
        re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.webp.*)"), lambda route: route.abort()
    )
    SaiPage = SaiContext.new_page()
    SaiPage.goto(WebSite)
    SaiPage.wait_for_load_state("networkidle")
    SaiPage.bring_to_front()
    return SaiBrowser, SaiContext, SaiPage


def SaiScroll(ScrollPage, ScrollTimes):
    # 滚动加载更多内容，直到不再加载或者滚动了10次
    NotEnd = True
    ScrollTime = 1
    while NotEnd and ScrollTime < ScrollTimes:
        # 滚动前的页面高度
        BeforeScrollHeight = ScrollPage.evaluate("() => document.body.scrollHeight")
        ScrollTime += 1
        for i in range(3):
            # 滚动到页面底部
            ScrollPage.evaluate("() => window.scrollTo(0,document.body.scrollHeight)")
            # 微上划一下模拟人类
            ScrollPage.keyboard.press("PageUp")
            ScrollPage.wait_for_timeout(random.randint(1000, 3000))
        # 滚动后的页面高度
        AfterScrollHeight = ScrollPage.evaluate("() => document.body.scrollHeight")
        if BeforeScrollHeight == AfterScrollHeight or ScrollTime >= ScrollTimes:
            NotEnd = False


def ExtractQAInfo(WritePage):
    # 问题部分
    Answer = WritePage.query_selector(Xpath_Answer).text_content()
    Answer_Desc = ""
    # 判断问题描述是否存在，有些问题没有描述
    if WritePage.locator(Xpath_Answer_Desc).count() != 0:
        # 判断问题描述是否被收起
        if WritePage.locator(Xpath_Answer_Desc + "//button").count() != 0:
            WritePage.locator(Xpath_Answer_Desc + "//button").click()
        # 因问题描述可能包含图片，故此处使用HTML2Text提取富文本
        Answer_Content_Html = WritePage.query_selector(Xpath_Answer_Desc).inner_html()
        Answer_Desc = MarkDownMaker.handle(Answer_Content_Html)
        with open("test.md", mode="a", encoding="utf-8") as f:
            f.write(
                "### " + Answer + "\n" + "> " + Answer_Desc + "\n\n" + "----" + "\n"
            )
        # 答案部分
        # 判断答案是否存在，有些问题没有答案
        if WritePage.locator(Xpath_Questions_Block).count() != 0:
            # 获取所有答案块
            Elements = WritePage.query_selector_all(Xpath_Questions)
            for element in Elements:
                Author = element.query_selector(Xpath_Author).text_content()
                # 因答案内容可能包含图片，故此处使用HTML2Text提取富文本
                QuestionHtml = element.query_selector(Xpath_Question).inner_html()
                Question = MarkDownMaker.handle(QuestionHtml)
                with open("test.md", mode="a", encoding="utf-8") as f:
                    f.write("##### " + Author + "\n" + Question + "----" + "\n")


# 提取专栏文章
def ExtractZLInfo(WritePage):
    # 因答案内容可能包含图片，故此处使用HTML2Text提取富文本
    Article_Title_Html = WritePage.query_selector(Xpath_Article_Title).inner_html()
    Article_Title = MarkDownMaker.handle(Article_Title_Html)
    Article_Content_Html = WritePage.query_selector(Xpath_Article_Content).inner_html()
    Article_Content = MarkDownMaker.handle(Article_Content_Html)
    with open("test.md", mode="a", encoding="utf-8") as f:
        f.write(
            "### " + Article_Title + "\n" + Article_Content + "\n\n" + "----" + "\n"
        )


def run(playwright: Playwright) -> None:
    # 浏览器预备
    SaiBrowser, SaiContext, SaiPage = Initialize(WebSite)
    # 滚动搜索页获取更多数据
    SaiScroll(SaiPage, 2)
    # 获取搜索结果链接
    Elements = SaiPage.query_selector_all(Xpath_Search_Results)
    for element in Elements:
        if element.query_selector(Xpath_Search_Result_url) is not None:
            with SaiContext.expect_page() as SonPageInfo:
                element.query_selector(Xpath_Search_Result_url).click()
            SonPage = SonPageInfo.value
            SonPage.wait_for_load_state()
            SonPage.bring_to_front()
            if "zhuanlan" in SonPage.url:
                # 专栏页面
                ExtractZLInfo(SonPage)
                SonPage.close()
            elif "zvideo" in SonPage.url:
                # 视频页面不抓取
                pass
            else:
                # 问答页面
                # 点击「查看全部回答」
                SonPage.locator(Xpath_Check_All).click()
                SonPage.wait_for_load_state()
                # 滚动搜索页获取更多数据
                SaiScroll(SonPage, 1)
                # 写入MarkDown
                ExtractQAInfo(SonPage)
                SonPage.close()
    # 收尾
    SaiContext.close()
    SaiBrowser.close()


with sync_playwright() as playwright:
    run(playwright)
```

上述代码直接模拟点击，还可从搜索结果中抽取出结果的url，逐个打开url来进入二级页

> ```python
> Elements = SaiPage.query_selector_all(Xpath_Search_Results)
> for element in Elements:
>     # 判断搜索页的每个节点是否有URL，有就提取出链接，通过链接打开
>     if element.query_selector(Xpath) is not None:
>         elementUrl = element.query_selector(Xpath).get_attribute('content')
>         SonPage = SaiContext.new_page()
>         SonPage.goto(elementUrl)
> ```

* #### 场景三：翻页+提取一级页信息&二级页信息

> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310180107192.png)
> 
> ```python
> import random, os, html2text
> from playwright.sync_api import Playwright, sync_playwright
> 
> # MarkDown文件目录
> MDdir = '/Users/jiangsai/Desktop'
> os.chdir(MDdir)
> MarkDownMaker = html2text.HTML2Text()
> MarkDownMaker.ignore_links = True
> # 待爬的第一个页面
> WebSite = 'https://space.bilibili.com/107861587/video?pn=1'
> # 底部导航Xpath
> Xpath_Nav = '//ul[@class="be-pager"]'
> # 一级页FatherPage的信息块list
> Xpath_FP_Et_List = '//ul[@class="clearfix cube-list"]/*'
> # 一级页FatherPage每个信息块的标题
> Xpath_FP_Et_Title = '//a[@class="title"]'
> # 一级页FatherPage每个信息块的时长
> Xpath_FP_Et_Length = '//span[@class="length"]'
> # 一级页FatherPage每个信息块的播放次数
> Xpath_FP_Et_PlayNum = '//span[@class="play"]'
> # 二级页SonPage的发布时间
> Xpath_SP_Publish_Date = '//span[@class="pubdate-text"]'
> # 二级页SonPage的点赞数
> Xpath_Thumb = '//span[contains(@class,"video-like-info")]'
> 
> 
> # 创建浏览器环境
> def Initialize(WebSite):
>        SaiBrowser = playwright.chromium.connect_over_cdp('http://localhost:9222')
>        SaiContext = SaiBrowser.contexts[0]
>        # SaiContext.route(re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.webp.*)"), lambda route: route.abort())
>        SaiPage = SaiContext.new_page()
>        SaiPage.goto(WebSite)
>        SaiPage.wait_for_load_state("networkidle")
>        SaiPage.bring_to_front()
>        return SaiBrowser, SaiContext, SaiPage
> 
> # 翻页
> def TurnPage(SaiContext, SaiPage):
>        # 所有导航数字集合
>        All_Nav = set()
>        # 已点击导航数字集合
>        Clicked_Nav = set()
>        # 可点击导航数字集合，初始设置为1，即第一页
>        Able_Click_Nav = [1]
>        while len(Able_Click_Nav) > 0:
>            # 取最小导航数
>            To_Click_Nav = Able_Click_Nav[0]
>            # 点击最小导航数
>            # locator('text=1')模糊匹配1,01,10,11等;locator('text="1"')精确匹配1
>            SaiPage.locator(Xpath_Nav).locator('text="'+str(To_Click_Nav)+'"').click()
>            SaiPage.wait_for_timeout(random.randint(1000,3000))
>            # 刚点击的数字追加到「已点击导航数字集合」
>            Clicked_Nav.add(To_Click_Nav)
>            # 当前页导航列表
>            Current_Nav_list = SaiPage.query_selector_all(Xpath_Nav + '/*')
>            for i in Current_Nav_list:
>                Nav_num = i.text_content()
>                # 抽取出导航列表中的数字，「上一页」「下一页」这种非确定性导航都排除
>                if str(Nav_num).isdigit():
>                    All_Nav.add(int(Nav_num))
>            # 可点击导航数字集合 = 所有导航数字集合 ∩ 已点击导航数字集合，再转换成列表
>            Able_Click_Nav= sorted(list(All_Nav.difference(Clicked_Nav)))
>            ExtractFPInfo(SaiContext, SaiPage)
> 
> # 一级页FatherPage信息爬取
> def ExtractFPInfo(SaiContext, FatherPage):
>        Element_Blocks = FatherPage.query_selector_all(Xpath_FP_Et_List)
>        for element in Element_Blocks:
>            Title = element.query_selector(Xpath_FP_Et_Title).text_content()
>            Length = element.query_selector(Xpath_FP_Et_Length).text_content()
>            PlayNum = element.query_selector(Xpath_FP_Et_PlayNum).text_content()
>            with open('test.md', mode='a', encoding='utf-8') as f:
>                f.write('片名：' + Title + '\n' + '时长：' + Length + '\n' + '播放数：' + PlayNum + '\n')
>            # 打开二级页，二级页在新标签加载
>            with SaiContext.expect_page() as SonPageInfo:
>                element.click()
>            SonPage = SonPageInfo.value
>            SonPage.wait_for_load_state()
>            SonPage.bring_to_front()
>            ExtractSPInfo(SonPage)
>            SonPage.close()
> 
> # 二级页SonPage信息爬取
> def ExtractSPInfo(SonPage):
>        Publish_Date = SonPage.query_selector(Xpath_SP_Publish_Date).text_content()
>        Thumb = SonPage.query_selector(Xpath_Thumb).text_content()
>        Publish_Date = Publish_Date.strip() 
>        with open('test.md', mode='a', encoding='utf-8') as f:
>            f.write('发布时间：' + Publish_Date + '\n' + '点赞数：' + Thumb + '\n\n' + '----' + '\n')
> 
> def run(playwright: Playwright) -> None:
>        SaiBrowser, SaiContext, SaiPage = Initialize(WebSite)
>        TurnPage(SaiContext, SaiPage)
>        # 收尾
>        SaiPage.close()
>        SaiContext.close() 
>        SaiBrowser.close()
> 
> with sync_playwright() as playwright:
>        run(playwright)
> ```

---

#### 爬CCP文章

> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310182349285.png)
> 
> > 分析：一级页文章列表，二级页文章正文
> > 
> > 思路：场景三，从一级页列表进入二级页爬取

```python
import random, os, html2text
from playwright.sync_api import Playwright, sync_playwright

# MarkDown文件目录
MDdir = '/Users/jiangsai/Desktop'
os.chdir(MDdir)
MarkDownMaker = html2text.HTML2Text()
MarkDownMaker.ignore_links = True
# 待爬的第一个页面
WebSite = 'http://cpc.people.com.cn/GB/64093/64387/'
# 底部导航Xpath
Xpath_Nav = '//div[@class="page"]'
# 一级页FatherPage标题list
Xpath_FP_Et_List = '//div[@class="fl"]/ul/li'
# 一级页FatherPage每个标题
Xpath_FP_Et_Title = '//a'
# 二级页正文
Xpath_SP_Article = '//div[@class="text_c"]'

# 创建浏览器环境
def Initialize(WebSite):
    SaiBrowser = playwright.chromium.connect_over_cdp('http://localhost:9222')
    SaiContext = SaiBrowser.contexts[0]
    # SaiContext.route(re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.webp.*)"), lambda route: route.abort())
    SaiPage = SaiContext.new_page()
    SaiPage.goto(WebSite)
    SaiPage.wait_for_load_state("networkidle")
    SaiPage.bring_to_front()
    return SaiBrowser, SaiContext, SaiPage

# 翻页
def TurnPage(SaiContext, SaiPage):
    # 所有导航数字集合
    All_Nav = set()
    # 已点击导航数字集合
    Clicked_Nav = set()
    # 可点击导航数字集合，初始设置为1，即第一页
    Able_Click_Nav = [1]
    while len(Able_Click_Nav) > 0:
        # 取最小导航数
        To_Click_Nav = Able_Click_Nav[0]
        # 点击最小导航数
        # locator('text=1')模糊匹配1,01,10,11等;locator('text="1"')精确匹配1
        SaiPage.locator(Xpath_Nav).locator('text="'+str(To_Click_Nav)+'"').click()
        SaiPage.wait_for_timeout(random.randint(1000,3000))
        # 刚点击的数字追加到「已点击导航数字集合」
        Clicked_Nav.add(To_Click_Nav)
        # 当前页导航列表
        Current_Nav_list = SaiPage.query_selector_all(Xpath_Nav + '/*')
        for i in Current_Nav_list:
            Nav_num = i.text_content()
            # 抽取出导航列表中的数字，「上一页」「下一页」这种非确定性导航都排除
            if str(Nav_num).isdigit():
                All_Nav.add(int(Nav_num))
        # 可点击导航数字集合 = 所有导航数字集合 ∩ 已点击导航数字集合，再转换成列表
        Able_Click_Nav= sorted(list(All_Nav.difference(Clicked_Nav)))
        ExtractFPInfo(SaiContext, SaiPage)

# 一级页FatherPage信息爬取
def ExtractFPInfo(SaiContext, FatherPage):
    Element_Blocks = FatherPage.query_selector_all(Xpath_FP_Et_List)
    for element in Element_Blocks:
        # 打开二级页，二级页在新标签加载
        with SaiContext.expect_page() as SonPageInfo:
            element.click()
        SonPage = SonPageInfo.value
        SonPage.wait_for_load_state()
        SonPage.bring_to_front()
        SonPage.wait_for_timeout(random.randint(1000,3000))
        ExtractSPInfo(SonPage)
        SonPage.close()

# 二级页SonPage信息爬取
def ExtractSPInfo(SonPage):
    ArticleHtml = SonPage.query_selector(Xpath_SP_Article).inner_html()
    Article = MarkDownMaker.handle(ArticleHtml)
    with open('test.md', mode='a', encoding='utf-8') as f:
        f.write(Article + '\n\n' + '----' + '\n')

def run(playwright: Playwright) -> None:
    SaiBrowser, SaiContext, SaiPage = Initialize(WebSite)
    TurnPage(SaiContext, SaiPage)
    # 收尾
    SaiPage.close()
    SaiContext.close() 
    SaiBrowser.close()

with sync_playwright() as playwright:
    run(playwright)
```

#### 爬Quora

```python
import os, html2text, re, random
from playwright.sync_api import Playwright, sync_playwright

# MarkDown文件目录
MDdir = "/Users/jiangsai/Desktop"
os.chdir(MDdir)
MarkDownMaker = html2text.HTML2Text()
MarkDownMaker.ignore_links = True
# 待爬的页面
WebSite = "https://ethology.quora.com/What-is-the-most-heroic-and-touching-gesture-ever-made-by-a-human-for-an-animal"
# 类型一：问答型
# 问题
Xpath_Answer = '//div[@class="q-text puppeteer_test_question_title"]'
# 问题描述
# Xpath_Answer_Desc = '//div[@class="css-eew49z"]'
# 整个答案块
# Xpath_Questions_Block = '//div[@role="list"]/div'
# 答案块中的答案list
Xpath_Questions = '//*[@id="mainContent"]/div/div[2]/div'
# 答案块中的每个答案的作者
Xpath_Author = "//div/div/div/div/div/div[1]/div[2]/div/div[1]/div[1]/div/div/div/div/div[2]/div[1]/span[1]"
# 答案块中的每个答案的内容
Xpath_Question = "//div/div/div/div/div/div[1]/div[2]/div/div[1]/div[2]/div"


def Initialize(WebSite):
    SaiBrowser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    SaiContext = SaiBrowser.contexts[0]
    # SaiContext.route(re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.webp.*)"), lambda route: route.abort())
    SaiPage = SaiContext.new_page()
    SaiPage.goto(WebSite)
    SaiPage.wait_for_load_state("networkidle")
    SaiPage.bring_to_front()
    return SaiBrowser, SaiContext, SaiPage


def SaiScroll(ScrollPage, ScrollTimes):
    # 滚动加载更多内容，直到不再加载或者滚动了10次
    NotEnd = True
    ScrollTime = 1
    while NotEnd and ScrollTime < ScrollTimes:
        # 滚动前的页面高度
        BeforeScrollHeight = ScrollPage.evaluate("() => document.body.scrollHeight")
        ScrollTime += 1
        for i in range(3):
            # 滚动到页面底部
            ScrollPage.evaluate("() => window.scrollTo(0,document.body.scrollHeight)")
            # 微上划一下模拟人类
            ScrollPage.keyboard.press("PageUp")
            ScrollPage.wait_for_timeout(random.randint(1000, 3000))
        # 滚动后的页面高度
        AfterScrollHeight = ScrollPage.evaluate("() => document.body.scrollHeight")
        if BeforeScrollHeight == AfterScrollHeight or ScrollTime >= ScrollTimes:
            NotEnd = False
    # 点开每一个答案的「(more)」来查看更多
    MoreClicks = ScrollPage.query_selector_all('text="(more)"')
    for eliment in MoreClicks:
        eliment.click()
        ScrollPage.wait_for_timeout(random.randint(1000, 3000))
    return ScrollPage


def ExtractQAInfo(WritePage):
    # 问题部分
    Answer = WritePage.query_selector(Xpath_Answer).text_content()
    Answer_Desc = ""
    # # 判断问题描述是否存在，有些问题没有描述
    # if WritePage.locator(Xpath_Answer_Desc).count() != 0:
    #     # 判断问题描述是否被收起
    #     if WritePage.locator(Xpath_Answer_Desc + "//button").count() != 0:
    #         WritePage.locator(Xpath_Answer_Desc + "//button").click()
    #     # 因问题描述可能包含图片，故此处使用HTML2Text提取富文本
    #     Answer_Content_Html = WritePage.query_selector(Xpath_Answer_Desc).inner_html()
    #     Answer_Desc = MarkDownMaker.handle(Answer_Content_Html)
    with open("test.md", mode="a", encoding="utf-8") as f:
        f.write("### " + Answer + "\n" + "> " + Answer_Desc + "\n\n" + "----" + "\n")
    # 答案部分
    Elements = WritePage.query_selector_all(Xpath_Questions)
    # 分析源码发现Elements的第1个和最后一个都不是答案，故删除
    del Elements[0]
    del Elements[-1]
    for element in Elements:
        # 有些答案莫名没加载出来，就不要这个答案了
        if element.query_selector(Xpath_Author) is not None:
            Author = element.query_selector(Xpath_Author).text_content()
            # 因答案内容可能包含图片，故此处使用HTML2Text提取富文本
            QuestionHtml = element.query_selector(Xpath_Question).inner_html()
            Question = MarkDownMaker.handle(QuestionHtml)
            with open("test.md", mode="a", encoding="utf-8") as f:
                f.write("##### " + Author + "\n" + Question + "----" + "\n")


def run(playwright: Playwright) -> None:
    SaiBrowser, SaiContext, SaiPage = Initialize(WebSite)
    # 滚动搜索页获取更多数据
    SaiPage = SaiScroll(SaiPage, 5)
    # 写入MarkDown
    ExtractQAInfo(SaiPage)
    # 收尾
    SaiPage.close()
    SaiContext.close()
    SaiBrowser.close()


with sync_playwright() as playwright:
    run(playwright)
```

