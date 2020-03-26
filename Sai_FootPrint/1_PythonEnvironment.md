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



## MySql 安装

#### dmg 安装 mysql

1. 安装 mysql 数据库：

   [下载链接](https://downloads.mysql.com/archives/community/)

   [安装步骤](https://www.jianshu.com/p/833f388da8e3)

2. 查看mysql进程是否存在   `ps aux | grep mysql`

3. 测试数据库

   1. mysql 默认安装在 /usr/local/mysql，该目录下有对应的bin、lib、doc等目录

      `cd /usr/local/mysql && ls`

   2. 在bin目录下，执行 ./mysql -u root -p ，输入安装时设置的初始化密码，即可看到mysql版本信息和mysql命令行界面

      `cd bin && ./mysql -u root -p`

4. 配置环境变量   `open ~/.bash_profile`  文件最后新起一行，插入下面两行代码

   ```bash
   export PATH=$PATH:/usr/local/mysql/bin
   export PATH=$PATH:/usr/local/mysql/support-files
   ```

   

5. 操作数据库（命令行）

   1. 启动MySQL服务12   `sudo mysql.server start`

   2. 停止MySQL服务   `sudo mysql.server stop`

   3. 重启MySQL服务    `sudo mysql.server restart`

   4. 查看MySQL服务状态    `sudo mysql.server status`

   5. 进入MySQL   `mysql -u root -p`

   6. 修改root密码（必须修改，否则将来莫名报错）   `ALTER USER 'root'@'localhost' IDENTIFIED BY 'sai'; `

   7. 退出MySQL   `exit`

      > 错误： ERROR! MySQL server PID file could not be found!  [参考方案](https://blog.51cto.com/dahui09/1841627)
      >
      > 1. 重启 sql：系统偏好设置 - MySQL

   

#### brew 安装 mysql

1. 安装 MySQL：`brew  install mysql`

2. 启动 MySQL：`brew services start mysql`

3. 重启 MySQL：`brew services restart mysql`

4. 停止 MySQL：`brew services stop mysql`

5. 登录 MySQL：`mysql -u root -p`
   
    > 第一次登录没有密码，回车即可进入
    
6. 设置 MySQL 初始密码 ：`mysql_secure_installation`

7. 修改 MySQL 密码 

    > 1. 查看 mysql 初始的密码策略
    >
    >    >  `SHOW VARIABLES LIKE 'validate_password%';`
    >    >
    >    > ```sql
    >    > +--------------------------------------+-------+
    >    > | Variable_name                        | Value |
    >    > +--------------------------------------+-------+
    >    > | validate_password.check_user_name    | ON    |
    >    > | validate_password.dictionary_file    |       |
    >    > | validate_password.length             | 4     |
    >    > | validate_password.mixed_case_count   | 1     |
    >    > | validate_password.number_count       | 1     |
    >    > | validate_password.policy             | LOW   |
    >    > | validate_password.special_char_count | 1     |
    >    > +--------------------------------------+-------+
    >    > ```
    >    >
    >    > 
    >
    > 2. 设置密码的验证强度等级  `set global validate_password.policy = LOW;`
    >
    > 3. 设置密码的长度  `set global validate_password.length = 3;`
    >
    >    > 4位密码是最小限度，只要设置密码的长度小于 3 ，都将自动设值为 4
    >
    > 4. 修改密码  
    >
    >    `ALTER USER 'root'@'localhost' IDENTIFIED WITH mysql_native_password BY 'will';`



#### SSH远程登录数据库

1. 连接远程服务器：`ssh user@remote -p port`
   * user 是你在远程机器上的用户名
   * remote 是远程机器的地址，可以是 IP或域名
   * port 是 SSH Server 监听的端口，如果不指定的话就为默认值 22
   * 执行完该指令后，输入密码，随后即可登录远程服务器



#### 配置数据库工具 **Sequel Pro**

1. **查看 MySQL 端口号**

   > `show global variables like 'port';`
   >
   > ```sql
   > +---------------+-------+
   > | Variable_name | Value |
   > +---------------+-------+
   > | port          | 3306  |
   > +---------------+-------+
   > ```

2. **配置 Sequel Pro**

   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/20200128104320.png)

3. 