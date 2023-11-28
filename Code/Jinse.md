###### 金色财经 

[返回](FootPrint/Playwright.md#金色财经)

```python
import os, html2text, re, random, requests, time
from playwright.sync_api import Playwright, sync_playwright
from Module import Play_Wright_modules as pwm

# 已获取最新新闻的时间戳
Latest_time = ""
# MarkDown文件目录
MDdir = "/Users/jiangsai/Desktop"
# MarkDown文件名
MDFile = "Test.md"
# MarkDown引用的图片目录
MD_Pic_dir = "/Users/jiangsai/Desktop/Pic"
# 内容块list
Xpath_Blocks = '//div[contains(@class,"js-lives__box")]/div'
# 内容块的时间
Xpath_Time = '//div[contains(@class,"time")]'
# 内容块的标题
Xpath_Title = '//div[contains(@class,"content")]/a[1]'
# 内容块的内容
Xpath_Content = '//div[contains(@class,"content")]/a[2]'
# 内容块的图片
Xpath_Pics = '//div[@class="js-lives__photo"]//*[@*[name()="src"]]'


# 下载图片并替换图片引用路径
def DownLoad_Pic_Get_New_MDContent(WritePage, urls):
    Local_urls = []
    if len(urls) != 0:
        for image_url in urls:
            # 提取图片名称
            # 格式：https://fe.t.sis.cn/ap.png/ddkkk 提取出ap.png
            match = re.search(r"/([^/]+\.(?:png|jpg|jpeg|webp))(?:/|$)", image_url)
            if match:
                PicName = match.group(1)
                # 拼接已下载的本地图片的完整路径
                ThisPicDir = f"{MD_Pic_dir}/{PicName}"
                # 利用requests下载图片
                Requests_DownLoad_Pic(WritePage, image_url, ThisPicDir)
                ThisPicDir_MD = f"![]({ThisPicDir})"
                Local_urls.append(ThisPicDir_MD)
            else:
                print(f"图片格式需要扩充: {image_url}")
    return ThisPicDir_MD


# 利用requests下载图片
def Requests_DownLoad_Pic(SaiPage, image_url, ThisPicDir):
    # 创建一个Session会话
    session = requests.Session()
    # 获取页面的Cookies
    cookies = SaiPage.context.cookies()
    # 将Cookies添加到Session会话中
    for cookie in cookies:
        session.cookies.set(cookie["name"], cookie["value"], domain=cookie["domain"])
    # 使用Session会话来下载图像
    response = session.get(image_url)
    # 检查响应状态码
    if response.status_code == 200:
        # 将图像保存到文件
        with open(ThisPicDir, "wb") as fp:
            fp.write(response.content)
    else:
        print("下载失败")


# 获取信息
def ExtractInfo(WritePage):
    # 获取所有答案块
    # Blocks = WritePage.query_selector_all(Xpath_Blocks)
    # for block in Blocks:

    # 已获取最新新闻的时间戳
    global Latest_time
    # query_selector只取列表第1条，因为第1条最新
    block = WritePage.query_selector(Xpath_Blocks)
    # 滚动到当前元素位置
    block.evaluate("element => element.scrollIntoView()")
    # 当前第一条内容的时间；strip()删除开头、结尾的所有换行和空格
    this_block_time = block.query_selector(Xpath_Time).text_content().strip()

    if Latest_time != this_block_time:
        Latest_time = this_block_time
        # 标题
        Title = block.query_selector(Xpath_Title).text_content().strip()
        # 内容
        Content = block.query_selector(Xpath_Content).text_content().strip()
        # 替换多个换行为单个换行
        Content = re.sub(r"\n+", "\n", Content)
        # 替换多个空格为单个空格
        Content = re.sub(r" +", " ", Content)

        Pics_MD = ""
        if len(block.query_selector_all(Xpath_Pics)) != 0:
            Pics = []
            for i in block.query_selector_all(Xpath_Pics):
                Pic = block.query_selector(Xpath_Pics).get_attribute("src")
                Pics.append(Pic)
            Pics_MD = DownLoad_Pic_Get_New_MDContent(WritePage, Pics)
        with open(MDFileDir, mode="a", encoding="utf-8") as f:
            f.write("> " + Latest_time + "\n\n" + "#### " + Title + "\n\n")
            f.write(Content + "\n\n" + Pics_MD + "\n\n" + "----" + "\n")
    WritePage.wait_for_timeout(random.randint(1000, 3000))


def run(playwright: Playwright) -> None:
    global MarkDownMaker, MDFileDir
    WebSites = [
        "https://www.jinse.cn/lives",
    ]
    SaiBrowser, SaiContext, SaiPages = pwm.Initial_Chrome(playwright, WebSites, AbortPic=True, WaitLoad=True)
    MarkDownMaker, MDFileDir = pwm.Initial_Single_MDFile(MDdir, MDFile)
    # 币圈图片可能境内无法访问，故需要下载
    if not os.path.exists(MD_Pic_dir):
        os.mkdir(MD_Pic_dir)
    while True:
        ExtractInfo(SaiPages[0])
    SaiPage.close()
    # 收尾
    SaiContext.close()
    SaiBrowser.close()


with sync_playwright() as playwright:
    run(playwright)
```

