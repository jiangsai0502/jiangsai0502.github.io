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
   SHOW DATABASES;
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
   use mysql;
   Reading table information for completion of table and column names
   You can turn off this feature to get a quicker startup with -A
   Database changed
   
   use employees;
   Reading table information for completion of table and column names
   You can turn off this feature to get a quicker startup with -A
   Database changed
   ```

   > 切换数据库，直接`use 数据库名称;`即可

3. 查看当前数据库

   ```bash
   select database();
   +------------+
   | database() |
   +------------+
   | employees  |
   +------------+
   ```

4. 展示所有表

   ```bash
   SHOW TABLES;
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
   SHOW COLUMNS FROM departments;
   +-----------+-------------+------+-----+---------+-------+
   | Field     | Type        | Null | Key | Default | Extra |
   +-----------+-------------+------+-----+---------+-------+
   | dept_no   | char(4)     | NO   | PRI | NULL    |       |
   | dept_name | varchar(40) | NO   | UNI | NULL    |       |
   +-----------+-------------+------+-----+---------+-------+
   ```

6. 退出数据库

   ```bash
   exit;
   Bye
   ```

   

#### 2. 数据库管理

1. 数据格式

   | 类型     | 描述                                                        |
   | -------- | ----------------------------------------------------------- |
   | INT      | 整数，范围为：(-2,147,483,648, 2,147,483,647)               |
   | FLOAT    | 浮点小数，小数点最多24位                                    |
   | DATE     | 日期，输出格式为：YYYY-MM-DD                                |
   | TIME     | 时间，输出格式为：HH:MM:SS                                  |
   | DATETIME | 时间，输出格式为：YYYY-MM-DD HH:MM:SS                       |
   | YEAR     | 年份，输出格式为：YYYY                                      |
   | VARCHAR  | 变长字符串，使用格式为：VARCHAR(100)，最多100个字符的字符串 |
   | TEXT     | 长文本                                                      |

2. 常见函数

   | 描述           | 函数                      | 案例                                                         |
   | -------------- | ------------------------- | ------------------------------------------------------------ |
   | 当前日期       | curdate()                 | select curdate();<br />2021-08-28                            |
   | 当前时间       | curtime()                 | select curtime();<br />23:42:04                              |
   | 日期字符串转换 | date_format(date, format) | select date_format('2021-08-27 23:42:04', '%W %M %Y');<br />Friday August 2021<br />select date_format('2021-08-27 23:42:04', '%Y/%m/%d %H_%i_%s');<br />2021/08/27 23_42_04 |
   | 时间字符串转换 | time_format(time, format) |                                                              |
   |                |                           |                                                              |

   

3. 常见符

   | 描述 | 符号   | 描述 | 符号   |
   | ---- | ------ | ---- | ------ |
   | !=   | 不等于 | <>   | 不等于 |
   |      |        |      |        |
   |      |        |      |        |

   

4. 创建并进入库

   ```bash
   CREATE DATABASE IF NOT EXISTS SaiDB;
   
   SHOW DATABASES;
   ```

5. 创建表

   ```mysql
   use SaiDB;
   
   # 创建表时字段名被反引号`引起来，而不是单引号'
   CREATE TABLE `Student` (
     `stu_id` int(10) NOT NULL,
     `name` varchar(20) DEFAULT NULL,
     `sex` varchar(4) DEFAULT NULL,
     `birth` year(4) DEFAULT NULL,
     `leader_id` int(10) DEFAULT NULL,
     `department` varchar(20) DEFAULT NULL,
     `address` varchar(50) DEFAULT NULL,
     PRIMARY KEY (`stu_id`)
   ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
   
   # id从11开始自增
   CREATE TABLE `CourseScore` (
     `id` int(10) NOT NULL AUTO_INCREMENT,
     `stu_id` int(10) NOT NULL,
     `course` varchar(20) DEFAULT NULL,
     `score` int(10) DEFAULT NULL,
     PRIMARY KEY (`id`)
   ) ENGINE=InnoDB AUTO_INCREMENT=11 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
   ```

6. 插入数据

   ```mysql
   INSERT INTO `Student` (`stu_id`, `name`, `sex`, `birth`, `leader_id` , `department`, `address`) VALUES
   ('902', '张二', '男', '1986', '907', '中文系', '北京市昌平区'),
   ('903', '张三', '女', '1990', '907', '中文系', '湖南省永州市'),
   ('904', '李四', '男', '1990', '906', '英语系', '辽宁省阜新市'),
   ('905', '王五', '女', '1991', '906', '英语系', '福建省厦门市'),
   ('911', '张大', '男', '1985', '907', '计算机系', '北京市海淀区');
   
   INSERT INTO `Student` (`stu_id`, `name`, `sex`, `birth`, `department`, `address`) VALUES
   ('906', '王六', '男', '1988', '计算机系', '湖南省衡阳市'),
   ('907', '小七', '男', '1998', '计算机系', '湖南省衡阳市');
   ```

   > * 插入时可指定插入字段

   ```mysql
   INSERT INTO `CourseScore` (`stu_id`, `course`, `score`) VALUES
   ('901', '计算机', '98'),
   ('901', '英语', '80'),
   ('902', '计算机', '65'),
   ('902', '中文', '88'),
   ('903', '中文', '95'),
   ('904', '计算机', '70'),
   ('904', '英语', '92'),
   ('905', '英语', '94'),
   ('906', '计算机', '90'),
   ('906', '英语', '85');
   ```

7. 复制表结构和表数据

   ```mysql
   CREATE TABLE salary SELECT * FROM score
   ```

8. 改表名

   ```mysql
   rename table salary to YoungMan
   ```

9. 新增字段

   ```mysql
   -- 新增 people_name字段 在 age字段 之后
   ALTER TABLE salary ADD COLUMN people_name VARCHAR(100) DEFAULT NULL AFTER NO;
   ```

10. 删除表

    ```bash
    SHOW TABLES;   #展示所有表
    
    DROP TABLE student;   #删除表
    ```

11. 删除库

    ```mysql
    select database();   #查看当前使用的库
    
    SHOW DATABASES;   #展示所有数据库
    
    drop database SaiDB;   #删除SaiDB库
    ```

12. 查询数据

    ```mysql
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

    2. LIMIT

       ```mysql
       SELECT * FROM student LIMIT 3;    # 查询前3条数据
       
       SELECT * FROM student LIMIT 2,4;    # 查询第3条到6条数据，即忽略前2个之后，取前4条
       ```
       
    3. IN

       ```mysql
       SELECT * FROM student WHERE department IN ('计算机系','英语系');    # 查询计算机系和英语系的数据
       ```
       
    4. COUNT()

       ```mysql
       SELECT department, COUNT(id) FROM student GROUP BY department;    # 查询每个院系有多少人
       ```
       
    5. MAX()

       ```mysql
       SELECT c_name,MAX(grade),MAX(grade)+5 as AddGrade FROM score GROUP BY c_name;    # 查询每科的最高分
       ```
       
    6. AVG()

       ```mysql
       SELECT c_name,AVG(grade),AVG(grade)*5 FROM score GROUP BY c_name;    # 查询每科的平均分
       ```
       
    6. ORDER BY

       ```mysql
       SELECT s.stu_id,t.name,s.grade FROM score s,student t WHERE s.stu_id = t.id and s.c_name='英语' ORDER BY s.grade DESC;    # 将英语成绩从高到低展示
       ```

    7. like

       ```mysql
       SELECT s.id, s.name, s.department, t.c_name, t.grade FROM student s, score t WHERE (s.name LIKE '李%' OR s.name LIKE '王%') AND s.id=t.stu_id ;    # 模糊查询姓李或姓王的学生数据
       ```

    8. join（两表连接）

       ```mysql
       # 查询每个学生对应的leader信息
       # student表含2部分数据，可看作2个子表，普通学生表classmate，组长表leader
       # classmate表的leader_id字段 = leader表的stu_id字段
       SELECT c.stu_id,c.name,c.leader_id,l.name FROM Student c join Student l on c.leader_id = l.stu_id
       
       # 查询每个学生各科的分数
       SELECT t.stu_id,t.name,t.sex,s.course,s.score FROM Student t join CourseScore s on t.stu_id = s.stu_id;
       
       # 查询每个学生所有科目的总分
       SELECT t.stu_id,t.name,sum(s.score) FROM Student t join CourseScore s on t.stu_id = s.stu_id GROUP by t.stu_id;
       
       # 查询湖南的每个学生的所有科目的总分
       SELECT t.stu_id,t.name, s.course, s.score FROM Student t join CourseScore s on t.stu_id = s.stu_id and t.address LIKE '湖南%';
       ```

    9. join（两表连接）

       ```mysql
       SELECT o.order_id, c.customer_id, os.order_status_id FROM orders o
       JOIN customers c 
       	ON o.customer_id = c.customer_id
       JOIN order_statuses os 
       	ON o.status = os.order_status_id
       ```

    10. 子查询

       ```mysql
       # 查询英语成绩低于95的学生数据
       SELECT * FROM student WHERE id IN (SELECT stu_id FROM score WHERE c_name="英语" and grade<95);
       
       # 查询同时参加计算机和英语考试的学生的信息
       SELECT * FROM student WHERE id = ANY (SELECT stu_id FROM score WHERE stu_id IN (SELECT stu_id FROM score WHERE c_name = '计算机') AND c_name= '英语');
       ```

    11. 修改和删除数据


    > **UPDATE和DELETE都是没有后悔药的操作，因此最好使用事务**
    >
    > * START TRANSACTION：开始一个事务
    >
    > * ROLLBACK：回滚之前的操作
    >
    > * COMMIT：提交事务内的操作

    * 修改"王五"的名字成"王伍"

      ```bash
      START TRANSACTION;
      
      SELECT * FROM student WHERE id = '905';
      
      UPDATE student SET name = '王伍' WHERE id = '905';
      
      ROLLBACK;   #若后悔了就执行回滚，否则不执行ROLLBACK直接执行COMMIT
      COMMIT;    #无论
      ```
      
    * 删除王六的英语成绩

      ```bash
      START TRANSACTION;
      
      SELECT * FROM score t WHERE t.c_name = '英语' and t.stu_id = (SELECT s.id FROM student s where s.`name` = '王六');   #先用select确定查询条件
      
      DELETE FROM score t WHERE t.c_name = '英语' and t.stu_id = (SELECT s.id FROM student s where s.`name` = '王六');   #再用上面条件进行删除
      
      ROLLBACK;   #若后悔了就执行回滚，否则不执行ROLLBACK直接执行COMMIT
      COMMIT;    #无论
      ```

13. 清空表数据（保留表结构）

    ```bash
    truncate table score;
    ```

14. 案例

    >描述：向MySQL中导入数据进行分析，要求MySQL表具有自增的字段，序号列“No”

    1. 建库建表

       ```sql
       DROP DATABASE IF EXISTS `ColorV`;
       CREATE DATABASE `ColorV`; 
       USE `ColorV`;
       
       CREATE TABLE `NonNextStay` (
         `id` varchar(100) NOT NULL,
         `user_id` varchar(50) NOT NULL,
         `udid` varchar(50) NOT NULL,
         `os` varchar(50) NOT NULL,
         `version` varchar(50) NOT NULL,
         `timestamp` datetime DEFAULT NULL,
         `category` varchar(50) NOT NULL,
         `page` varchar(50) NOT NULL,
         `No` int(10) AUTO_INCREMENT NOT NULL PRIMARY KEY
       ) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
       ```

    2. csv表头

       | No   | id   | user_id | udid | os   | version | timestamp | category | page |
       | ---- | ---- | ------- | ---- | ---- | ------- | --------- | -------- | ---- |

    3. TablePlus导入csv

       ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210825180906.png)

    4. 案例

       ```mysql
       -- （临时表）非次留用户访问页面 x<5 的全部页面
       create table Passby (
       select n. `No`,	n.user_id,	n. `timestamp`,	n.category,	n.page
       from NonNextStay n 
       INNER JOIN 
       (select user_id,count(user_id) num from NonNextStay n group by user_id having num < 5) t
       ON n.user_id = t.user_id and category NOT in ('个人中心','直播','群组','话题','其他'))
       
       -- 删除临时表
       SELECT * FROM Passby;
       SHOW databases;
       DROP TABLE IF EXISTS Passby;
       
       -- 非次留用户访问页面 x<5 的最后1个页面
       select * from 
       (select n.No,	n.user_id,	n. `timestamp`,	n.category,	n.page,row_number() over(partition by user_id order by No desc) as a from Passby n) r
       where a<=1
       
       -- 非次留用户访问页面 x<5 的最后2个页面
       select * from 
       (select n.No,	n.user_id,	n. `timestamp`,	n.category,	n.page,row_number() over(partition by user_id order by No desc) as a from Passby n) r 
       where a<=2
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





