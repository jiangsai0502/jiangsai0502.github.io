# 杂记

#### final cut Pro 用法
1. 导出方式
> 文件 - 共享 - Apple 设备 1080P - 设置
> 修改2个地方
> 1. 格式：电脑
> 2. 完成时：什么都不做



#### VS Code 

1. 批量注释/取消注释 ：`command` + `/`
2. 调整编辑界面和终端字体大小：`command` + `-`，`command` + `+`



#### 将任务转移到后台运行

> 场景描述：运行 `docsify serve` ，前台一直运行这个命令，终端被占据

> 解决方案：`ctrl + z` 暂停进程，`bg` 把它丢到后台去运行

* `jobs -l` 显示所有后台任务的 `Job号job_num`  和 `进程号pid_num` 

  > 终端显示格式：[Job号]   进程号   Job状态   Job的启动命令
  >
  > [1]  - 64981 running    ydoc serve
  > [2]  + 67089 suspended (signal)  docsify serve

1. `ctrl + z`，將前台任务丟到后台，并处于中暂停状态

   > 终端显示：[2]  + 67089 suspended  docsify serve

2. `bg %job_num`，让在后台暂停的进程在后台继续运行

   > `bg %2`
   >
   > 终端显示：[2]  - 67089 continued  docsify serve

   （命令 `kill -cont pid_num`  功能一样）

3. `kill -stop %job_num` ，将后台运行的运行的进程暂停住

   > `kill -stop 64981`
   >
   > 终端显示：[1]  + 64981 suspended (signal)  ydoc serve

   （命令 `kill -stop pid_num` 功能一样）

4. `kill %job_num`，杀掉后台进程

   （命令`kill pid_num` 也可以）

5. `command &`，命令前面加`&`，启动任务时就让任务去后台运行

   > `docsify serve &`
   >
   > 终端显示：[1] 96071
   >
   > `jobs -l`
   >
   > 终端显示：[1]  + 96071 running    docsify serve

#### 删除指定程序的进程

如Google Chrome：`pkill Google Chrome`



#### chrome 书签&插件同步不及时

**手动强制同步**

1. 架梯子
2. 地址栏输入：chrome://sync-internals
3. 中间那列中下方，点击“Stop Sync (Keep Data)”，之后点击“Request Start”
4. 两个设备上的Chrome都进行一次这个操作



#### 获取IP

1. 局域网IP：`ifconfig en0 | grep 'inet' | grep -vE 'inet6'`

   <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200330111301.png" align='left' style="zoom:33%;" />

2. 外网IP：`curl 'http://httpbin.org/get' -s | grep 'origin'`



#### 简单HTTP服务器

1. 进入共享目录

2. 后台启动HTTP服务：`python -m http.server 8000 &`

3. 获取局域网IP：`ifconfig en0 | grep 'inet' | grep -vE 'inet6'`

   <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200330111301.png" align='left' style="zoom:33%;" />

4. Ipad浏览器访问：`http://192.168.1.5:8000`

   <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200330112119.png" style="zoom:33%;" />
   
5. 局域网共享Axure原型

   1. Axure生成html文件到：/Users/sai/Documents/Axure

      ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210701144312.png)

   2. 在html文件所在目录启动web服务

   3. 访问：http://192.168.0.166:8000/m站.html

#### nplayer不显示视频信息直接播放

<img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200512171934.png" style="zoom:53%;" />



#### ScreenFlow 变速

1. 双击那个视频，改变 Speed 

   ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200324174710.png)
   
   



#### Mac录制鼠标键盘动作

1. MurGaa Recoder

#### Mac txt乱码问题

1. cd [文件所在目录]

2. iconv -c -f GB2312 -t UTF-8 [你要看的文件] >> [新文件的名称]

   ```bash
   iconv -c -f GB2312 -t UTF-8 凡人修仙转.txt >> 凡人修仙转2.txt
   //GB2312是常用中文编码，其他还有gbk等，UTF-8是mac能够识别的编码
   ```

#### Mac 终端翻页

1. 回车向下翻一行
2. 空格向下翻一页

#### 字符串转成驼峰式

* `print('INT NOT NULL UNIQUE PRIMARY KEY AUTO_INCREMENT'.title())`

#### Mac 删除文件和文件夹的命令

1. `rm -rf 目录名字`

   * -r 就是向下递归，不管有多少级目录，一并删除
   * -f 就是直接强行删除，不作任何提示的意思

   > linux没有回收站的，rm删除不会进入废纸篓



#### 查看网站自动填充的密码

* input标签，密码字段，即type="password"，输入不可见，右键检查该元素，修改其type属性为text即可见

  > ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200430102333.png)



#### 自定义PPT工具栏

> ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200523232610.png)



#### Mac莫名奇妙自动重启

1. 关闭安全性与隐私，高级，“不活跃后退出登录”

   <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200712215643.png" style="zoom:50%;" />

2. 关闭 `autopoweroff` 

   ```bash
   pmset -g
   
   # 输出
   λ sai [~/Downloads] → pmset -g
   System-wide power settings:
   Currently in use:
    lidwake              1
    autopoweroff         1
    standbydelayhigh     86400
    autopoweroffdelay    28800
    standbydelaylow      10800
    
   # 关闭 autopoweroff
   sudo pmset -a autopoweroff 0
   ```


#### MacBook 突然没有声音

```python
sudo killall coreaudiod
```



#### Applescript入门

```bash
# tell指明脚本要控制的程序对象
tell current application
	
	# 变量赋值
	set str to "World"
	# 字符串展示
	display dialog "Hello " & str
	
	set temp to 5
	
	# 流程语句
	if temp < 3 then
		# 整型转字符型
		display dialog (temp as text) & " < 3"
	else if temp > 4 then
		display dialog (temp as text) & " > 4"
	end if
	
	# 条件循环
	repeat until temp < 4
		display dialog "until条件循环中 temp is " & (temp as text)
		set temp to temp - 1
	end repeat
	
	repeat while temp > 2
		display dialog "while条件循环中 temp is " & (temp as text)
		set temp to temp - 1
	end repeat
	
	# 限定次数循环，3次
	repeat 3 times
		display dialog "限定次数循环中 temp is " & (temp as text)
	end repeat
end tell
```

##### QQ截图OCR

![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200807111739.png)

![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200807113607.png)

##### QQ截图录屏转gif



##### Ubuntu安装到U盘

![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200808164137.png)

##### Win10安装到U盘 - Windows To Go

[视频参考](https://www.youtube.com/watch?v=8CCGPEiD7Vw) [文字参考](https://sspai.com/post/44699)



####  word表格插入行快捷键

1. 表格最后一行插入行：光标定位到表格末尾，按**Tab**即可
2. 表格中间一行插入行：光标定位到中间一行，按**Enter**即可



#### Excel vlookup用法

* [参考1](https://zhuanlan.zhihu.com/p/29161495)，[参考2](https://zhidao.baidu.com/question/1734379668253114707.html)

* **坑**：公式：VLOOKUP(D1,A$1:B$9,2,0)，要加上绝对引用符号 $，否则会匹配出问题

#### Excel 正态分布画图

* [参考](https://www.bilibili.com/video/BV1Hi4y1L7Eg)
* ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20201230204751.png)

#### Excel生成随机数

* RAND()：产生0到1之间的随机小数
* RANDBETWEEN(A,B)：产生A到B之间的随机整数

1. 随机生成0~1的小数：RAND()
2. 随机生成0~20的小数：20*RAND()
3. 随机生成30~50的小数：30+(50-30)*RAND()
4. 随机生成30~50的整数：RANDBETWEEN(30,50)
5. 随机生成1~5000的含3为小数的数：RANDBETWEEN(1,4999)+RANDBETWEEN(1,1000)/1000
6. 随机生成均值为250，标准差为100的正态分布数据：NORMINV(RAND(),250,100)
7. 取正数：ABS()
8. 取整数：INT()

#### 大陆苹果ID变为美国苹果账号

[参考](https://zhuanlan.zhihu.com/p/138058796)

#### 下载微信公众号文章的语音

![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210222210825.png)

##### Mac 163邮箱：添加邮箱 无法验证账户或密码

1. [开启pop3](https://blog.csdn.net/weixin_44203158/article/details/108652460)
2. 开启IMAP

##### 批量清理iPhone通讯录

1. iPhone - 设置 - iCloud - 通讯录 - 关闭 - “从我的iPhone删除”
2. PC登录iCloud - 通讯录 - command + 单击选择 - 左下角设置 - 删除



##### FinePrint 双面打印

![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210619100110.png)

> 打印机：Microsoft Print to PDF
>
> 订口：8mm



#### [预览拼接图片](https://www.jianshu.com/p/d2cab29e6c0c)

1. 获取空白面白：随便打开个图片，全选，删除
2. 设置面板大小：工具调整大小 - 去掉“比例缩放” - 宽度50、高度50
3. 导入素材：**截图**可粘贴进来；**本地图片**可用预览打开后全选粘贴进来
4. 移动整个素材：点击选中素材，拖动
5. 移动部分素材：框选，剪切，再粘贴，拖动

#### [iphone接力失败](https://blog.newnius.com/apple-handoff-cross-device-paste-not-work.html)

1. 在iPhone上打开记事本，Mac上也会同时出现记事本的标记，接力可用了



#### Axure中使用iconfont

1. 扎到icon后，下载 - 复制SVG代码 - 到Axure中粘贴

   ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210629200737.png)



#### PDF里的图片文字不清晰

1. Mac预览app打开pdf

2. 菜单中选择文件→导出，Quartz滤镜选取“亮度减少”选项

   使用一次后，对比度会明显增加。如果还不清楚，可连续操作。

   ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210703235411.png)