###### 人人都是产品经理-36氪爬虫源码

[返回](FootPrint/Playwright.md#人人都是产品经理-36氪)

```python
import os, html2text, re, random
from playwright.sync_api import Playwright, sync_playwright
from Module import Play_Wright_modules as pwm

#########################全局变量#########################
# MarkDown文件目录
MDdir = "/Users/jiangsai/Desktop"
# MarkDown文件名
MDFile = "Test.md"
############## woshipm ###########
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
    global MarkDownMaker, MDFileDir
    WebSites = [
        "https://www.woshipm.com/zhichang/5824950.html",
        "https://36kr.com/p/2399884943188356",
    ]
    SaiBrowser, SaiContext, SaiPages = pwm.Initial_Chrome(playwright, WebSites)
    MarkDownMaker, MDFileDir = pwm.Initial_Single_MDFile(MDdir, MDFile)
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

