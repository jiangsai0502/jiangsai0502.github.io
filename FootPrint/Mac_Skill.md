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

      > 方式一：[按次购买，每次买一个月](https://www.youtube.com/watch?v=kkl2YPO33qc) ，[教程](https://hailangya.com/articles/2021/04/02/apple-gift-card/)
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
      > * 本地视频/音频转文字
      >
      >   ```python
      >   import os
      >   import whisper
      >   from zhconv import convert
      >   
      >   
      >   # 处理单个音视频
      >   def transcribe_audio_file(model, input_path, output_path, language):
      >       # 使用Whisper模型进行语音转文字
      >       result = model.transcribe(input_path, language=language)
      >       # 将转换后的文字从繁体中文转换为简体中文
      >       simplified_text = convert(result["text"], "zh-cn")
      >       # 将转换后的文字保存到文本文件中
      >       with open(output_path, "w") as f:
      >           f.write(simplified_text)
      >       print(f"{output_path} 转录完成")
      >   
      >   
      >   # 处理文件夹内的所有音视频
      >   def transcribe_directory(model, input_folder, language):
      >       # 获取指定文件夹内的所有视频文件
      >       video_files = [
      >           f for f in os.listdir(input_folder) if f.endswith((".mp3", ".m4a", ".webm", ".mp4", ".mkv", ".avi"))
      >       ]
      >   
      >       # 处理每个音视频
      >       for video_file in video_files:
      >           video_path = os.path.join(input_folder, video_file)
      >           transcription_path = os.path.join(input_folder, os.path.splitext(video_file)[0] + ".txt")
      >           print(f"{video_file}，正在转录....")
      >           transcribe_audio_file(model, video_path, transcription_path, language)
      >   
      >   
      >   def cooking(input_path):
      >       # 加载Whisper模型 "tiny", "base", "small", "medium", "large"
      >       # 使用时会自动下载到~/.cache/whisper
      >       model = whisper.load_model("small")
      >   
      >       if os.path.isdir(input_path):
      >           transcribe_directory(model, input_path, language="zh")
      >       elif os.path.isfile(input_path):
      >           output_path = os.path.splitext(input_path)[0] + ".txt"
      >           print(f"{input_path}，正在转录....")
      >           transcribe_audio_file(model, input_path, output_path, language="zh")
      >       else:
      >           print(f"提供的路径无效：{input_path}")
      >   
      >   
      >   if __name__ == "__main__":
      >       # 要处理的目录或文件
      >       input_path = "/Users/jiangsai/Desktop/未命名文件夹"
      >       cooking(input_path)
      >   ```
      >
      > * 在线视频转文字
      >
      >   ```python
      >   import subprocess  # 导入subprocess模块，用于执行系统命令
      >   import whisper  # 导入whisper模块，用于语音转文字
      >   
      >   # 定义YouTube视频的URL
      >   youtube_url = "https://www.youtube.com/watch?v=qZ3T5hunOuQ"
      >   # 定义输出的音频文件名
      >   output_audio = "audio.m4a"
      >   
      >   # 使用yt-dlp下载音频并提取为m4a格式，设置为低等品质
      >   # -f bestaudio: 选择最佳音频质量
      >   # --extract-audio: 只提取音频
      >   # --audio-format m4a: 转换音频为m4a格式
      >   # --audio-quality 2: 设置音频质量为低等，0最低，9最高
      >   # -o output_audio: 指定输出文件名为 output_audio
      >   subprocess.run(
      >       [
      >           "yt-dlp",
      >           "-f",
      >           "bestaudio",
      >           "--extract-audio",
      >           "--audio-format",
      >           "m4a",
      >           "--audio-quality",
      >           "2",
      >           "-o",
      >           output_audio,
      >           youtube_url,
      >       ]
      >   )
      >   
      >   # 加载Whisper模型
      >   # "base" 是模型的大小，可以根据需要选择 "tiny", "base", "small", "medium", "large"
      >   model = whisper.load_model("base")
      >   
      >   # 使用Whisper模型读取音频文件并进行语音转文字
      >   result = model.transcribe(output_audio)
      >   
      >   # 打印转换后的文字
      >   print(result["text"])
      >   
      >   # 将转换后的文字保存到文本文件中
      >   # with open("transcription.txt", "w") as f:
      >   #     f.write(result["text"])
      >   ```

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
      > * Python 文字转本地语音脚本
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

1. 分割中英字幕脚本

      ```python
      import re
      
      text = """Excuse me. My name is Richard Stewart. 对不起，我叫Richard Stewart。
      I'm a photographer. 我是一位摄影师。"""
      
      # 使用正则表达式在每段中文的第一个汉字前面增加数字112
      result = re.sub(r"(^|[^\u4e00-\u9fff])([\u4e00-\u9fff])", r"\1 分割词 \2", text, count=1)
      result = re.sub(r"([。！？\n])([^\u4e00-\u9fff]*)([\u4e00-\u9fff])", r"\1\2 分割词 \3", result)
      
      print(result)
      ```

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

1. Sublime Text在非空行且没有标点符号的行末添加句号

      > `(?<![。，？！；：）])(?<=\S)$` 替换 `\0。`

1. Flow番茄钟

      >
      > flow 休息前的叮一声可替换Keep录屏提示音（[MP3转aiff后修改后缀为aif](https://www.freeconvert.com/zh/aif-converter)）
      >
      > /Applications/Flow.app/Contents/Resources/Flow.aif

1. 自制番茄钟

      > 每隔30分钟，暂停chrome，mpv的所有播放，并锁屏

      ```python
      import os
      import time
      import tempfile
      import socket
      import json
      from tqdm import tqdm
      
      
      def lock_screen():
          # 使用 AppleScript 锁屏命令
          os.system(
              'osascript -e "tell application \\"System Events\\" to keystroke \\"q\\" using {control down, command down}"'
          )
      
      
      def pause_browser_media():
          # 使用临时文件存储AppleScript脚本
          pause_chrome_script = """
          tell application "Google Chrome"
              activate
              set foundMedia to false
              repeat with w in windows
                  repeat with t in tabs of w
                      try
                          -- 执行 JavaScript 查找和暂停所有媒体元素
                          set mediaCount to (execute t javascript "document.querySelectorAll('video, audio').length;")
                          if mediaCount > 0 then
                              execute t javascript "document.querySelectorAll('video, audio').forEach(media => media.pause());"
                              set foundMedia to true
                          end if
                      on error errMsg
                              -- 捕获错误，但不做任何处理，防止弹窗
                              -- display dialog "Error in tab: " & errMsg
                      end try
                      delay 0.5 -- 添加延迟来防止浏览器卡死
                  end repeat
              end repeat
          end tell
          """
      
          # 将AppleScript代码写入临时文件
          with tempfile.NamedTemporaryFile("w", delete=False, suffix=".applescript") as script_file:
              script_file.write(pause_chrome_script)
              script_file_path = script_file.name
      
          # 执行临时AppleScript文件
          os.system(f"osascript {script_file_path}")
      
          # 删除临时文件
          os.remove(script_file_path)
      
      
      def pause_mpv():
          # 在~/.config/mpv/mpv.conf 增加一句：input-ipc-server=/tmp/mpvsocket
          # 发送暂停命令到 mpv 的 IPC socket
          try:
              mpv_socket = "/tmp/mpvsocket"  # 确保使用正确的 socket 文件路径
              command = json.dumps({"command": ["set_property", "pause", True]})
      
              # 连接到 mpv 的 socket 并发送命令
              with socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as client_socket:
                  client_socket.connect(mpv_socket)
                  client_socket.sendall(command.encode() + b"\n")
          except Exception as e:
              print(f"Error pausing mpv: {e}")
      
      
      if __name__ == "__main__":
          total_time = 30 * 60  # 30分钟
          interval = 1  # 每秒更新进度条
          
          while True:
              for _ in tqdm(range(0, total_time, interval), desc="工作中", unit="秒"):
                  time.sleep(interval)
              pause_browser_media()  # 暂停浏览器中的媒体播放
              pause_mpv()  # 暂停 mpv 播放
              lock_screen()  # 锁屏
      ```

      
