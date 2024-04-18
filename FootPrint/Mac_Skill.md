#### Mac使用技巧

1. 将任务转移到后台运行

    > 场景描述：运行 `docsify serve` ，前台一直运行这个命令，终端被占据

    > 解决方案：`ctrl + z` 暂停进程，`bg` 把它丢到后台去运行

1. Terminal中断、还原、杀死Python程序

    > * Control + z：暂停进程，并将至放入后台
    >
    >     ```
    >     [1]  + 74136 suspended  /Users/jiangsai/anaconda3/envs/py3/bin/python 
    >     ```
    >
    > * Control + c：杀死进程，并将至放入后台
    >
    >     ```bash
    >     KeyboardInterrupt
    >     Future exception was never retrieved
    >     future: <Future finished exception=Error('Connection closed')>
    >     playwright._impl._api_types.Error: Connection closed
    >     ```
    >
    > * `jobs -l` ：显示所有后台任务的 `Job号job_num`  和 `进程号pid_num` 
    >
    >     ```bash
    >     终端显示格式：[Job号]   进程号   Job状态   Job的启动命令
    >     [1]  - 64981 running    ydoc serve
    >     [2]  + 67089 suspended (signal)  docsify serve
    >     ```
    >
    >     ```
    >     [1]  - suspended  /Users/jiangsai/anaconda3/envs/py3/bin/python 
    >     [2]  + suspended  /Users/jiangsai/anaconda3/envs/py3/bin/python 
    >     ```
    >
    > * `fg %N`：使进程[N]在前台进行
    >
    >     ```bash
    >     [1]  + 74845 continued  /Users/jiangsai/anaconda3/envs/py3/bin/python 
    >     ```
    >
    > * `kill %N`：杀掉后台暂停的进程[N]（最前面的数字）
    >
    >     ```bash
    >     [1]  + 73282 terminated  /Users/jiangsai/anaconda3/envs/py3/bin/python  
    >     ```
    >

1. 获取IP

    > 1. 局域网IP：`ifconfig en0 | grep 'inet' | grep -vE 'inet6'`
    >
    >    <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200330111301.png" align='left' style="zoom:33%;" />
    >
    > 2. 外网IP：`curl 'http://httpbin.org/get' -s | grep 'origin'`

1. 简单HTTP服务器

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

1. nplayer不显示视频信息直接播放

    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309201516405.png)

1. Mac txt 乱码问题

    > 1. cd [文件所在目录]
    >
    > 2. iconv -c -f GB2312 -t UTF-8 [你要看的文件] >> [新文件的名称]
    >
    >    ```bash
    >    iconv -c -f GB2312 -t UTF-8 凡人修仙转.txt >> 凡人修仙转2.txt
    >    //GB2312是常用中文编码，其他还有gbk等，UTF-8是mac能够识别的编码
    >    ```

1. 自定义PPT工具栏

    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309201520425.png)

1. MacBook 突然没有声音

    > `sudo killall coreaudiod`

1. FinePrint 双面打印

    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210619100110.png)
    >
    > 打印机：Microsoft Print to PDF
    >
    > 订口：8mm

1. PDF里的图片文字不清晰

    > 1. Mac预览app打开pdf
    >
    > 2. 菜单中选择文件→导出，Quartz滤镜选取“亮度减少”选项
    >
    >    使用一次后，对比度会明显增加。如果还不清楚，可连续操作。
    >
    >    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210703235411.png)

1. Photoshop任意角度旋转图片

     > | 标尺工具                                                     | 图像--图像旋转--任意角度                                     |
     > | ------------------------------------------------------------ | ------------------------------------------------------------ |
     > | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210812184958.png) | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210812185049.png) |

1. 购买ChatGPT4

     > 方式一：[按次购买，每次买一个月](https://www.youtube.com/watch?v=kkl2YPO33qc)
     >
     > > 1. 注册Apple美国免税洲账号
     > > 2. 办理招商双币信用卡
     > > 3. Apple官网使用信用卡购买礼品卡，送给自己的美区Apple账号
     > > 4. ChatGPT iOS端内购时自动扣礼品卡金额
     >

1. Typora设置

     > 1. 展示设置：增加行宽
     >
     >    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202312161642913.png)
     >
     > 2. 打印设置
     >
     >    1. 页边距
     >
     >       > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310261112999.png)
     >
     >    2. [行距](https://www.twblogs.net/a/5db288f8bd9eee310d9fd66c/?lang=zh-cn)
     >
     >       > 1. 微调`body`中的`line-height`参数
     >       > 2. 关闭文件重新打开，修改即可生效
     >       >
     >       > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310261109296.png)

1. OpenAI语音转文字模型Whisper

     > [教程](https://github.com/openai/whisper)
     >
     > ```bash
     > pip3 install -U openai-whisper
     > // 会自动下载medium模型到 ~/.cache/whisper
     > whisper audio.mp3 --model medium
     > ```
     >

1. 微软文字转语音库

     > [教程](https://github.com/rany2/edge-tts)
     >
     > ```bash
     > //更新pip
     > pip install --upgrade pip
     > //安装依赖库
     > pip install cchardet
     > //安装edge-tts
     > pip3 install edge-tts
     > ```
     >
     > * 安装后测试
     >
     >   ```bash
     >   edge-tts --text "手机微信扫码登录，成功后按回车继续" --write-media 'test.mp3'
     >   ```
     >
     > * 转换指定文件
     >
     >   ```bash
     >   cd /Users/jiangsai/Desktop
     >   edge-tts -f "demo.txt" --write-media "demo.mp3"
     >   ```
     >
     > * 转换指定文件 - 使用指定语音
     >
     >   ```bash
     >   edge-tts --voice zh-CN-YunxiNeural -f "demo.txt" --write-media "demo.mp3"
     >   ```
     >   
     > * 调整语速
     >
     >   ```bash
     >   //语速降低50%
     >   edge-tts --voice zh-CN-YunxiNeural --rate=-50% -f "demo.txt" --write-media "demo.mp3"
     >   //语速增加50%
     >   edge-tts --voice zh-CN-YunxiNeural --rate=+50% -f "demo.txt" --write-media "demo.mp3"
     >   ```
     >
     > * 调整音量
     >
     >   ```bash
     >   //音量降低30%
     >   edge-tts --voice zh-CN-YunxiNeural --rate=-50% --volume=-30% -f "demo.txt" --write-media "demo.mp3"
     >   //音量增加30%
     >   edge-tts --voice zh-CN-YunxiNeural --rate=+50% --volume=+30% -f "demo.txt" --write-media "demo.mp3"
     >   ```
     >   
     >   
     >
     > * 查看更多发音
     >
     >   ```bash
     >   (py3)  Sai  ~/Desktop ：edge-tts --list-voices
     >   Name: af-ZA-AdriNeural
     >   Gender: Female
     >   
     >   Name: af-ZA-WillemNeural
     >   Gender: Male
     >   ```
     >
     >   ```python
     >   import os
     >   
     >   Voice_List = [
     >       "en-AU-NatashaNeural",
     >       "en-AU-WilliamNeural",
     >       "en-IN-NeerjaExpressiveNeural",
     >       "en-IN-PrabhatNeural",
     >       "en-US-AnaNeural",
     >       "en-US-JennyNeural",
     >       "en-US-RogerNeural",
     >       "en-US-SteffanNeural",
     >       "zh-CN-XiaoxiaoNeural",
     >       "zh-CN-XiaoyiNeural",
     >       "zh-CN-YunjianNeural",
     >       "zh-CN-YunxiaNeural",
     >       "zh-CN-YunxiNeural",
     >       "zh-CN-YunyangNeural",
     >       "zh-HK-HiuGaaiNeural",
     >       "zh-HK-WanLungNeural",
     >       "zh-TW-HsiaoChenNeural",
     >       "zh-TW-YunJheNeural",
     >   ]
     >   
     >   folderPath = "/Users/jiangsai/Desktop/1"
     >   
     >   for Voice in Voice_List:
     >       Voice_Path = f"{folderPath}/{Voice}.mp3"
     >       cmd = f'edge-tts --text "手机微信扫码登录，成功后按回车继续，Our companies have a track record of becoming billion dollar companies." --voice {Voice} --write-media "{Voice_Path}"'
     >       print(cmd)
     >       os.system(cmd)
     >   ```
     >
     > * Python 文字转语音脚本
     >
     >   ```python
     >   import os
     >                   
     >   Voice = "zh-CN-YunjianNeural"
     >   Rate = "+0%"
     >   Volume = "+0%"
     >                   
     >   Handle_Folder = "/Users/jiangsai/Desktop/1"
     >                   
     >   # 转换目录内所有单个txt文件为单个mp3音频
     >   for Folder_Path, SonFolders, FileNames in os.walk(Handle_Folder):
     >       for FileName in FileNames:
     >           if FileName.endswith(".txt"):
     >               # 把 dirpath 和 每个文件名拼接起来 就是全路径
     >               FilePath = f"{Folder_Path}/{FileName}"
     >               mp3Name = FileName.replace(".txt", ".mp3")
     >               mp3Path = f"{Folder_Path}/{mp3Name}"
     >               cmd = f'edge-tts --voice {Voice} --rate={Rate} --volume={Volume} -f {FilePath} --write-media "{mp3Path}"'
     >               os.system(cmd)
     >   ```

1. Mac创建双击执行脚本

     > 1. 新建文件`command`文件
     >
     >    `touch 重启音频服务.command`
     >
     > 2. 使用`Sublime Text`打开`重启音频服务.command`文件
     >
     >    ```
     >    #!/bin/bash
     >    sudo killall coreaudiod
     >    ```
     >
     > 3. 文件授权
     >
     >    `chmod +x 重启音频服务.command`

1. 批量删除文件夹内所有视频的开头 x 秒，结尾 y 秒

     > ```python
     > import subprocess
     > import os
     > 
     > # 要处理的视频文件夹路径
     > video_folder = "/Users/jiangsai/Desktop/tt"
     > 
     > # 处理后的视频保存的文件夹
     > output_folder = "/Users/jiangsai/Desktop/ss"
     > if not os.path.exists(output_folder):
     >     os.makedirs(output_folder)
     > 
     > # 要删除的开头时长和结尾时长
     > start_duration = 24  # 开头时长
     > end_duration = 8  # 结尾时长
     > 
     > # 获取文件夹内所有的视频文件
     > videos = [f for f in os.listdir(video_folder) if f.endswith((".mp4", ".mkv", ".avi"))]
     > 
     > for video in videos:
     >     input_path = os.path.join(video_folder, video)
     >     output_path = os.path.join(output_folder, f"trimmed_{video}")
     > 
     >     # 获取视频总时长
     >     cmd = f'ffprobe -v error -show_entries format=duration -of default=noprint_wrappers=1:nokey=1 "{input_path}"'
     >     total_duration = float(subprocess.check_output(cmd, shell=True).decode("utf-8").strip())
     > 
     >     # 计算裁剪后的视频长度
     >     trimmed_duration = total_duration - start_duration - end_duration
     > 
     >     # 使用ffmpeg命令行工具来裁剪视频
     >     cmd = f'ffmpeg -y -i "{input_path}" -ss {start_duration} -t {trimmed_duration} -c copy "{output_path}"'
     >     subprocess.call(cmd, shell=True)
     > 
     > print("所有视频处理完毕。")
     > ```

1. chrome 书签&插件同步不及时

     > 手动强制同步
     >
     > 1. 架梯子
     > 2. 地址栏输入：chrome://sync-internals
     > 3. 中间那列中下方，点击“Stop Sync (Keep Data)”，之后点击“Request Start”
     > 4. 两个设备上的Chrome都进行一次这个操作

1. iOS备忘录写日记

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

1. 
