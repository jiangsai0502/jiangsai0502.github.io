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

  > * 查看此时要用的pip在哪个环境
  >
  >   > 详见[Python 周边环境](Sai_FootPrint/1_PythonEnvironment.md)
  >   >
  >   > `pip3 -V`
  >   >
  >   > `conda install pip3`
  >
  > * `pip3 install pytest-playwright`

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
  >   >   >    | COMMAND | PID   | USER     | FD   | TYPE | DEVICE            | SIZE/OFF | NODE | NAME                             |
  >   >   >    | ------- | ----- | -------- | ---- | ---- | ----------------- | -------- | ---- | -------------------------------- |
  >   >   >    | Google  | 93266 | jiangsai | 97u  | IPv4 | 0xf8edc13e875fe59 | 0t0      | TCP  | localhost:teamcoherence (LISTEN) |
  >   >   >
  >   >   >    > 即9222端口被「Google进程」占用，PID为「93266」
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
  >   >   ```
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
  >   >   > `SaiContext.route()`和`SaiPage.route()`的区别：前者应用于`SaiContext`下的所有页面，后者只应用于`SaiPage`这一个页面
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
  >   >   > 所有`//`开头的表达式都会默认为 XPath
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
  >   >      >`Shift`, `Control`,` Alt`, `Meta(Meta = Win/Cmd 键)`
  >   >      >[其他的按键参考这里](https://playwright.dev/python/docs/api/class-keyboard)
  >   >
  >   >      全选`Command+A`：`SaiPage.keyboard.press("Meta+A") `
  >   >
  >   > *  鼠标点击
  >   >
  >   >   `SaiPage.locator('//button[@class="SearchBar"]').click()`
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
  >   >       SaiPage.wait_for_timeout(3000)
  >   >       # 滚动后的页面高度
  >   >       AfterScrollHeight = SaiPage.evaluate("() => document.body.scrollHeight")
  >   >       if BeforeScrollHeight == AfterScrollHeight:
  >   >           # 知乎加载到一定程度，加载速度会变慢，但实际还没加载完
  >   >           SaiPage.wait_for_timeout(5000)
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
  >   >     # 每个元素的文本值 text_content
  >   >     print(element.text_content())
  >   >     # 每个元素的链接
  >   >     print(element.query_selector('//a[@class="Link"]').get_attribute('href'))
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
  >   > * 将页面部分内容转化为`markdown`后下载到本地
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
  >   > 打开二级页
  >   >
  >   > * 方法一：从一级页获取二级页的链接后再打开
  >   >
  >   >   ```python
  >   >   SonPage = SaiContext.new_page()
  >   >   SonPageUrl = SaiPage.query_selector('//div[@class="fl"]').get_attribute('href')
  >   >   SonPage.gotoSonPageUrl(SonPageUrl)
  >   >   SonPage.wait_for_load_state("networkidle")
  >   >   SonPage.bring_to_front()
  >   >   ```
  >   >
  >   > * 方法二：从一级页点击二级页链接打开
  >   >
  >   >   ```python
  >   >   with SaiContext.expect_page() as SonPageInfo:
  >   >       SaiPage.locator('//div[@class="fl"]').click()
  >   >   SonPage = SonPageInfo.value
  >   >   SonPage.wait_for_load_state()
  >   >   SonPage.bring_to_front()
  >   >   ```
  >   >
  >   > 翻页
  >   >
  >   > * 翻页方法1：底部导航条最后一个按钮不是【下一页】，[范例CPC](http://cpc.people.com.cn/GB/64093/64387/index16.html)
  >   >
  >   >   ```python
  >   >   HaveNextPage = True
  >   >   while HaveNextPage:
  >   >       if SaiPage.locator('//div[@class="page"]/a[last()]').text_content() == '下一页':
  >   >           PageURL = SaiPage.url
  >   >           print('页面网址：', PageURL)
  >   >           SaiPage.locator('//div[@class="page"]/a[last()]').click()
  >   >       else:
  >   >           HaveNextPage = False
  >   >           print("没有下一页了...，爬取结束")
  >   >   ```
  >   >
  >   > * 翻页方法2：底部导航条最后一个按钮是【下一页】，但不可见，[范例BiBi](https://space.bilibili.com/107861587/video?pn=13)
  >   >
  >   >   ```python
  >   >   HaveNextPage = True
  >   >   while HaveNextPage:
  >   >       if SaiPage.is_visible('//li[@title="下一页"]/a'):
  >   >           SaiPage.click('//li[@title="下一页"]/a')
  >   >           timeout = random.randint(1500, 2500)
  >   >           SaiPage.wait_for_timeout(timeout)
  >   >           SaiPage.mouse.wheel(0,20000)
  >   >           PageURL = SaiPage.url
  >   >           print('页面网址：', PageURL)
  >   >       else:
  >   >           HaveNextPage = False
  >   >           print("没有下一页了...，爬取结束")
  >   >   ```
  >   >
  >   > * 翻页方法3：底部导航条最后一个按钮是【下一页】，可见，可不点击，范例[DB](https://movie.douban.com/top250?start=200)
  >   >
  >   >   ```python
  >   >   # 判断页面中是否存在某个元素：Page.locator(xpath).count() != 0
  >   >   HaveNextPage = True
  >   >   while HaveNextPage:
  >   >       if SaiPage.locator('//span[@class="next"]/link').count() != 0:
  >   >           PageURL = SaiPage.url
  >   >           print('页面网址：', PageURL)
  >   >           SaiPage.click('//span[@class="next"]')
  >   >       else:
  >   >           HaveNextPage = False
  >   >           print("没有下一页了...，爬取结束")
  >   >     
  >   >   # 判断页面中是否存在某个元素：Page.query_selector('//span[@class="next"]/link') is not None
  >   >   HaveNextPage = True
  >   >   while HaveNextPage:
  >   >       if Page.query_selector('//span[@class="next"]/link') is not None:
  >   >           PageURL = SaiPage.url
  >   >           print('页面网址：', PageURL)
  >   >           SaiPage.click('//span[@class="next"]')
  >   >       else:
  >   >           HaveNextPage = False
  >   >           print("没有下一页了...，爬取结束")
  >   >   ```
  >   >
  >   > 存储Cookie
  >   >
  >   > > 将`cookie`保存到`state.json`，方便方式二Playwright无头浏览器进行免登录
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
   > def run(playwright: Playwright) -> None:
   >     SaiBrowser = playwright.chromium.connect_over_cdp('http://localhost:9222')
   >     SaiContext = SaiBrowser.contexts[0]
   >     SaiPage = SaiContext.new_page()
   >     SaiPage.route(re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.webp.*)"), lambda route: route.abort())
   > 
   >     SaiPage.goto('https://chat.openai.com/')
   >     
   >     SaiPage.wait_for_timeout(5000)
   >     question_list=['python','sql','oracle','mysql']
   >     for qst in question_list:
   >         SaiPage.get_by_role("textbox").fill(qst)
   >         SaiPage.get_by_role("textbox").press("Enter")
   >         SaiPage.wait_for_timeout(1000)
   >         text1 = "1"
   >         text2 = "2"
   >         while(text1 != text2):
   >             t1_list = SaiPage.query_selector_all('//div[@class="flex flex-col text-sm dark:bg-gray-800"]/div')
   >             if(len(t1_list)>0):
   >                 text1 = t1_list[-2].inner_text()
   >             SaiPage.wait_for_timeout(3000)
   >             t2_list = SaiPage.query_selector_all('//div[@class="flex flex-col text-sm dark:bg-gray-800"]/div')
   >             if(len(t2_list)>0):
   >                 text2 = t2_list[-2].inner_text()
   >             print(text1)
   >     
   >     SaiPage.wait_for_timeout(200000)
   >     SaiContext.close()
   >     SaiBrowser.close()
   > # ---------------------收尾工作---------------------
   > 
   > with sync_playwright() as playwright:
   >     run(playwright)
   > ```
   > 

##### 爬虫实操

* 爬取接口json数据

  [参考](https://3yya.com/lesson/61)，[]()

  > 打开开发者工具 -> 切到`Network`  -> 刷新页面 -> 点击`XHR`过滤请求 -> 逐个查看每个请求的`Response`
  >
  > 案例1：[B站个人空间](https://space.bilibili.com/107861587/video)
  >
  > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310071930814.png)
  >
  > > 通过观察和测试发现
  > >
  > > 1. 接口API：https://api.bilibili.com/x/space/wbi/arc/search?mid=107861587&ps=30&tid=0&pn=1&keyword=&order=pubdate&platform=web&web_location=1550101&order_avoided=true&w_rid=ae73d64fedd5ef027f2a7309c3fa27c5&wts=1696676696
  > > 2. 接口API通过pn=1、2的方式进行翻页请求
  > > 3. 所有`XHR`中请求中，接口API的特征为以`https://api.bilibili.com/x/space/wbi/arc/search?`开头
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
  >
  
* 爬取知乎答案

  > ```python
  > import os, html2text
  > from playwright.sync_api import Playwright, sync_playwright
  > 
  > def run(playwright: Playwright) -> None:
  >     SaiBrowser = playwright.chromium.connect_over_cdp('http://localhost:9222')
  >     SaiContext = SaiBrowser.contexts[0]
  >     SaiPage = SaiContext.new_page()
  >     SaiPage.goto('https://www.zhihu.com/question/47034512')
  >     SaiPage.wait_for_load_state("networkidle")
  >     SaiPage.bring_to_front()
  > 
  >     # 滚动加载更多内容，直到不再加载
  >     NotEnd = True
  >     while NotEnd:
  >         # 滚动前的页面高度
  >         BeforeScrollHeight = SaiPage.evaluate("() => document.body.scrollHeight")
  >         # 滚动到页面底部
  >         SaiPage.evaluate("() => window.scrollTo(0,document.body.scrollHeight)")
  >         # 等待网络加载，单位是毫秒
  >         SaiPage.wait_for_timeout(3000)
  >         # 微上划一下模拟人类
  >         SaiPage.mouse.wheel(0, -10000)
  >         # 滚动后的页面高度
  >         AfterScrollHeight = SaiPage.evaluate("() => document.body.scrollHeight")
  >         if BeforeScrollHeight == AfterScrollHeight:
  >             # 知乎加载到一定程度，加载速度会变慢，但实际还没加载完
  >             SaiPage.mouse.wheel(0, -10000)
  >             SaiPage.evaluate("() => window.scrollTo(0,document.body.scrollHeight)")
  >             SaiPage.wait_for_timeout(1000)
  >             AfterScrollHeight = SaiPage.evaluate("() => document.body.scrollHeight")
  >             # 两次等待，两次加载后依然页面高度不变，则判断为加载完了
  >             if BeforeScrollHeight == AfterScrollHeight:
  >                 NotEnd = False
  > 
  >     # 切换目录
  >     os.chdir('/Users/jiangsai/Desktop')
  >     MarkDownMaker = html2text.HTML2Text()
  >     MarkDownMaker.ignore_links = True
  >     # 获取问题
  >     Answer_Title = SaiPage.query_selector('//h1[@class="QuestionHeader-title"]').text_content()
  >     Answer_Content = SaiPage.query_selector('//div[@class="css-eew49z"]').text_content()
  >     with open('test.md', mode='a', encoding='utf-8') as f:
  >         f.write('### ' + Answer_Title + '\n')
  >         f.write('> ' + Answer_Content + '\n\n')
  >         f.write('----' + '\n')
  > 
  >     # 获取答案
  >     Elements = SaiPage.query_selector_all('//div[@class="List-item"]')
  >     for element in Elements:
  >         Author = element.query_selector('//div[@class="AuthorInfo-head"]').text_content()
  >         QuestionHtml = element.query_selector('//span[@class="RichText ztext CopyrightRichText-richText css-117anjg"]').inner_html()
  >         Question = MarkDownMaker.handle(QuestionHtml)
  >         with open('test.md', mode='a', encoding='utf-8') as f:
  >             f.write('##### ' +Author + '\n')
  >             f.write(Question)
  >             f.write('----' + '\n')
  > 
  >     # 收尾
  >     SaiContext.close()
  >     SaiBrowser.close()
  > 
  > with sync_playwright() as playwright:
  >     run(playwright)
  > ```
  >
  
* 爬取知乎搜索结果

  > ```python
  > import os, html2text
  > import re
  > from playwright.sync_api import Playwright, sync_playwright
  > 
  > def SaiScroll(ScrollPage, ScrollTimes):
  >     # 滚动加载更多内容，直到不再加载或者滚动了n次
  >     NotEnd = True
  >     ScrollTime = 1
  >     while NotEnd and ScrollTime < ScrollTimes:
  >         # 滚动前的页面高度
  >         BeforeScrollHeight = ScrollPage.evaluate("() => document.body.scrollHeight")
  >         # 滚动到页面底部
  >         ScrollPage.evaluate("() => window.scrollTo(0,document.body.scrollHeight)")
  >         ScrollTime += 1
  >         # 等待网络加载，单位是毫秒
  >         ScrollPage.wait_for_timeout(3000)
  >         # 微上划几下模拟人类
  >         for i in range(3):
  >             ScrollPage.keyboard.press('PageUp')
  >             ScrollPage.wait_for_timeout(200)
  >         # 滚动到页面底部
  >         ScrollPage.evaluate("() => window.scrollTo(0,document.body.scrollHeight)")
  >         # 滚动后的页面高度
  >         AfterScrollHeight = ScrollPage.evaluate("() => document.body.scrollHeight")
  >         if BeforeScrollHeight == AfterScrollHeight or ScrollTime >= ScrollTimes:
  >             NotEnd = False
  > 
  > def WriteMD(WritePage):
  >     # 创建MD文件
  >     os.chdir('/Users/jiangsai/Desktop')
  >     MarkDownMaker = html2text.HTML2Text()
  >     MarkDownMaker.ignore_links = True
  >     # 问题
  >     Answer_Title = WritePage.query_selector('//h1[@class="QuestionHeader-title"]').text_content()
  >     Answer_Content = ''
  >     # 判断问题描述是否存在，有些问题没有描述
  >     if WritePage.query_selector('//div[@class="css-eew49z"]') is not None:
  >         # 判断问题描述是否被收起
  >         if WritePage.locator('//div[@class="css-eew49z"]//button').count() != 0:
  >             WritePage.locator('//div[@class="css-eew49z"]//button').click()
  >         Answer_Content_Html = WritePage.query_selector('//div[@class="css-eew49z"]').inner_html()
  >         Answer_Content = MarkDownMaker.handle(Answer_Content_Html)
  >     with open('test.md', mode='a', encoding='utf-8') as f:
  >         f.write('### ' + Answer_Title + '\n')
  >         f.write('> ' + Answer_Content + '\n\n')
  >         f.write('----' + '\n')
  > 
  >     # 答案
  >     # 判断答案是否存在，有些问题没有答案
  >     if WritePage.query_selector_all('//div[@role="list"]/div') is not None:
  >         Elements = WritePage.query_selector_all('//div[@role="list"]/*[not(@role="listitem")]')
  >         for element in Elements:
  >             Author = element.query_selector('//div[@class="AuthorInfo-head"]').text_content()
  >             QuestionHtml = element.query_selector('//span[@class="RichText ztext CopyrightRichText-richText css-117anjg"]').inner_html()
  >             Question = MarkDownMaker.handle(QuestionHtml)
  >             with open('test.md', mode='a', encoding='utf-8') as f:
  >                 f.write('##### ' +Author + '\n')
  >                 f.write(Question)
  >                 f.write('----' + '\n')
  > 
  > def run(playwright: Playwright) -> None:
  >     SaiBrowser = playwright.chromium.connect_over_cdp('http://localhost:9222')
  >     SaiContext = SaiBrowser.contexts[0]
  >     SaiContext.route(re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.webp.*)"), lambda route: route.abort())
  >     SaiPage = SaiContext.new_page()
  >     SaiPage.goto('https://www.zhihu.com/search?q=%E6%91%A9%E6%89%98%E8%BD%A6%E4%BF%AE%E7%90%86%E4%B8%8E%E7%A6%85')
  >     SaiPage.wait_for_load_state("networkidle")
  >     SaiPage.bring_to_front()
  > 
  >     # 滚动搜索页获取更多数据
  >     SaiScroll(SaiPage, 3)
  > 
  >     # 获取搜索结果链接
  >     elementUrls = []
  >     Elements = SaiPage.query_selector_all('//div[@class="List"]/div/*[not(@class="Card SearchResult-Card")]')
  >     for element in Elements:
  >         # 判断节点是否有URL，有就提取出链接
  >         if element.query_selector('//meta[@itemprop="url"]') is not None:
  >             elementUrl = element.query_selector('//meta[@itemprop="url"]').get_attribute('content')
  >             elementUrls.append(elementUrl)
  > 
  >     # 打开搜索结果链接
  >     for elementUrl in elementUrls:
  >         SonPage = SaiContext.new_page()
  >         SonPage.goto(elementUrl)
  >         SonPage.wait_for_load_state("networkidle")
  >         SonPage.bring_to_front()
  >         # 判断问题是否存在，有些链接是专题链接而不是问题链接，则不爬
  >         if SonPage.query_selector('//h1[@class="QuestionHeader-title"]') is None:
  >             SonPage.close()
  >         else:
  >             # 滚动二级页获取更多数据
  >             SaiScroll(SonPage, 5)
  >             WriteMD(SonPage)
  >             SonPage.close()
  >         
  >     # 收尾
  >     SaiContext.close()
  >     SaiBrowser.close()
  > 
  > with sync_playwright() as playwright:
  >     run(playwright)
  > ```
  >
  > 