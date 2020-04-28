# [Todolist](https://github.com/jiangsai0502/todolist)源码阅读实例

### 第1版：显示TodoList

#### 准备工作

1. 下载源码

   ```bash
   $ cd ~/Documents/FlaskProjects && git clone https://github.com/jiangsai0502/todolist.git
   ```

2. 切换到第一次提交

   ```bash
   $ cd todolist && git checkout ae5fa41ec42b20475553da1893b2a86b0546bd35
   ```

3. 导入数据库表结构

   ```bash
   $ mysql -h 127.0.0.1 -P 3306 -u root -p SaiDB < schema.sql
   ```

   > `mysql`命令的参数区分大小写，如`-P`表示端口号，`-p`表示数据库名

   schema.sql

   ```bash
   CREATE TABLE IF NOT EXISTS `todolist` (
     `id` int(11) NOT NULL AUTO_INCREMENT,
     `user_id` int(11) NOT NULL,
     `title` varchar(1024) NOT NULL,
     `status` int(2) NOT NULL COMMENT '0:未完成 1:完成',
     `create_time` int(11) NOT NULL,
     PRIMARY KEY (`id`)
   )
   ```

4. 导入数据

   ```bash
   mysql> insert into todolist(user_id, title, status, create_time) values(1, '习近平五谈稳中求进 织密扎牢民生保障网', '1', 1482214350), (1, '特朗普获超270张选举人票将入主白 宫', '0', 1482214350);
   ```

5. 创建项目虚拟环境

   ```bash
   $ conda create -n py2_todolist python=2 && source activate py2_todolist
   ```

6. 导入依赖包

   ```bash
   $ pip install -r requirements.txt
   ```

   requirements.txt

   ```bash
   pymysql
   flask
   ```

#### 源码分析

1. app.py

   ```python
   import pymysql
   from flask import Flask, render_template, g
   
   app = Flask(__name__)
   app.secret_key = 'This is my key'
   
   #返回一个新的数据库连接
   def connect_db():
       return pymysql.connect(host='127.0.0.1',
               user='root',
               passwd='will',
               db='saidb',
               charset='utf8')
   
   #每次请求，都专门创建一个新的数据库连接
   @app.before_request
   def before_request():
       g.db = connect_db()
   
   #每次请求执行后，都关闭为本次请求创建的数据库连接
   @app.after_request
   def after_request(response):
       g.db.close()
       return response
   
   @app.route('/')
   def show_todo_list():
       sql = 'select id, user_id, title, status, create_time from todolist'
       with g.db as cur:
           cur.execute(sql)
           data = cur.fetchall()
           todo_list = [ dict(id=row[0], user_id=row[1], title=row[2], status=bool(row[3]), create_time=row[4]) for row in data]
       return render_template('index.html', todo_list=todo_list)
   
   if __name__ == '__main__':
   	app.run(host='0.0.0.0', port=5000, debug=True)
   ```

2. index.html

   ```js
   <table class="table table-hover">
       <thead>
           <th class="active">No</th>
           <th class="active">描述</th>
           <th class="active">是否完成</th>
           <th class="active">创建时间</th>
       </thead>
       <tbody>
           {% for todo in todo_list %}
               <td>{{ loop.index }}</td>
               <td>{{ todo['title'] }}</td>
               <td>{{ todo['status'] }}</td>
               <td>{{ todo['create_time'] }}</td>
               </tr>
           {% endfor %}
       </tbody>
   </table>
   ```

3. 解析

   > 1. `loop.index`：是`flask jinjia loop`变量，表示当前迭代索引(从1开始)
   >
   > 2. `flask之g对象`[案例参考](https://www.jianshu.com/p/d4385c637d95)
   >
   >    1. g的全称是global，专门用来存储用户信息
   >    2. g对象在一次请求设计的所有的代码的地方，都可以使用，甚至跨文件
   >    3. session对象跨request，只要session还未过期，不同的request请求能使用同一个session
   >    4. g对象更牛逼，根本不会，请求一次就g对象就改变了一次，能一直使用
   >
   >    > 本例中使用g.db作为数据库连接
   >
   > 3. `@app.before_request`与`@app.after_request`
   >
   >    > 钩子函数：即运行路由函数前或后会被顺带运行的函数
   >    >
   >    > * `@app.before_request`：运行**路由函数**前被运行的函数
   >    >
   >    >   ```python
   >    >   from flask import Flask
   >    >   
   >    >   app = Flask(__name__)
   >    >   
   >    >   @app.before_request
   >    >   def Sai_b_r_1():
   >    >       print("------Sai_b_r_1-------")
   >    >   
   >    >   # @app.before_request
   >    >   def Sai_b_r_2():
   >    >       print("------Sai_b_r_2-------")
   >    >   
   >    >   @app.before_request
   >    >   def Sai_b_r_3():
   >    >       print("------Sai_b_r_3-------")
   >    >   
   >    >   @app.route("/")
   >    >   def index():
   >    >       print("------执行了index()视图------")
   >    >       return "str"
   >    >   
   >    >   if __name__ == '__main__':
   >    >       app.run(host='0.0.0.0', port=5000, debug=True)
   >    >   ```
   >    >
   >    >   > ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200428210947.png)
   >    >   >
   >    >   > > `def Sai_b_r_2()`没有执行，因为没有被钩子函数`@app.before_request`修饰
   >    >
   >    > * `@app.after_request`：运行**路由函数**后被运行的函数
   >    >
   >    >   ```python
   >    >   from flask import Flask
   >    >   
   >    >   app = Flask(__name__)
   >    >   
   >    >   @app.after_request
   >    >   def Sai_a_r1(res):
   >    >       print("Sai_a_r1------", res)
   >    >       return res
   >    >   
   >    >   def Sai_a_r2(res):
   >    >       print("Sai_a_r2------", res)
   >    >       return res
   >    >   
   >    >   @app.after_request
   >    >   def Sai_a_r3(res):
   >    >       print("Sai_a_r3------", res)
   >    >       return res
   >    >   
   >    >   @app.route("/")
   >    >   def index():
   >    >       print("执行了index()视图------")
   >    >       return "这是Sai首页"
   >    >   
   >    >   if __name__ == '__main__':
   >    >       app.run(host='0.0.0.0', port=5000, debug=True)
   >    >   ```
   >    >
   >    >   > ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200428210702.png)
   >    >   >
   >    >   > * `@app.after_request`：必须有一个参数,这个参数实际上是服务器的响应，且函数必须返回这个响应参数.
   >    >
   >    > [所有钩子函数](https://www.jianshu.com/p/971e80c0c8f1)
   >    >
   >    > ```python
   >    > from flask import Flask
   >    > 
   >    > app = Flask(__name__)
   >    > 
   >    > @app.before_first_request
   >    > def Sai_b_f_r():
   >    >     print("----before_first_request----")
   >    >     print("系统初始化的时候,执行这个钩子方法")
   >    >     print("用途：会在接收第一个客户端请求时,执行这里的代码，如建立数据库连接")
   >    > 
   >    > @app.before_request
   >    > def Sai_b_r():
   >    >     print("----before_request----")
   >    >     print("每一次接收到客户端请求时,执行这个钩子方法")
   >    >     print("用途：一般可以用来判断权限,或者转换路由参数或者预处理客户端请求的数据")
   >    > 
   >    > @app.after_request
   >    > def Sai_a_r(response):
   >    >     print("----after_request----")
   >    >     print("在处理请求以后,执行这个钩子方法")
   >    >     print("用途：一般可以用于记录会员/管理员的操作历史,浏览历史,清理收尾的工作")
   >    >     # 必须返回response参数
   >    >     return response
   >    > 
   >    > @app.teardown_request
   >    > def Sai_t_r(exc):
   >    >     print("----teardown_request----")
   >    >     print("用途：每次请求后执行；接收一个参数：错误信息，如果有相关错误抛出，需要设置flask的配置DEBUG=False，teardown_request才会接收到异常对象")
   >    >     print(exc)
   >    > 
   >    > @app.route("/")
   >    > def index():
   >    >     print("----视图函数----")
   >    >     print("index()视图函数被运行了")
   >    >     return "index()视图函数被运行了<br>"
   >    > 
   >    > if __name__ == '__main__':
   >    >     app.run(host='0.0.0.0', port=5000, debug=False)
   >    >     # app.run(host='0.0.0.0', port=5000, debug=True)
   >    > ```





