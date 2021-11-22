# 杂记

#### final cut Pro 用法

1. 导出方式

> 文件 - 共享 - Apple 设备 1080P - 设置
> 修改2个地方
>
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

#### Excel数值判断大小并添加颜色

1. 选中待判断的单元格
2. 开始-条件格式-突出显示单元格规则

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

#### PDF里的图片文字不清晰

1. Mac预览app打开pdf

2. 菜单中选择文件→导出，Quartz滤镜选取“亮度减少”选项

   使用一次后，对比度会明显增加。如果还不清楚，可连续操作。

   ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210703235411.png)



#### Axure小技巧

1. 方案设计流程

   1. 需求分析：背景、目标
   2. 核心功能流程图：不是全部功能都画，只花核心
      1. 先手画流程草稿
      2. 再drawio绘制
   3. 页面架构图：所有页面的上下级关系
      1. 先手画架构草稿
      2. 再Axure顶层页面，右键”生成流程图“
   4. 页面布局设计：每个页面的展示
      1. 先手画页面布局
      2. 再Axure绘制
   5. 交互原型：每个页面的交互
      1. Axure绘制

2. 常用设置

   | 设置自己喜欢的颜色                                           | 顶部快捷栏                                                   |
   | ------------------------------------------------------------ | ------------------------------------------------------------ |
   | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210707165106.png) | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210707123014.png) |

   | 画布设置网格                                                 | Axure中使用iconfont                                          |
   | ------------------------------------------------------------ | ------------------------------------------------------------ |
   | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210707170155.png) | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210629200737.png) |

   | 发布Axure到手机                                              |                                                              |
   | ------------------------------------------------------------ | ------------------------------------------------------------ |
   | 1. 原型尺寸：375 x 812：可去掉iPhone x/11/12顶端状态栏，设为**375 x 768** <br />2. 共享 - 登录Axure云：jiangsai0502@gmail.com - js1122334<br />3. 手机打开发布链接 | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210707184808.png) |

3. 修改画布背景色：Page - style - 填充 - 改为灰色

4. 调整图片大小：样式 -      位置和尺寸 - 锁定宽高比 - w：640

5. 标尺：按住鼠标，从左/上往下拽；空白处框选标尺即可delete

6. 调整图片偏转角度

   1. 样式 - 位置和尺寸：手动输入调整旋转角度
   2. 按住command，鼠标移到图形某个角，旋转

7. 居中：A移到B的中间，先选B再选A，居中

8. 水平/垂直移动原件：按住shift，移动原件

9. 复制元件：按住option，拖动图形

10. 恢复默认工具摆放：视图 - 重置视图

11. 母版：将多个页面公用的组件设为母版可以方便修改

12. 事件添加条件：新建交互 - 选择动作 - 鼠标回到交互主界面 - 鼠标再移动到动作即可看到**启动情形**

13. 动态面板功能

    1. [tab切换](http://www.woshipm.com/rp/4186275.html)
       1. 拖入1个动态面板；增加3个状态，分别命名为衣服、手机、电脑；双击进入每个状态，设置不同的展示
       2. 拖入3个按钮；给按钮增加交互：单击时 - 设置面板状态 - 选择上述面板 - 选择状态、选择动画、选择时间
    2. [滚动效果](https://blog.csdn.net/hst_gogogo/article/details/91350504)
       1. 拖入**1个动态面板**，命名为**第1层面板**，**第1层状态**
       2. 向**第1层状态**中再拖入**1个动态面板**，**尺寸**与第1层面板一致，命名为**第2层面板**，**第2层状态**
       3. 向**第2层状态**中拖入要展示的**内容组件**
       4. 将**第2层面板**右键设置为：滚动条 - 垂直滚动
       5. 拖动**第2层面板**的右边框，拖到超过**第1层面板**的尺寸，完成
    3. [App键盘弹出](https://www.bilibili.com/read/cv10174226)
    4. [保持固定位置](https://www.axureshop.com/qa/25/)：把需要固定位置的内容转换为动态面板

14. 创建自己的元件库

15. 案例

    | 1. 鼠标悬浮在湖南时，湖南下拉框展开，而湖北和江西的下拉框收起 | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210709214734.png) |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | 用变量实现<br /><br />0. willFlag初始值设为0<br />1.若willFlag为0，则隐藏菜单，并将willFlag设为1<br />2.若willFlag为1，则隐藏菜单，并将willFlag设为0<br /> | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210709224621.png) |

    | 【垂直菜单】鼠标悬停变色                                     |                                                              |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | 1. 随便选择一个【垂直菜单】中的菜单<br />2. 交互配置区最下方**交互样式**<br />3. 添加类似“鼠标悬停”的交互样式 - 鼠标悬停样式 - 更多样式选项 - 勾选“填充色” - 选个色 - 确定 | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210709000736.png) |

    | 【垂直菜单】一对一联动                                       |                                                              |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | 1. 下拉框1：Name<br />2. 下拉框2：Rank<br />3. 思路<br /><1>.选项改变时<br />①.若Name的选项为某值，则Rank切换到指定选项 | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210717225632.png) |

    | 【垂直菜单】一对多联动                                       |                                                              |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | 1. 下拉框1：Province<br />2. 下拉框2：Citys<br />3. 思路<br /><1>.下拉框Citys转换为动态面板，1个状态的下拉框设为1个省的n个城市<br />选项改变时<br /> | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210710002626.png) |

    

    | 倒计时                                                       |                                                              |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | **点击按钮开始倒计时**<br /><br />1. 按钮Start：开始<br />2. 矩形框NumBoarder：显示数字<br />3. 全局变量Counter：修改数字<br />4. 动态面板Switcher：设2个状态，用转态切换控住数字改变<br />5. 思路：<br />    <1>.点击Start<br />    <2>.Switcher切换状态<br />    <3>.当Switcher状态改变时<br />        ①NumBoarder显示Counter<br />        ②Counter自减1<br />        ③等待1秒<br />        ④Switcher切换状态<br />        ⑤触发事件”当Switcher状态改变时“ | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210717133247.png) |
    | **页面载入开始倒计时**<br /><br />1. 矩形框NumBoarder：显示数字<br />2. 全局变量Counter：修改数字<br />3. 思路：<br />    <1>.当元件载入时<br />        ①.NumBoarder显示Counter<br />        ②.Counter自减1<br />       ③.等待1秒<br />       ④触发事件”当元件载入时“ | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210717124529.png) |

    | 登录                                                         | 元件闪烁                                                     |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210717232640.png) | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210717235459.png) |
    | 拨动开关                                                     | 滑动幻灯片                                                   |
    | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210718144243.png) | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210718145029.png) |

    

16. [Photoshop任意角度旋转图片](https://jingyan.baidu.com/article/6f2f55a15b7bd3b5b93e6c89.html)

    | 标尺工具                                                     | 图像--图像旋转--任意角度                                     |
    | ------------------------------------------------------------ | ------------------------------------------------------------ |
    | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210812184958.png) | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210812185049.png) |

    

    

    1. 

