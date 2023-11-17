###### 场景三：【翻页】提取一级页&二级页信息

###### [返回](FootPrint/Playwright.md#场景三：【翻页】提取一级页二级页信息)

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
Xpath_Nav = '//ul[@class="be-pager"]'
# 一级页FatherPage的信息块list
Xpath_FP_Block_List = '//ul[@class="clearfix cube-list"]/*'
# 一级页FatherPage每个信息块的标题
Xpath_FP_Block_Title = '//a[@class="title"]'
# 一级页FatherPage每个信息块的时长
Xpath_FP_Block_Length = '//span[@class="length"]'
# 一级页FatherPage每个信息块的播放次数
Xpath_FP_Block_PlayNum = '//span[@class="play"]'
# 二级页SonPage的发布时间
Xpath_SP_Publish_Date = '//span[@class="pubdate-text"]'
# 二级页SonPage的点赞数
Xpath_Thumb = '//span[contains(@class,"video-like-info")]'
#########################全局变量#########################


# 获取一级页FatherPage信息（直接定位到目标信息）
def GetFatherPageInfo(block):
    Title = block.query_selector(Xpath_FP_Block_Title).text_content()
    Length = block.query_selector(Xpath_FP_Block_Length).text_content()
    PlayNum = block.query_selector(Xpath_FP_Block_PlayNum).text_content()
    with open(MDFileDir, mode="a", encoding="utf-8") as f:
        f.write("片名：" + Title + "\n" + "时长：" + Length + "\n" + "播放数：" + PlayNum + "\n")


# 获取二级页SonPage信息
def GetSonPageInfo(SaiContext, block):
    # 在新标签加载二级页
    with SaiContext.expect_page() as SonPageInfo:
        block.click()
    SonPage = SonPageInfo.value
    SonPage.bring_to_front()
    SonPage.wait_for_load_state()

    # 抓取二级页信息
    Publish_Date = SonPage.query_selector(Xpath_SP_Publish_Date).text_content()
    Thumb = SonPage.query_selector(Xpath_Thumb).text_content()
    Publish_Date = Publish_Date.strip()
    with open(MDFileDir, mode="a", encoding="utf-8") as f:
        f.write("发布时间：" + Publish_Date + "\n" + "点赞数：" + Thumb + "\n\n" + "----" + "\n")
    SonPage.close()


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
        Blocks = FatherPage.query_selector_all(Xpath_FP_Block_List)
        for block in Blocks:
            # 获取每个一级页信息块的具体信息
            GetFatherPageInfo(block)
            # 获取每个一级页信息块的二级页的具体信息
            GetSonPageInfo(SaiContext, block)
            FatherPage.wait_for_timeout(random.randint(1000, 3000))
        if Nav["Finish_Nav"] == True:
            break


def run(playwright: Playwright) -> None:
    global MarkDownMaker, MDFileDir
    WebSites = [
        "https://space.bilibili.com/111082383/video",
    ]
    SaiBrowser, SaiContext, SaiPages = pwm.Initial_Chrome(playwright, WebSites, AbortPic=True, WaitLoad=True)
    MarkDownMaker, MDFileDir = pwm.Initial_Single_MDFile(MDdir, MDFile)
    for SaiPage in SaiPages:
        # 获取目标信息
        GetInfo(SaiContext, SaiPage)
        SaiPage.close()
    # 收尾
    SaiContext.close()
    SaiBrowser.close()


with sync_playwright() as playwright:
    run(playwright)
```

方法2：**逐个遍历整个HTML文件，直到找到目标信息**

```python
def ExtractFPInfo(SaiContext, FatherElement):
 Infor_Elements = FatherElement.query_selector_all("xpath=/*")
 # 逐个进入子节点
 for Infor_E in Infor_Elements:
     # 页面不展示的内容就不爬了
     if Infor_E.get_attribute("style") == "display: none;":
         continue
     else:
         Title_Num = len(Infor_E.query_selector_all(Xpath_FP_Et_Title))
         if Title_Num > 0:
             if Title_Num == 1:
                 Title = Infor_E.query_selector(Xpath_FP_Et_Title).text_content()
                 Length = Infor_E.query_selector(Xpath_FP_Et_Length).text_content()
                 PlayNum = Infor_E.query_selector(Xpath_FP_Et_PlayNum).text_content()
                 with open("test.md", mode="a", encoding="utf-8") as f:
                     f.write("片名：" + Title + "\n" + "时长：" + Length + "\n" + "播放数：" + PlayNum + "\n")
                 # 打开二级页，二级页在新标签加载
                 with SaiContext.expect_page() as SonPageInfo:
                     Infor_E.query_selector(Xpath_FP_Et_Title).click()
                 SonPage = SonPageInfo.value
                 SonPage.wait_for_load_state()
                 SonPage.bring_to_front()
                 ExtractSPInfo(SonPage)
                 SonPage.close()
             else:
                 if Infor_E.query_selector_all("xpath=/*") is not None:
                     ExtractFPInfo(SaiContext, Infor_E)
```

