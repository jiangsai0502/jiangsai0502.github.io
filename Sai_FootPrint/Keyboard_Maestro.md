#### [Keyboard Maestro软件介绍](https://sspai.com/post/36442)

1. **Trigger**

   1. Hot Key Trigger：快捷**组合**键触发
   2. Global Macro Palette Trigger：屏幕显示「宏调色板触发器」窗口，点击窗口中的 Macro 来触发
   3. Typed String Trigger：某些字符被敲下时触发，与 HotKeyTrigger 不同的是，Typed String 敲下的字符不需要包含修饰键，同时这些按键不需要被同时按下。**慎用**
   4. Application Trigger：当某个应用程序处于某个状态时，触发。像 「Finder 从后台被激活到前台时（关闭其他窗口）」，「Chrome 被 `⌘ Q` 退出时（询问是否启动 Safari）」。Audio Output Changed Trigger
   5. Cron Trigger：具体在某年某月某日的某时，触发
   6. Time of Day Trigger：具体在一天的某一时间点时，触发
   7. Folder Trigger：这个触发器会关注某个特定文件夹，当这个文件夹添加了新文件，移除了文件，添加或移除了文件时，触发。
   8. Sleep Trigger：当 Mac 睡眠时触发，这个触发器能够将 Mac 睡眠推迟最长大概 30s 用于执行相应的 Action。
   9. Wake Trigger：类似 Sleep Trigger，在 Mac 唤醒时触发。

2. **Action**

   1. **Application Control**
      
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031748852.png) | 激活一个App，并置于顶部 |
      | ------------------------------------------------------------ | ----------------------- |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031749812.png) | 退出一个App             |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031750146.png) | 隐藏一个App             |
      
   2. **Clipboard Actions**

      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031753111.png) | 将文本赋值给剪切板 |
      | ------------------------------------------------------------ | ------------------ |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031754712.png) | 将变量赋值给剪切板 |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031755959.png) | 将图片赋值给剪切板 |

   3. **Control Flow Actions**

      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031756726.png) | 暂停xxx秒                                                |
      | ------------------------------------------------------------ | -------------------------------------------------------- |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031757251.png) | 暂停，直到某些条件达成                                   |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031757636.png) | 一直执行某些操作，直到某些条件达成时结束                 |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031758033.png) | 满足某些条件时，执行某些操作                             |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031758883.png) | 重复某些操作xxx次                                        |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031759448.png) | 如果满足某些条件，则执行某些操作，否则执行其他操作       |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031759535.png) | 在一组值上循环（如数字、当前运行的程序、文件夹里的文件） |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031800077.png) | 跳出循环，执行后面的操作                                 |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031800408.png) | 取消当前正在执行的所有宏                                 |

   4. **Debugger Actions**

      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031802329.png) | 设置断点 |
      | ------------------------------------------------------------ | -------- |

   5. **Execute Actions**

      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031803296.png) | 执行shell脚本 |
      | ------------------------------------------------------------ | ------------- |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031803138.png) | 执行一个宏    |

   6. **File Actions**

      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031806050.png) | 新建文件夹                     |
      | ------------------------------------------------------------ | ------------------------------ |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031806651.png) | 移动（或重命名）文件           |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031807831.png) | 删除文件                       |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031807332.png) | 打开一个文件、文件夹、App      |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031807569.png) | 将一个文件读入剪切板、变量     |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031808087.png) | 将变量、剪切板清空写入一个文件 |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031808502.png) | 将变量、剪切板追加写入文件     |

   7. **Google Chrome Actions**

      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031810455.png) | 新建窗口，打开指定URL |
      | ------------------------------------------------------------ | --------------------- |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031811454.png) | 新建Tab，打开指定URL  |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031811276.png) | 选择指定Tab           |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031812427.png) | 等待页面加载          |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031812352.png) | 点击指定标题的链接    |

   8. **Interface Control**

      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031814192.png) | 调窗口整大小，移动到指定坐标，置顶，关闭                     |
      | ------------------------------------------------------------ | ------------------------------------------------------------ |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031815203.png) | 移动光标，点击（单击、双击、三击），拖动，组合键点击，在指定窗口按图找坐标 |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031815848.png) | 寻找图片，并点击它                                           |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031816373.png) | 操作指定App顶部菜单栏                                        |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031816517.png) | 模拟按下指定按键或组合键                                     |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031817606.png) | 用变量移动鼠标、窗口、App、音量                              |

   9. **Keyboard Maestro Actions**

      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031819220.png) | 录制一个临时宏         |
      | ------------------------------------------------------------ | ---------------------- |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031819582.png) | 通过名字触发宏         |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031820540.png) | 启用、禁用某个宏       |
      | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031820669.png) | 不执行任何操作，宏注释 |

   10. **Notification Actions**

       | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031821763.png) | 阻断式提示<br />【Stop】会中断这个宏后面的所有操作，【Continue】会继续这个宏后面的操作 |
       | ------------------------------------------------------------ | ------------------------------------------------------------ |
       | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031821534.png) | 自定义按钮的Alert                                            |

   11. **Text Actions**

       | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031823929.png) | 通过粘贴插入文本 |
       | ------------------------------------------------------------ | ---------------- |
       | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031823361.png) | 通过输入插入文本 |
       | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031823723.png) | 文本朗读         |

   12. **Variable**

       | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031825174.png) | 将文本赋值给变量                   |
       | ------------------------------------------------------------ | ---------------------------------- |
       | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031825007.png) | 在变量前插入文本                   |
       | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031826923.png) | 在变量后插入文本                   |
       | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031826250.png) | 计算数字变量                       |
       | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031827888.png) | 将剪切板赋值给变量                 |
       | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031827010.png) | 设置字典                           |
       | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307031828714.png) | 对剪切板、文本、变量进行格式化处理 |

3. 基础设置说明

   1. 删除Groups列的All Macros中的所有宏
   2. Groups列：创建一个Sai Global
   3. Macros列：创建下列宏
   
4. 宏案例

   | 宏                                                           |                                                              |
   | ------------------------------------------------------------ | ------------------------------------------------------------ |
   | 停止所有宏                                                   | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306091847693.png) |
   | 录音                                                         | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306031102821.png) |
   | 锁屏                                                         | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306031104819.png) |
   | 防误退出宏                                                   | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306211412581.png) |
   | 模拟Alfred搜索KM宏<br/><br/>1. 创建一个Sai Search Group，所有不想设置快捷键的宏都放这里<br/><br/>2. 在Sai Global新建一个宏Trigger by Sai Search | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306031536092.png) |
   | KM自带OCR宏<br/><br/>[Keyboard Maestro ，在多语言环境中轻松抓取文字](https://utgd.net/article/9528)、[在 Mac 上随时提取屏幕上的文字](https://www.notion.so/Mac-b7ded7e6bfb6408d99f61832c043570a) | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306031545004.png) |
   | 第三方OCR宏<br />环境配置见下方<br />                        | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306031548451.png) |
   | 阅读摘录<br />`实现从Marginote复制文字时，文字携带所属笔记链接；从Chrome复制文字时，文字携带所属网页链接` | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306211453150.png) |
   | Chrome打开指定标签文件夹中的所有网页                         | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306031505068.png) |
   | 找到unisat钱包插件，点击 -> 输入密码 -> 回车，进入钱包       | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306031611502.png) |
   | 打开Zoom，输入会议号、密码、邮箱                             | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306031805707.png) |
   | 视频网站5秒快进                                              | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306032242967.png) |

   第三方OCR宏

   > 1. [ KM 调用百度OCR接口](https://medium.com/@Cyborger/keyboard-maestro-%E4%BD%BF%E7%94%A8-km-%E5%AE%9E%E7%8E%B0%E5%85%8D%E8%B4%B9%E4%B8%AD%E6%96%87-ocr-%E5%85%89%E5%AD%A6%E5%AD%97%E7%AC%A6%E8%AF%86%E5%88%AB-94ff46e5625)、[申请百度文字识别API的AppID 、API Key、Secret Key](https://www.jianshu.com/p/e10dc43c38d0)
   >
   > 2. 百度OCR API：`pip3 install baidu-aip`
   >
   > 3. 通用字符编码检测器：`pip install chardet`
   >
   > 4. 宏脚本
   >
   >    ```
   >    #!/usr/bin/python3
   >    
   >    # -*- coding: utf-8 -*-
   >    
   >    # encoding=utf8
   >    
   >    from aip import AipOcr
   >    import sys,io
   >    sys.stdout=io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
   >    
   >    """ 你的 APPID AK SK """
   >    APP_ID = '34338402'
   >    API_KEY = 'GVeTGTZdRIiH3AphNQtumCk4'
   >    SECRET_KEY = 'csTzqbvYHbj8XGMnIgCAOtN7Gq1Ra58H'
   >    
   >    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
   >    
   >    def get_file_content(file):
   >     with open(file, 'rb') as fp:
   >         return fp.read()
   >    
   >    def img_to_str(image_path):
   >     image = get_file_content(image_path)
   >     result = client.basicGeneral(image)
   >     if 'words_result' in result:
   >         return u'\n'.join([w['words'] for w in result['words_result']])
   >    
   >    print(img_to_str(image_path='/Users/jiangsai/Downloads/1.png'))
   >    ```

   #### 测试

   * 在一个App中等一个界面出现，以5秒为周期检查一下，界面出现立刻执行一个操作，不出现就一直等着，一旦等到就继续执行下面的代码，循环5个周期后还没等到就放弃，继续执行下面的代码

     ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306092052172.png)

   1. 剪切板宏（没paste漂亮，放弃了）

      ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306031108245.png)
      
   1. Chrome专用快捷键

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

* 断点调试

​	![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306032334153.png)

* 自制动作重复器

  > 无法精细控制，适用于简单的重复动作，更复杂的还是用record，record可以修改中间的动作细节

  ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202306032343693.png)

