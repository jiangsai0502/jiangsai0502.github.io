#### Mac使用技巧

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
    > * jobs：查看当前暂停的进程
    >
    >     ```bash
    >     [1]  - suspended  /Users/jiangsai/anaconda3/envs/py3/bin/python 
    >     [2]  + suspended  /Users/jiangsai/anaconda3/envs/py3/bin/python 
    >     ```
    >
    > * fg %N：使进程[N]在前台进行
    >
    >     ```bash
    >     [1]  + 74845 continued  /Users/jiangsai/anaconda3/envs/py3/bin/python 
    >     ```
    >
    > * kill %N：杀掉后台暂停的进程[N]（最前面的数字）
    >
    >     ```bash
    >     [1]  + 73282 terminated  /Users/jiangsai/anaconda3/envs/py3/bin/python  
    >     ```
    >

1. 购买ChatGPT4

    > 方式一：[按次购买，每次买一个月](https://www.youtube.com/watch?v=kkl2YPO33qc)
    >
    > > 1. 注册Apple美国免税洲账号
    > > 2. 办理招商双币信用卡
    > > 3. Apple官网使用信用卡购买礼品卡，送给自己的美区Apple账号
    > > 4. ChatGPT iOS端内购时自动扣礼品卡金额
    >

1. Typora打印PDF格式设置

    > 1. 页边距
    >
    >    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310261112999.png)
    >
    > 2. [行距](https://www.twblogs.net/a/5db288f8bd9eee310d9fd66c/?lang=zh-cn)
    >
    >    > 1. 微调`body`中的`line-height`参数
    >    > 2. 关闭文件重新打开，修改即可生效
    >    >
    >    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310261109296.png)

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
    >    `chmod +x Restart_AudioService.command`

