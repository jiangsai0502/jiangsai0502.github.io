###### PlayWright爬虫通用方法

> 文件路径：`Module/PlayWright_modules.py`

[返回](FootPrint/Playwright.md#通用方法)

```python
import re, os, html2text, random, csv
from urllib.parse import urlparse
import mimetypes
import requests


def Initial_Chromium(playwright, WebSite, headless, AbortPic, WaitLoad):
    """
    初始化PlayWright自带的Chromium浏览器，在新标签打开目标网页，并切换到该标签
    """
    # 1、初始化一个浏览器（headless = False 有头浏览器；slow_mo = 3000 每个操作停3秒）
    SaiBrowser = playwright.chromium.launch(headless=headless, slow_mo=3000)
    # 2、是否加载本地cookie，有则加载，无则新建
    os.chdir("/Users/jiangsai/Desktop")
    if os.path.exists("state.json"):
        SaiContext = SaiBrowser.new_context(storage_state="state.json")
    else:
        SaiContext = SaiBrowser.new_context()
    # 3、是否阻止图片加载：拦截SaiContext下所有页面的图片请求（凡含.png的链接，都当做是png图片）
    if AbortPic:
        SaiContext.route(re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.gif.*)|(.*\.webp.*)"), lambda route: route.abort())
    # 4、初始化一个网页
    SaiPage = SaiContext.new_page()
    SaiPage.goto(WebSite)
    SaiPage.bring_to_front()
    if WaitLoad:
        SaiPage.wait_for_load_state("networkidle")
    else:
        # SaiPage.wait_for_timeout(random.randint(1000, 3000))
        pass
    return SaiBrowser, SaiContext, SaiPage


def Initial_LocalChrome(playwright, WebSites, AbortPic, WaitLoad):
    """
    初始化浏览器：调用本地Chrome，在新标签打开目标网页，并切换到该标签
    """
    # 1、调起本地Chrome，只能有头，调起前要手动退出Chrome程序
    SaiBrowser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    SaiContext = SaiBrowser.contexts[0]
    # 2、是否阻止图片加载
    if AbortPic:
        SaiContext.route(re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.gif.*)|(.*\.webp.*)"), lambda route: route.abort())
    # 3、逐个打开目标网页
    SaiPages = []
    for i in WebSites:
        SaiPage = SaiContext.new_page()
        SaiPage.goto(i)
        SaiPage.bring_to_front()
        # 4、不同的加载模式：等待页面反馈加载 or 读秒加载
        if WaitLoad:
            SaiPage.wait_for_load_state("networkidle")
        else:
            SaiPage.wait_for_timeout(random.randint(1000, 3000))
        SaiPages.append(SaiPage)
    return SaiBrowser, SaiContext, SaiPages


def Initial_EachWeb_MDFile(SaiPage):
    """
    每个网页初始化写入方法：切换到目标路径，将网页标题处理成合法文件名
    """
    # 1、切换MarkDown文件目录
    MDdir = "/Users/jiangsai/Desktop"
    os.chdir(MDdir)
    # 2、声明全局MarkDown文件操作类
    MarkDownMaker = html2text.HTML2Text()
    MarkDownMaker.ignore_links = True
    # 3、处理MarkDown文件名
    #   知乎网页标题格式：(99+ 封私信 / 81 条消息) 期货怎么才能赚钱？ - 知乎
    MDFile = SaiPage.title()
    # 4、文件名中不能含有'.', '/', ':' 这些字符
    replace_dict = {".": "_", "/": "_", ":": "_", " ": "_"}
    #   遍历字典的键值对，将字符串中的每一个键都替换为对应的值
    for key, value in replace_dict.items():
        MDFile = MDFile.replace(key, value)
    #   将重复的'_'替换为1个
    MDFile = re.sub(r"(_)\1+", "_", MDFile)
    #   将括号和括号中的字符替换掉
    MDFile = re.sub(r"\((.*?)\)", "", MDFile)
    # 5、声明全局MarkDown文件路径
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


def Initial_CSVFile(CSVdir, CSVFile):
    """
    初始化1个CSV文件：切换到目标路径，指定文件名
    """
    # 切换CSV文件目录
    os.chdir(CSVdir)
    # 声明全局CSV文件路径
    CSVFileDir = f"{CSVdir}/{CSVFile}"
    return CSVFileDir


def Page_Scroll(ScrollPage, ScrollTimes):
    """
    滚动加载更多内容，直到不再加载
    """
    #
    NotEnd = True
    ScrollTime = 1
    while NotEnd and ScrollTime < ScrollTimes:
        # 1、记录滚动前的页面高度
        BeforeScrollHeight = ScrollPage.evaluate("() => document.body.scrollHeight")
        ScrollTime += 1
        for i in range(3):
            # 2、滚动到页面底部
            ScrollPage.evaluate("() => window.scrollTo(0,document.body.scrollHeight)")
            # 3、微上划一下模拟人类
            ScrollPage.keyboard.press("PageUp")
            # 4、缓一下模拟人类
            ScrollPage.wait_for_timeout(random.randint(500, 2000))
        # 5、记录滚动后的页面高度
        AfterScrollHeight = ScrollPage.evaluate("() => document.body.scrollHeight")
        # 6、判断滚动前后的页面是否有变化，如果没变，说明到底了
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
    if Nav["Is_First_Nav"]:
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


def Write_to_CSV(WriteList, CsvFile):
    # 将数据写入CSV文件
    with open(CsvFile, "w", encoding="utf-8-sig") as csv_file:
        # 取列表首个元素（dict）的key，作为表头
        Head = []
        for key in WriteList[0]:
            Head.append(key)
        # 创建一个读写对象
        CSVwriter = csv.writer(csv_file)
        # 写入表头
        CSVwriter.writerow(Head)
        # 逐行写入
        for temp_dict in WriteList:
            row = []
            # 按照key取出dict的每个元素
            for key in Head:
                row.append(temp_dict[key])
            CSVwriter.writerow(row)


def Write_to_TXT(data, txt_file):
    """保存到txt文件
    data：待保存数据，如：[("name1", "value1"),("name2", "value2")]
    txt_file：保存文件路径
    """
    """"""
    # 打开文件以写入数据
    with open(txt_file, "a+") as file:
        for item in data:
            # 将每个项写入文件，以适当的格式
            file.write(f"{item[0]}：{item[1]}\n")
    print(f"已写入文件：{txt_file}")


def download_file(url, filename, folder):
    """下载文件
    url：文件URL
    filename：文件名
    folder：文件保存的目录
    """
    # 检查保存文件的文件夹是否存在
    if not os.path.exists(folder):
        os.makedirs(folder)

    # 提取URL的文件扩展名
    parsed_url = urlparse(url)
    path = parsed_url.path
    extension = os.path.splitext(path)[1]

    # 如果无法从URL中获取扩展名，尝试从内容类型中获取
    if not extension:
        response = requests.head(url)
        content_type = response.headers.get("content-type")
        extension = mimetypes.guess_extension(content_type)

    # 构造完整的文件名
    filename = f"{filename}{extension}"
    file_path = os.path.join(folder, filename)

    # 检查文件是否存在
    if not os.path.exists(file_path):
        print(f"正在下载: {file_path}")
        # 下载文件
        response = requests.get(url)
        response.raise_for_status()  # 确保请求成功
        # 保存文件
        with open(file_path, "wb") as file:
            file.write(response.content)
        print(f"文件已下载: {file_path}")
    else:
        print(f"{file_path} 已存在")


def convert_wan_to_number(num):
    if "万" in num:
        # 删除"万"字符
        num = num.replace("万", "").strip()
        return str(int(float(num) * 10000))
    else:
        return str(num)
```

