## 安装

#### 1. dmg 安装 MySql

1. 安装 MySql 数据库：[下载链接](https://downloads.mysql.com/archives/community/)，[安装步骤](https://www.jianshu.com/p/833f388da8e3)

   > * 安装位置默认，最后填写强密码，且勾选掉默认启动
   >
   >   ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310290036599.png)
   >
   > * 安装目录
   >
   >   ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210917143749.png)

2. 查看MySql进程是否存在  

   > `ps aux | grep mysql`
   >
   > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310290035935.png)
   >
   > 没有`mysqld`进程，可见MySQL服务器并没有运行

3. 设置环境变量

   > 1. 检查终端上的mysql调用
   >
   >    ```bash
   >    > which mysql
   >    /Users/jiangsai/anaconda3/bin/mysql
   >    ```
   >
   >    > 这里明显有错误，安装时我们知道mysql被安装在了/usr/local/mysql/bin
   >
   > 2. 修改环境变量的引用
   >
   >    > 查看本地使用的是`bash`还是`zsh`
   >    > 若输出`/bin/zsh`，则编辑`~/.zshrc`；若输出`/bin/bash`，则编辑`~/.bash_profile`
   >    >
   >    > ```bash
   >    > > echo $SHELL
   >    > /bin/zsh
   >    > > open ~/.zshrc
   >    > ```
   >    >
   >    > > ```
   >    > > export PATH="/usr/local/mysql/bin:$PATH"
   >    > > 
   >    > > # >>> conda initialize >>>
   >    > > # !! Contents within this block are managed by 'conda init' !!
   >    > > __conda_setup="$('/Users/jiangsai/anaconda3/bin/conda' 'shell.zsh' 'hook' 2> /dev/null)"
   >    > > if [ $? -eq 0 ]; then
   >    > >     eval "$__conda_setup"
   >    > > else
   >    > >     if [ -f "/Users/jiangsai/anaconda3/etc/profile.d/conda.sh" ]; then
   >    > >         . "/Users/jiangsai/anaconda3/etc/profile.d/conda.sh"
   >    > >     fi
   >    > > ```
   >    >
   >    > 重新加载环境配置文件
   >    >
   >    > ```bash
   >    > > source ~/.zshrc
   >    > 
   >    > >  which mysql
   >    > /usr/local/mysql/bin/mysql
   >    > ```

4. 启动数据库

   1. 界面启动

      > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310290046703.png)

   2. 代码操作

      > ```bash
      > # 启动MySQL服务
      > sudo /usr/local/mysql/support-files/mysql.server start
      > Password:电脑密码
      > # 关闭MySQL服务
      > sudo /usr/local/mysql/support-files/mysql.server stop
      > Password:电脑密码
      > # 重启MySQL服务
      > sudo /usr/local/mysql/support-files/mysql.server restart
      > Password:电脑密码
      > # 查看状态
      > sudo /usr/local/mysql/support-files/mysql.server status
      > # 进入MySQL：强制MySQL客户端通过TCP/IP连接
      > mysql -uroot -p -h 127.0.0.1
      > Enter password:数据库密码
      > # 修改密码：由jiangsai改为sai
      > ALTER USER 'root'@'localhost' IDENTIFIED BY 'sai';
      > # 退出MySQL
      > exit
      > ```

5. 卸载

   ```bash
   备份数据库
   # 关闭MySQL服务（停止方式与开启方式对应）
   	# 若是从系统偏好里启动的，则从系统偏好设置里关闭
   	# 若是命令行启动的，则命令行关闭
   
   # 卸载
   系统偏好设置 - Uninstall
   
   # 删除剩余文件
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
       * 把mysql文件夹的拥有者改成`_mysql`：`sudo chown -R _mysql /usr/local/mysql`



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


#### 5. 数据库工具 **Sequel Pro**（不常用）

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




#### 6. 数据库工具[tableplus](https://www.macwk.com/soft/tableplus)（不常用）

1. 配置

   ![ghGbNN](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/uPic/ghGbNN.png)



#### 7. 数据库工具[navicat premium](https://www.macwk.com/soft/navicat-premium)（常用）

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

2. 日期函数

   ```mysql
   # 日期函数
   # NOW()，当前日期+时间，如2021-09-12 17:58:26
   # CURDATE()，当前日期，如2021-09-12
   # CURTIME()，当前时间，如17:58:26
   SELECT NOW(), CURDATE(), CURTIME();
   
   # YEAR()，获取数值年份
   # MONTH()，获取数值月份
   # DAY()，获取数值天
   # HOUR()，获取小时
   # MINUTE()，获取分钟
   # SECOND()，获取秒
   select YEAR(NOW()), MONTH(NOW()), DAY(NOW()), HOUR(NOW()), MINUTE(NOW()), SECOND(NOW()); 
   
   # MONTHNAME()，获取字符串月份
   # DAYNAME()，获取字符串天
   select MONTHNAME(NOW()), DAYNAME(NOW());
   
   # DATE_FORMAT(date, format)：格式化日期+时间
   # 如Friday September 2021，September 12 2021
   select DATE_FORMAT(NOW(), '%W %M %Y'), DATE_FORMAT(now(), '%M %d %Y')
   ;
   # 如2021/08/27 23_42_04
   select DATE_FORMAT(NOW(), '%Y/%m/%d %H_%i_%s');
   
   # DATE_ADD()，增加时间（1秒、2分、3小时、4天、5个月、6年）
   SELECT now(), DATE_ADD(now(), INTERVAL 1 SECOND), DATE_ADD(now(), INTERVAL 2 MINUTE), DATE_ADD(now(), INTERVAL 3 HOUR), DATE_ADD(now(), INTERVAL 4 DAY), DATE_ADD(now(), INTERVAL 5 MONTH), DATE_ADD(now(), INTERVAL 6 YEAR) ;
   # DATE_ADD()，减小时间（1秒、2分、3小时、4天、5个月、6年）
   SELECT now(), DATE_ADD(now(), INTERVAL -1 SECOND), DATE_ADD(now(), INTERVAL -2 MINUTE), DATE_ADD(now(), INTERVAL -3 HOUR), DATE_ADD(now(), INTERVAL -4 DAY), DATE_ADD(now(), INTERVAL -5 MONTH), DATE_ADD(now(), INTERVAL -6 YEAR) ;
   ```

3. 数字函数

   ```mysql
   # ROUND()，四舍五入函数
   SELECT ROUND(5.73429), ROUND(5.73429, 2)
   
   # TRUNCATE()，小数截取
   SELECT TRUNCATE(5.73429,4), TRUNCATE(5.73429, 2)
   
   # RAND()，随机值
   SELECT RAND()
   ```

4. 字符串函数

   ```mysql
   # LENGTH()，字符串长度
   # UPPER()，字符串转大写
   # LOWER()，字符串转小写
   SELECT LENGTH('Jiang Sai'), UPPER('Jiang Sai'), LOWER('Jiang Sai')
   
   # TRIM()，删除字符串前后空格
   SELECT TRIM(' Jiang Sai ')
   
   # LEFT()，截取左侧字符串
   # RIGHT()，截取右侧字符串
   # SUBSTR()，截取左侧指定位置，指定长度的字符串
   SELECT LEFT('Jiang Sai',4),RIGHT('Jiang Sai',2),SUBSTR('Jiang Sai',3,2)
   
   # RIGHT()，替换指定字符串
   SELECT REPLACE('Jiang Sai','ng',' Ma ')
   
   # CONCAT()，连接字符串
   SELECT CONCAT(first_name, '_', last_name)
   FROM customers
   ```

5. Null判断函数

   ```mysql
   # IFNULL(field1，'appointed_str')，若是字段field1的值为Null，则替换为字符'appointed_str'
   SELECT order_id,
   	IFNULL(shipper_id, 'no shipper')
   FROM orders
   
   # COALESCE(field1，field2，'appointed_str')，若是字段field1的值为Null，则替换为字段field2，若field2也为空，则替换为字符'appointed_str'
   SELECT order_id,
   	COALESCE(shipper_id, comments, 'no shipper')
   FROM orders
   ```

6. IF函数

   ```mysql
   # IF(expression, fist_value, second_value)，若表达式expression为真，则结果为fist_value，为假则结果为second_value
   SELECT order_id, order_date,
   	IF(YEAR(order_date) = '2018', 'Right', 'Wrong')
   FROM orders
   ```

7. CASE函数

   ```mysql
   # CASE条件判断
   SELECT order_id, order_date,
   	CASE 
   		WHEN YEAR(order_date) = '2018' THEN 'This Year'
   		WHEN YEAR(order_date) = '2017' THEN 'Last Year'
   		ELSE 'Wrong'
   	END
   FROM orders
   ```

8. 常见符

   | 描述 | 符号   | 描述 | 符号   |
   | ---- | ------ | ---- | ------ |
   | !=   | 不等于 | <>   | 不等于 |
   |      |        |      |        |
   |      |        |      |        |

9. 创建并进入库

   ```mysql
   CREATE DATABASE IF NOT EXISTS SaiDB;
   
   SHOW DATABASES;
   ```

10. 创建表

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

11. 插入数据

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

12. 复制表结构和表数据

    ```mysql
    CREATE TABLE salary SELECT * FROM score
    ```

13. 新增字段

    ```mysql
    -- 新增 people_name字段 在 age字段 之后
    ALTER TABLE salary ADD COLUMN people_name VARCHAR(100) DEFAULT NULL AFTER NO;
    ```

14. 复制并新增字段

    ```mysql
    -- 新增age默认0岁，新增出生年份有生日算出来
    CREATE TABLE salary SELECT id, name, department, 0 as age, date_format(`birthday`, '%Y/%m/%d') birthYear FROM score
    ```

15. 改表名

    ```mysql
    rename table salary to YoungMan
    ```

16. 获取表字段名

    ```mysql
    select COLUMN_NAME from information_schema.COLUMNS where table_name = 'Stay_FristDay';
    ```
    
17. 删除表

    ```bash
    SHOW TABLES;   #展示所有表
    
    DROP TABLE student;   #删除表
    ```

18. 删除库

    ```mysql
    select database();   #查看当前使用的库
    
    SHOW DATABASES;   #展示所有数据库
    
    drop database SaiDB;   #删除SaiDB库
    ```

19. 查询数据

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
       
    4. ORDER BY

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

    9. join（多表连接）

       ```mysql
       SELECT o.order_id, c.customer_id, os.order_status_id FROM orders o
       JOIN customers c 
       	ON o.customer_id = c.customer_id
       JOIN order_statuses os 
       	ON o.status = os.order_status_id
       ```

    8. over partition by

       描述：Trade_Record表中共有100个客户渠道，每个渠道有5000个客户，一共50万条数据。

       目标：取出100个渠道中，每个渠道的最后1个交易时间对应的数据

       > 最后1个时间点未必只有1条数据，也可能有多条

       | 客户渠道  | 客户    | 交易时间     | 交易金额 |
       | --------- | ------- | ------------ | -------- |
       | source_id | user_id | trading_time | cash     |

       ```mysql
       -- 对所有数据，按照trading_time进行倒序，并给出序号
       select *, rank()over(partition by source_id order by trading_time desc) tempRank from Trade_Record
       
       -- 查询每个客户来源source_id，排序第1的数据
       select source_id , user_id, trading_time ,cash  
       from (select *, rank()over(partition by source_id order by trading_time desc) tempRank from Trade_Record) n
       where n.tempRank = 1
       ```

       ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210909113642.png)

       > 注意n.tempRank = 1，会取这个user_id的前4条数据，因为他们的序号都是1
       >
       > 注意n.tempRank = 2，取不到这个user_id的任何数据，因为没有数据的序号是2

    9. 拼接查询结果

       > 只要查询结果的列数相同即可拼接，没别的条件

       ```mysql
       SELECT a.address from clients a
       UNION
       SELECT b.birth_date from customers b
       ```

    10. 字符串转数字

        ```mysql
        ORDER BY '123'+0;
        ```
        
    11. 聚合函数

        1. COUNT()

           ```mysql
           # 每个客户有多少笔交易
           SELECT
           	a.client_id,
           	COUNT(*)
           FROM
           	invoices a
           GROUP BY
           	a.client_id
           ```

        2. MAX()、MIN()、AVG()

           ```mysql
           # 每个客户最大、最小、平均交易金额
           SELECT
           	a.client_id,
           	max(invoice_total) max_cost,
           	min(invoice_total) min_cost,
           	avg(invoice_total) avg_cost
           FROM
           	invoices a
           GROUP BY
           	a.client_id;
           ```

        3. SUM()

           ```mysql
           # 每个客户的总交易金额
           SELECT
           	client_id,
           	sum(invoice_total) total_sale
           FROM
           	invoices
           GROUP BY
           	client_id
           	
           # 统计每个城市的每个客户的总交易金额
           SELECT
           	b.city,
           	a.client_id,
           	sum(a.invoice_total) total_sale
           FROM
           	invoices a
           	JOIN clients b ON a.client_id = b.client_id
           GROUP BY
           	b.city,
           	a.client_id
           ```

        4. Having：分组条件

           ```mysql
           # 每个城市的每个客户最大、最小、平均交易金额，其中最大金额>185 且 最小金额>150的数据
           SELECT
           	b.city,
           	a.client_id,
           	max(a.invoice_total) max_cost,
           	min(a.invoice_total) min_cost,
           	avg(a.invoice_total) avg_cost
           FROM
           	invoices a
           	JOIN clients b ON a.client_id = b.client_id
           GROUP BY
           	b.city,
           	a.client_id
           HAVING
           	max_cost < 185
           	or avg_cost > 150;
           ```

        5. with ROLLUP 结果集汇总

           ```mysql
           # 每个城市的每个客户的总交易金额，其中总交易金额>100的数据，并对每个城市和每个客户的结果汇总
           SELECT
           	b.city,
           	a.client_id,
           	SUM(a.invoice_total) sum_cost
           FROM
           	invoices a
           	JOIN clients b ON a.client_id = b.client_id
           GROUP BY
           	b.city,
           	a.client_id with ROLLUP
           HAVING
           	sum_cost > 100
           ```

           

    12. 子查询

        ```mysql
        # 查询英语成绩低于95的学生数据
        SELECT * FROM student WHERE id IN (SELECT stu_id FROM score WHERE c_name="英语" and grade<95);
        
        # 查询同时参加计算机和英语考试的学生的信息
        SELECT * FROM student WHERE id = ANY (SELECT stu_id FROM score WHERE stu_id IN (SELECT stu_id FROM score WHERE c_name = '计算机') AND c_name= '英语');
        ```

        

    13. 修改和删除数据

        ```mysql
        * UPDATE和DELETE都是没有后悔药的操作，因此最好使用事务**
        
        * START TRANSACTION：开始一个事务
        
        * ROLLBACK：回滚之前的操作
        
        * COMMIT：提交事务内的操作
        
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


#### 3. MySQL导入百万行csv文件

* [参考1](https://blog.csdn.net/quiet_girl/article/details/71436108)，[参考2](https://swordpal.cn/posts/33306/)

##### 命令行操作

```mysql
# 登录MySQL，密码js1122334
mysql -u root -p

# 修改禁止写入的配置，值为null则禁止写入
show variables like '%secure_file_priv%';

# 新建my.cnf
sudo vim /etc/my.cnf

# 复制粘贴my.cnf内容，:wq!命令保存退出my.cnf文件

# 修改my.cnf文件权限
sudo chmod 664 /etc/my.cnf

# 设置MySQL配置
系统偏好设置 - MySQL - Configuration - Configuration File：/private/etc/my.cnf

# 重启MySQL
sudo /usr/local/mysql/support-files/mysql.server restart

# 开启本地导入权限
set global local_infile=1;

# 创建数据库
CREATE DATABASE IF NOT EXISTS SaiDB;

# 使用数据库
use SaiDB;

# 建表
CREATE TABLE `PourData` (
	`id` varchar(100) NOT NULL,
	`user_id` varchar(50) NOT NULL,
	`udid` varchar(50) NOT NULL,
	`os` varchar(50) NOT NULL,
	`version` varchar(50) NOT NULL,
	`timestamp` datetime DEFAULT NULL,
	`分类` varchar(50) NOT NULL,
	`事件` varchar(50) NOT NULL,
	`event_date` date DEFAULT NULL,
	`No` int(10) AUTO_INCREMENT NOT NULL PRIMARY KEY) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_0900_ai_ci;

# 确认csv 文件是ANSI 编码

# 导入
load data local infile  '/Users/sai/Documents/MyTestStore/test.csv'
into table PourData
fields terminated by ',' #分隔符
optionally enclosed by '"' escaped by '"'
lines terminated by '\n'
IGNORE 1 ROWS #忽略csv文件第一行
;
```

my.cnf内容

```bash
[client]  
default-character-set=utf8  
port        = 3306 
#根据实际情况调整mysql.sock配置
socket      = /tmp/mysql.sock  
default-character-set= utf8mb4

[mysqld]  
default-storage-engine=INNODB  
character-set-server=utf8  
collation-server=utf8_general_ci  
# 服务端口号 默认3306
port        = 3306
# MySQL按照目录
basedir = /usr/local/mysql
# MySQL数据文件所在位置
datadir = /usr/local/mysql/data
# socke文件所在目录
socket      = /tmp/mysql.sock
# 临时目录
tmpdir = /tmp
skip-external-locking  
key_buffer_size = 16K  
max_allowed_packet = 1M  
table_open_cache = 4 
sort_buffer_size = 64K  
read_buffer_size = 256K  
read_rnd_buffer_size = 256K  
net_buffer_length = 2K  
thread_stack = 128K
#设置为空，即允许导入数据
secure_file_priv=
#Mysql服务的唯一编号 每个mysql服务Id需唯一
server-id   = 1 
character-set-client-handshake = FALSE
character-set-server = utf8mb4
collation-server = utf8mb4_unicode_ci
init_connect='SET NAMES utf8mb4'

[mysqldump]  
quick  
max_allowed_packet = 16M  

[mysql]  
no-auto-rehash  
local-infile=1
default-character-set= utf8mb4

[myisamchk]  
key_buffer_size = 8M  
sort_buffer_size = 8M  

[mysqlhotcopy]  
interactive-timeout
```

* [MySQL字段支持表情包](https://blog.csdn.net/dongwuming/article/details/79761096)

  ```mysql
  ALTER DATABASE 数据库名 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci;
  
  ALTER TABLE 表名 CONVERT TO CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
  ```

  

#### 4. python连接MySQL

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





