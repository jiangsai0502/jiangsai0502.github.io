>从网站获取下载链接，写入txt

```python
import os, re, random, requests
from playwright.sync_api import Playwright, sync_playwright
from Module import PlayWright_modules as pwm
from urllib.parse import urlparse
import mimetypes

#########################全局变量#########################
# 底部导航Xpath
Xpath_Nav = '//*[@id="rc-tabs-0-panel-videoUpload"]/div/div/div/div/ul'
# 内容块
Xpath_list = '//div[@id="rc-tabs-0-panel-videoUpload"]//tbody[@class="ant-table-tbody"]/*'
# 内容块的标题
Xpath_title = "//td[2]/div/p[2]/a"
# 内容块的预览
Xpath_click = "//td[1]/div/button"
# 内容块的下载
Xpath_download = '//div[@class="ant-modal-body"]//source'
#########################全局变量#########################


# 获取每页信息
def Get_Each_Page_Info(WritePage, count):
    # 增加页面加载时间，防止Dom获取不到节点
    WritePage.wait_for_timeout(random.randint(5000, 7000))
    Elements = WritePage.query_selector_all(Xpath_list)
    # 本页数据集
    data = []
    for element in Elements:
        # 1、获取标题
        title = element.query_selector(Xpath_title).text_content()
        title = f"{count}-{title}"
        # 2、点击视频预览，获取视频链接
        element.query_selector(Xpath_click).click()
        WritePage.wait_for_timeout(random.randint(500, 1500))
        download_url = WritePage.query_selector(Xpath_download).get_attribute("src")
        # 3、关闭弹窗
        WritePage.keyboard.press("Escape")
        # 4、填充本页数据集
        data.append((title, download_url))
        # 5、计数器自增
        count = count + 1
        print(f"{title}：{download_url}")
    # 6、将（文件名，下载链接）写入txt文件
    txt_file = "/Users/jiangsai/Desktop/test/output.txt"
    pwm.Write_to_TXT(data, txt_file)
    return count


# 获取信息
def GetInfo(SaiContext, SaiPage):
    # 导航
    Nav = {
        "All_Nav": set(),
        "Clicked_Nav": set(),
        "Able_Click_Nav": [],
        "Is_First_Nav": True,
        "Finish_Nav": False,
    }
    # 下载计数器
    count = 1
    # 持续取本页的数据，直到导航到最后一页
    while True:
        # 1、翻页
        pwm.Turn_Page(SaiPage, Xpath_Nav, Nav)
        # 2、获取本页信息块的具体信息
        count = Get_Each_Page_Info(SaiPage, count)
        # 3、判断是否到达最后一页
        if Nav["Finish_Nav"] == True:
            break


def run(playwright: Playwright) -> None:
    global MarkDownMaker, MDFileDir  # 文件名称（含路径）
    WebSites = [
        "https://manage.colorv.com/general-manage/#/user/allUser/18284639",
    ]
    SaiBrowser, SaiContext, SaiPages = pwm.Initial_LocalChrome(playwright, WebSites, AbortPic=False, WaitLoad=False)
    for SaiPage in SaiPages:
        MarkDownMaker, MDFileDir = pwm.Initial_EachWeb_MDFile(SaiPage)
        SaiPage.bring_to_front()
        # 获取信息
        GetInfo(SaiContext, SaiPage)
        # 收尾
        # SaiPage.close()
    SaiContext.close()
    SaiBrowser.close()


with sync_playwright() as playwright:
    run(playwright)
```

> 从txt获取下载信息，进行下载

```PY
from Module import PlayWright_modules as pwm
import os
import requests
from urllib.parse import urlparse
import mimetypes


# 读取文本文件并下载文件
def download_files_from_text(download_file, download_dir):
    with open(download_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split("：")
            if len(parts) == 2:
                filename = parts[0]
                url = parts[1]
                pwm.download_file(url, filename, download_dir)


if __name__ == "__main__":
    download_dir = "/Users/jiangsai/Desktop/test"
    download_file = "/Users/jiangsai/Desktop/test/output.txt"
    # 调用下载文件的函数
    download_files_from_text(download_file, download_dir)
```

> Xpath 获取视频链接和视频名后存入txt，格式如下
>
> ```
> 001_什么是迷宫理论？如何入门金融交易?：https://www.youtube.com/watch?v=Jy6mkzDsbmE
> 002_02_基本面分析，技术分析和盘口分析概述：https://www.youtube.com/watch?v=bgZBeaa3H6Y
> ```

```python
import os
import subprocess


def download_url(url, filename, folder):
    """下载文件
    url：文件URL
    filename：文件名
    folder：文件保存的目录
    """
    # 检查保存文件的文件夹是否存在
    if not os.path.exists(folder):
        os.makedirs(folder)
    os.chdir(folder)

    # 检查文件是否存在
    if not os.path.exists(filename):
        print(f"正在下载: {filename}")
        # 定义要执行的命令
        command = ["yt-dlp", "--cookies-from-browser", "chrome", "-o", filename, url]

        # 使用subprocess.Popen()创建子进程来执行命令
        process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

        # 实时获取并打印命令的输出
        while True:
            output = process.stdout.readline()
            if output == "" and process.poll() is not None:
                break
            if output:
                print(output.strip())

        # 获取命令的返回代码
        return_code = process.poll()
        print(f"命令执行完毕，返回代码: {return_code}")
    else:
        print(f"{filename} 已存在")


# 读取文本文件并下载文件
def download_files_from_text(download_file, download_dir):
    with open(download_file, "r") as file:
        lines = file.readlines()
        for line in lines:
            parts = line.strip().split("：")
            if len(parts) == 2:
                filename = parts[0]
                url = parts[1]
                download_url(url, filename, download_dir)


if __name__ == "__main__":
    download_dir = "/Users/jiangsai/Desktop/test"
    download = "/Users/jiangsai/Desktop/1.txt"
    # 调用下载文件的函数
    download_files_from_text(download, download_dir)
```

