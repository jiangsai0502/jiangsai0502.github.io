# Selenium + Chrome Headless

#### 1. 安装环境

1. 切换到 `py3` 虚拟环境：`source activate py3`

2. 查看当前环境是否已包含 `Scrapy` 模块：`conda list`

3. 安装 `selenium` 模块：`pip install selenium`

4. 下载 [chromedriver驱动器](https://sites.google.com/a/chromium.org/chromedriver/home)，因为Chrome 版本是 79.0.3945.130，因此ChromeDriver版本选 79.0.3945.36

5. 将` chromedriver驱动器` 移动到虚拟环境中 `/opt/anaconda3/envs/py3/bin/`

6. 将` chromedriver驱动器`加入环境变量

   `open ~/.bash_profile`

   最后插入一行：`export PATH=$PATH:/opt/anaconda3/envs/py3/bin/chromedriver`

#### 2. 下载学习强国视频

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
> * 元素定位 `find_element_by……` 和 `find_elements_by……` 
>
>   * `find_element_by_id("id_vaule")`，`find_element_by_name("name_vaule")`
>     `find_element_by_tag_name("tag_name_vaule")`，`find_element_by_class_name("class_name")`
>     `find_element_by_xpath("xpath")`，`find_element_by_link_text("text_vaule")`
>     `find_element_by_css_selector()`
>   * `find_elements_by……` 用法同理
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

   















