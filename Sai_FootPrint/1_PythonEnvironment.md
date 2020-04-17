# 搭建Python环境

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
    >   http: http://127.0.0.1:1087
    >   https: https://127.0.0.1:1087
    > ```

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
    > Python - 代码分析，高亮，规范化
    >
    > Bracket Pair Colorizer - 括号颜色
    >
> Anaconda Extension Pack - 代码提示增强
    >
    > Python Extension Pack(Don Jayamanne) - 代码补全

2. 查看Python版本路径
    > ```js
    > which python
    >    /Users/jiangsai02/opt/anaconda3/bin/python
    > which python3
    >    /Users/jiangsai02/opt/anaconda3/bin/python3
    > ```

3. 配置VS Code中用户配置
    > code - preference - settings，点击右上角的open settings(UI)，输入
    > ```js
    > {
    >  "python.pythonPath": "/Users/jiangsai02/opt/anaconda3/envs/py3/bin/python",
    >  "workbench.startupEditor": "newUntitledFile",
    >  "terminal.integrated.inheritEnv": false,
    >  "editor.minimap.enabled": false,
    >  "editor.suggestSelection": "first",
    >  "vsintellicode.modify.editor.suggestSelection": "automaticallyOverrodeDefaultValue",
    >  "python.jediEnabled": false,
    >  "terminal.integrated.shell.osx": "/bin/zsh",
    >  "editor.renderControlCharacters": true,
    >  "editor.renderWhitespace": "all",
    >  "editor.suggest.snippetsPreventQuickSuggestions": false,
    > }
    > ```
    
4. 改变当前python运行环境

    * 手动修改 `python.pythonPath`的值，重启

    * 点击左下角的运行环境，选择想使用的环境即可

      <img src="https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/20200208131736.png" style="zoom:40%;" />

5. 设置当前debug调试配置

    <img src="https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/20200218183754.png" style="zoom:33%;" />

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

    

6. VSCode 代码无提示的解决办法

    > 点击右下角的当前文件类型，选择 "Auto Detect 自动检测"，等它加载一会即可自动提示

    <img src="https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/20200208131258.png" style="zoom:40%;" />

7. unresolved import "xxx"

    > code - preference - settings，搜索 jedi，勾选

8. 验证Python程序的运行环境

    ```python
    import platform
    print("platform = ",platform.python_version())
    ```



