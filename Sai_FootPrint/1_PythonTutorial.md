# Python语法

### Python基础

#### !/usr/bin/python

```python
#!/usr/bin/python
print("Hello, World!")
```
> \#!/usr/bin/python 是告诉操作系统执行这个脚本时，调用 /usr/bin 下的 python 解释器，相当于写死了 python 路径。

#### 注释

```python
# 第一种注释方式 
'''
第二种注释方式
第二种注释方式
'''
```

#### 等待用户输入

```python
sentence = input("输入一句话：")
print("你输入的话是：",sentence)
```
运行结果
```python
输入一句话：i love the world
你输入的话是： i love the world
```

#### 测试程序清空shell

```python
import os
input("")
# 调用系统命令
os.system('pwd;clear')
```

#### 格式化字符串 f-string

f-string 格式化字符串以 f 开头，变量用大括号 {} 包起来，它会将变量或表达式计算后的值替换进去

```python
name = 'Runoob'
print(f'Hello {name}')
print(f'1 + 3 = {1+3}')
```
运行结果
```python
Hello Runoob
1 + 3 = 4
```

#### 运算符

| 运算符 | 描述 | 实例 |
| --- | --- | --- |
| / | 正常除法 | 5/3=1.667 |
| // | 取整 | 5//3=1 |
| % | 取余 | 5%3=2 |
| ** | 次幂 | 5**3=125 |
| x and y | 与运算 | (True and False)返回False |
| x or y | 或运算 | (True or False)返回True |
| not x | 非运算 | (not False)返回True |
| in | 包含关系 | ('a' in ('a','b'))返回True |
| not in | 包含关系 | ('a’ not in ('a','b'))返回False |
| is | 判断两个变量是否引用同一个对象 |  |
| is not | 判断两个变量是否引用同一个对象 |  |

#### end关键字

end实现不换行效果

```python
a, b = 0, 1
while b < 1000:
    print(b, end=',')
    a, b = b, a+b
```
运行结果
```python
1,1,2,3,5,8,13,21,34,55,89,144,233,377,610,987,
```

#### 标准数据类型

* 不可变类型：Number（int, float）、String（str）、Tuple（tuple）
* 可不类型：List（列表）、Set（set）、Dictionary（dict）

> 类型判断方法：type()，isinstance()
> string、list 和 tuple 都属于 sequence（序列），都可以遍历


#### String（字符串）

```python
str='12345abcde'

# 第1个参数 -1 表示倒数第1个字符
# 第2个参数为空，表示移动到列表末尾
# 第3个参数为步长，负号表示逆向
print("str[-1::-1] =",str[-1::-1])
print("str[-1::-2] =",str[-1::-2])
print("str[0] =",str[0])               # 输出第1个字符
print("str[5:] =",str[5:])              # 输出从第6个开始后的所有字符
print("str[:5] =",str[:5])              # 输出从第1个开始到第6个字符，不包含第6个
print("str[2:5] =",str[2:5])             # 输出从第3个开始到第6个的字符，不包含第6个
print("str[5:-2] =",str[5:-2])            # 输出从第6个到倒数第3个字符
```
运行结果
```python
str[-1::-1] = edcba54321
str[-1::-2] = eca42
str[0] = 1
str[-1] = e
str[5:] = abcde
str[:5] = 12345
str[2:5] = 345
str[5:-2] = abc
```

#### List（列表）
```python
TypeList = [2, 2.2, 'will', (1,'a','a'), [1,'a','a'], {1,'a','a'}, {'1st': 1,'2nd':'a', '3rd':'a'}]

print('TypeList[1:4]是：',TypeList[1:4])
for element in TypeList:
    print(str(element) + ' 的类型是：'+str(type(element))+' '+str(isinstance(element, type(element))))
```
运行结果
```python
TypeList[1:4]是： [2.2, 'will', (1, 'a', 'a')]
2 的类型是：<class 'int'> True
2.2 的类型是：<class 'float'> True
will 的类型是：<class 'str'> True
(1, 'a', 'a') 的类型是：<class 'tuple'> True
[1, 'a', 'a'] 的类型是：<class 'list'> True
{1, 'a'} 的类型是：<class 'set'> True
{'1st': 1, '2nd': 'a', '3rd': 'a'} 的类型是：<class 'dict'> True
```

#### Tuple（元组）

```python
TypeTuple = (2, 2.2, 'will', (1,'a','a'), [1,'a','a'], {1,'a','a'}, {'1st': 1,'2nd':'a', '3rd':'a'})

print('TypeTuple[1:4]是：',TypeTuple[1:4])
for element in TypeTuple:
    print(str(element) + ' 的类型是：'+str(type(element))+' '+str(isinstance(element, type(element))))
```
运行结果
```python
TypeTuple[1:4]是： (2.2, 'will', (1, 'a', 'a'))
2 的类型是：<class 'int'> True
2.2 的类型是：<class 'float'> True
will 的类型是：<class 'str'> True
(1, 'a', 'a') 的类型是：<class 'tuple'> True
[1, 'a', 'a'] 的类型是：<class 'list'> True
{1, 'a'} 的类型是：<class 'set'> True
{'1st': 1, '2nd': 'a', '3rd': 'a'} 的类型是：<class 'dict'> True
```

#### Set（集合）

> 1.会自动去重，不包含重复元素
> 2.作用：成员测试，去重复

```python
TypeSet = {'Tom', 'Tom', 'Jack', 'Rose'}

# 输出集合，去重复
print("{'Tom', 'Tom', 'Jack', 'Rose'}集合自动去重：",TypeSet)
 
# 成员测试
if 'Rose' in TypeSet :
    print('Rose 在集合中')
else :
    print('Rose 不在集合中')
 
# set可以进行集合运算
a = set('abracadabra')
b = set('alacazam')

print('a：',a)     # a 去重复
print('b：',b)     # b 去重复
print('a - b：',a - b)     # a 和 b 的差集
print('a | b：',a | b)     # a 和 b 的并集
print('a & b：',a & b)     # a 和 b 的交集
print('a ^ b：',a ^ b)     # a 和 b 中不同时存在的元素
```
运行结果
```python
{'Tom', 'Tom', 'Jack', 'Rose'}集合自动去重： {'Tom', 'Rose', 'Jack'}
Rose 在集合中
a： {'r', 'b', 'd', 'c', 'a'}
b： {'l', 'z', 'm', 'c', 'a'}
a - b： {'d', 'r', 'b'}
a | b： {'r', 'b', 'l', 'd', 'z', 'm', 'c', 'a'}
a & b： {'c', 'a'}
a ^ b： {'d', 'z', 'm', 'r', 'l', 'b'}
```
集合的基本操作

| TypeSet.add('Will') | 添加元素 |
| --- | --- |
| TypeSet.remove('Jack') | 删除元素 |
| len(TypeSet) | 计算元素个数 |
| TypeSet.clear() | 清空集合 |
| 'Will' in TypeSet | 判断存在 |


#### Dictionary（字典）

```python
TypeDic = {'1st': 1,'2nd':'a', '3rd':'a'}

print ("TypeDic['2nd']是：",TypeDic['2nd'])
print (TypeDic.keys())   # 输出所有键
print (TypeDic.values())   # 输出所有键

for DicKey,DicValue in TypeDic.items():
    print(DicKey,'的值是：',DicValue)
```
运行结果
```python
TypeDic['2nd']是： a
dict_keys(['1st', '2nd', '3rd'])
dict_values([1, 'a', 'a'])
1st 的值是： 1
2nd 的值是： a
3rd 的值是： a
```

#### 方法（字典）

* 不定长参数 *vartuple

```python
def printinfo( arg, *varTuple ):
   print ('参数 arg 是：', arg,'; 参数 varTuple 是：', varTuple)
   return
 
printinfo(10)
printinfo(70, 60, 50)
```
运行结果
```python
参数 arg 是： 10 ; 参数 varTuple 是： ()
参数 arg 是： 70 ; 参数 varTuple 是： (60, 50)
```

* 不定长参数 **varDict

```python
def printinfo( arg, **varDict ):
   print ('参数 arg 是：', arg,'; 参数 varDict 是：', varDict)
   return

printinfo(1)
printinfo(1, a=2,b=3)
```
运行结果
```python
参数 arg 是： 1 ; 参数 varDict 是： {}
参数 arg 是： 1 ; 参数 varDict 是： {'a': 2, 'b': 3}
```

* lambda 表达式

```python
Cac = lambda arg1, arg2: (arg1 + arg2)*2
 
print ("计算后的值: ", Cac( 10, 20 ))
print ("计算后的值: ", Cac( 20, 20 ))
```
运行结果
```python
计算后的值:  60
计算后的值:  80
```

* 列表推导式

```python
myList = [2, 4, 6]

print('[3*x for x in myList] 的结果是:', [3*x for x in myList])
print('[3*x for x in myList if x > 3] 的结果是:', [3*x for x in myList if x > 3])
print('[[x, x**2] for x in myList] 的结果是:', [[x, x**2] for x in myList])

yourList = [4, 3, -9]
print('[x+y for x in myList for y in yourList] 的结果是:',[x+y for x in myList for y in yourList])
print('[myList[i]*yourList[i] for i in range(len(myList))] 的结果是:',[myList[i]*yourList[i] for i in range(len(myList))])
```
运行结果
```python
[3*x for x in myList] 的结果是: [6, 12, 18]
[3*x for x in myList if x > 3] 的结果是: [12, 18]
[[x, x**2] for x in myList] 的结果是: [[2, 4], [4, 16], [6, 36]]
[x+y for x in myList for y in yourList] 的结果是: [6, 5, -7, 8, 7, -5, 10, 9, -3]
[myList[i]*yourList[i] for i in range(len(myList))] 的结果是: [8, 12, -54]
```

* 嵌套列表解析

```python
matrix = [
[1, 2, 3, 4],
[5, 6, 7, 8],
[9, 10, 11, 12],
]

print('矩阵转置后：',[[row[i] for row in matrix] for i in range(4)])
```
运行结果
```
矩阵转置后： [[1, 5, 9], [2, 6, 10], [3, 7, 11], [4, 8, 12]]
```

* del删除语句

```python
a = [-1, 1, 66.25, 333, 333, 1234.5]
del a[0]
print('del a[0]的结果：',a)
del a[2:4]
print('del a[2:4]的结果：',a)
del a[:]
print('del a[:]的结果：',a)
```
运行结果
```python
del a[0]的结果： [1, 66.25, 333, 333, 1234.5]
del a[2:4]的结果： [1, 66.25, 1234.5]
del a[:]的结果： []
```

* __name__属性

一个模块 myModule.py 被另一个模块 yourModule.py 第一次引入时，其主程序将运行。如果想在模块被引入时，模块中的某一程序块不执行，可以用__name__属性来使该程序块仅在该模块自身运行时执行
```python
# Filename: myModule.py

if __name__ == '__main__':
   print('程序自身在运行')
else:
   print('我来自另一模块')
```
运行结果
```python
# 直接运行 myModule.py 时
程序自身在运行
# 从另一个模块 yourModule.py 调用myModule.py 时
我来自另一模块
```

* dir() 方法

dir() 可以找到模块内定义的所有名称

```python
print(dir(list))
```
运行结果
```python
['__add__', '__class__', '__contains__', '__delattr__', '__delitem__', '__dir__', '__doc__', '__eq__', '__format__', '__ge__', '__getattribute__', '__getitem__', '__gt__', '__hash__', '__iadd__', '__imul__', '__init__', '__init_subclass__', '__iter__', '__le__', '__len__', '__lt__', '__mul__', '__ne__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__reversed__', '__rmul__', '__setattr__', '__setitem__', '__sizeof__', '__str__', '__subclasshook__', 'append', 'clear', 'copy', 'count', 'extend', 'index', 'insert', 'pop', 'remove', 'reverse', 'sort']
```

#### pickle 模块

```python
import pickle

# 使用pickle模块将数据对象保存到文件
OriginalData = {'a': [1, 2.0, 3, 4+6j],
         'b': ('string', u'Unicode string'),
         'c': None}

selfref_list = [1, 2, 3]
selfref_list.append(selfref_list)

with open('/Users/jiangsai02/Documents/Temp/myPickle.pkl', 'wb') as OpenPickle:
    pickle.dump(OriginalData, OpenPickle)
    pickle.dump(selfref_list, OpenPickle, -1)

with open('/Users/jiangsai02/Documents/Temp/myPickle.pkl', 'rb') as OpenPickle:
    GetData = pickle.load(OpenPickle)
    print(GetData)
```


#### 异常

```python
	 try    ├── 执行代码
	except  ├── 有异常时执行的代码
	 else   ├── 没有异常时执行的代码
	finally ├── 有没有异常都会执行的代码
```

```python
try:
    print('这是try里的代码')
except AssertionError as error:
    print('except AssertionError 的异常内容：',error)
else:
    try:
        with open('file.log') as file:
            read_data = file.read()
    except FileNotFoundError as fnf_error:
        print('except FileNotFoundError 的异常内容：',fnf_error)
finally:
    print('有没有异常都会执行的代码')
```
运行结果
```python
这是try里的代码
except FileNotFoundError 的异常内容： [Errno 2] No such file or directory: 'file.log'
有没有异常都会执行的代码
```

#### 强制抛异常
> 1. **raise**：有时为了满足需求，即便没有运行错误，也要人为抛出异常
> 2. raise之后的代码不会执行

```python
try:
    num = input("输入一个小于10的数：")
    if(not num.isdigit()):
        raise ValueError("num 必须是数字")
        print('raise 之后的代码不会执行')
    else:
        if(int(num) > 10):
            raise ValueError("num 必须小于10")
            print('raise 之后的代码不会执行')
except ValueError as e:
    print("引发异常：",repr(e))
```

#### 自定义的异常

> 1. 必须继承 Exception 

```python
class DemoException(Exception):

    def __init__(self, name, msg = '自定义的 Demo 异常'):
        self.__name = name
        self.__msg = msg

    def __str__(self):
        return (f'{self.__name} 异常的报警是 {self.__msg}')

try:
    raise DemoException('脚本错误')
except DemoException as e:
    print(e)
```




# Python面向对象

> 1.对象 = 静态属性 + 动态方法
> 2.Python 中的类名约定以大写字母开头

#### 最简单的类

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



### 多线程

1. 进程与线程
   * 一个进程至少有一个或多个线程
   * 一个进程内的所有线程共享这个进程内的所有信息
   * 一个信息一次只能被一个线程使用，用的时候会加 "互斥锁"，其他线程见到锁就会排队
   * 所有信息都被使用时，叫 "信号量"
2. 







