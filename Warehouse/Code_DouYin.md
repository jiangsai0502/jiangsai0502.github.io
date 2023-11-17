###### 抖音搜索 爬虫源码

[返回](FootPrint/Playwright.md#抖音搜索)

```python
import os, html2text, re, random
from playwright.sync_api import Playwright, sync_playwright
from Module import Play_Wright_modules as pwm
import pandas as pd

#########################全局变量#########################
# CSV文件目录
CSVDir = "/Users/jiangsai/Desktop"
# CSV文件名
CSVFile = "Test.csv"

# 用户搜索
# 搜索结果list
Xpath_List = '//*[@id="search-content-area"]//ul[contains(@class,"fb5dK_Rl WTCKzPrM")]/*'
# 昵称
Xpath_Author = '//p[contains(@class,"bMoJi1wE")]'
# 是否店铺
Xpath_Shop = '//div[contains(@class,"OiNrUQTP GZzMrzN4")]'
# 获赞
Xpath_Thrumb = '//div[contains(@class,"H7Xy0nwI")]/span[3]'
# 粉丝
Xpath_Follower = '//div[contains(@class,"H7Xy0nwI")]/span[5]'
# 简介
Xpath_Intro = '//p[contains(@class,"go5cmngM")]'
#########################全局变量#########################


# 获取抖音搜索信息
def GetSearchResultsInfo(WritePage):
    # 获取所有搜索结果list
    Elements = WritePage.query_selector_all(Xpath_List)
    Author_Infos = []
    for element in Elements:
        # element.evaluate("element => element.scrollIntoView()")
        Author = element.query_selector(Xpath_Author).text_content()
        if element.query_selector(Xpath_Shop) != None:
            Shop = element.query_selector(Xpath_Shop).text_content()
        else:
            Shop = ""
        if element.query_selector(Xpath_Thrumb) != None:
            Thrumb = element.query_selector(Xpath_Thrumb).text_content().replace("获赞", "")
            Thrumb = pwm.convert_wan_to_number(Thrumb)
        else:
            Thrumb = ""
        if element.query_selector(Xpath_Follower) != None:
            Follower = element.query_selector(Xpath_Follower).text_content().replace("粉丝", "")
            Follower = pwm.convert_wan_to_number(Follower)
        else:
            Follower = ""
        if element.query_selector(Xpath_Intro) != None:
            Intro = element.query_selector(Xpath_Intro).text_content()
        else:
            Intro = ""
        Author_Infos.append(
            {"Author": Author, "Shop": Shop, "Thrumb": Thrumb, "Follower": Follower, "Intro": Intro}
        )
    return Author_Infos


def run(playwright: Playwright) -> None:
    global CSVFileDir  # 文件名称（含路径）
    WebSites = [
        "https://www.douyin.com/search/%E5%A4%A7%E6%9D%BF?aid=3a03db05-a799-4870-8e28-1f1e5ea221ee&source=normal_search&type=user",
    ]
    SaiBrowser, SaiContext, SaiPages = pwm.Initial_Chrome(
        playwright, WebSites, AbortPic=False, WaitLoad=False
    )
    for SaiPage in SaiPages:
        CSVFileDir = pwm.Initial_CSVFile(CSVDir, CSVFile)
        SaiPage.bring_to_front()
        pwm.Page_Scroll(SaiPage, 0)
        Author_Infos = GetSearchResultsInfo(SaiPage)
        pwm.Write_to_CSV(Author_Infos, CSVFileDir)
        # 收尾
        SaiPage.close()
    SaiContext.close()
    SaiBrowser.close()


with sync_playwright() as playwright:
    run(playwright)
```

