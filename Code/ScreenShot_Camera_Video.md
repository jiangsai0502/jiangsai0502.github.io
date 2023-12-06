##### 从视频中抽帧

> 本地视频：每个5帧截一帧

```python
import cv2 as cv
import os

def extract_frames(video_path, output_folder, frame_rate=1):
    """从视频中截取帧并保存"""
    video = cv.VideoCapture(video_path)
    count = 0
    num = 1
    success = True
    while success:
        success, frame = video.read()
        if not success:
            break
        if count % frame_rate == 0:
            frame_path = os.path.join(output_folder, f"frame_{num}.png")
            num += 1
            cv.imwrite(frame_path, frame)
        count += 1


if __name__ == "__main__":
    # 图像输出目录
    input_folder_img = "/Users/jiangsai/Desktop/new/1.original_pic"  # 待检测图片目录
    # 确保输出目录存在
    os.makedirs(input_folder_img, exist_ok=True)
    # 从视频中截取帧并保存
    video_path = "/Users/jiangsai/Desktop/box01.mp4"  # 视频文件路径
    extract_frames(video_path, input_folder_img, frame_rate=5)  # 每5帧保存一次
```

> 摄像头、本地视频：每个2秒截一帧

```bash
pip install pyobjc-framework-Quartz
pip install numpy
pip install opencv-python
pip install pynput
pip install pyautogui
```

```python
import Quartz, time, pyautogui, os, threading
from AppKit import NSWorkspace, NSScreen
import numpy as np
import Quartz.CoreGraphics as CG
from pynput import keyboard
import cv2 as cv


def capture_camera_or_video(cap, frame_interval, frame_count, capture_count, image_folder):
    """从摄像头或视频文件中捕获图像并保存"""
    ret, frame = cap.read()
    # 若视频结束，则退出循环
    if not ret:
        exit()
    # cv.imshow("camera", frame)  # 显示图像，不显示会极大的加快截帧速度
    # cv.waitKey(1)  # 配合cv.imshow使用，没有waitKey窗口会不显示
    frame_count += 1  # 帧计数加1

    # 检查是否达到指定帧间隔
    if frame_count % frame_interval == 0:
        filename = os.path.join(image_folder, f"screenshot_{capture_count}.png")
        cv.imwrite(filename, frame)
        capture_count += 1  # 帧计数加1
        print(f"Screenshot saved: {filename}")

    return frame_count, capture_count


# 本地视频 / 摄像头截帧
if __name__ == "__main__":
    # 视频源可以是摄像头（例如 0 代表默认摄像头）或视频文件路径
    # video_source = "/Users/jiangsai/Desktop/box.mp4"  # 或者 "path/to/video.mp4"
    video_source = 0
    # 截图保存的路径
    image_folder = "/Users/jiangsai/Desktop/smile"
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

    # 主程序参数
    last_capture_time = 0  # 上一次截图的时间
    frame_count = 0  # 当前帧数
    capture_count = 1  # 已截图数量
    frame_rate = int(cap.get(cv.CAP_PROP_FPS))  # 获取每秒视频帧数
    capture_second = 2  # 每隔2秒截取一帧
    frame_interval = capture_second * frame_rate

    while True:
        capture_camera_or_video_args = cap, frame_interval, frame_count, capture_count, image_folder
        frame_count, capture_count = capture_camera_or_video(*capture_camera_or_video_args)

    # 截屏函数参数太长的变通方式
    cap.release()
    cv.destroyAllWindows()
```

