##### 异步

```python
import random, os, html2text, re, asyncio
from playwright.async_api import Playwright, async_playwright


#########################全局变量#########################
# 待爬的第一个页面
WebSite = "http://dangjian.people.com.cn/GB/394443/index.html"
# 底部导航Xpath
Xpath_Nav = '//div[@class="page"]'
# 一级页FatherPage标题list
Xpath_FP_Title_List = '//div[@class="fl"]/ul/li'
# 一级页FatherPage每个标题
Xpath_FP_Title = "//a"
# 二级页正文
Xpath_SP_Article = '//div[@class="text_c"]'
# 翻页导航全部数字
All_Nav = set()
# 翻页导航点击过的数字
Clicked_Nav = set()
# 翻页导航可点击数字
Able_Click_Nav = []
# 是否第1个导航
Is_First_Nav = True
# 是否已点击完所有导航
Finish_Nav = False
#########################全局变量#########################


# 初始化浏览器：调用本地Chrome，在新标签打开目标网页，并切换到该标签
async def InitialChrome(playwright, WebSite):
    SaiBrowser = await playwright.chromium.connect_over_cdp("http://localhost:9222")
    SaiContext = SaiBrowser.contexts[0]
    SaiContext.route(
        re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.gif.*)|(.*\.webp.*)"), lambda route: route.abort()
    )
    SaiPage = await SaiContext.new_page()
    await SaiPage.goto(WebSite)
    await SaiPage.bring_to_front()
    await SaiPage.wait_for_load_state("networkidle")
    return SaiBrowser, SaiContext, SaiPage


# 初始化写入方法：切换到目标路径，指定文件名
async def InitialMDFile(MDdir, MDFile):
    # 切换MarkDown文件目录
    os.chdir(MDdir)
    # 声明全局MarkDown文件操作类
    global MarkDownMaker
    MarkDownMaker = html2text.HTML2Text()
    MarkDownMaker.ignore_links = True
    # 声明全局MarkDown文件路径
    global MDFileDir
    MDFileDir = f"{MDdir}/{MDFile}"


# 翻页
async def TurnPage(FatherPage):
    global All_Nav
    global Clicked_Nav
    global Able_Click_Nav
    global Is_First_Nav
    global Finish_Nav
    # 当前页导航列表
    Current_Nav_list = await FatherPage.query_selector_all(Xpath_Nav + "/*")
    for i in Current_Nav_list:
        Nav_num = await i.text_content()
        # 抽取出导航列表中的数字，「上一页」「下一页」这种非确定性导航都排除
        if str(Nav_num).isdigit():
            All_Nav.add(int(Nav_num))
    # 若本页是第1页，则不用点击
    if Is_First_Nav == True:
        # 取所有导航数列表中最小的数为即将点击的数
        To_Click_Nav = sorted(list(All_Nav))[0]
        pass
    else:
        # 取可点击列表的最小导航数为即将点击的数
        To_Click_Nav = Able_Click_Nav[0]
        # 点击最小导航数
        # locator('text=1')模糊匹配1,01,10,11等;locator('text="1"')精确匹配1
        await FatherPage.locator(Xpath_Nav).locator('text="' + str(To_Click_Nav) + '"').click()
        await FatherPage.wait_for_timeout(random.randint(1000, 3000))
    # 刚点击的数字追加到「已点击导航数字集合」
    Clicked_Nav.add(To_Click_Nav)
    Is_First_Nav = False
    # 可点击导航数字集合 = 所有导航数字集合 ∩ 已点击导航数字集合，再转换成列表
    Able_Click_Nav = sorted(list(All_Nav.difference(Clicked_Nav)))
    if len(Able_Click_Nav) == 0:
        Finish_Nav = True


# 获取信息
async def GetInfo(SaiContext, FatherPage):
    global Finish_Nav
    # 持续取本页的数据，直到导航到最后一页
    while True:
        await TurnPage(FatherPage)
        # 列出每个一级页信息块
        Son_Page_Titles = await FatherPage.query_selector_all(Xpath_FP_Title_List)
        for SP_Title in Son_Page_Titles:
            # 获取每个一级页信息块的二级页的具体信息
            await GetSonPageInfo(SaiContext, SP_Title)
            await FatherPage.wait_for_timeout(random.randint(1000, 3000))
        if Finish_Nav == True:
            break


# 获取二级页SonPage信息
async def GetSonPageInfo(SaiContext, SP_Title):
    # 在新标签加载二级页
    async with SaiContext.expect_page() as SonPageInfo:
        await SP_Title.click()
    SonPage = await SonPageInfo.value
    await SonPage.wait_for_load_state()
    await SonPage.bring_to_front()
    # 抓取二级页信息
    ArticleElement = await SonPage.query_selector(Xpath_SP_Article)
    ArticleHtml = await ArticleElement.inner_html()
    Article = MarkDownMaker.handle(ArticleHtml)
    with open(MDFileDir, mode="a", encoding="utf-8") as f:
        f.write(Article + "\n\n" + "----" + "\n")
    await SonPage.close()


async def run(playwright: Playwright) -> None:
    SaiBrowser, SaiContext, SaiPage = await InitialChrome(playwright, WebSite)
    # MarkDown文件目录
    MDdir = "/Users/jiangsai/Desktop"
    # MarkDown文件名
    MDFile = "Test.md"
    # 初始化MarkDown操作方法
    await InitialMDFile(MDdir, MDFile)
    # 获取目标信息
    await GetInfo(SaiContext, SaiPage)

    # 收尾
    await SaiPage.close()
    await SaiContext.close()
    await SaiBrowser.close()


async def main():
    async with async_playwright() as playwright:
        await run(playwright)


# vscode中运行时使用asyncio.run
asyncio.run(main())
# Jupyter中运行时使用await
# await main()
```

