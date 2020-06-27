# Selenium + Chrome Headless

#### 1. 安装环境

1. 切换到 `py3` 虚拟环境：`source activate py3`

2. 查看当前环境是否已包含 `Scrapy` 模块：`conda list`

3. 安装 `selenium` 模块：`pip install selenium`

4. 下载 [chromedriver驱动器](https://sites.google.com/a/chromium.org/chromedriver/home)，因为Chrome 版本是 79.0.3945.130，因此ChromeDriver版本选 79.0.3945.36

5. 将` chromedriver驱动器` 移动到虚拟环境中 `/opt/anaconda3/envs/py3/bin/`

   1. 先确定虚拟环境位置：`which python`得知`/opt/anaconda3/envs/py3/bin/python/`

6. 将` chromedriver驱动器`加入环境变量

   `open ~/.bash_profile`

   最后插入一行：`export PATH=$PATH:/opt/anaconda3/envs/py3/bin/chromedriver`

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
import os, requests, time

# 基本用法
def BasicUsage(driver):
    driver.get('https://www.baidu.com/')
    # find_element 获取WebElement对象
    # send_keys() 向WebElement对象输入内容
    driver.find_element_by_xpath('//*[@id="kw"]').send_keys('sai的小站')
    # click() 点击WebElement对象
    driver.find_element_by_xpath('//*[@id="su"]').click()
    # text 获取WebElement对象的文本内容
    temp = driver.find_element_by_xpath('//*[@id="1"]/h3/a').text
    print(temp)
    # get_attribute() 获取WebElement对象的某个属性的值，括号内是属性名
    temp = driver.find_element_by_xpath('//*[@id="1"]').get_attribute('srcid')
    print(temp)
    # get_attribute('outerHTML') 获取WebElement对象的某个属性的全部Html
    temp = driver.find_element_by_xpath('//*[@id="1"]').get_attribute('outerHTML')
    print(temp)

# 创建新标签
def CreateTab(driver):
    # js新建标签
    driver.execute_script('window.open();')
    # 获取当前浏览器所有标签的句柄
    handles = driver.window_handles
    # 获取当前标签的句柄
    main_handle = driver.current_window_handle
    # 切换标签
    driver.switch_to.window(handles[1])
    # 新标签打开网页
    driver.get('https://www.sogou.com/')

# 页面含frame时的操作
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
    # alert
    driver.find_element_by_xpath('/html/body/button[1]').click()
    # 打印alert提示信息
    print(driver.switch_to.alert.text)
    # 点击alert的OK按钮
    driver.switch_to.alert.accept()
    # confirm
    driver.find_element_by_xpath('/html/body/button[2]').click()
    # 打印confirm提示信息
    print(driver.switch_to.alert.text)
    # 点击confirm的OK按钮
    # driver.switch_to.alert.accept()
    # 点击confirm的Cancel按钮
    driver.switch_to.alert.dismiss()
    # prompt
    driver.find_element_by_xpath('/html/body/button[3]').click()
    # 打印prompt提示信息
    print(driver.switch_to.alert.text)
    # 向prompt输入信息
    driver.switch_to.alert.send_keys('你猜猜我想说什么')
    # 点击prompt的OK按钮
    # driver.switch_to.alert.accept()
    # 点击prompt的Cancel按钮
    driver.switch_to.alert.dismiss()

# 更多鼠标键盘操作
def MoreActions(driver):
    driver.get('https://www.mi.com/')
    # 鼠标悬停
    ac = ActionChains(driver)
    ac.move_to_element(driver.find_element_by_xpath('//*[@id="app"]/div[1]/div/div[3]/div[1]/div[2]/ul/li[2]/a/span')).perform()
    driver.find_element_by_xpath('//*[@id="J_navMenu"]/div/ul/li[2]/a/div[2]').click()
    # 点击链接打开新标签，切换到新标签句柄
    driver.switch_to.window(driver.window_handles[1])
    print(driver.find_element_by_xpath('//*[@id="app"]/div[3]/div/div/div/div[2]/div[2]/div[3]/div/span[2]').text)

if __name__ == '__main__':
    try:
        # 创建浏览器
        path = "/Users/sai/miniconda3/envs/py3_428/bin/chromedriver"
        options = Options()
        # True为无头浏览器
        # options.headless = True  
        # 托管当前打开的浏览器，先命令行打开浏览器（见参考2）
        options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        driver = webdriver.Chrome(executable_path=path, options=options)
        # 每隔0.5秒检查一次元素是否加载完成，最多等10秒
        driver.implicitly_wait(10)

        # BasicUsage(driver)
        # CreateTab(driver)
        # FrameSwith(driver)
        # CheckedWidgets(driver)
        # MoreActions(driver)
        Popup(driver)
    finally:
        # 关闭当前标签
        driver.close()
        # 关闭当前浏览器
        driver.quit()
```

1. [Python下selenium 打开新的窗口和切换到其他窗口](https://www.jianshu.com/p/affcccdf5ea2)

2. [mac selenium 连接已经打开的chrome浏览器](https://blog.csdn.net/w5688414/article/details/106032555/)

   ```bash
   1. 向~/.zshrc添加环境变量
     open ~/.zshrc
     export PATH="/Applications/Google Chrome.app/Contents/MacOS:$PATH"
     source ~/.zshrc
   2. 打开chrome
   	–remote-debugging-port=9222：指定启动端口9222
   	–user-data-dir="/ChromeProfile"：指定浏览器数据存储目录
   	Google\ Chrome --remote-debugging-port=9222 --user-data-dir="~/ChromeProfile"
   3. 程序增加1行
   	options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
   ```

3. 对于鼠标悬停出现，鼠标移开消失的元素，可以冻住页面

   1. Console中执行`setTimeout(function(){ debugger }, 2000);`，即可冻住页面2秒

      <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200627232839.png" style="zoom:30%;" />



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

#### 3.案例

1. 模拟登录访问Hipda

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

2. 载入 `cookie` 访问Hipda

   > 优势：绕过模拟登陆时可能出现的验证码

   ```
   
   ```

   















