### 爬虫3板斧

1. 数据抓取 `Fetch_Data(url)`

2. 数据解析 `Parse_Data(html)`

3. 数据存储 `Process_Data(Data)`

   > 解析的目的：将网页里非结构化的数据解析成结构化数据，方便从新组织
   >
   > 规范：不管多大或多小的代码量，都要封装成这3部分



### crul入门

1. 用法

   | 参数 | 描述                        | 示例                                                         |
   | ---- | --------------------------- | ------------------------------------------------------------ |
   | `-A` | 设置`User-Agent`            |                                                              |
   | `-X` | 指定`GET`，`POST`请求       | `curl -X POST http://httpbin.org/post`<br>`curl -X GET http://httpbin.org/get` |
   | `-I` | 只返回请求头信息            | `curl -I http://httpbin.org/get`                             |
   | `-d` | 将参数以`POST`请求传递给url | `curl -d 'a=1&b=2&c=3' http://httpbin.org/post` <br>`curl -d @tempArgs.json http://httpbin.org/post` <br>传递json文件里的参数（文件里的参数必须是这种格式a=1&b=2&c=3） |
   | `-O` | 以远程文件名下载文件        | `curl -O http://httpbin.org/image/png`                       |
   | `-o` | 以指定文件名下载文件        | `curl -o a.png http://httpbin.org/image/png`                 |
   | `-k` | 运行发起不安全的SSL请求     | `curl -k https://www.12306.cn`                               |
   | `-b` | 发起带cookie的请求          | `curl -b a=1 http://httpbin.org/cookies`                     |

   

### wget入门

1. **安装环境**：`brew install wget`

2. **用法**

   | 参数              | 描述                               | 示例                                                         |
   | ----------------- | ---------------------------------- | ------------------------------------------------------------ |
   | 无参数            | 以远程文件名下载文件               | `wget http://httpbin.org/image/png`                          |
   | `-O`              | 以指定文件名下载文件               | `wget -O sai.png http://httpbin.org/image/png`               |
   | `--limit-rate=1k` | 限速下载                           | `wget -O sai.jpeg --limit-rate=10k http://httpbin.org/image/jpeg` |
   | `-c`              | 断点续传                           | `wget -c http://httpbin.org/image/png`                       |
   | `-b`              | 后台下载                           | `wget -b http://httpbin.org/image/png` <br>`tail -f wget-log` 实时刷新日志信息<br/>`control+c` 退出日志信息 |
   | `-U`              | 指定`User-Agent`                   |                                                              |
   | `-p`              | 下载所有为了html页面显示正常的文件 |                                                              |
   | `--convert-links` | 下载后，转换成本地的链接           | `wget -c --mirror -U 'Mozilla' -p --convert-links https://requests.readthedocs.io/en/master/` |
   | `--mirror`        | 镜像目标网站                       | `wget -c --mirror -U 'Mozilla' -p --convert-links https://httpie.org/doc` |
   | `-i`              | 下载文件内的链接                   | `wget -i filelist.txt`                                       |

   备注：

   > 1. `python`内建的`web服务器`可启动mirror下来的`镜像网站`
   >
   >    `python -m http.server`
   >
   >    启动服务后，根据提示访问`0.0.0.1:8000`
   >
   >    > `http.server` 自动启动当前目录的index.html

   

### Requests入门

1. **安装环境**

   1. 切换到 `py3` 虚拟环境：`source activate py3`
   2. 查看当前环境是否已包含 `requests` 模块：`conda list`
   3. 安装 `requests` 模块：`pip install requests`

2. **用法**

   ```python
   import requests
   
   # Get请求，无参数
   res = requests.get('http://httpbin.org/get')
   print(res.status_code,res.reason)
   print(res.text)
   
   # Get请求，有参数
   res = requests.get('http://httpbin.org/get',params={'x':1,'y':2})
   print(res.json())
   
   # Post请求
   res = requests.post('http://httpbin.org/post',{'a':1,'b':2})
   print(res.json())
   
   # 自定义headers
   myheaders = {'User-Agent':'sai user agent'}
   res = requests.get('http://httpbin.org/headers',headers=myheaders)
   print(res.json())
   
   # 带cookies的请求
   mycookies = dict(myid='sai',mytoken='abcdefg')
   res = requests.get('http://httpbin.org/cookies',cookies=mycookies)
   print(res.json())
   
   # Basic-auth请求
   res = requests.get('http://httpbin.org/basic-auth/sai/1122334',auth=('sai','1122334'))
   print(res.json())
   
   # 主动抛出状态码异常
   bad_res = requests.get('http://httpbin.org/status/404')
   print(bad_res.status_code)
   try:
       bad_res.raise_for_status()
   except requests.exceptions.HTTPError as e:
       print(e)
   
   # 设置等待时间
   # http://httpbin.org/delay/2 表示网站2秒后相应
   res = requests.get('http://httpbin.org/delay/2',timeout=3)
   print(res.json())
   res = requests.get('http://httpbin.org/delay/2',timeout=2)
   print(res.json())
   
   # Session对象请求
   my_ses = requests.Session()
   # Session对象my_ses会保存服务器返回的set-cookies头信息的内容
   my_ses.get('http://httpbin.org/cookies/set/myname/sai')
   my_ses.get('http://httpbin.org/cookies/set/mypassword/1122334')
   # 下次请求会将本地所有的cookies信息自动添加到请求头中
   res = my_ses.get('http://httpbin.org/cookies')
   print(res.json())
   
   # 代理IP
   free_proxies = {
       'http': 'http://112.248.11.140:9999',
       'https': 'https://112.248.11.140:9999'
   }
   
   ss_proxies = {
       'http': 'http://127.0.0.1:1087',
       'https': 'https://127.0.0.1:1087'
   }
   
   fake_headers = {
       'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36',
       }
   
   url = 'http://httpbin.org/ip'
   res = requests.get(url=url, headers=fake_headers)
   print(f'本地IP是{res.json()}')
   try:
       proxies_res = requests.get(url = url, headers = fake_headers, proxies = ss_proxies, timeout = 15)
       html = proxies_res.content.decode('utf-8')
       print(f'代理IP是{proxies_res.json()}')
   except:
       print("代理IP无效")
   ```

   > * 关于代理IP
   >
   >   1. proxies 必须是个字典
   >
   >      1. key 只能有 2 个值：http 和 https
   >
   >   2. 格式
   >
   >      1. http 只能对应 http 协议的代理
   >      2. Https 只能对应 https 协议的代理
   >
   >   3. IP 后面跟 端口号 port
   >
   >   4. `http://httpbin.org/ip` 是个测试 IP 的网站
   >
   >   5. 使用本地 shadowsocks
   >
   >      > <img src="https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/20200209180738.png" style="zoom:30%;" />



### 解析器对比

| 解析器        | 速度 | 难度 |
| ------------- | ---- | ---- |
| re            | 最快 | 最难 |
| xpath         | 快   | 适中 |
| BeautifulSoup | 慢   | 简单 |



### BeautifulSoup 入门

1. 安装环境

   1. 切换到 `py3` 虚拟环境：`source activate py3`
   2. 查看当前环境是否已包含 `beautifulsoup4` 模块：`conda list`
   3. 安装 `beautifulsoup4` 模块：`pip install beautifulsoup4`
   
2. 第一个 `BeautifulSoup` 示例

   ```python
   from bs4 import BeautifulSoup
   
   html_doc = """
   <html><head><title>The Dormouse's story</title></head>
   <body>
   <p class="title"><b>The Dormouse's story</b><b>Another story</b></p>
   <p class="story" test-name="value1 value2">Once upon a time there were three little sisters; and their names were
   <a href="http://xxx/elsie" class="sister" id="link1">Elsie</a>
   <a class="sister" type="funny" id="link2">Lacie</a>
   <p class="story two">
   <a class="bro" id="link3">Andy</a>
   <a class="bro" id="link4">Jack</a>
   </p>
   """
   
   soup = BeautifulSoup(html_doc, 'lxml')
   # 把HTML源码用解释器html.parser格式化一下
   ```

   * BeautifulSoup 将 HTML 转成标签树，标签树的每个节点都是 Python 的对象

   * BeautifulSoup 基本元素

     1. Tag：即标签，最基本的信息组织单元，分别用 <> 和 </> 标明开头和结尾
  2. Comment：即标签内字符串的注释部分，一种特殊的 Comment 类型
     3. Name：获取标签的名字，\<p>...\</p> 的名字是 'p'
        * 用法：\<tag>.name
     4. Attributes：获取标签的属性，字典的形式组织。
        * 用法：\<tag>.attrs
     5. NavigableString：获取标签内非属性字符串，<>...</> 中的字符串。
        * 用法：\<tag>.string

   * **获取节点的常用方法**

     1. **find()** 和 **find_all()**

        find() 是 find_all() 获取 List 中的第一个元素，两者用法完全一样

        * soup.find('a')
       * 获取源码中第一个 \<a>...\</a> 标签内容对象
        * soup.find('a', id='next')
          * 获取源码中第一个有属性为 id，值为 next 的 \<a> 对象，比如\<a id="next">...\</a>
        * soup.find('a', id='next', class_ = 'next', xx='yyy')
          * find() 参数可以有多个
        * **注1**：**class** 属性因为是 Python 关键字，不能直接使用，要用 **class_** 进行代替，如soup.find('a', class_ = 'next')
        * **注2**：返回值数量很大时，可用 **limit** 参数限制返回值数量，soup.find('a', class_ = 'next', limit = 2)
   
     2. **多值属性**

        * \<p class="story two">  属性值  **value1 value2**  被**空格**隔开

          `soup.find("p", class_= ["story", "two"])`

          `soup.find("p", class_= "story two")`   也可以

          `soup.select(".story.two")`

        * \<div test-name = "value1 value2">  属性名  **test-name**  被**横杠**隔开，横杠是不被识别的

          `soup.find('div', attrs={'test-name':'value1 value2'})`

          `soup.find('div', {'test-name':'value1 value2'})`   可省略字典前面的  `attrs=`

     3. **select()**

        通过css选择器的select()来定位，获取 List

        * 通过**标签名**找所有节点

          `soup.select('p')`

        * 通过**类的值**查找所有节点，**格式：类的值前面加点  '.'**

          * **单值属性**，即类的值没被空格隔开

            \<p class="story" test-name="value1 value2">

            `soup.select(".story")`

          * **多值属性**，即类的值被空格隔开

            \<p class="story two">

            `soup.select(".story.two")`

        * 通过 **id的值** 查找所有节点，**格式：id的值前面加  '#'**

          \<a class="sister" type='funny' id="link2">

          `soup.select('#link2')`

        * 通过 **标签名联合一个属性** 精确查找节点，**格式：标签名[属性]，中间没有空格**

          \<a class="sister" type='funny' id="link2">

          `items = soup.select('a[class="sister"]')`

          `items = soup.select('a[type="funny"]')`

          `items = soup.select('a[id="link2"]')`
     
        ```python
        soup.getText() = # 获取全文
        
        # soup中的title标签的全部内容
        soup.title = <title>The Dormouse's story</title>
        
        # soup中的title标签的名字
        soup.title.name = title
        
        # soup中的title标签的文本字符串
        soup.title.string = The Dormouse's story
        
        # soup中的title标签的父节点的名字
        soup.title.parent.name = head
        
        # soup中的第一个p标签的'class'属性的内容
        soup.p["class"] = ['title']
        
        # soup中的第一个a标签的文本
        soup.a.string =  Elsie
        
        # soup中的第一个a标签的文本，与soup.a.string一样
        soup.a.text =  Elsie
        
        # soup中的第一个a标签的字典
        soup.a.attrs =  {'href': 'http://example.com/elsie', 'class': ['sister'], 'id': 'link1'}
        
        # soup中的第一个a标签的字典中key为"href"的值
        soup.a.attrs["href"] =  http://example.com/elsie
        
        # soup中的所有a标签的全部内容的列表
        soup.find_all("a") =  [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" > href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister" href="http://example.com/tillie" > id="link3">Tillie</a>]
        
        # soup中id="link3"所在标签的全部内容
        soup.find(id="link3") =  <a class="sister" href="http://example.com/tillie" id="link3">Tillie</a>
        ```

   * **下行遍历**：从当前节点向子孙节点遍历
   
     * .contents：获取全部儿子节点的全部内容的列表（全部内容包含标签，属性，文本，及子孙节点的标签，属性，文本）
     
     * .children：获取儿子节点的迭代类型，用于遍历
     
     * .descendants：获取子孙节点的迭代类型，用于遍历
       
       * 注：.contents和.children只获得当前节点的下一层节点的信息，而.descendants可获得当前节点后续的所有节点的信息
       
       ```python
       # 获取整个<body>……</body>的全部内容
       print('soup.body = ',soup.body)
       
       # 获取<body>标签的全部儿子节点的全部内容的列表
       print('soup.body.contents = ',soup.body.contents)
       
       # 获取<body>标签的全部儿子节点的内容
       num = 1
       print('soup.body.children = ')
       for child in soup.body.children:
       print("第" + str(num) + "个儿子：" , child)
           num += 1
       
       # 获取<body>标签的全部子孙节点，首先获取第1个儿子节点的全部内容，然后进入第1个儿子节点获取第一个孙子节点，直到没有下级节点后，获取同级的孙子节点及其下级节点，同级遍历结束后返回上级节点
       num = 1
       print('soup.body.descendants = ')
       for descendant in soup.body.descendants:
           print("第" + str(num) + "个子孙：" , descendant)
           num += 1
       ```
     
   * **上行遍历**：从当前节点向父祖节点遍历
   
     * .parent：获取当前节点的**父节点**标签的全部内容（全部内容包含标签，属性，文本，及子孙节点的标签，属性，文本）
     
     * .parents：获取当前节点的**父祖节点**标签的全部内容的迭代类型
     
       ```python
       for parent in soup.a.parents:
           if parent is None:
               print('soup.a.parent = ',parent)
           else:
               print('soup.a.parent.name = ',parent.name)
       ```
     
   * **平行遍历**：同一父节点下的子节点遍历
   
     * .next_sibling：获取同一父节点下的下一个兄弟节点标签
     
     * .previous_sibling：获取同一父节点下的上一个兄弟节点标签
     
     * .next_siblings：迭代类型，获取同一父节点下的所有后续兄弟节点标签
     
       * .previous_siblings：迭代类型，获取同一父节点下的所有前续兄弟节点标签
     
         ```python
         for sibling in soup.a.next_siblings:
             print('soup.a.next_sibling = ',sibling)
         ```
     

#### chrome xpath插件

* XPath Helper

  > 快速验证 xpath **语句对错**和**匹配结果**，**匹配数量**
  >
  > > 最好少用 "检查" 里的 copy xpath，自己写的 xpath 更健壮
  >
  > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/20200215101822.png)
  >
  > 



#### 爬取python的字符串内建函数的描述信息

**分析**

> 1. 获取table第一列的所有链接	
> 2. 遍历所有链接内容的返回值信息

```python
import requests
from lxml import etree

start_url = 'https://www.runoob.com/python/python-strings.html'

# 数据抓取
def Fetch_Data(url):
    res = requests.get(url)
    if res.status_code != 200:
        res.raise_for_status()
    else:
        return res.text.replace('\n','').replace('\r','')
# 数据分析
def Parse_Data(html):
    selector = etree.HTML(html)
    data = {}
    data['语法'] = selector.xpath('//*[@id="content"]/pre/text()')[0]
    data['参数'] = selector.xpath('//*[@id="content"]/ul/li/text()')
    data['返回值'] = selector.xpath('//*[@id="content"]/p[4]/text()')[0]
    return data

# 数据存储
def Process_Data(Datas):
    print(Datas)

if __name__ == '__main__':
    # 1.请求入口
    html = Fetch_Data(start_url)
    selector = etree.HTML(Fetch_Data(start_url))
    # 2.提取列表链接
    links_tail = selector.xpath('//*[@id="content"]/table[5]/tbody/tr/td[1]/p//a/@href')
    link_head = 'https://www.runoob.com/python/'
    Datas =[]
    for link in links_tail[0:5]:
        # 3.提取子页面数据
        sub_html = Fetch_Data(link_head+link)
        # 4.分析子页面数据
        data = Parse_Data(sub_html)
        Datas.append(data)
    # 5.存储数据
    Process_Data(Datas)
```





#### 爬下厨房的主页图片

```python
import requests, os
from bs4 import BeautifulSoup

res = requests.get('https://www.xiachufang.com/')
soup = BeautifulSoup(res.text,'lxml')

imgs = []
# 图片链接在 src 或 data-src 中
for img in soup.select('img'):
    if img.has_attr('data-src'):
        imgs.append(img.attrs['data-src'].split('@')[0])
    else:
        imgs.append(img.attrs['src'].split('@')[0])

# 初始化下载目录
img_dir = os.path.join(os.curdir, 'IMG')
if not os.path.isdir(img_dir):
    os.mkdir(img_dir)

for img in imgs[:4]:
    img_name = img.split('/')[-1]
    img_path = os.path.join(img_dir,img_name)
    print(img_path)
    r = requests.get(img)
    with open(img_path,'wb+') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
```

> * `requests.get(url)`默认是下载在**内存**中的，下载完成才存到硬盘上
>
> * `Response.iter_content`　来边下载边存硬盘

```python
import requests, os
from lxml import etree

res = requests.get('https://www.xiachufang.com/')
tree = etree.HTML(res.text)

# 图片链接在 src 或 data-src 中
src_a = tree.xpath('//img[contains(@src,"http")]/@src')
src_b = tree.xpath('//img[contains(@data-src,"http")]/@data-src')
imgs = []
for img in src_a + src_b:
    imgs.append(img.split('@')[0])

# 初始化下载目录
img_dir = os.path.join(os.curdir, 'IMG')
if not os.path.isdir(img_dir):
    os.mkdir(img_dir)

for img in imgs[:4]:
    img_name = img.split('/')[-1]
    img_path = os.path.join(img_dir,img_name)
    print(img_path)
    r = requests.get(img)
    with open(img_path,'wb+') as f:
        for chunk in r.iter_content(1024):
            f.write(chunk)
```



### Json 入门

1. ***json.dumps()*  数据序列化**

   1. *序列化*  即将 **python对象** 转换成 **JSON对象**，就是在 **python对象**的最外层添加一对 **引号''**，使之变成字符串

   2. 序列化时，中文汉字会被转换为 unicode 码，添加参数 ensure_ascii=False 即可解决

      ```python
      import json
      
      Python_Data1 = ({'id': 1, 'name': '赛'}, True)
      Python_Data2 = {'id': 2, 'intro': ['age',32]}
      Python_Data3 = [{'id': 1, 'name': 'will'}, {'id': 2, 'name': 'sai'}]
      
      Json_Data1 = json.dumps(Python_Data1)
      Json_Data2 = json.dumps(Python_Data2)
      Json_Data3 = json.dumps(Python_Data3)
      Json_Data1_cn = json.dumps(Python_Data1, ensure_ascii=False)
      
      print(f'Json_Data1 数据类型：{type(Json_Data1)} | 数据是：{repr(Json_Data1)}')
      # Json_Data1 数据类型：<class 'str'> | 数据是：'[{"id": 1, "name": "\\u8d5b"}, true]'
      
      print(f'Json_Data2 数据类型：{type(Json_Data2)} | 数据是：{repr(Json_Data2)}')
      # Json_Data2 数据类型：<class 'str'> | 数据是：'{"id": 2, "intro": ["age", 32]}'
      
      print(f'Json_Data3 数据类型：{type(Json_Data3)} | 数据是：{repr(Json_Data3)}')
      # Json_Data3 数据类型：<class 'str'> | 数据是：'[{"id": 1, "name": "will"}, {"id": 2, "name": "sai"}]'
      
      print(f'Json_Data1 数据类型：{type(Json_Data1_cn)} | 数据是：{repr(Json_Data1_cn)}')
      # Json_Data1 数据类型：<class 'str'> | 数据是：'[{"id": 1, "name": "赛"}, true]'
      ```

      > **序列化后，列表类型 List 还是 List，字典类型 Dictionay 还是 Dictionay，但元组类型 Tuple 变成列表类型 List**

2. ***json.loads()*   数据反序列化**

   1. *反序列化* 即将 **JSON对象** 转换成 **python对象**，就是去掉 **JSON对象** 最外层的一对 **引号''** 去掉

      ```python
      Json_Data1 = '{"id": 2, "intro": ["age", 32]}'
      Json_Data2 = '[{"id": 1, "name": "will"}, {"id": 2, "name": "sai"}]'
      
      Python_Data1 = json.loads(Json_Data1)
      Python_Data2 = json.loads(Json_Data2)
      
      print(f'Python_Data1 数据类型：{type(Python_Data1)} | 数据是：{repr(Python_Data1)}')
      # Python_Data1 数据类型：<class 'dict'> | 数据是：{'id': 2, 'intro': ['age', 32]}
      
      print(f'Python_Data2 数据类型：{type(Python_Data2)} | 数据是：{repr(Python_Data2)}')
      # Python_Data2 数据类型：<class 'list'> | 数据是：[{'id': 1, 'name': 'will'}, {'id': 2, 'name': 'sai'}]
      ```

3. **json.dump()  写入文件**

   1. 将 **Python对象** 写入  **Json 文件** 

      ```python
      import json
      
      python_data = ['Apple', 52, ['sai', True], {'sex':'male', 'age': 32}]
      
      with open('/Users/jiangsai02/Documents/Temp/testJson.txt', 'w') as json_file:
          json.dump(python_data, json_file)
      ```

4. **json.load()  读取文件**

   1. 读取 Json 文件

      ```python
      import json
      
      python_data = ['Apple', 52, ['sai', True], {'sex':'male', 'age': 32}]
      
      with open('/Users/jiangsai02/Documents/Temp/testJson.txt', 'r') as json_file:
          result = json.load(json_file)
          print(result)
      ```





### 正则表达式

> 字符串前面加上 r 表示原生不转义的字符串，**不管何时都加上，绝对没错**

| 字符       | 含义                                                       | 举例                                                         |
| ---------- | ---------------------------------------------------------- | ------------------------------------------------------------ |
| **\\**     | 将下一个字符转义成特殊字符                                 | `\n` 是换行符  `\\` 匹配 `\`                                 |
| **^**      | 匹配字符串开头                                             |                                                              |
| **$**      | 匹配字符串结尾                                             |                                                              |
| *****      | 匹配前一个字符或表达式 0 次或 n 次                         | zo* 能匹配 “`z`”，“`zo`”，“`zoo`”                            |
| **+**      | 匹配前一个字符或表达式 1 次或 n 次                         | zo+ 能匹配 “`zo`”，“`zoo`”                                   |
| **?**      | 匹配前一个字符或表达式 0 次或 1 次                         | zo? 能匹配 “`z`”，“`zo`”                                     |
| **.**      | 匹配除换行符 \n 之外的任何字符                             |                                                              |
| **{n}**    | 严格匹配前一个字符 n 次                                    | `o{2}` 能匹配 “`food`” 中的两个 “`o`” , 不能匹配 “`Bob`” 中的 “`o`” |
| **{n,}**   | 至少匹配前一个字符 n 次                                    | `o{2,}` 能匹配 “`food`” 中的两个 “`o`” , 不能匹配 “`Bob`” 中的 “`o`” |
| **x\|y**   | 目标字符**可以是 x** ，**也可以是 y**                      | “`z|food`” 能匹配 “`z`” 或 “`food`”，【因为 x 是 z，y 是 food】，而“`(z|f)ood`” 则匹配 “`zood`” 或 “`food`”，【因为x 是z，y 是 f】 |
| **[xyz]**  | 目标字符**可以 x** ，**也可以是 y** ，**也可以是 z**       | “`[abc]`” 可以匹配 “`plain`” 中的 “`a`”                      |
| **[^xyz]** | 目标字符**不可以 x** ，**也不可以是 y** ，**也不可以是 z** | “`[^abc]`” 可以匹配 “`plain`” 中的 “`p`”                     |
| **[a-z]**  | 目标字符**可以**是 26 个小写字母中的任意一个               |                                                              |
| **[^a-z]** | 目标字符**不可以**是 26 个小写字母中的任意一个             |                                                              |
| **\b**     | 匹配一个单词的结尾                                         | “`er\b`” 能匹配 “`never`” ，但不能匹配 “`verb`” 和 “`era`”   |
| **\B**     | 匹配一个单词的非结尾                                       | “`er\b`” 能匹配 “`verb`” 和 “`era`”，但不能匹配 “`never`”    |
| **\d**     | 匹配任何一个数字字符                                       | 等同于 **[0-9]**                                             |
| **\D**     | 匹配任何一个非数字字符                                     | 等同于 **[^0-9]**                                            |
| **\s**     | 匹配任何空白字符，包括空格、制表符、换页符                 | 等同于 **[\f\n\r\t\v]**                                      |
| **\S**     | 匹配任何非空白字符，包括空格、制表符、换页符               | 等同于 **[^\f\n\r\t\v]**                                     |
| **\w**     | 匹配任何单词字符，包括下划线                               | 等同于 **[A-Za-z0-9_]**                                      |
| **\W**     | 匹配任何非单词字符                                         | 等同于 **[^A-Za-z0-9_]**                                     |



#### 常用方法

1. **re.search( *pattern*, *string* )** 

   按照能够匹配的正则表达式 pattern ，获取**第一个**匹配的结果

   ```python
   result = re.search(r"(\d+), Date: (.+)", "ID: 021523, Date: Feb/12/2017")
   print(result.group())                   # 021523, Date: Feb/12/2017
   print(result.group(1))                  # 021523
   print(result.group(2))                  # Date: Feb/12/2017
   ```

   > 一次使用多个正则时，会匹配出多个结果，可以将多个结果分组管理
   >
   > 1. 分组时每组必须用小括号括起来
   >
   > 2. (\d+) 先去字符串里匹配，结果是
   >
   >    ```python
   >    result = re.search(r"(\d+)", "ID: 021523, Date: Feb/12/2017")
   >    print(result.group())                   # 021523
   >    print(result.group(1))                  # 021523
   >    ```
   >
   > 3. (.+) 之后去字符串里匹配，结果是
   >
   >    ```python
   >    result = re.search(r"Date: (.+)", "ID: 021523, Date: Feb/12/2017")
   >    print(result.group())                   # Date: Feb/12/2017
   >    print(result.group(1))                  # Feb/12/2017
   >    ```

2. **re.findall( *pattern*, *string* )** 

   获取**全部**匹配的结果

   ```python
   print(re.findall(r"r[ua]n", "run ran ren"))    # ['run', 'ran']
   print(re.findall(r"(run|ran)", "run ran ren")) # ['run', 'ran']
   ```

3. **re.sub( *pattern*, *repl*, *old_string* )** 

   按照能够匹配的正则表达式 pattern ，则将 old_string 替换成 repl

   ```python
   print(re.sub(r"rans", "catches", "dog runs to cat"))     # dog runs to cat
   print(re.sub(r"runs", "catches", "dog runs to cat"))     # dog catches to cat
   print(re.sub(r"r[au]ns", "catches", "dog runs to cat"))     # dog catches to cat
   print(re.sub(r"r(a|u)ns", "catches", "dog runs to cat"))    # dog catches to cat
   ```

   > 1. 若能在 "dog runs to cat" 中找到 rans ，则将其替换成 catches
   > 2. 若能在 "dog runs to cat" 中找到 runs ，则将其替换成 catches
   > 3. 若能在 "dog runs to cat" 中找到 rans 或 runs ，则将其替换成 catches

4. **re.split( *pattern*, *old_string* )**

   按照能够匹配的正则表达式 pattern ，则将 old_string 分割成一个 List

   ```python
   print(re.split(r"[,;\.\s]", "a;b,c.d eg"))             # ['a', 'b', 'c', 'd', 'eg']
   ```

   > 1. 按照4个符号： <1> **逗号 ','**  <2>**分号 ';'**  <3>**点号 '.'**  <4>**空格 ' '** ，分割字符串

   

#### 示例分析

1. **IP匹配**

   ```python
   import re
   
   判断数字字符串是否是 IP
   IPs = ['1.1.1.1', '1.11.111.0']
   
   for ip in IPs:
       if re.match(r"^(?:[0-9]{1,3}\.){3}[0-9]{1,3}$", ip):
           print(f"Vaild IP {ip}")
       else:
           print(f"Invaild IP {ip}")
   
   从文本字符串中提取 IP
   string_ip = "apple1.1.1.1 orange2.2.2.2c 3.3.3.3 pineapple"
   result = re.findall(r"(?:[0-9]{1,3}\.){3}[0-9]{1,3}", string_ip)
   if result:
       print(result)
   else:
       print("re cannot find ip")
   ```




1. 

### postman入门







### YAML 语言入门

1. 语法

   > 1. 大小写敏感
   > 2. 缩进表示层级
   > 3. 缩进只允许用空格，不允许 Tab
   > 4. 缩进空格数量不重要，对齐即可

2. 三种数据结构

   * 对象

     > 对象是一组键值对

     | YAML 对象                       | 对应的 Json 对象                        |
     | ------------------------------- | --------------------------------------- |
     | animal : pets                   | { animal: 'pets' }                      |
     | hash: { name: Steve, foo: bar } | { hash: { name: 'Steve', foo: 'bar' } } |

   * 数组

     > 数组是一组连词线开头的行

     | YAML 对象                                     | 对应的 Json 对象                 |
     | --------------------------------------------- | -------------------------------- |
     | - Cat <br/>- Dog <br/>- Goldfish              | [ 'Cat', 'Dog', 'Goldfish' ]     |
     | -<br/>   - Cat<br/>   - Dog<br/>   - Goldfish | [ [ 'Cat', 'Dog', 'Goldfish' ] ] |
     | animal: [Cat, Dog]                            | { animal: [ 'Cat', 'Dog' ] }     |

   * 对象与数组复合类型

     | YAML 对象                                                    | 对应的 Json 对象                                             |
     | ------------------------------------------------------------ | ------------------------------------------------------------ |
     | languages:<br/>  - Ruby<br/>  - Perl<br/>  - Python <br/>websites:<br/>  YAML: yaml.org <br/>  Ruby: ruby-lang.org <br/>  Python: python.org <br/>  Perl: use.perl.org | { languages: [ 'Ruby', 'Perl', 'Python' ],<br/>   websites: <br/>      { YAML: 'yaml.org',<br/>         Ruby: 'ruby-lang.org',<br/>         Python: 'python.org',<br/>         Perl: 'use.perl.org' } } |

   * 纯量

     > 纯量是最基本的、不可再分的值
     >
     > 包括：字符串，布尔值，数值，Null，时间，日期

     | 纯量   | YAML 对象                                                    | 对应的 Json 对象                                    |
     | ------ | ------------------------------------------------------------ | --------------------------------------------------- |
     | 布尔值 | isSet: true                                                  | { isSet: true }                                     |
     | 数值   | number: 12.30                                                | { number: 12.30 }                                   |
     | Null   | parent: ~                                                    | { parent: null }                                    |
     | 时间   | iso8601: 2001-12-14t21:59:43.10-05:00                        | iso8601: new Date('2001-12-14t21:59:43.10-05:00') } |
     | 日期   | date: 1976-07-31                                             | { date: new Date('1976-07-31') }                    |
     | 字符串 | 字符串默认不使用引号<br/>str: 这是一行字符串                 | { str: '这是一行字符串' }                           |
     |        | 字符串中包含空格或特殊字符，要用引号<br/>str: '内容： 字符串' | { str: '内容: 字符串' }                             |
     |        | 单引号和双引号都能用<br/>s1: '内容\n字符串'<br/>s2: "内容\n字符串" | { s1: '内容\\n字符串', s2: '内容\n字符串' }         |
     |        | 字符串可以写成多行，从第二行开始，必须有缩进<br/>str: 这是一段<br/>  多行<br/>  字符串 | { str: '这是一段 多行 字符串' }                     |









