# 重装系统
1. 快捷键

   * Chrome外的沙拉查词：⌘ + ～
   * 锁屏：⌘ + L
   * Snipaste截图：⌘ + 1
   * Anki挖空：⌘ + 3
   * PicGo上传剪切板图片：⌘ + 4
   * QQ截图识字：⌘ + 5
   * 新建录音：⌥ + 1
   * 暂停录音：⌥ + 2
   * Paste调起剪切板：⌥ + S
   * 切换输入法：Control + 空格

2. 常备软件

   * sougou
   * 微信

   * QQ

   * Chrome

   * office

   * PDF expert

   * istat menus

   * itsycal

   * snipaste

   * sublime

   * App Cleaner & Uninstaller Pro

   * Photoshop

   * Typora

   * XMind ZEN

   * Permute

   * go2shell（官网下载）

   * 欧路

   * Picgo

   * Paste（官网下载helper）

3. 安装brew

   > 1. 命令
   >
   >    `/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)" `
   >
   > 2. 推荐使用中科大源

4. 安装mpv

   > ```
   > brew install mpv --cask
   > 
   > # 创建配置文件：~/.config/mpv/input.conf
   > AXIS_UP add volume -2
   > AXIS_DOWN add volume 2
   > AXIS_LEFT seek -2 exact
   > AXIS_RIGHT seek 2 exact
   > LEFT seek -2 exact
   > RIGHT seek 2 exact
   > UP add volume 2
   > DOWN add volume -2
   > ```

5. 安装iterm2

   > 1. 命令
   >
   >    `brew install iterm2`
   >
   > 2. 把iTerm2设为默认
   >
   >    * iTerm2 -> Make ITerm2 Default Term
   >
   >      ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413110312.png)
   >
   > 3. 快捷键
   >
   >    1. 光标按照单词快速移动
   >
   >       * iTerm2 -> Preferences -> Keys -> Key Bindings
   >
   >         修改 ⌘← 和 ⌘→ 的映射，双击进入后，选择Action为 “Send Escape Sequence”，Esc+为 ⌘← 对应 b ， ⌘→ 对应 f
   >
   >         ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220412205506.png)
   >
   >    2. 按照单词快速删除（结合BetterTouchTool）
   >
   >       * 修改 ⌘+Delete 的映射，⌘+Delete 代表 control + w
   >
   >         ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220412210000.png)
   >
   > 4. 安装Oh my zsh [参考](https://segmentfault.com/a/1190000041138667?utm_source=sf-similar-article)
   >
   >    ```
   >    brew install wget;
   >    export REMOTE=https://gitee.com/imirror/ohmyzsh.git;
   >    sh -c "$(wget -O- https://cdn.jsdelivr.net/gh/ohmyzsh/ohmyzsh/tools/install.sh)";
   >    
   >    open ~/.zshrc
   >    # 在.zshrc文件中搜索 source $ZSH/oh-my-zsh.sh，在本句之前加一句
   >    ZSH_DISABLE_COMPFIX="true"
   >    # 禁用oh-my-zsh自动更新
   >    找到DISABLE_AUTO_UPDATE一行，将行首的注释'#'去掉
   >    source ~/.zshrc
   >    ```
   >
   > 5. 安装PowerFonts字体
   >
   >    ```
   >    1. 下载：https://github.com/powerline/fonts
   >    2. 解压
   >    3. 进入文件夹：cd fonts-master
   >    4. 安装：./install.sh
   >    ```
   >
   > 6. 设置字体
   >
   >    iTerm2 -> Preferences -> Profiles -> Text，在Font区域选中Change Font，然后找到Meslo LG字体，有L、M、S可选
   >
   >    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413112345.png)
   >
   > 7. 配色方案
   >
   >    iTerm2 -> Preferences -> Profiles -> Colors -> Color Presets
   >
   >    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413113614.png)
   >
   > 8. 设置主题
   >
   >    ```
   >    open ~/.zshrc
   >    # 搜索'ZSH_THEME'，修改为ZSH_THEME="agnoster"
   >    source ~/.zshrc
   >    ```
   >
   > 9. 设置语法高亮
   >
   >    ```
   >    brew install zsh-syntax-highlighting
   >    
   >    open ~/.zshrc
   >    最后插入一行：source /opt/homebrew/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
   >    source ~/.zshrc
   >    ```
   >
   > 10. 获取代理地址
   >
   >     ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413141420.png)
   >
   > 11. 自动提示与命令补全
   >
   >     `git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions`
   >
   >     ```
   >     open ~/.zshrc
   >     搜索'plugins'，修改为plugins=(zsh-autosuggestions)
   >     source ~/.zshrc
   >     ```
   >
   > 12. 隐藏名字和主机名
   >
   >     ```
   >     open ~/.oh-my-zsh/themes
   >     打开agnoster.zsh-theme文件，找到prompt_context()函数，替换为
   >     prompt_context() {
   >       if [[ "$USERNAME" != "$DEFAULT_USER" || -n "$SSH_CLIENT" ]]; then
   >         prompt_segment black default "Sai"
   >       fi
   >     }
   >     source agnoster.zsh-theme
   >     ```
   >
   >     ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413135638.png)

6. 安装youtube-dl

   > `brew install youtube-dl`
   >
   > *  下载默认类型视频（无字幕）
   >
   >   `youtube-dl https://www.youtube.com/watch?v=n_6p-1J551Y`
   >
   > * 下载默认类型视频（有字幕）
   >
   >   `youtube-dl --write-auto-sub https://www.youtube.com/watch?v=n_6p-1J551Y`
   >
   > * 下载视频（指定名称）
   >
   >   `youtube-dl https://www.youtube.com/watch?v=n_6p-1J551Y -o '你要的名字'`
   >
   > * 单独下载**字幕**（无视频）
   >
   >   `youtube-dl --proxy 127.0.0.1:1081 --write-sub --skip-download https://www.youtube.com/watch?v=n_6p-1J551Y`
   >
   > * 查看视频所有类型
   >
   >   `youtube-dl -F https://www.youtube.com/watch?v=n_6p-1J551Y`
   >
   > * 查看视频所有字幕
   >
   >   `youtube-dl --list-subs https://www.youtube.com/watch?v=n_6p-1J551Y`
   >
   > * 下载指定质量的视频和音频并自动合并（有字幕）
   >
   >   `youtube-dl -f 160+249 https://www.youtube.com/watch?v=n_6p-1J551Y`
   >
   > * 下载指定质量的视频和音频并自动合并，并转码成mp4格式（有字幕）
   >
   >   `youtube-dl -f 160+249 --recode-video mp4 https://www.youtube.com/watch?v=n_6p-1J551Y`
   >
   > * 使用代理下载默认类型的视频
   >
   >   `youtube-dl --proxy 127.0.0.1:1081 https://www.youtube.com/watch?v=xqdI6ljJ954`
   >
   > * 使用代理下载默认类型的视频**列表**
   >
   >   `youtube-dl --proxy 127.0.0.1:1081 --yes-playlist https://www.youtube.com/watch?v=xqdI6ljJ954`
   >
   > * B站无音频格式，故会先下视频载ffmepg自动转成音频
   >   `youtube-dl --extract-audio https://www.bilibili.com/video/BV1xJ411r7Yo`

7. 安装you-get

   > `brew install you-get`
   >
   > * 分析视频可供下载的全部格式：-i参数
   >   `you-get -i https://www.youtube.com/watch?v=jNQXAC9IVRw`
   >
   > * 直接下载默认格式：
   >   `you-get https://www.youtube.com/watch?v=jNQXAC9IVRw`
   >
   > * 指定下载名称
   >
   >   `you-get https://www.youtube.com/watch?v=jNQXAC9IVRw -O FileName`
   >
   > * 自定义下载格式：
   >   `you-get --itag=18 'https://www.youtube.com/watch?v=jNQXAC9IVRw'`
   >
   > * 使用HTTP代理下载：
   >   `you-get -x 127.0.0.1:1081 --itag=18 'https://www.youtube.com/watch?v=jNQXAC9IVRw'`

8. 启动台图标数量7 x 11

   > ```
   > defaults write com.apple.dock springboard-rows -int 7;
   > defaults write com.apple.dock springboard-columns -int 11;
   > defaults write com.apple.dock ResetLaunchPad -bool true;
   > killall Dock
   > ```

9. Finder顶端显示完整路径

   > `defaults write com.apple.finder _FXShowPosixPathInTitle -bool YES`

10. Alfred

   > 1. 将Spotlight的快捷键分给Alfred
   >
   >    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413142827.png)
   >
   > 2. 搜索排除某个文件夹
   >
   >    1. 添加要排除的文件夹
   >    2. 调出alfred，输入reload回车，清空alfred缓存
   >
   >    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413143239.png)
   >
   > 3. 自定义文件操作
   >
   >    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413143409.png)
   >
   > 4. **Quick Search**：最常用，`Space + 关键字`快速启用打开文件，功能类似于使用`Open + 关键字`
   >
   > 5. **Inside Files**：最常用，`in + 关键字`查找包含查询字的文件
   >

11. ClashX 设置方法

    > 1. 获取订阅链接
    >
    >    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202111261625570.png)
    >
    > 2. 添加配置
    >
    >    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202111261625530.png)
    >
    >    - `Url`: 填入订阅链接
    >
    >    - `Config Name`：填写一个备注名称

12. brew 挂代理方式

    > ```bash
    > 1. touch ~/.curlrc
    > 2. 见上教程，获取代理地址
    > 3. open ~/.curlrc
    > 4. 输入代理地址：proxy=127.0.0.1:1081
    > 5. 用完可以删掉该文件，否则墙内资源会受限
    >    rm ~/.curlrc
    > 
    > # 单个命令挂代理1
    > http_proxy=http://127.0.0.1:1081 https_proxy=http://127.0.0.1:1081 brew install PACKAGE
    > # 单个命令挂代理2
    > ALL_PROXY=socks5://127.0.0.1:1081 brew install PACKAGE
    > ```
    >

13. sublime配置

    > ```
    > # command+Shift+P，输入
    > install package
    > # 回车自动安装
    > 
    > # 解决乱码问题：command+Shift+P，输入install package，弹出框，输入
    > ConvertToUTF8
    > # 回车自动安装
    > 
    > # 中文汉化包：command+Shift+P，输入install package，弹出框，输入
    > ChineseLocalizations
    > # 回车自动安装
    > 
    > # Ayu主题：command+Shift+P，输入install package，弹出框，输入
    > ayu
    > # 回车自动安装
    > # 选择主题：ayu: Activate theme，选择，回车
    > ```

14. Git 挂代理方式

    > `git clone https://github.com/altercation/solarized/ --config http.proxy='http://127.0.0.1:1087'`

15. Chrome 搜索后新标签打开链接

    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413155126.png)

16. Mac 修改文件创建时间

    > `touch -mt YYYYMMDDhhmm`
    > 示例
    >
    > ```bash
    > 1. 在Terminal中输入 touch -mt 20160101  
    > 2. 将/Users/will/Downloads/1.png拖入Terminal中
    > 3. Terminal会显示 touch -mt 20160101 /Users/will/Downloads/123.png
    > 4. 回车执行即可
    > 注：改成当天 touch -m 文件名
    > ```
    >

17. 文献阅读：沙拉查词 + Alfred

    > [参考](https://zhuanlan.zhihu.com/p/113809716)
    >
    > 1. 安装Chrome插件：沙拉查词
    >
    > 2. 配置浏览器外划词翻译
    >
    >    > 浏览器外配置好后，其调用沙拉查词的方式同样适用于浏览器内，因此一劳永逸
    >
    >    1. 在Chrome内为沙拉查词设置**全局快捷键**
    >
    >       > 地址栏：chrome://extensions/shortcuts
    >
    >       ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413160100.png)
    >
    >    2. 开启沙拉查词的Chrome权限
    >
    >       ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413160125.png)
    >
    >    3. 配置Alfred
    >
    >       1. [下载Alfred workflow脚本](https://link.zhihu.com/?target=https%3A//github.com/crimx/ext-saladict/files/3711425/saladict.alfredworkflow.zip)
    >
    >       2. 双击，import脚本
    >
    >       3. 设置hotkey：`control + ~`
    >
    >       4. 结合BetterTouchTool修改触发条件：在PDF expert中鼠标移到底边触发`control + ~`
    >
    >          ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413160145.png)
    >
    >       5. 沙拉词典焦点
    >
    >          1. 方法1：设置
    >
    >             ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413160217.png)
    >
    >          2. 方法2：修改Run NSAppleScript脚本
    >
    >             ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413160246.png)
    >
    >             ```bash
    >             on alfred_script(q)
    >               tell application "System Events"
    >             	# 快捷键打开沙拉词典
    >             	key code 37 using {control down, command down}
    >             	delay 0.1
    >             	# 焦点从沙拉词典移回源文件
    >             key code 48 using {command down}
    >               end tell
    >             end alfred_script
    >             ```
    >
    >    4. 积累生词
    >
    >       ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413155850.png)
    >
    >    5. Saladict 生词本导出生词
    >       ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413155956.png)
    >

18. Karabiner

    >1. 修改单个键位
    >
    >   ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220426110827.png)
    >
    >2. 修改组合快捷键[参考](https://blog.csdn.net/qq_26012495/article/details/88539120)
    >
    >   1. 新建MyShortcut.json，放入`~/.config/karabiner/assets/complex_modifications`
    >
    >      ```
    >      {
    >        "title": "JiangSai",
    >        "rules": [
    >          {
    >            "description": "锁屏",
    >            "manipulators": [
    >              {
    >                "type": "basic",
    >                "from": {
    >                  "key_code": "l",
    >                  "modifiers": {
    >                    "mandatory": ["command"]
    >                  }
    >                },
    >                "to": [
    >                  {
    >                    "key_code": "q",
    >                    "modifiers": [
    >                      "command",
    >                      "control"
    >                      ]
    >                  }
    >                ]
    >              }
    >            ]
    >          },
    >          {
    >            "description": "录音-新建",
    >            "manipulators": [
    >              {
    >                "type": "basic",
    >                "from": {
    >                  "key_code": "1",
    >                  "modifiers": {
    >                    "mandatory": ["option"]
    >                  }
    >                },
    >                "to": [
    >                  {
    >                    "key_code": "r",
    >                    "modifiers": [
    >                      "shift",
    >                      "command"
    >                      ]
    >                  }
    >                ]
    >              }
    >            ]
    >          },
    >          {
    >            "description": "录音-暂停",
    >            "manipulators": [
    >              {
    >                "type": "basic",
    >                "from": {
    >                  "key_code": "2",
    >                  "modifiers": {
    >                    "mandatory": ["option"]
    >                  }
    >                },
    >                "to": [
    >                  {
    >                    "key_code": "c",
    >                    "modifiers": [
    >                      "shift",
    >                      "command"
    >                      ]
    >                  }
    >                ]
    >              }
    >            ]
    >          },
    >          {
    >            "description": "typora",
    >            "manipulators": [
    >              {
    >                "type": "basic",
    >                "from": {
    >                  "key_code": "grave_accent_and_tilde",
    >                  "modifiers": {
    >                    "mandatory": ["command"]
    >                  }
    >                },
    >                "to": [
    >                  {
    >                    "key_code": "grave_accent_and_tilde",
    >                    "modifiers": [
    >                      "shift",
    >                      "control"
    >                      ]
    >                  }
    >                ]
    >              }
    >            ]
    >          },
    >          {
    >            "description": "Anki_cloze",
    >            "manipulators": [
    >              {
    >                "type": "basic",
    >                "from": {
    >                  "key_code": "3",
    >                  "modifiers": {
    >                    "mandatory": ["command"]
    >                  }
    >                },
    >                "to": [
    >                  {
    >                    "key_code": "c",
    >                    "modifiers": [
    >                      "left_command",
    >                      "left_shift",
    >                      "left_option"
    >                    ]
    >                  }
    >                ]
    >              }
    >            ]
    >          }
    >        ]
    >      }
    >      ```
    >
    >   2. preference - complex modification - add rule - 第一行Anki_cloze内的命令"Change command+option+shift+c key to command+3"点击"Enable"
    >
    >   3. grave_accent_and_tilde即键盘esc下方的`



#### 下载[喜马拉雅](https://github.com/zeakhold/xmlyfetcher)

* 安装

  ```bash
  brew install node
  npm install -g xmlyfetcher
  ```

* 使用

  ```bash
  # 下载专辑
  xmlyfetcher https://www.ximalaya.com/ertong/10078066/
  
  # 下载专辑单页
  xmlyfetcher https://www.ximalaya.com/ertong/12891461/p2/
  
  # 下载单个曲目
  xmlyfetcher https://www.ximalaya.com/ertong/12891461/211393643
  
  # 下载到指定目录
  xmlyfetcher https://www.ximalaya.com/ertong/12891461/211393643 -o ~/Downloads
  
  # 指定下载单个音频的超时时间（默认8s）
  xmlyfetcher https://www.ximalaya.com/ertong/12891461/211393643 -t 20
  ```


#### Subler合并视频和字幕

![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200504124414.png)

#### jupyter用法

1. 安装：

   ```bash
   # 切换虚拟环境
   source activate py3.8
   # 安装jupyter
   conda install jupyter
   # 安装支持conda虚拟环境的插件
   conda install nb_conda
   # 安装指定虚拟环境的kernel到notebook
   python -m ipykernel install --user --name py3.8 --display-name "Python py3.8"
   # 查看kernel虚拟环境
   jupyter kernelspec list
   # 删除指定虚拟环境的kernel
   jupyter kernelspec remove kernel_name
   # 
   ```

2. 基本用法

   ```bash
   # 切换到jupyter文件目录
   cd /Users/sai/Documents/Temp
   # 启动 jupyter
   jupyter notebook
   # 退出 jupyter
   `control`+`c`
   ```

3. Vscode 中使用

   ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200708161754.png)

   ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200708162432.png)



#### PDF增加大纲书签

![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210214231022.png)

##### PDF阅读器不显示部分文字

* 方法：Chrome打开







