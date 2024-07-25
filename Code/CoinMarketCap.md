###### CoinMarketCap获取实时BTC价格

> 价格>XXX时，弹窗提示

```python
import time  # 处理睡眠和时间延迟
import subprocess  # 运行系统命令
import webbrowser  # 打开浏览器
from playwright.sync_api import sync_playwright
from rich.progress import Progress, SpinnerColumn, BarColumn, TextColumn  # 显示进度条
from rich.live import Live  # 实时更新控制台输出


def get_btc_price(page):
    # 查找价格元素
    price_element = page.query_selector("//*[@id='section-coin-overview']/div[2]/span")
    if price_element:  # 检查价格元素是否存在
        price_text = price_element.inner_text()
        price = float(price_text.replace("$", "").replace(",", ""))
        return price
    return None


def show_notification(price):
    title = "BTC 价格"
    message = f"当前 BTC 价格: ${price}"
    subprocess.run(
        ["osascript", "-e", f'display notification "{message}" with title "{title}"']
    )  #  显示 macOS 通知


def open_url():
    webbrowser.open("https://coinmarketcap.com/zh/currencies/bitcoin/")


def countdown(tag, seconds, live):
    progress = Progress(  # 创建进度条
        SpinnerColumn(),
        BarColumn(bar_width=None),
        TextColumn("[progress.percentage]{task.percentage:>3.0f}%"),
        TextColumn("[progress.description]{task.description}"),
    )
    task = None
    if tag == "page":
        task = progress.add_task("[blue]等待页面加载", total=seconds)  # 添加新任务到进度条
    elif tag == "getprice":
        task = progress.add_task("[green]获取实时价格", total=seconds)

    for _ in range(seconds):
        time.sleep(1)
        progress.advance(task)
        live.update(progress)  # 实时更新进度条


with sync_playwright() as p:
    # 本地 Chrome 浏览器路径
    chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
    browser = p.chromium.launch(headless=True, executable_path=chrome_path)  # 启动无头 Chrome 浏览器
    page = browser.new_page()  # 创建一个新页面
    page.goto("https://coinmarketcap.com/currencies/bitcoin/")

    # 使用倒计时进度条等待页面加载
    with Live() as live:
        countdown("page", 5, live)
        while True:
            price = get_btc_price(page)
            if price:
                live.update(f"当前 BTC 价格: ${price}")
                if price > 64150:  # 调整价格阈值以确保测试
                    show_notification(price)
                    # open_url()
                    break
            else:
                live.update("无法获取 BTC 价格")

            # 每3秒检查一次，并显示倒计时进度条
            countdown("getprice", 3, live)

    browser.close()
```



