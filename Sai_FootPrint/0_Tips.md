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

3. 获取局域网IP：`inet 192.168.1.5`

   <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200330111301.png" align='left' style="zoom:33%;" />

4. Ipad浏览器访问：`http://192.168.1.5:8000`

   <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200330112119.png" style="zoom:33%;" />



#### nplayer不显示视频信息直接播放

<img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200512171934.png" style="zoom:53%;" />



#### ScreenFlow 变速

1. 双击那个视频，改变 Speed 

   ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200324174710.png)
   
   

### Parallels软件侵权告知函

<img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200331103115.png" style="zoom:50%;" />



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