###### 依赖库

```bash
pip install subprocess
pip install pyautogui
pip install pyperclip
pip install pillow
pip install pynput
pip install PyQt5
```

###### 调试

```python
import pyautogui, time
from Module import PyAutoGUI_modules as PAU

if __name__ == "__main__":
    # 调用在执行动作后暂停的秒数
    pyautogui.PAUSE = 0.1
    # 启用自动防故障功能，locateOnScreen()会使 FailSafe 检测失效
    # pyautogui.FAILSAFE = True

    pic = "/Users/jiangsai/Desktop/2.png"
    pic_location = PAU.Pic_Location(pic, confidence=0.7, max_times=5)
    if pic_location is not None:
        # 找到图像后执行的代码
        print(pic_location)
    else:
        # 找不到图像是执行的代码
        print("依然没找到啊啊啊啊啊啊")
        pass
```

#### 实战

* ###### 获取鼠标坐标

  >[pynput库keyboard函数获取键盘按键](#pynput库keyboard函数获取键盘按键)
  >
  >* 快捷键：`command + shift + option + control + 4`
  >* 终止程序：终端 `control + c`

  ```python
  import pyautogui
  from pynput import keyboard
  
  # 跟踪是否按下了所有需要的键：Command键按下时keyboard.Key.cmd为True，释放为False
  keys_pressed = {
      keyboard.Key.cmd: False,
      keyboard.Key.shift: False,
      keyboard.Key.alt: False,
      keyboard.Key.ctrl: False,
  }
  
  # 按键按下时执行
  def key_press(key):
      try:
          global keys_pressed
          # print(f"Key pressed: {key}")  # 输出当前按下的按键是啥
          # 1、判断
          if key in keys_pressed:
              keys_pressed[key] = True
          # all(list)：list中的所有value都为True时，返回True
          elif key == keyboard.KeyCode.from_char("4") and all(keys_pressed.values()):
              x, y = pyautogui.position()
              print(f"Mouse position: ({x}, {y})")
      except AttributeError:
          pass
  
  # 按键释放时执行
  def on_key_release(key):
      try:
          global keys_pressed
          # print(f"Key released: {key}")  # 输出当前释放的按键是啥
          if key in keys_pressed:
              keys_pressed[key] = False
      except AttributeError:
          pass
  
  # 启动键盘事件监听器
  with keyboard.Listener(on_press=key_press, on_release=on_key_release) as listener:
      listener.join()
  ```

* ###### 按照坐标：点击、输入

  > 需求：启动chrome浏览器，输入网址，输入搜索词，滚动查找搜索结果

  >获取App的完整调用路径
  >
  >1. 应用程序文件夹 - 程序右键 - 显示包内容 - `Contents` - `MacOS` - `Google Chrome`
  >2. 复制Google Chrome并粘贴到任意文本栏，即可得到 `/Applications/Google Chrome.app/Contents/MacOS/Google Chrome`

  ```python
  import subprocess, pyautogui, time, pyperclip
  
  # 启动 Chrome 浏览器
  ChromeApp = r"/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
  subprocess.Popen([ChromeApp])
  
  # 最大化浏览器窗口：
  pyautogui.hotkey("command", "ctrl", "f", interval=0.25)
  
  # 定位到地址栏，点击一下使光标定位在这里，然后输入网址，回车
  pyautogui.click(x=200, y=105)
  pyautogui.write("www.baidu.com")
  time.sleep(1)
  # 按两次回车键，防止输入法干扰
  pyautogui.press(["enter", "enter"], interval=0.25)
  
  # 定位到地址栏，点击一下使光标定位在这里，然后输入网址
  pyautogui.click(x=660, y=425)
  pyperclip.copy("今天天气")
  time.sleep(0.2)
  pyautogui.hotkey("command", "v")
  time.sleep(1)
  pyautogui.press(["enter", "enter"], interval=0.25)
  
  # 等待页面加载完成
  time.sleep(3)
  
  # 假设鼠标滚轮滚动50次为一屏
  per_screen = 50
  for i in range(5):
      pyautogui.scroll(-per_screen)
      time.sleep(1)
  ```

* ###### 按照图片：点击、输入

  >需求：与chrome插件交互，点击、输入、滚动

  ```python
  import subprocess, pyautogui, time, pyperclip
  
  def get_pic_location(pic):
      while True:
          try:
              location = pyautogui.locateOnScreen(pic, confidence=0.8)
              x, y = pyautogui.center(location)
              pic_location = {"x": x / 2, "y": y / 2}
              return pic_location
          except pyautogui.ImageNotFoundException:
              print("图像未找到")
  
  # 1、点击chrome插件：图像定位，移动鼠标，点击目标
  pic_location = get_pic_location("/Users/jiangsai/Desktop/Chrome_plugin.png")
  pyautogui.moveTo(pic_location["x"], pic_location["y"])
  pyautogui.click()
  time.sleep(3)
  
  # 2、输入插件密码：复制到剪切板，粘贴，回车
  pyperclip.copy("xxxx")
  time.sleep(0.2)
  pyautogui.hotkey("command", "v")
  time.sleep(1)
  pyautogui.press(["enter", "enter"], interval=0.25)
  time.sleep(3)
  
  # 3、移动光标到插件主体中心：向下，向左移动鼠标
  pyautogui.move(0, 500)  # 从当前位置向下移动50像素
  pyautogui.move(-200, 0)  # 从当前位置向左移动30像素
  time.sleep(1)
  
  # 4、向下滚动插件页面：假设鼠标滚轮滚动20次为一屏，共5屏
  per_screen = 20
  for i in range(5):
      pyautogui.scroll(-per_screen)
      time.sleep(1)
  ```

* 安全措施

  ```python
  # 调用在执行动作后暂停的秒数
  pyautogui.PAUSE = 0.1
  # 启用自动防故障功能，鼠标移到屏幕左上角，利用failSafeException异常停止程序
  pyautogui.FAILSAFE = True 
  ```

  * 手动定义的自动防故障功能

    > 鼠标移到屏幕左上角时触发防故障机制

    ```python
    import pyautogui, time
    from pynput import keyboard
    
    def check_failsafe():
        x, y = pyautogui.position()
        if x == 1799 and y == 0:
            raise pyautogui.FailSafeException
    
    def Do_Sth():
        check_failsafe()
        time.sleep(1)
        print("打印一下")
    
    try:
        while 1:
            Do_Sth()
    except pyautogui.FailSafeException:
        print("自动防故障触发，程序已停止。")
    ```

#### 语法

* 鼠标

  * 获取当前鼠标位置

    ```python
    pyautogui.position()  # Point(x=820, y=929)
    ```

  * 移动当前鼠标位置

    ```python
    pyautogui.moveTo(100, 200)  # 移动到(100, 200)
    pyautogui.move(0, 50)  # 从当前位置向下移动50像素
    pyautogui.move(-30, 0, duration=2)  # 从当前位置向左移动30像素，慢动作持续2秒 
    ```

  * 点击

    ```python
    pyautogui.click()  # 单击左键
    pyautogui.click(button='right')  # 单击右键
    pyautogui.click(clicks=2)  # 双击左键
    pyautogui.click(clicks=2, interval=0.2)  # 双击左键，间隔0.2秒
    pyautogui.click(button='right', clicks=3, interval=0.2)  # 三击右键，间隔0.2秒
    pyautogui.click(x=100, y=200)  # 移动到(100, 200)，单击左键

  * 拖动

    ```python
    pyautogui.dragTo(100, 200, button='left')  # 按住左键，拖到(100, 200)
    pyautogui.drag(30, 0, button='left')   # 按住左键，从当前位置，向右拖动30像素

  * 滚动

    ```python
    pyautogui.scroll(10)   # 向上移动10格
    pyautogui.scroll(-10)  # 向下移动10格
    pyautogui.scroll(10, x=100, y=400)  # 移动到(100, 200)，向上移动10格
    ```

    ```python
    # 假设鼠标滚轮滚动50次为一屏
    per_screen = 50
    for i in range(5):
        pyautogui.scroll(-per_screen)
        time.sleep(1)
    ```

* 键盘

  * 模拟字符串输入

    > `Pyautogui`：模拟按键来输入，无法输入中文，遇到不允许粘贴的场景如输入密码时可用
    > `Pyperclip`：模拟粘贴来输入，更强大，常用

    1. `Pyautogui`

       ```python
       pyautogui.write('Hello world!')  # 输入'Hello world!'
       pyautogui.write('Hello world!', interval=0.2)  # 输入时字符间隔0.2秒
       ```

    2. `Pyperclip`

       ```py
       import pyautogui, pyperclip, time
       pyperclip.copy("今天天气")  # 1、将文本复制到剪贴板
       time.sleep(0.2)  # 2、等待0.2秒让剪贴板命令完成
       pyautogui.hotkey('command', 'v')  # 3、使用热键粘贴文本
       ```

  * 模拟按键盘按键

    > [按键与键盘的对应关系](#按键与键盘的对应关系)

    1. 单个按键

       ```python
       pyautogui.press('enter')  # 按下 Enter 键然后释放它
       pyautogui.press('f1')     # 按下 F1 键然后释放它
       pyautogui.press('left')   # 按下 左箭头 然后释放它
       ```

    2. 组合键

       1. 多个单个按键组合

          案例1：`command + control + f`  将Chrome全屏

          ```python
          pyautogui.keyDown("command")  # 1、按下 command 键
          pyautogui.keyDown("ctrl")  # 2、按下 control 键
          pyautogui.press("f")  # 3、按下 f 键然后释放它
          time.sleep(0.2)  # 4、暂停0.2秒
          pyautogui.keyUp("ctrl")  # 5、释放 control 键
          pyautogui.keyUp("command")  # 5、释放 command 键
          ```

          案例2：按住 Shift 键的同时按3次左箭头

          ```python
          pyautogui.keyDown('shift')  # 1、按下 shift 键
          pyautogui.press(['left', 'left', 'left'] , interval=0.2)  # 2、按下 左箭头 然后释放它，重复3次，每次操作间隔0.2秒
          pyautogui.keyUp('shift')  # 3、释放 shift 键
          ```

       2. 组合键函数

          案例：`command + control + f`  将Chrome全屏

          ```python
          # 必须用interval=0.2，增加每个按键之间的时间间隔，确保系统有足够的时间识别这些按键
          pyautogui.hotkey("command", "ctrl", "f", interval=0.2)
          ```

* 弹窗

  ```python
  alert(text='', title='', button='OK')  # 就一个“确定”按钮，返回按钮名称
  confirm(text='', title='', buttons=['OK', 'Cancel'])  # “确定”、“取消”按钮，返回按钮名称
  prompt(text='', title='' , default='')  # 输入框、“确定”、“取消”按钮。确定返回输入的文本，取消返回“无”
  password(text='', title='', default='', mask='*')  # 有输入框（输入时字符显示为*）、“确定”和“取消”按钮。确定返回输入的文本，取消返回“无”

* 截图

  ```python
  # 当前屏幕分辨率 1800x1169
  pyautogui.size()
  ```

  * 全屏截图

    ```python
    pyautogui.screenshot().save("/Users/jiangsai/Desktop/my_shot.png")
    pyautogui.screenshot().size  # (3600, 2338)
    ```

    > 截屏尺寸是屏幕分辨率的2倍，Retina屏的特点，实际操作该图片要将取到的x坐标/2、y坐标/2

  * 局部截图

    ```python
    region = (0, 0, 500, 500)  # (x, y, width, height)
    pyautogui.screenshot(region=region).save("/Users/jiangsai/Desktop/my_shot.png")

* 定位

  * 定位区域

    * 全屏定位

      ```python
      # 定位第一个与calc.png相似度达到90%的图像，返回结果位置的（左、上、宽、高）
      my_location = pyautogui.locateOnScreen('calc.png' , confidence=0.9)
      # Box(left=3412, top=467, width=104, height=86)

    * 局部定位

      >Mac上很不好用，因为麦克电脑的分辨率是屏幕的2倍，计算容易出错

      ```python
      定位第一个与calc.png相似度达到90%的图像的坐标
      region = (0, 0, 500, 500)  # (left, top, width, height)
      my_location = pyautogui.locateOnScreen('calc.png' , confidence=0.9, region=region)

  * 定位方法

    * 定位**首个**符合条件的目标

      ```python
      # 全屏范围内，定位第一个与calc.png相似度达到90%的图像的中心点坐标（x, y）
      my_point = pyautogui.locateCenterOnScreen('calc.png')
      # 中心点Point(x, y)，x = left+width/2, y = top+height/2
      # 点击中心点坐标(x=3464, y=511)
      pyautogui.click(my_point.x/2, my_point.y/2)

    * 定位**全部**符合条件的目标

      ```python
      # 全屏范围内，定位所有与calc.png相似度达到100%的图像的坐标
      for my_location in pyautogui.locateAllOnScreen('calc.png'):
          # 获取每个符合条件的目标的中心的坐标：Point(x=3464, y=511)
          my_point = pyautogui.center(my_location)  
          # 点击中心点：中心点(x=3464, y=511)大于屏幕分辨率1800x1169，Mac通病，解法是坐标/2
          pyautogui.click(my_point[0]/2, my_point[1]/2)

坑

1. 调用`pyautogui.locateOnScreen(target_pic)`时，报错`TypeError: '<' not supported between instances of 'str' and 'int'`

   > 定位：pyautogui的bug
   >
   > 解决[参考](https://zhuanlan.zhihu.com/p/657907193)

----

#### 储备库

###### pynput库keyboard函数获取键盘按键 

###### [Back](#获取鼠标坐标)

```python
# 获取 F1 键
f1_key = keyboard.Key.f1
# 获取数字键 1
number_1_key = keyboard.KeyCode.from_char('1')
# 获取大写字母键 A
capital_a_key = keyboard.Key.A
# 获取小写字母键 b
small_b_key = keyboard.Key.b
# 获取 Backspace 键
backspace_key = keyboard.Key.backspace
# 获取 Delete 键
delete_key = keyboard.Key.delete
# 获取 Tab 键
tab_key = keyboard.Key.tab
# 获取 Escape 键
escape_key = keyboard.Key.esc
# 获取 End 键
end_key = keyboard.Key.end
# 获取 Enter 键
enter_key = keyboard.Key.enter
# 获取 Home 键
home_key = keyboard.Key.home
# 获取 Insert 键
insert_key = keyboard.Key.insert
# 获取 PageUp 键
page_up_key = keyboard.Key.page_up
# 获取 PageDown 键
page_down_key = keyboard.Key.page_down
# 获取方向键上
arrow_up_key = keyboard.Key.up
# 获取方向键下
arrow_down_key = keyboard.Key.down
# 获取方向键左
arrow_left_key = keyboard.Key.left
# 获取方向键右
arrow_right_key = keyboard.Key.right
```

* `command + 4` 监控鼠标位置

  ```python
  import pyautogui
  from pynput import keyboard
  
  # cmd_pressed在Command键按下时为True，释放为False
  cmd_pressed = False
  
  # 按键按下时执行
  def key_press(key):
      global cmd_pressed
      try:
          # print(f"Key pressed: {key}")  # 输出当前按下的按键是啥
          if key == keyboard.Key.cmd:
              cmd_pressed = True
          elif key == keyboard.KeyCode.from_char("4") and cmd_pressed:
              x, y = pyautogui.position()
              print(f"Mouse position: ({x}, {y})")
      except AttributeError:
          print("press函数出错了")
          pass
  
  # 按键释放时执行
  def key_release(key):
      global cmd_pressed
      try:
          # print(f"Key released: {key}")  # 输出当前释放的按键是啥
          if key == keyboard.Key.cmd:
              cmd_pressed = False
      except AttributeError:
          print("release函数出错了")
          pass
  
  # 启动键盘事件监听器，终端control + c终止程序
  with keyboard.Listener(on_press=key_press, on_release=key_release) as listener:
      listener.join()
  ```

###### 按键与键盘的对应关系

[参考](https://pyautogui.readthedocs.io/en/latest/keyboard.html)   [Back](#键盘)

| PyAutoGUI Key | Mac Keyboard Key   | Description                    |
| ------------- | ------------------ | ------------------------------ |
| 'command'     | Command (⌘)        | 命令键                         |
| 'shift'       | Shift (⇧)          | 上档键                         |
| 'ctrl'        | Control (⌃)        | 控制键                         |
| 'option'      | Option (⌥)         | 选项键                         |
| 'alt'         | Option (⌥)         | 选项键（通常等同于 Option）    |
| 'enter'       | Return/Enter       | 回车键                         |
| 'esc'         | Escape             | 退出键                         |
| 'space'       | Spacebar           | 空格键                         |
| 'delete'      | Forward Delete (⌦) | 向前删除键（删除光标后的字符） |
| 'pagedown'    | Page Down (⇟)      | 向下翻页键                     |
| 'pageup'      | Page Up (⇞)        | 向上翻页键                     |
| 'f1'-'f19'    | F1-F19             | 功能键                         |
| 'up'          | Up Arrow (↑)       | 向上箭头键                     |
| 'down'        | Down Arrow (↓)     | 向下箭头键                     |
| 'left'        | Left Arrow (←)     | 向左箭头键                     |
| 'right'       | Right Arrow (→)    | 向右箭头键                     |

##### 按键精灵

> 1. Excel格式
>
>    | 序号 | 操作指令 | 操作内容 | 重复次数（不填则执行1次） |
>    | ---- | -------- | -------- | ------------------------- |
>    |      |          |          |                           |
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
> ```python
> #导入 用于自动化控制鼠标与键盘
> import pyautogui, time, xlrd, pyperclip
> from openpyxl import Workbook, load_workbook
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

##### 
