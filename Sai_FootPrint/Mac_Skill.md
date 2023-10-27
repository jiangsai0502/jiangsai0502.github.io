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
    >   edge-tts --text "自动化测试第2步，需要您手机微信扫码登录，成功后，请按回车继续" --write-media '1.mp3' --voice zh-CN-YunxiNeural
    >   ```
    >
    >   > `--text` 要转为语音的文字
    >   >
    >   > `--write-media` 要保存的文件路径
    >   >
    >   > `--voice` 指明了使用哪种语言
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
    >   cd /Users/jiangsai/Desktop
    >   edge-tts -f "demo.txt" --write-media "demo.mp3" --voice zh-CN-YunxiNeural
    >   ```
    >
    > * 调整语速
    >
    >   ```bash
    >   //语速降低50%
    >   edge-tts -f "d:\byhy\xy.txt" --write-media "d:\byhy\xy.mp3" --voice zh-CN-YunxiNeural --rate=-50%
    >   //语速增加50%
    >   edge-tts -f "d:\byhy\xy.txt" --write-media "d:\byhy\xy.mp3" --voice zh-CN-YunxiNeural --rate=+50%
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
    >       cmd = f'edge-tts --text "自动化测试，需要您手机微信扫码登录，Our companies have a track record of becoming billion dollar companies." --voice {Voice} --write-media "{Voice_Path}"'
    >       print(cmd)
    >       os.system(cmd)
    >   ```
    >
    >   
    >
    > * Python 文字转语音脚本
    >
    >   ```python
    >   import os
    >   
    >   VOICE = "zh-CN-YunjianNeural"
    >   folderPath = "/Users/jiangsai/Desktop/1"
    >   
    >   for dirpath, dirnames, filenames in os.walk(folderPath):
    >       for fn in filenames:
    >           # 把 dirpath 和 每个文件名拼接起来 就是全路径
    >           fpath = os.path.join(dirpath, fn)
    >           mp3Path = os.path.join(dirpath, fn.replace(".txt", ".mp3"))
    >           cmd = f'edge-tts --voice {VOICE} -f "{fpath}" --write-media "{mp3Path}"'
    >           print(cmd)
    >           os.system(cmd)
    >   ```