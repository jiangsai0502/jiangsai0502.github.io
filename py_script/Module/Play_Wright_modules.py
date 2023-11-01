import re, os, html2text, random


def Initial_Chrome(playwright, WebSites, AbortPic, WaitLoad):
    """
    初始化浏览器：调用本地Chrome，在新标签打开目标网页，并切换到该标签
    """
    SaiBrowser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    SaiContext = SaiBrowser.contexts[0]
    if AbortPic == True:
        SaiContext.route(
            re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.gif.*)|(.*\.webp.*)"), lambda route: route.abort()
        )
    SaiPages = []
    for i in WebSites:
        SaiPage = SaiContext.new_page()
        SaiPage.goto(i)
        SaiPage.bring_to_front()
        if WaitLoad == True:
            SaiPage.wait_for_load_state("networkidle")
        SaiPage.wait_for_timeout(random.randint(1000, 3000))
        SaiPages.append(SaiPage)
    return SaiBrowser, SaiContext, SaiPages


def Initial_EachWeb_MDFile(SaiPage):
    """
    每个网页初始化写入方法：切换到目标路径，将网页标题处理成合法文件名
    """
    # 切换MarkDown文件目录
    MDdir = "/Users/jiangsai/Desktop"
    os.chdir(MDdir)
    # 声明全局MarkDown文件操作类
    MarkDownMaker = html2text.HTML2Text()
    MarkDownMaker.ignore_links = True
    # 知乎网页标题格式：(99+ 封私信 / 81 条消息) 期货怎么才能赚钱？ - 知乎
    # 处理MarkDown文件名
    MDFile = SaiPage.title()
    # 文件名中不能含有'.', '/', ':' 这些字符
    replace_dict = {".": "_", "/": "_", ":": "_", " ": "_"}
    # 遍历字典的键值对，将字符串中的每一个键都替换为对应的值
    for key, value in replace_dict.items():
        MDFile = MDFile.replace(key, value)
    # 将重复的'_'替换为1个
    MDFile = re.sub(r"(_)\1+", "_", MDFile)
    # 将括号和括号中的字符替换掉
    MDFile = re.sub(r"\((.*?)\)", "", MDFile)
    # 声明全局MarkDown文件路径
    MDFileDir = f"{MDdir}/{MDFile}.md"
    return MarkDownMaker, MDFileDir


def Initial_Single_MDFile(MDdir, MDFile):
    """
    初始化1个Mrdkdown文件：切换到目标路径，指定文件名
    """
    # 切换MarkDown文件目录
    os.chdir(MDdir)
    # 声明全局MarkDown文件操作类
    MarkDownMaker = html2text.HTML2Text()
    MarkDownMaker.ignore_links = True
    # 声明全局MarkDown文件路径
    MDFileDir = f"{MDdir}/{MDFile}"
    return MarkDownMaker, MDFileDir


def Page_Scroll(ScrollPage, ScrollTimes):
    """
    滚动加载更多内容，直到不再加载或者滚动了10次
    """
    #
    NotEnd = True
    ScrollTime = 1
    while NotEnd and ScrollTime < ScrollTimes:
        # 滚动前的页面高度
        BeforeScrollHeight = ScrollPage.evaluate("() => document.body.scrollHeight")
        ScrollTime += 1
        for i in range(3):
            # 滚动到页面底部
            ScrollPage.evaluate("() => window.scrollTo(0,document.body.scrollHeight)")
            # 微上划一下模拟人类
            ScrollPage.keyboard.press("PageUp")
            ScrollPage.wait_for_timeout(random.randint(1000, 3000))
        # 滚动后的页面高度
        AfterScrollHeight = ScrollPage.evaluate("() => document.body.scrollHeight")
        if BeforeScrollHeight == AfterScrollHeight or ScrollTime >= ScrollTimes:
            NotEnd = False


def Turn_Page(FatherPage, Xpath_Nav, Nav):
    """
    翻页
    """
    # 当前页导航列表
    Current_Nav_list = FatherPage.query_selector_all(Xpath_Nav + "/*")
    for i in Current_Nav_list:
        Nav_num = i.text_content()
        # 抽取出导航列表中的数字，「上一页」「下一页」这种非确定性导航都排除
        if str(Nav_num).isdigit():
            Nav["All_Nav"].add(int(Nav_num))
    # 若本页是第1页，则不用点击
    if Nav["Is_First_Nav"] == True:
        # 取所有导航数列表中最小的数为即将点击的数
        To_Click_Nav = sorted(list(Nav["All_Nav"]))[0]
        pass
    else:
        # 取可点击列表的最小导航数为即将点击的数
        To_Click_Nav = Nav["Able_Click_Nav"][0]
        # 点击最小导航数
        # locator('text=1')模糊匹配1,01,10,11等;locator('text="1"')精确匹配1
        FatherPage.locator(Xpath_Nav).locator('text="' + str(To_Click_Nav) + '"').click()
        FatherPage.wait_for_timeout(random.randint(1000, 3000))
    # 刚点击的数字追加到「已点击导航数字集合」
    Nav["Clicked_Nav"].add(To_Click_Nav)
    Nav["Is_First_Nav"] = False
    # 可点击导航数字集合 = 所有导航数字集合 ∩ 已点击导航数字集合，再转换成列表
    Nav["Able_Click_Nav"] = sorted(list(Nav["All_Nav"].difference(Nav["Clicked_Nav"])))
    if len(Nav["Able_Click_Nav"]) == 0:
        Nav["Finish_Nav"] = True
