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

##### 1. 写操作，写入时覆盖原文

```python
# 自动关闭文件
with open('/Users/jiangsai02/Documents/Temp/test.csv', 'w', encoding="gbk", newline='') as OpenCSV:
    CSVwriter = csv.writer(OpenCSV)
    CSVwriter.writerow([value1, value2, value3])
```

> 1. Windows默认编码是gbk，如果用utf-8，excel打开可能会乱码
> 2. newline='' 是为了让writer自动添加的换行符和文件的不重复，防止出现跳行的情况
> 3. 每行写入 1 个 list

##### 2. 读操作

```python
# 自动关闭文件
with open('/Users/jiangsai02/Documents/Temp/test.csv', 'r', encoding="gbk") as OpenCSV:
    CSVreader = csv.reader(OpenCSV)
    for row in reader:
        print(row)
```

> 1. 读取的编码要和写入的保持一致，写入时是 "gbk" ，读取时也要 "gbk"
> 2. 每次读 1 行

##### 3. 项目模块

```python
import csv

# bigData 是 List，data 是 Dictionary
def WriteToCSV(bigData):
    with open('/Users/jiangsai02/Documents/Temp/test.csv', 'w', encoding="gbk", newline='') as OpenCSV:
        CSVwriter = csv.writer(OpenCSV)
        CSVwriter.writerow(list(bigData[0].keys()))
        for data in bigData:
            CSVwriter.writerow(list(data.values()))
```



### 读写 Excel

##### 1. 安装 openpyxl

> 1. 切换到虚拟环境： `source activate jspython3`
>2. 安装openpyxl   ： `pip install openpyxl`

##### 2. 写操作，写入时覆盖原文

```python
MyWB = Workbook()
MyWS = MyWB.active
MyWS.append(["第1行第1列", "第1行第2列", "第1行第3列"])
MyWB.save('test.xlsx')
```

> 1. 每行写入 1 个 list

#####  3. 读操作

```python
MyWB = load_workbook('test.xlsx')
print(MyWB.get_sheet_names())
MyWS = MyWB.get_sheet_by_name("TempData")
print(MyWS['B2'].value)
```

> 1. 获取指定单元格的值  `MyWS['B2'].value`
>
> 2. 按行取值
>
>    1. 按行获取所有值
>
>       ```python
>       for row in MyWS.rows:
>           for cell in row:
>               print(f'{cell.value}', end=' ')
>       ```
>
>    2. 获取指定行的值
>
>       ```python
>       for cell in MyWS[3]:
>           print(f'{cell.value}', end=' ')
>       ```
>
> 3. 按列取值
>
>    1. 按列获取所有值
>
>       ```python
>       for column in MyWS.columns:
>           for cell in column:
>               print(f'{cell.value}', end=' ')
>       ```
>
>    2. 获取指定列的值
>
>       ```python
>       for cell in MyWS['B']:
>           print(f'{cell.value}', end=' ')
>       ```
>
> 4. 获取切片范围的单元格
>
>    ```python
>    for row in MyWS['A1':'C2']:
>        for cell in row:
>            print(f'{cell.value}', end=' ')
>    ```

##### 项目模块

```python
from openpyxl import Workbook, load_workbook

# bigData 是 List，data 是 Dictionary
def WriteToExcel(bigData):
    MyWB = Workbook()
    MyWS = MyWB.active
    MyWS.title = "TempData"
    # 将 bigData 的第一个 data 字典的键设置为 Excel 第 1 行的表头
    MyWS.append(list(bigData[0].keys()))
    for data in bigData:
        MyWS.append(list(data.values()))
    MyWB.save('/Users/jiangsai02/Documents/Temp/test.xlsx')
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



### 进度条

##### 1. 安装 tqdm

> 1. 切换到虚拟环境： `source activate jspython3`
> 2. 安装openpyxl   ： `pip install tqdm`

##### 2. 用法

```python
from tqdm import tqdm
import time
 
for i in tqdm(range(30)):
    time.sleep(0.1)
```



### 多线程

```python
import time, random, threading
from tqdm import tqdm
from queue import Queue

# 线程池
threads = []
# 线程数
threads_num = 3

# 让线程一直从队列获取消息，一直等待一直获取，直至等到结束信号，就退出
def a():
    while True:
        # Queue().get()的作用是阻塞队列直到获得消息
        num = test_queue.get()
        if num is 'signal_exit':
            break

        print(f'随机数是{num}的开始时间是{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}')
        for i in tqdm(range(num)):
            time.sleep(1)
        print(f'随机数是{num}的结束时间是{time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())}')
        
        test_queue.task_done()

if __name__ == '__main__':
    test_queue = Queue()
    numlist = [4,5,6,7,8,9,10]
    for i in numlist:
        test_queue.put(i)

    # 启动线程，并将线程对象 放入列表保存
    for i in range(threads_num):
        # target从队列里取任务去执行
        mythread = threading.Thread(target=a)
        mythread.start()
        threads.append(mythread)

    # 阻塞队列，直到队列被清空
    test_queue.join()
    # 向队列发送多个退出信号
    for i in range(threads_num):
         test_queue.put('signal_exit')

    # 阻塞队列，直到所有线程退出
    for t in threads:
        t.join()
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



### 下载B站视频

```python
import os
video_list = [
    'https://www.bilibili.com/video/av73941955/',
    'https://www.bilibili.com/video/av73950240/'
]
cmd = 'you-get --playlist '
acount = 0   # 下载失败后的重试次数
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



### 下载BNU畅课平台视频流m3u8中的ts视频片段

> 1. 网站后台把视频切片成数百个`xx.ts`文件，一般10秒一个，每个几百kb
> 2. 浏览器通过`xx.m3u8`播放列表把这些`ts`文件连接起来
>
> [原教程](https://blog.csdn.net/weixin_33739627/article/details/88595353)

#### 分析

1. 通过`Chrome DevTool`的`Network`栏，能看到加载过程

2. 直接点击`m3u8`播放列表文件，在旁边的`preview`栏查看其内容

   ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200307101507.png)

   1. `master.m3u8`文件存放的是`index-v1-a1.m3u8`文件的地址
   2. `index-v1-a1.m3u8`才是播放列表文件
   3. 播放列表展示了397个`ts`文件

#### 思路

* 下载所有`ts`切片文件，然后合成一个完整视频

#### 步骤

1. `Network`栏点击`index-v1-a1.m3u8`，右侧`Headers`栏，`General`的`Request URL`

2. `Request URL`: `http://lmsmedia.bnu.edu.cn/hls/http/lms.bnu.edu.cn/api/uploads/videos/4569/vod/index-v1-a1.m3u8`

3. 使用`ffmpeg`下载`index-v1-a1.m3u8`播放列表中所有的视频，然后直接合并成一个完整视频

   `ffmpeg -i http://lmsmedia.bnu.edu.cn/hls/http/lms.bnu.edu.cn/api/uploads/videos/4569/vod/index-v1-a1.m3u8 -c copy OUTPUT.mp4`

   ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200307103820.png)

[延伸学习](https://www.jianshu.com/p/802074a62a42)




