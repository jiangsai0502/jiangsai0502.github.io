#### pynput

* **常用按键**

  1. 特殊按键 (`Key`)：
     - `Key.esc`：`Escape键`
     - `Key.space`：`空格键`
     - `Key.enter`：`回车键`
     - `Key.tab`：`Tab键`
     - `Key.shift`, `Key.shift_r`, `Key.shift_l`：`Shift键（右、左）`
     - `Key.ctrl`, `Key.ctrl_r`, `Key.ctrl_l`：`Control键（右、左）`
     - `Key.alt`, `Key.alt_r`, `Key.alt_l`：`Alt键（右、左）`
     - `Key.cmd`： `Command键`
  2. 普通按键 (`KeyCode`)：
     - 使用`KeyCode.from_char('a')`来表示字母键，例如`'a'`
     - 使用`KeyCode.from_char('1')`来表示数字键，例如`'1'`

* **使用方式**

  * 监听键盘和鼠标的输入

    ```python
    from pynput import keyboard
    
    # 按键按下时的处理函数
    def on_press(key):
        if key == keyboard.Key.esc:
            # 按下了Escape键时执行的代码
            return False
        elif key == keyboard.KeyCode.from_char('a'):
            # 按下了字母键'a'时执行的代码
            pass
        # 其他按键处理...
    
    # 按键释放时的处理函数
    def on_release(key):
        if key == Key.esc:
            # 按下ESC键时退出监听
            return False
          
    # 监听会一直停留在后台，直到手动终止
    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()
    ```

  * 模拟键盘和鼠标的输入

    ```python
    # 模拟按下Command+A组合键
    keyboard_controller.press(Key.cmd)
    keyboard_controller.press("a")
    keyboard_controller.release("a")
    keyboard_controller.release(Key.cmd)
    ```


* 案例

  * 自定义全选快捷键 `command + 9`

    ```python
    from pynput import keyboard
    from pynput.keyboard import Key, Controller
    
    # 创建一个键盘控制器对象
    keyboard_controller = Controller()
    
    # cmd_pressed在Command键按下时为True，释放为False
    cmd_pressed = False
    
    def on_press(key):
        global cmd_pressed
        try:
            # 当按下的按钮是command时
            if key == Key.cmd:
                cmd_pressed = True
            elif key.char == "9" and cmd_pressed:
                # 模拟按下Command+A组合键
                keyboard_controller.press(Key.cmd)
                keyboard_controller.press("a")
                keyboard_controller.release("a")
                keyboard_controller.release(Key.cmd)
        except AttributeError:
            print("press函数出错了")
            pass
    
    # 按键释放时的处理函数
    def on_release(key):
        if key == Key.esc:
            # 按下ESC键时退出监听
            return False
    
    # 设置监听器监听按键事件
    with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()
    ```

    



