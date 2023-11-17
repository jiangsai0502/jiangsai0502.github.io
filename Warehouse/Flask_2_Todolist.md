# [Todolist](https://github.com/jiangsai0502/todolist)源码阅读实例

### 第1版：显示TodoList

#### 准备工作

1. 下载源码

   ```bash
   $ cd ~/Documents/FlaskProjects && git clone https://github.com/jiangsai0502/todolist.git
   ```

2. 切换到第1次提交

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
   
   #返回一个新的数据库连接
   def connect_db():
       return pymysql.connect(host='127.0.0.1',
               user='root',
               passwd='will',
               db='saidb',
               charset='utf8')
   
   #每次请求，都专门创建一个新的数据库连接
   @app.before_request
   def Sai_b_r():
       g.db = connect_db()
   
   #每次请求执行后，都关闭为本次请求创建的数据库连接
   @app.after_request
   def Sai_a_r(response):
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

   > 1. `cur.fetchall()`：一次`fetchall()`之后，`cur`里的数据就没了，再次`fetchall()`就拿不到东西了
   >
   > 2. `loop.index`：是`flask jinjia loop`变量，表示当前迭代索引(从1开始)
   >
   > 3. `flask之g对象`[案例参考](https://www.jianshu.com/p/d4385c637d95)
   >
   >    1. g的全称是global，专门用来存储用户信息
   >    2. g对象在一次请求设计的所有的代码的地方，都可以使用，甚至跨文件
   >    3. session对象跨request，只要session还未过期，不同的request请求能使用同一个session
   >    4. g对象更牛逼，根本不会，请求一次就g对象就改变了一次，能一直使用
   >
   >    > 本例中使用g.db作为数据库连接
   >
   > 4. `@app.before_request`与`@app.after_request`
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



### 第2版：增加login和logout

#### 准备工作

1. 切换到第2次提交

   ```bash
   $ rm -rf ~/Documents/FlaskProjects/todolist
   $ cd ~/Documents/FlaskProjects && git clone https://github.com/jiangsai0502/todolist.git
   $ cd todolist && git checkout 5b9cf5d88c0846cbce46d8970834930bd38e4370
   ```

#### 源码分析

1. app.py

   ```python
   import pymysql
   from flask import Flask, render_template, g, session, redirect, url_for, request
   
   app = Flask(__name__)
   app.config['SECRET_KEY'] = 'ThisIsTheKey'
   app.config['USERNAME'] = 'admin'
   app.config['PASSWORD'] = 'admin'
   
   #返回一个新的数据库连接
   def connect_db():
       return pymysql.connect(host='127.0.0.1',
               user='root',
               passwd='will',
               db='saidb',
               charset='utf8')
   
   #每次请求，都专门创建一个新的数据库连接
   @app.before_request
   def Sai_b_r():
       g.db = connect_db()
   
   #每次请求执行后，都关闭为本次请求创建的数据库连接
   @app.after_request
   def Sai_a_r(response):
       g.db.close()
       return response
   
   @app.route('/')
   def show_todo_list():
       if not session.get('logged_in'):
           return redirect(url_for('login'))
       else:
           sql = 'select id, user_id, title, status, create_time from todolist'
           with g.db as cur:
               cur.execute(sql)
               data = cur.fetchall()
               todo_list = [ dict(id=row[0], user_id=row[1], title=row[2], status=bool(row[3]), create_time=row[4]) for row in data]
           return render_template('index.html', todo_list=todo_list)
   
   @app.route('/login', methods=['GET', 'POST'])
   def login():
       error = None
       if request.method == 'POST':
           if request.form['username'] != app.config['USERNAME']:
               error = 'Invalid username'
           elif request.form['password'] != app.config['PASSWORD']:
               error = 'Invalid password'
           else:
               session['logged_in'] = True
               return redirect(url_for('show_todo_list'))
       return render_template('login.html')
   
   @app.route('/logout')
   def logout():
       session.pop('logged_in', None)
       return redirect(url_for('login'))
   
   if __name__ == '__main__':
   	app.run(host='0.0.0.0', port=5000, debug=False)
   	# app.run(host='0.0.0.0', port=5000, debug=True)
   ```

2. login.html

   ```js
   <div class="row">
       <div class="col-md-4 col-md-offset-4">
           <form class="form-signin" role="form" method='POST' action="{{url_for('login') }}">
               <h2 class="form-signin-heading">please sigin in</h2>
               <input type="username" name="username" class="form-control" placeholder="username" required autofocus><br>
               <input type="password" name="password" class="form-control" placeholder="Password" required><br>
               <button class="btn btn-lg btn-primary btn-block" type="submit">Sign in</button>
           </form>
       </div>
   </div>
   ```

3. 流程图

   ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200429121008.png)

4. 解析

   > 1. `app.config[]`
   >
   >    * `app.config`是flask配置的统一接口，用户配置和获取配置
   >
   >    * 使用方式
   >
   >      1. 直接写在app.py主程序文件里
   >
   >         ```python
   >         app.config['SECRET_KEY'] = 'ThisIsTheKey'
   >         app.config['USERNAME'] = 'admin'
   >         app.config['PASSWORD'] = 'admin'
   >         ```
   >
   >      2. 单独拎出一个配置文件
   >
   >         app.py
   >
   >         ```python
   >         app.config.from_pyfile('default_config.py')
   >         ```
   >
   >         default_config.py
   >
   >         ```python
   >         SECRET_KEY = 'ThisIsTheKey'
   >         USERNAME = 'admin'
   >         PASSWORD = 'admin'
   >         ```
   >
   > 2. `app.config['SECRET_KEY']`
   >
   >    > `flask`的`session`是通过加密之后放到`cookie`中的。有加密就有密钥用于解密，所以只要用到了`flask`的`session`模块就一定要配置`SECRET_KEY`这个全局宏
   >
   > 3. `session`
   >
   >    1. 作用：**不同请求之间传递数据**（ HTTP 是无状态协议，后端无法知道不同请求是否来自同一个人）
   >    2. 原理：
   >       1. 用户第一次请求，客户端的HTTP request（cookie为空）到服务端，服务端创建session，视图函数根据用户请求中的form表单填写session，请求结束时，session内容填写入response的cookie中并返回给客户端，客户端的cookie中便保存了用户的数据。
   >       2. 同一客户端再次请求时， 客户端的HTTP request中cookie已经携带数据，视图函数根据cookie中值做相应操作（如已经携带用户名和密码就可以直接登陆）




### 第3版：添加flash消息

#### 准备工作

1. 切换到第3次提交

   ```bash
   $ rm -rf ~/Documents/FlaskProjects/todolist
   $ cd ~/Documents/FlaskProjects && git clone https://github.com/jiangsai0502/todolist.git
   $ cd todolist && git checkout 2116581c8618fb9e1daf7477899614f8622c1f55
   ```

#### 源码分析

1. app.py

   ```python
   @app.route('/login', methods=['GET', 'POST'])
   def login():
       error = None
       if request.method == 'POST':
           if request.form['username'] != app.config['USERNAME']:
               flash('Invalid username')
           elif request.form['password'] != app.config['PASSWORD']:
               flash('Invalid password')
           else:
               session['logged_in'] = True
               flash('you have logged in!')
               return redirect(url_for('show_todo_list'))
       return render_template('login.html')
   
   @app.route('/logout')
   def logout():
       session.pop('logged_in', None)
       flash('you have logout!')
       return redirect(url_for('login'))
   ```

2. base.html

   ```html
   <!-- flash message -->
   {% for message in get_flashed_messages() %}
   <div class="alert alert-warning alert-dismissible" role="alert">
       <button type="button" class="close" data-dismiss="alert">
           <span aria-hidden="true">&times;</span>
           <span class="sr-only">close</span></button>
       {{ message }}
   </div>
   {% endfor %}
   ```

3. 解析

   > `flash`传递给前端的信息若没有被`get_flashed_messages()`拿出来，则会一直堆积在`flash队列`中



### 第4版：增加 todo 条目

#### 准备工作

1. 切换到第4次提交

   ```bash
   $ rm -rf ~/Documents/FlaskProjects/todolist
   $ cd ~/Documents/FlaskProjects && git clone https://github.com/jiangsai0502/todolist.git
   $ cd todolist && git checkout f8cfe0f926fa2e35a527323fa34081c5f72a0816
   ```

#### 源码分析

1. app.py



### 第5版：删除 todo 条目

#### 准备工作

1. 切换到第5次提交

   ```bash
   $ rm -rf ~/Documents/FlaskProjects/todolist
   $ cd ~/Documents/FlaskProjects && git clone https://github.com/jiangsai0502/todolist.git
   $ cd todolist && git checkout c03a59d37798f9d7b708ea0fbee8a40a8e4a7106
   ```

#### 源码分析

1. app.py

