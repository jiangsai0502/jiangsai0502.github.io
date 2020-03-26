# Ajax 动态网页

### 浏览器渲染引擎原理

> 浏览器向服务器发送请求，得到服务器返回的资源文件后，需要经过**渲染引擎**的处理，将资源文件显示在浏览器窗口中

**渲染流程**

> 解析 html 来构建 Dom树 -> 构建 render树 -> 布局 render树 -> 绘制 render树

1. 渲染引擎解析 html，将标签转化为 Dom树的节点

   1. 解析中若遇到 js，则会启用另外的连接进行下载

      > 下载过程中 Dom 树的构建**不会停止**

   2. js 下载完成后立即执行，直到 Dom 树构建完成

      > 执行过程中会阻塞浏览器的其他行为，因为 js 的运行可能会改变 Dom树的结构，为了不让刚构建好的 Dom树又被 js 改变，聪明的浏览器停止了 Dom树的构建

2. 渲染引擎解析外部 css文件和 style标签中的样式信息

   1. css 和 style 样式信息以及 html 中的可见性指令将被用来构建另一棵树—— render树

      > 其实这一步是和上一步同时进行的，为了页面显示更迅速，css 不会等到 Dom树构建完毕才开始构建 render树

   2. render树由一些包含颜色和大小等属性的矩形组成

3. 渲染引擎布局 render树的每个节点在屏幕上的确切坐标

4. 渲染引擎绘制 render树，即遍历 render树，并使用UI后端层绘制每个节点



**Javascript的加载和执行特点**

1. 载入后马上执行

2. 执行时会阻塞页面后续的内容，包括页面渲染和其它资源的下载

   > 因为浏览器需要一个稳定的 DOM树结构，而 JS中很可能有代码会直接改变 DOM树结构，浏览器为了防止出现 JS修改 DOM树，需要重新构建DOM树的情况，就选择直接阻塞其他的下载和呈现



**动态网页加载和解析过程**

1. 输入网址，浏览器向服务器发出请求，服务器返回 html文件
2. 浏览器载入 html代码，发现＜head＞标签内有一个＜link＞标签引用外部 CSS文件
3. 浏览器向服务器请求这个CSS文件，同时继续载入 html中＜body＞部分
4. 浏览器收到 CSS文件，开始渲染页面
5. 浏览器在＜body＞中发现一个＜img＞标签引用了一张图片
6. 浏览器向服务器请求这个图片，同时继续渲染后面的代码
7. 浏览器收到这个图片，由于图片占了一定面积，影响了后面的排布，因此浏览器需要回过头来重新渲染这部分代码
8. 浏览器发现了一个包含一行 Javascript代码的＜script＞标签，赶快运行它
9. Javascript脚本执行了这条语句，命令浏览器隐藏掉代码中的某个＜div＞（style.display=”none”）
10. 突然少了这么一个元素，浏览器不得不重新渲染这部分代码
11. 终于等到了＜/html＞的到来，浏览器泪流满面……
12. 等等，还没完，用户点了 “换肤” 按钮，Javascript让浏览器换了一下＜link＞标签的CSS路径
13. 浏览器召集了在座的各位＜div＞＜span＞＜ul＞＜li＞们，“大伙儿收拾收拾行李，咱得重新来过……”，浏览器向服务器请求了新的CSS文件，重新渲染页面



**定位不到元素的原因**

1. 没有加等待

   * 原因：代码运行速度远快于浏览器加载渲染速度

   * 思路：加入延迟给浏览器加载 js数据

2. 源码有frame

   * frame类似于在主html 的基础上又嵌套一个或多个子html，而且嵌套的子html是独立使用，互不影响



### 抓取动态网页视频

1. **分析网页代码**

   * "检查" 元素发现视频链接是 

     `https://boot-video.xuexi.cn/video/1012/p/de0eab9c9ba30c75bc8574f91188d252-bfd35263f6b446aa8eba38c3cf996c44-2.mp4`

   * 但是网页源码却没有，说明这是 js 后期动态加载的信息

   * "检查" -> "network" -> 重新加载 -> "ctr+f" -> 搜索这个视频链接发现这个信息在 `2457151200699439109.js`

   * 下载这个 js 文件

2. **分析 js 文件**

   * 把 js 文件内容装载到 json 中，把数据转成标准的字典，方便后期提取
   * json 只能接受字典格式，但是这个 js 文件里的字典内容被 'callback()' 包裹住了，所以用**切片方式**去掉外层的字符串 'callback()'
   * 字典元素 sub_items 存放就是视频信息，但 key值为 'url' 和 'js_url' 只在第 1 个视频信息中有，所以中间加了一层判断

   ```python
   import requests, json
   
   def GetJsonDict(url):
       fake_headers = {
       'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.79 Safari/537.36'
       }
       response = requests.get(url, headers=fake_headers)
       html = response.content.decode('utf-8')
       JsonDict = json.loads(html[9:-1])
       return JsonDict
   
   def GetVideosList(JsonDict):
       VideosList = []
       for item in JsonDict['sub_items']:
           VideoInfo = {}
           VideoInfo['title'] = item['pcsite_info']['title']
           VideoInfo['videos'] = item['videos'][0]['video_storage_info'][0]['normal']
           VideosList.append(VideoInfo)
       return VideosList
   
   if __name__ == '__main__':
       url = 'https://article.xuexi.cn/data/app/15757223571164471700.js'
       JsonDict = GetJsonDict(url)
       videos_dict = GetVideosList(JsonDict)
       print(videos_dict[0:2])
   ```

   







