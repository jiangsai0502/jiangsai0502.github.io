> 每个2秒对桌面程序截一次屏

```python
import Quartz, time, pyautogui, os, threading
from AppKit import NSWorkspace, NSScreen
import numpy as np
import Quartz.CoreGraphics as CG
from pynput import keyboard
import cv2 as cv


def find_app_window(app_name):
    """获取目标程序窗口的信息"""
    workspace = NSWorkspace.sharedWorkspace()
    active_apps = workspace.runningApplications()
    for app in active_apps:
        # 模糊查找运行中的所有应用名称，用于调试
        if "sub" in app.localizedName().lower():
            print(app.localizedName())
        if app.localizedName() == app_name:
            # 获取目标程序的进程ID
            app_pid = app.processIdentifier()
            # 获取所有窗口的信息
            window_info_list = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID)
            for window_info in window_info_list:
                # 如果窗口属于目标程序
                if window_info["kCGWindowOwnerPID"] == app_pid:
                    # 获取窗口的位置和大小
                    window = window_info["kCGWindowBounds"]
                    return (window["X"], window["Y"], window["Width"], window["Height"])


def capture_screen(x, y, width, height):
    """捕获屏幕上指定区域的图像"""
    region = CG.CGRectMake(x, y, width, height)
    image_ref = CG.CGWindowListCreateImage(region, CG.kCGWindowListOptionOnScreenOnly, CG.kCGNullWindowID, CG.kCGWindowImageDefault)
    width = CG.CGImageGetWidth(image_ref)
    height = CG.CGImageGetHeight(image_ref)
    bytes_per_row = CG.CGImageGetBytesPerRow(image_ref)
    pixel_data = CG.CGDataProviderCopyData(CG.CGImageGetDataProvider(image_ref))
    image = np.frombuffer(pixel_data, dtype=np.uint8).reshape((height, bytes_per_row // 4, 4))
    image = image[:, :width, :3]
    image = np.ascontiguousarray(image, dtype=np.uint8)
    return image


def save_screenshot(x, y, w, h, last_capture_time, frame_count, image_folder, interval):
    """每隔一定时间截取屏幕上的一帧并保存"""
    current_time = time.time()
    if current_time - last_capture_time >= interval:
        try:
            screenshot = capture_screen(x, y, w, h)
            frame_count += 1
            filename = os.path.join(image_folder, f"screenshot_{frame_count}.png")
            cv.imwrite(filename, screenshot)
            print(f"Screenshot saved: {filename}")
            last_capture_time = current_time
        except Exception as e:
            print(f"Error during screen capture: {e}")
    return frame_count, last_capture_time


def keyboard_listener():
    """用于键盘输入的线程"""

    def on_press(key):
        try:
            if key.char == "q":
                print("自动防故障触发，程序停止中……")
                return False  # 停止监听
        except AttributeError:
            pass  # 忽略非字符按键

    with keyboard.Listener(on_press=on_press) as listener:
        listener.join()


# 屏幕程序截帧
if __name__ == "__main__":
    app_name = "Google Chrome"
    # 获取目标程序的窗口信息
    window_info = find_app_window(app_name)
    print(f"{app_name} 的左上角坐标和宽高是: {window_info}")
    # 截图保存的路径
    image_folder = "/Users/jiangsai/Desktop/test"

    # 在单独的线程中启动键盘监听
    keyboard_listener_thread = threading.Thread(target=keyboard_listener)
    keyboard_listener_thread.start()

    # 检查是否找到App
    if not window_info:
        print(f"找不到App: {app_name}")
        exit()

    # 检查保存截屏的文件夹是否存在
    if not os.path.exists(image_folder):
        print(f"新建目录: {image_folder}")
        os.makedirs(image_folder)

    last_capture_time = time.time()  # 上一次截图的时间
    x, y, w, h = window_info
    frame_count = 0  # 截图的帧数
    interval = 2  # 每2秒截屏一次
    try:
        while keyboard_listener_thread.is_alive():
            # 截屏函数参数太长的变通方式
            save_screenshot_args = x, y, w, h, last_capture_time, frame_count, image_folder, interval
            frame_count, last_capture_time = save_screenshot(*save_screenshot_args)
    finally:
        keyboard_listener_thread.join()  # 结束键盘监听线程
        cv.destroyAllWindows()

```

