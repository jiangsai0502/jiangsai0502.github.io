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
  >   >   >
  >   >   >    ```bash
  >   >   >    /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
  >   >   >    ```
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
  >   >   3. 滚动到页面顶部
  >   >
  >   >      `page.evaluate("() => window.scrollTo(0,0)")`
  >   >
  >   >   4. 向下滚动一屏
  >   >
  >   >      `page.evaluate("() => window.scrollBy(0,window.innerHeight)")`
  >   >
  >   >   5. 向上滚动一屏
  >   >
  >   >      `page.evaluate("() => window.scrollBy(0,-window.innerHeight)")`
  >   >
  >   >   6. 滚动到当前元素位置
  >   >
  >   >      `element = page.locator(xpath)` 或 `element = page.query_selector(xpath)`
  >   >
  >   >      `element.evaluate("element => element.scrollIntoView()")`
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
  >   > * 判断某个节点是否有直接子节点存在
  >   >
  >   >   > 平时可以直接用简写语句`'//div'`的双斜杠开头表示，这是个xpath，但是需要用到单斜杠时，就必须用到完整语句`'xpath=/div'`，`'xpath=/span'`，`'xpath=/*'`
  >   >   >
  >   >   > ```python
  >   >   > if root_element.query_selector_all("xpath=/*") is not None:
  >   >   >        pass
  >   >   > ```
  >   >   
  >   > * 移除某个节点
  >   >
  >   >   ```python
  >   >   Target_node = WritePage.query_selector(Xpath)
  >   >   Target_node_remove = Target_node.query_selector(Xpath)
  >   >   Target_node_remove.evaluate("element => element.remove()")
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
  >   > 
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
> 伪代码
>
> > > 准备工作：初始化浏览器、初始化写入方法、页面滚动
> >
> > 1. 判断页面类型：问答题？专栏？视频？
> > 2. 问答题
> >    1. 滚动加载全部答案
> >    2. 问题：获取问题标题 -> 展示收起的问题描述 -> 获取markdown描述
> >    3. 答案：获取答案list -> 获取每个答案的作者 -> 获取markdown内容
> > 3. 专栏
> >    * 获取专栏页的markdown内容
> > 4. 视频
> >    * 不爬

```python
import os, html2text, re, random
from playwright.sync_api import Playwright, sync_playwright


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
Xpath_Question = '//span[@class="RichText ztext CopyrightRichText-richText css-117anjg"]'
# 类型二：专题型
Xpath_Article_Title = "//article/header/h1"
Xpath_Article_Content = '//article/div[@class="Post-RichTextContainer"]'


# 初始化浏览器：调用本地Chrome，在新标签打开目标网页，并切换到该标签
def InitialChrome(WebSite):
    SaiBrowser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    SaiContext = SaiBrowser.contexts[0]
    SaiContext.route(
        re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.gif.*)|(.*\.webp.*)"), lambda route: route.abort()
    )
    SaiPage = SaiContext.new_page()
    SaiPage.goto(WebSite)
    SaiPage.bring_to_front()
    SaiPage.wait_for_load_state("networkidle")
    return SaiBrowser, SaiContext, SaiPage


# 初始化写入方法：切换到目标路径，将网页标题处理成合法文件名
def InitialMDFile(SaiPage):
    # 切换MarkDown文件目录
    MDdir = "/Users/jiangsai/Desktop"
    os.chdir(MDdir)
    # 声明全局MarkDown文件操作类
    global MarkDownMaker
    MarkDownMaker = html2text.HTML2Text()
    MarkDownMaker.ignore_links = True
    # 知乎网页标题格式：(99+ 封私信 / 81 条消息) 期货怎么才能赚钱？ - 知乎
    # 处理MarkDown文件名
    MDFile = SaiPage.title()
    # 文件名中不能含有'.', '/', ':' 这些字符
    replace_dict = {".": "_", "/": "_", ":": "_", " ": "_"}
    # 遍历字典的键值对，将字符串中的每一个键都替换为对应的值
    for key, value in replace_dict.items():
        MDFile = MDFile.replace(key, value)
    # 将重复的'_'替换为1个
    MDFile = re.sub(r"(_)\1+", "_", MDFile)
    # 将括号和括号中的字符替换掉
    MDFile = re.sub(r"\((.*?)\)", "", MDFile)
    # 声明全局MarkDown文件路径
    global MDFileDir
    MDFileDir = f"{MDdir}/{MDFile}.md"


# 页面滚动方法：对指定页面，滚动指定次数或滚动到底
def PageScroll(ScrollPage, ScrollTimes):
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


# 获取问答页信息
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
    with open(MDFileDir, mode="a", encoding="utf-8") as f:
        f.write("### " + Answer + "\n" + "> " + Answer_Desc + "\n\n" + "----" + "\n")
    # 答案部分
    # 判断答案是否存在，有些问题没有答案
    if WritePage.locator(Xpath_Questions_Block).count() != 0:
        # 获取所有答案块
        Elements = WritePage.query_selector_all(Xpath_Questions)
        for element in Elements:
            # 滚动到当前元素位置
            element.evaluate("element => element.scrollIntoView()")
            Author = element.query_selector(Xpath_Author).text_content()
            # 因答案内容可能包含图片，故此处使用HTML2Text提取富文本
            QuestionHtml = element.query_selector(Xpath_Question).inner_html()
            Question = MarkDownMaker.handle(QuestionHtml)
            with open(MDFileDir, mode="a", encoding="utf-8") as f:
                f.write("##### " + Author + "\n" + Question + "----" + "\n")


# 获取专栏页信息
def ExtractZLInfo(WritePage):
    # 因答案内容可能包含图片，故此处使用HTML2Text提取富文本
    Article_Title_Html = WritePage.query_selector(Xpath_Article_Title).inner_html()
    Article_Title = MarkDownMaker.handle(Article_Title_Html)
    Article_Content_Html = WritePage.query_selector(Xpath_Article_Content).inner_html()
    Article_Content = MarkDownMaker.handle(Article_Content_Html)
    with open(MDFileDir, mode="a", encoding="utf-8") as f:
        f.write("### " + Article_Title + "\n" + Article_Content + "\n\n" + "----" + "\n")


def run(playwright: Playwright) -> None:
    WebSite = input("请输入要爬取的知乎网址: ")
    SaiBrowser, SaiContext, SaiPage = InitialChrome(WebSite)
    InitialMDFile(SaiPage)
    # 专栏页面
    if "zhuanlan" in SaiPage.url:
        ExtractZLInfo(SaiPage)
    # 视频页面不抓取
    elif "zvideo" in SaiPage.url:
        pass
    # 问答页面
    else:
        PageScroll(SaiPage, 1)
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
> 伪代码
>
> > > 准备工作：初始化浏览器、初始化写入方法、页面滚动
> >
> > 1. 获取一级页条目list，并逐个点击进入二级页
> > 2. 判断页面类型：问答题？专栏？视频？
> > 3. 问答题
> >    1. 滚动加载全部答案
> >    2. 问题：获取问题标题 -> 展示收起的问题描述 -> 获取markdown描述
> >    3. 答案：获取答案list -> 获取每个答案的作者 -> 获取markdown内容
> > 4. 专栏
> >    * 获取专栏页的markdown内容
> > 5. 视频
> >    * 不爬

```python
import os, html2text, re, random
from playwright.sync_api import Playwright, sync_playwright

#########################全局变量#########################
# 搜索结果页每个结果标题的url
Xpath_Search_Result_urls = '//h2[@class="ContentItem-title"]//div/a'
###########类型一：问答型###########
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
Xpath_Question = '//span[@class="RichText ztext CopyrightRichText-richText css-117anjg"]'
###########类型二：专题型###########
Xpath_Article_Title = "//article/header/h1"
Xpath_Article_Content = '//article/div[@class="Post-RichTextContainer"]'
#########################全局变量#########################


# 初始化浏览器：调用本地Chrome，在新标签打开目标网页，并切换到该标签
def InitialChrome(WebSite):
    SaiBrowser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    SaiContext = SaiBrowser.contexts[0]
    SaiContext.route(
        re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.gif.*)|(.*\.webp.*)"), lambda route: route.abort()
    )
    SaiPage = SaiContext.new_page()
    SaiPage.goto(WebSite)
    SaiPage.bring_to_front()
    SaiPage.wait_for_load_state("networkidle")
    return SaiBrowser, SaiContext, SaiPage


# 初始化写入方法：切换到目标路径，指定文件名
def InitialMDFile(MDdir, MDFile):
    # 切换MarkDown文件目录
    os.chdir(MDdir)
    # 声明全局MarkDown文件操作类
    global MarkDownMaker
    MarkDownMaker = html2text.HTML2Text()
    MarkDownMaker.ignore_links = True
    # 声明全局MarkDown文件路径
    global MDFileDir
    MDFileDir = f"{MDdir}/{MDFile}"


# 页面滚动方法：对指定页面，滚动指定次数或滚动到底
def SaiScroll(ScrollPage, ScrollTimes):
    # 滚动加载更多内容，直到不再加载或者滚动了10次
    NotEnd = True
    ScrollTime = 1
    while NotEnd and ScrollTime < ScrollTimes:
        # 滚动前的页面高度
        BeforeScrollHeight = ScrollPage.evaluate("() => document.body.scrollHeight")
        ScrollTime += 1
        # 向下滚动一屏
        ScrollPage.evaluate("() => window.scrollBy(0,window.innerHeight)")
        ScrollPage.wait_for_timeout(random.randint(500, 1000))
        # 滚动后的页面高度
        AfterScrollHeight = ScrollPage.evaluate("() => document.body.scrollHeight")
        if BeforeScrollHeight == AfterScrollHeight or ScrollTime >= ScrollTimes:
            NotEnd = False


# 通过搜索结果进入二级页
def FromSearchResultsToSonPage(SaiContext, FatherPage):
    # 获取搜索结果链接
    Result_urls = FatherPage.query_selector_all(Xpath_Search_Result_urls)
    for element in Result_urls:
        if element is not None:
            # 点击每个搜索结果标题，进入二级页
            with SaiContext.expect_page() as SonPageInfo:
                # 滚动到当前元素位置
                element.evaluate("element => element.scrollIntoView()")
                element.click()
            SonPage = SonPageInfo.value
            SonPage.wait_for_timeout(random.randint(1000, 2000))
            # 视频页面不抓取
            if "zvideo" in SonPage.url:
                SonPage.close()
            else:
                SonPage.bring_to_front()
                SonPage.wait_for_load_state()
                # 专栏页面
                if "zhuanlan" in SonPage.url:
                    # 写入MarkDown
                    GetZhuanLanInfo(SonPage)
                    SonPage.close()
                # 问答页面
                else:
                    # 点击「查看全部回答」
                    SonPage.locator(Xpath_Check_All).click()
                    SonPage.wait_for_load_state()
                    # 滚动搜索页获取更多数据
                    SaiScroll(SonPage, 1)
                    GetQAInfo(SonPage)
                    SonPage.close()


# 获取问答页内容
def GetQAInfo(WritePage):
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
        with open(MDFileDir, mode="a", encoding="utf-8") as f:
            f.write("### " + Answer + "\n" + "> " + Answer_Desc + "\n\n" + "----" + "\n")
    # 答案部分
    # 判断答案是否存在，有些问题没有答案
    if WritePage.locator(Xpath_Questions_Block).count() != 0:
        # 获取所有答案块
        Elements = WritePage.query_selector_all(Xpath_Questions)
        for element in Elements:
            # 滚动到当前元素位置
            element.evaluate("element => element.scrollIntoView()")
            Author = element.query_selector(Xpath_Author).text_content()
            # 因答案内容可能包含图片，故此处使用HTML2Text提取富文本
            QuestionHtml = element.query_selector(Xpath_Question).inner_html()
            Question = MarkDownMaker.handle(QuestionHtml)
            with open(MDFileDir, mode="a", encoding="utf-8") as f:
                f.write("##### " + Author + "\n" + Question + "----" + "\n")


# 获取专栏文章内容
def GetZhuanLanInfo(WritePage):
    # 因答案内容可能包含图片，故此处使用HTML2Text提取富文本
    Article_Title_Html = WritePage.query_selector(Xpath_Article_Title).inner_html()
    Article_Title = MarkDownMaker.handle(Article_Title_Html)
    Article_Content_Html = WritePage.query_selector(Xpath_Article_Content).inner_html()
    Article_Content = MarkDownMaker.handle(Article_Content_Html)
    with open(MDFileDir, mode="a", encoding="utf-8") as f:
        f.write("### " + Article_Title + "\n" + Article_Content + "\n\n" + "----" + "\n")


def run(playwright: Playwright) -> None:
    WebSite = input("请输入要爬取的知乎搜索网址: ")
    SaiBrowser, SaiContext, SaiPage = InitialChrome(WebSite)
    # MarkDown文件目录
    MDdir = "/Users/jiangsai/Desktop"
    # MarkDown文件名
    MDFile = "Test.md"
    # 初始化MarkDown操作方法
    InitialMDFile(MDdir, MDFile)
    # 滚动搜索页获取更多数据
    SaiScroll(SaiPage, 2)
    # 获取搜索结果的全部内容
    FromSearchResultsToSonPage(SaiContext, SaiPage)
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
> 伪代码
>
> > > 准备工作：初始化浏览器、初始化写入方法、页面滚动
> >
> > 1. 获取一级页条目list，提取每个条目信息
> > 2. 逐个点击进入二级页，提取二级页信息
> > 3. 翻页

```python
import random, os, html2text, re
from playwright.sync_api import Playwright, sync_playwright

#########################全局变量#########################
# 底部导航Xpath
Xpath_Nav = '//ul[@class="be-pager"]'
# 一级页FatherPage的信息块list
Xpath_FP_Block_List = '//ul[@class="clearfix cube-list"]/*'
# 一级页FatherPage每个信息块的标题
Xpath_FP_Block_Title = '//a[@class="title"]'
# 一级页FatherPage每个信息块的时长
Xpath_FP_Block_Length = '//span[@class="length"]'
# 一级页FatherPage每个信息块的播放次数
Xpath_FP_Block_PlayNum = '//span[@class="play"]'
# 二级页SonPage的发布时间
Xpath_SP_Publish_Date = '//span[@class="pubdate-text"]'
# 二级页SonPage的点赞数
Xpath_Thumb = '//span[contains(@class,"video-like-info")]'
# 翻页导航全部数字
All_Nav = set()
# 翻页导航点击过的数字
Clicked_Nav = set()
# 翻页导航可点击数字
Able_Click_Nav = []
# 是否第1个导航
Is_First_Nav = True
# 是否已点击完所有导航
Finish_Nav = False
#########################全局变量#########################


# 初始化浏览器：调用本地Chrome，在新标签打开目标网页，并切换到该标签
def InitialChrome(WebSite):
    SaiBrowser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    SaiContext = SaiBrowser.contexts[0]
    SaiContext.route(
        re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.gif.*)|(.*\.webp.*)"), lambda route: route.abort()
    )
    SaiPage = SaiContext.new_page()
    SaiPage.goto(WebSite)
    SaiPage.bring_to_front()
    SaiPage.wait_for_load_state("networkidle")
    return SaiBrowser, SaiContext, SaiPage


# 初始化写入方法：切换到目标路径，指定文件名
def InitialMDFile(MDdir, MDFile):
    # 切换MarkDown文件目录
    os.chdir(MDdir)
    # 声明全局MarkDown文件操作类
    global MarkDownMaker
    MarkDownMaker = html2text.HTML2Text()
    MarkDownMaker.ignore_links = True
    # 声明全局MarkDown文件路径
    global MDFileDir
    MDFileDir = f"{MDdir}/{MDFile}"


# 翻页
def TurnPage(FatherPage):
    global All_Nav
    global Clicked_Nav
    global Able_Click_Nav
    global Is_First_Nav
    global Finish_Nav
    # 当前页导航列表
    Current_Nav_list = FatherPage.query_selector_all(Xpath_Nav + "/*")
    for i in Current_Nav_list:
        Nav_num = i.text_content()
        # 抽取出导航列表中的数字，「上一页」「下一页」这种非确定性导航都排除
        if str(Nav_num).isdigit():
            All_Nav.add(int(Nav_num))
    # 若本页是第1页，则不用点击
    if Is_First_Nav == True:
        # 取所有导航数列表中最小的数为即将点击的数
        To_Click_Nav = sorted(list(All_Nav))[0]
        pass
    else:
        # 取可点击列表的最小导航数为即将点击的数
        To_Click_Nav = Able_Click_Nav[0]
        # 点击最小导航数
        # locator('text=1')模糊匹配1,01,10,11等;locator('text="1"')精确匹配1
        FatherPage.locator(Xpath_Nav).locator('text="' + str(To_Click_Nav) + '"').click()
        FatherPage.wait_for_timeout(random.randint(1000, 3000))
    # 刚点击的数字追加到「已点击导航数字集合」
    Clicked_Nav.add(To_Click_Nav)
    Is_First_Nav = False
    # 可点击导航数字集合 = 所有导航数字集合 ∩ 已点击导航数字集合，再转换成列表
    Able_Click_Nav = sorted(list(All_Nav.difference(Clicked_Nav)))
    if len(Able_Click_Nav) == 0:
        Finish_Nav = True


# 获取一级页FatherPage信息（直接定位到目标信息）
def GetFatherPageInfo(block):
    Title = block.query_selector(Xpath_FP_Block_Title).text_content()
    Length = block.query_selector(Xpath_FP_Block_Length).text_content()
    PlayNum = block.query_selector(Xpath_FP_Block_PlayNum).text_content()
    with open(MDFileDir, mode="a", encoding="utf-8") as f:
        f.write("片名：" + Title + "\n" + "时长：" + Length + "\n" + "播放数：" + PlayNum + "\n")


# 获取二级页SonPage信息
def GetSonPageInfo(SaiContext, block):
    # 在新标签加载二级页
    with SaiContext.expect_page() as SonPageInfo:
        block.click()
    SonPage = SonPageInfo.value
    SonPage.wait_for_load_state()
    SonPage.bring_to_front()
    # 抓取二级页信息
    Publish_Date = SonPage.query_selector(Xpath_SP_Publish_Date).text_content()
    Thumb = SonPage.query_selector(Xpath_Thumb).text_content()
    Publish_Date = Publish_Date.strip()
    with open(MDFileDir, mode="a", encoding="utf-8") as f:
        f.write("发布时间：" + Publish_Date + "\n" + "点赞数：" + Thumb + "\n\n" + "----" + "\n")
    SonPage.close()


# 获取信息
def GetInfo(SaiContext, FatherPage):
    global Finish_Nav
    # 持续取本页的数据，直到导航到最后一页
    while True:
        TurnPage(FatherPage)
        # 列出每个一级页信息块
        Blocks = FatherPage.query_selector_all(Xpath_FP_Block_List)
        for block in Blocks:
            # 获取每个一级页信息块的具体信息
            GetFatherPageInfo(block)
            # 获取每个一级页信息块的二级页的具体信息
            GetSonPageInfo(SaiContext, block)
            FatherPage.wait_for_timeout(random.randint(1000, 3000))
        if Finish_Nav == True:
            break


def run(playwright: Playwright) -> None:
    WebSite = "https://space.bilibili.com/111082383/video"
    # WebSite = input("请输入要爬的网址: ")
    SaiBrowser, SaiContext, SaiPage = InitialChrome(WebSite)
    # MarkDown文件目录
    MDdir = "/Users/jiangsai/Desktop"
    # MarkDown文件名
    MDFile = "Test.md"
    # 初始化MarkDown操作方法
    InitialMDFile(MDdir, MDFile)
    # 获取目标信息
    GetInfo(SaiContext, SaiPage)

    # 收尾
    SaiPage.close()
    SaiContext.close()
    SaiBrowser.close()


with sync_playwright() as playwright:
    run(playwright)
```

> **逐个遍历整个HTML文件，直到找到目标信息**

```python
def ExtractFPInfo(SaiContext, FatherElement):
 Infor_Elements = FatherElement.query_selector_all("xpath=/*")
 # 逐个进入子节点
 for Infor_E in Infor_Elements:
     # 页面不展示的内容就不爬了
     if Infor_E.get_attribute("style") == "display: none;":
         continue
     else:
         Title_Num = len(Infor_E.query_selector_all(Xpath_FP_Et_Title))
         if Title_Num > 0:
             if Title_Num == 1:
                 Title = Infor_E.query_selector(Xpath_FP_Et_Title).text_content()
                 Length = Infor_E.query_selector(Xpath_FP_Et_Length).text_content()
                 PlayNum = Infor_E.query_selector(Xpath_FP_Et_PlayNum).text_content()
                 with open("test.md", mode="a", encoding="utf-8") as f:
                     f.write("片名：" + Title + "\n" + "时长：" + Length + "\n" + "播放数：" + PlayNum + "\n")
                 # 打开二级页，二级页在新标签加载
                 with SaiContext.expect_page() as SonPageInfo:
                     Infor_E.query_selector(Xpath_FP_Et_Title).click()
                 SonPage = SonPageInfo.value
                 SonPage.wait_for_load_state()
                 SonPage.bring_to_front()
                 ExtractSPInfo(SonPage)
                 SonPage.close()
             else:
                 if Infor_E.query_selector_all("xpath=/*") is not None:
                     ExtractFPInfo(SaiContext, Infor_E)
```



---

#### 爬CCP文章

> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310182349285.png)
>
> 伪代码
>
> > > 准备工作：初始化浏览器、初始化写入方法、翻页
> >
> > 1. 获取一级页条目list
> > 2. 逐个点击进入二级页，提取二级页信息
> > 3. 翻页

```python
import random, os, html2text, re
from playwright.sync_api import Playwright, sync_playwright

#########################全局变量#########################
# 待爬的第一个页面
WebSite = "http://dangjian.people.com.cn/GB/394443/index.html"
# 底部导航Xpath
Xpath_Nav = '//div[@class="page"]'
# 一级页FatherPage标题list
Xpath_FP_Title_List = '//div[@class="fl"]/ul/li'
# 一级页FatherPage每个标题
Xpath_FP_Title = "//a"
# 二级页正文
Xpath_SP_Article = '//div[@class="text_c"]'
# 翻页导航全部数字
All_Nav = set()
# 翻页导航点击过的数字
Clicked_Nav = set()
# 翻页导航可点击数字
Able_Click_Nav = []
# 是否第1个导航
Is_First_Nav = True
# 是否已点击完所有导航
Finish_Nav = False
#########################全局变量#########################


# 初始化浏览器：调用本地Chrome，在新标签打开目标网页，并切换到该标签
def InitialChrome(WebSite):
    SaiBrowser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    SaiContext = SaiBrowser.contexts[0]
    SaiContext.route(
        re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.gif.*)|(.*\.webp.*)"), lambda route: route.abort()
    )
    SaiPage = SaiContext.new_page()
    SaiPage.goto(WebSite)
    SaiPage.bring_to_front()
    SaiPage.wait_for_load_state("networkidle")
    return SaiBrowser, SaiContext, SaiPage


# 初始化写入方法：切换到目标路径，指定文件名
def InitialMDFile(MDdir, MDFile):
    # 切换MarkDown文件目录
    os.chdir(MDdir)
    # 声明全局MarkDown文件操作类
    global MarkDownMaker
    MarkDownMaker = html2text.HTML2Text()
    MarkDownMaker.ignore_links = True
    # 声明全局MarkDown文件路径
    global MDFileDir
    MDFileDir = f"{MDdir}/{MDFile}"


# 翻页
def TurnPage(FatherPage):
    global All_Nav
    global Clicked_Nav
    global Able_Click_Nav
    global Is_First_Nav
    global Finish_Nav
    # 当前页导航列表
    Current_Nav_list = FatherPage.query_selector_all(Xpath_Nav + "/*")
    for i in Current_Nav_list:
        Nav_num = i.text_content()
        # 抽取出导航列表中的数字，「上一页」「下一页」这种非确定性导航都排除
        if str(Nav_num).isdigit():
            All_Nav.add(int(Nav_num))
    # 若本页是第1页，则不用点击
    if Is_First_Nav == True:
        # 取所有导航数列表中最小的数为即将点击的数
        To_Click_Nav = sorted(list(All_Nav))[0]
        pass
    else:
        # 取可点击列表的最小导航数为即将点击的数
        To_Click_Nav = Able_Click_Nav[0]
        # 点击最小导航数
        # locator('text=1')模糊匹配1,01,10,11等;locator('text="1"')精确匹配1
        FatherPage.locator(Xpath_Nav).locator('text="' + str(To_Click_Nav) + '"').click()
        FatherPage.wait_for_timeout(random.randint(1000, 3000))
    # 刚点击的数字追加到「已点击导航数字集合」
    Clicked_Nav.add(To_Click_Nav)
    Is_First_Nav = False
    # 可点击导航数字集合 = 所有导航数字集合 ∩ 已点击导航数字集合，再转换成列表
    Able_Click_Nav = sorted(list(All_Nav.difference(Clicked_Nav)))
    if len(Able_Click_Nav) == 0:
        Finish_Nav = True


# 获取信息
def GetInfo(SaiContext, FatherPage):
    global Finish_Nav
    # 持续取本页的数据，直到导航到最后一页
    while True:
        TurnPage(FatherPage)
        # 列出每个一级页信息块
        Son_Page_Titles = FatherPage.query_selector_all(Xpath_FP_Title_List)
        for SP_Title in Son_Page_Titles:
            # 获取每个一级页信息块的二级页的具体信息
            GetSonPageInfo(SaiContext, SP_Title)
            FatherPage.wait_for_timeout(random.randint(1000, 3000))
        if Finish_Nav == True:
            break


# 获取二级页SonPage信息
def GetSonPageInfo(SaiContext, SP_Title):
    # 在新标签加载二级页
    with SaiContext.expect_page() as SonPageInfo:
        SP_Title.click()
    SonPage = SonPageInfo.value
    SonPage.wait_for_load_state()
    SonPage.bring_to_front()
    # 抓取二级页信息
    ArticleHtml = SonPage.query_selector(Xpath_SP_Article).inner_html()
    Article = MarkDownMaker.handle(ArticleHtml)
    with open(MDFileDir, mode="a", encoding="utf-8") as f:
        f.write(Article + "\n\n" + "----" + "\n")
    SonPage.close()


def run(playwright: Playwright) -> None:
    # WebSite = input("请输入要爬的网址: ")
    SaiBrowser, SaiContext, SaiPage = InitialChrome(WebSite)
    # MarkDown文件目录
    MDdir = "/Users/jiangsai/Desktop"
    # MarkDown文件名
    MDFile = "Test.md"
    # 初始化MarkDown操作方法
    InitialMDFile(MDdir, MDFile)
    # 获取目标信息
    GetInfo(SaiContext, SaiPage)

    # 收尾
    SaiPage.close()
    SaiContext.close()
    SaiBrowser.close()


with sync_playwright() as playwright:
    run(playwright)
```

#### Quora

> quora的HTML节点层级非常非常多，且几乎找不到唯一性，故使用如下穷举的策略
>
> * 从顶部节点开始，一级一级列出所有子节点，逐个检测子节点是否包含答题者和答案
>   * 若不包含则切到下一个子节点
>   * 若包含则判断数量是否唯一
>     * 若唯一，则写入
>     * 若不唯一，则调用自身，列出自己的所有子节点
>
> 伪代码
>
> > > 准备工作：初始化浏览器、初始化写入方法、页面滚动
> >
> > 1. 滚动加载全部答案
> > 2. 问题：获取问题标题
> > 3. 答案：获取答案list -> 获取每个答案的作者 -> 点击展开每个答案内容 -> 获取markdown内容

```python
import os, html2text, re, random
from playwright.sync_api import Playwright, sync_playwright

#########################全局变量#########################
# 问题
Xpath_Answer = '//div[@class="q-text puppeteer_test_question_title"]'
# 答案块中的每个答案的作者
Xpath_Author = '//div[@class="q-inlineFlex qu-alignItems--center qu-wordBreak--break-word"]'
# 答案块中的每个答案的内容
Xpath_Question = '//div[@class="q-box spacing_log_answer_content puppeteer_test_answer_content"]'
#########################全局变量#########################


# 初始化浏览器：调用本地Chrome，在新标签打开目标网页，并切换到该标签
def InitialChrome(WebSite):
    SaiBrowser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    SaiContext = SaiBrowser.contexts[0]
    # quora只要加这个规则就触发反爬
    # SaiContext.route(re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.webp.*)"), lambda route: route.abort())
    SaiPage = SaiContext.new_page()
    SaiPage.goto(WebSite)
    SaiPage.bring_to_front()
    # quora只要加这个规则就触发超时
    # SaiPage.wait_for_load_state("networkidle")
    SaiPage.wait_for_timeout(random.randint(3000, 5000))
    return SaiBrowser, SaiContext, SaiPage


# 初始化写入方法：切换到目标路径，将网页标题处理成合法文件名
def InitialMDFile(MDFile, MDdir):
    # 切换MarkDown文件目录
    os.chdir(MDdir)
    # 声明全局MarkDown文件操作类
    global MarkDownMaker
    MarkDownMaker = html2text.HTML2Text()
    MarkDownMaker.ignore_links = True
    # MarkDown文件名中不能含有'.', '/', ':' 全替换成_
    replace_dict = {".": "_", "/": "_", ":": "_", " ": "_"}
    # 遍历字典的键值对，将字符串中的键替换为对应的值
    for key, value in replace_dict.items():
        MDFile = MDFile.replace(key, value)
    # 将重复的'_'替换为1个
    MDFile = re.sub(r"(_)\1+", "_", MDFile)
    # 声明全局MarkDown文件路径
    global MDFileDir
    MDFileDir = f"{MDdir}/{MDFile}.md"


# 页面滚动方法：对指定页面，滚动指定次数或滚动到底，并点开每一个收起的答案
def PageScroll(ScrollPage, ScrollTimes):
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
    # 点开每一个答案的「(more)」或「Continue Reading」来查看更多
    MoreClicks = ScrollPage.query_selector_all('text="(more)"')
    ContinueReading = ScrollPage.query_selector_all('text="Continue Reading"')
    for eliment in MoreClicks:
        eliment.click()
        ScrollPage.wait_for_timeout(random.randint(1000, 3000))
    for eliment in ContinueReading:
        eliment.click()
        ScrollPage.wait_for_timeout(random.randint(1000, 3000))
    return ScrollPage


# 获取页面信息
def GetInfo(WritePage):
    # 获取问题信息
    Answer = WritePage.query_selector(Xpath_Answer).text_content()
    with open("test.md", mode="a", encoding="utf-8") as f:
        f.write("### " + Answer + "\n" + "----" + "\n")
    # 获取答案信息
    if WritePage.query_selector_all("xpath=/*") is not None:
        Son_Elements = WritePage.query_selector_all("xpath=/*")
        for Son_E in Son_Elements:
            Author_Num = len(Son_E.query_selector_all(Xpath_Author))
            Question_Num = len(Son_E.query_selector_all(Xpath_Question))
            if Author_Num > 0 and Question_Num > 0:
                if Author_Num == 1 and Question_Num == 1:
                    # 滚动到当前元素位置
                    element.evaluate("element => element.scrollIntoView()")
                    Author = Son_E.query_selector(Xpath_Author).text_content()
                    # 因答案内容可能包含图片，故此处使用HTML2Text提取富文本
                    QuestionHtml = Son_E.query_selector(Xpath_Question).inner_html()
                    Question = MarkDownMaker.handle(QuestionHtml)
                    # 图片链接有些被莫名增加了换行，句子中间也莫名增加了换行
                    Question = Question.replace("-\n", "-").replace("\n", " ").replace("  ", "\n\n")
                    with open("test.md", mode="a", encoding="utf-8") as f:
                        f.write("##### " + Author + "\n" + Question + "----" + "\n")
                else:
                    if Son_E.query_selector_all("xpath=/*") is not None:
                        ExtractAnswersInfo(Son_E)
                    else:
                        print("见鬼了")


def run(playwright: Playwright) -> None:
    # https://www.quora.com/How-advanced-is-high-speed-rail-in-China
    WebSite = input("请输入要爬取的quora网址: ")
    SaiBrowser, SaiContext, SaiPage = InitialChrome(WebSite)
    # MarkDown文件目录
    MDdir = "/Users/jiangsai/Desktop"
    # MarkDown文件名
    MDFile = SaiPage.title()
    # 初始化MarkDown操作方法
    InitialMDFile(MDdir, MDFile)
    # 滚动指定次数
    SaiPage = PageScroll(SaiPage, 1)
    # 获取页面信息
    GetInfo(SaiPage)
    # 收尾
    SaiPage.close()
    SaiContext.close()
    SaiBrowser.close()


with sync_playwright() as playwright:
    run(playwright)
```

#### 贴吧

> 准备工作：初始化浏览器、初始化写入方法、页面滚动
>
> 1. 滚动加载全部可见内容
> 2. 获取标题
> 3. 获取所有楼层
>    1. 获取楼层信息：作者、回答时间、MarkDown内容
>    2. 获取楼层评论
>       1. 若评论被折腾，点击「点击查看」展开
>       2. 获取每条评论：作者、文字内容
>       3. 评论翻页
> 4. 页面翻页

```python
import random, os, html2text, re
from playwright.sync_api import Playwright, sync_playwright


# 页面底部导航
Xpath_Page_Nav = '//div[@class="pb_footer"]//li[contains(@class, "l_pager")]'
# 帖子标题
Xpath_Post_Title = '//*[contains(@class,"core_title_txt")]'
# 当前页的帖子回复楼层list
Xpath_Floors = '//div[contains(@class, "p_postlist")]/*'
# 帖子回复楼层作者
Xpath_Floor_Author = '//ul[@class="p_author"]/li[@class="d_name"]/a'
# 帖子回复楼层时间
Xpath_Floor_Time = '//div[contains(@class,"d_post_content_main")]//span[contains(@class,"tail-info")][last()]'
# 帖子回复楼层内容
Xpath_Floor_Content = '//div[contains(@class,"p_content")]//div[contains(@class,"d_post_content")]'

# 评论换页导航
Xpath_Floor_Nav = '//p[contains(@class,"j_pager")]'
# 当楼层的当前评论页的评论list
Xpath_Floor_Comments = '//li[contains(@class, "lzl_single_post")]'
# 评论作者
Xpath_Comment_Author = '//div[@class="lzl_cnt"]//a[contains(@class,"j_user_card")]'
# 评论内容
Xpath_Comment_Content = '//div[@class="lzl_cnt"]//span[contains(@class,"lzl_content_main")]'


# 初始化浏览器：调用本地Chrome，在新标签打开目标网页，并切换到该标签
def InitialChrome(WebSite):
    SaiBrowser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    SaiContext = SaiBrowser.contexts[0]
    SaiContext.route(
        re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.gif.*)|(.*\.webp.*)"), lambda route: route.abort()
    )
    SaiPage = SaiContext.new_page()
    SaiPage.goto(WebSite)
    SaiPage.bring_to_front()
    SaiPage.wait_for_load_state("networkidle")
    return SaiBrowser, SaiContext, SaiPage


# 初始化写入方法：切换到目标路径，指定文件名
def InitialMDFile():
    # 切换MarkDown文件目录
    MDdir = "/Users/jiangsai/Desktop"
    os.chdir(MDdir)
    # 声明全局MarkDown文件操作类
    global MarkDownMaker
    MarkDownMaker = html2text.HTML2Text()
    MarkDownMaker.ignore_links = True
    MDFile = "Test"
    # 声明全局MarkDown文件路径
    global MDFileDir
    MDFileDir = f"{MDdir}/{MDFile}.md"


# 页面滚动方法：对指定页面，滚动指定次数或滚动到底
def PageScroll(ScrollPage, ScrollTimes):
    ScrollTime = 1
    # 滚动到页面顶部
    ScrollPage.evaluate("() => window.scrollTo(0,0)")
    while ScrollTime < ScrollTimes:
        # 滚动计数
        ScrollTime += 1
        ScrollPage.evaluate("() => window.scrollBy(0,-window.innerHeight)")
        ScrollPage.wait_for_timeout(random.randint(500, 1000))


# 获取问题信息
def ExtractTileInfo(WritePage):
    Title = WritePage.query_selector(Xpath_Post_Title).text_content()
    with open("test.md", mode="a", encoding="utf-8") as f:
        f.write("### " + Title + "\n" + "----" + "\n")
        f.write("----" + "\n\n")


# 获取每一个楼层信息
def ExtractCurrentFloorInfo(CurrentFloor):
    if CurrentFloor.query_selector(Xpath_Floor_Author) != None:
        Floor_Author = CurrentFloor.query_selector(Xpath_Floor_Author).text_content()
        if Floor_Author == "贴吧用户_0DWb97a":
            pass
        Floor_Time = CurrentFloor.query_selector(Xpath_Floor_Time).text_content()
        Floor_Content_Html = CurrentFloor.query_selector(Xpath_Floor_Content).inner_html()
        Floor_Content = MarkDownMaker.handle(Floor_Content_Html)
        with open(MDFileDir, mode="a", encoding="utf-8") as f:
            f.write("作者：" + Floor_Author + "\n" + "时间：" + Floor_Time + "\n" + Floor_Content + "\n")
            f.write("----" + "\n\n")


# 页面翻页
def TurnPage(PageToTurn):
    global Page_All_Nav
    global Page_Clicked_Nav
    global Page_Able_Click_Nav
    # 取最小导航数为下一个要点击的
    Page_To_Click_Nav = Page_Able_Click_Nav[0]
    # 点击最小导航数
    # locator('text=1')模糊匹配1,01,10,11等;locator('text="1"')精确匹配1
    PageToTurn.locator(Xpath_Page_Nav).locator('text="' + str(Page_To_Click_Nav) + '"').click()
    PageToTurn.wait_for_timeout(random.randint(1000, 3000))
    # 刚点击的数字追加到「已点击导航数字集合」
    Page_Clicked_Nav.add(Page_To_Click_Nav)
    # 当前页导航列表
    Current_Nav_list = PageToTurn.query_selector_all(Xpath_Page_Nav + "/*")
    for i in Current_Nav_list:
        Nav_num = i.text_content()
        # 抽取出导航列表中的数字，「上一页」「下一页」这种非确定性导航都排除
        if str(Nav_num).isdigit():
            Page_All_Nav.add(int(Nav_num))
    # 可点击导航数字集合 = 所有导航数字集合 ∩ 已点击导航数字集合，再转换成列表
    Page_Able_Click_Nav = sorted(list(Page_All_Nav.difference(Page_Clicked_Nav)))


# 获取每一页的信息
def ExtractEachPageInfo(SaiContext, CurrentPage):
    # 所有导航数字集合
    global Page_All_Nav
    Page_All_Nav = set()
    # 已点击导航数字集合
    global Page_Clicked_Nav
    Page_Clicked_Nav = set()
    # 可点击导航数字集合，初始设置为1，即第一页
    global Page_Able_Click_Nav
    Page_Able_Click_Nav = [1]
    # 逐个页面获取信息
    while len(Page_Able_Click_Nav) > 0:
        TurnPage(CurrentPage)
        # 贴吧有些内容不划到位是不展示的
        PageScroll(CurrentPage, 10)
        # 获取当前页的所有楼层
        Floors = CurrentPage.query_selector_all(Xpath_Floors)
        # 遍历每个楼层
        for this_floor in Floors:
            # 获取当前楼层的信息
            ExtractCurrentFloorInfo(this_floor)
            # 若本楼层有评论，且评论被折叠，则展开
            if this_floor.query_selector('text="点击查看"') != None:
                this_floor.query_selector('text="点击查看"').click()
                CurrentPage.wait_for_timeout(random.randint(500, 1000))
            if this_floor.query_selector(Xpath_Floor_Comments) != None:
                ExtractFloorCommentsInfo(SaiContext, CurrentPage, this_floor)
            # CurrentPage.wait_for_timeout(random.randint(1000, 3000))


# 评论：获取当前楼层每一个评论页信息
def ExtractFloorCommentsInfo(SaiContext, CurrentCommentPage, this_page_floor):
    # 所有导航数字集合
    global All_Nav
    All_Nav = set()
    # 已点击导航数字集合
    global Clicked_Nav
    Clicked_Nav = set()
    # 可点击导航数字集合，初始设置为1，即第一页
    global Able_Click_Nav
    # 判断当前楼层的评论是否为多页，多页才会出现1、2、3导航，只有1页没有导航
    if (
        this_page_floor.query_selector(Xpath_Floor_Nav) != None
        and this_page_floor.query_selector(Xpath_Floor_Nav).inner_html() != "&nbsp;"
    ):
        Able_Click_Nav = [1]
        # 逐个评论页面获取信息
        while len(Able_Click_Nav) > 0:
            TurnCommentsPage(CurrentCommentPage, this_page_floor)
            # 获取当楼层的当前评论页的评论list
            Comment_Floors = this_page_floor.query_selector_all(Xpath_Floor_Comments)
            # 遍历每个评论楼层
            for this_comment_floor in Comment_Floors:
                # 获取当前评论楼层的信息
                ExtractCurrentComentFloorInfo(this_page_floor, this_comment_floor)
                # CurrentPage.wait_for_timeout(random.randint(1000, 3000))
    else:
        # 获取当楼层的当前评论页的评论list
        Comment_Floors = this_page_floor.query_selector_all(Xpath_Floor_Comments)
        # 遍历每个评论楼层
        for this_comment_floor in Comment_Floors:
            # 获取当前评论楼层的信息
            ExtractCurrentComentFloorInfo(this_page_floor, this_comment_floor)


# 评论：获取每一个评论楼层信息
def ExtractCurrentComentFloorInfo(this_page_floor, this_comment_floor):
    if this_comment_floor.query_selector(Xpath_Comment_Author) != None:
        Comment_Author = this_comment_floor.query_selector(Xpath_Comment_Author).text_content()
        Comment_Content = this_comment_floor.query_selector(Xpath_Comment_Content).text_content()
        with open(MDFileDir, mode="a", encoding="utf-8") as f:
            f.write("> " + Comment_Author + ": " + Comment_Content + "\n")


# 评论：翻页
def TurnCommentsPage(CurrentPage, this_page_floor):
    global All_Nav
    global Clicked_Nav
    global Able_Click_Nav
    # 取最小导航数为下一个要点击的
    To_Click_Nav = Able_Click_Nav[0]
    # 点击最小导航数
    # locator('text=1')模糊匹配1,01,10,11等;locator('text="1"')精确匹配1
    this_page_floor.query_selector(Xpath_Floor_Nav).query_selector('text="' + str(To_Click_Nav) + '"').click()
    CurrentPage.wait_for_timeout(random.randint(500, 1500))
    # 刚点击的数字追加到「已点击导航数字集合」
    Clicked_Nav.add(To_Click_Nav)
    # 当前页导航列表
    Current_Nav_list = this_page_floor.query_selector_all(Xpath_Floor_Nav + "/*")
    for i in Current_Nav_list:
        Nav_num = i.text_content()
        # 抽取出导航列表中的数字，「上一页」「下一页」这种非确定性导航都排除
        if str(Nav_num).isdigit():
            All_Nav.add(int(Nav_num))
    # 可点击导航数字集合 = 所有导航数字集合 ∩ 已点击导航数字集合，再转换成列表
    Able_Click_Nav = sorted(list(All_Nav.difference(Clicked_Nav)))


def run(playwright: Playwright) -> None:
    WebSite = "https://tieba.baidu.com/p/8670538425"
    # WebSite = input("请输入要爬的网址: ")
    SaiBrowser, SaiContext, SaiPage = InitialChrome(WebSite)
    InitialMDFile()
    # 获取帖子标题
    ExtractTileInfo(SaiPage)
    # 获取楼层信息
    ExtractEachPageInfo(SaiContext, SaiPage)

    # 收尾
    SaiPage.close()
    SaiContext.close()
    SaiBrowser.close()


with sync_playwright() as playwright:
    run(playwright)
```

#### 人人都是产品经理、36氪

> 网页结构简单，只需要抓标题和内容即可

```python
import os, html2text, re, random
from playwright.sync_api import Playwright, sync_playwright

#########################全局变量#########################
# 待爬网址
WebSites = [
    # "https://www.woshipm.com/zhichang/5824950.html",
    "https://36kr.com/p/2399884943188356",
]
############## woshipm ##############
# 标题
Xpath_woshipm_Title = '//*[contains(@class,"article--title")]'
# 内容
Xpath_woshipm_Content = '//*[contains(@class,"article--content")]'

############## 36kr ##############
# 标题
Xpath_36kr_Title = '//h1[contains(@class,"article-title")]'
# 概要
Xpath_36kr_Summary = '//div[contains(@class,"summary")]'
# 内容
Xpath_36kr_Content = '//div[contains(@class,"articleDetailContent")]'
#########################全局变量#########################


# 初始化浏览器：调用本地Chrome，在新标签打开目标网页，并切换到该标签
def InitialChrome(WebSites):
    SaiBrowser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    SaiContext = SaiBrowser.contexts[0]
    SaiContext.route(
        re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.gif.*)|(.*\.webp.*)"), lambda route: route.abort()
    )
    SaiPages = []
    for i in WebSites:
        SaiPage = SaiContext.new_page()
        SaiPage.goto(i)
        SaiPages.append(SaiPage)
        SaiPage.wait_for_timeout(random.randint(1000, 3000))
    return SaiBrowser, SaiContext, SaiPages


# 初始化写入方法：切换到目标路径，指定文件名
def InitialMDFile(MDdir, MDFile):
    # 切换MarkDown文件目录
    os.chdir(MDdir)
    # 声明全局MarkDown文件操作类
    global MarkDownMaker
    MarkDownMaker = html2text.HTML2Text()
    MarkDownMaker.ignore_links = True
    # 声明全局MarkDown文件路径
    global MDFileDir
    MDFileDir = f"{MDdir}/{MDFile}"


# 获取woshipm信息
def GetInfo_woshipm(WritePage):
    title = WritePage.query_selector(Xpath_woshipm_Title).text_content()
    content_node = WritePage.query_selector('//*[contains(@class,"article--content")]')
    # 要从正文中移除的节点
    content_node_remove = content_node.query_selector("//div[contains(@class,'copyright')]")
    content_node_remove.evaluate("element => element.remove()")
    content_node_remove = content_node.query_selector("//div[contains(@class,'bottomActions')]")
    content_node_remove.evaluate("element => element.remove()")
    # 因正文可能包含图片，故此处使用HTML2Text提取富文本
    content_Html = content_node.inner_html()
    content = MarkDownMaker.handle(content_Html)
    with open(MDFileDir, mode="a", encoding="utf-8") as f:
        f.write("### " + title + "\n" + content + "\n" + "---" + "\n\n")


# 获取36kr信息
def GetInfo_36kr(WritePage):
    Title = WritePage.query_selector(Xpath_36kr_Title).text_content()
    Summary = WritePage.query_selector(Xpath_36kr_Summary).text_content()
    # 因答案内容可能包含图片，故此处使用HTML2Text提取富文本
    Content_Html = WritePage.query_selector(Xpath_36kr_Content).inner_html()
    Content = MarkDownMaker.handle(Content_Html)
    with open(MDFileDir, mode="a", encoding="utf-8") as f:
        f.write("### " + Title + "\n" + "> " + Summary + "\n\n" + Content + "\n\n" + "----" + "\n")


def run(playwright: Playwright) -> None:
    SaiBrowser, SaiContext, SaiPages = InitialChrome(WebSites)
    # MarkDown文件目录
    MDdir = "/Users/jiangsai/Desktop"
    # MarkDown文件名
    MDFile = "Test.md"
    # 初始化MarkDown操作方法
    InitialMDFile(MDdir, MDFile)
    # 逐个抓取每个网页
    for saipage in SaiPages:
        if "36kr" in saipage.url:
            GetInfo_36kr(saipage)
            saipage.close()
        elif "woshipm" in saipage.url:
            GetInfo_woshipm(saipage)
            saipage.close()
    # 收尾
    SaiContext.close()
    SaiBrowser.close()


with sync_playwright() as playwright:
    run(playwright)
```

#### 微博

```python
import os, html2text, re, random, requests
from playwright.sync_api import Playwright, sync_playwright

#########################全局变量#########################
# 待爬网址
WebSite = "https://weibo.com/u/2959386434"
# list
Xpath_list = '//div[@class="vue-recycle-scroller__item-wrapper"]/*'
# name
Xpath_name = '//a[@class="ALink_default_2ibt1 head_cut_2Zcft head_name_24eEB"]'
# content
Xpath_content = '//div[@class="Feed_body_3R0rO"]/div[contains(@class,"wbpro-feed-content")]'
# image
Xpath_content_image = '//div[contains(@class,"woo-picture-slot")]'
# reply
Xpath_reply = '//div[@class="Feed_body_3R0rO"]/div[contains(@class,"Feed_retweet_JqZJb")]'
#########################全局变量#########################


# 初始化浏览器：调用本地Chrome，在新标签打开目标网页，并切换到该标签
def InitialChrome():
    SaiBrowser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    SaiContext = SaiBrowser.contexts[0]
    # SaiContext.route(
    #     re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.gif.*)|(.*\.webp.*)"), lambda route: route.abort()
    # )
    SaiPage = SaiContext.new_page()
    SaiPage.goto(WebSite)
    SaiPage.wait_for_load_state("networkidle")
    # SaiPage.wait_for_timeout(random.randint(1000, 3000))
    return SaiBrowser, SaiContext, SaiPage


# 初始化写入方法：切换到目标路径，指定文件名
def InitialMDFile(MD_dir, MDFile):
    # 切换MarkDown文件目录
    if not os.path.exists(MD_Pic_dir):
        os.mkdir(MD_Pic_dir)
    # 声明全局MarkDown文件操作类
    global MarkDownMaker
    MarkDownMaker = html2text.HTML2Text()
    MarkDownMaker.ignore_links = True
    # 声明全局MarkDown文件路径
    global MDFileDir
    MDFileDir = f"{MD_dir}/{MDFile}"


# 获取微博信息
# 微博的DOM节点一直在更新，新内容会覆盖旧内容的节点，无法像知乎一样滚动加载完成后抓取
# 每滚动3屏抓一次，边滚边抓，记录每个内容块的纵坐标，汇总成已抓取的内容块的纵坐标list
# 利用纵坐标进行内容排序，并排除重复
def GetInfo_WeiBo(SaiPage, TimesToGet):
    # 已抓取的内容块的纵坐标list
    AllSequenceNo = []
    for i in range(TimesToGet):
        # 翻页：每滚动3屏记为1页，每页取1次值
        for i in range(3):
            # 滚动1屏
            SaiPage.evaluate("() => window.scrollBy(0,window.innerHeight)")
            SaiPage.wait_for_timeout(random.randint(1000, 1500))
        # 获取内容块：获取当前页所有内容块
        Blocks = SaiPage.query_selector_all(Xpath_list)
        # 获取内容块数据：获取当前页所有内容块中每一个块的具体信息
        CurrentPageData = GetInfo_PerPage(SaiPage, Blocks, AllSequenceNo)
        # 按照内容块的纵坐标对本页内容块排序
        sorted_PageData = sorted(CurrentPageData, key=lambda x: x["SequenceNo"])
        for ElementData in sorted_PageData:
            with open(MDFileDir, mode="a", encoding="utf-8") as f:
                f.write("##### " + ElementData["name"] + "\n")
                f.write(ElementData["content"] + "\n")
                if ElementData["reply"] != "":
                    f.write("> " + ElementData["reply"] + "\n")
                f.write("----" + "\n")


# 获取当前页所有内容块中每一个块的具体信息
def GetInfo_PerPage(SaiPage, Blocks, AllSequenceNo):
    # 当前页每一个块的具体信息list
    CurrentPageData = []
    for Block in Blocks:
        # 获取当前节点的style属性值，该值即是当前节点的纵坐标
        # 格式：<div class="vue-***-view" style="transform: translateY(227px);">
        style = Block.evaluate("el => el.getAttribute('style')")
        style_value = re.findall(r"\((.*?)\)", style)[0].replace("px", "")
        # <0的纵坐标是个占位符，忽略
        if int(style_value) >= 0:
            # 已经获取过的纵坐标不用重新获取，忽略
            if style_value not in AllSequenceNo:
                # 当前纵坐标加入纵坐标list
                AllSequenceNo.append(style_value)
                # 滚动到当前元素位置
                # element.evaluate("element => element.scrollIntoView()")
                # 若内容有折叠，则展开
                if Block.query_selector('text="展开"') != None:
                    Block.query_selector('text="展开"').click()
                    SaiPage.wait_for_timeout(random.randint(1000, 1500))
                # 提取当前内容块的数据
                CurrentElementData = GetInfo_PerBlock(SaiPage, Block, style_value)
                # 将当前内容块数据加入本页数据
                CurrentPageData.append(CurrentElementData)
    return CurrentPageData


# 提取当前内容块的数据
def GetInfo_PerBlock(SaiPage, element, style_value):
    # 当前内容块的数据字典
    CurrentElementData = {}
    # 内容块纵坐标（整数）
    CurrentElementData["SequenceNo"] = int(style_value)
    # 内容块作者（字符串）
    name = element.query_selector(Xpath_name).text_content()
    CurrentElementData["name"] = name

    # 内容块的具体内容（因内容可能包含图片，故用HTML2Text提取MarkDown富文本）
    content_Html = element.query_selector(Xpath_content).inner_html()
    # 提取的原始内容的图片都是在线的
    content_Online_Pic = MarkDownMaker.handle(content_Html)
    # 但微博禁止站外部引用他的图片，故先将在线图片下载到本地再引用
    content_Local_Pic = DownLoad_Pic_Get_New_MDContent(SaiPage, content_Online_Pic)
    CurrentElementData["content"] = content_Local_Pic

    # 内容块的回复部分
    CurrentElementData["reply"] = ""
    # 若本内容没有回复则忽略
    if element.query_selector(Xpath_reply) != None:
        # 提取逻辑同上述内容块
        reply_Html = element.query_selector(Xpath_reply).inner_html()
        reply_Online_Pic = MarkDownMaker.handle(reply_Html)
        reply_Local_Pic = DownLoad_Pic_Get_New_MDContent(SaiPage, reply_Online_Pic)
        # 剔除多余换行
        reply_clean = reply_Local_Pic.replace("\n", "")
        CurrentElementData["reply"] = reply_clean
    return CurrentElementData


# 下载图片并替换图片引用路径
def DownLoad_Pic_Get_New_MDContent(SaiPage, MDContent):
    # 提取出MarkDown文本中所有 ![](url) 中 url
    MDPicUrls = re.findall(r"!\[\]\((.*?)\)", MDContent)
    if len(MDPicUrls) != 0:
        for image_url in MDPicUrls:
            # 提取图片名称
            # 格式：https://fe.t.sis.cn/ap.png/ddkkk 提取出ap.png
            match = re.search(r"/([^/]+\.(?:png|jpg|jpeg|webp))(?:/|$)", image_url)
            if match:
                PicName = match.group(1)
                # 拼接已下载的本地图片的完整路径
                ThisPicDir = f"{MD_Pic_dir}/{PicName}"
                # 利用requests下载图片
                Requests_DownLoad_Pic(SaiPage, image_url, ThisPicDir)
                # 将MarkDown文本中的在线图片链接替换为本地图片连接
                MDContent = MDContent.replace(image_url, ThisPicDir)
            else:
                print(f"图片格式需要扩充: {image_url}")
    return MDContent


# 利用requests下载图片
def Requests_DownLoad_Pic(SaiPage, image_url, ThisPicDir):
    # 创建一个Session会话
    session = requests.Session()
    # 获取页面的Cookies
    cookies = SaiPage.context.cookies()
    # 将Cookies添加到Session会话中
    for cookie in cookies:
        session.cookies.set(cookie["name"], cookie["value"], domain=cookie["domain"])
    # 直接抓的是小图，需要下载大图
    # 小图链接：https://wx3.sinaimg.cn/orj360/b06442n.jpg
    # 大图链接：https://wx3.sinaimg.cn/mw690/b06442n.jpg
    image_url = image_url.replace("orj360", "mw690")
    # 使用Session会话来下载图像
    response = session.get(image_url)
    # 检查响应状态码
    if response.status_code == 200:
        # 将图像保存到文件
        with open(ThisPicDir, "wb") as fp:
            fp.write(response.content)
    else:
        print("下载失败")


def run(playwright: Playwright) -> None:
    # 初始化浏览器
    SaiBrowser, SaiContext, SaiPage = InitialChrome()
    # MarkDown文件目录
    MD_dir = "/Users/jiangsai/Desktop"
    # MarkDown文件名
    MDFile = "Test.md"
    # MarkDown引用的图片目录
    global MD_Pic_dir
    MD_Pic_dir = "/Users/jiangsai/Desktop/Pic"
    # 初始化MarkDown操作方法
    InitialMDFile(MD_dir, MDFile)
    # 获取目标信息
    GetInfo_WeiBo(SaiPage, 10)
    # 收尾
    SaiContext.close()
    SaiBrowser.close()


with sync_playwright() as playwright:
    run(playwright)
```

