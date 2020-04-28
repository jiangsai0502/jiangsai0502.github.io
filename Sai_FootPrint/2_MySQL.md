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

   1. 修改密码：`alter user 'root'@'localhost' identified with mysql_native_password by 'will';`

      > 密码改成will

9. 设置安全配置：`mysql_secure_installation`

   ```bash
   $ mysql_secure_installation
   
   Securing the MySQL server deployment.
   Enter password for user root:    #输入密码will
   
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

#### 4. SSH远程登录数据库

1. 连接远程服务器：`ssh user@remote -p port`

   * user 是你在远程机器上的用户名

   * remote 是远程机器的地址，可以是 IP或域名

   * port 是 SSH Server 监听的端口，如果不指定的话就为默认值 22

   * 执行完该指令后，输入密码，随后即可登录远程服务器

     

#### 5. 数据库工具 **Sequel Pro**

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




#### 6. 数据库工具[tableplus](https://www.macwk.com/soft/tableplus)

1. 配置

   ![ghGbNN](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/uPic/ghGbNN.png)



#### 7. 数据库工具[navicat premium](https://www.macwk.com/soft/navicat-premium)

1. 配置

   ![mk5Yqg](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/uPic/mk5Yqg.png)





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

1. 创建并进入库

   ```bash
   mysql> CREATE DATABASE IF NOT EXISTS SaiDB;
   
   mysql> SHOW DATABASES;
   ```

2. 创建表

   ```bash
   mysql> use SaiDB;
   
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

   ```bash
   mysql> INSERT INTO student (id, name, sex, birth, department, address) VALUES( 911,'张老大', '男',1985,'计算机系', '北京市海淀区');
   mysql> INSERT INTO student (id, name, sex, birth, department, address) VALUES( 902,'张老二', '男',1986,'中文系', '北京市昌平区');
   mysql> INSERT INTO student (id, name, sex, birth, department, address) VALUES( 903,'张三', '女',1990,'中文系', '湖南省永州市');
   mysql> INSERT INTO student (id, name, sex, birth, department, address) VALUES( 904,'李四', '男',1990,'英语系', '辽宁省阜新市');
   mysql> INSERT INTO student (id, name, sex, birth, department, address) VALUES( 905,'王五', '女',1991,'英语系', '福建省厦门市');
   mysql> INSERT INTO student (id, name, sex, birth, department, address) VALUES( 906,'王六', '男',1988,'计算机系', '湖南省衡阳市');
   
   mysql> INSERT INTO student (id, name, sex, department) VALUES( 907,'小七', '男','计算机系');
   ```

   > * 插入时可指定插入字段

   ```bash
   mysql> INSERT INTO score (id, stu_id, c_name, grade) VALUES(NULL,901, '计算机',198);
   mysql> INSERT INTO score (id, stu_id, c_name, grade) VALUES(NULL,901, '英语', 80);
   mysql> INSERT INTO score (id, stu_id, c_name, grade) VALUES(NULL,902, '计算机',65);
   mysql> INSERT INTO score (id, stu_id, c_name, grade) VALUES(NULL,902, '中文',88);
   mysql> INSERT INTO score (id, stu_id, c_name, grade) VALUES(NULL,903, '中文',95);
   mysql> INSERT INTO score (id, stu_id, c_name, grade) VALUES(NULL,904, '计算机',70);
   mysql> INSERT INTO score (id, stu_id, c_name, grade) VALUES(NULL,904, '英语',92);
   mysql> INSERT INTO score (id, stu_id, c_name, grade) VALUES(NULL,905, '英语',94);
   mysql> INSERT INTO score (id, stu_id, c_name, grade) VALUES(NULL,906, '计算机',90);
   mysql> INSERT INTO score (id, stu_id, c_name, grade) VALUES(NULL,906, '英语',85);
   ```

4. 删除表

   ```bash
   mysql> SHOW TABLES;   #展示所有表
   
   mysql> DROP TABLE student;   #删除表
   ```

5. 删除库

   ```bash
   mysql> select database();   #查看当前使用的库
   
   mysql> SHOW DATABASES;   #展示所有数据库
   
   mysql> drop database SaiDB;   #删除SaiDB库
   ```

6. 查询数据

   1. 查询student表的所有记录

      ```bash
      mysql> select * from student;
      +-----+-----------+------+-------+--------------+--------------------+
      | id  | name      | sex  | birth | department   | address            |
      +-----+-----------+------+-------+--------------+--------------------+
      | 901 | 张老大    | 男   |  1985 | 计算机系     | 北京市海淀区       |
      | 902 | 张老二    | 男   |  1986 | 中文系       | 北京市昌平区       |
      | 903 | 张三      | 女   |  1990 | 中文系       | 湖南省永州市       |
      | 904 | 李四      | 男   |  1990 | 英语系       | 辽宁省阜新市       |
      | 905 | 王五      | 女   |  1991 | 英语系       | 福建省厦门市       |
      | 906 | 王六      | 男   |  1988 | 计算机系     | 湖南省衡阳市       |
      +-----+-----------+------+-------+--------------+--------------------+
      ```

   2. 查询student表的第2条到4条记录

      ```bash
      mysql> SELECT * FROM student LIMIT 1,3;
      +-----+-----------+------+-------+------------+--------------------+
      | id  | name      | sex  | birth | department | address            |
      +-----+-----------+------+-------+------------+--------------------+
      | 902 | 张老二    | 男   |  1986 | 中文系     | 北京市昌平区       |
      | 903 | 张三      | 女   |  1990 | 中文系     | 湖南省永州市       |
      | 904 | 李四      | 男   |  1990 | 英语系     | 辽宁省阜新市       |
      +-----+-----------+------+-------+------------+--------------------+
      ```

   3. 查询student表中计算机系和英语系的学生的信息

      ```bash
      mysql> SELECT * FROM student WHERE department IN ('计算机系','英语系');
      +-----+-----------+------+-------+--------------+--------------------+
      | id  | name      | sex  | birth | department   | address            |
      +-----+-----------+------+-------+--------------+--------------------+
      | 901 | 张老大    | 男   |  1985 | 计算机系     | 北京市海淀区       |
      | 904 | 李四      | 男   |  1990 | 英语系       | 辽宁省阜新市       |
      | 905 | 王五      | 女   |  1991 | 英语系       | 福建省厦门市       |
      | 906 | 王六      | 男   |  1988 | 计算机系     | 湖南省衡阳市       |
      +-----+-----------+------+-------+--------------+--------------------+
      ```

   4. 查询student表中每个院系有多少人

      ```bash
      mysql> SELECT department, COUNT(id) FROM student GROUP BY department;
      +--------------+-----------+
      | department   | COUNT(id) |
      +--------------+-----------+
      | 计算机系     |         2 |
      | 中文系       |         2 |
      | 英语系       |         2 |
      +--------------+-----------+
      ```

   5. 查询score表中每个科目的最高分

      ```bash
      mysql> select * from score;
      +----+--------+-----------+-------+
      | id | stu_id | c_name    | grade |
      +----+--------+-----------+-------+
      |  1 |   901  | 计算机    |    98 |
      |  . |    .   |   .      |    .  |
         . |    .   |   .      |    .  |
      |  . |    .   |   .      |    .  |
      | 10 |   906  |   英语    |    85 |
      +----+--------+-----------+-------+
      
      mysql> SELECT c_name,MAX(grade) FROM score GROUP BY c_name;
      +-----------+------------+
      | c_name    | MAX(grade) |
      +-----------+------------+
      | 计算机    |         98 |
      | 英语      |         94 |
      | 中文      |         95 |
      +-----------+------------+
      ```

   6. 联合student表和score表，查询所有学生的信息和考试信息

      ```bash
      mysql> SELECT a.id,a.name,a.sex,b.c_name,b.grade FROM student a,score b WHERE a.id=b.stu_id;
      +-----+-----------+------+-----------+-------+
      | id  | name      | sex  | c_name    | grade |
      +-----+-----------+------+-----------+-------+
      | 901 | 张老大    | 男   | 计算机    |    98 |
      | 901 | 张老大    | 男   | 英语      |    80 |
      | 902 | 张老二    | 男   | 计算机    |    65 |
      | 902 | 张老二    | 男   | 中文      |    88 |
      | 903 | 张三      | 女   | 中文      |    95 |
      | 904 | 李四      | 男   | 计算机    |    70 |
      | 904 | 李四      | 男   | 英语      |    92 |
      | 905 | 王五      | 女   | 英语      |    94 |
      | 906 | 王六      | 男   | 计算机    |    90 |
      | 906 | 王六      | 男   | 英语      |    85 |
      +-----+-----------+------+-----------+-------+
      ```

   7. 联合student表和score表，计算每个学生的总成绩

      ```bash
      mysql> SELECT a.id,a.name,SUM(b.grade) FROM student a,score b WHERE a.id=b.stu_id GROUP BY a.id;
      +-----+-----------+--------------+
      | id  | name      | SUM(b.grade) |
      +-----+-----------+--------------+
      | 901 | 张老大    |          178 |
      | 902 | 张老二    |          153 |
      | 903 | 张三      |           95 |
      | 904 | 李四      |          162 |
      | 905 | 王五      |           94 |
      | 906 | 王六      |          175 |
      +-----+-----------+--------------+
      ```

   8. 计算每个考试科目的平均成绩

      ```bash
      mysql> SELECT c_name,AVG(grade) FROM score GROUP BY c_name;
      +-----------+------------+
      | c_name    | AVG(grade) |
      +-----------+------------+
      | 计算机    |    80.7500 |
      | 英语      |    87.7500 |
      | 中文      |    91.5000 |
      +-----------+------------+
      ```

   9. 查询计算机成绩低于95的学生信息

      ```bash
      mysql> SELECT * FROM student WHERE id IN (SELECT stu_id FROM score WHERE c_name="计算机" and grade<95);
      +-----+-----------+------+-------+--------------+--------------------+
      | id  | name      | sex  | birth | department   | address            |
      +-----+-----------+------+-------+--------------+--------------------+
      | 902 | 张老二    | 男   |  1986 | 中文系       | 北京市昌平区       |
      | 904 | 李四      | 男   |  1990 | 英语系       | 辽宁省阜新市       |
      | 906 | 王六      | 男   |  1988 | 计算机系     | 湖南省衡阳市       |
      +-----+-----------+------+-------+--------------+--------------------+
      ```

   10. 查询同时参加计算机和英语考试的学生的信息

       ```bash
       mysql> SELECT * FROM student WHERE id = ANY (SELECT stu_id FROM score WHERE stu_id IN (SELECT stu_id FROM score WHERE c_name = '计算机') AND c_name= '英语');
       +-----+-----------+------+-------+--------------+--------------------+
       | id  | name      | sex  | birth | department   | address            |
       +-----+-----------+------+-------+--------------+--------------------+
       | 901 | 张老大    | 男   |  1985 | 计算机系     | 北京市海淀区       |
       | 904 | 李四      | 男   |  1990 | 英语系       | 辽宁省阜新市       |
       | 906 | 王六      | 男   |  1988 | 计算机系     | 湖南省衡阳市       |
       +-----+-----------+------+-------+--------------+--------------------+
       ```

   11. 将计算机考试成绩按从高到低进行排序

       > **排序**：`ORDER BY`，`ASC`升序，`DESC`降序

       ```bash
       mysql> SELECT s.stu_id,t.name,s.grade FROM score s,student t WHERE s.stu_id = t.id and s.c_name='计算机' ORDER BY s.grade DESC;
       +--------+-----------+-------+
       | stu_id | name      | grade |
       +--------+-----------+-------+
       |    901 | 张老大    |    98 |
       |    906 | 王六      |    90 |
       |    904 | 李四      |    70 |
       |    902 | 张老二    |    65 |
       +--------+-----------+-------+
       ```

   12. 查询姓李或姓王的同学的姓名、院系和考试科目及成绩

       > **模糊查询**：`like`通常和`%`一起使用

       ```bash
       mysql> SELECT s.id, s.name, s.department, t.c_name, t.grade FROM student s, score t WHERE (s.name LIKE '李%' OR s.name LIKE '王%') AND s.id=t.stu_id ;
       +-----+--------+--------------+-----------+-------+
       | id  | name   | department   | c_name    | grade |
       +-----+--------+--------------+-----------+-------+
       | 904 | 李四   | 英语系       | 计算机    |    70 |
       | 904 | 李四   | 英语系       | 英语      |    92 |
       | 905 | 王五   | 英语系       | 英语      |    94 |
       | 906 | 王六   | 计算机系     | 计算机    |    90 |
       | 906 | 王六   | 计算机系     | 英语      |    85 |
       +-----+--------+--------------+-----------+-------+
       ```

   13. 查询湖南学生的姓名、院系和考试科目及成绩

       ```bash
       mysql> SELECT s.id, s.name, s.department, t.c_name, t.grade FROM student s, score t WHERE s.address LIKE '湖南%' AND s.id=t.stu_id;
       +-----+--------+--------------+-----------+-------+
       | id  | name   | department   | c_name    | grade |
       +-----+--------+--------------+-----------+-------+
       | 903 | 张三   | 中文系       | 中文      |    95 |
       | 906 | 王六   | 计算机系     | 计算机    |    90 |
       | 906 | 王六   | 计算机系     | 英语      |    85 |
       +-----+--------+--------------+-----------+-------+
       ```

7. 修改和删除数据

   > **UPDATE和DELETE都是没有后悔药的操作，因此最好使用事务**
   >
   > * START TRANSACTION：开始一个事务
   >
   > * ROLLBACK：回滚之前的操作
   >
   > * COMMIT：提交事务内的操作

   * 修改"王五"的名字成"王伍"

     ```bash
     mysql> START TRANSACTION;
     
     mysql> SELECT * FROM student WHERE id = '905';
     +-----+--------+------+-------+------------+--------------------+
     | id  | name   | sex  | birth | department | address            |
     +-----+--------+------+-------+------------+--------------------+
     | 905 | 王五    | 女   |  1991 | 英语系     | 福建省厦门市       |
     +-----+--------+------+-------+------------+--------------------+
     
     mysql> UPDATE student SET name = '王伍' WHERE id = '905';
     
     mysql> ROLLBACK;   #若后悔了就执行回滚，否则不执行ROLLBACK直接执行COMMIT
     mysql> COMMIT;    #无论
     ```

   * 删除王六的英语成绩

     ```bash
     mysql> START TRANSACTION;
     
     mysql> SELECT * FROM score t WHERE t.c_name = '英语' and t.stu_id = (SELECT s.id FROM student s where s.`name` = '王六');   #先用select确定查询条件
     
     mysql> DELETE FROM score t WHERE t.c_name = '英语' and t.stu_id = (SELECT s.id FROM student s where s.`name` = '王六');   #再用上面条件进行删除
     
     mysql> ROLLBACK;   #若后悔了就执行回滚，否则不执行ROLLBACK直接执行COMMIT
     mysql> COMMIT;    #无论
     ```

8. 清空表数据（保留表结构）

   ```bash
   mysql> truncate table score;
   ```

#### 3. python连接MySQL

* 安装PyMySQL：`pip install pymysql`

  ```python
  import pymysql
  
  def ConnectDB():
      db = pymysql.connect(
          host = "127.0.0.1",   #主机名
          port = 3306,   #端口号
          user = "root",   #用户名
          passwd = "will",   #密码
          db = "saidb",   #数据库名
          charset='utf8', #设置编码为utf8是为输出中文
          ) 
      print('MySQL连接上了!')
      return db
  
  def CloseDB(db):
      db.close()
      print('MySQL关闭了!')
  
  def CreateTable(db):
      cursor = db.cursor()   #获取操作游标
      cursor.execute("DROP TABLE IF EXISTS NewStudent")   # 若存在Sutdent表则先删除
      sql = """CREATE TABLE NewStudent (
              ID CHAR(10) NOT NULL,
              Name CHAR(8),
              Grade INT )"""
      cursor.execute(sql)  #执行SQL语句
      
  def QueryData(db):
      ID = '01'
      cursor = db.cursor()   #获取操作游标 
      sql = "SELECT * FROM NewStudent where id = '%s';"%(ID)
  
      try:
          cursor.execute(sql)   #执行SQL语句
          results = cursor.fetchall()   #获取所有记录列表
          for row in results:   #方法1取值
              ID = row[0]
              Name = row[1]
              Grade = row[2]
              print(f"方法1取值：ID: {ID}, Name: {Name}, Grade: {Grade}")
          for ID, Name, Grade in results:   #方法2取值
              print(f"方法2取值：ID: {ID}, Name: {Name}, Grade: {Grade}")
      except pymysql.Warning as e:
          print("查询出异常了", e)
  
  def InsertData(db):
      ID = '01'
      Name = 'CZQ'
      Grade = 70
      cursor = db.cursor()   #获取操作游标
  
      sql = "INSERT INTO NewStudent VALUES ('%s','%s',%d)" %(ID, Name, Grade)
      try:
          cursor.execute(sql)   # 执行sql语句
          db.commit()
      except pymysql.Warning as e:
          print('插入数据失败!', e)
          db.rollback()
  
  def DeleteData(db):
      cursor = db.cursor()   #获取操作游标
      sql = "DELETE FROM NewStudent WHERE Grade = '73'"
      try:
         cursor.execute(sql)   #执行SQL语句
         db.commit()
      except pymysql.Warning as e:
          print('删除数据失败!', e)
          db.rollback()
  
  def UpdateData(db):
      cursor = db.cursor()   #获取操作游标
      sql = "UPDATE NewStudent SET Grade = Grade + 3 WHERE ID = '01'"
      try:
          cursor.execute(sql)   #执行SQL语句
          db.commit()
      except pymysql.Warning as e:
          print('更新数据失败!', e)
          db.rollback()
  
  if __name__ == '__main__':
      db = ConnectDB()    # 连接MySQL数据库
      CreateTable(db)     # 创建表
      InsertData(db)        # 插入数据
      print('\n插入后的数据:')
      QueryData(db) 
      UpdateData(db)        # 更新数据
      print('\n更新后的数据:')
      QueryData(db)
      DeleteData(db)        # 删除数据
    print('\n删除后的数据:')
      QueryData(db)
  
      CloseDB(db)         # 关闭数据库
  ```
  
  > * 拼接sql时，**字符串**字段必须使用单引号包围住，要写成'%s'，而不是%s





