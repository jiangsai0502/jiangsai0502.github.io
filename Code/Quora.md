###### Quora爬虫源码

[返回](FootPrint/Playwright.md#爬CCP文章)

```python
import os, html2text, re, random
from playwright.sync_api import Playwright, sync_playwright
from Module import Play_Wright_modules as pwm

#########################全局变量#########################
# MarkDown文件目录
MDdir = "/Users/jiangsai/Desktop"
# 问题
Xpath_Answer = '//div[@class="q-text puppeteer_test_question_title"]'
# 答案块中的每个答案的作者
Xpath_Author = '//div[@class="q-inlineFlex qu-alignItems--center qu-wordBreak--break-word"]'
# 答案块中的每个答案的内容
Xpath_Question = '//div[@class="q-box spacing_log_answer_content puppeteer_test_answer_content"]'
#########################全局变量#########################


# 获取页面信息
def GetInfo(WritePage):
    # 获取问题信息
    Answer = WritePage.query_selector(Xpath_Answer).text_content()
    with open(MDFileDir, mode="a", encoding="utf-8") as f:
        f.write("### " + Answer + "\n" + "----" + "\n")
    GetAnswersInfo(WritePage)


# 获取答案信息
def GetAnswersInfo(WritePage):
    # 判断当前节点下是否有子节点，没有则略过
    if len(WritePage.query_selector_all("xpath=/*")) != 0:
        Son_Elements = WritePage.query_selector_all("xpath=/*")
        for Son_E in Son_Elements:
            Author_Num = len(Son_E.query_selector_all(Xpath_Author))
            Question_Num = len(Son_E.query_selector_all(Xpath_Question))
            if Author_Num > 0 and Question_Num > 0:
                if Author_Num == 1 and Question_Num == 1:
                    # 滚动到当前元素位置
                    Son_E.evaluate("element => element.scrollIntoView()")
                    Author = Son_E.query_selector(Xpath_Author).text_content()
                    # 因答案内容可能包含图片，故此处使用HTML2Text提取富文本
                    QuestionHtml = Son_E.query_selector(Xpath_Question).inner_html()
                    Question = MarkDownMaker.handle(QuestionHtml)
                    # 图片链接有些被莫名增加了换行，句子中间也莫名增加了换行
                    Question = Question.replace("-\n", "-").replace("\n", " ").replace("  ", "\n\n")
                    with open(MDFileDir, mode="a", encoding="utf-8") as f:
                        f.write("##### " + Author + "\n" + Question + "----" + "\n")
                elif Son_E.query_selector_all("xpath=/*") is not None:
                    GetAnswersInfo(Son_E)


def Page_Scroll(ScrollPage, ScrollTimes):
    pwm.Page_Scroll(ScrollPage, ScrollTimes)
    # 点开每一个答案的「(more)」或「Continue Reading」来查看更多
    MoreClicks = ScrollPage.query_selector_all('text="(more)"')
    ContinueReading = ScrollPage.query_selector_all('text="Continue Reading"')
    for eliment in MoreClicks:
        eliment.click()
        ScrollPage.wait_for_timeout(random.randint(1000, 3000))
    for eliment in ContinueReading:
        eliment.click()
        ScrollPage.wait_for_timeout(random.randint(1000, 3000))
    return ScrollPage


def run(playwright: Playwright) -> None:
    global MarkDownMaker, MDFileDir  # 文件名称（含路径）
    WebSites = [
        "https://www.quora.com/How-advanced-is-high-speed-rail-in-China",
        "https://www.quora.com/How-successful-has-Chinas-high-speed-railway-system-been",
    ]
    SaiBrowser, SaiContext, SaiPages = pwm.Initial_Chrome(
        playwright, WebSites, AbortPic=False, WaitLoad=False
    )
    for SaiPage in SaiPages:
        MarkDownMaker, MDFileDir = pwm.Initial_EachWeb_MDFile(SaiPage)
        SaiPage.bring_to_front()
        # 滚动指定次数
        Page_Scroll(SaiPage, 1)
        # 获取页面信息
        GetInfo(SaiPage)
        # 收尾
        SaiPage.close()
    SaiContext.close()
    SaiBrowser.close()


with sync_playwright() as playwright:
    run(playwright)
```

