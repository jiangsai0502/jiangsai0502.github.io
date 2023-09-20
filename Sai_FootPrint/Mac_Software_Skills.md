##### chrome 书签&插件同步不及时

> 手动强制同步
>
> 1. 架梯子
> 2. 地址栏输入：chrome://sync-internals
> 3. 中间那列中下方，点击“Stop Sync (Keep Data)”，之后点击“Request Start”
> 4. 两个设备上的Chrome都进行一次这个操作

##### 禁止Chrome更新

> > 背景：使用爬虫工具时，一般会用到chromedriver，必须在Chrome和chromedriver的版本一致时才能正常工作，一旦Chrome更新后就不能正常工作了，而每次Chrome更新也不知道具体更新了个啥
>
> 1. 方法1
>
>    ```
>    1. 关闭 Chrome 浏览器，进入目录 “/Library/Google/GoogleSoftwareUpdate”
>    cd /Library/Google/GoogleSoftwareUpdate
>    2. 删除该目录下的 GoogleSoftwareUpdate.bundle 
>    ```
>
>    > 有些 Mac 上发现在 “/Library” 这个根目录下没有 Google 目录，用方法2即可
>
> 2. 方法2
>
>    ```
>    1. 关闭 Chrome 浏览器，进入目录 “~/Library/Google”
>    cd ~/Library/Google
>    2. 修改 GoogleSoftwareUpdate 这个文件夹的拥有者，使 Google 对该文件夹没有写入权限
>    sudo chown root:wheel GoogleSoftwareUpdate
>    3. 重启 Chrome， “帮助 -> 关于 Google Chrome”显示「更新失败（错误：10）」
>    ```
>
>    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309201459708.png)

##### iOS备忘录写日记

> 1. 手动创建指令，用于调试
>
>    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309181410996.png)
>
> 2. 自动
>
>    1. 早晨10:10新建一条日记，用于记ToDo
>
>       ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309181908378.png)
>
>    2. 晚上22:10打开当日日记，用于记总结
>
>       ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309201506823.png)
>
>    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309201505769.png)

##### final cut Pro 用法

> 1. 导出方式
>
>    > 文件 - 共享 - Apple 设备 1080P - 设置
>    > 修改2个地方
>    >
>    > 1. 格式：电脑
>    > 2. 完成时：什么都不做
>
> 2. 输出所选择区域输出
>
>    > 开始点设置入点I，结束点设置出点O ，右上角，分享

##### VS Code 

> 1. 批量注释/取消注释 ：`command` + `/`
> 2. 调整编辑界面和终端字体大小：`command` + `-`，`command` + `+`

##### 将任务转移到后台运行

> > 场景描述：运行 `docsify serve` ，前台一直运行这个命令，终端被占据
>
> > 解决方案：`ctrl + z` 暂停进程，`bg` 把它丢到后台去运行
>
> * `jobs -l` 显示所有后台任务的 `Job号job_num`  和 `进程号pid_num` 
>
>   > 终端显示格式：[Job号]   进程号   Job状态   Job的启动命令
>   >
>   > [1]  - 64981 running    ydoc serve
>   > [2]  + 67089 suspended (signal)  docsify serve
>
> 1. `ctrl + z`，將前台任务丟到后台，并处于中暂停状态
>
>    > 终端显示：[2]  + 67089 suspended  docsify serve
>
> 2. `bg %job_num`，让在后台暂停的进程在后台继续运行
>
>    > `bg %2`
>    >
>    > 终端显示：[2]  - 67089 continued  docsify serve
>
>    （命令 `kill -cont pid_num`  功能一样）
>
> 3. `kill -stop %job_num` ，将后台运行的运行的进程暂停住
>
>    > `kill -stop 64981`
>    >
>    > 终端显示：[1]  + 64981 suspended (signal)  ydoc serve
>
>    （命令 `kill -stop pid_num` 功能一样）
>
> 4. `kill %job_num`，杀掉后台进程
>
>    （命令`kill pid_num` 也可以）
>
> 5. `command &`，命令前面加`&`，启动任务时就让任务去后台运行
>
>    > `docsify serve &`
>    >
>    > 终端显示：[1] 96071
>    >
>    > `jobs -l`
>    >
>    > 终端显示：[1]  + 96071 running    docsify serve

##### 删除指定程序的进程

> 如Google Chrome：`pkill Google Chrome`

##### 获取IP

> 1. 局域网IP：`ifconfig en0 | grep 'inet' | grep -vE 'inet6'`
>
>    <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200330111301.png" align='left' style="zoom:33%;" />
>
> 2. 外网IP：`curl 'http://httpbin.org/get' -s | grep 'origin'`

##### 简单HTTP服务器

> 1. 进入共享目录
>
> 2. 后台启动HTTP服务：`python -m http.server 8000 &`
>
> 3. 获取局域网IP：`ifconfig en0 | grep 'inet' | grep -vE 'inet6'`
>
>    <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200330111301.png" align='left' style="zoom:33%;" />
>
> 4. Ipad浏览器访问：`http://192.168.1.5:8000`
>
>    <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200330112119.png" style="zoom:33%;" />
>
> 5. 局域网共享Axure原型
>
>    1. Axure生成html文件到：/Users/sai/Documents/Axure
>
>       ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210701144312.png)
>
>    2. 在html文件所在目录启动web服务
>
>    3. 访问：http://192.168.0.166:8000/m站.html

##### nplayer不显示视频信息直接播放

> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309201516405.png)

##### ScreenFlow 变速

> 双击那个视频，改变 Speed 
>
> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309201517282.png)

##### Mac txt乱码问题

> 1. cd [文件所在目录]
>
> 2. iconv -c -f GB2312 -t UTF-8 [你要看的文件] >> [新文件的名称]
>
>    ```bash
>    iconv -c -f GB2312 -t UTF-8 凡人修仙转.txt >> 凡人修仙转2.txt
>    //GB2312是常用中文编码，其他还有gbk等，UTF-8是mac能够识别的编码
>    ```
>

##### Mac 删除文件和文件夹的命令

> `rm -rf 目录名字`
>
> * -r 就是向下递归，不管有多少级目录，一并删除
> * -f 就是直接强行删除，不作任何提示的意思
>
> > linux没有回收站的，rm删除不会进入废纸篓

##### 查看网站自动填充的密码

> input标签，密码字段，即type="password"，输入不可见，右键检查该元素，修改其type属性为text即可见![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309201519799.png)

##### 自定义PPT工具栏

> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309201520425.png)

##### Mac莫名奇妙自动重启

> 1. 关闭安全性与隐私，高级，“不活跃后退出登录”
>
>    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309201522638.png)
>
> 2. 关闭 `autopoweroff` 
>
>    ```bash
>    pmset -g
>    
>    # 输出
>    λ sai [~/Downloads] → pmset -g
>    System-wide power settings:
>    Currently in use:
>     lidwake              1
>     autopoweroff         1
>     standbydelayhigh     86400
>     autopoweroffdelay    28800
>     standbydelaylow      10800
>     
>    # 关闭 autopoweroff
>    sudo pmset -a autopoweroff 0
>    ```
>

##### MacBook 突然没有声音

> ```python
> sudo killall coreaudiod
> ```
>

##### Applescript入门

> ```bash
> # tell指明脚本要控制的程序对象
> tell current application
> 	
> 	# 变量赋值
> 	set str to "World"
> 	# 字符串展示
> 	display dialog "Hello " & str
> 	
> 	set temp to 5
> 	
> 	# 流程语句
> 	if temp < 3 then
> 		# 整型转字符型
> 		display dialog (temp as text) & " < 3"
> 	else if temp > 4 then
> 		display dialog (temp as text) & " > 4"
> 	end if
> 	
> 	# 条件循环
> 	repeat until temp < 4
> 		display dialog "until条件循环中 temp is " & (temp as text)
> 		set temp to temp - 1
> 	end repeat
> 	
> 	repeat while temp > 2
> 		display dialog "while条件循环中 temp is " & (temp as text)
> 		set temp to temp - 1
> 	end repeat
> 	
> 	# 限定次数循环，3次
> 	repeat 3 times
> 		display dialog "限定次数循环中 temp is " & (temp as text)
> 	end repeat
> end tell
> ```
>

##### 批量清理iPhone通讯录

> 1. iPhone - 设置 - iCloud - 通讯录 - 关闭 - “从我的iPhone删除”
> 2. PC登录iCloud - 通讯录 - command + 单击选择 - 左下角设置 - 删除

##### FinePrint 双面打印

> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210619100110.png)

> 打印机：Microsoft Print to PDF
>
> 订口：8mm

##### PDF里的图片文字不清晰

> 1. Mac预览app打开pdf
>
> 2. 菜单中选择文件→导出，Quartz滤镜选取“亮度减少”选项
>
>    使用一次后，对比度会明显增加。如果还不清楚，可连续操作。
>
>    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210703235411.png)

##### [Photoshop任意角度旋转图片](https://jingyan.baidu.com/article/6f2f55a15b7bd3b5b93e6c89.html)

> | 标尺工具                                                     | 图像--图像旋转--任意角度                                     |
> | ------------------------------------------------------------ | ------------------------------------------------------------ |
> | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210812184958.png) | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210812185049.png) |
>