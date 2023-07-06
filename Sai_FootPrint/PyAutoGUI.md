#### PyAutoGUI

##### 打地鼠

```
# conda info --envs   查看当前系统下的虚拟环境
# conda activate py3   激活虚拟环境py3
# pip3 install pyautogui 屏幕操作库
# pip3 install opencv-python 图像处理库

from numpy import where
import pyautogui

pyautogui.PAUSE = 0.1
pyautogui.FAILSAFE = True

while True:

coords = pyautogui. locateonscreen("E:/pydemo/ demo/ image/image if coords is not None:

print("找到了，进行点击"）
x,y = pyautogui.center(coords)
pyautogui. leftclick(x,y)
else:

print（"没找到"）



```

##### 等待页面加载出控件，再点击它

```
import pyautogui
import time

# 目标图片
imageFile = '11.png'
# 目标图片坐标
location = None
# 等待加载时间
second = 0

# 只要没找到图片，或者加载时间没超过10秒，就一直循环
while (location == None and second != 10):
    try:
        time.sleep(0.5)
        second = second + 0.5
        location = pyautogui.locateOnScreen(imageFile)
    except Exception as e:
        print(e)

if location == None:
    print('不等了')
else:
    print(location)
    x, y = pyautogui.center(location)
    pyautogui.moveTo(x/2,y/2)
```



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
>
> 

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
>    # 以90%的精确度定位第一个图片calc.png的坐标
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
>
> 3. 

