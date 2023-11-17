###### 爬CCP文章

[返回](FootPrint/Playwright.md#爬CCP文章)

```python
import random, os, html2text, re
from playwright.sync_api import Playwright, sync_playwright
from Module import Play_Wright_modules as pwm

#########################全局变量#########################
# MarkDown文件目录
MDdir = "/Users/jiangsai/Desktop"
# MarkDown文件名
MDFile = "Test.md"
# 底部导航Xpath
Xpath_Nav = '//div[@class="page"]'
# 一级页FatherPage标题list
Xpath_FP_Title_List = '//div[@class="fl"]/ul/li'
# 一级页FatherPage每个标题
Xpath_FP_Title = "//a"
# 二级页正文
Xpath_SP_Article = '//div[@class="text_c"]'
#########################全局变量#########################


# 获取信息
def GetInfo(SaiContext, FatherPage):
    # 导航
    Nav = {
        "All_Nav": set(),
        "Clicked_Nav": set(),
        "Able_Click_Nav": [],
        "Is_First_Nav": True,
        "Finish_Nav": False,
    }
    # 持续取本页的数据，直到导航到最后一页
    while True:
        pwm.Turn_Page(FatherPage, Xpath_Nav, Nav)
        # 列出每个一级页信息块
        Son_Page_Titles = FatherPage.query_selector_all(Xpath_FP_Title_List)
        for SP_Title in Son_Page_Titles:
            # 获取每个一级页信息块的二级页的具体信息
            GetSonPageInfo(SaiContext, SP_Title)
            FatherPage.wait_for_timeout(random.randint(1000, 3000))
        if Nav["Finish_Nav"] == True:
            break


# 获取二级页SonPage信息
def GetSonPageInfo(SaiContext, SP_Title):
    # 在新标签加载二级页
    with SaiContext.expect_page() as SonPageInfo:
        SP_Title.click()
    SonPage = SonPageInfo.value
    SonPage.wait_for_load_state()
    SonPage.bring_to_front()
    # 抓取二级页信息
    ArticleHtml = SonPage.query_selector(Xpath_SP_Article).inner_html()
    Article = MarkDownMaker.handle(ArticleHtml)
    with open(MDFileDir, mode="a", encoding="utf-8") as f:
        f.write(Article + "\n\n" + "----" + "\n")
    SonPage.close()


def run(playwright: Playwright) -> None:
    global MarkDownMaker, MDFileDir
    WebSites = [
        "http://dangjian.people.com.cn/GB/394443/index.html",
    ]
    SaiBrowser, SaiContext, SaiPages = pwm.Initial_Chrome(playwright, WebSites, AbortPic=True, WaitLoad=True)
    MarkDownMaker, MDFileDir = pwm.Initial_Single_MDFile(MDdir, MDFile)
    # 获取目标信息
    for SaiPage in SaiPages:
        GetInfo(SaiContext, SaiPage)
        SaiPage.close()
    # 收尾
    SaiContext.close()
    SaiBrowser.close()


with sync_playwright() as playwright:
    run(playwright)
```

