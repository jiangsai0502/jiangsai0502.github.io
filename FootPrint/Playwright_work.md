#### 无头浏览器爬虫

1. 安装`stealth`插件，用来绕过无头浏览器检测

   > `pip install playwright-stealth`

2. debug模式启动Chrome本地无头浏览器

   > ```bash
   > /Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome --headless --remote-debugging-port=9222

```python
import os, html2text, re, random
from playwright.sync_api import Playwright, sync_playwright
from Module import Play_Wright_modules as pwm
from playwright_stealth import stealth_sync


def Initial_Headless_Chrome(playwright, WebSites, AbortPic, WaitLoad):
    """
    初始化浏览器：调用本地Chrome，在新标签打开目标网页，并切换到该标签
    """
    SaiBrowser = playwright.chromium.connect_over_cdp("http://localhost:9222")
    ########## 无头反爬处理 ##########
    # 设置用户代理和其他选项
    custom_user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"
    context_options = {"user_agent": custom_user_agent}
    SaiContext = SaiBrowser.new_context(**context_options)
    stealth_sync(SaiContext)
    # 处理WebGL检测
    SaiContext.add_init_script(
        """
        (() => {
            const getParameter = WebGLRenderingContext.getParameter;
            WebGLRenderingContext.prototype.getParameter = function(parameter) {
                if (parameter === 37445) {
                    return 'NVIDIA Corporation';
                }
                if (parameter === 37446) {
                    return 'NVIDIA GeForce GTX 1050 Ti with Max-Q Design OpenGL Engine';
                }
                return getParameter(parameter);
            };
        })();
    """
    )
    ########## 无头反爬处理 ##########
    # 是否阻止图片加载
    if AbortPic:
        SaiContext.route(
            re.compile(r"(.*\.png.*)|(.*\.jpg.*)|(.*\.gif.*)|(.*\.webp.*)"), lambda route: route.abort()
        )
    SaiPages = []
    for i in WebSites:
        SaiPage = SaiContext.new_page()
        SaiPage.goto(i)
        SaiPage.bring_to_front()
        if WaitLoad:
            SaiPage.wait_for_load_state("networkidle")
        SaiPage.wait_for_timeout(random.randint(1000, 3000))
        SaiPages.append(SaiPage)
    return SaiBrowser, SaiContext, SaiPages


def run(playwright: Playwright) -> None:
    global MarkDownMaker, MDFileDir  # 文件名称（含路径）
    WebSites = [
        "https://www.zhihu.com/question/21931620",
        "https://www.zhihu.com/question/485142113",
    ]
    SaiBrowser, SaiContext, SaiPages = pwm.Initial_Chrome(
        playwright, WebSites, AbortPic=False, WaitLoad=False
    )
    print(SaiPages[0].url)

    SaiContext.close()
    SaiBrowser.close()


with sync_playwright() as playwright:
    run(playwright)
```







