###### 微博 爬虫源码

[返回](FootPrint/Playwright.md#微博)

```python
import os, html2text, re, random, requests
from playwright.sync_api import Playwright, sync_playwright
from Module import Play_Wright_modules as pwm

#########################全局变量#########################
# MarkDown文件目录
MDdir = "/Users/jiangsai/Desktop"
# MarkDown文件名
MDFile = "Test.md"
# MarkDown引用的图片目录
MD_Pic_dir = "/Users/jiangsai/Desktop/Pic"
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
                Block.evaluate("element => element.scrollIntoView()")
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
    # 作者（字符串）
    name = element.query_selector(Xpath_name).text_content()
    CurrentElementData["name"] = name

    # 具体内容（因内容可能包含图片，故用HTML2Text提取MarkDown富文本）
    content_Html = element.query_selector(Xpath_content).inner_html()
    #        提取的原始内容的图片都是在线的
    content_Online_Pic = MarkDownMaker.handle(content_Html)
    #        但微博禁止站外部引用他的图片，故先将在线图片下载到本地再引用
    content_Local_Pic = DownLoad_Pic_Get_New_MDContent(SaiPage, content_Online_Pic)
    CurrentElementData["content"] = content_Local_Pic

    # 回复部分
    CurrentElementData["reply"] = ""
    #        若本内容没有回复则忽略
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
    global MarkDownMaker, MDFileDir
    WebSites = [
        "https://weibo.com/u/2959386434",
    ]
    SaiBrowser, SaiContext, SaiPages = pwm.Initial_Chrome(playwright, WebSites, AbortPic=False, WaitLoad=True)
    MarkDownMaker, MDFileDir = pwm.Initial_Single_MDFile(MDdir, MDFile)
    if not os.path.exists(MD_Pic_dir):
        os.mkdir(MD_Pic_dir)
    for SaiPage in SaiPages:
        # 获取目标信息
        GetInfo_WeiBo(SaiPage, 10)
        SaiPage.close()
    # 收尾
    SaiContext.close()
    SaiBrowser.close()


with sync_playwright() as playwright:
    run(playwright)
```

