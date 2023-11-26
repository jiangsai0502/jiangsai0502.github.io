import sys, subprocess, pyautogui, time, pyperclip
from pynput import keyboard
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QVBoxLayout, QPushButton
from PyQt5.QtGui import QPixmap


def show_image_popup(image_path):
    """
    在弹窗中展示一个图片，“继续”则执行后续程序，“终止”则终止后续程序
    """
    app = QApplication(sys.argv)
    window = QWidget()
    window.setWindowTitle("没找到图片，继续执行程序么？")

    layout = QVBoxLayout(window)

    image = QPixmap(image_path)
    label = QLabel()
    label.setPixmap(image)
    layout.addWidget(label)

    confirm_button = QPushButton("继续")
    cancel_button = QPushButton("终止")

    confirm_button.clicked.connect(window.close)
    cancel_button.clicked.connect(sys.exit)

    layout.addWidget(confirm_button)
    layout.addWidget(cancel_button)

    window.setLayout(layout)
    window.show()
    app.exec_()


def Pic_Location(pic, confidence=0.8, max_times=10):
    """
    pic：要定位的图片完整路径
    confidence：识别准确度，默认为80%
    max_times：最大重复次数，默认为10次
    定位到就返回图片(x, y)坐标；定位不到就返回None
    """
    while max_times > 0:
        try:
            location = pyautogui.locateOnScreen(pic, confidence=confidence)
            if location:
                x, y = pyautogui.center(location)
                pic_location = {"x": x / 2, "y": y / 2}
                return pic_location
            else:
                print("定位不到图像")
        except pyautogui.ImageNotFoundException:
            print("定位图像异常")
        max_times -= 1
    print("达到最大尝试次数，退出循环")
    # 弹出定位失败的图片
    show_image_popup(pic)
    return None


def Click_Pic(pic, confidence, max_times):
    """
    pic：要定位的图片完整路径
    confidence：识别准确度，默认为80%
    max_times：最大重复次数，默认为10次
    定位到就单击一次；定位不到就返回None
    """
    if pic_location is not None:
        pic_location = get_pic_location(pic)
        pyautogui.moveTo(pic_location["x"], pic_location["y"])
        pyautogui.click()
        time.sleep(1)
    else:
        return None


def Type_text(text):
    """
    粘贴文本到当前光标位置
    """
    pyperclip.copy(text)
    time.sleep(0.2)
    pyautogui.hotkey("command", "v")
    time.sleep(1)


def Scroll_Page(Pages, per_screen=50):
    """
    per_screen：默认鼠标滚轮滚动50次为1屏
    Pages：滚动屏数
    """
    for i in range(Pages):
        pyautogui.scroll(-per_screen)
        time.sleep(1)


def Anti_Fault():
    """
    防故障措施：鼠标移到左上角时，程序终止
    """
    try:
        while True:
            x, y = pyautogui.position()
            if x == 0 and y == 0:
                raise pyautogui.FailSafeException
            time.sleep(0.5)
    except pyautogui.FailSafeException:
        pyautogui.alert("触发防故障措施，程序已停止")
