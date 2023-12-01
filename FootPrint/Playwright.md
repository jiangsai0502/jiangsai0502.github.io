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
    > - `pip install pytest-playwright`

2. 为playwright安装浏览器

    > `playwright install`

3. 安装`stealth`插件，用来绕过无头浏览器检测

    > `pip install playwright-stealth`

4. 第一个录制脚本

    > `playwright codegen`
    > 
    > [教程](https://www.bilibili.com/video/BV1H24y1G745)

##### 网页爬虫实操

* 录制脚本

  > `playwright codegen`
  > 
  > [教程](https://www.bilibili.com/video/BV1H24y1G745)

* 常用功能

  > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310061535560.png)

* 使用PlayWright自带的Chromium

  ```python
  from playwright.sync_api import Playwright, sync_playwright
  import os, random
  from Module import Play_Wright_modules as pwm
  
  def run(playwright: Playwright) -> None:
      url = "https://space.bilibili.com/111082383/video"
      # 调用 Chromium 有头浏览器
      SaiBrowser, SaiContext, SaiPage = pwm.Initial_Chromium(
          playwright, url, headless=False, AbortPic=False, WaitLoad=False
      )
      # ------------- 代码逻辑 -------------#
      print(SaiPage.title)
      # ------------- 代码逻辑 -------------#
      # 收尾
      SaiPage.close()
      SaiContext.close()
      SaiBrowser.close()
  
  with sync_playwright() as playwright:
      run(playwright)
  ```

  > `SaiContext.route()`和 `SaiPage.route()`的区别：前者应用于 `SaiContext`下的所有页面，后者只应用于 `SaiPage`这一个页面

* 使用本地Chrome

  * 终端操作

    ```js
    // 查看9222端口是否被占用（端口可换）
    lsof -i:9222
    // 若结果如下，表示端口已被「Google进程」占用，PID为「645」
    COMMAND   PID     USER   FD   TYPE             DEVICE SIZE/OFF NODE NAME
    Google    645 jiangsai   59u  IPv4 0x3a42e324da35f619      0t0  TCP localhost:teamcoherence (LISTEN)
    // 杀掉进程，释放端口
    sudo kill -9 PID
    // 关闭当前所有Chrome浏览器
    // 启动本地Chrome有头浏览器
    /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --remote-debugging-port=9222
    ```

  * 代码部分

    ```python
    from playwright.sync_api import Playwright, sync_playwright
    import os, random
    from Module import Play_Wright_modules as pwm
    
    def run(playwright: Playwright) -> None:
        url = "https://space.bilibili.com/111082383/video"
        # 调用 本地Chrome 有头浏览器
        SaiBrowser, SaiContext, SaiPage = pwm.Initial_LocalChrome(playwright, url, AbortPic=False, WaitLoad=False)
        # ------------- 代码逻辑 -------------#
        print(SaiPage.title)
        # ------------- 代码逻辑 -------------#
        # 收尾
        SaiPage.close()
        SaiContext.close()
        SaiBrowser.close()
    
    with sync_playwright() as playwright:
        run(playwright)
    ```

* 页面交互

  * 打开一个网址

    `SaiPage.goto("https://www.zhihu.com/question/22543815")`

  * 等待页面加载，直至加载完成

    `SaiPage.wait_for_load_state("networkidle")`

  * 将这个tab页置于顶部

    `SaiPage.bring_to_front()`

  * 页面刷新

    `SaiPage.reload()`

  * 页面后退

    `SaiPage.go_back()`

  * 页面前进

    `SaiPage.go_forward()`

  * 鼠标悬停

    > 所有 `//`开头的表达式都会默认为 XPath

    `SaiPage.locator('//div[@class="Question"]').hover()`

  * 鼠标悬停

    > 所有 `//`开头的表达式都会默认为 XPath

    `SaiPage.locator('//div[@class="Question"]').hover()`

  * 键盘输入

    1. 模拟字符串输入

       `SaiPage.locator('//*[@id="Popover2"]').type('technical')`
       
    1. 模拟按键输入

       > `F(1-12)`,`数字(0-9)`,`Key(a-z、A-Z)大小写敏感`,`Backspace(向左删除)`,`Delete(向右删除)`,`Tab`,`Escape`,`End`,`Enter`,`Home`,`Insert`,`PageUp、PageDown`,`ArrowUp、ArrowDown、ArrowLeft、ArrowRight`
       
       `SaiPage.locator('//*[@id="Popover2"]').press("Z")`
       
       `SaiPage.locator('//*[@id="Popover2"]').press("Delete")`
       
       `SaiPage.keyboard.press('Enter')`
       
       `SaiPage.keyboard.press("Escape")`  ：常用于取消弹窗
       
      3. 模拟组合键输入

         > `Shift`, `Control`,` Alt`, `Meta(Meta = Win/Cmd 键)`
         >
         > [其他的按键参考这里](https://playwright.dev/python/docs/api/class-keyboard)
         
         全选 `Command+A`：`SaiPage.keyboard.press("Meta+A") `

  * 鼠标点击

    `SaiPage.locator('//button[@class="SearchBar"]').click()`

  * 页面滚动

    1. 滚动指定高度

       > `page.mouse.wheel(向右滚动长度,向下滚动长度)`

       `page.mouse.wheel(0,7000)`

    2. 滚动到页面底部

       `page.evaluate("() => window.scrollTo(0,document.body.scrollHeight)")`

    3. 滚动到页面顶部

       `page.evaluate("() => window.scrollTo(0,0)")`

    4. 向下滚动一屏

       `page.evaluate("() => window.scrollBy(0,window.innerHeight)")`

    5. 向上滚动一屏

       `page.evaluate("() => window.scrollBy(0,-window.innerHeight)")`

    6. 滚动到当前元素位置

       `element = page.locator(xpath)` 或 `element = page.query_selector(xpath)`

       `element.evaluate("element => element.scrollIntoView()")`
    
  * frame弹窗

    `SaiPage.frame_locator('//*[@id="iframe"]').locator('//div/input').click()`

* 页面数据提取

   * 截取页面当前可见部分

     `SaiPage.screenshot(path = "FullScreen.png")`

   * 截取页面指定部分

     `SaiPage.locator('//table[3]').screenshot(path = "PartPage.png")`

   * 截取整个页面

     `SaiPage.screenshot(path = "FullPage.png", full_page = True)`

   * 获取页面网址

     `PageURL = SaiPage.url`

   * 获取页面标题

     `PageTitle = SaiPage.title()`

   * 获取页面完整Html源代码

     `PageHtml = SaiPage.content()`

   * 获取页面某个节点的Html源代码

     `ElementHtml = SaiPage.locator('//div[@class="Question"]').inner_html()`

     `BSHtml = BeautifulSoup(ElementHtml).prettify()`

   * 获取页面完整文字

     `PageTextContent = SaiPage.text_content()`

   * 获取页面某个节点的完整文字内容

     > `text_content()`：返回代码内容；一股脑全部获取，包括隐藏内容
     >
     > `inner_text()`：返回页面显示内容；按照元素获取，元素间以换行分割

      `ElementTextContent = SaiPage.locator('//div[@class="HaHa"]').text_content()`

      `ElementInnerText = SaiPage.locator('//div[@class="HaHa"]').inner_text()`

   * 获取页面的列表元素

     ```python
     Elements = SaiPage.query_selector_all('//div[@class="Question"]/div')
     # 枚举列表元素所有目标值
      for element in Elements:
         # 每个元素的文本值 text_content
        print(element.text_content())
         # 每个元素的链接
        print(element.query_selector('//a[@id="Link"]').get_attribute('href'))
     ```

     ```python
     # 枚举列表中每个元素的每个属性值
     for element in Elements:
         # 提取每个元素的所有属性 evaluate
         el_attrs = element.evaluate("el => el.getAttributeNames()")
         # 枚举所有的属性名称和值 get_attribute
         for attr in el_attrs:
            print(attr, ":", element.get_attribute(attr))
     ```

   * 下载页面所有图片

     ```python
     Pic_folder = SaiPage.title()
     if not os.path.exists(Pic_folder):
         # 创建文件夹
         os.mkdir(Pic_folder)
        # 进入文件夹
         os.chdir(Pic_folder) 
     # 找到所有图片节点
     All_Pic = SaiPage.query_selector_all('//img')
     Pic_num = 1
     for Pic in All_Pic:
         # 提取所有图片链接
         Pic_url = Pic.get_attribute('src')
         if Pic_url != '':
             # 将图片写入文件
             with open(f'{Pic_num}.jpg', 'wb') as file:
                 file.write(requests.get(Pic_url).content)
                 Pic_num += 1
             print(Pic_url)
     ```

   * 将页面部分内容转化为 `markdown`后下载到本地

     ```python
     # 切换目录
     os.chdir('/Users/jiangsai/Desktop')
     MarkDownMaker = html2text.HTML2Text()
     MarkDownMaker.ignore_links = True
     TargetHtml = SaiPage.locator('//div[@class="article"]').inner_html()
     MarkDownContent = MarkDownMaker.handle(TargetHtml)
     with open('test.md', mode='w', encoding='utf-8') as f:
         f.write(MarkDownContent)

   1. 元素存在性判断[参考](https://www.cnblogs.com/yoyoketang/p/17214493.html)

      * `locator()`判断页面中是否存在某个元素

        > `locator()`定位页面上的元素，不管元素存不存在，都返回一个 `locator`对象，可用 `count() `方法统计元素个数，个数是 0则元素不存在

        ```python
        # 直接使用query_selector()和click()进行定位点击，若当前页面没有该元素则程序立刻报错
        # AttributeError：'NoneType' object has no attribute 'click'
        SaiPage.query_selector(xpath).click()
        # 因此要先判断一下，元素是否存在
        if SaiPage.query_selector(xpath) is not None:
           SaiPage.query_selector(xpath).click()
        ```

      * `query_selector()`判断页面中是否存在某个元素

          > `query_selector()`和 `query_selector_all()`定位页面上的Dom，若元素不存在则返回None

          ```python
        # 直接使用query_selector()和click()进行定位点击，若当前页面没有该元素则程序立刻报错
        # AttributeError：'NoneType' object has no attribute 'click'
        SaiPage.query_selector(xpath).click()
        # 因此要先判断一下，元素是否存在
        if SaiPage.query_selector(xpath) is not None:
           SaiPage.query_selector(xpath).click()
        ```

      * 判断某个节点是否有直接子节点存在

        > 平时可以直接用简写语句`'//div'`的双斜杠开头表示，这是个xpath，但是需要用到单斜杠时，就必须用到完整语句`'xpath=/div'`，`'xpath=/span'`，`'xpath=/*'`

        ```python
        if root_element.query_selector_all("xpath=/*") is not None:
            pass

      * 移除某个节点

        ```python
        Target_node = WritePage.query_selector(Xpath)
        Target_node_remove = Target_node.query_selector(Xpath)
        Target_node_remove.evaluate("element => element.remove()")

   2. 点击二级页链接

      1. 情况一：二级页在老标签加载

         ```python
         SaiPage.locator(xpath).click()
         SaiPage.wait_for_timeout(random.randint(1000,3000))
         # SaiPage是在打开二级页后，标签没有增加，一级页被二级页取代，未来只能操作二级页，但可以用SaiPage.go_back()在本标签回到一级页

      2. 情况二：二级页在新标签加载

         ```python
         with SaiContext.expect_page() as SonPageInfo:
             SaiPage.locator(xpath).click()
         SonPage = SonPageInfo.value
         SonPage.wait_for_load_state()
         SonPage.bring_to_front()
         # SaiPage是一级页的标签页，还在，SonPage是二级页的标签页，可以分别操作2个标签页
         ```

   3. 存储Cookie

      > 将 `cookie`保存到 `state.json`，方便方式二Playwright无头浏览器进行免登录

      `storage = SaiContext.storage_state(path="state.json")`

##### 通用方法

> 路径：`Module/Play_Wright_modules.py`
>
> [源码](Warehouse/Play_Wright_modules.md)

##### ChatGPT爬虫

> 向ChatGPT循环提交请求并获取请求结果
>
> [源码](Warehouse/Code_ChatGPT.md)

##### Json数据接口爬虫

> [参考](https://3yya.com/lesson/61)   [源码](Warehouse/Code_JsonCrawler.md#Json数据接口爬虫)

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

###### 场景一：【滚动加载】爬取一级页信息

> [源码](Warehouse/Code_Scroll_TopPage.md)
>
> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310171701388.png)
>
> > 1. 判断页面类型：问答题？专栏？视频？
> >2. 问答题
> >    1. 滚动加载全部答案
> >    2. 问题：获取问题标题 -> 展示收起的问题描述 -> 获取markdown描述
> >    3. 答案：获取答案list -> 获取每个答案的作者 -> 获取markdown内容
> > 3. 专栏
> >    * 获取专栏页的markdown内容
> > 4. 视频
> >    * 不爬

###### 场景二：【滚动加载】爬取二级页信息

> [源码](Warehouse/Code_Scroll_SonPage.md)
>
> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310171659341.png)
>
> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310181706425.png)
>
> > 1. 获取一级页条目list，并逐个点击进入二级页
> >2. 判断页面类型：问答题？专栏？视频？
> > 3. 问答题
> >    1. 滚动加载全部答案
> >    2. 问题：获取问题标题 -> 展示收起的问题描述 -> 获取markdown描述
> >    3. 答案：获取答案list -> 获取每个答案的作者 -> 获取markdown内容
> > 4. 专栏
> >    * 获取专栏页的markdown内容
> > 5. 视频
> >    * 不爬

###### 场景三：【翻页】提取一级页二级页信息

> [源码](Warehouse/Code_Turn_TopSonPage.md)
>
> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310180107192.png)
>
> > 1. 获取一级页条目list，提取每个条目信息
>>2. 逐个点击进入二级页，提取二级页信息
> > 3. 翻页



----

### 实战篇

###### 爬CCP文章

> [源码](Warehouse/Code_CCP.md)
>
> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310182349285.png)
>
> > 1. 获取一级页条目list
> >2. 逐个点击进入二级页，提取二级页信息
> > 3. 翻页

###### 爬Quora答案

> [源码](Warehouse/Code_Quora.md)
>
> quora的HTML节点层级非常非常多，且几乎找不到唯一性，故使用如下穷举的策略
>
> * 从顶部节点开始，一级一级列出所有子节点，逐个检测子节点是否包含答题者和答案
>   * 若不包含则切到下一个子节点
>   * 若包含则判断数量是否唯一
>     * 若唯一，则写入
>     * 若不唯一，则调用自身，列出自己的所有子节点
>
> > 1. 滚动加载全部答案
>>2. 问题：获取问题标题
> > 3. 答案：获取答案list -> 获取每个答案的作者 -> 点击展开每个答案内容 -> 获取markdown内容

###### 爬贴吧楼层

> [源码](Warehouse/Code_TieBa.md)
>
> 1. 滚动加载全部可见内容
>2. 获取标题
> 3. 获取所有楼层
>    1. 获取楼层信息：作者、回答时间、MarkDown内容
>    2. 获取楼层评论
>       1. 若评论被折腾，点击「点击查看」展开
>       2. 获取每条评论：作者、文字内容
>       3. 评论翻页
> 4. 页面翻页

###### 爬人人都是产品经理-36氪

> [源码](Warehouse/Code_WSPM.md)
>
> 网页结构简单，只需要抓标题和内容即可

###### 爬微博个人主页

> [源码](Warehouse/Code_WeiBo.md)

###### 爬金色财经实时新闻

> [源码](Warehouse/Code_Jinse.md)

###### 爬抖音搜索用户列表

> [源码](Warehouse/Code_DouYin.md)

