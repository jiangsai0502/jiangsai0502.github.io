### 安装 flask 环境

1. 查看虚拟环境   `conda info --envs`

2. 创建虚拟环境   `conda create -n flask_py3 python=3.8`

    > 虚拟环境位置：~/miniconda3/envs/flask_py3

3. 激活虚拟环境   `source activate flask_py3`

4. 安装flask   `pip install flask`

    > Flask被安装位置：~/miniconda3/envs/flask_py3/lib/python3.8/site-packages/
    >
    > 卸载flask`pip uninstall flask`

    * 安装 Flask-WTF 表单插件   `pip install Flask-WTF`
    * 安装 flask-sqlalchemy 数据库抽象插件   `pip install flask-sqlalchemy`
    * 安装 flask-mysqldb 数据库插件   `pip install pymysql`
    * 安装MySQL 数据库插件   `pip install cryptography`

5. 查看环境下所有包   `conda list`

6. 配置 VS Code 环境设置 

    ```bash
    $ which python
    /Users/sai/miniconda3/envs/flask_py3/bin/python
    ```

    ```bash
    setting.json : "python.pythonPath": "/Users/sai/miniconda3/envs/flask_py3/bin/python"
    ```

    > `/Users/sai/miniconda3/envs/flask_py3/bin/python`不能写成`~/miniconda3/envs/flask_py3/bin/python`

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

**切记！！！**: `app.run(debug=False)` 一定不能开启调试！否则无法命中断点

> 1. `lanuch.json`是`debug`相关的配置文件
> 2. "stopOnEntry": true 进入程序时立即暂停执行，相当于在程序的第一行放一个断点
>
> >```python
> >"configurations": [
> >    {
> >        "name": "Python: Current File (Integrated Terminal)",
> >        "type": "python",
> >        "request": "launch",
> >        "program": "${file}",
> >        "console": "integratedTerminal",
> >        "stopOnEntry": true,
> >    },
> >```
>
> 3. **切记！！！** ：Flask在启动时必须指定 `app.run(debug=False)`，一定不能开启调试！否则无法命中断点
>
> ```python
> if __name__ == '__main__':
>     app.run(debug = False)
> ```
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



### 一个最小的应用：返回网页

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
  def SaiIndex(name = None):
      return render_template('MyTemplate.html', name = name)
  
  if __name__ == '__main__':
      app.run(debug = True)
  ```

  ```javascript
  <!doctype html>
  <title>单一变量</title>
  {% if name %}
      <h1>Hello {{ name }}!</h1>
  {% else %}
      <h1>Hello World!</h1>
  {% endif %}
  ```

  > * {{ args }} 表示 HTML 的变量代码块
  >   * args 变量可以是任意类型，如{{ name }}，{{ student.age }}，{{ my_dict['key'] }}，{{ my_list[0] }}
  > * `name = name` ：等号前的name是前端html模板的变量，等号后的name是后端的变量

  > * 网址输入`http://127.0.0.1:5000/`，则展示`Hello World!`
  > * 网址输入`http://127.0.0.1:5000/sai`，则展示`Hello sai!`

* 变量代码块：多变量

  ```python
  from flask import Flask, render_template
  
  app = Flask(__name__)
  
  @app.route('/')
  def MoreArgs():
      web_name = '多变量'
      my_list = [1, 3, 5, 7, 9, 11, 13]
      my_dict = {'name':'sai','age':18}
  
      return render_template('MyTemplate.html', web_name = web_name, my_list = my_list, my_dict = my_dict)
    
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
  def MoreArgs():
      my_list = [1, 3, 5, 7, 9, 11, 13]
      my_dict = {'name':'sai','age':18}
      MovieList = [
      {'title': 'xxxxx', 'year': '1988'},
      {'title': 'yyyyy', 'year': '1989'}
      ]
      return render_template('MyTemplate.html', my_list = my_list, my_dict = my_dict, MovieList = MovieList)
    
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
  
  遍历 MovieList <br>
  {% for movie in MovieList %}
      {{ movie['title'] }} - {{ movie['year'] }} <br>
  {% endfor %}
  ```

* 3_Filter.html

```javascript
<!doctype html>
<title>Hello Filter</title>

百度的网址：{{BaiduUrl}} <br>
字符串大写：{{BaiduUrl | upper }} <br>
字符串反转：{{BaiduUrl | reverse | upper }} <br>
```

* 4_OriginalWebForm

```javascript
<!doctype html>
<form method="POST">
    <label>用户名：</label> <input type="text" name="username"></p>
    <label>密码：</label> <input type="password" name="password"></p>
    <label>确认密码：</label> <input type="password" name="password2"></p>
    <input type="submit" value="提交"><br>
</form>
```

* 5_FlashWebForm.html

```javascript
<!doctype html>
<form method="POST">
    <label>用户名：</label> <input type="text" name="username"></p>
    <label>密码：</label> <input type="password" name="password"></p>
    <label>确认密码：</label> <input type="password" name="password2"></p>
    <input type="submit" value="提交"><br>
    {% for message in get_flashed_messages() %}
        {{ message }}
    {% endfor %}
</form>
```

* 6_FlaskWTForm.html

```javascript
<!doctype html>
<form method="POST">
    {{ login_form_web.csrf_token() }}
    {{ login_form_web.username.label }}{{ login_form_web.username }} <br>
    {{ login_form_web.password.label }}{{ login_form_web.password }} <br>
    {{ login_form_web.password2.label }}{{ login_form_web.password2 }} <br>
    {{ login_form_web.submit }} <br>
    {% for message in get_flashed_messages() %}
        {{ message }}
    {% endfor %}
</form>
```

* app.py

```python
from flask import Flask
from flask import render_template
from flask import request
from flask import flash
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import EqualTo, DataRequired

app = Flask(__name__)

app.secret_key = 'The secret string for encryption'

@app.route('/f')
def Filter():
    BaiduUrl = 'https://www.baidu.com/'
    return render_template('3_Filter.html', BaiduUrl = BaiduUrl)

@app.route('/ot', methods = ['GET', 'POST'])
def OriginalWebForm():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        print(f'你输入的用户：{username}，密码：{password}，确认密码：{password2}')
        if not all([username, password, password2]):
            result = '参数不完整'
        elif password != password2:
            result = '两次输入的密码不同'
        else:
            result = 'POST 成功了, Yeah'
        return result
    return render_template('4_OriginalWebForm.html')

@app.route('/ft', methods = ['GET', 'POST'])
def FlashWebForm():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        password2 = request.form.get('password2')
        print(f'FlashWebForm 用户名：{username}，密码：{password}，确认密码：{password2}')
        if not all([username, password, password2]):
            flash('参数不完整')
        elif password != password2:
            flash('两次输入的密码不同')
        else:
            return 'FlashWebForm 成功了, Yeah'
    return render_template('5_FlashWebForm.html')

class LoginForm(FlaskForm):
    username = StringField('用户名', validators = [DataRequired()])
    password = PasswordField('密码', validators = [DataRequired()])
    password2 = PasswordField('确认密码', validators = [DataRequired(), EqualTo('password', '密码不一致')])
    submit = SubmitField('提交')

@app.route('/fwt', methods = ['GET', 'POST'])
def FlaskWTForm():
    login_form = LoginForm()
    print(f'FlaskWTForm 用户名：{login_form.username.data}, 密码：{login_form.password.data}, 确认密码：{login_form.password2.data}')
    print(f'FlaskWTForm 用户名：{login_form.data["username"]}, 密码：{login_form.data["password"]}, 确认密码：{login_form.data["password2"]}')
    if login_form.validate_on_submit():
        return 'FlaskWTForm 成功了, Yeah'
    else:
        flash(login_form.errors)
    return render_template('6_FlaskWTForm.html', login_form_web = login_form)

if __name__ == '__main__':
    app.run(debug = True)
```



> **3_Filter.html**
>
> ```javascript
> 百度的网址：{{BaiduUrl}} <br>
> 字符串大写：{{BaiduUrl | upper }} <br>
> 字符串反转：{{BaiduUrl | reverse | upper }} <br>
> ```
>
> 1. 过滤器格式：变量名 | 过滤器 {{ variable | filter_name(*args) }}
> 2. 过滤器的链式调用，即拼接多个过滤器 {{ variable | filter_name(*args) | filter_name(*args) }}

> **5_FlashWebForm.html**
>
> ```javascript
> {% for message in get_flashed_messages() %}
>     {{ message }}
> {% endfor %}
> ```
>
> 1. get_flashed_messages() 方法接受后端传来的 flash 消息

> **6_FlaskWTForm.html**
>
> ```javascript
> <!doctype html>
> <form method="POST">
>     {{ login_form_web.csrf_token() }}
>     {{ login_form_web.username.label }}{{ login_form_web.username }} <br>
>     {{ login_form_web.password.label }}{{ login_form_web.password }} <br>
>     {{ login_form_web.password2.label }}{{ login_form_web.password2 }} <br>
>     {{ login_form_web.submit }} <br>
>     {% for message in get_flashed_messages() %}
>         {{ message }}
>     {% endfor %}
> </form>
> ```
>
> 1. WTForms默认开启CSRF保护，所以必须有这段代码 <实例名>..csrf_token()

> ```python
> from flask import render_template
> 
> @app.route('/')
> @app.route('/<name>')
> def Index(name = None):
>  return render_template('1_Index.html', name = name)
> ```
> 1. 渲染模板需要导入 render_template
> 2. 对路径 '/' 的请求，将触发对 Index() 函数的调用
> 3. 对路径 '/\<name>' 的请求，将触发对 Index() 函数的调用，<name> 是任意 str
> 4. render_template('1_Index.html') 将渲染 templates 目录下的 1_Index.html 模板
> 5. 模板 1_Index.html 中的变量名和 app.py 中的变量保持一致，即 name = name

> ```python
> @app.route('/cb')
> def CodeBlock():
>     myList = [1, 3, 5, 7, 9, 11, 13]
>     return render_template('2_CodeBlock.html', myList = myList)
> ```
> 1. 对路径 '/cb' 的请求，将触发对 CodeBlock() 函数的调用

> ```python
> from flask import request
> 
> @app.route('/t', methods = ['GET', 'POST'])
> def OriginalWebForm():
>     if request.method == 'POST':
>         username = request.form.get('username')
>         password = request.form.get('password')
>         password2 = request.form.get('password2')
>         print(f'你输入的用户：{username}，密码：{password}，确认密码：{password2}')
>         if not all([username, password, password2]):
>             result = '参数不完整'
>         elif password != password2:
>             result = '两次输入的密码不同'
>         else:
>             result = 'POST 成功了, Yeah'
>         return result
>     return render_template('4_OriginalWebForm.html')
> ```
>
> 1. 获取前端的上传请求消息，需要导入 request 模块
> 2. 表单上传是 'POST' 方式
> 3. 路由通过 request.method 判断请求方式：'GET', 'POST' 。必须大写
> 4. 路由通过 request.form.get() 从前端获取请求的参数

> ```python
> from flask import flash
> 
> app.secret_key = 'The secret string for encryption'
> 
> @app.route('/ft', methods = ['GET', 'POST'])
> def FlashWebForm():
>     if request.method == 'POST':
>         username = request.form.get('username')
>         password = request.form.get('password')
>         password2 = request.form.get('password2')
>         print(f'你输入的用户：{username}，密码：{password}，确认密码：{password2}')
>         if not all([username, password, password2]):
>             flash('参数不完整')
>         elif password != password2:
>             flash('两次输入的密码不同')
>         else:
>             return 'POST 成功了, Yeah'
>     return render_template('5_FlashWebForm.html')
> ```
>
> 1. 从后端向前端传递消息，要导入 flash 模块
> 2. 通过 secret_key 给后端的消息加密

> ```python
> from flask_wtf import FlaskForm
> 
> from wtforms import StringField, PasswordField, SubmitField
> 
> from wtforms.validators import EqualTo, DataRequired
> 
> class LoginForm(FlaskForm):
>     username = StringField('用户名', validators = [Required()])
>     password = PasswordField('密码', validators = [Required()])
>     password2 = PasswordField('确认密码', validators = [Required(), EqualTo('password', '密码不一致')])
>     submit = SubmitField('提交')
> 
> @app.route('/fwt', methods = ['GET', 'POST'])
> def FlaskWTForm():
>     login_form = LoginForm()
>     print(f'FlaskWTForm 用户名：{login_form.username.data}, 密码：{login_form.password.data}, 确认密码：{login_form.password2.data}')
>     print(f'FlaskWTForm 用户名：{login_form.data["username"]}, 密码：{login_form.data["password"]}, 确认密码：{login_form.data["password2"]}')
>     if login_form.validate_on_submit():
>         return 'FlaskWTForm 成功了, Yeah'
>     else:
>         flash(login_form.errors)
>     return render_template('6_FlaskWTForm.html', login_form_web = login_form)
> ```
>
> 1. 使用 Flask-WTF 验证表单数据
>
> >1. 安装Flask-WTF： pip install Flask-WTF
> >2. StringField 文本字段
> >3. PasswordField 密码文本字段
> >4. SubmitField 表单提交按钮
> >5. EqualTo 验证函数，比较两个字段的值
> >6. DataRequired 验证函数，确保字段中有数据
>
> 2. 替代 request.method == 'POST' ，验证 FlaskForm 表单是否提交
>
> >1. 方法：validate_on_submit()
>
> 3. 获取 FlaskForm 属性值的两种方式
>
> >1. login_form.username.data
> >2. login_form.data["username"]



### 一个最小的应用：使用数据库

```python
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:will@127.0.0.1/sql_demo'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True
myDB = SQLAlchemy(app)

class Role(myDB.Model):
    __tablename__ = 'DB_Role'
    id = myDB.Column(myDB.Integer, primary_key=True)
    name = myDB.Column(myDB.String(64))
    users = myDB.relationship('User', backref='role')

    def __repr__(self):
        return f'{self.name}'

class User(myDB.Model):
    __tablename__ = 'DB_User'
    id = myDB.Column(myDB.Integer, primary_key=True)
    name = myDB.Column(myDB.String(64), unique=True, index=True)
    role_id = myDB.Column(myDB.Integer, myDB.ForeignKey('DB_Role.id'))

    def __repr__(self):
        return f'{self.name}'

if __name__ == '__main__':
    myDB.drop_all()
    myDB.create_all()

    # 增
    ro1 = Role(name='管理员')
    ro2 = Role(name='用户')
    myDB.session.add_all([ro1, ro2])
    myDB.session.commit()

    us1 = User(name='小李', role_id=ro1.id)
    us2 = User(name='小欣', role_id=ro2.id)
    us3 = User(name='小曲', role_id=ro1.id)
    myDB.session.add_all([us1, us2, us3])
    myDB.session.commit()

    userlist = myDB.session.query(User)
    for each_user in userlist:
        print(f'User id: {each_user.id} | User name: {each_user.name} | User role_id: {each_user.role_id} | User role: {each_user.role}')
    
    rolelist = myDB.session.query(Role)
    for each_role in rolelist:
        print(f'Role id: {each_role.id} | Role name: {each_role.name} | Role users: {each_role.users}')

    # 改
    us1.name = 'sai'
    us2.name = 'chao'
    myDB.session.commit()

    # 删
    myDB.session.delete(us1)
    myDB.session.commit()

    app.run(debug=False, port = 8888)
```

**剖析**

> 1. 首先安装 MySQL 数据库
>
> > 1. 详情查看 PythonEnvironment.md
>
> 2. 设置连接数据库的URL
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
> 3. 设置每次请求结束后会自动提交数据库的改动（为降低消耗资源，可设为False）
>
>    `app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True`
>
> 4. 通过类 SQLAlchemy 来连接数据库
>
>    `myDB = SQLAlchemy(app)`
>
> 5. 定义角色类 Role 都继承数据库模型 myDB.Model
>
>    > 1. 定义 Role 在数据库中的表名
>    >
>    >    `tablename__ = 'roles'`
>    >
>    > 2. 定义 id 为整数型，为主键
>    >
>    >    `id = myDB.Column(myDB.Integer, primary_key=True)`
>    >
>    > 3. 定义 name 为字符型，最大 64 个字符
>    >
>    >    `name = myDB.Column(myDB.String(64))`
>    >
>    > 4. 关于 relationship 的用法**（不懂，但是完全不影响，可以不使用）**
>    >
>    >    ```python
>    >    class Role(myDB.Model):
>    >        __tablename__ = 'DB_Role'
>    >        id = myDB.Column(myDB.Integer, primary_key=True)
>    >        name = myDB.Column(myDB.String(64))
>    >        users = myDB.relationship('User', backref='role')
>    >    
>    >        def __repr__(self):
>    >            return f'{self.name}'
>    >    
>    >    class User(myDB.Model):
>    >        __tablename__ = 'DB_User'
>    >        id = myDB.Column(myDB.Integer, primary_key=True)
>    >        name = myDB.Column(myDB.String(64), unique=True, index=True)
>    >        role_id = myDB.Column(myDB.Integer, myDB.ForeignKey('DB_Role.id'))
>    >    
>    >        def __repr__(self):
>    >            return f'{self.name}'
>    >    ```
>    >
>    >    > 1. 声明数据库 DB_Role 表的表名：`__tablename__ = 'DB_Role'`
>    >    >
>    >    > 2. 声明数据库 DB_Role 表的字段：id ,  name
>    >    >
>    >    > 3. id ,  name 是数据库 DB_Role 表的字段，而 user 不是字段，users 是为方便查询虚拟存在的。myDB.Column() **声明字段**，myDB.relationship() **声明关系**
>    >    >
>    >    >    ```python
>    >    >    id = myDB.Column()
>    >    >    name = myDB.Column()
>    >    >    users = myDB.relationship()
>    >    >    ```
>    >    >
>    >    > 4. 第一步，给 **Role 模型** 增加一个 users 属性，并与 **User 模型**建立关联
>    >    >
>    >    >    `users = myDB.relationship('User')`
>    >    >
>    >    > 5. 第二步，给 **User 模型** 增加一个 role 属性，并与 **Role 模型**建立关联
>    >    >
>    >    >    `users = myDB.relationship('User', backref='role')`
>    >    >
>    >    > 6. 声明了上面这一句代码，就相当于：给 **Role 模型** 增加一个 users 属性，同时给 **User 模型** 增加一个 role 属性。 **Role 模型** 中的一句代码给 **User 模型** 增加了一个属性，很神奇
>    >    >
>    >    > 7. 用法 
>    >    >
>    >    >    ```python
>    >    >    userlist = myDB.session.query(User)
>    >    >    for each_user in userlist:
>    >    >        print(f'User id: {each_user.id} | User name: {each_user.name} | User role_id: {each_user.role_id} | User role: {each_user.role}')
>    >    >    
>    >    >    rolelist = myDB.session.query(Role)
>    >    >    for each_role in rolelist:
>    >    >        print(f'Role id: {each_role.id} | Role name: {each_role.name} | Role users: {each_role.users}')
>    >    >    ```
>    >    >
>    >    >    > 1. User 模型的 each_user.role 取的是 `__repr__ `的值
>    >    >    > 2. Role 模型的 each_role.users 取的是 `__repr__ `的值
>
> 6. 定义用户类 User 继承数据库模型 myDB.Model
>
>    > 1. 定义 name 为字符型，值唯一unique，为本字段创建索引index
>    >
>    >    `name = myDB.Column(myDB.String(64), unique=True, index=True)`
>    >
>    > 2. 定义 role_id 为整数型，为主键，将 role_id 设为 roles 表中 id 字段的外键，即 外键主表是 roles 表，子表 users 表
>    >
>    >    `role_id = myDB.Column(myDB.Integer, myDB.ForeignKey('roles.id'))`
>    >
>    >    外键的作用
>    >
>    >    > 1. 完整性：即向子表 users 表插入数据时会检查 role_id 的值在主表 roles 表中是否存在，若不存在，则插入失败。
>    >    >
>    >    >    例如 roles 表有 '1', '2' 两个值，向子表 users 表插入数据 us3 = User(name = 'liuwei', role_id = 3)，则插入失败，因为 roles 表没有 '3' 这个值
>
> 7. 设置数据库
>
>    > 1. 进入数据库   `mysql -u root -p`
>    >
>    > 2. 创建数据库，并使用它
>    >
>    >    ```sql
>    >    create database sql_demo;
>    >    use sql_demo;
>    >    show tables;
>    >    ```
>
> 8. 在操作数据库
>
>    > 1. 删除所有表：`myDB.drop_all()` 
>    > 2. 创建所有表：`myDB.create_all()`
>    > 3. 加入 session ：`myDB.session.add_all([<实例1>, <实例2>])`
>    > 4. 提交 session ：`myDB.session.commit()`
>    > 5. 删除实例：`myDB.session.delete(<实例1>)`





