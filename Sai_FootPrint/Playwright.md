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

##### 实操

* 录制脚本

  > `playwright codegen`
  >
  > [教程](https://www.bilibili.com/video/BV1H24y1G745)

* 使用本地Chrome

  > * 查看9222端口是否被占用
  >
  >   > `lsof -i:9222`
  >   >
  >   > 若结果如下表示已被占用
  >   >
  >   > ```python
  >   > (base)  Sai  ~  lsof -i:9222
  >   > COMMAND   PID     USER     FD  TYPE       DEVICE         SIZE/OFF NODE NAME
  >   > Google   93266  jiangsai  97u  IPv4   0xf8edc13e875fe59    0t0         TCP
  >   > ```
  >   >
  >   > > 即9222端口被「Google进程」占用，PID为「93266」，杀死进程可释放端口
  >   > >
  >   > > `sudo kill -9 PID`
  >
  > * 关闭当前所有Chrome浏览器
  >
  > * debug模式启动Chrome浏览器
  >
  >   > `/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222`
  >
  > * 代码调用debug Chrome
  >
  >   > ```python
  >   > 见"启动本地Chrome（模拟完全真实场景）"
  >   > ```

* 常用功能

  ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310061535560.png)

  ```python
  import re, os
  from numbers import Integral
  from playwright.sync_api import Playwright, sync_playwright, expect
  from bs4 import BeautifulSoup
  
  def run(playwright: Playwright) -> None:
  # ---------------------Chrome本地浏览器---------------------
      # 启动本地Chrome（模拟完全真实场景）
      SaiBrowser = playwright.chromium.connect_over_cdp('http://localhost:9222')
      SaiContext = SaiBrowser.contexts[0]
      SaiPage = SaiContext.new_page()
      # 拦截所有的图片请求以减少带宽占用
      # 但凡链接包含.png，无论是否是否以之结尾，都当做是png图片
      SaiContext.route(re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.webp.*)"), lambda route: route.abort())
  # ---------------------Chrome本地浏览器---------------------
  
  # ---------------------Playwright无头浏览器---------------------
      # # 初始化一个无头浏览器
      # SaiBrowser = playwright.chromium.launch(headless=False)
      # # 加载本地cookie
      #     # 若本地有cookie，则在SaiBrowser中创建一个context（网页管理器），并加载该cookie，实现免登陆
      # os.chdir('/Users/jiangsai/Desktop')
      # if os.path.exists('state.json'):
      #     SaiContext = SaiBrowser.new_context(storage_state="state.json")
      #     # 若本地没有，则在SaiBrowser中创建一个空的context
      #     # 每个context是一个独立会话，用于环境隔离，每个context可使用1套代理，登录1套账号
      # else:
      #     SaiContext = SaiBrowser.new_context()
      # 拦截所有的图片请求以减少带宽占用
      # SaiContext.route(re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.webp.*)"), lambda route: route.abort())
      # # 初始化一个网页：在SaiContext中创建一个网页
      # SaiPage = SaiContext.new_page()
  # ---------------------Playwright无头浏览器---------------------
  
  # ---------------------页面交互---------------------
      # 打开一个网址
          # 在SaiPage中打开指定网址
      SaiPage.goto("https://www.zhihu.com/question/22543815")
  
      # 页面刷新
      # SaiPage.reload()
  
      # 页面后退
      # SaiPage.go_back()
  
      # 页面前进
      # SaiPage.go_forward()
  
      # 鼠标悬停
      # SaiPage.locator('//div[@class="QuestionHeader-topics"]/div[1]').hover()
      
      # 键盘输入
          # 模拟字符串输入
          # 光标定位可用XPath，所有 // 或者 .. 开头的表达式都会默认为 XPath
      # SaiPage.locator('//*[@id="Popover2-toggle"]').type('technical')
  
          # 模拟按键输入
          # F(1-12), 数字(0-9), Key(a-z、A-Z)大小写敏感, Backspace(向左删除), Delete(向右删除), Tab, Escape, End, Enter, Home, Insert, PageUp、PageDown, ArrowUp、ArrowDown、ArrowLeft、ArrowRight
      # SaiPage.locator('//*[@id="Popover2-toggle"]').press("Z")
      # SaiPage.locator('//*[@id="Popover2-toggle"]').press("Delete")
  
          # 模拟组合键输入
          # Shift, Control, Alt, Meta(Meta = Win/Cmd 键)
          # 其他的按键参考这里：https://playwright.dev/python/docs/api/class-keyboard
      # SaiPage.keyboard.press("Meta+A")  
  
      # 鼠标点击
      # SaiPage.locator('//button[@class="Button SearchBar-searchButton FEfUrdfMIKpQDJDqkjte Button--primary Button--blue epMJl0lFQuYbC7jrwr_o JmYzaky7MEPMFcJDLNMG"]').click()
  
      # 回车
      # SaiPage.keyboard.press('Enter')
  
      # 页面向下滚动加载更多内容，直到不再加载
      NotEnd = True
      while NotEnd:
          # 滚动前的页面高度
          BeforeScrollHeight = SaiPage.evaluate("() => document.body.scrollHeight")
          # 滚动到页面底部
          SaiPage.evaluate("() => window.scrollTo(0,document.body.scrollHeight)")
          # 等待网络加载，单位是毫秒
          SaiPage.wait_for_timeout(3000)
          # 滚动后的页面高度
          AfterScrollHeight = SaiPage.evaluate("() => document.body.scrollHeight")
          if BeforeScrollHeight == AfterScrollHeight:
              # 知乎加载到一定程度，加载速度会变慢，但实际还没加载完
              SaiPage.wait_for_timeout(5000)
              # SaiPage.mouse.wheel(0, 20000)
              SaiPage.evaluate("() => window.scrollTo(0,document.body.scrollHeight)")
              AfterScrollHeight = SaiPage.evaluate("() => document.body.scrollHeight")
              # 两次等待，两次加载后依然页面高度不变，则判断为加载完了
              if BeforeScrollHeight == AfterScrollHeight:
                  NotEnd = False
  # ---------------------页面交互---------------------
  
  # ---------------------页面数据提取------------------
      # 全屏截图
      # path = "FullScreenShot.png"
      # SaiPage.screenshot(path)
  
      # 页面网址
      # PageURL = SaiPage.url
      # print('页面网址：', PageURL)
  
      # 页面标题
      # PageTitle = SaiPage.title()
      # print('页面标题：', PageTitle)
  
      # 页面完整Html
      # PageHtml = SaiPage.content()
      # print('页面Html：', PageHtml)
  
      # 页面完整文字
      # PageTextContent = SaiPage.text_content()
      # print('页面文字：', PageTextContent)
  
      # 页面某个节点的完整Html
      # ElementHtml = SaiPage.inner_html('//div[@class="QuestionHeader-topics"]')
      # BSHtml = BeautifulSoup(ElementHtml).prettify()
      # print(BSHtml)
  
      # # 页面某个节点的完整文字内容
      # # text_content：返回代码内容；一股脑全部获取，包括隐藏内容
      # # inner_text：返回页面显示内容；按照元素获取，以换行分割
      # ElementTextContent = SaiPage.text_content('//div[@class="QuestionHeader-topics"]')
      # ElementTextContent = SaiPage.inner_text('//div[@class="QuestionHeader-topics"]')
      # print(ElementTextContent)
  
      # 定位网页的列表元素 query_selector_all
      # Elements = SaiPage.query_selector_all('//div[@class="QuestionHeader-topics"]/div')
      # 枚举列表元素所有目标值
      # for element in Elements:
          # 每个元素的文本值 text_content
          # print(element.text_content())
          # 每个元素的链接 query_selector, get_attribute
          # print(element.query_selector('//a[@class="TopicLink"]').get_attribute('href'))
      # # 枚举列表中每个元素的每个属性值
      # for element in Elements:
      #     # 提取每个元素的所有属性 evaluate
      #     el_attrs = element.evaluate("el => el.getAttributeNames()")
      #     # 枚举所有的属性名称和值 get_attribute
      #     for attr in el_attrs:
      #         print(attr, ":", element.get_attribute(attr))
  # ---------------------页面数据提取------------------
  
  # ---------------------翻页------------------
     # 情况一：有下一页标签
      # 翻页方法1：底部导航条最后一个按钮不是【下一页】
      # 如：http://cpc.people.com.cn/GB/64093/64387/index16.html
      # TurnPage = True
      # while TurnPage:
      #     if SaiPage.locator('//div[@class="page"]/a[last()]').text_content() == '下一页':
      #         PageURL = SaiPage.url
      #         print('页面网址：', PageURL)
      #         SaiPage.locator('//div[@class="page"]/a[last()]').click()
      #     else:
      #         TurnPage = False
      #         print("没有下一页了...，爬取结束")
      # 翻页方法2：底部导航条最后一个按钮是【下一页】，但不可见
      # 如：https://space.bilibili.com/107861587/video?pn=13
      # TurnPage = True
      # while TurnPage:
      #     if SaiPage.is_visible('//li[@title="下一页"]/a'):
      #         SaiPage.click('//li[@title="下一页"]/a')
      #         timeout = random.randint(1500, 2500)
      #         SaiPage.wait_for_timeout(timeout)
      #         SaiPage.mouse.wheel(0,20000)
      #         PageURL = SaiPage.url
      #         print('页面网址：', PageURL)
      #     else:
      #         TurnPage = False
      #         print("没有下一页了...，爬取结束")
      # 翻页方法3：底部导航条最后一个按钮是【下一页】，可见，可不点击
      # 判断页面中是否存在某个元素：Page.locator(xpath).count() != 0
      # 如：https://movie.douban.com/top250?start=200
      # TurnPage = True
      # while TurnPage:
      #     if SaiPage.locator('//span[@class="next"]/link').count() != 0:
      #         PageURL = SaiPage.url
      #         print('页面网址：', PageURL)
      #         SaiPage.click('//span[@class="next"]')
      #     else:
      #         TurnPage = False
      #         print("没有下一页了...，爬取结束")
  # ---------------------翻页------------------
  
  # ---------------------收尾工作---------------------
      # 将SaiContext的cookie保存到state.json，方便未来免登录
      # storage = SaiContext.storage_state(path="state.json")
  
      SaiPage.pause()
      SaiContext.close()
      SaiBrowser.close()
  # ---------------------收尾工作---------------------
  
  with sync_playwright() as playwright:
      run(playwright)
  ```