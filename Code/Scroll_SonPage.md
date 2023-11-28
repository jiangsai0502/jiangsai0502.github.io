###### 场景二：滚动加载 + 爬取二级页信息   [返回](FootPrint/Playwright.md#场景二：【滚动加载】爬取二级页信息)

```py
import os, html2text, re, random
from playwright.sync_api import Playwright, sync_playwright
from Module import Play_Wright_modules as pwm

#########################全局变量#########################
# MarkDown文件目录
MDdir = "/Users/jiangsai/Desktop"
# MarkDown文件名
MDFile = "Test.md"
# 搜索结果页每个结果标题的url
Xpath_Search_Result_urls = '//h2[@class="ContentItem-title"]//div/a'
###########类型一：问答型###########
# 二级页「查看全部回答」（从搜索页点击进入问答页，哪怕只有1个答案，也会展示这个按钮）
Xpath_Check_All = '//div[@class="Card ViewAll"][1]/a'
# 二级页问题
Xpath_Answer = '//h1[@class="QuestionHeader-title"]'
# 二级页问题描述
Xpath_Answer_Desc = '//div[@class="css-eew49z"]'
# 二级页整个答案块
Xpath_Questions_Block = '//div[@role="list"]/div'
# 二级页答案块中的答案list
Xpath_Questions = '//div[@role="list"]/*[not(@role="listitem")]'
# 二级页答案块中的每个答案的作者
Xpath_Author = '//div[@class="AuthorInfo-head"]'
# 二级页答案块中的每个答案的内容
Xpath_Question = '//span[@class="RichText ztext CopyrightRichText-richText css-117anjg"]'
###########类型二：专题型###########
Xpath_Article_Title = "//article/header/h1"
Xpath_Article_Content = '//article/div[@class="Post-RichTextContainer"]'
#########################全局变量#########################


# 通过搜索结果进入二级页
def FromSearchResultsToSonPage(SaiContext, FatherPage):
    # 获取搜索结果链接
    Result_urls = FatherPage.query_selector_all(Xpath_Search_Result_urls)
    for element in Result_urls:
        if element is not None:
            # 点击每个搜索结果标题，进入二级页
            with SaiContext.expect_page() as SonPageInfo:
                # 滚动到当前元素位置
                element.evaluate("element => element.scrollIntoView()")
                element.click()
            SonPage = SonPageInfo.value
            # 视频和话题页面不抓取
            if any(keyword in SonPage.url for keyword in ["zvideo", "topic"]):
                pass
            else:
                SonPage.bring_to_front()
                SonPage.wait_for_load_state()
                SonPage.wait_for_timeout(random.randint(3000, 5000))
                # 专栏页面
                if "zhuanlan" in SonPage.url:
                    GetZhuanLanInfo(SonPage)
                # 问答页面
                elif "question" in SonPage.url:
                    # 点击「查看全部回答」
                    SonPage.locator(Xpath_Check_All).click()
                    SonPage.wait_for_load_state()
                    # 滚动搜索页获取更多数据
                    pwm.Page_Scroll(SonPage, 1)
                    GetQAInfo(SonPage)
            SonPage.close()


# 获取问答页内容
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


# 获取专栏文章内容
def GetZhuanLanInfo(WritePage):
    # 因答案内容可能包含图片，故此处使用HTML2Text提取富文本
    Article_Title_Html = WritePage.query_selector(Xpath_Article_Title).inner_html()
    Article_Title = MarkDownMaker.handle(Article_Title_Html)
    Article_Content_Html = WritePage.query_selector(Xpath_Article_Content).inner_html()
    Article_Content = MarkDownMaker.handle(Article_Content_Html)
    with open(MDFileDir, mode="a", encoding="utf-8") as f:
        f.write("### " + Article_Title + "\n" + Article_Content + "\n\n" + "----" + "\n")


def run(playwright: Playwright) -> None:
    global MarkDownMaker, MDFileDir
    WebSites = [
        "https://www.zhihu.com/search?q=%E8%88%AC%E8%8B%A5%E6%B3%A2%E7%BD%97%E8%9C%9C",
    ]
    SaiBrowser, SaiContext, SaiPages = pwm.Initial_Chrome(playwright, WebSites, AbortPic=True, WaitLoad=True)
    MarkDownMaker, MDFileDir = pwm.Initial_Single_MDFile(MDdir, MDFile)
    for SaiPage in SaiPages:
        pwm.Page_Scroll(SaiPage, 2)
        # 获取搜索结果的全部内容
        FromSearchResultsToSonPage(SaiContext, SaiPage)
    # 收尾
    SaiContext.close()
    SaiBrowser.close()


with sync_playwright() as playwright:
    run(playwright)
```

上述代码直接模拟点击，还可从搜索结果中抽取出结果的url，逐个打开url来进入二级页

```py
Elements = SaiPage.query_selector_all(Xpath_Search_Results)
for element in Elements:
 # 判断搜索页的每个节点是否有URL，有就提取出链接，通过链接打开
 if element.query_selector(Xpath) is not None:
     elementUrl = element.query_selector(Xpath).get_attribute('content')
     SonPage = SaiContext.new_page()
     SonPage.goto(elementUrl)
```