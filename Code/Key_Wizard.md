##### 按键精灵

> 1. Excel格式
>
>    | 操作指令 | 操作内容                                   | 重复次数（不填则执行1次） |
>    | -------- | ------------------------------------------ | ------------------------- |
>    | 1        | /Users/jiangsai/Desktop/test/a/1.png       | 可留空                    |
>    | 2        | /Users/jiangsai/Desktop/test/a/1.png       | 可留空                    |
>    | 3        | /Users/jiangsai/Desktop/test/a/1.png       | 可留空                    |
>    | 4        | 你好啊                                     | 可留空                    |
>    | 5        | /Users/jiangsai/Desktop/test/a/5.png       | 必须留空                  |
>    | 6        | 每次滚动颗粒数，正数向顶部滚，负数向底部滚 | 滚动次数                  |
>    | 7        | 留空                                       | 等待秒数                  |
>
> 2. 用法
>
>    ```bash
>    1：左键单击
>    2：左键双击
>    3：右键单击
>    4：键盘输入
>    5：鼠标悬浮
>    6：鼠标滚轮滚动
>    7：等待操作
>    ```

```python
import pyautogui  # 用于自动化控制鼠标和键盘
import time  # 用于处理时间相关操作，例如等待
import pyperclip  # 用于处理剪贴板（复制粘贴操作）
from openpyxl import load_workbook  # 用于处理Excel文件


# 从Excel文件中读取数据
def read_excel(sheet_name, file_name):
    """从Excel文件读取数据"""
    workbook = load_workbook(filename=file_name)  # 加载Excel文件
    sheet = workbook[sheet_name]  # 获取指定的sheet
    return sheet  # 返回sheet对象


# 验证Excel数据的有效性
def validate_data(sheet):
    """验证Excel数据的有效性"""
    for row in sheet.iter_rows(min_row=2, values_only=True):  # 遍历sheet的每一行
        cmd_type, cmd_content, cmd_times = row
        # 验证指令类型是否有效
        if cmd_type not in [1, 2, 3, 4, 5, 6, 7]:
            print(f"Invalid command type in row: {cmd_type}")
            return False

        # 验证图片文件是否有效（对于鼠标操作）
        if cmd_type in [1, 2, 3, 5] and (cmd_content is None or not cmd_content.lower().endswith(".png")):
            print(f"Invalid image file in row: {cmd_content}")
            return False

        # 验证键盘输入内容是否有效
        if cmd_type == 4 and (cmd_content is None or cmd_content.strip() == ""):
            print(f"Invalid input content in row: {cmd_content}")
            return False

        # 验证滚轮滚动量是否为整数
        if cmd_type == 6 and (cmd_times is None or not isinstance(cmd_times, int)):
            print(f"Invalid scroll amount in row: {cmd_times}")
            return False

        # 验证等待时间是否为整数
        if cmd_type == 7 and (cmd_times is None or not isinstance(cmd_times, int)):
            print(f"Invalid wait time in row: {cmd_times}")
            return False

    return True  # 如果所有验证都通过，则返回True


# 执行Excel中的命令
def execute_commands(sheet):
    """执行Excel中定义的命令"""
    for row in sheet.iter_rows(min_row=2, values_only=True):  # 遍历sheet的每一行
        cmd_type, cmd_content, cmd_times = row  # 获取行中的指令类型、内容和次数
        cmd_times = cmd_times or 1  # 如果未指定次数，则默认为1次

        # 执行鼠标相关操作
        if cmd_type in [1, 2, 3, 5, 6]:  # 假设5是鼠标悬浮，6是滚轮滚动
            for _ in range(cmd_times):  # 根据指定次数执行操作
                if cmd_type in [1, 2, 3]:
                    perform_mouse_click(cmd_type, cmd_content)  # 执行鼠标点击操作
                elif cmd_type == 5:
                    perform_mouse_hover(cmd_content)  # 执行鼠标悬浮操作
                elif cmd_type == 6:
                    perform_mouse_scroll(cmd_content)  # 执行鼠标滚轮滚动操作
        # 执行键盘输入操作
        elif cmd_type == 4:
            perform_keyboard_action(cmd_content)  # 执行键盘输入操作
        # 执行等待操作
        elif cmd_type == 7:  # 假设7是等待
            time.sleep(cmd_times)  # 根据指定时间等待


# 执行鼠标点击操作
def perform_mouse_click(cmd_type, image_file):
    """执行鼠标操作"""
    button = "left" if cmd_type in [1, 2] else "right"  # 确定鼠标按钮类型
    clicks = 1 if cmd_type in [1, 3] else 2  # 确定点击次数
    location = pyautogui.locateCenterOnScreen(image_file, confidence=0.9)  # 查找屏幕上的目标图片
    if location:
        pyautogui.click((location.x / 2, location.y / 2), clicks=clicks, button=button)  # 在找到的位置执行点击
        print(f"Performed {button} click on {image_file}")
    else:
        print(f"Image not found: {image_file}")  # 如果找不到图片，打印错误信息


# 执行鼠标悬浮操作
def perform_mouse_hover(image_file):
    """执行鼠标悬浮操作"""
    location = pyautogui.locateCenterOnScreen(image_file, confidence=0.9)  # 查找屏幕上的目标图片
    if location:
        pyautogui.moveTo((location.x / 2, location.y / 2))  # 移动鼠标到找到的位置
        print(f"Mouse hovered over {image_file}")
    else:
        print(f"Image not found for hovering: {image_file}")  # 如果找不到图片，打印错误信息


# 执行鼠标滚轮滚动操作
def perform_mouse_scroll(scroll_amount):
    """执行鼠标滚轮滚动操作"""
    pyautogui.scroll(scroll_amount)  # 滚动鼠标滚轮
    print(f"Scrolled mouse wheel by {scroll_amount}")


# 执行键盘输入操作
def perform_keyboard_action(text):
    """执行键盘输入操作"""
    pyperclip.copy(text)  # 复制文本到剪贴板
    time.sleep(0.2)
    # 模拟按下 command 键
    pyautogui.keyDown("command")
    # 按下 v 键粘贴
    pyautogui.press("v")
    # 松开 command 键
    pyautogui.keyUp("command")
    time.sleep(1)
    pyautogui.press("enter")  # 按下回车键
    print(f"Entered text: {text}")  # 打印输入的文本


if __name__ == "__main__":
    file_name = "/Users/jiangsai/Desktop/test/test.xlsx"  # 指定Excel文件路径
    sheet = read_excel("Sheet1", file_name)  # 读取Excel数据
    if validate_data(sheet):  # 验证数据有效性
        execute_commands(sheet)  # 执行命令
    else:
        print("Data validation failed.")  # 数据验证失败

```

