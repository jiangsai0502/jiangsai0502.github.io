# Python 模块

**数据源**

```python
import requests
from bs4 import BeautifulSoup

def GetSoup(url):
    fake_headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
    }
    html = requests.get(url, headers=fake_headers).content.decode('utf-8')
    soup = BeautifulSoup(html, 'html.parser')
    return soup

def GetBigData(soup):
    all_movies = soup.find('ol', class_="grid_view")
    bigData = []
    for each_movie in all_movies.find_all('div', class_="info", limit = 2):
        data = {}
        hd_tag = each_movie.find('div', class_="hd")
        data['电影名'] = hd_tag.find('a').find_all('span', class_="title")[0].text
        bd_tag = each_movie.find('div', class_="bd")
        data['评分'] = bd_tag.div.find('span', class_="rating_num").text
        data['评价人数'] = bd_tag.div.find_all('span')[3].text
        bigData.append(data)
    return bigData

def PrintBigData(bigData):
    for data in bigData:
        for each_key,each_value in data.items():
            print(f'{each_key}:{each_value}')
        print('-'*30)

if __name__ == "__main__":
    Url = "https://movie.douban.com/top250?start="
    soup = GetSoup(Url)
    bigData = GetBigData(soup)
    PrintBigData(bigData)
```

**打印 print**

```python
# bigData 是 List，data 是 Dictionary
def PrintBigData(bigData):
    for data in bigData:
        for each_key,each_value in data.items():
            print(f'{each_key}:{each_value}')
        print('-'*30)
```



### 读写 TXT

##### 1. 写操作，写入时覆盖原文

```python
# 自动关闭文件
with open('/Users/jiangsai02/Documents/Temp/test.txt', 'w') as OpenTxt:
    OpenTxt.write(response.content.decode('utf-8'))
```

##### 2. 读操作

```python
# 自动关闭文件
with open('/Users/jiangsai02/Documents/Temp/test.txt', 'r', encoding="utf-8") as OpenTxt:
    Html = OpenTxt.read()
```

**3. 项目模块**

```python
# bigData 是 List，data 是 Dictionary
def WriteToTxt(bigData):
    with open('/Users/jiangsai02/Documents/Temp/test.txt', 'w') as OpenTxt:
        for data in bigData:
            for each_key,each_value in data.items():
                OpenTxt.write(f'{each_key}:{each_value}\n')
            OpenTxt.write('\n')
```



### 读写 CSV

```python
import requests, os, csv

CsvFile = "/Users/jiangsai/Desktop/test.csv"

MoiveList = [
    {"影片名": "教父", "评分": "9.7", "评价人数": "2938225人"},
    {"影片名": "冰与火", "评分": "9.6", "评价人数": "2170430人"},
]

with open(CsvFile, mode="w+", encoding="gbk", newline="") as OpenCSV:
    ########### 方法1：csv.DictWriter ##########
    # 设置CSV文件的表头
    Header = ["影片名", "评分", "评价人数"]
    # 创建一个DictWriter对象，指定字段名和CSV文件
    CSVwriter = csv.DictWriter(OpenCSV, fieldnames=Header)
    # 写入表头
    CSVwriter.writeheader()
    # 写入电影信息
    for movie in MoiveList:
        CSVwriter.writerow(movie)
        
    ########### 方法2：csv.writer ##########
    # 设置CSV文件的表头
    Header = ["影片名", "评分", "评价人数"]
    # 创建一个读写对象
    CSVwriter = csv.writer(OpenCSV)
    # 写入表头
    CSVwriter.writerow(Header)
    # 写入电影信息
    for movie in MoiveList:
        row = [movie["影片名"], movie["评分"], movie["评价人数"]]
        CSVwriter.writerow(row)
```

> 方法1和方法2的输出
>
> | 影片名 | 评分 | 评价人数  |
> | ------ | ---- | --------- |
> | 教父   | 9.7  | 2938225人 |
> | 冰与火 | 9.6  | 2170430人 |
>
> 方法3 的输出
>
> | 影片名 | 教父   | 评分 | 9.7  | 评价人数 | 2938225人 |
> | ------ | ------ | ---- | ---- | -------- | --------- |
> | 影片名 | 冰与火 | 评分 | 9.6  | 评价人数 | 2170430人 |
>
> ##### 1. 写操作
>
> ```python
> with open(CsvFile, mode="w+", encoding="gbk", newline="") as OpenCSV:
>     CSVwriter = csv.writer(OpenCSV)
>     for movie in MoiveList:
>         extend_row = []
>         for key, value in movie.items():
>             extend_row.extend([key, value])
>         CSVwriter.writerow(extend_row)
> ```
>
> > * mode = "w+" 覆盖式读写，若文件存在，则打开，若不存在，则新建后打开
> > * mode = "a+" 追加式读写，若文件存在，则打开，若不存在，则新建后打开
> > * python3 默认是 utf-8 读写文本，若乱码可切换为 utf-8-sig 或 gbk
> > * newline = "" 将数值写入新行
> > * writerow 每次写入一行
>
> ##### 2. 读操作
>
> ```python
> with open(CsvFile, mode="r", encoding="gbk", newline="") as OpenCSV:
>     CSVreader = csv.reader(OpenCSV)
>     # 逐行转换成list，同行内每一个单元格为一个元素
>     for row in CSVreader:
>         print(row)
>         print(row[2], row[4])
> ```
>
> > * mode = "r" 读取
> > * encoding="gbk" 读取的编码要和写入的保持一致，写入时是 "gbk" ，读取时也要 "gbk"
> > * 每次读取csv文件的 1 行
>
>
> ​		

### 读写 Excel

1. 环境

   > `pip install openpyxl`
   >
   > `pip install pandas `

2. 数据预备

   ```python
   import pandas as pd
   
   ExcelFile = "/Users/jiangsai/Desktop/test.xlsx"
   MoiveList = [
       {"影片名": "教父", "评分": "9.7", "评价人数": "2938225人"},
       {"影片名": "冰与火", "评分": "9.6", "评价人数": "2170430人"},
   ]
   ```

3. Pandas写Excel

   1. 覆盖写入

      ```python
      # 一次写入所有行
      df = pd.DataFrame(MoiveList)
      df.to_excel(ExcelFile, index=False, sheet_name="Sheet1")
      ```

   2. 追加写入

      ```python
      new_data = [
          {"影片名": "肖申克的救赎", "评分": 9.3, "评价人数": 2513246},
          {"影片名": "盗梦空间", "评分": 8.8, "评价人数": 2092510},
      ]
      
      # 转换新数据
      data_to_append = pd.DataFrame(new_data)
      # 读取旧数据
      original_data = pd.read_excel(ExcelFile)
      # 合并新旧数据
      combined_data = pd.concat([original_data, data_to_append], ignore_index=True)
      # 将合并后的数据写回 Excel
      with pd.ExcelWriter(ExcelFile, mode="w", engine="openpyxl") as writer:
          combined_data.to_excel(writer, sheet_name="Sheet1", index=False)
      ```

4. Pandas读Excel

   ```python
   # 一次读取所有行到字典列表
   df = pd.read_excel(ExcelFile, sheet_name="Sheet1")
   # 将DataFrame转换为字典列表
   movies_list = df.to_dict(orient="records")
   print(movies_list)
   ```

5. 不常用读写

   ```python
   # 逐行写入
   with pd.ExcelWriter(ExcelFile, engine="xlsxwriter") as writer:
       workbook = writer.book
       worksheet = workbook.add_worksheet("Sheet1")
       # 写入列名
       headers = MoiveList[0].keys()
       for col_num, header in enumerate(headers):
           worksheet.write(0, col_num, header)
       # 写入数据
       for row_num, row_data in enumerate(MoiveList, start=1):
           for col_num, value in enumerate(row_data.values()):
               worksheet.write(row_num, col_num, value)
   
   # 逐行读取到字典列表
   def read_excel_row_by_row(ExcelFile, sheet_name):
       # 读取 Excel 文件
       xls = pd.ExcelFile(ExcelFile)
       # 读取到的数据
       ReadData = []
       # 逐行读取每个 sheet
       for sheet_name in xls.sheet_names:
           df = xls.parse(sheet_name)
           # 获取列名
           column_names = df.columns
           # 逐行读取数据
           for index, row in df.iterrows():
               row_data = {}
               for column_name in column_names:
                   value = row[column_name]
                   row_data[column_name] = value
               ReadData.append(row_data)
       return ReadData
   
   ReadData = read_excel_row_by_row(ExcelFile, "Sheet1")
   print(ReadData)
   ```

##### 合并多个Excel的sheet到一个sheet

> 把 `yeying`目录下所有Excel中名为 "问题分类" 的sheet页合并到名为CombineTable的Excel中，名为combine的sheet页

```python
import xlrd
from openpyxl import Workbook, load_workbook
import os.path
import os

root_dir = '/Users/jiangsai02/Documents/Temp/yeying' #路径
files = os.listdir(root_dir) #获取文件夹下的所有文件
num = len(files) #获取文件数量

MyWB = load_workbook('/Users/jiangsai02/Documents/Temp/CombineTable.xlsx')
MyWS = MyWB.get_sheet_by_name("combine")

for n in range(num):  # 遍历每一个Excel文件
    path = os.path.join(root_dir,files[n]) #路径拼接，得出具体的文件名字
    wb = xlrd.open_workbook(path)  #打开excel表格
    ws = wb.sheet_by_name('问题分类')

    max_row = ws.nrows  #最大行数
    max_column = ws.ncols  #最大列数
    for row in range(1, max_row): # 第1行是表头，排除掉
        rowValues = ws.row_values(row)
        rowValues.append(files[n].replace('agile问题总结.xls',''))
        MyWS.append(rowValues)
    
MyWB.save('/Users/jiangsai02/Documents/Temp/CombineTable.xlsx')

```

> openpyxl 只能打开 .xlsx 文件，xlrd 能打开 .xls 文件

#### 操作csv

1. csv转Excel

   ```python
   import pandas as pd
   import time
   
   FromCsv = '/Users/sai/Documents/临时/Test.csv'
   ToExcel = '/Users/sai/Documents/临时/Test.xlsx'
   
   # 读取csv文件
   time_start=time.time()
   csv = pd.read_csv(FromCsv, encoding='utf-8')
   time_end=time.time()
   print('读取CSV用时：',time_end-time_start,' s')
   
   # 转换csv到Excel文件
   time_start=time.time()
   csv.to_excel(ToExcel, sheet_name='data')
   time_end=time.time()
   print('转换用时：',time_end-time_start,' s')
   ```

2. Excel转csv

   ```python
   import pandas as pd
   import time
   
   FromExcel = '/Users/sai/Documents/临时/Test.xlsx'
   ToCsv = '/Users/sai/Documents/临时/Test2.csv'
   
   # 读取Excel文件
   time_start=time.time()
   xls = pd.read_excel(FromExcel, index_col=0)
   time_end=time.time()
   print('读取Excel用时：',time_end-time_start,' s')
   
   # 转换Excel到csv文件
   time_start=time.time()
   xls.to_csv(ToCsv, encoding='utf-8')
   time_end=time.time()
   print('转换用时：',time_end-time_start,' s')
   ```
   
3. 拆分csv

   ```python
   import chardet,time
   myExcel = '/Users/sai/Documents/临时/Test.csv'
   f = open(myExcel, 'rb')
   lines = f.readline()
   file_code = chardet.detect(lines)['encoding']
   
   # 修改读取文件代码
   with open(myExcel, 'r', encoding=file_code) as f:
       csv_file = f.readlines()
   
   # 定义csv分割行数
   linesPerFile = 100000
   # 初始化文件编号为1
   filecount = 1
   # 以0为起点，文件行数为终点，分片大小为间隔，循环遍历文件，每次遍历行数即为分片大小，而不是每行遍历一次
   for i in range(0, len(csv_file), linesPerFile):
       # 打开目标文件准备写入，不存在则创建
       with open(myExcel[:-4] + '_' + str(filecount) + '.csv', 'w+') as f:
           # 判断是否为第一个文件，不是的话需要先写入标题行
           if filecount > 1:
               f.write(csv_file[0])
           # 批量写入i至i+分片大小的多行数据
           f.writelines(csv_file[i:i+linesPerFile])
           # 完成一个文件写入之后，文件编号增加1
           filecount += 1
   ```

   

### 多线程

> 线程用法
>
> 1. 独立线程：如 `keyboard_thread` 用于控制整个程序的结束
> 2. 并行线程：如 `threads` 用于多线程执行主程序任务（下载）

> 模拟多线程下载

```python
import time
import threading
from pynput import keyboard
import random


def keyboard_listener():
    """键盘监听函数：键盘输入q键退出整个程序"""

    def on_press(key):
        """内部函数：当键盘按键被按下时触发"""
        try:
            if key.char == "q":
                print("自动防故障触发，程序停止中……")
                stop_event.set()  # 设置停止事件
                return False  # 停止监听
        except AttributeError:
            pass  # 对于非字符按键（如功能键等）不做处理

    # 对于非字符按键（如功能键等）不做处理
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()  # 阻塞当前线程，直到监听器停止


def download(video):
    """模拟下载视频的函数"""
    # 随机生成一个下载所需的时间长度
    download_time = random.randint(5, 20)
    for i in range(1, download_time, 1):
        # 模拟下载当前视频，打印下载时间
        print(f"片名：{video[0]} 链接：{video[1]}，下载的第{i}秒")
        time.sleep(1)
    print(f"------ {video} 下载完成 ------")


def manage_threads(my_list):
    """管理工作线程"""
    threads = []  # 用于存储工作线程的列表
    while my_list and not stop_event.is_set():  # 检查视频列表和全局停止事件
        # 确保总是有两个线程在运行
        while len(threads) < 2 and my_list and not stop_event.is_set():
            # 从列表中取出一个视频
            item = my_list.pop(0)
            # 创建一个新的下载线程
            thread = threading.Thread(target=download, args=(item,), daemon=True)
            thread.start()  # 启动线程
            threads.append(thread)  # 将线程添加到线程列表

        # 移除已完成的线程
        threads = [t for t in threads if t.is_alive()]
        time.sleep(1)  # 每秒检查一次线程列表


if __name__ == "__main__":
    # 全局变量，用于指示程序是否应该停止
    stop_event = threading.Event()

    video_list = [("霸王别姬", "xxxxx"), ("白与黑", "yyyyy"), ("心灵捕手", "zzzz")]

    # 启动键盘监听线程
    keyboard_thread = threading.Thread(target=keyboard_listener)
    keyboard_thread.start()

    # 管理和执行工作线程
    manage_threads(video_list)

    # 等待键盘监听线程结束
    keyboard_thread.join()
    print("程序结束。")
```



#### yield单线程执行多任务

> * 并行：4核cpu，2个任务，每个任务占1个核，连续执行。真多任务
> * 并发：4核cpu，20个任务，每个任务，交替执行。假多任务

```python
import time

def Consumer():
    c_said = '我要下单'   # c_said 客户反馈
    c_order = 100   # c_order 订单数量
    while True:
        c_num = yield c_said,c_order   # c_num 客户收到的数量
        print('[Consumer] Consuming %s...' % c_num)
        time.sleep(1)
        if c_num < 500:
            c_said = f'{c_num} is OK'
            c_order += 100
        else:
            c_said = 'Stop Producing'

def Producer(consumer):
    p_heard,p_order = next(consumer)   # p_heard, p_order 厂家收到的反馈和订单数量
    while p_heard != 'Stop Producing':
        print('[Producer] Producing %s...' % p_order)
        p_heard,p_order = consumer.send(p_order)
        print('[Producer] Consumer said: %s' % p_heard)
    consumer.close()

if __name__=='__main__':
    consumer = Consumer()
    Producer(consumer)
```

> 注意到 `consumer` 函数是一个 `generator`（生成器），把一个 `consumer` 对象传入 `Producer` 后：
>
> 1. `Producer` 首先启动生成器 `p_heard,p_order = next(consumer)`
>
> 2. `consumer` 对象开始执行初始化
>
>    `c_said = '我要下单'`，`c_order = 100`
>
> 3. `consumer` 对象将初始化结果通过 `c_num = yield c_said,c_order` 传递给 `Producer`
>
> 4. `Producer` 通过 `p_heard,p_order = next(consumer)` 接收到客户反馈`c_said`和客户订单`c_order`
>
> 5. `Producer` 判断客户反馈不是 `'Stop Producing'` 后按照客户订单开始生产
>
> 6. `Producer` 将商品通过 `p_heard,p_order = consumer.send(p_order)` 卖给 `consumer`
>
> 7. `consumer` 通过 `c_num = yield c_said,c_order` 拿到商品，消费商品，睡1秒
>
> 8. `consumer` 判断接收的产品数量不到500时，给出客户反馈`c_said = f'{c_num} is OK'`，然后增加订单数量 `c_order += 100`
>
> 9. `consumer` 通过 `c_num = yield c_said,c_order` 将客户反馈传递给 `Producer`
>
> 10. `Producer` 通过 `p_heard,p_order = consumer.send(p_order)` 拿到客户反馈和订单数量
>
> 11. 重复第 5，6，7，8，9步骤
>
> 12. 第5步 `Producer` 判断客户反馈是 `'Stop Producing'` 后就会停止生产，然后，通过 `consumer.close()` 关闭 `consumer`，整个生产消费链结束

#### 下载B站视频

```python
import os
video_list = [
    'https://www.bilibili.com/video/av73941955/',
    'https://www.bilibili.com/video/av73950240/'
]
cmd = 'you-get --playlist '
acount = 0   # 下载失败后的重试次数
# 改变当前工作目录到指定的路径
os.chdir('/Users/sai/Downloads')
for i in video_list:
    flag = True
    while flag:
        flag = False
        var = os.system(cmd+i)
        print(f'执行码是：{var}')
        if var == 256:   # 下载成功返回0，失败返回256
            flag = True
            acount = acount + 1
            if acount == 5:
                break
```

#### 批量修改文件名

* 将文件夹“普心”内的所有文件改名成“普心1”，“普心2”，“普心3”

  ```python
  # 将文件重命名成目录 + 序号
  import os
  g = os.walk('/Users/sai/Desktop/《静秋姐姐手把手教你做运营》')
  
  # os.walk()产生3-元组 (dirpath, dirnames,folder_names)【文件夹路径, 文件夹名字, 文件名】
  for path, dir_list, file_list in g:
      # 去除系统文件.DS_Store
      if '.DS_Store' in file_list:
          file_list.remove('.DS_Store')
      if file_list:
          # 文件排序，保证原始文件名从小到大
          file_list.sort()
          folder_name = path.split('/')[-1]
          num = 1
          for f_name in file_list:
              # 利用 os.path.join() 拼接成完整文件名
              old_name = os.path.join(path, f_name)
              # 扩展名
              suffix = '.' + f_name.split('.')[-1]
              new_name = os.path.join(path, folder_name + '-' + str(num) + suffix)
              os.rename(old_name, new_name)
              num = num + 1
  ```

* 将Downie下载的B站视频，文件夹“普心”内的所有文件按照demo.txt重命名

  * demo.txt中的文件名由Xpath获得

  <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200727001137.png" style="zoom:50%;" />

  ```python
  import os
  g = os.walk('/Users/sai/Downloads/认知心理学（全14讲）')
  
  with open('/Users/sai/Downloads/认知心理学（全14讲）/demo.txt', 'r', encoding="utf-8") as f:
      lines = f.readlines()  # 读取所有行
  
  # os.walk()产生3-元组 (dirpath, dirnames,folder_names)【文件夹路径, 文件夹名字, 文件名】
  for path, dir_list, file_list in g:
      file_list.remove('demo.txt')
   # 去除系统文件.DS_Store
      if '.DS_Store' in file_list:
          file_list.remove('.DS_Store')
      if file_list:
          # 文件排序，保证原始文件名从小到大
          file_list.sort()
          folder_name = path.split('/')[-1]
          for f_name in file_list:
              # 利用 os.path.join() 拼接成完整文件名
              old_name = os.path.join(path, f_name)
              # 扩展名
              suffix = '.' + f_name.split('.')[-1]
              # 比对文件名列表，与列表一致时进行替换名称
              for line in lines:
                  new_name = os.path.join(path, line.replace('\n', '') + suffix)
                  # os.rename(old_name, new_name)
                  print(f'旧名称：{old_name}')
                  print(f'新名称：{new_name}')
                  lines.remove(line)  # 匹配成功后从列表删除
                  break  # break跳出整个for循环，continue跳出本次循环
  ```

  ```python
  import os
  
  address = input('(喜马拉雅重命名)输入要处理的目录：')
  file_address = address + '/demo.txt'
  g = os.walk(address)
  
  with open(file_address, 'r', encoding="utf-8") as f:
      lines = f.readlines()  # 读取所有行
  
  # os.walk()产生3-元组 (dirpath, dirnames,folder_names)【文件夹路径, 文件夹名字, 文件名】
  for path, dir_list, file_list in g:
   # 去除系统文件.DS_Store
      if 'demo.txt' in file_list:
          file_list.remove('demo.txt')
      if file_list:
          folder_name = path.split('/')[-1]
          for f_name in file_list:
           # 利用 os.path.join() 拼接成完整文件名
              old_name = os.path.join(path, f_name)
              # 扩展名
              suffix = '.' + f_name.split('.')[-1]
              # 比对文件名列表，与列表一致时进行替换名称
              for line in lines:
                  # 判断如文件名“01-序言\n” = “序言.mp3”
                  if line.replace('\n', '')[3:] == f_name.replace('.mp3', ''):
                      new_name = os.path.join(path, line.replace('\n', '') + suffix)
                      os.rename(old_name, new_name)
                      lines.remove(line)  # 匹配成功后从列表删除
                      break  # break跳出整个for循环，continue跳出本次循环
  
  ```

##### 批量修改文件时间 - 文件按时间排序

```python
import os
path = '/Users/sai/Desktop/tmp/怎样成为解决问题的高手'
# 获取目录下所有文件名
g = os.walk(path)
cmd = 'touch -m '

# os.walk()产生3-元组 (dirpath, dirnames,folder_names)【文件夹路径, 文件夹名字, 文件名】
for path, dir_list, file_list in g:
    # 跳转进入该目录
    os.chdir(path)
    print(f'当前目录：{path}')
    if file_list:
        # 文件排序，保证原始文件名从小到大。默认sort(reverse = False)升序，reverse = True降序
        file_list.sort(reverse = True)
        for f_name in file_list:
            f_name = "'" + f_name + "'"
            var = os.system(cmd + f_name)
            print(f'执行命令：{cmd + f_name}')
            print(f'执行码：{var}')
```

##### BNU抢研究间

```python
import requests,datetime,time

jscookie = 0

def Login(url, user):
    LoginHeaders = {
    "Accept": "application/json, text/javascript, */*; q=0.01",
    "Referer": "http://219.224.28.56/ClientWeb/xcus/ic2/Default.aspx",
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
    "Content-Type": "application/x-www-form-urlencoded; charset=UTF-8",
    }

    LoginReq = requests.post(url, data=user, headers=LoginHeaders)
    print(LoginReq.status_code)
    print(LoginReq.text)
    global jscookie
    jscookie = "ASP.NET_SessionId="+requests.utils.dict_from_cookiejar(LoginReq.cookies)['ASP.NET_SessionId']

def POST(url, t):
    PostHeaders = {
        "Host": "219.224.28.56",
        "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.90 Safari/537.36",
        "Accept": "application/json, text/javascript, */*; q=0.01",
        "Accept-Language": "zh-CN,zh;q=0.9,en-US;q=0.8,en;q=0.7,zh-TW;q=0.6",
        "Accept-Encoding": "gzip, deflate",
        "Referer": "http://219.224.28.56/ClientWeb/xcus/ic2/Default.aspx",
        "Connection": "keep-alive",
        "Cookie": jscookie
        }
    datas = {
        'dev_id':'766',  # 770是419研究间
        'lab_id':'131',
        'kind_id':'1257',
        'type':'dev',
        'start':'0000-00-00 00:00',
        'end':'0000-00-00 00:00',
        'act':'set_resv'
        }
    datas['start'] = t['start']
    datas['end'] = t['end']
    PostReq = requests.post(url,data=datas,headers=PostHeaders)
    print(PostReq.status_code)
    print(PostReq.text)    

if __name__ == '__main__':
    LoginUrl = "http://219.224.28.56/ClientWeb/pro/ajax/login.aspx"
    PostUrl = "http://219.224.28.56/ClientWeb/pro/ajax/reserve.aspx"
    users = [{
        'id':'201928061039',  # 罗云
        'pwd':'107726',
        'act':'login'
        },{
        'id':'201928061051',  # 雁飞
        'pwd':'418042',
        'act':'login'
        },{
        'id':'201928061041',  # 聪聪
        'pwd':'133725',
        'act':'login'
        },{
        'id':'201928061027',  # 李强
        'pwd':'056712',
        'act':'login'
        },{
        'id':'201928061011',  # 志行
        'pwd':'725001',
        'act':'login'
        },{
        'id':'201922100093',  # 琪琪
        'pwd':'314225',
        'act':'login'
        }
        ]
    tomorrow = (datetime.datetime.now()+datetime.timedelta(days=1)).strftime('%Y-%m-%d')
    times = [{
        'start':tomorrow+' 10:00',
        'end':tomorrow+' 14:00'
    },{
        'start':tomorrow+' 14:00',
        'end':tomorrow+' 18:00'
    },{
        'start':tomorrow+' 18:00',
        'end':tomorrow+' 21:30'
    }
    ]

    while True:
        # 判断此时是否夜里零点零分
        if(datetime.datetime.now().strftime('%H:%M') == '00:00'):
            for user in users:
                Login(LoginUrl, user)
                for t in times:
                    POST(PostUrl, t)
        time.sleep(20)
```

##### 修改文件名中的汉字数字

```python
import os

# 数字
num_collection = ["一", "二", "两", "三", "四", "五", "六", "七", "八", "九", "十"]
# 数字单位进制
num_units = ["零", "百", "千", "万", "亿"]
# 汉字与数字的对应关系
num_dict = {
    "零": 0,
    "一": 1,
    "二": 2,
    "两": 2,
    "三": 3,
    "四": 4,
    "五": 5,
    "六": 6,
    "七": 7,
    "八": 8,
    "九": 9,
    "十": 10,
    "百": 100,
    "千": 1000,
    "万": 10000,
    "亿": 100000000,
}


# 1.从文本中提取数字
def GetChNumber(OriginalStr):
    # 初始化变量
    finalStr = ""  # 最终文本
    CurrentIsNum = False  # 有无汉字数字
    CurrentNum = ""  # 中文数字

    lenStr = len(OriginalStr)  # 文本长度
    for index in range(lenStr):  # 从原文本逐个取字符
        if OriginalStr[index] in num_collection:  # 判断第index个字符是数字
            CurrentNum = CurrentNum + OriginalStr[index]  # 拼接中文数字
            if not CurrentIsNum:
                CurrentIsNum = True
        else:
            if CurrentIsNum:
                if OriginalStr[index] in num_units:  # 判断第index个字符是否数字单位进制
                    CurrentNum = CurrentNum + OriginalStr[index]
                    continue  # 结束本次for循环，进入下一个index
                else:  # 若原字符串包含非数字
                    numResult = str(ChToDigit(CurrentNum))  # 中文数字转阿拉伯数字
                    # 重新初始化
                    CurrentIsNum = False
                    CurrentNum = ""
                    finalStr = finalStr + numResult
            finalStr = finalStr + OriginalStr[index]
    # 若原字符串全是数字
    if len(CurrentNum) > 0:
        numResult = ChToDigit(CurrentNum)
        finalStr = finalStr + str(numResult)
    return finalStr


def ChToDigit(CurrentNum):
    total = 0
    r = 1  # 表示单位：个十百千...
    for i in range(len(CurrentNum) - 1, -1, -1):
        val = num_dict.get(CurrentNum[i])
        if val >= 10 and i == 0:  # 应对 十三 十四 十*之类
            if val > r:
                r = val
                total = total + val
            else:
                r = r * val
                # total =total + r * x
        elif val >= 10:
            if val > r:
                r = val
            else:
                r = r * val
        else:
            total = total + r * val
    return total


def main():
    Dir = input("输入要转换的路径: ")
    # os.walk()产生3-元组 (dirpath, dirnames,folder_names)【文件夹路径, 文件夹名字, 文件名】
    g = os.walk(Dir)

    for path, dir_list, file_list in g:
        # 去除系统文件.DS_Store
        if ".DS_Store" in file_list:
            file_list.remove(".DS_Store")
        if file_list:
            # 文件排序，保证原始文件名从小到大
            file_list.sort()
            folder_name = path.split("/")[-1]
            for f_name in file_list:
                # 利用 os.path.join() 拼接成完整文件名
                old_name = os.path.join(path, f_name)
                f_name = GetChNumber(f_name)
                new_name = os.path.join(path, f_name)
                os.rename(old_name, new_name)


if __name__ == "__main__":
    main()
```

> ```python
> # 数字
> num_collection = ['一', '二', '两', '三', '四', '五', '六', '七', '八', '九', '十']
> # 数字单位进制
> num_units = ['零', '百', '千', '万', '亿']
> # 汉字与数字的对应关系
> num_dict = {
>     '零': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000
> }
> 
> #1.从文本中提取数字
> def GetChNumber(OriginalStr):
>     # 初始化变量
>     finalStr = ''  # 最终文本
>     CurrentIsNum = False  # 有无汉字数字
>     CurrentNum = ''  # 中文数字
> 
>     lenStr = len(OriginalStr)  # 文本长度
>     for index in range(lenStr):  # 从原文本逐个取字符
>         if OriginalStr[index] in num_collection:  # 判断第index个字符是数字
>             CurrentNum = CurrentNum + OriginalStr[index]  # 拼接中文数字
>             if not CurrentIsNum:
>                 CurrentIsNum = True
>         else:
>             if CurrentIsNum:
>                 if OriginalStr[index] in num_units:  # 判断第index个字符是否数字单位进制
>                     CurrentNum = CurrentNum + OriginalStr[index]
>                     continue  # 结束本次for循环，进入下一个index
>                 else:  # 若原字符串包含非数字
>                     numResult = str(ChToDigit(CurrentNum))  # 中文数字转阿拉伯数字
>                     # 重新初始化
>                     CurrentIsNum = False
>                     CurrentNum = ''
>                     finalStr = finalStr + numResult
>             finalStr = finalStr + OriginalStr[index]
>     # 若原字符串全是数字
>     if len(CurrentNum) > 0:
>         numResult = ChToDigit(CurrentNum)
>         finalStr = finalStr + str(numResult)
>     return finalStr
> 
> def ChToDigit(CurrentNum):
>     total = 0
>     r = 1  # 表示单位：个十百千...
>     for i in range(len(CurrentNum) - 1, -1, -1):
>         val = num_dict.get(CurrentNum[i])
>         if val >= 10 and i == 0:  # 应对 十三 十四 十*之类
>             if val > r:
>                 r = val
>                 total = total + val
>             else:
>                 r = r * val
>                 # total =total + r * x
>         elif val >= 10:
>             if val > r:
>                 r = val
>             else:
>                 r = r * val
>         else:
>             total = total + r * val
>     return total
> 
> testStr = [
>     '两百三十二',
>     '我有两百三十二块钱',
>     '今天天气真不错',
>     '百分之八十 discount rate很高了',
>     '我的一百件商品have quality',
>     '找一找我的收藏夹里，有没有一个眼镜',
> ]
> 
> for tstr in testStr:
>     print(tstr + ' = ' + GetChNumber(tstr))
> ```

#### [ffmpeg用法](https://zhuanlan.zhihu.com/p/67878761)

#### [windows安装](https://blog.csdn.net/m0_46278037/article/details/113790540)

#### 1. 下载BNU畅课平台视频流m3u8中的ts视频片段

> 1. 网站后台把视频切片成数百个`xx.ts`文件，一般10秒一个，每个几百kb
> 2. 浏览器通过`xx.m3u8`播放列表把这些`ts`文件连接起来
>
> [原教程](https://blog.csdn.net/weixin_33739627/article/details/88595353)

1. 分析

   1. 通过`Chrome DevTool`的`Network`栏，能看到加载过程

   2. 直接点击`m3u8`播放列表文件，在旁边的`preview`栏查看其内容

      ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200307101507.png)

      1. `master.m3u8`文件存放的是`index-v1-a1.m3u8`文件的地址
      2. `index-v1-a1.m3u8`才是播放列表文件
      3. 播放列表展示了397个`ts`文件

2. 思路

   * 下载所有`ts`切片文件，然后合成一个完整视频

3. 步骤

   1. `Network`栏点击`index-v1-a1.m3u8`，右侧`Headers`栏，`General`的`Request URL`

   2. `Request URL`: `http://lmsmedia.bnu.edu.cn/hls/http/lms.bnu.edu.cn/api/uploads/videos/4569/vod/index-v1-a1.m3u8`

   3. 使用`ffmpeg`下载`index-v1-a1.m3u8`播放列表中所有的视频，然后直接合并成一个完整视频

      `ffmpeg -i 'http://lmsmedia.bnu.edu.cn/hls/http/lms.bnu.edu.cn/api/uploads/videos/4569/vod/index-v1-a1.m3u8' -c copy OUTPUT.mp4`

#### 2. 下载加密视频流m3u8中的ts视频片段

> [延伸学习](https://www.jianshu.com/p/802074a62a42)

1. 分析

   ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200330194309.png)

2. 下载

   > 直接下载报错`Protocol 'http' not on whitelist 'file,crypto'!`

   1. 方法1：使用包含加密信息的完整m3u8链接

      `ffmpeg -i 'http://media.learn.baidu.com/v1/kanbaidu/v/26cc8826-9009-4ba6-96c9-26545f96e251/b2ccfd03-c2d3-4d84-9842-7bbb8f121029/camera_out_low.m3u8?authorization=bce-auth-v1%2xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx' -c copy 视频名.mp4`

   2. 方法2：使用参数忽略加密报错`-protocol_whitelist "file,http,https,tcp,tls"`

      1. 下载m3u8到本地：`camera_out_high.m3u8`
      2. `ffmpeg -protocol_whitelist "file,http,https,tcp,tls" -i 'camera_out_low.m3u8'  -c copy OUTPUT.mp4`

#### 3. 截取视频

```bash
# 第1种方法：截取第6分钟15秒 - 第11分钟25秒之间的视频，共截取时长为5分10秒的片段
# 特点：分割精准，但可能采不到关键帧，开头出现黑屏
ffmpeg -i input.mp4 -ss 00:06:15 -to 00:11:25 -c copy output1.mp4

# 第2种方法，截取第6分钟15秒 - 第11分钟25秒之间的视频，共截取时长为5分10秒的片段
# 特点：分割不够精准，但开头没有黑屏
ffmpeg -ss 00:06:15 -to 00:11:25 -accurate_seek -i input.mp4 -codec copy -avoid_negative_ts 1 output2.mp4

# 第3种方法，从第6分钟15秒开始，共截取时长为2分25秒的片段
# 特点：没有黑屏
ffmpeg -ss 00:06:15 -i input.mp4 -to 00:02:25 -vcodec copy -acodec copy -y output3.mp4
```

#### 4. 合并视频

1. 创建一个文本文件`filelist.txt`

   ```bash
   file 'input1.mkv'
   file 'input2.mkv'
   file 'input3.mkv'
   ```

2. 命令

   ```bash
   ffmpeg -f concat -i filelist.txt -c copy output.mkv
   ```

#### 5. 下载微博视频

![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200501092000.png)

```bash
ffmpeg -i http://f.video.weibocdn.com/fRBCoWqdlx07CcXsFP0Q01041204RKRm0E020.mp4\?label\=mp4_720p\&template\=960x540.25.0\&trans_finger\=11ccc9c970f47cffd9369c72510b3033\&Expires\=1588298484\&ssig\=KiTVMxQF%2F8\&KID\=unistore,video -c copy OUTPUT.mp4
```

#### 6. 视频转换格式

1. 视频转视频

   ```bash
   ffmpeg -i video.mp4 video.avi
   
   #如果想维持源视频文件的质量，使用 -qscale 0 参数
   ffmpeg -i video.mp4 -qscale 0 video.avi
   ```

2. 视频转音频

   ```bash
   ffmpeg -i input.mp4 -vn output.mp3
   ```

#### 7. 修改视频分辨率

```bash
#查看视频流信息
ffmpeg -i input.mp4

#将分辨转成640×480
ffmpeg -i input.mp4 -s 640x480 -c:a copy output.mp4
```

#### 8. 降低分辨率

```bash
# 采用H.264视频压缩算法，
ffmpeg -i input.mp4 -c:v libx264 -crf 24 output.mp4

# 采用H.264视频压缩算法和AAC音频压缩算法，视频帧率10fps，音频码率32k
ffmpeg -i input.mp4 -vcodec libx264 -crf 20 output.mp4

# （首选）对它降低fps和音频码率的方法大大压缩文件大小，而清晰度不变
ffmpeg -i input.mp4 -r 10 -b:a 32k output.mp4
```

#### 下载荔枝音频

<img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200729012642.png" style="zoom:50%;" />

















