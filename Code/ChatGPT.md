###### ChatGPT爬虫   [返回](FootPrint/Playwright.md#ChatGPT爬虫)

```js
from numbers import Integral
import re, os, random
from playwright.sync_api import Playwright, sync_playwright, expect
from bs4 import BeautifulSoup

WebSite = 'https://chat.openai.com/'
Xpath_Answer = '//div[@class="flex flex-col text-sm dark:bg-gray-800"]/div'

def Initialize(WebSite):
 SaiBrowser = playwright.chromium.connect_over_cdp('http://localhost:9222')
 SaiContext = SaiBrowser.contexts[0]
 SaiPage = SaiContext.new_page()
 SaiPage.goto(WebSite)
 SaiPage.wait_for_load_state("networkidle")
 SaiPage.bring_to_front()
 SaiPage.wait_for_timeout(10000)
 return SaiBrowser, SaiContext, SaiPage

def run(playwright: Playwright) -> None:
 SaiBrowser, SaiContext, SaiPage = Initialize(WebSite)
 question_list=['python','sql','oracle','mysql']
 for qst in question_list:
     SaiPage.get_by_role("textbox").fill(qst)
     SaiPage.get_by_role("textbox").press("Enter")
     SaiPage.wait_for_timeout(random.randint(1500, 2500))
     text1 = "1"
     text2 = "2"
     while(text1 != text2):
         t1_list = SaiPage.query_selector_all(Xpath_Answer)
         if(len(t1_list)>0):
             text1 = t1_list[-2].inner_text()
         SaiPage.wait_for_timeout(random.randint(1000,3000))
         t2_list = SaiPage.query_selector_all(Xpath_Answer)
         if(len(t2_list)>0):
             text2 = t2_list[-2].inner_text()
         print(text1)

 SaiContext.close()
 SaiBrowser.close()
# ---------------------收尾工作---------------------

with sync_playwright() as playwright:
 run(playwright)
```

