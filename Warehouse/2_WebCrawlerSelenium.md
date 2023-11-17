# Selenium + Chrome Headless

#### 1. 安装环境

1. 切换到 `py3` 虚拟环境：`source activate py3`

2. 查看当前环境是否已包含 `Scrapy` 模块：`conda list`

3. 安装 `selenium` 模块：`pip install selenium`

4. 下载 [chromedriver驱动器](https://sites.google.com/a/chromium.org/chromedriver/home)，因为Chrome 版本是 79.0.3945.130，因此ChromeDriver版本选 79.0.3945.36

5. 将` chromedriver驱动器` 移动到虚拟环境中 `/Users/sai/opt/anaconda3/envs/py3_demo/bin`

   1. 先确定虚拟环境位置：`which python`得知`/Users/sai/opt/anaconda3/envs/py3_demo/bin/python/`

6. 将` chromedriver驱动器`加入环境变量

   `open ~/.bash_profile`

   最后插入一行：`export PATH=$PATH:/Users/sai/opt/anaconda3/envs/py3_demo/bin/chromedriver`

   `source ~/.bash_profile`

#### 2. 基础用法

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
import os, requests, time, json, pickle
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def BasicInfo(driver):
    driver.get('https://www.baidu.com/')
    # 当前页面的url
    print(driver.current_url)
    # 当前页面源码，转码成中文，加ignore避免无法识别的生僻字
    print(driver.page_source.encode("gbk","ignore"))
    # 刷新页面
    driver.refresh()
    # 窗口最大化
    driver.maximize_window()
    # 页面title
    print(driver.title)

# 基本用法
def BasicUsage(driver):
    driver.get('https://www.baidu.com/')
    # find_element 获取WebElement对象
    # 向WebElement对象输入内容
    driver.find_element_by_xpath('//*[@id="kw"]').send_keys('sai的小站')
    # 点击WebElement对象
    driver.find_element_by_xpath('//*[@id="su"]').click()
    # 清空输入框
    driver.find_element_by_xpath('//*[@id="kw"]').clear()
    # 获取WebElement对象的文本内容
    temp = driver.find_element_by_xpath('//*[@id="1"]/h3/a').text
    print(temp)
    # get_attribute() 获取WebElement对象的某个属性的值，括号内是属性名
    temp = driver.find_element_by_xpath('//*[@id="1"]').get_attribute('srcid')
    print(temp)
    # get_attribute('outerHTML') 获取WebElement对象的某个属性的全部Html
    temp = driver.find_element_by_xpath('//*[@id="1"]').get_attribute('outerHTML')
    print(temp)
    # 模糊查找文本
    temp = driver.find_elements_by_partial_link_text('百度')
    for i in temp:
        print(i.text)

# 创建新标签
def CreateTab(driver):
    # js新建标签
    driver.execute_script('window.open();')
    # 获取当前浏览器所有标签的句柄
    handles = driver.window_handles
    # 获取当前标签的句柄
    main_handle = driver.current_window_handle
    # 切换标签
    driver.switch_to.window(handles[-1])
    # 新标签打开网页
    driver.get('https://www.sogou.com/')

# 页面含frame时
def FrameSwith(driver):
    # 当页面内包含frame时，切入指定frame才能选择元素
    # 页面默认是主frame
    driver.get('https://www.w3school.com.cn/html/html_iframe.asp')
    temp = driver.find_element_by_xpath('//*[@id="maincontent"]/h1').text
    print('默认frame主题是：'+ temp)
    # 找到目标frame
    aim_frame = driver.find_element_by_xpath('//*[@id="intro"]/iframe')
    # 切换到目标frame
    driver.switch_to.frame(aim_frame)
    temp = driver.find_element_by_xpath('//*[@id="maincontent"]/h1').text
    print('子frame主题是：'+ temp)
    # 切回默认frame
    driver.switch_to.default_content()
    temp = driver.find_element_by_xpath('//*[@id="maincontent"]/h1').text
    print('子frame主题是：'+ temp)

# Radio，Checkbox，Select控件操作方式
def CheckedWidgets(driver):
    driver.get('file:///Users/sai/Documents/GitHub/jiangsai0502.github.io/Sai_FootPrint/LearnHtml.html')
    # 选中某个Radio选项
    driver.find_element_by_xpath('//*[@id="main"]/form[1]/input[@value="female"]').click()
    # 获取选中项的值
    for input in driver.find_elements_by_xpath('//*[@id="main"]/form[1]/input'):
        if input.is_selected():
            print(input.get_attribute('value'))

    # 选中某个Checkbox选项
    driver.find_element_by_xpath('//*[@id="main"]/form[2]/input[@value="Bike"]').click()
    # 获取选中项的值
    for input in driver.find_elements_by_xpath('//*[@id="main"]/form[2]/input'):
        if input.is_selected():
            print(input.get_attribute('value'))
    
    # 选中某个Select选项
    driver.find_element_by_xpath('//*[@id="main"]/select/option[@value="saab"]').click()
    for input in driver.find_elements_by_xpath('//*[@id="main"]/select/option'):
        if input.is_selected():
            print(input.get_attribute('value'))

# 弹窗操作方式
def Popup(driver):
    driver.get('file:///Users/sai/Documents/GitHub/jiangsai0502.github.io/Sai_FootPrint/LearnHtml.html')
    # 1.alert
    driver.find_element_by_xpath('/html/body/button[1]').click()
        # 打印alert提示信息
    print(driver.switch_to.alert.text)
        # 点击alert的OK按钮
    driver.switch_to.alert.accept()
    # 2.confirm
    driver.find_element_by_xpath('/html/body/button[2]').click()
        # 打印confirm提示信息
    print(driver.switch_to.alert.text)
        # 点击confirm的OK按钮
        # driver.switch_to.alert.accept()
        # 点击confirm的Cancel按钮
    driver.switch_to.alert.dismiss()
    # 3.prompt
    driver.find_element_by_xpath('/html/body/button[3]').click()
        # 打印prompt提示信息
    print(driver.switch_to.alert.text)
        # 向prompt输入信息
    driver.switch_to.alert.send_keys('你猜猜我想说什么')
        # 点击prompt的OK按钮
        # driver.switch_to.alert.accept()
        # 点击prompt的Cancel按钮
    driver.switch_to.alert.dismiss()

# 模拟滚动到底
def Scroll(driver):
    driver.get('https://www.zhihu.com/question/23498580')
    old_height = 0
    while True:
        new_height = driver.execute_script('return action=document.body.scrollHeight')
        # 每执行一次滚动条拖到最后，就进行一次参数校验，并且刷新页面高度
        if new_height > old_height:
            driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
            old_height = new_height
            time.sleep(1)
        else:
            # 当页面高度不再增加的时候，我们就认为已经是页面最底部，结束条件判断
            print("滚动条已经处于页面最下方!")
            driver.execute_script('window.scrollTo(0, 0)')  # 把滚动条拖到页面顶部
            break
# 翻页
def NextPage(driver):
    driver.get('https://search.bilibili.com/')
    driver.find_element_by_xpath('//*[@id="search-keyword"]').send_keys('测试一下网站',Keys.ENTER)
    # 元素不存在时，find_element抛异常，find_elements返回空列表，所以用后者判断是否存在该元素
    while driver.find_elements_by_xpath('//li[@class="page-item next"]'):
        driver.find_element_by_xpath('//li[@class="page-item next"]').click()
        time.sleep(2)

# 更多鼠标键盘操作
# ActionChains支持链式写法，即调用ActionChains方法不会立即执行，而是将所有操作顺序放入队列中，调用perform()方法后顺序执行队列中的方法
def MouseActions(driver):
    driver.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
    driver.switch_to.frame("iframeResult")
    source = driver.find_element_by_xpath('//*[@id="draggable"]')
    target = driver.find_element_by_xpath('//*[@id="droppable"]')
    # 1.鼠标悬停
    ActionChains(driver).move_to_element(source).perform()
    # 2.鼠标右键
    ActionChains(driver).context_click(target).perform()
    # 3.鼠标双击
    ActionChains(driver).double_click(target).perform()
    # 4.鼠标左键按住source，拖拽到距离原位置(300,500)的右下角
    ActionChains(driver).drag_and_drop_by_offset(source,150,200).perform()
    # 5.鼠标左键按住source，拖拽到target位置
    # ActionChains(driver).drag_and_drop(source,target).perform()
    # driver.switch_to.alert.accept()
    # 6.(功能同5)鼠标左键按住source，拖拽到target位置，释放鼠标
    ActionChains(driver).click_and_hold(source).move_to_element(target).release().perform()
    driver.switch_to.alert.accept()
    pass

def KeyActions(driver):
    driver.get('https://www.baidu.com/')
    # 输入框输入内容
    driver.find_element_by_xpath('//*[@id="kw"]').send_keys("seleniummmm")
    # 删除多输入的一个字母，先定位光标，再输入BACKSPACE键
    driver.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.BACK_SPACE)
        # 此时光标已经在输入框中，所以还能直接用ActionChains(driver)
    ActionChains(driver).send_keys(Keys.BACK_SPACE).perform()
        # Keys.BACK_SPACE对应的key是'\ue003'
    ActionChains(driver).send_keys('\ue003').perform()
    # 输入空格键+“教程”
    ActionChains(driver).send_keys(Keys.SPACE, "教程").perform()
    # Mac上的Keys.CONTROL无效，是个bug。FireFox没问题
    # 通过回车键来代替单击操作
    driver.find_element_by_xpath('//*[@id="kw"]').send_keys(Keys.ENTER)
    # ActionChains(driver).send_keys( Keys.Alt+"q").perform()容易出错
    # ActionChains(driver).key_down(Keys.ALT).send_keys("q").key_up(Keys.ALT).perform()更好

# 设置获取cookie
def GetSetCookie(driver):
    driver.get('https://www.douban.com/')
    cookieFile = '~/zhihuCookie.json'
    if not os.path.exists(cookieFile):
        # 首先清除由于浏览器打开已有的cookies
        driver.delete_all_cookies()
        # cookie文件不存在时，要先手工登录一下，以便获取
        input("请先手工登录一下，然后回车")
        dictCookies = driver.get_cookies()
        print(dictCookies)
        with open(cookieFile, 'w') as f:
            json.dump(dictCookies, f)
    else:
        # 清空所有cookie
        driver.delete_all_cookies()
        driver.refresh()
        with open(cookieFile, 'r') as f:
            listCookies = json.load(f)
        print(listCookies)
        for cookie in listCookies:
            driver.add_cookie(cookie)
        # time.sleep(2)
        driver.refresh()

def GetResousce(driver):
    driver.get("https://www.baidu.com/")
    #静态资源链接存储集合
    urls = []
    #获取静态资源有效链接
    for log in driver.get_log('performance'):
        if 'message' not in log:
                continue
        log_entry = json.loads(log['message'])
        try:
            #该处过滤了data:开头的base64编码引用和document页面链接
                if "data:" not in log_entry['message']['params']['request']['url'] and 'Document' not in  log_entry['message']['params']['type']:
                    urls.append(log_entry['message']['params']['request']['url'])
        except Exception as e:
                pass
    # print(urls)
    for url in urls:
        if url.endswith('.woff2'):
            print('-'*20,'\n',url,'\n','-'*20)

if __name__ == '__main__':
    try:
        # 创建浏览器
        path = "/Users/sai/opt/anaconda3/envs/py3_demo/bin/chromedriver"
        options = Options()
        # 获取资源文件会用到类DesiredCapabilities
        desiredCapabilities = DesiredCapabilities.CHROME
        desiredCapabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
        # True为无头浏览器
        # options.headless = True  
        # 托管当前打开的浏览器，先命令行打开浏览器（见参考2）
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        driver = webdriver.Chrome(executable_path=path, options=options, desired_capabilities=desiredCapabilities)
        # 每隔0.5秒检查一次元素是否加载完成，最多等6秒
        driver.implicitly_wait(6)

        # BasicInfo(driver)
        # BasicUsage(driver)
        # CreateTab(driver)
        # FrameSwith(driver)
        # CheckedWidgets(driver)
        # Popup(driver)
        # MouseActions(driver)
        # KeyActions(driver)
        # GetSetCookie(driver)
        # Scroll(driver)
        # NextPage(driver)
        GetResousce(driver)
        
    finally:
        # 关闭当前标签
        driver.close()
        # 关闭当前浏览器
        driver.quit()
```

1. [Python下selenium 打开新的窗口和切换到其他窗口](https://www.jianshu.com/p/affcccdf5ea2)

2. [mac selenium 连接已经打开的chrome浏览器](https://blog.csdn.net/w5688414/article/details/106032555/)

   ```bash
   # 1. 向~/.zshrc添加环境变量
   open ~/.zshrc
   export PATH="/Applications/Google Chrome.app/Contents/MacOS:$PATH"
   source ~/.zshrc
   
   # 2. 打开chrome
   # –remote-debugging-port=9222：指定启动端口9222
   # –user-data-dir="/ChromeProfile"：指定浏览器数据存储目录
   cd ~/Documents/Temp;
   Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"
   # 3. 程序增加1行
   options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
   ```

3. 对于鼠标悬停出现，鼠标移开消失的元素，可以冻住页面

   1. Console中执行`setTimeout(function(){ debugger }, 2000);`，即可冻住页面2秒

      <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200627232839.png" style="zoom:30%;" />

4. [selenium 键盘操作 键盘对应的key](https://blog.csdn.net/chang995196962/article/details/106499208)

5. [通过DesiredCapabilities获取请求的资源文件](https://stackoverflow.com/questions/27644615/getting-chrome-performance-and-tracing-logs)





#### 下载学习强国视频

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os, requests

def GetUrls(driver, original_url):
    print('-'*15,'获取所有视频网址列表','-'*15)
    driver.get(original_url)
    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'loaded')))

    video_list = driver.find_elements_by_xpath('//*[@id="detail_sections_list"]/li')
    head_url = 'https://article.xuexi.cn/articles/video/index.html?art_id='
    Urls = []
    for video in video_list:
        video_url = head_url + video.find_element_by_xpath('./a').get_attribute('data-id')
        Urls.append(video_url)
        # exit()
    return Urls

def GetVideoInfos(Urls):
    print('-'*15,'获取所有视频名称和下载链接','-'*15)
    VideoInfos = []
    for url in Urls:
        driver.get(url)
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, 'loaded')))

        info = {}
        info['src'] = driver.find_element_by_xpath('//*[@id="dplayer-video-wrap"]/video').get_attribute('src')
        info['name'] = driver.find_element_by_xpath('//*[@id="main"]/div[2]/div[1]/div[1]/div[1]/h1').text
        VideoInfos.append(info)
    return VideoInfos
    
def DownLoadVideos(VideoInfos):
    print('-'*15,'下载所有视频','-'*15)
    for VideoInfo in VideoInfos:
        DownLoadVideoFolder = 'DownLoadVideo'
        if not os.path.exists(DownLoadVideoFolder):
            os.mkdir(DownLoadVideoFolder)

        suffix = VideoInfo['src'].split('.')[-1]
        VideoName = VideoInfo['name'] + '.' + suffix
        VideoPath = os.path.join(DownLoadVideoFolder, VideoName)

        print(f'正在下载{VideoName}')
        VideoByte = requests.get(VideoInfo['src'])
        with open(VideoPath, 'wb') as f:
            f.write(VideoByte.content)
        print('下载完成')

if __name__ == '__main__':
    original_url = 'https://article.xuexi.cn/articles/video/index.html?art_id=2457151200699439109'
    options = Options()
    options.headless = True
    driver = webdriver.Chrome(options=options)
    
    Urls = GetUrls(driver, original_url)
    VideoInfos = GetVideoInfos(Urls)
    DownLoadVideos(VideoInfos)
    driver.close()
```

> * 显性等待模块 `WebDriverWait` 
>
>   * `WebDriverWait(driver, 10)`，等待的最长时间为10秒，10秒之内条件成立则执行下一步，10秒之后抛 TimeoutException 异常
>
> * 预期条件判断模块 `expected_conditions` 
>
>   * `presence_of_element_located`，判断某个元素是否被加到了 dom 树里
>
> * 定位模块 `By` 
>
>   * `By.ID`，`By.NAME`，`By.CLASS_NAME`，`By.XPATH`，`By.TAG_NAME`，`By.CSS_SELECTOR`，`By.LINK_TEXT`
>
> * Webdriver在页面内定位元素： `find_element_by……` 和 `find_elements_by……` 
>
>   * `find_element_by_id()`
>     
>   * `find_element_by_name()`
>     
>   * `find_element_by_tag_name()`
>     
>   * `find_element_by_class_name()`
>     
>   * `find_element_by_xpath()`
>     
>   * `find_element_by_link_text()`
>     
>   * `find_element_by_css_selector()`
>     
>     > * `find_element`：返回第一个复合条件的`WebElement`对象，若找不到对象，则抛异常
>     > * `find_elements` ：返回所有复合条件的`WebElement`对象组成的列表，若找不到对象，则返回空列表
>
> * `WebElement`对象在对象内定位元素
>
> * `get_attribute`
>
>   实际参数用法
>
>   * `video_element.get_attribute("test")`：获取 `video_element`标签的 `test`属性的值
>
>   固定参数用法
>
>   * `video_element.get_attribute('innerHTML')`：获取`video_element`标签内的全部HTML，不包含`video_element`标签
>   * `video_element.get_attribute('outerHTML')`：获取`video_element`标签内的全部HTML，包含`video_element`标签
>   * `video_element.get_attribute(‘textContent’)`：获取`video_element`标签的文本内容
>
> * 获取元素方法
>
>   * 方法 1：webdriver的 `find_element_by……` 和 `find_elements_by……` 方法
>   * 方法 2：BeautifulSoup：`soup = BeautifulSoup(driver.page_source, "lxml")`
>   * 方法 3：XPath：`XpathTree = etree.HTML(driver.page_source)`

#### 下载总统教师资格证视频

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
import os, requests, time, json, pickle
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def GetResousce(driver):
    driver.get('https://www.zongtongedu.com/video/video?examid=19&year=2020&courseid=1&vtid=346&vtfid=6')
    res_urls = []
    tar_url = ''
    
    # 获取所有视频（真题解析班）
    video_list = driver.find_elements_by_xpath('//*[@id="videoDetail"]/li')
    for video_url in video_list:
        # 逐个点击视频链接
        video_url.click()
        time.sleep(2)
        for log in driver.get_log('performance'):
            if 'message' not in log:
                    continue
            log_entry = json.loads(log['message'])
            try:
                    if "data:" not in log_entry['message']['params']['request']['url'] and 'Document' not in  log_entry['message']['params']['type']:
                        res_urls.append(log_entry['message']['params']['request']['url'])
            except Exception as e:
                    pass
        Movie_Name = driver.find_element_by_xpath('//li[@class="videoZhangListThis"]').text
        for url in res_urls:
            if url.endswith('.mp4'):
                print(url)
                tar_url = f'you-get {url} -O {Movie_Name}'
        print(tar_url,'\n')
        os.system(tar_url)
    # 获取所有模块(精讲班)
    # model_list = driver.find_elements_by_xpath('//*[@id="videoDetail"]/li')
    # for model_url in model_list:
    #     # 逐个点击模块链接
    #     model_url.click()
    #     time.sleep(2)
    #     video_list = model_url.find_elements_by_xpath('ul/li')
    #     #获取所有视频连接的元素
    #     for video_url in video_list:
    #         # 逐个点击视频链接
    #         video_url.click()
    #         time.sleep(2)
    #         for log in driver.get_log('performance'):
    #             if 'message' not in log:
    #                     continue
    #             log_entry = json.loads(log['message'])
    #             try:
    #                     if "data:" not in log_entry['message']['params']['request']['url'] and 'Document' not in  log_entry['message']['params']['type']:
    #                         res_urls.append(log_entry['message']['params']['request']['url'])
    #             except Exception as e:
    #                     pass
    #         Movie_Name = driver.find_element_by_xpath('//li[@class="videoZhangListThis"]').text
    #         for url in res_urls:
    #             if url.endswith('.mp4'):
    #                 tar_url = f'you-get {url} -O {Movie_Name}'
    #         print(tar_url,'\n')
    #         os.system(tar_url)

if __name__ == '__main__':
    try:
        # 创建浏览器
        path = "/Users/sai/opt/anaconda3/envs/py3_demo/bin/chromedriver"
        options = Options()
        # 获取资源文件会用到类DesiredCapabilities
        desiredCapabilities = DesiredCapabilities.CHROME
        desiredCapabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
        # 设置pageLoadStrategy不等网络加载完也可以操作
        # desiredCapabilities["pageLoadStrategy"] = "none"
        # True为无头浏览器
        # options.headless = True
        # 托管当前打开的浏览器，先命令行打开浏览器（见参考2）
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        driver = webdriver.Chrome(executable_path=path, options=options, desired_capabilities=desiredCapabilities)
        # 每隔0.5秒检查一次元素是否加载完成，最多等10秒
        driver.implicitly_wait(5)

        GetResousce(driver)
        
    finally:
        # 关闭当前标签
        driver.close()
        # 关闭当前浏览器
        driver.quit()
```

##### 下载《得到》音频

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
import os, requests, time, json, pickle
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def GetResousce(driver):
    driver.get('https://www.biji.com/article/ml9WNdP1QvaeKYG0PJAzx82Dyog0BZ')
    res_urls = []
    tar_url = ''
    
    # 获取条目数量
    Model_list = driver.find_elements_by_xpath('//*[@id="app"]/div[2]/div[2]/div[1]/div[3]/div/div[1]/div')
    flag = False
    for model in Model_list[3:]:
        Item_list = model.find_elements_by_xpath('ul/li')
        for item in Item_list:
            # 获取所有可点击的音频按钮数量
            if not item.find_elements_by_xpath('div/div[2]/div[2]'):
                continue
            else:
                # selenium模拟点击被网页检查
                # item.find_element_by_xpath('div/div[2]/div[2]').click()
                # js模拟点击没问题
                temp = item.find_element_by_xpath('div/div[2]/div[2]')
                driver.execute_script("arguments[0].click();", temp)
                time.sleep(2)
            for log in driver.get_log('performance'):
                if 'message' not in log:
                        continue
                log_entry = json.loads(log['message'])
                try:
                        if "data:" not in log_entry['message']['params']['request']['url'] and 'Document' not in  log_entry['message']['params']['type']:
                            res_urls.append(log_entry['message']['params']['request']['url'])
                except Exception as e:
                        pass
            # 音频名称
            Audio_Name = driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div/div[1]/div[2]/div[2]/h5/em').text
            for url in res_urls:
                if url.endswith('.m3u8'):
                    # print(url)
                    tar_url = f'ffmpeg -i {url} -c copy {Audio_Name}.m4a'
            print(tar_url,'\n')
            if Audio_Name=='第111讲丨违约与赔偿':
                flag = True
            if flag:
                os.system(tar_url)
            
if __name__ == '__main__':
    try:
        path = "/Users/sai/opt/anaconda3/envs/py3_demo/bin/chromedriver"
        options = Options()
        desiredCapabilities = DesiredCapabilities.CHROME
        desiredCapabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        driver = webdriver.Chrome(executable_path=path, options=options, desired_capabilities=desiredCapabilities)
        driver.implicitly_wait(5)

        GetResousce(driver)
        
    finally:
        driver.close()
        driver.quit()
```

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
import os, requests, time, json, pickle
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def GetResousce(driver):
    driver.get('https://www.dedao.cn/article/7EGBgdkRbn1mKg3ngKY890D3rvPOAN')
    res_urls = []
    tar_url = ''

    # 获取条目数量
    Model_list = driver.find_elements_by_xpath('//*[@id="app"]/div[2]/div[2]/div[2]/div[3]/div/div[1]/ul/li')
    for model in Model_list:
        temp = model.find_element_by_xpath('div/div[2]/div[2]')
        driver.execute_script("arguments[0].click();", temp)
        time.sleep(2)

        for log in driver.get_log('performance'):
            if 'message' not in log:
                    continue
            log_entry = json.loads(log['message'])
            try:
                    if "data:" not in log_entry['message']['params']['request']['url'] and 'Document' not in  log_entry['message']['params']['type']:
                        res_urls.append(log_entry['message']['params']['request']['url'])
            except Exception as e:
                    pass
        # 音频名称
        Audio_Name = driver.find_element_by_xpath('//*[@id="app"]/div[4]/div/div/div[1]/div[2]/div[2]/h5/em').text.replace(' ', '').replace('|', '-')
        for url in res_urls:
            if url.endswith('.m3u8'):
                tar_url = f'ffmpeg -i {url} -c copy {Audio_Name}.m4a'
        print(tar_url,'\n')
        os.system(tar_url)

if __name__ == '__main__':
    try:
        path = "/Users/sai/opt/anaconda3/envs/py3_demo/bin/chromedriver"
        options = Options()
        desiredCapabilities = DesiredCapabilities.CHROME
        desiredCapabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        driver = webdriver.Chrome(executable_path=path, options=options, desired_capabilities=desiredCapabilities)
        driver.implicitly_wait(5)

        GetResousce(driver)

    finally:
        driver.close()
        driver.quit()
```



##### 下载荔枝

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
import os, requests, time, json, pickle
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def GetResousce(driver):
    driver.get('https://m.lizhi.fm/vod/voicesheet/30161735618871067')
    res_urls = []
    tar_url = ''
    
    # 获取条目数量
    Url_list = driver.find_elements_by_xpath('//*[@id="app"]/div/div[5]/a')
    for url in Url_list:
        down_url = url.get_attribute('href')
        # 新建标签
        driver.execute_script('window.open();')
        handles = driver.window_handles
        main_handle = driver.current_window_handle
        print(driver.title)
        # 切换到最后一个标签
        driver.switch_to.window(handles[-1])
        driver.get(down_url)
        print(driver.title)
        for log in driver.get_log('performance'):
            if 'message' not in log:
                    continue
            log_entry = json.loads(log['message'])
            try:
                    if "data:" not in log_entry['message']['params']['request']['url'] and 'Document' not in  log_entry['message']['params']['type']:
                        res_urls.append(log_entry['message']['params']['request']['url'])
            except Exception as e:
                    pass
        # 音频名称
        Audio_Name = driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/h1').text.replace(' ', '').replace('(', '').replace(')', '')
        for url in res_urls:
            if url.endswith('.mp3'):
                tar_url = f'youtube-dl {url} -o {Audio_Name}.mp3'
        print(tar_url,'\n')
        os.system(tar_url)
        # 关闭标签
        driver.close()
        # handle切回主标签
        driver.switch_to.window(main_handle)
            
if __name__ == '__main__':
    try:
        path = "/Users/sai/opt/anaconda3/envs/py3_demo/bin/chromedriver"
        options = Options()
        desiredCapabilities = DesiredCapabilities.CHROME
        desiredCapabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        driver = webdriver.Chrome(executable_path=path, options=options, desired_capabilities=desiredCapabilities)
        driver.implicitly_wait(5)

        GetResousce(driver)
        
    finally:
        driver.close()
        driver.quit()
```

**模拟登录访问Hipda**

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC
import os, requests

def Login(login_url):

    driver.get(login_url)
    driver.find_element_by_xpath('//*[@id="umenu"]/a[2]').click()   #首页点击右上角的登录，进入登录页面
    driver.find_element_by_name('username').send_keys('荒江孤叟')   #默认是用户名登录
    driver.find_element_by_name('password').send_keys('hipda1122334')
    driver.find_element_by_name('loginsubmit').click()

    wait = WebDriverWait(driver, 10)
    wait.until(EC.presence_of_element_located((By.ID, 'forum6')))

    name = driver.find_element_by_xpath('//*[@id="forum6"]/tr/th/div/h2/a').text
    print(name)

if __name__ == '__main__':
    home_page_url = 'https://www.hi-pda.com/forum/'
    options = Options()
    # options.headless = True   # 测试登录时注释掉这句，则会看到登录的场景
    driver = webdriver.Chrome(options=options)
    Login(home_page_url)
```

预定北师研究室

1. 启动程序

   ```python
   # 直接运行主程序总是预定失败，不明所以，因此外部套一层调用程序
   import os,datetime,time
   # 调用系统命令
   while True:
       print("dispatch：",datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
       if(datetime.datetime.now().strftime('%H:%M') == '00:02'):
           os.system('python3 ~/Documents/Temp/抢研究间.py')
           break
       time.sleep(59)
   ```

2. 主程序

   ```python
   import requests,datetime,time,schedule
   
   jscookie = 0
   
   def Login(url, user):
       LoginHeaders = {
       "Accept": "application/json, text/javascript, */*; q=0.01",
       "Referer": "http://219.224.28.56/ClientWeb/xcus/ic2/Default.aspx",
       "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
       "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
       }
       # 每次登录前先登出
       LoginReq = requests.post(url, data=user, headers=LoginHeaders)
       requests.get("http://219.224.28.56/ClientWeb/pro/ajax/login.aspx?act=logout")
       LoginReq = requests.post(url, data=user, headers=LoginHeaders)
       print(LoginReq.status_code)
       print(LoginReq.text)
       global jscookie
       jscookie = "ASP.NET_SessionId="+requests.utils.dict_from_cookiejar(LoginReq.cookies)['ASP.NET_SessionId']
   
   def POST(url, t):
       PostHeaders = {
           "Host": "219.224.28.56",
           "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
           "Accept": "application/json, text/javascript, */*; q=0.01",
           "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
           "Accept-Encoding": "gzip, deflate",
           "Referer": "http://219.224.28.56/ClientWeb/xcus/ic2/Default.aspx",
           "Connection": "keep-alive",
           "Cookie": jscookie
           }
       datas = {
           'dev_id':'770',  # 770是419研究间
           'lab_id':'131',
           'kind_id':'1257',
           'type':'dev',
           'start':'0000-00-00 00:00',
           'end':'0000-00-00 00:00',
           'act':'set_resv'
           }
       datas['start'] = t['start']
       datas['end'] = t['end']
       
       PostReq = requests.post(url,data=datas,headers=PostHeaders)
       print(PostReq.status_code)
       print(PostReq.text)    
   
   if __name__ == '__main__':
       LoginUrl = "http://219.224.28.56/ClientWeb/pro/ajax/login.aspx"
       PostUrl = "http://219.224.28.56/ClientWeb/pro/ajax/reserve.aspx"
       users = [{
           'id':'1111',  # 罗云
           'pwd':'1111',
           'act':'login'
           },{
           'id':'2222',  # 雁飞
           'pwd':'2222',
           'act':'login'
           }
           ]
       tomorrow = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d')
       times = [{
           'start':tomorrow+' 10:00',
           'end':tomorrow+' 14:00'
       },{
           'start':tomorrow+' 14:00',
           'end':tomorrow+' 18:00'
       },{
           'start':tomorrow+' 18:00',
           'end':tomorrow+' 21:30'
       }
       ]
   
       for user in users:
           Login(LoginUrl, user)
           time.sleep(2)
           for t in times:
               POST(PostUrl, t)
               time.sleep(2)
   ```

下载超星音频

```python
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver import ActionChains
import os, requests, time, json, pickle
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

def GetResousce(driver):
    driver.get('https://special.chaoxing.com/mobile/mooc/tocourse/95755212')
    res_urls = []
    tar_url = ''

    # 获取条目数量
    Url_list = driver.find_elements_by_xpath('/html/body/div[3]/div[2]/div/div/ul/li')
    for url in Url_list:
        down_url = url.find_element_by_xpath('a').get_attribute('attr')
        # 音频名称
        Audio_Name = url.find_element_by_xpath('a').get_attribute('chaptername').replace(' ', '_').replace('：', '_').replace('，', '_')
        # 新建标签
        driver.execute_script('window.open();')
        handles = driver.window_handles
        main_handle = driver.current_window_handle
        print(driver.title)
        # 切换到最后一个标签
        driver.switch_to.window(handles[-1])
        driver.get(down_url)
        print(driver.title)
        # 找到目标iframe
        if driver.find_elements_by_xpath('//*[@id="contentBox"]/div[1]/p[1]/div/iframe'):
            aim_frame = driver.find_element_by_xpath('//*[@id="contentBox"]/div[1]/p[1]/div/iframe')
            # 切换到目标iframe
            driver.switch_to.frame(aim_frame)
        # 点击播放，使音频加载入缓存
        if driver.find_elements_by_xpath('//*[@id="reader"]/div/div[1]/a'):
            driver.find_element_by_xpath('//*[@id="reader"]/div/div[1]/a').click()

        for log in driver.get_log('performance'):
            if 'message' not in log:
                    continue
            log_entry = json.loads(log['message'])
            try:
                    if "data:" not in log_entry['message']['params']['request']['url'] and 'Document' not in  log_entry['message']['params']['type']:
                        res_urls.append(log_entry['message']['params']['request']['url'])
            except Exception as e:
                    pass
        print("")
        for url in res_urls:
            if '.mp3' in url:
                tar_url = f'you-get -O {Audio_Name}.mp3 {url}'
                # tar_url = f'youtube-dl {url} -o {Audio_Name}.mp3'

                # break
        print(tar_url,'\n')
        os.system(tar_url)
        # 暂停便于调试
        # input()
        # 关闭标签
        driver.close()
        # handle切回主标签
        driver.switch_to.window(main_handle)

if __name__ == '__main__':
    try:
        path = "/Users/sai/opt/anaconda3/envs/py3_demo/bin/chromedriver"
        options = Options()
        # 测试登录时注释掉这句，则会看到登录的场景
        options.headless = True
        desiredCapabilities = DesiredCapabilities.CHROME
        desiredCapabilities['goog:loggingPrefs'] = {'performance': 'ALL'}
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        driver = webdriver.Chrome(executable_path=path, options=options, desired_capabilities=desiredCapabilities)
        driver.implicitly_wait(5)

        GetResousce(driver)

    finally:
        driver.close()
        driver.quit()
```

### 下载小鹅通收费视频

[参考](https://github.com/lfdotleo/edownload)

1. 安装wget：brew install wget

2. 安装php：brew install php

3. 获取视频参数

   1. 在 Filter 栏中输入 ts 可以看到多个包含 ts 的链接，选择任一链接复制，该链接为 ts_url
   2. 点击该链接在右侧框中的 Headers - Request Headers 中找到 referer 字段，复制该值为 referer 。（其他值会随着课程变化而变化，该值每次不用重新获取）
   3. 在 Filter 栏中输入 m3u8 可以看到包含 m3u8 的链接，该链接为 m3u8_url

4. 下载key文件：在 Filter 栏中输入 key 可以看到包含 key 的链接，wget 下载该文件，改名为test.key

5. 下载视频test.ts：`./edownload.sh <referer> <m3u8_url> <ts_url> <filename>`

   * 例：`./edownload.sh https://appf5z0prau5564.h5.xiaoeknow.com/ https://appf5z0prau5564.h5.xiaoeknow.com/video_encrypt/index\?m3u8\=axHiRa0oceH_Mv6iLdye9ol_bemnNcyreyXpBt0_LwWhsitrdlmy9_kiLsn_hal_dlCi5a0nZgWzNaoiLzk3NjRhN2E1dm9kdHJhbnNnenAxMjUyNTI0MTI2L2FmYzc5YTEyNTI4NTg5MDgxNjU0NjUwMTc0OS9kcm0vdm9kZHJtLnRva2VuLk5URXhaV1U1TnpZM05qQmhZemxoTnl0aVNsaEtiSEZpVGxSTGNqVmlXbU01U25WRWQxcGtZbGxOZVdFNFMwYzVlRTlpZGxJeVRtbFhlbkoxUVU1R1J3LnYuZjQyMTIyMC5tM3U4P3Q9NjE5NGI1MjcmZXhwZXI9MCZ1cz1BQzZkU2Z1b2FHblImc2lnbj1kNjY0NjA5YmY1M2NhNWZjYjYwMTYxOWUyZGM3N2U3MAO0O0OO0O0O https://encrypt-k-vod.xet.tech/9764a7a5vodtransgzp1252524126/afc79a125285890816546501749/drm/v.f421220.ts\?start\=0\&end\=312655\&type\=mpegts\&exper\=0\&sign\=71d42e1cca101029d16ad7510cf2df1d\&t\=6194cd76\&us\=o43ea9xZEWWh test`

     















