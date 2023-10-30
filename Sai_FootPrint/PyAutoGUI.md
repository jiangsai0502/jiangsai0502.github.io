#### PyAutoGUI

**安装**

`pip install pyautogui`

##### 等待页面加载出控件，再点击它

```python
import pyautogui
import time

# 目标图片
target_pic = "/Users/jiangsai/Desktop/1.png"
# 目标图片坐标
location = None
# 等待加载时间
second = 0

# 只要没找到图片，或者加载时间没超过10秒，就一直循环
while location == None and second != 10:
    try:
        time.sleep(0.5)
        second = second + 0.5
        location = pyautogui.locateOnScreen(target_pic)
    except Exception as e:
        print(e)

if location == None:
    print("不等了")
else:
    print(location)
    x, y = pyautogui.center(location)
    pyautogui.moveTo(x / 2, y / 2)
```

##### 按键精灵

> 1. Excel格式
>    
>    | 序号  | 操作指令 | 操作内容 | 重复次数（不填则执行1次） |
>    | --- | ---- | ---- | ------------- |
>    |     |      |      |               |
> 
> 2. 用法
>    
>    > 1. 操作指令：1-单击、2-双击、3-右键、4-输入、5-等待、6-滚轮
>    > 2. 操作内容：
>    >    1. 指令1、2、3对应的操作内容为png图片
>    >    2. 指令4对应的为输入文字
>    >    3. 指令5为等待
>    >    4. 指令6为滚动
> 
> ```
> #导入 用于自动化控制鼠标与键盘
> import pyautogui
> import time
> import xlrd
> from openpyxl import Workbook, load_workbook
> import pyperclip
> 
> # Excel数据检查
> def dataCheck(C_sheet):
>     # 默认Excel的数据全部有效
>     Validation = True
> 
>     #Excel行数检查
>     if C_sheet.max_row <2:
>         print("没数据")
>         Validation = False
>         return Validation
> 
>     #每行数据检查
>     current_line = 2
>     while current_line <= C_sheet.max_row:
>         # 第1列 操作类型
>         cmd_type = C_sheet[current_line][0]
>         # 判断第1列数据有效性
>         if cmd_type.value not in [1,2,3,4]:
>             print('第',current_line,"行,第1列当前是", cmd_type.value,"，必须是1-6的数字")
>             Validation = False
> 
>         # 第2列 内容检查
>         cmd_content = C_sheet[current_line][1]
>         # 判断第2列数据有效性
>         # 1、2、3是图片操作，操作内容必须为字符串类型
>         if cmd_type.value ==1 or cmd_type.value == 2 or cmd_type.value == 3:
>             if not cmd_content.value.lower().endswith('.png'):
>                 print('第',current_line,"行,第2列当前是", cmd_content.value,"，图片操作必须预备png图片")
>                 Validation = False
>         # 4是输入操作，输入内容不能为空
>         elif cmd_type.value == 4:
>             if cmd_content.value.strip() is None:
>                 print('第',current_line,"行,第2列当前是", cmd_content.value,"，输入操作必须设置输入内容")
>                 Validation = False
> 
>         # 第3列 重复次数检查
>         cmd_times = C_sheet[current_line][2]
>         # 判断第3列数据有效性
>         if cmd_times.value is not None:
>             if type(cmd_times.value) is not int:
>                 print('第',current_line,"行,第3列当前是", cmd_times.value,"，重复次数必须是整数")
>                 Validation = False
>             elif cmd_times.value < 1:
>                 print('第',current_line,"行,第2列当前是", cmd_times.value,"，重复次数必须>=1")
>                 Validation = False
>         current_line += 1
>     return Validation
> 
> #定义鼠标操作方法
> def mouseClick(clicks,mouse,image,reTry):
>     # 目标图片坐标
>     location = None
>     # 等待加载时间
>     second = 0
>     while reTry == 0:
>         # 只要没找到图片，或者加载时间没超过10秒，就一直循环
>         while (location == None and second != 10):
>             try:
>                 time.sleep(0.5)
>                 second = second + 0.5
>                 location = pyautogui.locateCenterOnScreen(image,confidence=0.9)
>             except Exception as e:
>                 print(e)
>         # 找到图，或者过了10秒没找到图
>         if location is None:
>             print('不等了')
>         else:
>             pyautogui.click(location.x/2,location.y/2,clicks=clicks,interval=0.2,duration=0.2,button=mouse)
>             print("点击1次")
>             reTry -= 1
> 
> #任务
> def mainWork(W_sheet):
>     current_line = 2
>     while current_line <= W_sheet.max_row:
>         #取本行第1列，操作类型
>         cmd_type = W_sheet[current_line][0]
>         # 图片操作
>         if cmd_type.value in [1,2,3]:
>             # 取本行第2列，操作内容
>             imageFile = W_sheet[current_line][1].value
>             # 默认重复执行1次
>             reTry = 1
>             # 若本行第3列不为空，则重新赋值重复次数
>             if W_sheet[current_line][2].value is not None:
>                 reTry = W_sheet[current_line][2].value
>             if cmd_type.value == 1:
>                 print("左键单击",imageFile,reTry,"次")
>                 mouseClick(1,"left",imageFile,reTry)
>             elif cmd_type.value == 2:
>                 print("左键双击",imageFile,reTry,"次")
>                 mouseClick(2,"left",imageFile,reTry)
>             elif cmd_type.value == 3:
>                 print("右键单击",imageFile,reTry,"次")
>                 mouseClick(1,"right",imageFile,reTry)
>         # 输入操作
>         elif cmd_type.value == 4:
>             pyautogui.click(x=1470,y=850,clicks=2)
>             inputValue = W_sheet[current_line][1].value
>             # 复制内容
>             pyperclip.copy(inputValue)
>             # 粘贴复制的内容
>             pyautogui.hotkey('command','v')
>             pyautogui.hotkey('enter')
>             time.sleep(0.5)
>             print("输入:",inputValue) 
>         current_line += 1
> 
> if __name__ == '__main__':
>     # 打开Excel文件
>     myWorkbook = load_workbook('test.xlsx')
>     # 引用指定表单Mysheet
>     Mysheet = myWorkbook['Sheet2']
> 
>     #数据检查
>     checkCmd = dataCheck(Mysheet)
>     if checkCmd:
>         mainWork(Mysheet)
>     else:
>         print('输入有误或者已经退出!')
> ```

##### 固定配置

> ```
> pyautogui.PAUSE = 0.1 # 调用在执行动作后暂停的秒数
> pyautogui.FAILSAFE = True # 启用自动防故障功能，鼠标移到屏幕左上角，利用failSafeException异常停止程序
> ```

##### 鼠标

> 1. 位置
>    
>    1. 当前位置
>       
>       ```
>       >>> pyautogui.position()   # 当前鼠标位置
>       Point(x=820, y=929)
>       >>> pyautogui.size()   # 当前屏幕分辨率
>       Size(width=1800, height=1169)
>       ```
>    
>    2. 移动位置
>       
>       ```
>       >>> pyautogui.moveTo(100, 200)   # 移动到(100, 200)
>       >>> pyautogui.move(0, 50)       # 从当前位置向下移动50像素
>       >>> pyautogui.move(-30, 0)      # 从当前位置向左移动30像素
>       ```
> 
> 2. 动作
>    
>    1. 点击
>       
>       ```
>       >>> pyautogui.click()  # 单击左键
>       >>> pyautogui.click(button='right')  # 单击右键
>       >>> pyautogui.click(clicks=2)  # 双击左键
>       >>> pyautogui.click(clicks=2, interval=0.25)  # 双击左键，两次单击间隔1/4秒
>       >>> pyautogui.click(x=100, y=200)  # 移动到(100, 200)，单击左键
>       >>> pyautogui.click(button='right', clicks=3, interval=0.25)  ## 三击右键，三次单击间隔1/4秒
>       ```
>    
>    2. 拖动
>       
>       ```
>       >>> pyautogui.dragTo(100, 200, button='left')     # 按住左键，拖到(100, 200)
>       >>> pyautogui.drag(30, 0, button='left')   # 按住左键，从当前位置，向右拖动30像素
>       ```
>    
>    3. 滚动
>       
>       ```
>       >>> pyautogui.scroll(10)   # 向上移动10格
>       >>> pyautogui.scroll(-10)  # 向下移动10格
>       >>> pyautogui.scroll(10, x=100, y=400)  # 移动到(100, 200)，向上移动10格
>       ```

##### 键盘

> 1. 输入字符串
>    
>    ```
>    >>> pyautogui.write('Hello world!')   # 在当前光标下输入'Hello world!'
>    >>> pyautogui.write('Hello world!', interval=0.25)  # 在当前光标下输入'Hello world!'，每个字符间隔1/4秒
>    ```
> 
> 2. 单个键
>    
>    ```
>    >>> pyautogui.press('enter')  # 按下 Enter 键然后释放它
>    >>> pyautogui.press('f1')     # 按下 F1 键然后释放它
>    >>> pyautogui.press('left')   # 按下 左箭头 然后释放它
>    ```
> 
> 3. 组合键
>    
>    ```
>    # 按住 Shift 键的同时按向左箭头键3次
>    >>> pyautogui.keyDown('shift')  # 按下 shift 键
>    >>> pyautogui.press(['left', 'left', 'left'] , interval=0.25)    # 按下 左箭头 然后释放它，重复3次，每次操作间隔1/4秒
>    >>> pyautogui.keyUp('shift')    # 释放 shift 键
>    ```
>    
>    ```
>    # 按住 Shift 键的同时按向左箭头键3次
>    >>> with pyautogui.hold('shift'):  # 按下 shift 键
>            pyautogui.press(['left', 'left', 'left'])    # 按下 左箭头 然后释放它，重复3次
>    ```
>    
>    ```
>    # 热键 ctrl+shift+esc
>    >>> pyautogui.hotkey('ctrl', 'shift', 'esc')
>    ```

##### 弹窗

> ```
> >>> alert(text='', title='', button='OK')    # 就一个“确定”按钮，返回按钮名称
> >>> confirm(text='', title='', buttons=['OK', 'Cancel'])    # “确定”和“取消”按钮，返回按钮名称
> >>> prompt(text='', title='' , default='')    # 有个可输入框、“确定”和“取消”按钮。确定返回输入的文本，取消返回“无”
> >>> password(text='', title='', default='', mask='*')    # 有个可输入框（输入时字符显示为*）、“确定”和“取消”按钮。确定返回输入的文本，取消返回“无”
> ```

##### 截图

> 1. 截图
>    
>    ```
>    >>> pyautogui.screenshot().save("my_shot.png")    # 全屏截图，并保存在当前目录的my_shot.png中
>    ```
> 
> 2. 定位截图
>    
>    ```
>    # 当前屏幕分辨率才1800x1169，截屏尺寸却是3600x2338，实际操作该图片要将取到的x、y坐标/2
>    >>> pyautogui.size()
>    Size(width=1800, height=1169)   # 当前屏幕分辨率才1800x1169
>    >>> pyautogui.screenshot().size
>    (3600, 2338)   # 截屏尺寸却是3600x2338
>    ```
>    
>    ```
>    # 以90%的精确度定位第一个图片calc.png的坐标，精确度默认为 1
>    >>> my_location = pyautogui.locateOnScreen('calc.png' , confidence=0.9)    
>    >>> my_location
>    Box(left=3412, top=467, width=104, height=86)    # （左、上、宽、高）
>    ```
>    
>    ```
>    # 点击图片的中心，这种方法点不中，因为原坐标放大了2倍，以原坐标找不到
>    >>> pyautogui.click('./calc.png') 
>    ```
>    
>    ```
>    # 定位第一个图片calc.png的中心坐标
>    >>> my_point1 = pyautogui.center(my_location)
>    >>> my_point1
>    Point(x=3464, y=511)    # 屏幕分辨率才1800x1169，这是Mac通病，解法是坐标/2
>       
>    >>> my_point2 = pyautogui.locateCenterOnScreen('calc.png')    # 该图片的中心坐标
>    >>> my_point2
>    Point(x=3464, y=511)   # x = left+width/2, y = top+height/2
>    >>> pyautogui.click(button7point.x/2, button7point.y/2)  # 点击图片的中心
>    ```
>    
>    ```
>    for my_location in pyautogui.locateAllOnScreen('calc.png'):
>        my_point = pyautogui.center(my_location)   # 定位每个calc.png
>        pyautogui.click(my_point[0]/2, my_point[1]/2)   # 点击每个calc.png中心
>    ```

坑

1. 调用`pyautogui.locateOnScreen(target_pic)`时，报错`TypeError: '<' not supported between instances of 'str' and 'int'`

   > 定位：pyautogui的bug
   >
   > 解决[参考](https://zhuanlan.zhihu.com/p/657907193)



