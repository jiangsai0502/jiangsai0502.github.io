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

> 给无序文件名添加序号，如
>
> 墓志铭.mp3    ---->>>>    01-墓志铭.mp3
> 前言.mp3    ---->>>>    02-前言.mp3
>
> ```python
> import os
> g = os.walk('/Users/sai/Desktop/tmp/深度思维')
> 
> with open('/Users/sai/Desktop/tmp/demo.txt', 'r', encoding="utf-8") as f:
>     lines = f.readlines()  # 读取所有行
> 
> # os.walk()产生3-元组 (dirpath, dirnames,folder_names)【文件夹路径, 文件夹名字, 文件名】
> for path, dir_list, file_list in g:
>     # 去除系统文件.DS_Store
>     if '.DS_Store' in file_list:
>         file_list.remove('.DS_Store')
>     if file_list:
>         # 文件排序，保证原始文件名从小到大
>         file_list.sort()
>         folder_name = path.split('/')[-1]
>         for f_name in file_list:
>             # 利用 os.path.join() 拼接成完整文件名
>             old_name = os.path.join(path, f_name)
>             # 扩展名
>             suffix = '.' + f_name.split('.')[-1]
>             # 比对文件名列表，与列表一致时进行替换名称
>             for line in lines:
>                 # 判断如文件名“01-序言\n” = “序言.mp3”
>                 if line.replace('\n', '')[3:] == f_name.replace('.mp3', ''):
>                     new_name = os.path.join(path,
>                                             line.replace('\n', '') + suffix)
>                     os.rename(old_name, new_name)
>                     lines.remove(line)  # 匹配成功后从列表删除
>                     break  # break跳出整个for循环，continue跳出本次循环
> ```



##### 修改文件名中的汉字数字

```python
# 数字
num_collection = ['一', '二', '两', '三', '四', '五', '六', '七', '八', '九', '十']
# 数字单位进制
num_units = ['零', '百', '千', '万', '亿']
# 汉字与数字的对应关系
num_dict = {
    '零': 0, '一': 1, '二': 2, '两': 2, '三': 3, '四': 4, '五': 5, '六': 6, '七': 7, '八': 8, '九': 9, '十': 10, '百': 100, '千': 1000, '万': 10000, '亿': 100000000
}

#1.从文本中提取数字
def GetChNumber(OriginalStr):
    # 初始化变量
    finalStr = ''  # 最终文本
    CurrentIsNum = False  # 有无汉字数字
    CurrentNum = ''  # 中文数字

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
                    CurrentNum = ''
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

import os
g = os.walk('/Users/sai/Desktop/tmp')

# os.walk()产生3-元组 (dirpath, dirnames,folder_names)【文件夹路径, 文件夹名字, 文件名】
for path, dir_list, file_list in g:
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
            f_name = GetChNumber(f_name)
            new_name = os.path.join(path, f_name)
            os.rename(old_name, new_name)
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

### [ffmpeg用法](https://zhuanlan.zhihu.com/p/67878761)

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

      `ffmpeg -i http://lmsmedia.bnu.edu.cn/hls/http/lms.bnu.edu.cn/api/uploads/videos/4569/vod/index-v1-a1.m3u8 -c copy OUTPUT.mp4`

#### 2. 下载加密视频流m3u8中的ts视频片段

> [延伸学习](https://www.jianshu.com/p/802074a62a42)

1. 分析

   ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200330194309.png)

2. 下载

   > 直接下载报错`Protocol 'http' not on whitelist 'file,crypto'!`

   1. 方法1：使用包含加密信息的完整m3u8链接

      `ffmpeg -i http://media.learn.baidu.com/v1/kanbaidu/v/26cc8826-9009-4ba6-96c9-26545f96e251/b2ccfd03-c2d3-4d84-9842-7bbb8f121029/camera_out_low.m3u8?authorization=bce-auth-v1%2xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx -c copy 视频名.mp4`

   2. 方法2：使用参数忽略加密报错`-protocol_whitelist "file,http,https,tcp,tls"`

      1. 下载m3u8到本地：`camera_out_high.m3u8`
      2. `ffmpeg -protocol_whitelist "file,http,https,tcp,tls" -i camera_out_low.m3u8  -c copy OUTPUT.mp4`

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



#### 获取知乎问题答案并转换为MarkDown文件

[参考](https://www.jianshu.com/p/59028353d0aa)

> 知乎接口`https://www.zhihu.com/api/v4/questions/{}/answers?include=data[*].content,voteup_count,created_time&offset=0&limit=20&sort_by=default`

```python
# pip install html2text
# pip install bs4
# pip install lxml

from multiprocessing import Pool
import re, os, html2text, requests, json, time
from requests import RequestException
from bs4 import BeautifulSoup

headers = {
    'User-Agent':
    'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.84 Safari/537.36',
    'authorization': 'oauth c3cef7c66a1843f8b3a9e6a1e3160e20',
}


def html_template(data):
    # api content
    html = '''
            <html>
            <head>
            <body>
            %s
            </body>
            </head>
            </html>
            ''' % data
    return html


def request(url):
    try:
        response = requests.get(url=url, headers=headers)
        if response.status_code == 200:
            # 不管是不是最后一条数据, 先进行解析再说
            text = response.text
            # 此处进行进一步解析
            # print('url =', url, 'text =', text)
            content = json.loads(text)
            parse_content(content)
            # 如果不是最后一条数据, 继续递归请求并解析
            if not content.get('paging').get('is_end'):
                # next_page_url = content.get('paging').get('next').replace('http', 'https')
                next_page_url = content.get('paging').get('next')
                request(next_page_url)

        return None
    except RequestException:
        print(RequestException)
        return None


def parse_content(content):
    if 'data' in content.keys():
        for data in content.get('data'):
            parsed_data = parse_data(data)
            transform_to_markdown(parsed_data)


def parse_data(content):
    data = {}
    answer_content = content.get('content')

    author_name = content.get('author').get('name')
    print('author_name =', author_name)
    answer_id = content.get('id')
    question_id = content.get('question').get('id')
    question_title = content.get('question').get('title')
    vote_up_count = content.get('voteup_count')

    content = html_template(answer_content)
    soup = BeautifulSoup(content, 'lxml')
    answer = soup.find("body")

    soup.body.extract()
    soup.head.insert_after(soup.new_tag("body", **{'class': 'zhi'}))

    soup.body.append(answer)

    img_list = soup.find_all("img", class_="content_image lazy")
    for img in img_list:
        img["src"] = img["data-actualsrc"]
    img_list = soup.find_all("img",
                             class_="origin_image zh-lightbox-thumb lazy")
    for img in img_list:
        img["src"] = img["data-actualsrc"]
    noscript_list = soup.find_all("noscript")
    for noscript in noscript_list:
        noscript.extract()

    data['content'] = soup
    data['author_name'] = author_name
    data['answer_id'] = answer_id
    data['question_id'] = question_id
    data['question_title'] = question_title
    data['vote_up_count'] = vote_up_count
    return data


def transform_to_markdown(data):
    content = data['content']
    author_name = data['author_name']
    answer_id = data['answer_id']
    question_id = data['question_id']
    question_title = data['question_title']
    vote_up_count = data['vote_up_count']

    file_name = f'{question_title}.md'
    answer_path = os.path.join(os.getcwd(), file_name)

    with open(answer_path, 'a+', encoding='utf-8') as f:
        origin_url = 'https://www.zhihu.com/question/{}/answer/{}'.format(
            question_id, answer_id)
        f.write("-" * 40 + "\n")
        f.write("##### Author_Name: " + author_name + "\n")
        f.write("##### VoteCount: %s" % vote_up_count + "\n")
        text = html2text.html2text(content.decode('utf-8'))
        # 标题
        r = re.findall(r'\*\*(.*?)\*\*', text, re.S)
        for i in r:
            if i != " ":
                text = text.replace(i, i.strip())

        r = re.findall(r'_(.*)_', text)
        for i in r:
            if i != " ":
                text = text.replace(i, i.strip())
        text = text.replace('_ _', '')
        text = text.replace('_b.', '_r.')
        # 图片
        r = re.findall(r'!\[\]\((?:.*?)\)', text)
        for i in r:
            text = text.replace(i, i + "\n\n")
            folder_name = f'{os.getcwd()}/{question_title}_img'
            if not os.path.exists(folder_name):
                os.mkdir(folder_name)
            img_url = re.findall('\((.*)\)', i)[0]
            save_name = img_url.split('/')[-1]
            file_path = '%s/%s' % (folder_name, save_name)

            try:
                content = download_image(img_url)
                if content:
                    save_image(content, file_path)
            except Exception as e:
                print(e)
            else:  # if no exception,get here
                text = text.replace(img_url, file_path)

        f.write(text)
        f.close()


def download_image(url):
    print('正在下载图片', url)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return response.content
    except RequestException:
        print('请求图片错误', url)
        pass


def save_image(content, file_path):
    with open(file_path, 'wb') as f:
        f.write(content)
        f.close()


if __name__ == '__main__':
    # todo 这里的header可能需要加cookie了, 因为有的作者名不加cookie拿不到真名, 只能得到一个叫做"知乎用户"的作者名,
    # 真实的作者名给隐藏了

    os.chdir('/Users/sai/Desktop/tmp/zhihu')  # 切换当前目录
    question_id = '20926054'  # 知乎问题'https://www.zhihu.com/question/37400041'

    url_format = 'https://www.zhihu.com/api/v4/questions/{}/answers?include=data[*].content,voteup_count,created_time&offset=0&limit=20&sort_by=default'
    url = url_format.format(question_id)
    request(url)
```

