> 每个2秒对摄像头、本地视频截一次屏

```python
import Quartz, time, pyautogui, os, threading
from AppKit import NSWorkspace, NSScreen
import numpy as np
import Quartz.CoreGraphics as CG
from pynput import keyboard
import cv2 as cv

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

def capture_camera_or_video(cap, interval, last_capture_time, frame_count, image_folder):
    """从摄像头或视频文件中捕获图像并保存"""
    ret, frame = cap.read()
    # 若视频结束，则退出循环
    if not ret:
        exit()
    cv.imshow("carmera", frame)
    current_time = time.time()
    if current_time - last_capture_time > interval:
        frame_count += 1
        filename = os.path.join(image_folder, f"screenshot_{frame_count}.png")
        cv.imwrite(filename, frame)
        print(f"Screenshot saved: {filename}")
        last_capture_time = current_time
    return frame_count, last_capture_time

# 本地视频 / 摄像头截帧
if __name__ == "__main__":
    # 视频源可以是摄像头（例如 0 代表默认摄像头）或视频文件路径
    video_source = 0  # 或者 "path/to/video.mp4"
    # 截图保存的路径
    image_folder = "/Users/jiangsai/Desktop/test"
    # 获取视频源
    cap = cv.VideoCapture(video_source)
    # 检查是否打开视频源
    if not cap.isOpened():
        print(f"无法打开视频源: {video_source}")
        exit()
    # 检查保存截屏的文件夹是否存在
    if not os.path.exists(image_folder):
        print(f"新建目录: {image_folder}")
        os.makedirs(image_folder)
    # 在单独的线程中启动键盘监听
    keyboard_listener_thread = threading.Thread(target=keyboard_listener)
    keyboard_listener_thread.start()
    
    # 主程序参数
    last_capture_time = 0  # 上一次截图的时间
    frame_count = 0  # 截图的帧数
    interval = 2  # 每2秒截屏一次
    try:
        while keyboard_listener_thread.is_alive():
            # 截屏函数参数太长的变通方式
            capture_camera_or_video_args = cap, interval, last_capture_time, frame_count, image_folder
            frame_count, last_capture_time = capture_camera_or_video(*capture_camera_or_video_args)
    finally:
        keyboard_listener_thread.join()  # 结束键盘监听线程
        cap.release()
        cv.destroyAllWindows()
```

