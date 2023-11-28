###### 【滚动加载】爬取一级页信息   [返回](FootPrint/Playwright.md#场景一：【滚动加载】爬取一级页信息)

```js
import os, html2text, re, random
from playwright.sync_api import Playwright, sync_playwright
from Module import Play_Wright_modules as pwm

#########################全局变量#########################
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
#########################全局变量#########################


# 获取问答页信息
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


# 获取专栏页信息
def GetZhuanLanInfo(WritePage):
    # 因答案内容可能包含图片，故此处使用HTML2Text提取富文本
    Article_Title_Html = WritePage.query_selector(Xpath_Article_Title).inner_html()
    Article_Title = MarkDownMaker.handle(Article_Title_Html)
    Article_Content_Html = WritePage.query_selector(Xpath_Article_Content).inner_html()
    Article_Content = MarkDownMaker.handle(Article_Content_Html)
    with open(MDFileDir, mode="a", encoding="utf-8") as f:
        f.write("### " + Article_Title + "\n" + Article_Content + "\n\n" + "----" + "\n")


def run(playwright: Playwright) -> None:
    global MarkDownMaker, MDFileDir  # 文件名称（含路径）
    WebSites = [
        "https://www.zhihu.com/question/21931620",
        "https://www.zhihu.com/question/485142113",
    ]
    SaiBrowser, SaiContext, SaiPages = pwm.Initial_Chrome(
        playwright, WebSites, AbortPic=False, WaitLoad=False
    )
    for SaiPage in SaiPages:
        MarkDownMaker, MDFileDir = pwm.Initial_EachWeb_MDFile(SaiPage)
        SaiPage.bring_to_front()
        # 专栏页面
        if "zhuanlan" in SaiPage.url:
            GetZhuanLanInfo(SaiPage)
        # 问答页面
        elif "question" in SaiPage.url:
            # 滚动搜索页获取更多数据
            pwm.Page_Scroll(SaiPage, 1)
            GetQAInfo(SaiPage)
        # 收尾
        SaiPage.close()
    SaiContext.close()
    SaiBrowser.close()


with sync_playwright() as playwright:
    run(playwright)
```