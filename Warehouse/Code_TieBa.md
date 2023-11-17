###### 贴吧爬虫源码

[返回](FootPrint/Playwright.md#贴吧)

```python
import random, os, html2text, re
from playwright.sync_api import Playwright, sync_playwright


# 页面底部导航
Xpath_Page_Nav = '//div[@class="pb_footer"]//li[contains(@class, "l_pager")]'
# 帖子标题
Xpath_Post_Title = '//*[contains(@class,"core_title_txt")]'
# 当前页的帖子回复楼层list
Xpath_Floors = '//div[contains(@class, "p_postlist")]/*'
# 帖子回复楼层作者
Xpath_Floor_Author = '//ul[@class="p_author"]/li[@class="d_name"]/a'
# 帖子回复楼层时间
Xpath_Floor_Time = '//div[contains(@class,"d_post_content_main")]//span[contains(@class,"tail-info")][last()]'
# 帖子回复楼层内容
Xpath_Floor_Content = '//div[contains(@class,"p_content")]//div[contains(@class,"d_post_content")]'

# 评论换页导航
Xpath_Floor_Nav = '//p[contains(@class,"j_pager")]'
# 当楼层的当前评论页的评论list
Xpath_Floor_Comments = '//li[contains(@class, "lzl_single_post")]'
# 评论作者
Xpath_Comment_Author = '//div[@class="lzl_cnt"]//a[contains(@class,"j_user_card")]'
# 评论内容
Xpath_Comment_Content = '//div[@class="lzl_cnt"]//span[contains(@class,"lzl_content_main")]'


# 初始化浏览器：调用本地Chrome，在新标签打开目标网页，并切换到该标签
def InitialChrome(WebSite):
    SaiBrowser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    SaiContext = SaiBrowser.contexts[0]
    SaiContext.route(
        re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.gif.*)|(.*\.webp.*)"), lambda route: route.abort()
    )
    SaiPage = SaiContext.new_page()
    SaiPage.goto(WebSite)
    SaiPage.bring_to_front()
    SaiPage.wait_for_load_state("networkidle")
    return SaiBrowser, SaiContext, SaiPage


# 初始化写入方法：切换到目标路径，指定文件名
def InitialMDFile():
    # 切换MarkDown文件目录
    MDdir = "/Users/jiangsai/Desktop"
    os.chdir(MDdir)
    # 声明全局MarkDown文件操作类
    global MarkDownMaker
    MarkDownMaker = html2text.HTML2Text()
    MarkDownMaker.ignore_links = True
    MDFile = "Test"
    # 声明全局MarkDown文件路径
    global MDFileDir
    MDFileDir = f"{MDdir}/{MDFile}.md"


# 页面滚动方法：对指定页面，滚动指定次数或滚动到底
def PageScroll(ScrollPage, ScrollTimes):
    ScrollTime = 1
    # 滚动到页面顶部
    ScrollPage.evaluate("() => window.scrollTo(0,0)")
    while ScrollTime < ScrollTimes:
        # 滚动计数
        ScrollTime += 1
        ScrollPage.evaluate("() => window.scrollBy(0,-window.innerHeight)")
        ScrollPage.wait_for_timeout(random.randint(500, 1000))


# 获取问题信息
def ExtractTileInfo(WritePage):
    Title = WritePage.query_selector(Xpath_Post_Title).text_content()
    with open("test.md", mode="a", encoding="utf-8") as f:
        f.write("### " + Title + "\n" + "----" + "\n")
        f.write("----" + "\n\n")


# 获取每一个楼层信息
def ExtractCurrentFloorInfo(CurrentFloor):
    if CurrentFloor.query_selector(Xpath_Floor_Author) != None:
        Floor_Author = CurrentFloor.query_selector(Xpath_Floor_Author).text_content()
        if Floor_Author == "贴吧用户_0DWb97a":
            pass
        Floor_Time = CurrentFloor.query_selector(Xpath_Floor_Time).text_content()
        Floor_Content_Html = CurrentFloor.query_selector(Xpath_Floor_Content).inner_html()
        Floor_Content = MarkDownMaker.handle(Floor_Content_Html)
        with open(MDFileDir, mode="a", encoding="utf-8") as f:
            f.write("作者：" + Floor_Author + "\n" + "时间：" + Floor_Time + "\n" + Floor_Content + "\n")
            f.write("----" + "\n\n")


# 页面翻页
def TurnPage(PageToTurn):
    global Page_All_Nav
    global Page_Clicked_Nav
    global Page_Able_Click_Nav
    # 取最小导航数为下一个要点击的
    Page_To_Click_Nav = Page_Able_Click_Nav[0]
    # 点击最小导航数
    # locator('text=1')模糊匹配1,01,10,11等;locator('text="1"')精确匹配1
    PageToTurn.locator(Xpath_Page_Nav).locator('text="' + str(Page_To_Click_Nav) + '"').click()
    PageToTurn.wait_for_timeout(random.randint(1000, 3000))
    # 刚点击的数字追加到「已点击导航数字集合」
    Page_Clicked_Nav.add(Page_To_Click_Nav)
    # 当前页导航列表
    Current_Nav_list = PageToTurn.query_selector_all(Xpath_Page_Nav + "/*")
    for i in Current_Nav_list:
        Nav_num = i.text_content()
        # 抽取出导航列表中的数字，「上一页」「下一页」这种非确定性导航都排除
        if str(Nav_num).isdigit():
            Page_All_Nav.add(int(Nav_num))
    # 可点击导航数字集合 = 所有导航数字集合 ∩ 已点击导航数字集合，再转换成列表
    Page_Able_Click_Nav = sorted(list(Page_All_Nav.difference(Page_Clicked_Nav)))


# 获取每一页的信息
def ExtractEachPageInfo(SaiContext, CurrentPage):
    # 所有导航数字集合
    global Page_All_Nav
    Page_All_Nav = set()
    # 已点击导航数字集合
    global Page_Clicked_Nav
    Page_Clicked_Nav = set()
    # 可点击导航数字集合，初始设置为1，即第一页
    global Page_Able_Click_Nav
    Page_Able_Click_Nav = [1]
    # 逐个页面获取信息
    while len(Page_Able_Click_Nav) > 0:
        TurnPage(CurrentPage)
        # 贴吧有些内容不划到位是不展示的
        PageScroll(CurrentPage, 10)
        # 获取当前页的所有楼层
        Floors = CurrentPage.query_selector_all(Xpath_Floors)
        # 遍历每个楼层
        for this_floor in Floors:
            # 获取当前楼层的信息
            ExtractCurrentFloorInfo(this_floor)
            # 若本楼层有评论，且评论被折叠，则展开
            if this_floor.query_selector('text="点击查看"') != None:
                this_floor.query_selector('text="点击查看"').click()
                CurrentPage.wait_for_timeout(random.randint(500, 1000))
            if this_floor.query_selector(Xpath_Floor_Comments) != None:
                ExtractFloorCommentsInfo(SaiContext, CurrentPage, this_floor)
            # CurrentPage.wait_for_timeout(random.randint(1000, 3000))


# 评论：获取当前楼层每一个评论页信息
def ExtractFloorCommentsInfo(SaiContext, CurrentCommentPage, this_page_floor):
    # 所有导航数字集合
    global All_Nav
    All_Nav = set()
    # 已点击导航数字集合
    global Clicked_Nav
    Clicked_Nav = set()
    # 可点击导航数字集合，初始设置为1，即第一页
    global Able_Click_Nav
    # 判断当前楼层的评论是否为多页，多页才会出现1、2、3导航，只有1页没有导航
    if (
        this_page_floor.query_selector(Xpath_Floor_Nav) != None
        and this_page_floor.query_selector(Xpath_Floor_Nav).inner_html() != "&nbsp;"
    ):
        Able_Click_Nav = [1]
        # 逐个评论页面获取信息
        while len(Able_Click_Nav) > 0:
            TurnCommentsPage(CurrentCommentPage, this_page_floor)
            # 获取当楼层的当前评论页的评论list
            Comment_Floors = this_page_floor.query_selector_all(Xpath_Floor_Comments)
            # 遍历每个评论楼层
            for this_comment_floor in Comment_Floors:
                # 获取当前评论楼层的信息
                ExtractCurrentComentFloorInfo(this_page_floor, this_comment_floor)
                # CurrentPage.wait_for_timeout(random.randint(1000, 3000))
    else:
        # 获取当楼层的当前评论页的评论list
        Comment_Floors = this_page_floor.query_selector_all(Xpath_Floor_Comments)
        # 遍历每个评论楼层
        for this_comment_floor in Comment_Floors:
            # 获取当前评论楼层的信息
            ExtractCurrentComentFloorInfo(this_page_floor, this_comment_floor)


# 评论：获取每一个评论楼层信息
def ExtractCurrentComentFloorInfo(this_page_floor, this_comment_floor):
    if this_comment_floor.query_selector(Xpath_Comment_Author) != None:
        Comment_Author = this_comment_floor.query_selector(Xpath_Comment_Author).text_content()
        Comment_Content = this_comment_floor.query_selector(Xpath_Comment_Content).text_content()
        with open(MDFileDir, mode="a", encoding="utf-8") as f:
            f.write("> " + Comment_Author + ": " + Comment_Content + "\n")


# 评论：翻页
def TurnCommentsPage(CurrentPage, this_page_floor):
    global All_Nav
    global Clicked_Nav
    global Able_Click_Nav
    # 取最小导航数为下一个要点击的
    To_Click_Nav = Able_Click_Nav[0]
    # 点击最小导航数
    # locator('text=1')模糊匹配1,01,10,11等;locator('text="1"')精确匹配1
    this_page_floor.query_selector(Xpath_Floor_Nav).query_selector('text="' + str(To_Click_Nav) + '"').click()
    CurrentPage.wait_for_timeout(random.randint(500, 1500))
    # 刚点击的数字追加到「已点击导航数字集合」
    Clicked_Nav.add(To_Click_Nav)
    # 当前页导航列表
    Current_Nav_list = this_page_floor.query_selector_all(Xpath_Floor_Nav + "/*")
    for i in Current_Nav_list:
        Nav_num = i.text_content()
        # 抽取出导航列表中的数字，「上一页」「下一页」这种非确定性导航都排除
        if str(Nav_num).isdigit():
            All_Nav.add(int(Nav_num))
    # 可点击导航数字集合 = 所有导航数字集合 ∩ 已点击导航数字集合，再转换成列表
    Able_Click_Nav = sorted(list(All_Nav.difference(Clicked_Nav)))


def run(playwright: Playwright) -> None:
    WebSite = "https://tieba.baidu.com/p/8670538425"
    # WebSite = input("请输入要爬的网址: ")
    SaiBrowser, SaiContext, SaiPage = InitialChrome(WebSite)
    InitialMDFile()
    # 获取帖子标题
    ExtractTileInfo(SaiPage)
    # 获取楼层信息
    ExtractEachPageInfo(SaiContext, SaiPage)

    # 收尾
    SaiPage.close()
    SaiContext.close()
    SaiBrowser.close()


with sync_playwright() as playwright:
    run(playwright)
```

