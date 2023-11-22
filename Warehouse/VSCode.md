

##### Vscode配置

> [教程](https://developer.aliyun.com/article/1053197)
>
> 1. 左侧最下方“Extensions”，安装以下插件
>
>    1. Python - 代码分析，高亮，规范化
>    2. Anaconda Extension Pack - 代码提示增强
>    3. Python Extension Pack(Don Jayamanne) - 代码补全
>    4. Error Lens - 错误实时提示
>    5. Highlight Matching Tag - 相同选中时高亮
>    6. Live Server - 保存即可实施预览html（右键Open with live server）
>    7. Auto Rename Tag - 同步修改html前后标签名
>    8. Black Formatter - python格式美化工具
>    9. TONGYI Lingma - 代码注释生成器（牛逼）
>
> 2. 查看Python版本路径
>
>    > ```bash
>    > which python ; which python3
>    > # /Users/sai/opt/anaconda3/bin/python
>    > # /Users/sai/opt/anaconda3/bin/python3
>    > ```
>
> 3. 配置VS Code中用户配置
>
>    > code - preference - settings，点击右上角的open settings(UI)，输入
>    >
>    > ```js
>    > {
>    > // 主题设为淡黄色
>    > "workbench.colorTheme": "Solarized Light",
>    > "terminal.integrated.inheritEnv": false,
>    > "editor.minimap.enabled": false,
>    > "git.openRepositoryInParentFolders": "always",
>    > "python.defaultInterpreterPath": "/Users/jiangsai/anaconda3/envs/py3/bin/python",
>    > "security.workspace.trust.untrustedFiles": "open",
>    > // 编辑器保存任何文件时都格式美化
>    > "editor.formatOnSave": true,
>    > "[python]": {
>    >  // python文件保存时格式美化
>    >  "editor.formatOnSaveMode": "file",
>    >  "editor.formatOnSave": true,
>    >  // black-formatter设为python文件格式美化工具
>    >  "editor.defaultFormatter": "ms-python.black-formatter"
>    > },
>    > // black-formatter插件的每行允许的字符数默认最大为88，此处改为110
>    > "black-formatter.args": [
>    >  "--line-length",
>    >  "110"
>    > ]
>    > }
>    > ```
>
> 4. 改变当前python运行的虚拟环境
>
>    1. CTRL+P打开搜索，输入""> select interpreter"
>
>    2. 选择Python解释器
>
>    3. 点击左下角的当前运行环境，重新选择运行环境
>
>       ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307051108205.png)
>
> 5. 设置当前debug调试配置
>
>    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307062309938.png)
>
>    ```js
>    {
>        "version": "0.2.0",
>        "configurations": [
>            {
>                "name": "Python: 用vscode内部终端调试",
>                "type": "python",
>                "request": "launch",
>                "program": "${file}",  //调试当前打开的文件
>                "console": "integratedTerminal"
>            },
>            {
>                "name": "Python: 用系统终端调试",
>                "type": "python",
>                "request": "launch",
>                "program": "${file}",
>                "console": "externalTerminal"
>            },
>            {
>                "name": "Python: 调试quotes",
>                "type": "python",
>                "request": "launch",
>                "module": "scrapy",
>                "cwd": "${workspaceRoot}/QuotesSpider", //项目目录，${workspaceRoot}是当前目录
>                "args": [
>                    "crawl", //执行命令
>                    "quotes" //爬虫名
>                ]
>            }
>        ]
>    }
>    ```
>
> 6. debug状态下交互调试
>
>    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307062003989.png)
>
> 7. VSCode 代码无提示的解决办法
>
>    > 点击右下角的当前文件类型，选择 "Auto Detect 自动检测"，等它加载一会即可自动提示
>    >
>    > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202307062003261.png)
>
> 8. 验证Python程序的运行环境
>
>    ```python
>    import platform
>    print("platform = ",platform.python_version())
>    ```

##### JS调试

* 安装`Live Server`插件

![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311111221157.png)

>* 浏览器地址：`http://127.0.0.1:5500/文件名`
>
>* 保存即自动执行

##### Jupyter用法

> [教程](https://zhuanlan.zhihu.com/p/139776843)
>
> 1. 安装
>
>    ```bash
>    # 切换到虚拟环境
>    conda activate py3
>    # 安装jupyter
>    conda install jupyter
>    # 安装ipykernel
>    conda install ipykernel
>    # 创建一个新的 kernel 
>    python -m ipykernel install --user --name py3 --display-name "py3_kernel"
>    # 启动jupyter
>    jupyter notebook
>    ```
>
> 2. 网页中使用
>
>    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311201711904.png)
>
> 3. VSCode中使用
>
>    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311202336112.png)