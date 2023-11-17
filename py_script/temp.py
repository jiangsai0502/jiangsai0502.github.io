import requests
from bs4 import BeautifulSoup
import os

# 确定第1个网页的URL
first_page_url = "https://space.bilibili.com/111082383/video"

# 创建一个目录来保存所有下载的网页
download_dir = "/Users/jiangsai/Desktop/Temp"
if not os.path.exists(download_dir):
    os.makedirs(download_dir)

# 发送请求并获取第1个网页的内容
fake_headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36"
}
response = requests.get(first_page_url, headers=fake_headers)
first_page_content = response.text

# 使用BeautifulSoup来解析第1个网页的内容
soup = BeautifulSoup(first_page_content, "html.parser")

# 保存第1个网页到本地文件
first_page_local_path = os.path.join(download_dir, "first_page.html")
with open(first_page_local_path, "w", encoding="utf-8") as file:
    file.write(first_page_content)
