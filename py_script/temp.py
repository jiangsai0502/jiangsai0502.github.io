from datetime import datetime
import cv2 as cv
import numpy as np


# 检测函数
def detect_face_eye_smile(pic):
    # 1、灰度转换
    gray_pic = cv.cvtColor(pic, cv.COLOR_BGR2GRAY)
    # 2、人脸检测：在全图的灰度图像中的检测人脸矩形区域
    face_coord = detect_face.detectMultiScale(gray_pic, 1.3, 2)
    # 3、在原图上的多张人脸绘制人脸矩形框
    for x, y, w, h in face_coord:
        cv.rectangle(pic, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
        # 4、框选出人脸区域，在人脸区域而不是全图中进行人眼和微笑检测，节省资源
        face_area = pic[y : y + h, x : x + w]
        # 5、人眼检测：在人脸区域的灰度图像中的检测人眼矩形区域
        eyes_coord = detect_eyes.detectMultiScale(face_area, 1.3, 10)
        for x, y, w, h in eyes_coord:
            cv.rectangle(face_area, (x, y), (x + w, y + h), color=(0, 255, 0), thickness=2)
        # 6、微笑检测：在人脸区域的灰度图像中的检测人眼矩形区域
        smile_coord = detect_smile.detectMultiScale(face_area, scaleFactor=1.16, minNeighbors=65, minSize=(25, 25), flags=cv.CASCADE_SCALE_IMAGE)
        for x, y, w, h in smile_coord:
            cv.rectangle(face_area, (x, y), (x + w, y + h), color=(255, 0, 0), thickness=2)
            # 7、检测到微笑后
            cv.putText(pic, "smile", (x, y - 7), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv.LINE_AA)
    cv.imshow("original video", pic)


# 其他检测方法


def main():
    while True:
        # 1、读取视频的当前帧：获取帧成功则flag为True，frame为当前帧
        flag, frame = cap_video.read()
        # 2、判断当前帧是否为True
        if not flag:
            break
        # 3、检测并展示当前帧
        detect_face_eye_smile(frame)
        # 4、监听键盘：每隔60毫秒检测一次，焦点落在视频窗口时，获取键盘上按下哪个键
        key_pressed = cv.waitKey(60)
        print(f"按下的键是：{key_pressed} ")
        # 5、焦点落在视频窗口时，按下c键开始录制，再按c键停止录制
        if recording:
            record_video.write(frame)
        if key == ord("c"):
            # 如果按下 'c' 键，开始或停止录制
            if recording:
                # 停止录制
                recording = False
                record_video.release()
                print("停止录制")
            else:
                # 开始录制
                recording = True
                record_video = cv2.VideoWriter("/Users/jiangsai/Desktop/output.avi", fourcc, 20.0, (640, 480))
                print("开始录制")
        # 5、焦点落在视频窗口时，按下esc键，就退出程序
        if key_pressed == 27:
            break


if __name__ == "__main__":
    # 1、获取视频源
    #   摄像头，0获取系统默认摄像头，1,2……可替换更多摄像头
    # cap_video = cv.VideoCapture(0, cv.CAP_DSHOW)
    # #  打开摄像头
    # cap_video.open(0)
    #   获取视频文件
    cap_video = cv.VideoCapture("/Users/jiangsai/Desktop/test/jump boy.mp4")
    #   判断视频是否打开
    if not cap_video.isOpened():
        print("视频打开失败")
        exit(0)
    #   获取视频的宽、高信息：cap.get()传入的参数可以是0-18的整数
    print(f"视频宽度：{cap_video.get(3)}  视频高度：{cap_video.get(4)}")
    # 2、定义视频录制变量
    fourcc = cv.VideoWriter_fourcc(*"XVID")
    record_video = None
    recording = False
    # 3、初始化检测器：人脸检测器、眼睛检测器、微笑检测器
    detect_face = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_alt2.xml")
    detect_eyes = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_eye.xml")
    detect_smile = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_smile.xml")
    # 4、主函数
    main()
    # 5、关闭摄像头
    cap_video.release()
    if recording:
        out.release()
    # 6、关闭窗口
    cv.destroyAllWindows()


def detect_edge(pic):
    # 1、灰度转换
    gray_pic = cv.cvtColor(pic, cv.COLOR_BGR2GRAY)
    # 2、边缘检测：返回单通道图像
    edge_pic = cv.Canny(gray_pic, 100, 200)
    # 3、3个单通道摞成1个3通道图像
    edge_pic = np.dstack([edge_pic, edge_pic, edge_pic])
    # 4、检测灰度图像中的人脸
    detected_coord = detect_face.detectMultiScale(gray_pic)
    # 5、在图像上绘制出检测到的人脸矩形框
    for x, y, w, h in detected_coord:
        cv.rectangle(pic, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
        cv.rectangle(gray_pic, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
        cv.rectangle(edge_pic, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
    # 6、显示图像
    cv.imshow("original video", pic)
    cv.imshow("grey video", gray_pic)
    cv.imshow("frame video", edge_pic)
