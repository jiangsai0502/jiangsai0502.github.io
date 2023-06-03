Keyboard Maestro设置

1. 删除Groups列的All Macros中的所有宏

2. 全局通用快捷键

   1. Groups列：创建一个Sai Global

   2. Macros列：创建下列宏

      1. 录音宏

         ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306031102821.png)

      2. 锁屏宏

         ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306031104819.png)

      3. 剪切板宏（没paste漂亮，放弃了）

         ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306031108245.png)

      4. KM自带OCR宏

         [Keyboard Maestro ，在多语言环境中轻松抓取文字](https://utgd.net/article/9528)、[在 Mac 上随时提取屏幕上的文字](https://www.notion.so/Mac-b7ded7e6bfb6408d99f61832c043570a)

         ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306031545004.png)

      5. 第三方OCR宏

         1. [ KM 调用百度OCR接口](https://medium.com/@Cyborger/keyboard-maestro-%E4%BD%BF%E7%94%A8-km-%E5%AE%9E%E7%8E%B0%E5%85%8D%E8%B4%B9%E4%B8%AD%E6%96%87-ocr-%E5%85%89%E5%AD%A6%E5%AD%97%E7%AC%A6%E8%AF%86%E5%88%AB-94ff46e5625)、[申请百度文字识别API的AppID 、API Key、Secret Key](https://www.jianshu.com/p/e10dc43c38d0)

         2. 安装环境

            > 百度OCR API：pip3 install baidu-aip
            >
            > 通用字符编码检测器：pip install chardet
            >
            > ```
            > #!/usr/bin/python3
            > 
            > # -*- coding: utf-8 -*-
            > 
            > # encoding=utf8
            > 
            > from aip import AipOcr
            > import sys,io
            > sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
            > 
            > """ 你的 APPID AK SK """
            > APP_ID = '34338402'
            > API_KEY = 'GVeTGTZdRIiH3AphNQtumCk4'
            > SECRET_KEY = 'csTzqbvYHbj8XGMnIgCAOtN7Gq1Ra58H'
            > 
            > client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
            > 
            > def get_file_content(file):
            >     with open(file, 'rb') as fp:
            >         return fp.read()
            > 
            > def img_to_str(image_path):
            >     image = get_file_content(image_path)
            >     result = client.basicGeneral(image)
            >     if 'words_result' in result:
            >         return u'\n'.join([w['words'] for w in result['words_result']])
            > 
            > print(img_to_str(image_path='/Users/jiangsai/Downloads/1.png'))
            > ```

         ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306031548451.png)

      6. 阅读摘录

         > 实现从Marginote复制文字时，文字携带所属笔记链接；从Chrome复制文字时，文字携带所属网页链接
         >
         > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306031542955.png)

      7. Chrome打开指定标签文件夹中的所有网页

         ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306031505068.png)

      8. 找到unisat钱包插件，点击 -> 输入密码 -> 回车，进入钱包

         ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306031611502.png)

      9. 模拟Alfred搜索KM宏

         1. 创建一个Sai Search Group，所有不想设置快捷键的宏都放这里

         2. 在Sai Global新建一个宏Trigger by Sai Search

            ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306031536092.png)

3. Chrome专用快捷键

   [Keyboard Maestro: 设置特定应用内的宏](https://www.bilibili.com/video/BV125411s79e/?spm_id_from=333.337.search-card.all.click&vd_source=052b07ad0190d9dabdf1d78fda0168a7)

   1. Groups列：创建一个group：Sai Chrome Group，并设置Sai Chrome Group仅在Chrome中生效

      ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306022331425.png)

   2. 已有快捷键替换

      1. 下载内容页宏

         > 1. Macros列创建宏：Downloads
         > 2. 设置下载内容快捷键：⌘ + D
         > 3. 通过「type a keystroke」模拟实际快捷键：⌥ + ⌘ + L

   3. Chrome没有快捷键，用Keyboard Maestro创造快捷键宏

      1. 扩展程序宏

         > 1. Macros列创建宏：Extensions
         > 2. 设置下载内容快捷键：⌘ + E
         > 3. 通过「select or show a Menu item」模拟点击顶部菜单栏-窗口-扩展程序

         ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306022340183.png)