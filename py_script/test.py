import cv2 as cv
import numpy as np


def initialize_capture():
    """初始化视频捕捉."""
    # 1、获取视频源
    #   1.1、摄像头，0获取系统默认摄像头，1,2……可替换更多摄像头
    cap_video = cv.VideoCapture(0, cv.CAP_DSHOW)
    #   1.2、打开摄像头
    cap_video.open(0)
    # 1、获取视频文件
    # cap_video = cv.VideoCapture("/Users/jiangsai/Desktop/test/jump boy.mp4")

    # 检查视频源是否成功打开
    if not cap_video.isOpened():
        print("视频打开失败")
        exit(0)

    # 打印视频的宽度和高度信息
    print(f"视频宽度：{cap_video.get(3)} 视频高度：{cap_video.get(4)}")
    return cap_video


def initialize_detectors():
    """初始化检测器."""
    # 加载人脸检测的Haar级联分类器
    face_detector = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_alt2.xml")
    # 加载眼睛检测的Haar级联分类器
    eye_detector = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_eye.xml")
    # 加载微笑检测的Haar级联分类器
    smile_detector = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_smile.xml")
    return face_detector, eye_detector, smile_detector


def detect_face_eye_smile(pic, face_detector, eye_detector, smile_detector):
    """检测人脸、眼睛和微笑."""
    # 将图片转换为灰度图，因为Haar分类器需要灰度图像
    gray_pic = cv.cvtColor(pic, cv.COLOR_BGR2GRAY)
    # 使用人脸检测器在灰度图像中检测人脸
    faces = face_detector.detectMultiScale(gray_pic, 1.3, 2)

    # 遍历检测到的每个人脸
    for x, y, w, h in faces:
        # 在原图上绘制人脸矩形框
        cv.rectangle(pic, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
        # 提取人脸区域
        face_area = pic[y : y + h, x : x + w]

        # 在人脸区域内使用眼睛检测器检测眼睛
        eyes = eye_detector.detectMultiScale(face_area, 1.3, 10)
        for ex, ey, ew, eh in eyes:
            # 在人脸区域上绘制眼睛矩形框
            cv.rectangle(face_area, (ex, ey), (ex + ew, ey + eh), color=(0, 255, 0), thickness=2)

        # 在人脸区域内使用微笑检测器检测微笑
        smiles = smile_detector.detectMultiScale(face_area, scaleFactor=1.16, minNeighbors=65, minSize=(25, 25), flags=cv.CASCADE_SCALE_IMAGE)
        for sx, sy, sw, sh in smiles:
            # 在人脸区域上绘制微笑矩形框
            cv.rectangle(face_area, (sx, sy), (sx + sw, sy + sh), color=(255, 0, 0), thickness=2)
            # 如果检测到微笑，在原图上绘制文本
            cv.putText(pic, "smile", (sx, sy - 7), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv.LINE_AA)
    # 显示处理后的图像
    cv.imshow("original video", pic)


def main():
    # 初始化视频捕捉和检测器
    cap = initialize_capture()
    face_detector, eye_detector, smile_detector = initialize_detectors()

    # 初始化录制相关变量
    recording = False
    record_video = None
    fourcc = cv.VideoWriter_fourcc(*"XVID")

    # 获取视频流的实际帧率和分辨率
    fps = cap.get(cv.CAP_PROP_FPS)
    print(f"当前视频帧率是：{fps}")
    width = int(cap.get(cv.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv.CAP_PROP_FRAME_HEIGHT))

    while True:
        # 处理视频的每一帧：成功获取当前帧则flag为True，frame为当前帧
        ret, frame = cap.read()
        if not ret:
            break
        detect_face_eye_smile(frame, face_detector, eye_detector, smile_detector)

        # 处理按键事件
        key_pressed = cv.waitKey(1)
        print(f"按下的键是：{key_pressed} ")
        if recording:
            record_video.write(frame)
        if key_pressed == ord("c"):
            # 切换录制状态
            if recording:
                recording = False
                record_video.release()
                print("停止录制")
            else:
                recording = True
                record_video = cv.VideoWriter("/Users/jiangsai/Desktop/output.avi", fourcc, fps, (width, height))
                print("开始录制")
        elif key_pressed == 27:
            # 如果按下ESC键，则退出
            break

    # 释放资源
    cap.release()
    if recording:
        record_video.release()
    cv.destroyAllWindows()


if __name__ == "__main__":
    main()
