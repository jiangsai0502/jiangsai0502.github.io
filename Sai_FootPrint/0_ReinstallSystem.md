# 重装系统
### 常备软件安装

| sougou     | 微信        | Chrome    | office                  |
| ---------- | ----------- | --------- | ----------------------- |
| PDF expert | snipaste    | itsycal   | istat menusistat menus  |
| Picgo      | Snagit      | sublime   | Paste（官网下载helper） |
| Permute    | QQ          | Mweb      | bettertouchtool         |
| ScreenFlow | Axure       | 欧路      | go2shell（官网下载）    |
| xcode      | Appcleaner  | stretchly | GitHub Desktop          |
| brew       | Anaconda    | Anki      | Parallels Desktop       |
| Photoshop  | 百度云盘    | iMoive    | 网易邮箱大师            |
| Typora     | XMind ZEN   | ename     | ShadowsocksX            |
| ezip       | Caffeinated | draw.io   | Dr. Unarchiver          |

```bash
brew install youtube-dl

brew install you-get

brew cask install stretchly

# tree 可生成当前目录内子目录的优美树状图
# tree -a 显示包括隐藏文件在内的所有文件的树状图
brew install tree

brew cask install mpv

# Finder顶端显示完整路径
defaults write com.apple.finder _FXShowPosixPathInTitle -bool YES

# 启动台图标数量
defaults write com.apple.dock springboard-rows -int 7;
defaults write com.apple.dock springboard-columns -int 11;
defaults write com.apple.dock ResetLaunchPad -bool true;killall Dock

# 创建配置文件：~/.config/mpv/input.conf
AXIS_UP  add volume 2
AXIS_DOWN  add volume -2
AXIS_LEFT  seek -2 exact
AXIS_RIGHT seek 2 exact
LEFT  seek -2 exact
RIGHT  seek 2 exact
UP  add volume 2
DOWN  add volume -2

```





* iterm2   `brew cask install iterm2`
  
    * 打开 Go2Shell 配置页，将自动调用设置为iterm2
    
         `open -a Go2Shell --args config`
    
    * 设置 iterm2 的快捷键
      
        > 1. 光标按照单词快速移动
        >
        >    iTerm2 -> Preferences -> Keys -> Key Bindings
        >
        >    修改 ⌘← 和 ⌘→ 的映射，双击进入后，选择Action为 “Send Escape Sequence”，Esc+为 ⌘← 对应 b ， ⌘→ 对应 f
        >
        >    ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200131101305.png)
        >    
        > 2. 按照单词快速删除（结合BetterTouchTool）
        >
        >    修改 ⌘+Delete 的映射，⌘+Delete 代表 control + w
        >
        >    ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200429144312.png)
        
    * 安装Oh my zsh
      
        ```bash
        sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"
        open ~/.zshrc
        # 在.zshrc文件中搜索 source $ZSH/oh-my-zsh.sh，只本句之前加一句
        ZSH_DISABLE_COMPFIX="true"
        source $ZSH/oh-my-zsh.sh
        ```
        
    * 安装PowerLine
    
        ```json
        sudo easy_install pip;
        pip install powerline-status --user
        ```
        
    * 安装PowerFonts字体
    
      ```json
      mkdir ~/Documents/Temp;
      git clone https://github.com/powerline/fonts.git --depth=1;
      ./fonts/install.sh
      ```
    
      设置字体：iTerm2 -> Preferences -> Profiles -> Text，在Font区域选中Change Font，然后找到Meslo LG字体，有L、M、S可选
      ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200112165201.png)
    
    * 安装配色方案
    
      ```json
      cd ~/Documents/Temp;
      git clone https://github.com/altercation/solarized/ --config http.proxy='http://127.0.0.1:1081';
      cd solarized/iterm2-colors-solarized/;
      open solarized/iterm2-colors-solarized/
      ```
    
      设置配色：iTerm2 -> Preferences -> Profiles -> Colors -> Color Presets
    
      ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200112182935.png)
      
    * 修改主题
    
      > ```bash
      > cd ~/Documents/Temp;
      > git clone https://github.com/fcamblor/oh-my-zsh-agnoster-fcamblor.git --config http.proxy='http://127.0.0.1:1081';
      > ./oh-my-zsh-agnoster-fcamblor/install;
      > open ~/.zshrc
      > # 搜索'ZSH_THEME'，修改为ZSH_THEME="agnoster"
      > ----或者使用自己的主题----
      > https://github.com/jiangsai0502/WillFileStore
      > 1.把主题文件WillTheme.zsh-theme放入/Users/sai/.oh-my-zsh/themes
      > 2.open ~/.zshrc
      > 3.修改ZSH_THEME="WillTheme"
      > ```
    
    * 安装高亮插件
    
      > ```bash
      > brew install zsh-syntax-highlighting
      > open ~/.zshrc
      > 最后插入一行：source /usr/local/share/zsh-syntax-highlighting/zsh-syntax-highlighting.zsh
      > source ~/.zshrc
      > ```
      
    * 自动提示与命令补全
    
      > ```bash
      > cd ~/.oh-my-zsh/custom/plugins/
      > git clone https://github.com/zsh-users/zsh-autosuggestions  --config http.proxy='http://127.0.0.1:1081'
      > open ~/.zshrc
      > 搜索'plugins'，修改为plugins=(zsh-autosuggestions git)
      > ```
    
* Sublime Text

    * Command + Control +G 一次性选择所有相同的词

    * 安装插件

      ```bash
      # 通过View->Show Console菜单打开命令行，输入
      import urllib.request,os; pf = 'Package Control.sublime-package'; ipp = sublime.installed_packages_path(); urllib.request.install_opener( urllib.request.build_opener( urllib.request.ProxyHandler()) ); open(os.path.join(ipp, pf), 'wb').write(urllib.request.urlopen( 'http://sublime.wbond.net/' + pf.replace(' ',' ')).read())
      # 回车自动安装
      
      # command+Shift+P，输入
      install package
      # 回车自动安装
      
      # 解决乱码问题：command+Shift+P，输入install package，弹出框，输入
      ConvertToUTF8
      # 回车自动安装
      
      # 中文汉化包：command+Shift+P，输入install package，弹出框，输入
      ChineseLocalizations
      # 回车自动安装
      ```

##### finder排序规则

<img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200808210729.png" style="zoom:40%;" />

##### Alfred搜索排除某个文件夹

1. 系统偏好设置 - Spotlight - 隐私

2. 可见文件夹：直接添加要排除的文件夹

   <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200808232048.png" style="zoom:50%;" />

3. 不可见文件夹：Finder - “前往文件夹” - 输入路径，进入文件夹 - 把要排除的文件夹拖进 Spotlight 的 隐私 窗口

4. 清空alfred缓存：调出alfred，输入reload回车

##### Alfred文件动作

![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200809145254.png)

### you-get / YouTube-dl

**you-get用法**

* 分析视频可供下载的全部格式：-i参数
  `you-get -i https://www.youtube.com/watch?v=jNQXAC9IVRw`

* 直接下载默认格式：
  `you-get https://www.youtube.com/watch?v=jNQXAC9IVRw`

* 指定下载名称

  `you-get https://www.youtube.com/watch?v=jNQXAC9IVRw -O FileName`

* 自定义下载格式：
  `you-get --itag=18 'https://www.youtube.com/watch?v=jNQXAC9IVRw'`

* 使用HTTP代理下载：
`you-get -x 127.0.0.1:1081 --itag=18 'https://www.youtube.com/watch?v=jNQXAC9IVRw'`



**youtube-dl用法**

* 下载默认类型视频（无字幕）
`youtube-dl https://www.youtube.com/watch?v=n_6p-1J551Y`
* 下载默认类型视频（有字幕）
`youtube-dl --write-auto-sub https://www.youtube.com/watch?v=n_6p-1J551Y`
* 下载视频（指定名称）
`youtube-dl https://www.youtube.com/watch?v=n_6p-1J551Y -o '你要的名字'`
* 单独下载**字幕**（无视频）
`youtube-dl --proxy 127.0.0.1:1081 --write-sub --skip-download https://www.youtube.com/watch?v=n_6p-1J551Y`
* 查看视频所有类型
`youtube-dl -F https://www.youtube.com/watch?v=n_6p-1J551Y`
* 查看视频所有字幕
`youtube-dl --list-subs https://www.youtube.com/watch?v=n_6p-1J551Y`
* 下载指定质量的视频和音频并自动合并（有字幕）
`youtube-dl -f 160+249 https://www.youtube.com/watch?v=n_6p-1J551Y`
* 下载指定质量的视频和音频并自动合并，并转码成mp4格式（有字幕）
`youtube-dl -f 160+249 --recode-video mp4 https://www.youtube.com/watch?v=n_6p-1J551Y`
* 使用代理下载默认类型的视频
`youtube-dl --proxy 127.0.0.1:1081 https://www.youtube.com/watch?v=xqdI6ljJ954`
* 使用代理下载默认类型的视频**列表**
`youtube-dl --proxy 127.0.0.1:1081 --yes-playlist https://www.youtube.com/watch?v=xqdI6ljJ954`
* 获取proxy_url:proxy_port的方式
`在Shadowsocks找到copy HTTP proxy shell export line，如‘export http_proxy=http://127.0.0.1:1081’即可提取代理地址何端口`



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

  

##### 下载bibi音频

* B站无音频格式，故会先下视频载ffmepg自动转成音频

  `youtube-dl --extract-audio https://www.bilibili.com/video/BV1xJ411r7Yo`



#### 下载工具axel

1. 安装axel：`brew install axel`

2. 下载：`axel -n 30 https://download.jetbrains.8686c.com/cpp/CLion-2017.3.dmg`

   > 30代表的是线程数



#### Mac 修改文件创建时间

`touch -mt YYYYMMDDhhmm`
示例
```bash
1. 在Terminal中输入 touch -mt 20160101  
2. 将/Users/will/Downloads/1.png拖入Terminal中
3. Terminal会显示 touch -mt 20160101 /Users/will/Downloads/123.png
4. 回车执行即可
注：改成当天 touch -m 文件名
```



#### Git 挂代理方式

`git clone https://github.com/altercation/solarized/ --config http.proxy='http://127.0.0.1:1087'`

#### Chrome 搜索后新标签打开链接

![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200216125118.png)

#### brew 挂代理方式

```bash
touch ~/.curlrc
open ~/.curlrc
输入代理地址：proxy=127.0.0.1:1081
用完可以删掉该文件，否则墙内资源会受限
rm ~/.curlrc

# 单个命令挂代理1
http_proxy=http://127.0.0.1:1081 https_proxy=http://127.0.0.1:1081 brew install PACKAGE
# 单个命令挂代理2
ALL_PROXY=socks5://127.0.0.1:1081 brew install PACKAGE
```

#### brew下载慢

**问题描述**

1. brew安装软件一直卡在Update阶段
2. 从github.com下载文件也极度缓慢

**排查**

1. 使用`brew update --verbose`观察update过程

**解决方案：[参考](https://www.cnblogs.com/tp0829/p/Homebrew.html)**

1. `Homebrew`源

   ```bash
   # 查看brew镜像源
   git -C "$(brew --repo)" remote -v
   # 修改brew镜像源
   git -C "$(brew --repo)" remote set-url origin https://mirrors.ustc.edu.cn/brew.git
   ```

   > `"$(brew --repo)"`是用来自动指向Homebrew的目录的

2. `homebrew-core`源

   ```bash
   # 查看homebrew-core镜像源
   git -C "$(brew --repo homebrew/core)" remote -v
   # 修改homebrew-core镜像源
   git -C "$(brew --repo homebrew/core)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-core.git
   ```

3. 替换`homebrew-cask`源

   ```bash
   # 查看homebrew-cask镜像源（需要安装后才能查看）
   git -C "$(brew --repo homebrew/cask)" remote -v
   # 修改homebrew-cask镜像源（需要安装后才能修改）
   git -C "$(brew --repo homebrew/cask)" remote set-url origin https://mirrors.ustc.edu.cn/homebrew-cask.git
   ```
   
4. 更新替换源

   ```bash
   brew update
   ```

   


#### pip安装慢

指定安装源：pip install jupyter -i https://pypi.tuna.tsinghua.edu.cn/simple

#### Alfred用法

1. 取消spotlight快捷键，设置Alfred快捷键

   ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200522092941.png)

   > 1. 设置Alfred的快捷键
   > 2. **Quick Search**：最常用，`Space + 关键字`快速启用打开文件，功能类似于使用`Open + 关键字`
   > 3. **Inside Files**：最常用，`in + 关键字`查找包含查询字的文件
   > 4. 预览：`shift`



### 文献阅读：沙拉查词 + Alfred

[参考](https://zhuanlan.zhihu.com/p/113809716)

1. 安装Chrome插件：沙拉查词

2. 配置浏览器外划词翻译

   > 浏览器外配置好后，其调用沙拉查词的方式同样适用于浏览器内，因此一劳永逸

   1. 在Chrome内为沙拉查词设置**全局快捷键**

      > 地址栏：chrome://extensions/shortcuts

      <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20201031151535.png" style="zoom:30%;" />

   2. 开启沙拉查词的Chrome权限

      <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20201031151255.png" style="zoom:30%;" />

   3. 配置Alfred

      1. [下载Alfred workflow脚本](https://link.zhihu.com/?target=https%3A//github.com/crimx/ext-saladict/files/3711425/saladict.alfredworkflow.zip)

      2. 双击，import脚本

      3. 设置hotkey：`control + ~`

      4. 结合BetterTouchTool修改触发条件：在PDF expert中鼠标移到底边触发`control + ~`

         <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200731184206.png" style="zoom:50%;" />

      5. 沙拉词典焦点

         1. 方法1：设置

            ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200731151246.png)

         2. 方法2：修改Run NSAppleScript脚本
   
            <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200731013451.png" style="zoom:50%;" />
   
            ```bash
            on alfred_script(q)
              tell application "System Events"
            	# 快捷键打开沙拉词典
            	key code 37 using {control down, command down}
            	delay 0.1
            	# 焦点从沙拉词典移回源文件
         	key code 48 using {command down}
              end tell
         end alfred_script
            ```

   4. 小技巧

      1. 沉浸式的`黑暗模式`

         ![C4wOBf](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/uPic/C4wOBf.png)

      2. PDF和沙拉查词并列显示

         ![0Vh7oi](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/uPic/0Vh7oi.png)

      3. 积累生词

         ![ZTryoy](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/uPic/ZTryoy.png)

      4. 生词导入Anki

         1. Anki中创建新卡片类型

            1. 点开 `Anki -> Tools -> Manage Note Types -> Add` 

            2. 选最基础的 `Add: Basic`，填写名字，如 Saladict，添加成功后，点击 `Fields` 编辑字段

            3. 默认提供了 `Front` 和 `Back` ，全部删掉或直接改名成 `Word`, `Translation`，完成后， 点击 `Cards` 编辑卡片模板

            4. 提供一个简单的模板
   
               * Front Template

                 ```html
              <p>{{Word}}</p>
                 ```
   
               * Back Template
   
                 ```html
                 {{FrontSide}}
                 
              <hr id=answer>
                 
              <p>{{Translation}}</p>
                 ```

         2. Saladict 生词本导出生词

            ![Sw0Zqw](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/uPic/Sw0Zqw.png)

            1. 选`换行替换为空格`
   
            2. 模板设为

               ```html
            %text% ` %trans%
               ```

         3. Anki导入生词
   
            ![DPmCzS](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/uPic/DPmCzS.png)
   
            1. 导入类型选 `Text separated by tabs or semicolons`
            2. `Type` 选 `Saladict`
            3. `Fields separated by: Space` 。我们换成 `
            4. 勾选`Allow HTML in fields` 。因为导出时选了 `<br>` 或 `<p>` 等 HTML排版
            5.  `Field Mapping` 是字段映射关系

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

![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200710105047.png)