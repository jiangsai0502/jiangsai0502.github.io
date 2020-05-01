### 安装 flask 环境

1. 查看虚拟环境   `conda info --envs`

2. 创建虚拟环境   `conda create -n flask_py3.8 python=3.8`

    > 虚拟环境位置：~/miniconda3/envs/flask_py3.8

3. 激活虚拟环境   `source activate flask_py3.8`

4. 安装flask   `pip install flask`

    > Flask被安装位置：`~/miniconda3/envs/flask_py3/lib/python3.8/site-packages/`
    >
    > 卸载flask`pip uninstall flask`

    * 安装 Flask-WTF 表单插件   `pip install Flask-WTF`
    * 安装 flask-sqlalchemy 数据库抽象插件   `pip install flask-sqlalchemy`
    * 安装 flask-mysqldb 数据库插件   `pip install pymysql`
    * 安装 MySQL 数据库插件   `pip install cryptography`

5. 查看环境下所有包   `conda list`

6. 配置 VS Code 环境设置 

    ```bash
    $ which python
    /Users/sai/miniconda3/envs/flask_py3/bin/python
    ```

    ```bash
    setting.json : "python.pythonPath": "/Users/sai/miniconda3/envs/flask_py3/bin/python"
    ```

    > 1. 下图修改的`setting.json`是项目的配置文件，而不是全局的配置文件
    >    * 项目配置文件：`/Users/sai/Documents/FlaskProjects/.vscode/settings.json`
    >    * 全局配置文件：`/Users/sai/Library/Application Support/Code/User/settings.json`
    >
    > 2. `/Users/sai/miniconda3/envs/flask_py3/bin/python`不能写成`~/miniconda3/envs/flask_py3/bin/python`

    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/uPic/image-20200424231604934.png)

    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/uPic/image-20200424232720416.png)

7. requirements.txt
    1. python项目中必须包含一个 requirements.txt 文件，用于记录所有依赖包及其精确的版本号，以便新环境部署

    2. 在本机的虚拟环境下使用pip生成    `pip freeze >requirements.txt`
       
    3. 将 requirements.txt 文件拷贝到部署机器的虚拟目录下，进入文件所在目录，进入虚拟环境，安装全部依赖

        ```bash
        cd /Users/jiangsai02/opt/anaconda3/envs/flask_py3
        source activate flask_py3
        pip install -r requirements.txt
        ```

#### Flask 调试

> ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200425195458.png)
>
> 1. `lanuch.json`是`debug`相关的配置文件
>
> 2. "stopOnEntry": true 进入程序时立即暂停执行，相当于在程序的第一行放一个断点
>
>    > ```bash
>    > "configurations": [
>    >     {
>    >         "name": "Python: Current File (Integrated Terminal)",
>    >         "type": "python",
>    >         "request": "launch",
>    >         "program": "${file}",
>    >         "console": "integratedTerminal",
>    >         "stopOnEntry": true,
>    >     }
>    > ]
>    > ```
>
> 3. **切记！！！** ：Flask在启动时必须指定 `app.run(debug=False)`，一定不能开启调试！否则无法命中断点
>
>    ```python
>    if __name__ == '__main__':
>        app.run(debug = False)
>    ```
>
> 4. 监视变量
>
>    Debug 时有两种方式监视变量
>
>    <1> variables (变量窗口) 会默认显示当前 scope 内的 local 变量的值 
>
>    <2> watch (监视窗口) 是用户自己输入的表达式，因此不仅限于变量的值，还可以监视变量的变化
>
>    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200124144504.png)
>
> 5. [参考](https://zhuanlan.zhihu.com/p/41189402)



### 一个最小的应用：返回字符串

```python
#1. 导入flask扩展
from flask import Flask

#2. 创建flask程序实例，传入__name__，作用是确定资源所在位置
app = Flask(__name__)

#3. 定义路由及视图函数
@app.route('/', methods = ['GET', 'POST'])
def hello_world():
    return 'Hello Flask Sai!'

@app.route('/<order_id>')
def get_order_id(order_id):
    print(f'你的订单号类型 : {type(order_id)}')
    return f'你的订单号 : {order_id}'

#4. 启动程序
if __name__ == '__main__':
    app.run(debug = True)
```

**剖析**

> 1. 定义路由及视图函数
> > ```python
> > @app.route('/', methods = ['GET', 'POST'])
> > def hello_world():
> >  return 'Hello Flask Sai!'
> > ```
> > 1. 用 app 变量的 route() 装饰器来告诉 Flask 框架，哪些 URL 触发哪些视图函数
> > 2. 如 对路径 '/' 的请求，将触发对 hello_world() 函数的调用
> > 3. 如 对路径 '/<order_id>' 的请求，将触发对 get_order_id() 函数的调用
> > 4. 路由默认只支持 GET 请求，可用 methods = [] 自行扩展
> >
> > ```python
> > @app.route('/<order_id>')
> > def get_order_id(order_id):
> >     return f'Your order ID : {order_id}'
> > ```
> > 1. 使用同一个视图函数 get_order_id() 显示不同用户的订单信息
> > 2. 格式：
> >    1. `<>`定义路由的参数 <路由参数> 
> >    2. get_order_id(路由参数)
>
> 3. 启动程序
> > ```python
> > if __name__ == '__main__':
> >     app.run(debug = True)
> > ```
> > 1. app.run()将 Flask 运行到一个 Flask 提供的简易测试服务器上
> > 2. debug = True 启动调试模式，每次修改代码后服务自动重启
> > 3. app.run(port = 8888, debug = True) 可将 Web 服务默认监听本地的 5000 端口修改为监听 8888 端口，即 http://127.0.0.1:8888/



### 一个最小的应用：返回jinja2网页

* 创建一个基本的 Flask 目录结构

  ```bash
  ├── ~/Documents/Temp/SaiFlask/
      ├── MyApp.py
      ├── templates/
          ├── MyTemplate.html
          └── HelloYou.html
      └── static/
          ├── TeddyBear.jpg
  ```

  | 目录        | 描述                                                 |
  | ----------- | ---------------------------------------------------- |
  | `MyApp.py`  | 主程序                                               |
  | `templates` | 存放模板文件                                         |
  | `static`    | 存放静态文件，如图片，音频，视频，JS文件以及样式文件 |


* 变量代码块：单一变量

  ```python
  from flask import Flask, render_template
  
  app = Flask(__name__)
  
  @app.route('/', methods = ['GET', 'POST'])
  @app.route('/<name>')
  def SingleArg(name = None):
      return render_template('MyTemplate.html', FEname = name)
  
  if __name__ == '__main__':
      app.run(debug = True)
  ```

  > * 渲染模板需要导入 `render_template`
  > * 对路径 `/` 的请求，将触发对 `SingleArg()` 函数的调用
  > * 对路径 `/\<name>` 的请求，将触发对 `SingleArg()` 函数的调用，`<name>` 是任意 str
  > * `render_template('MyTemplate.html')` 将渲染 `templates` 目录下的 `MyTemplate.html` 模板
  > * 模板 `MyTemplate.html` 中的变量名和 `MyApp.py` 中的变量保持一致，即 `FEname = name`

  ```javascript
  <!doctype html>
  <title>单一变量</title>
  {% if FEname %}
      <h1>Hello {{ FEname }}!</h1>
  {% else %}
      <h1>Hello World!</h1>
  {% endif %}
  ```

  > * `{{ args }}` 表示 HTML 的变量代码块
  >   * `args` 变量可以是任意类型，如`{{ arg }}`，`{{ my_list[0] }}`，`{{ my_dict['key'] }}`
  > * `FEname = name` ：等号前的`FEname`是前端html模板的变量，等号后的`name`是后端的变量

  > * 网址输入`http://127.0.0.1:5000/`，则展示`Hello World!`
  > * 网址输入`http://127.0.0.1:5000/sai`，则展示`Hello sai!`

* 变量代码块：多变量

  ```python
  from flask import Flask, render_template
  
  app = Flask(__name__)
  
  @app.route('/')
  def MoreArgs():
      webName = '多变量'
      myList = [1, 3, 5, 7, 9, 11, 13]
      myDict = {'name':'sai','age':18}
  
      return render_template('MyTemplate.html', web_name = webName, my_list = myList, my_dict = myDict)
    
  if __name__ == '__main__':
      app.run(debug = True)
  ```

  ```javascript
  <!doctype html>
  <title>{{ web_name }}</title>
  
  my_list 是 {{ my_list }} , 共 {{ my_list | length }} 个元素, 其中第2个是 {{ my_list[1] }} <br>
  my_dict 是 {{ my_dict }} , 共 {{ my_dict | length }} 个元素, age对应的值是 {{ my_dict['age'] }} <br>
  ```

* 控制代码块

  ```python
  from flask import Flask, render_template
  
  app = Flask(__name__)
  
  @app.route('/')
  def Controller():
      myList = [1, 3, 5, 7, 9, 11, 13]
      myDict = {'name':'sai','age':18}
      movieList = [
      {'title': 'xxxxx', 'year': '1988'},
      {'title': 'yyyyy', 'year': '1989'}
      ]
      return render_template('MyTemplate.html', my_list = myList, my_dict = myDict, movie_list = movieList)
    
  if __name__ == '__main__':
      app.run(debug = True)
  ```

  ```javascript
  <!doctype html>
  <title> 控制代码块 </title>
  
  遍历 my_list 中小于10的数
  {% for num in my_list %}
      {% if num < 10 %}
          {{ num }}, 
      {% endif %}
  {% endfor %} <br>
  
  遍历 my_dict  <br>
  {% for k,v in my_dict.items() %}
      {{k}}：{{v}} <br>
  {% endfor %}
  
  遍历 movie_list <br>
  {% for movie in movie_list %}
      {{ movie['title'] }} - {{ movie['year'] }} <br>
  {% endfor %}
  ```

* 过滤器

  ```python
  from flask import Flask, render_template
  
  app = Flask(__name__)
  
  @app.route('/')
  def Filter():
      myStr = 'My name is Sai'
      myList = [1, 3, 5, 7, 9, 11, 13]
      return render_template('MyTemplate.html', my_str = myStr, my_list = myList)
    
  if __name__ == '__main__':
      app.run(debug = True)
  ```

  ```javascript
  <!doctype html>
  <title>Hello Filter</title>
  
  原字符串是：{{my_str}} <br>
  字符串全大写：{{my_str | upper }} <br>
  字符串全小写：{{my_str | lower }} <br>
  字符串首单词首字母大写：{{my_str | capitalize }} <br>
  字符串所有单词首字母大写：{{my_str | title }} <br>
  字符串反转+全大写：{{my_str | reverse | upper }} <br>
  <hr>
  原list是：{{my_list}} <br>
  list第1个元素：{{my_list | first }} <br>
  list最后1个元素：{{my_list | last }} <br>
  list长度：{{my_list | length }} <br>
  list排序：{{my_list | sort }} <br>
  ```

  > 1. 过滤器格式：变量名 | 过滤器 {{ variable | filter_name(*args) }}
  > 2. 过滤器的链式调用，即拼接多个过滤器 {{ variable | filter_name(\*args) | filter_name(\*args) }}

* 原生表单

  ```python
  from flask import Flask, render_template, request
  
  app = Flask(__name__)
  
  # 定义路由，设置请求方式
  # 1. 第1次请求是Get请求，为了获取空表单
  # 2. 第2次请求是Post请求，为了提交表单数据
  @app.route('/', methods = ['GET', 'POST'])
  def OriginalWF():
      #3. 判断请求方式
      if request.method == 'POST':
        #4. 获取请求参数
          username = request.form.get('user_name')
          password = request.form.get('pass_word')
          password2 = request.form.get('pass_word2')
          print(f'你输入的用户：{username}，密码：{password}，确认密码：{password2}')
          #5. 对参数进行逻辑判断
          if not all([username, password, password2]):
              result = '输入不完整'
          elif password != password2:
              result = '两次输入的密码不同'
          else:
              result = 'POST 成功了, Yeah'
          return result
      return render_template('MyTemplate.html')
  
  if __name__ == '__main__':
      app.run(debug = True)
  ```

  > 1. 路由通过 request.method 判断请求方式：'GET', 'POST' 。必须大写
  > 2. 路由通过 request.form.get() 从前端获取请求的参数

  ```javascript
  <!doctype html>
  <form method="POST">
      <label>用户名：</label> <input type="text" name="user_name"></p>
      <label>密码：</label> <input type="password" name="pass_word"></p>
      <label>确认密码：</label> <input type="password" name="pass_word2"></p>
      <input type="submit" value="提交"><br>
  </form>
  ```

* 原生表单（后端向前端传递消息）

  > ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200425170002.png)
  >
  > ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200425172613.png)

  ```python
  from flask import Flask, render_template, request, flash
  
  app = Flask(__name__)
  app.secret_key = 'The secret string for encryption'
  
  @app.route('/', methods = ['GET', 'POST'])
  def OriginalWF_Flash():
      if request.method == 'POST':
          username = request.form.get('user_name')
          password = request.form.get('pass_word')
          password2 = request.form.get('pass_word2')
          print(f'你输入的用户：{username}，密码：{password}，确认密码：{password2}')
          if not all([username, password, password2]):
              flash('输入不完整')
          elif password != password2:
              flash('两次输入的密码不同')
          else:
              return 'OriginalWF_Flash 成功了, Yeah'
      return render_template('MyTemplate.html')
  
  if __name__ == '__main__':
      app.run(debug = True)
  ```

  > 1. 从后端向前端传递消息，要导入 flash 模块
  > 2. 通过 secret_key 给后端的消息加密

  ```javascript
  <!doctype html>     
  <form method="POST">
      {# wtf必须开启CSRF保护，使用csrf_token()函数 #}
      {{ login_Form.csrf_token() }}
      {{ login_Form.username.label }} : {{ login_Form.username }} <br>
      {{ login_Form.password.label }} : {{ login_Form.password }} <br>
      {{ login_Form.password2.label }} : {{ login_Form.password2 }} <br>
      {{ login_Form.submit }} <br>
  </form>
  
  {# 获取后端传递的flash消息 #}
  {% for message in get_flashed_messages() %}
      {{ message }}
  {% endfor %}
  ```

  > `get_flashed_messages()` ：此函数能从后端获取消息list

* Flask表单wtf

  > 优势：很多验证函数，省去了写自己写逻辑判断的工作
  >
  > 用法：1. python中定义表单类，往表单类中存数据  2. html中从表单类中取数据
  >
  > ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200425230425.png)
  >
  > ![](https://gitee.com/jiangsai0502/PicBedRepo/raw/master/img/20200426114019.png)

  ```python
  from flask import Flask, render_template, request, flash
  from flask_wtf import FlaskForm   #导入wtf表单类
  from wtforms import StringField, PasswordField, SubmitField   #导入表单所需字段
  from wtforms.validators import EqualTo, DataRequired, Length  #导入表单验证器
  
  app = Flask(__name__)
  app.secret_key = 'The secret string for encryption'
  
  #1. 定义表单类
  class LoginForm(FlaskForm):
      username = StringField('用户名', validators = [DataRequired(), Length(min=3,max=10,message="用户名长度有问题")])
      password = PasswordField('密码')
      password2 = PasswordField('确认密码', validators = [DataRequired(), EqualTo('password', '密码不一致')])
      submit = SubmitField('提交')
  
  #2. 定义路由，设置请求方式
  @app.route('/', methods = ['GET', 'POST'])
  def FlaskWTForm():
      loginForm = LoginForm()
      print(f'FlaskWTForm 用户名：{loginForm.username.data}, 密码：{loginForm.password.data}, 确认密码：{loginForm.password2.data}')
      
      if request.method == 'POST':
          if loginForm.validate_on_submit():   #3. wtf一句话实现所有校验
              return 'FlaskWTForm 成功了, Yeah'
          else:
              flash(loginForm.errors)
      return render_template('MyTemplate.html', login_Form = loginForm)
  
  if __name__ == '__main__':
      app.run(debug = False)
      # app.run(debug = True)
  ```

  > * 类实例.字段名.label：表示字段名
  > * 类实例.字段名.data：表示字段值

  ```javascript
  <!doctype html>
  <form method="POST">
      {# wtf必须开启CSRF保护，使用csrf_token()函数 #}
      {{ login_Form.csrf_token() }}
      {{ login_Form.username.label }} : {{ login_Form.username }} <br>
      {{ login_Form.password.label }} : {{ login_Form.password }} <br>
      {{ login_Form.password2.label }} : {{ login_Form.password2 }} <br>
      {{ login_Form.submit }} <br>
  </form>
  
  {% for message in get_flashed_messages() %}
      {{ message }}
  {% endfor %}
  ```

  | 字段类型            | 字段说明                                   | 验证函数     | 函数说明                                    |
  | ------------------- | ------------------------------------------ | ------------ | ------------------------------------------- |
  | StringField         | 文本字段， 相当于type类型为text的input标签 | DataRequired | 确保字段中有数据                            |
  | PasswordField       | 密码文本字段                               | EqualTo      | 比较两个字段的值， 常用于密码的两次输入确认 |
  | SubmitField         | 表单提交按钮                               | Length       | 验证输入字符串的长度                        |
  | DateField           | 文本字段， 值为datetime.date格式           | URL          | 验证url                                     |
  | IntegerField        | 文本字段， 值为整数                        | Email        | 验证是电子邮件地址                          |
  | FloatField          | 文本字段， 值为浮点数                      | IPAddress    | 验证IPv4网络地址                            |
  | BooleanField        | 复选框， 值为True 和 False                 | NumberRange  | 验证输入的值在数字范围内                    |
  | RadioField          | 一组单选框                                 |              |                                             |
  | SelectField         | 下拉列表                                   |              |                                             |
  | SelectMultipleField | 下拉列表， 可选择多个值                    |              |                                             |
  | TextAreaField       | 多行文本字段                               |              |                                             |
  | FileField           | 文件上传字段                               |              |                                             |



### 一个最小的应用：使用数据库

1. 查

   ```python
   from flask import Flask, render_template, request
   from flask_sqlalchemy import SQLAlchemy
   
   app = Flask(__name__)
   
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:will@127.0.0.1/SaiDB'
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   myDB = SQLAlchemy(app)
   
   @app.route('/', methods = ['GET', 'POST'])
   def select():
       sql = "select * from student where id = '%s';" %(901)
       data = myDB.session.execute(sql)
       my_list = data.fetchall()
       return render_template("MyTemplate.html", my_list = my_list)
                                         
   if __name__ == '__main__':
       # app.run(debug=True, port = 8889)
       app.run(debug=False, port = 8889)
   ```

   > * SQLAlchemy，会话用db.session表示

   ```js
   <!doctype html>
   <title>Flask 示例</title>
         操作结果 : {{ my_list }}
         <h2><a href = "/">返回主页</a></h2>
   ```

2. 增

   ```python
   from flask import Flask, render_template, request
   from flask_sqlalchemy import SQLAlchemy
   
   app = Flask(__name__)
   
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:will@127.0.0.1/SaiDB'
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   myDB = SQLAlchemy(app)
   
   @app.route('/',methods = ['POST', 'GET'])
   def insert():
       stu_id = 901
       c_name = '英语'
       if request.method == 'GET':
           try:
               sql = "INSERT INTO score (stu_id,c_name) VALUES ('%s','%s')" %(stu_id,c_name)
               myDB.session.execute(sql)
               myDB.session.commit()
               msg = "插入成功"
           except:
               myDB.session.rollback()
               msg = "插入失败"
           finally:
               return render_template("MyTemplate.html", msg = msg)
                                         
   if __name__ == '__main__':
       # app.run(debug=True, port = 8889)
       app.run(debug=False, port = 8889)
   ```

   > * 由于score的字段 id 的类型是 Int(10)  Not Null  Unique  Primary Key  Auto_Increment，即非空自增整数，因此插入时不必特意声明，会自动自增的

   ```js
   <!doctype html>
   <title>Flask 示例</title>
         操作结果 : {{ msg }}
         <h2><a href = "/">返回主页</a></h2>
   ```

3. 改

   ```python
   from flask import Flask, render_template, request
   from flask_sqlalchemy import SQLAlchemy
   
   app = Flask(__name__)
   
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:will@127.0.0.1/SaiDB'
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   myDB = SQLAlchemy(app)
   
   @app.route('/',methods = ['POST', 'GET'])
   def insert():
       ID = 14
       Grade = 40
       if request.method == 'GET':
           try:
               sql = "UPDATE score SET Grade = '%d' WHERE ID = '%s'" %(Grade, ID)
               myDB.session.execute(sql)
               myDB.session.commit()
               msg = "修改成功"
           except:
               myDB.session.rollback()
               msg = "修改失败"
           finally:
               return render_template("MyTemplate.html", msg = msg)
                                         
   if __name__ == '__main__':
       # app.run(debug=True, port = 8889)
       app.run(debug=False, port = 8889)
   ```

   ```js
   <!doctype html>
   <title>Flask 示例</title>
         操作结果 : {{ msg }}
         <h2><a href = "/">返回主页</a></h2>
   ```

4. 删

   ```python
   from flask import Flask, render_template, request
   from flask_sqlalchemy import SQLAlchemy
   
   app = Flask(__name__)
   
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:will@127.0.0.1/SaiDB'
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   myDB = SQLAlchemy(app)
   
   @app.route('/',methods = ['POST', 'GET'])
   def insert():
       ID = 12
       if request.method == 'GET':
           try:
               sql = "DELETE FROM score WHERE ID = '%d'"%(ID)
               myDB.session.execute(sql)
               myDB.session.commit()
               msg = "修改成功"
           except:
               myDB.session.rollback()
               msg = "修改失败"
           finally:
               return render_template("MyTemplate.html", msg = msg)
                                         
   if __name__ == '__main__':
       app.run(debug=True, port = 8889)
       # app.run(debug=False, port = 8889)
   ```

   ```js
   <!doctype html>
   <title>Flask 示例</title>
         操作结果 : {{ msg }}
         <h2><a href = "/">返回主页</a></h2>
   ```

   > 1. 设置连接数据库的URL
   >
   >    ```sql
   >    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:will@127.0.0.1/sql_demo'
   >    ```
   >
   >    > 1. 数据库协议：mysql+pymysql（不可变）
   >    > 2. 用户名：root（可改为其他用户名）
   >    > 3. 用户名密码：will
   >    > 4. 服务器地址：127.0.0.1 或 localhost
   >    > 5. 端口号：3306
   >    > 6. 数据库名：sql_demo
   >
   > 2. 设置每次请求结束后会自动提交数据库的改动（为降低消耗资源，可设为False）
   >
   >    `app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True`
   >
   > 3. 通过类 SQLAlchemy 来连接数据库
   >
   >    `myDB = SQLAlchemy(app)`
   >
   > > 报错`Instance of 'SQLAlchemy' has no 'Column' member`，[参考](https://blog.csdn.net/stone0823/article/details/90488029)

   > * `pymysql`操作游标`cursor`
   >
   > * `SQLAlchemy`操作会话`session`



### 图书管理系统

1. 配置数据库

   ```bash
   $ mysql -u root -p
   
   mysql> use SaiDB;
   
   Mysql> Create Table Books (
       -> Id Int(10) Not Null Unique Primary Key Auto_Increment,
       -> Name Varchar(20) Not Null Unique,
       -> Author Varchar(4)
       -> );
       
   Mysql> Insert Into Books (ID, Name, Author) Values(Null, '肉蒲团', '李渔');
   Mysql> Insert Into Books (ID, Name, Author) Values(Null, '大开眼界', '马尔科姆');
   Mysql> Insert Into Books (ID, Name, Author) Values(Null, '眨眼之间', '马尔科姆');
   Mysql> Insert Into Books (ID, Name, Author) Values(Null, '财富自由之路', '李笑来');
   Mysql> Insert Into Books (Name, Author) Values('把时间当作朋友', '李笑来');
   Mysql> Insert Into Books (Name, Author) Values('数据库系统实现', '加西亚');
   Mysql> Insert Into Books (Name, Author) Values('引爆点', '加西亚');
   Mysql> Insert Into Books (Name, Author) Values('数学思维导论', '加西亚');
   ```

2. 展示数据

   ```python
   from flask import Flask, render_template, request
   from flask_sqlalchemy import SQLAlchemy
   
   app = Flask(__name__)
   
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:will@127.0.0.1/SaiDB'
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   myDB = SQLAlchemy(app)
   
   @app.route('/', methods = ['GET', 'POST'])
   def BooK_list_Index():
       Author_list, Book_list = showBooks()
       return render_template("MyTemplate.html", Author_list = Author_list, Book_list = Book_list)
   
   # 展示所有作者/图书信息
   def showBooks():
       sql = "SELECT author, COUNT(*) count FROM books GROUP BY author;"
       data = myDB.session.execute(sql)
       Author_list = data.fetchall()
       sql = "SELECT author, name FROM books;"
       data = myDB.session.execute(sql)
       Book_list = data.fetchall()
       return Author_list, Book_list
                                         
   if __name__ == '__main__':
       app.run(debug=True, port = 8889)
       # app.run(debug=False, port = 8889)
   ```

   ```js
   <!doctype html>
   <title>Flask 示例</title>
   
   <ul>
       {% for author in Author_list %}
           <li>作者：{{ author['author'] }}，{{ author['count'] }} 本著作</li>
           <ul>
               {% for book in Book_list %}
                   {% if book['author'] == author['author'] %}
                       <li>{{ book['name'] }}</li>
                   {% endif %}
               {% endfor %}
           </ul>
       {% endfor %}
   </ul>
   ```

3. 展示数据（增加wtf表单）

   ```python
   from flask import Flask, render_template, request, flash
   from flask_sqlalchemy import SQLAlchemy
   from flask_wtf import FlaskForm   #导入wtf表单类
   from wtforms import StringField, SubmitField   #导入表单所需字段
   from wtforms.validators import DataRequired  #导入表单验证器
   
   app = Flask(__name__)
   app.secret_key = 'The secret string for encryption'
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:will@127.0.0.1/SaiDB'
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   myDB = SQLAlchemy(app)
   
   #1. 定义表单类
   class BookForm(FlaskForm):
       bookName = StringField('书名', validators = [DataRequired()])
       authorName = StringField('作者', validators = [DataRequired()])
       submit = SubmitField('提交')
   
   @app.route('/', methods = ['GET', 'POST'])
   def BooK_list_Index():
       bookForm = BookForm()
       print(f'书名：{bookForm.bookName.data}, 作者：{bookForm.authorName.data}')
       
       if request.method == 'GET':
           Author_list, Book_list = QueryData()
       elif request.method == 'POST':
           if bookForm.validate_on_submit():
               print('录入数据库操作成功, Yeah')
               Author_list, Books_list = QueryData()
           else:
               flash(bookForm.errors)
       
       return render_template("MyTemplate.html", bookForm = bookForm, Author_list = Author_list, Book_list = Book_list)
   
   # 展示所有作者/图书信息
   def QueryData():
       try:
           sql = "SELECT author, COUNT(*) count FROM books GROUP BY autho;"
           data = myDB.session.execute(sql)
           author_list = data.fetchall()
           sql = "SELECT author, name FROM books;"
           data = myDB.session.execute(sql)
           book_list = data.fetchall()
       except Exception as e:
           print('-'*30,'\n',e,'\n','-'*30)
       return author_list, book_list
                                         
   if __name__ == '__main__':
       # app.run(debug=True, port = 8889)
       app.run(debug=False, port = 8889)
   ```

   ```js
   <!doctype html>
   <title>Flask 示例</title>
   
   <form method="POST">
       {# wtf必须开启CSRF保护，使用csrf_token()函数 #}
       {{ book_Form.csrf_token() }}
       {{ book_Form.book_Name.label }} : {{ book_Form.book_Name }} <br>
       {{ book_Form.author_Name.label }} : {{ book_Form.author_Name }} <br>
       {{ book_Form.submit }} <br>
   </form>
   
   {% for message in get_flashed_messages() %}
       {{ message }}
   {% endfor %}
   
   <ul>
       {% for author in Author_list %}
           <li>作者：{{ author['author'] }}，{{ author['count'] }} 本著作</li>
           <ul>
               {% for book in Book_list %}
                   {% if book['author'] == author['author'] %}
                       <li>{{ book['name'] }}</li>
                   {% endif %}
               {% endfor %}
           </ul>
       {% endfor %}
   </ul>
   ```

4. 插入数据

   ```python
   from flask import Flask, render_template, request, flash
   from flask_sqlalchemy import SQLAlchemy
   from flask_wtf import FlaskForm   #导入wtf表单类
   from wtforms import StringField, SubmitField   #导入表单所需字段
   from wtforms.validators import DataRequired  #导入表单验证器
   
   app = Flask(__name__)
   app.secret_key = 'The secret string for encryption'
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:will@127.0.0.1/SaiDB'
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   myDB = SQLAlchemy(app)
   
   #1. 定义表单类
   class Book_Form(FlaskForm):
       book_Name = StringField('书名', validators = [DataRequired()])
       author_Name = StringField('作者', validators = [DataRequired()])
       submit = SubmitField('提交')
   
   @app.route('/', methods = ['GET', 'POST'])
   def BooK_list_Index():
       book_Form = Book_Form()
       print(f'书名：{book_Form.book_Name.data}, 作者：{book_Form.author_Name.data}')
       
       if request.method == 'GET':
           author_list, book_list = QueryData()
       elif request.method == 'POST':
           if book_Form.validate_on_submit():
               msg = InsertData(book_Form)
               flash(msg)
               author_list, book_list = QueryData()
           else:
               flash(book_Form.errors)
       
       return render_template("MyTemplate.html", book_Form = book_Form, author_list = author_list, book_list = book_list)
   
   # 展示所有作者/图书信息
   def QueryData():
       try:
           sql = "SELECT author, COUNT(*) count FROM books GROUP BY author;"
           data = myDB.session.execute(sql)
           author_list = data.fetchall()
           sql = "SELECT author, name FROM books;"
           data = myDB.session.execute(sql)
           book_list = data.fetchall()
       except Exception as e:
           print('-'*30,'\n',e,'\n','-'*30)
       return author_list, book_list
   
   # 新增图书
   def InsertData(book_Form):
       try:
           sql = "Insert Into Books (name, author) Values ('%s','%s')" %(book_Form.book_Name.data, book_Form.author_Name.data)
           myDB.session.execute(sql)
           myDB.session.commit()
           msg = "修改成功"
       except Exception as e:
           print('-'*30,'\n',e,'\n','-'*30)
           myDB.session.rollback()
           msg = "修改失败"
       finally:
           return msg
   
   if __name__ == '__main__':
       # app.run(debug=True, port = 8889)
       app.run(debug=False, port = 8889)
   ```

   ```js
   # html文件与上面相同
   ```

5. 插入数据前进行查重

   ```python
   from flask import Flask, render_template, request, flash
   from flask_sqlalchemy import SQLAlchemy
   from flask_wtf import FlaskForm   #导入wtf表单类
   from wtforms import StringField, SubmitField   #导入表单所需字段
   from wtforms.validators import DataRequired  #导入表单验证器
   
   app = Flask(__name__)
   app.secret_key = 'The secret string for encryption'
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:will@127.0.0.1/SaiDB'
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   myDB = SQLAlchemy(app)
   
   #1. 定义表单类
   class Book_Form(FlaskForm):
       book_Name = StringField('书名', validators = [DataRequired()])
       author_Name = StringField('作者', validators = [DataRequired()])
       submit = SubmitField('提交')
   
   @app.route('/', methods = ['GET', 'POST'])
   def BooK_list_Index():
       book_Form = Book_Form()
       print(f'书名：{book_Form.book_Name.data}, 作者：{book_Form.author_Name.data}')
       
       if request.method == 'GET':
           author_list, book_list = QueryData()
       elif request.method == 'POST':
           if book_Form.validate_on_submit():
               msg = InsertData(book_Form)
               flash(msg)
               author_list, book_list = QueryData()
           else:
               flash(book_Form.errors)
       
       return render_template("MyTemplate.html", book_Form = book_Form, author_list = author_list, book_list = book_list)
   
   # 展示所有作者/图书信息
   def QueryData():
       try:
           sql = "SELECT author, COUNT(*) count FROM books GROUP BY author;"
           data = myDB.session.execute(sql)
           author_list = data.fetchall()
           sql = "SELECT author, name FROM books;"
           data = myDB.session.execute(sql)
           book_list = data.fetchall()
       except Exception as e:
           print('-'*30,'\n',e,'\n','-'*30)
       return author_list, book_list
   
   # 新增图书
   def InsertData(book_Form):
       try:
           sql = "SELECT * FROM books where name = '%s';" %(book_Form.book_Name.data)
           data = myDB.session.execute(sql)
           if data.rowcount > 0:   #库里已有这本书
               msg = "数据库已有 " + book_Form.book_Name.data + " 这本书"
           else:
               sql = "Insert Into Books (name, author) Values ('%s','%s')" %(book_Form.book_Name.data, book_Form.author_Name.data)
               myDB.session.execute(sql)
               myDB.session.commit()
               msg = "修改成功"
       except Exception as e:
           print('-'*30,'\n',e,'\n','-'*30)
           myDB.session.rollback()
           msg = "修改失败"
       finally:
           return msg
   
   if __name__ == '__main__':
       # app.run(debug=True, port = 8889)
       app.run(debug=False, port = 8889)
   ```

   ```js
   # html文件与上面相同
   ```

6. 重定向用法

   ```python
   from flask import Flask, render_template, redirect, url_for
   
   app = Flask(__name__)
   
   @app.route('/', methods = ['GET', 'POST'])
   @app.route('/<name>')
   def SaiIndex(name = None):
       return render_template('MyTemplate1.html', FEname = name)
   
   @app.route('/delete/<id>', methods = ['GET', 'POST'])
   def delete(id = None):
       return redirect(url_for('SaiIndex'))
   
   if __name__ == '__main__':
       app.run(debug=True, port = 8889)
       # app.run(debug=False, port = 8889)
   ```

   ```js
   <!doctype html>
   <title>单一变量</title>
   {% if name %}
       <h1>Hello {{ name }}!</h1>
   {% else %}
       <h1>Hello World!</h1>
   {% endif %}
   ```

   > * 引入重定向包：`from flask import redirect, url_for`
   > * 用法：`redirect(url_for('SaiIndex'))`，`url_for()`的参数是将要跳转到的函数名
   >
   > > 访问`http://127.0.0.1:8889/sai`，再访问`http://127.0.0.1:8889/delete/321`，会跳转到`http://127.0.0.1:8889`

7. 删除数据

   > * 点击发送待删数据的ID给**删除函数的路由**，路由接收ID，执行删除函数，最后路由重定向回首页

   ```python
   from flask import Flask, render_template, request, flash, redirect, url_for
   from flask_sqlalchemy import SQLAlchemy
   from flask_wtf import FlaskForm   #导入wtf表单类
   from wtforms import StringField, SubmitField   #导入表单所需字段
   from wtforms.validators import DataRequired  #导入表单验证器
   
   app = Flask(__name__)
   app.secret_key = 'The secret string for encryption'
   app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:will@127.0.0.1/SaiDB'
   app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
   myDB = SQLAlchemy(app)
   
   @app.route('/', methods = ['GET', 'POST'])
   def BooksIndex():
       if request.method == 'GET':
           author_list, book_list = QueryData()
       elif request.method == 'POST':
           if book_Form.validate_on_submit():
               msg = InsertData(book_Form)
               flash(msg)
               author_list, book_list = QueryData()
           else:
               flash(book_Form.errors)
       
       return render_template("MyTemplate.html", author_list = author_list, book_list = book_list)
   
   @app.route('/delete/<del_name>', methods = ['GET', 'POST'])
   def delete(del_name = None):
       try:
           sql = "SELECT * FROM books where name = '%s';" %(del_name)
           data = myDB.session.execute(sql)
           if data.rowcount == 0:   #库里没有这本书
               flash("数据库没有 " + del_name + " 这本书")
           else:
               sql = "DELETE FROM Books WHERE name = '%s'" %(del_name)
               myDB.session.execute(sql)
               myDB.session.commit()
               flash(del_name + " 已删除")
       except Exception as e:
           print('-'*30,'\n',e,'\n','-'*30)
           myDB.session.rollback()
           flash("无法删除 "+ del_name + "这本书")
       return redirect(url_for('BooksIndex'))
   
   # 展示所有作者/图书信息
   def QueryData():
       try:
           sql = "SELECT author, COUNT(*) count FROM books GROUP BY author;"
           data = myDB.session.execute(sql)
           author_list = data.fetchall()
           sql = "SELECT author, name FROM books;"
           data = myDB.session.execute(sql)
           book_list = data.fetchall()
       except Exception as e:
           print('-'*30,'\n',e,'\n','-'*30)
       return author_list, book_list
   
   if __name__ == '__main__':
       app.run(debug=True, port = 8889)
       # app.run(debug=False, port = 8889)
   ```

   ```js
   <!doctype html>
   <title>Flask 示例</title>
   
   {% for message in get_flashed_messages() %}
       {{ message }}
   {% endfor %}
   
   <ul>
       {% for author in author_list %}
           <li>作者：{{ author['author'] }}，{{ author['count'] }} 本著作</li>
           <ul>
               {% for book in book_list %}
                   {% if book['author'] == author['author'] %}
                       <li>{{ book['name'] }} - <a href="{{ url_for('delete', del_name = book['name']) }}">删除</a></li>
                   {% endif %}
               {% endfor %}
           </ul>
       {% endfor %}
   </ul>
   ```

   > 删除链接：`<a href="{{ url_for('delete', del_name = book['name']) }}">`
   >
   > * 用法：`url_for('跳转函数', 路由变量名 = book['name'])`

8. 修改数据

   ```python
   
   ```

   ```js
   
   ```

   



