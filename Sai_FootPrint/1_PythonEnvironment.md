# 搭建Python环境

### 安装miniconda

1. [下载](https://docs.conda.io/en/latest/miniconda.html)并安装

   ```bash
   $ cd ~/Downloads
   $ sh Miniconda3-latest-MacOSX-x86_64.sh
   
   Do you accept the license terms? [yes|no]
   [no] >>> yes
   
   Do you wish the installer to initialize Miniconda3 by running conda init? [yes|no]
   [yes] >>> yes
   
   modified      /Users/sai/.zshrc
   Thank you for installing Miniconda3!
   ```

   > 一路`空格`略过读license的过程

2. 重新加载配置文件：`source ~/.zshrc`

3. 替换源

   ```bash
   $ conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/main/
   $ conda config --add channels https://mirrors.ustc.edu.cn/anaconda/pkgs/free/
   $ conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/
   $ conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/msys2/
   $ conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/bioconda/
   $ conda config --add channels https://mirrors.ustc.edu.cn/anaconda/cloud/menpo/
   
   $ conda config --set show_channel_urls yes
   $ conda info
   ```

   > 报错：`CondaHTTPError: HTTP 000 CONNECTION FAILED for url <https://mirrors.ustc.edu.cn/anaconda/cloud/conda-forge/osx-64/current_repodata.json>`
   >
   > 解决：将https改为http即可
   >
   > $ open ~/.condarc

4. 升级conda：`conda upgrade conda`

#### 卸载miniconda

1. 删除目录

   ```bash
   $ rm -rf ~/miniconda3
   ```

2. 删除下面关于conda的配置

   ```bash
   # >>> conda initialize >>>
   # !! Contents within this block are managed by 'conda init' !!
   __conda_setup="$('/Users/sai/miniconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
   if [ $? -eq 0 ]; then
       eval "$__conda_setup"
   else
       if [ -f "/Users/sai/miniconda3/etc/profile.d/conda.sh" ]; then
           . "/Users/sai/miniconda3/etc/profile.d/conda.sh"
       else
           export PATH="/Users/sai/miniconda3/bin:$PATH"
       fi
   fi
   unset __conda_setup
   # <<< conda initialize <<<
   ```

3. 删除相关隐藏文件

   ```bash
   rm -rf ~/.condarc ~/.conda ~/.continuum
   ```

4. 重新加载配置文件：`source ~/.zshrc`





## Anaconda

#### 搭建环境

* 官网下载后默认安装即可  
* 搜索anaconda3，得知安装路径是/opt/anaconda3
* 在环境变量中添加anaconda3的路径
    > ```
    > open ~/.bash_profile
    > 在最后插入一行：export PATH="/opt/anaconda3/bin:$PATH"
    > source ~/.bash_profile
    > ```
* 在oh-my-zsh中添加anaconda3的路径
    > ```
    > open ~/.zshrc
    > 在第三行插入一行：export PATH="/opt/anaconda3/bin:$PATH"
    > source ~/.zshrc
    > ```
* 给conda挂代理  
    > ```
    > open ~/.condarc
    > 最后插入几行
    > proxy_servers:
    >   http: http://127.0.0.1:1081
    >   https: https://127.0.0.1:1081
    > ```

#### 卸载anaconda

* 安装卸载插件

  ```bash
  $ conda install anaconda-clean
  $ anaconda-clean
  $ rm -r /Users/sai/.anaconda_backup/2020-04-24T164213    #删除备份
  ```

* 删除Anaconda的文件夹

  ```bash
  $ which conda
  /opt/anaconda3/bin/conda
  $ sudo rm -rf /opt/anaconda3
  ```

* 删除 `~/.bash_profile`中anaconda的环境变量，即删除最后一行：`export PATH="/opt/anaconda3/bin:$PATH"`

* 删除Anaconda的可能存在隐藏的文件：`rm -rf ~/.condarc ~/.conda ~/.continuum`

  

#### 基础用法

* 查看当前系统下的虚拟环境   `conda info --envs`
  
* 激活base虚拟环境(base是默认创建的)   `source activate base`
* 退出虚拟环境   `conda deactivate`
* 创建名为 py2 的python2.7的虚拟环境   `conda create -n py2 python=2.7`
* 创建名为 py3 的python3.7的虚拟环境   `conda create -n py3 python=3.7`
* 虚拟环境的安装路径
  
    > /Users/jiangsai02/opt/anaconda3/envs
* 激活虚拟环境 py3   `source activate py3`
* 切换虚拟环境 py3 到flask_py3  
    > ```bash
    > conda deactivate
    > source activate flask_py3
    > ```
    >
    > 虚拟环境的切换原理：修改环境变量 $PATH
    >
    > 1. 系统环境下执行 `echo $PATH`
    >
    >    ```bash
    >    echo $PATH
    >    /opt/anaconda3/condabin:/opt/anaconda3/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
    >    ```
    >
    > 2. py3虚拟环境下执行 `echo $PATH`
    >
    >    ```bash
    >    echo $PATH
    >    /opt/anaconda3/envs/py3/bin:/opt/anaconda3/condabin:/opt/anaconda3/bin:/usr/local/bin:/usr/bin:/bin:/usr/sbin:/sbin
    >    ```
    >
    >    py3虚拟环境的 $PATH 前面增加了一段 `/opt/anaconda3/envs/py3/bin:`
* 删除虚拟环境 py3   `conda env remove -n py3`
* 为当前的虚拟环境 flask_py3 安装flask包   `conda install flask`
* 虚拟环境下包的安装路径

    > /Users/jiangsai02/opt/anaconda3/envs/flask_py3/lib/python3.7/site-packages/flask
* 为当前的虚拟环境 flask_py3 更新flask包   `conda update flask`
* 为当前的虚拟环境 flask_py3 卸载flask包   `conda remove flask`
* 查看当前的虚拟环境 flask_py3 的所有安装包   `conda list`



## VSCode配置

1. 左侧最下方“Extensions”，安装以下插件
    1. Python - 代码分析，高亮，规范化
    2. Bracket Pair Colorizer - 括号颜色
    3. Anaconda Extension Pack - 代码提示增强
    4. Python Extension Pack(Don Jayamanne) - 代码补全
    5. Live Server - 保存即可实施预览html（右键Open with live server）
    6. Auto Rename Tag - 同步修改html前后标签名
2. 查看Python版本路径
    > ```bash
    > $ which python
    >    /Users/jiangsai02/opt/anaconda3/bin/python
    > $ which python3
    >    /Users/jiangsai02/opt/anaconda3/bin/python3
    > ```

3. 配置VS Code中用户配置
    > code - preference - settings，点击右上角的open settings(UI)，输入
    > ```js
    > {
    >     "python.venvPath":"/Users/sai/miniconda3/envs",
    >     "python.pythonPath": "/Users/sai/miniconda3/envs/flask_py3/bin/python",
    >     "workbench.startupEditor": "newUntitledFile",
    >     "terminal.integrated.inheritEnv": false,
    >     "editor.minimap.enabled": false,
    >     "editor.suggestSelection": "first",
    >     "vsintellicode.modify.editor.suggestSelection": "automaticallyOverrodeDefaultValue",
    >     "python.jediEnabled": false,
    >     "terminal.integrated.shell.osx": "/bin/zsh",
    >     "editor.renderControlCharacters": true,
    >     "editor.renderWhitespace": "all",
    >     "editor.suggest.snippetsPreventQuickSuggestions": false,
    >     "python.linting.enabled": true, //格式化python代码
    >     "editor.formatOnType": true, //保存时自动格式化html代码
    >     "editor.formatOnSave": true,
    > }
    > ```
    >
    > > `"python.linting.enabled"`无法格式化python的缩进，因为对python而言，缩进是语法，语法错误是格式化工具是无效的
    
4. 改变当前python运行环境

    * 手动修改 `python.pythonPath`的值，重启

    * 点击左下角的运行环境，选择想使用的环境即可

      <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200208131736.png" style="zoom:40%;" />

5. 设置当前debug调试配置

    <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200218183754.png" style="zoom:33%;" />

    ```js
    {
        "version": "0.2.0",
        "configurations": [
            {
                "name": "Python: 用vscode内部终端调试",
                "type": "python",
                "request": "launch",
                "program": "${file}",  //调试当前打开的文件
                "console": "integratedTerminal"
            },
            {
                "name": "Python: 用系统终端调试",
                "type": "python",
                "request": "launch",
                "program": "${file}",
                "console": "externalTerminal"
            },
            {
                "name": "Python: 调试quotes",
                "type": "python",
                "request": "launch",
                "module": "scrapy",
                "cwd": "${workspaceRoot}/QuotesSpider", //项目目录，${workspaceRoot}是当前目录
                "args": [
                    "crawl", //执行命令
                    "quotes" //爬虫名
                ]
            }
        ]
    }
    ```

6. debug状态下交互调试

    ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200429002831.png)

7. VSCode 代码无提示的解决办法

    > 点击右下角的当前文件类型，选择 "Auto Detect 自动检测"，等它加载一会即可自动提示

    <img src="https://gitee.com/jiangsai0502/PicBedRepo/raw/master/20200208131258.png" style="zoom:40%;" />

8. unresolved import "xxx"

    > code - preference - settings，搜索 jedi，勾选

9. 验证Python程序的运行环境

    ```python
    import platform
    print("platform = ",platform.python_version())
    ```

10. vscode列选中

    option+shift，光标拖动



#### 完全卸载VSCode

1. vscode拖入废纸篓

   ```bash
   rm -rf "/Applications/Visual Studio.app"
   rm -rf ~/Library/Caches/VisualStudio
   rm -fr ~/Library/Caches/com.microsoft.VSCode
   rm -fr ~/Library/Caches/com.microsoft.VSCode.ShipIt/
   rm -rf ~/Library/Preferences/VisualStudio
   rm -rf ~/Library/Preferences/Visual\ Studio
   rm -fr ~/Library/Preferences/com.microsoft.VSCode.helper.plist
   rm -fr ~/Library/Preferences/com.microsoft.VSCode.plist
   rm -rf ~/Library/Preferences/Xamarin/
   rm -fr ~/Library/Application\ Support/Code/
   rm -rf ~/Library/Application\ Support/VisualStudio
   rm -rf ~/Library/Application\ Support/VisualStudio/7.0/LocalInstall/Addins/
   rm -rf ~/Library/Application\ Support/VisualStudio/8.0/LocalInstall/Addins/
   rm -rf ~/Library/Logs/VisualStudio
   rm -rf ~/Library/VisualStudio
   rm -fr ~/Library/Saved\ Application\ State/com.microsoft.VSCode.savedState/
   rm -fr ~/.vscode/
   rm -rf ~/.vscode*
   ```

   