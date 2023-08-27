##### 快捷键

* Chrome外的沙拉查词：⌘ + ～
* 锁屏：⌘ + L
* Snipaste截图：⌘ + 1
* OCR：⌘ + 2
* Anki挖空：⌘ + 3
* PicGo上传剪切板图片：⌘ + 4
* 新建录音：⌥ + 1
* 暂停录音：⌥ + 2
* Paste调起剪切板：⌥ + S
* 切换输入法：⌃⇧ + 空格

##### 常备软件

1. 文字处理
   1. office
   2. sublime
   3. Typora
   4. PDF expert
   5. marginote3
   6. goodnote
2. 思维梳理
   1. XMind ZEN
   2. MindNote
3. 科学上网
   1. Geph
   2. shadowrocket
4. 效率工具
   1. Keyboard Maestro
   2. Paste（官网下载helper）
   3. MurGaa Recorder
   4. rename
   5. go2shell（官网下载）
   6. magnet
   7. MacroRecorder
5. 截图：
   1. 主力贴图：snipaste
   2. 长截图：xnip
   3. 截图OCR：Easydict
6. istat menus
7. itsycal
8. App Cleaner & Uninstaller Pro
9. Photoshop
10. Permute
11. 欧路
12. flow
13. eXtra Voice Recorder Pro
14. proxyman
15. 剪映
16. downie

##### 安装brew

> 1. 命令
>
>    `/bin/zsh -c "$(curl -fsSL https://gitee.com/cunkai/HomebrewCN/raw/master/Homebrew.sh)" `
> 2. 推荐使用中科大源
> 3. brew update报错[参考](https://www.jianshu.com/p/bee56e756ece)

##### 安装mpv

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
>
> 设置mpv多开
>
> 1. 打开Script Editor
>
>    > ```
>    > on run
>    >     do shell script "open -n /Applications/mpv.app"
>    >     tell application "mpv" to activate
>    > end run
>    >
>    > on open theFiles
>    >     repeat with theFile in theFiles
>    >         do shell script "open -na /Applications/mpv.app " & quote & (POSIX path of theFile) & quote
>    >     end repeat
>    >     tell application "mpv" to activate
>    > end open
>    > ```
>    >
> 2. 保存
>
>    1. 名称：mpv multiple
>    2. 文件格式：应用程序
> 3. 将mpv multiple拖入应用程序，修改视频文件的默认打开方式

##### 安装iterm2

> 1. 命令
>
>    `brew install iterm2`
> 2. 把iTerm2设为默认
>
>    * iTerm2 -> Make ITerm2 Default Term
>
>      ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413110312.png)
> 3. 快捷键
>
>    1. 光标按照单词快速移动
>
>       * iTerm2 -> Preferences -> Keys -> Key Bindings
>
>         修改 ⌘← 和 ⌘→ 的映射，双击进入后，选择Action为 “Send Escape Sequence”，Esc+为 ⌘← 对应 b ， ⌘→ 对应 f
>
>         ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220412205506.png)
>    2. 按照单词快速删除（结合BetterTouchTool）
>
>       * 修改 ⌘+Delete 的映射，⌘+Delete 代表 control + w
>
>         ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220412210000.png)
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
>    DISABLE_AUTO_UPDATE="true"
>    source ~/.zshrc
>    ```
> 5. 安装PowerFonts字体
>
>    ```
>    1. 下载：https://github.com/powerline/fonts
>    2. 解压
>    3. 进入文件夹：cd fonts-master
>    4. 安装：./install.sh
>    ```
> 6. 设置字体
>
>    iTerm2 -> Preferences -> Profiles -> Text，在Font区域选中Change Font，然后找到Meslo LG字体，有L、M、S可选
>
>    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413112345.png)
> 7. 配色方案
>
>    iTerm2 -> Preferences -> Profiles -> Colors -> Color Presets
>
>    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413113614.png)
> 8. 设置主题
>
>    ```
>    open ~/.zshrc
>    # 搜索'ZSH_THEME'，修改为ZSH_THEME="agnoster"
>    source ~/.zshrc
>    ```
> 9. 设置语法高亮
>
>    ```
>    brew install zsh-syntax-highlighting
>
>    open ~/.zshrc
>    最后插入一行：source /opt/homebrew/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
>    source ~/.zshrc
>    ```
> 10. 获取代理地址
>
>     ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413141420.png)
> 11. 自动提示与命令补全
>
>     ```
>     下载 https://github.com/zsh-users/zsh-autosuggestions
>     解压到目录~/.oh-my-zsh/plugins/zsh-autosuggestions
>     open ~/.zshrc
>     搜索'plugins'，修改为plugins=(zsh-autosuggestions)
>     source ~/.zshrc
>     ```
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

##### 安装

> `brew install yt-dlp`（youtube-dl已死）
>
> * 查看视频所有类型
>
>   `yt-dlp -F URL（获取ID)`
>
>   ![img](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202308271236418.png)
> * 下载指定ID的视频
>
>   `yt-dlp -f ID URL`
>
>   * `yt-dlp -f 22 URL`
>   * `yt-dlp -f 242+230 URL`
> * 单独下载**字幕**（无视频）
>
>   `yt-dlp --write-subs URL`

##### 安装you-get

> `brew install you-get`
>
> * 分析视频可供下载的全部格式：-i参数
>   `you-get -i https://www.youtube.com/watch?v=jNQXAC9IVRw`
> * 直接下载默认格式：
>   `you-get https://www.youtube.com/watch?v=jNQXAC9IVRw`
> * 指定下载名称
>
>   `you-get https://www.youtube.com/watch?v=jNQXAC9IVRw -O FileName`
> * 自定义下载格式：
>   `you-get --itag=18 'https://www.youtube.com/watch?v=jNQXAC9IVRw'`
> * 使用HTTP代理下载：
>   `you-get -x 127.0.0.1:1081 --itag=18 'https://www.youtube.com/watch?v=jNQXAC9IVRw'`

##### 启动台图标数量7 x 11

> ```
> defaults write com.apple.dock springboard-rows -int 7;
> defaults write com.apple.dock springboard-columns -int 11;
> defaults write com.apple.dock ResetLaunchPad -bool true;
> killall Dock
> ```

##### Finder顶端显示完整路径

> `defaults write com.apple.finder _FXShowPosixPathInTitle -bool YES`

##### Alfred

> 1. 将Spotlight的快捷键分给Alfred
>
>    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413142827.png)
> 2. 搜索排除某个文件夹
>
>    1. 添加要排除的文件夹
>    2. 调出alfred，输入reload回车，清空alfred缓存
>
>       ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413143239.png)
>    3. 自定义文件操作
>
>       ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413143409.png)
>
>    **Quick Search**：最常用，`Space + 关键字`快速启用打开文件，功能类似于使用 `Open + 关键字`
>
>    **Inside Files**：最常用，`in + 关键字`查找包含查询字的文件

##### ClashX 设置方法

> 1. 获取订阅链接
>
>    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202111261625570.png)
> 2. 添加配置
>
>    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202111261625530.png)
>
>    `Url`: 填入订阅链接
>
>    `Config Name`：填写一个备注名称

##### brew 挂代理方式

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

##### sublime配置

> 1. 安装
>
>    > ⌘+⇧+P，输入install package，回车自动安装
>    >
> 2. 解决乱码问题
>
>    > ⌘+⇧+P，输入install package，弹出框，输入ConvertToUTF8,回车自动安装
>    >
> 3. 中文汉化包
>
>    > ⌘+⇧+P，输入install package，弹出框，输入ChineseLocalizations，回车自动安装
>    >
> 4. Ayu主题
>
>    > ⌘+⇧+P，输入install package，弹出框，输入ayu，回车自动安装
>    >
>    > 选择主题：ayu: Activate theme，选择，回车
>    >

##### Git 挂代理方式

> `git clone https://github.com/altercation/solarized/ --config http.proxy='http://127.0.0.1:1087'`

##### Chrome 搜索后新标签打开链接

##### Mac 修改文件创建时间

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

##### 文献阅读：沙拉查词 + Alfred

> [参考](https://zhuanlan.zhihu.com/p/113809716)
>
> 1. 安装Chrome插件：沙拉查词
> 2. 配置浏览器外划词翻译
>
>    > 浏览器外配置好后，其调用沙拉查词的方式同样适用于浏览器内，因此一劳永逸
>    >
>
>    1. 在Chrome内为沙拉查词设置**全局快捷键**
>
>       > 地址栏：chrome://extensions/shortcuts
>       >
>
>       ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413160100.png)
>    2. 开启沙拉查词的Chrome权限
>
>       ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413160125.png)
>    3. 配置Alfred
>
>       1. [下载Alfred workflow脚本](https://link.zhihu.com/?target=https%3A//github.com/crimx/ext-saladict/files/3711425/saladict.alfredworkflow.zip)
>       2. 双击，import脚本
>       3. 设置hotkey：`control + ~`
>       4. 结合BetterTouchTool修改触发条件：在PDF expert中鼠标移到底边触发 `control + ~`
>
>          ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413160145.png)
>       5. 沙拉词典焦点
>
>          1. 方法1：设置
>
>             ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413160217.png)
>          2. 方法2：修改Run NSAppleScript脚本
>
>             ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413160246.png)
>
>             ```bash
>             on alfred_script(q)
>               tell application "System Events"
>                 # 快捷键打开沙拉词典
>                 key code 37 using {control down, command down}
>                 delay 0.1
>                 # 焦点从沙拉词典移回源文件
>             key code 48 using {command down}
>               end tell
>             end alfred_script
>             ```
>    4. 积累生词
>
>       ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413155850.png)
>    5. Saladict 生词本导出生词
>       ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20220413155956.png)

##### Karabiner

> 问题：连外接键盘时，键位不对应
>
> 1. 修改单个键位
> 2. 修改组合快捷键[参考](https://blog.csdn.net/qq_26012495/article/details/88539120)

##### 中国大陆无法登陆某些网站（newbing、binance）

#### Subler合并视频和字幕

#### jupyter用法

> 1. 安装：
>
>    ```bash
>    # 切换虚拟环境
>    source activate py3.8
>    # 安装jupyter
>    conda install jupyter
>    # 安装支持conda虚拟环境的插件
>    conda install nb_conda
>    # 安装指定虚拟环境的kernel到notebook
>    python -m ipykernel install --user --name py3.8 --display-name "Python py3.8"
>    # 查看kernel虚拟环境
>    jupyter kernelspec list
>    # 删除指定虚拟环境的kernel
>    jupyter kernelspec remove kernel_name
>    # 
>    ```
> 2. 基本用法
>
>    ```bash
>    # 切换到jupyter文件目录
>    cd /Users/sai/Documents/Temp
>    # 启动 jupyter
>    jupyter notebook
>    # 退出 jupyter
>    `control`+`c`
>    ```
> 3. Vscode 中使用
>
>    ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200708161754.png)
>
>    ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200708162432.png)

#### PDF增加大纲书签
