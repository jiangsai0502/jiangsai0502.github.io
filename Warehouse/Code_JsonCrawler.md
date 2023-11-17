###### Json数据接口爬虫   [返回](FootPrint/Playwright.md#Json数据接口爬虫)

```python
import json
from playwright.sync_api import Playwright, sync_playwright, expect

def handle_json(json):
    for p in json['data']['list']['vlist']:
        title = p['title']
        comment = p['comment']
        print('title: ', title, ' comment: ', comment)

def handle(response):
    if response is not None:
        if response.url.startswith("https://api.bilibili.com/x/space/wbi/arc/search?"):
            print(response.request.url)
            print(response.request.post_data)
            handle_json(response.json())

def run(playwright: Playwright) -> None:
    SaiBrowser = playwright.chromium.connect_over_cdp('http://localhost:9222')
    SaiContext = SaiBrowser.contexts[0]
    SaiPage = SaiContext.new_page()
    SaiPage.on("response", lambda response: handle(response=response))
    SaiPage.goto('https://space.bilibili.com/107861587/video?pn=2')

    SaiContext.close()
    SaiBrowser.close()

with sync_playwright() as playwright:
    run(playwright)
```

