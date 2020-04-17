## 安装

#### 1. dmg 安装 MySql

1. 安装 MySql 数据库：[下载链接](https://downloads.mysql.com/archives/community/)，[安装步骤](https://www.jianshu.com/p/833f388da8e3)

2. 查看MySql进程是否存在   `ps aux | grep mysql`

3. 测试数据库

   1. MySql默认安装路径

      ```bash
      $ which mysql
      /usr/local/mysql
      ```

   2. 该路径下有bin、lib、doc等目录

      `cd /usr/local/mysql && ls`

   3. 在bin目录下，执行 `./mysql -u root -p` ，输入安装时设置的初始化密码，即可看到mysql版本信息和mysql命令行界面

      `cd bin && ./mysql -u root -p`

4. 配置环境变量   `open ~/.bash_profile`  文件最后新起一行，插入下面两行代码

   ```bash
   export PATH=$PATH:/usr/local/mysql/bin
   export PATH=$PATH:/usr/local/mysql/support-files
   ```

5. 操作数据库

   1. 启动：`mysql.server start`

   2. 停止：`mysql.server stop`

   3. 重启 ：`mysql.server restart`

   4. 查看状态 ：`mysql.server status`

   5. 登录：`mysql -u root -p`

      * `mysql -h 主机名 -u 用户名 -p`
        * **-h** : 指定要登录的 MySQL 主机名, 登录本机(localhost 或 127.0.0.1)，该参数可以省略
        * **-u** : 登录的用户名
        * **-p** : 告诉服务器将会使用密码登录, 若密码为空, 可忽略此选项

   6. 修改root密码（必须修改，否则将来莫名报错）：`ALTER USER 'root'@'localhost' IDENTIFIED BY 'sai'; `

   7. 退出MySQL： `exit`

      > 错误： ERROR! MySQL server PID file could not be found!  [参考方案](https://blog.51cto.com/dahui09/1841627)
      >
      > 1. 重启 sql：系统偏好设置 - MySQL

6. 卸载

   ```bash
   备份数据库
   系统偏好设置 - Stop MySQL Server - Uninstall
   sudo rm /usr/local/mysql;
   sudo rm -rf /usr/local/mysql*;
   sudo rm -rf /Library/StartupItems/MySQLCOM;
   sudo rm -rf /Library/PreferencePanes/My*;
   vim /etc/hostconfig (and removed the line MYSQLCOM=-YES-);
   sudo rm -rf ~/Library/PreferencePanes/My*;
   sudo rm -rf /Library/Receipts/mysql*;
   sudo rm -rf /Library/Receipts/MySQL*;
   sudo rm -rf /private/var/db/receipts/*mysql*;
   sudo rm -rf /var/db/receipts/com.mysql.*;
   ```

   * 检查卸载是否干净

     ```bash
     ls /usr/local/bin 里的*mysql*相关文件
     ls /usr/local/Cellar 里的mysql文件
     ls /usr/local/var 里的mysql文件
     ls /tmp 里的mysql.sock, mysql.sock.lock, my.cnf文件
     ```

#### 2. brew 安装 MySQL

1. 安装 ：`brew install mysql`

2. 查看版本：`mysqladmin --version`

3. 启动 ：`mysql.server start`

4. 重启 ：`mysql.server restart`

5. 停止 ：`mysql.server stop`

6. 查看状态：`mysql.server status`

7. 初始化：`mysql_secure_installation`

8. 登录：  `mysql -u root -p`

   > 第一次登录没有密码，回车即可进入

   1. 修改密码：`alter user 'root'@'localhost' identified with mysql_native_password by 'sai';`

      > 密码改成sai

9. 设置安全配置：`mysql_secure_installation`

   ```bash
   $ mysql_secure_installation
   
   Securing the MySQL server deployment.
   Enter password for user root:    #输入密码sai
   
   VALIDATE PASSWORD COMPONENT can be used to test passwords and improve security. It checks the strength of password and allows the users to set only those passwords which are secure enough. Would you like to setup VALIDATE PASSWORD component?
   
   Press y|Y for Yes, any other key for No:   #设置安全密码，3种安全密码都是8位以上的。没必要，输入n
   
   ... skipping.
   By default, a MySQL installation has an anonymous user, allowing anyone to log into MySQL without having to have a user account created for them. This is intended only for testing, and to make the installation go a bit smoother. You should remove them before moving into a production environment.
   
   Remove anonymous users? (Press y|Y for Yes, any other key for No) :   #删除匿名用户，回车即可
   
    ... skipping.
   Normally, root should only be allowed to connect from 'localhost'. This ensures that someone cannot guess at the root password from the network.
   
   Disallow root login remotely? (Press y|Y for Yes, any other key for No) :   #禁止远程登录root，回车即可
   
    ... skipping.
   By default, MySQL comes with a database named 'test' that anyone can access. This is also intended only for testing, and should be removed before moving into a production
   environment.
   
   Remove test database and access to it? (Press y|Y for Yes, any other key for No) :   #删除测试库，回车即可
   
    ... skipping.
   Reloading the privilege tables will ensure that all changes made so far will take effect immediately.
   
   Reload privilege tables now? (Press y|Y for Yes, any other key for No) :   #重新加载权限表，回车即可
   
    ... skipping.
   All done!
   ```

10. 卸载

    * 查看安装路径：`brew list mysql`

    * 步骤

      ```bash
      停止数据库服务器
      sudo rm /usr/local/mysql
      sudo rm -rf /usr/local/mysql*
      sudo rm -rf /Library/StartupItems/MySQLCOM
      sudo rm -rf /private/var/db/receipts/mysql
      ```

11. 备注

    > 1. 查看 mysql 初始的密码策略
    >
    >    >  `SHOW VARIABLES LIKE 'validate_password%';`
    >    >
    >    >  ```sql
    >    >  +--------------------------------------+-------+
    >    >  | Variable_name                        | Value |
    >    >  +--------------------------------------+-------+
    >    >  | validate_password.check_user_name    | ON    |
    >    >  | validate_password.dictionary_file    |       |
    >    >  | validate_password.length             | 4     |
    >    >  | validate_password.mixed_case_count   | 1     |
    >    >  | validate_password.number_count       | 1     |
    >    >  | validate_password.policy             | LOW   |
    >    >  | validate_password.special_char_count | 1     |
    >    >  +--------------------------------------+-------+
    >    >  ```
    >    >
    >    >  
    >
    > 2. 设置密码的验证强度等级  `set global validate_password.policy = LOW;`
    >
    > 3. 设置密码的长度  `set global validate_password.length = 3;`
    >
    >    > 4位密码是最小限度，只要设置密码的长度小于 3 ，都将自动设值为 4

12. 报错

    1. `ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/tmp/mysql.sock' (62)`
       * [参考](https://segmentfault.com/a/1190000007536436)
       * 查看mysql错误日志：`cat /usr/local/var/mysql/xxx-mini.local.err`
       *  [NOTE] 和 [WARNING] 可以不用管它，我直接找到了 [ERROR] 即错误信息，发现是没有读写权限
       * 查看mysql在Mac中的用户名`_mysql`：`dscl . list /Users | grep my`
       * 把mysql文件夹的拥有者改成`_mysql`：`sudo chown -R _mysql /usr/local/Cellar/mysql`



#### 3. 安装测试库

* 安装官方库[参考](https://www.cnblogs.com/omsql/p/9489091.html)

  1. 下载repository文件到`temp`目录

     ```bash
     $ cd temp
     $ unzip test_db-master.zip
     $ mysql -u root -p -t < employees.sql   #安装数据
     $ mysql -u root -p -t < employees_partitioned.sql   #安装数据
     $ mysql -u root -p -t < test_employees_md5.sql   #测试安装的数据
     ```

  2. 

#### 4. SSH远程登录数据库

1. 连接远程服务器：`ssh user@remote -p port`

   * user 是你在远程机器上的用户名

   * remote 是远程机器的地址，可以是 IP或域名

   * port 是 SSH Server 监听的端口，如果不指定的话就为默认值 22

   * 执行完该指令后，输入密码，随后即可登录远程服务器

     



#### 5. 配置数据库工具 **Sequel Pro**

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






## 教程

#### 1. 数据库一览

1. 展示所有数据库

   ```bash
   mysql> SHOW DATABASES;
   +--------------------+
   | Database           |
   +--------------------+
   | employees          |
   | mysql              |
   | sys                |
   +--------------------+
   ```

2. 进入/切换数据库

   ```bash
   mysql> use mysql;
   Reading table information for completion of table and column names
   You can turn off this feature to get a quicker startup with -A
   Database changed
   
   mysql> use employees;
   Reading table information for completion of table and column names
   You can turn off this feature to get a quicker startup with -A
   Database changed
   ```

   > 切换数据库，直接`use 数据库名称;`即可

3. 查看当前数据库

   ```bash
   mysql> select database();
   +------------+
   | database() |
   +------------+
   | employees  |
   +------------+
   ```

4. 展示所有表

   ```bash
   mysql> SHOW TABLES;
   +----------------------+
   | Tables_in_employees  |
   +----------------------+
   | current_dept_emp     |
   | departments          |
   | dept_emp             |
   | dept_emp_latest_date |
   | dept_manager         |
   | employees            |
   | salaries             |
   | titles               |
   +----------------------+
   ```

5. 展示表结构

   ```bash
   mysql> SHOW COLUMNS FROM departments;
   +-----------+-------------+------+-----+---------+-------+
   | Field     | Type        | Null | Key | Default | Extra |
   +-----------+-------------+------+-----+---------+-------+
   | dept_no   | char(4)     | NO   | PRI | NULL    |       |
   | dept_name | varchar(40) | NO   | UNI | NULL    |       |
   +-----------+-------------+------+-----+---------+-------+
   ```

6. 退出数据库

   ```bash
   mysql> exit;
   Bye
   ```

   

#### 2. 数据库管理

1. 创建并进入数据库

   ```bash
   mysql> CREATE DATABASE IF NOT EXISTS sai0417;
   
   mysql> SHOW DATABASES;
   ```

2. 创建2张表

   ```bash
   mysql> use sai0417;
   
   mysql> CREATE  TABLE  student (
       -> id  INT(10)  NOT NULL  UNIQUE  PRIMARY KEY  ,
       -> name  VARCHAR(20)  NOT NULL ,
       -> sex  VARCHAR(4)  ,
       -> birth  YEAR,
       -> department  VARCHAR(20) ,
       -> address  VARCHAR(50)
       -> );
   
   mysql> CREATE  TABLE  score (
       -> id  INT(10)  NOT NULL  UNIQUE  PRIMARY KEY  AUTO_INCREMENT ,
       -> stu_id  INT(10)  NOT NULL ,
       -> c_name  VARCHAR(20) ,
       -> grade  INT(10)
       -> );
   ```

3. 插入数据

   

4. 删除数据库







