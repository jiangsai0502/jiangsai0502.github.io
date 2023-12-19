##### 常用方法

1. 查看一个变量的所有方法

   > ```python
   > name_list = ["Jessie", "Tom", "Crystal"]
   > 
   > for fun in dir(name_list):
   >     if "__" not in fun:
   >         print(fun)
   > ```
   >

1. 格式化输出：**f-string**

   > ```py
   > name = "testerzhang" 
   > print(f'Hello {name}')
   > ```

1. 变量名加冒号

   > ```python
   > user: User = xxxxx
   > ```
   >
   > 变量名：类型注解，3.6 引入的语法，为解释器指明变量类型，方便写代码时，点自动提示补齐

1. Python 中实现一些常用的命令行命令

   1. 获取当前目录位置（类似于 `pwd` ）

      ```
      pwd
      ```

      ```python
      import os
      print("当前目录位置：", os.getcwd())
      ```

   2. 打开目录（类似于 `open` ）

      ```bash
      open /Users/jiangsai/Downloads
      ```

      ```python
      import subprocess
      
      folder_path = '/Users/jiangsai/Downloads'
      subprocess.run(["open", folder_path])
      ```

   3. 列出目录内容（类似于 `ls` ）

      ```
      ls /Users/jiangsai
      ```

      ```python
      import os
      
      directory_path = "/Users/jiangsai"
      print(os.listdir(directory_path))
      ```

   4. 复制文件（类似于 `cp`）

      ```bash
      cp "/Users/jiangsai/source.txt" "/Users/jiangsai/Downloads/destination.txt"
      ```

      ```python
      import shutil
      
      source_file = "/Users/jiangsai/source.txt"
      destination_file = "/Users/jiangsai/Downloads/destination.txt"
      shutil.copyfile(source_file, destination_file)
      ```

   5. 移动或重命名文件（类似于 `mv`）

      ```bash
       mv "/Users/jiangsai/source.txt" "/Users/jiangsai/Downloads/destination.txt"
      ```

      ```python
      import shutil
      
      source_file = "/Users/jiangsai/source.txt"
      destination_file = "/Users/jiangsai/Downloads/destination.txt"
      shutil.move(source_file, destination_file)
      ```

   6. 删除文件（类似于 `rm`）

      ```bash
      rm "/Users/jiangsai/destination.txt"
      ```

      ```python
      import os
      
      delete_file = "/Users/jiangsai/Desktop/destination.txt"
      os.remove(delete_file)
      ```

   7. 创建目录（类似于 `mkdir`）

      ```bash
      mkdir /Users/jiangsai/Desktop/Becca
      ```

      ```python
      import os
      
      create_folder = "/Users/jiangsai/Desktop/Becca"
      os.mkdir(create_folder)
      ```

   8. 改变当前工作目录（类似于 `cd`）

      ```bash
      cd "/Users/jiangsai/Desktop/Becca"
      ```

      ```python
      import os
      
      create_folder = "/Users/jiangsai/Desktop/Becca"
      os.chdir(create_folder)
      print(f"当前工作目录已更改为：{os.getcwd()}")
      ```

   9. 执行下载命令

      ```bash
      yt-dlp --cookies-from-browser chrome  https://www.bilibili.com/video/BV1dP411f7kX
      ```

      ```python
      # 单纯执行
      import subprocess
      
      # 定义要执行的命令
      command = ["yt-dlp", "--cookies-from-browser", "chrome", "https://www.bilibili.com/video/BV1dP411f7kX"]
      
      # 使用subprocess.run()执行命令
      result = subprocess.run(command, capture_output=True, text=True)
      
      # 打印命令的标准输出和标准错误
      print(f"标准输出: {result.stdout}")
      print(f"标准错误: {result.stderr}")
      ```

      ```python
      # 观察执行过程
      import subprocess
      
      # 定义要执行的命令
      command = ["yt-dlp", "--cookies-from-browser", "chrome", "https://www.bilibili.com/video/BV1dP411f7kX"]
      
      # 使用subprocess.Popen()创建子进程来执行命令
      process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
      
      # 实时获取并打印命令的输出
      while True:
          output = process.stdout.readline()
          if output == "" and process.poll() is not None:
              break
          if output:
              print(output.strip())
      
      # 获取命令的返回代码
      return_code = process.poll()
      print(f"命令执行完毕，返回代码: {return_code}")
      ```

      

#### Python面向对象

> 1.对象 = 静态属性 + 动态方法
> 2.Python 中的类名约定以大写字母开头

##### 最简单的类

* 封装：类可以封装 **属性** 和 **方法**

```python
class Turtle():
    '''__doc__ 是类描述，写在第一行'''
    # 属性
    mouth = 'Turtle 的大嘴'
    
    # 方法
    def climb(self):
        print("Turtle 在向前爬......")

turtleA = Turtle()
turtleA.climb()
print(turtleA.mouth)
print(turtleA.__doc__)
```

* 继承：子类继承父类的所有属性和方法后，**增加**新的 **属性** 和 **方法**

```python
class GreenTurtle(Turtle):
    # 新增属性
    color = 'GreenTurtle 是绿色'
    
    # 新增方法
    def eat(self):
        print("GreenTurtle 在吃绿藻")

turtleB = GreenTurtle()
turtleB.climb()
print(GreenTurtle.mouth)
turtleB.eat()
print(GreenTurtle.color)
```

#### 属性名称的命名规则

> 1. \_name：没有任何约束，约定该属性只在类内部使用，虽然不建议但可以任性的在类外部用 <实例名>.\_name 的形式访问
> 2. name\_：没有任何约束，只是在 name 与保留字冲突时这么用，比如 BeautifulSoup 中访问 class 时，要用 class\_
> 3. \_\_name：有约束，双下划线会被解释器修改为\_<类名>.\_\_name
> 4. \_\_name\_\_：尽量不要用
> 5. \_：单独一个下划线，表示一个临时用一用，以后都不会被用到，非常无关紧要的变量，用完即扔，完全可以不关注

```Python
for _ in range(5):
    print('Hello, World.')
```

```Python
car = ('red', 'auto', 12, 3812.4)
color, _, _, mileage = car
print(color)
print(mileage)
```

#### 最小空类

> 1. 作用：通过动态增加属性，管理临时数据

```Python
class Tiny_Empty_Class:
    pass

t = Tiny_Empty_Class()
print(f'初始时 t.__dict__是 {t.__dict__}')
t.name = 'will'
t.age = 30
t.family = {'bro':'超','papa':'山'}
print(f'动态增加属性后 t.__dict__是 {t.__dict__}')
```

#### 实例方法

```python
class Student():

    def talk(self, *args):
        print(f'我是实例方法 args:{args}')

UX_Stu = Student()
UX_Stu.talk('MAP')
```

> 1.**实例方法** 第一个参数必须是 **self**  
> 2.**实例方法** 只有1种调用方式
>
> > 1.<实例名>.<类方法名>()

#### 类方法 @classmethod

```python
class Student():

    @classmethod
    def talk(cls, *args):
        print(f'我是类方法 args:{args}')

UX_Stu = Student()
UX_Stu.talk('MAP')
Student.talk('MAP')
```

> 1.**类方法** 第一个参数必须是 **cls** 
> 2.**类方法** 可以有2种调用方式
> > 1.<实例名>.<类方法名>()
> > 2.<类名>.<类方法名>()

#### 静态方法 @staticmethod

```python
class Student():

    @staticmethod
    def talk(*args):
        print(f'我是静态方法 args：{args}')

UX_Stu = Student()
UX_Stu.talk('MAP')
Student.talk('MAP')
```

> 1.**静态方法** 不需要 **self** 和 **cls**，随便用什么参数
> 2.**静态方法** 可以有2种调用方式
> > 1.<实例名>.<类方法名>()
> > 2.<类名>.<类方法名>()

#### \__init\__() 构造方法

> 1. init 前后各2个下划线
> 2. 类实例化时会自动调用 \__init\__()，

```python
class Turtle():
    
    # 方法
    def __init__(self, name):
        self.name = name

    def kick(self):
        print(f"Turtle {self.name} 被踢了...")

turtleA = Turtle('小黄')
turtleA.kick()
```

#### 私有属性和私有方法

> 1. **私有属性__private_attrs**：两个下划线开头，只能在类内部的方法中以self.__private_attrs方式使用，不能在类外部使用。
> 2. **私有方法__private_method**：两个下划线开头，只能在类内部以self.__private_methods方式调用，不能在类外部调用。

#### 多重继承

```python
class Name_Class:
    def __init__(self, name):
        self.__name = name
    def printName(self):
        return self.__name

class Nick_Class:
    def __init__(self, nick):
        self.__nick = nick
    def printName(self):
        return self.__nick + ' 同志'

class Name_Nick_Class(Name_Class, Nick_Class):
    def printName(self):
        print(f'{super().printName()} 你好')

class Nick_Name_Class(Nick_Class, Name_Class):
    def printName(self):
        print(f'{super().printName()} 你好')

p1 = Name_Nick_Class('Will')
p1.printName()

p2 = Nick_Name_Class('Sai')
p2.printName()
```
> 1. super() 按照深度优先，从左至右的方式寻找基类方法

#### 重载

```python
import time

class Fish:
    def myMethod(self):
        self.time = time.time()
        print (f'调用父类方法的时间 {self.time}')
 
class Shark(Fish):
    def myMethod(self):
        super().myMethod()
        print (f'调用子类方法的时间 {self.time}')

Baby_Shark = Shark()
Baby_Shark.myMethod()
```

> 1. super() 方法能调用父类的方法
> 2. 要使用父类的属性，必须调用super() 方法


#### 多态

```python
class Animal(object):
    def run(self):
        print('Animal is running...')

class Dog(Animal):
    def run(self):
        print('Dog is running fast...')

class Cat(Animal):
    def run(self):
        print('Cat is running softly...')

def run_twice(animal):
    animal.run()
    animal.run()

run_twice(Dog())
run_twice(Cat())
```

> 多态真正的威力：调用方只管调用，不管细节，如果我们要新增一个 Animal 的子类 Tortoise 时，只要确保正确重载 run() 方法，原来的代码不需要任何改动

```Python
class Tortoise(Animal):
    def run(self):
        print('Tortoise is running slowly...')

run_twice(Tortoise())
```

#### 从方法中返回方法

```python
def hi(name="will"):
    def greet():
        return "这是 greet() 方法"
 
    def welcome():
        return "这是 welcome() 方法"
 
    if name == "will":
        return greet
    else:
        return welcome
 
a = hi()
print('print a 打印的是:',a)
print('print a() 打印的是:',a())

b = hi(name = "sai")()
print('print b 打印的是:',b)
```
运行结果
```python
print a 打印的是: <function hi.<locals>.greet at 0x10f7acf28>
print a() 打印的是: 这是 greet() 方法
print b 打印的是: 这是 welcome() 方法
```
在 if/else 返回 greet 和 welcome，而不是 greet() 和 welcome()。是因为greet 和 welcome 有小括号时，函数就会执行；而没有小括号时，它可以被到处传递，并且可以赋值给别的变量而不去执行它。

当我们写下 a = hi()，由于 name 参数默认是 yasoob，那么函数 greet 将被返回。
当我们写下 b = hi(name = "ali")，那么函数 welcome 将被返回。
当我们写下 b = hi(name = "ali")()，那么函数 welcome() 将被返回。

#### 可变参数 *args

> 1. \*args：形参名前加一个*，参数被存放在元组 tuple 中

```python
def argsFunc(*args):
	print(my_args)
	
argsFunc(1, 2, 3, 4)
argsFunc()
```

#### 可变参数 **kwargs

> 1. \*\*kwargs：形参名前加两个*，参数被存放在字典 dictionary 中，调用方法需要采用 arg1 = value1, arg2 = value2 这样的形式

```python
def argsFunc(**kwargs):
	print(my_args)
	
argsFunc(x=1, y=2, z=3)
argsFunc()
```

#### attr三兄弟（hasattr、getattr、setatter）

* hasattr：判断是否包含属性
* getattr：获取属性值
* setatter：设置属性值

```python
class Turtle():

    color = 'black'
    
    def __init__(self, name):
        self.name = name

    def Turtle_info(self):
        print(f"Turtle 的名字是{self.name}, 颜色是{self.color}")

turtleA = Turtle('小黄')

print(hasattr(turtleA,'color'))
print(getattr(turtleA,'color'))
setattr(turtleA,'color','green')
print(getattr(turtleA,'color'))
```

#### property() 函数

> 1. property(get_attr, set_attr, del_attr, '属性描述')可以操作属性值
> 2. get_attr, set_attr, del_attr 最好符合这种格式，前半部分是 get, set, del 中间是一个下划线'_',后半部分的属性名
> 3. 若只有get_attr，则属性为只读，不能写不能删，若只有get_attr, set_attr，则属性为可读可写，不能删，等等

```python
class Student():

    def __init__(self, name):
        '''初始化方法'''
        self.__name = name
        self.__score = 0

    def __str__(self):
        return f'我的姓名是{self.__name}，分数是{self.__score}'

    def get_score(self):
        return self.__score

    def set_score(self, value):
        if not isinstance(value, int):
            raise ValueError('分数必须是整型')
        if value < 0 or value > 100:
            raise ValueError('分数区间必须是 0 ~ 100!')
        self.__score = value

    def del_score(self):
        print('删除了 score 属性')
        del self.__score

    score = property(get_score, set_score, del_score, "有关余额操作的属性")

will = Student("sai")
print(will)

will.score = 500
print(will.score)

print(Student.score.__dict__)

del will.score
print(will.score)
```

> 1. **对象**.score 会调用get_score方法
> 2. **对象**.score=值 会调用set_score方法
> 3. del **对象**.score 会调用del_score方法
> 4. **<类名>**.属性名.__doc__ 会打印'属性描述'
> 5. 由于 get_score() 方法中需要返回 score 属性，如果使用 self.score 的话，其本身又被调用 get_score()，这将进入无限死循环。为了避免这种情况的出现，程序中的 score 属性必须设置为私有属性，即使用 __score（前面有 2 个下划线）

#### @property 装饰器 替代 property() 函数

```python
class Student(object):

    def __init__(self, name):
        '''初始化方法'''
        self.__name = name
        self.__score = 0

    def __str__(self):
        return f'我的姓名是{self.__name}，分数是{self.__score}'
        
    @property
    def score(self):
        return self.__score

    @score.setter
    def score(self, value):
        if not isinstance(value, int):
            raise ValueError('分数必须是整型')
        if value < 0 or value > 100:
            raise ValueError('分数区间必须是 0 ~ 100!')
        self.__score = value

    @score.deleter
    def score(self):
        print('删除了 score 属性')
        del self.__score

will = Student("sai")
print(will)

will.score = 500
print(will.score)

print(Student.score.__dict__)

del will.score
print(will.score)
```

#### @classmethod 装饰器

```python
class Student():
    def eat(self, x):
        print(f"{x} 一个人吃饭 {self}")

    @classmethod
    def class_eat(cls, x):
        print(f"{x} 班级聚餐 {cls}")
   
a = Student()
a.eat('will')
a.class_eat('Map')
Student.class_eat('Map')
```

> 1. @classmethod 修饰类方法，一般用不到
> 2. 必须包含 cls 参数


#### @装饰器

**语法**

```python
def 装饰器名(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        return func(*args, **kwargs)
    return wrapper

def 装饰器(text):
    @functools.wraps(func)
    def decorator(func):
        def wrapper(*args, **kwargs):
            print(f'{text},{func.__name__}')
            return func(*args, **kwargs)
        return wrapper
    return decorator
```

> 1. 作用：扩展方法的功能
> 2. 场景：下面的备份代码，想在不修改原有代码的前提下，增加一个打印备份时间的功能
> 3. @functools.wraps(func) 能保留原函数的名称，不懂

示例 1
```python
import functools,datetime

def BackUpLog(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        CurrentTime = datetime.datetime.now().strftime("%Y.%m.%d %H:%M:%S")
        print(f'数据备份时间是 {CurrentTime}')
        return func(*args, **kwargs)
    return wrapper

@BackUpLog
def BackUp():
    print('备份已完成')

BackUp()
```

> 分析：装饰器BackUpLog 的作用是，把在BackUp() 方法**前面**插入一些新的代码
> @BackUpLog 就是下面代码的简写
```python
BackUp = BackUpLog(BackUp)
```

示例 2
```python
import functools,time,random

def TimeCost(func):
    @functools.wraps(func)
    def wraper(*args, **kwargs):
        before = time.time()
        result = func(*args, **kwargs)
        after = time.time()
        print(f"BackUp()方法耗时: {after-before}")
        return result
    return wraper

@TimeCost
def BackUp():
    time.sleep(random.random())
    print('备份已完成')
    
BackUp()
```

> 分析：装饰器TimeCost 的作用是，把在BackUp() 方法**前后**插入一些新的代码
> @TimeCost 就是下面代码的简写
```python
BackUp = TimeCost(BackUp)
```

示例 3
```python
import functools

def bread(func):
    @functools.wraps(func)
    def wrapper():
        print("</''''''\>")
        func()
        print("<\______/>")
    return wrapper

def ingredients(func):
    @functools.wraps(func)
    def wrapper():
        print("#tomatoes#")
        func()
        print("~  salad  ~")
    return wrapper

@bread
@ingredients
def sandwich(food="--Hamburg--"):
    print(food)

sandwich()
```
运行结果
```python
</''''''\>
#tomatoes#
--Hamburg--
~  salad  ~
<\______/>
```

#### 小模块：打印实例及其类的所有属性`__dict__`

```python
class Print_AttrValues_Instance_Class():

    '''打印实例及其类的所有属性和属性值'''

    def Get_Key_Value_Instance(self,instance):
        print(f'\n{"*"*10}实例的__dict__{"*"*10}')
        
        for each_key,each_value in instance.__dict__.items():
            print(each_key,'：',each_value)
        
        print(f'\n{"*"*35}')

    def Get_Key_Value_Class(self,instance):
        print(f'\n{"*"*10}类的__dict__{"*"*10}')
        
        for each_key,each_value in type(instance).__dict__.items():
            print(each_key,'：',each_value)
        
        print(f'\n{"*"*35}')

    def Get_Key_Value_Instance_Class(self,instance):
        self.Get_Key_Value_Instance(instance)
        self.Get_Key_Value_Class(instance)

class Student():

    def eat(self, x):
        print(f"{x} 一个人吃饭 {self}")
   
will = Student()
will.talk = 'Hi BaiDu'
printValues = Print_AttrValues_Instance_Class()
printValues.Get_Key_Value_Instance_Class(will)
```







