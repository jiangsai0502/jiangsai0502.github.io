###### 环境搭建

> yolo5的标注软件只能在python3.9运行

```bash
conda create -n py3.9 python=3.9
pip install opencv-python
pip install torch
pip install ultralytics
```

###### 检测案例

* 图片人脸检测：认出图像中哪些区域是人脸，并框选出来

  > [人脸识别模型获取方式](#人脸识别模型)

  ```python
  import cv2 as cv
  
  def read_image(filepath):
      """读取图片并返回."""
      image = cv.imread(filepath)
      if image is None:
          print("无法读取图片")
          exit(0)
      return image
  
  def resize_image(image, width, height):
      """调整图片尺寸并返回."""
      # 指定宽高调整
      resized_image = cv.resize(image, (150, 300))
      # 等比例调整，宽高都放大3倍
      resized_image = cv.resize(image, (0, 0), fx=3, fy=3)
      return resized_image
  
  def convert_to_gray(image):
      """将图片转换为灰度图像并返回."""
      gray_image = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
      return gray_image
  
  def detect_faces(gray_image, classifier_path):
      """检测人脸并返回坐标."""
      # 加载人脸检测的Haar级联分类器
      face_cascade = cv.CascadeClassifier(classifier_path)
      # 检测人脸
      return 抓紧给下载下来了，我操。face_cascade.detectMultiScale(gray_image)
  
  def draw_rectangles(image, coordinates):
      """在图片上绘制矩形框."""
      for x, y, w, h in coordinates:
          # 绘制矩形
          cv.rectangle(image, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
  
  def display_and_save_image(image, display_title, save_path):
      """显示图片并保存."""
      # 显示图片
      cv.imshow(display_title, image)
      # 保存图片
      cv.imwrite(save_path, image)
  
  def main():
      original_pic = read_image("/Users/jiangsai/Desktop/test/demo.png")
      resized_pic = resize_image(original_pic, 1500, 1500)
      gray_pic = convert_to_gray(resized_pic)
      detected_faces = detect_faces(gray_pic, cv.data.haarcascades + "haarcascade_frontalface_alt2.xml")
      draw_rectangles(resized_pic, detected_faces)
      display_and_save_image(resized_pic, "Detected Faces", "/Users/jiangsai/Desktop/test/temp.png")
  
      # 等待键盘输入q来退出
      while True:
          if cv.waitKey(1) & 0xFF == ord("q"):
              break
  
      # 释放所有窗口
      cv.destroyAllWindows()
  
  if __name__ == "__main__":
      main()
  ```

  > 1. `cv.imread(image_path)`：用于将图像 `image_path` 加载到内存；返回一个NumPy 数组。其中包含图像的红、绿、蓝通道或灰度通道信息
  >
  > 2. `cv.resize(image_NumPy, dsize=(500, 500))`：用于将图像 `image_NumPy` 的大小调整为 `dsize`
  >
  > 3. `cv.imshow("image_name", image_NumPy)`：用于将图像 `image_NumPy` 显示在名为 `image_name` 的窗口里
  >
  > 4. `cv2.cvtColor(image_NumPy, cv2.COLOR_BGR2GRAY)`：用于将图像 `image_NumPy` 转换为灰度图；返回一个NumPy 数组。因检测不需要颜色信息，而且灰度图处理速度更快，
  >
  > 5. `cv.CascadeClassifier(cv.data.haarcascades + "xxx.xml")` + `detectMultiScale(image_NumPy)`：用于识别或检测图像 `image_NumPy` 中的特定对象；返回一个匹配到的矩形，矩形的左上角坐标以及矩形宽、高
  >
  > 6. `cv.rectangle(image_NumPy, (x, y), (x+w, y+h), color=(0, 0, 255), thickness=2)`：用于绘制矩形；绘制的底图 `image_NumPy`，矩形框的左上角 `(x, y)`，右下角坐标 `(x+w, y+h)`，矩形框的颜色 `color` 和线宽 `thickness`
  >
  >    `cv.circle(image_NumPy, center=(x, y), radius=150, color=(255, 0, 0), thickness=2)`：用于绘制圆形；绘制的底图 `image_NumPy`，圆形的圆心 `(x, y)`，半径 `radius`，圆形框的颜色 `color` 和线宽 `thickness`
  >
  > 7. `cv.imwrite(image_path, image_NumPy)`：用于将一个内存中的图像 `image_NumPy` 保存为图像文件 `image_path`
  >
  > 8. `if cv.waitKey(1) & 0xFF == ord("q")`：固定写法，用于键盘监听到 `q` 键被按下，则返回 `True`，否则返回 `False`
  >
  > 9. `cv.destroyAllWindows()`：固定写法，用于关闭当前打开的所有窗口

* 视频人脸检测：认出视频中哪些区域是人脸，并框选出来

  ```python
  import cv2 as cv
  import numpy as np
  
  
  def initialize_capture():
      """初始化视频捕捉."""
      # 1、将视频源加载到内存
      #   1.1、摄像头，0获取系统默认摄像头，1,2……可替换更多摄像头
      cap_video = cv.VideoCapture(0, cv.CAP_DSHOW)
      #   1.2、打开摄像头
      cap_video.open(0)
      # 1、获取视频文件
      # cap_video = cv.VideoCapture("/Users/jiangsai/Desktop/test/jump boy.mp4")
  
      # 2、检查视频源是否加载成功
      if not cap_video.isOpened():
          print("视频打开失败")
          exit(0)
  
      # 3、打印视频的宽度和高度信息
      print(f"视频宽度：{cap_video.get(3)} 视频高度：{cap_video.get(4)}")
      # 4、返回加载到内存的视频源
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
      # 1、将图片转换为灰度图，因为Haar分类器需要灰度图像
      gray_pic = cv.cvtColor(pic, cv.COLOR_BGR2GRAY)
      # 2、在灰度图像中使用人脸检测器检测人脸
      faces = face_detector.detectMultiScale(gray_pic, 1.3, 2)
  
      # 3、遍历检测到的每个人脸
      for x, y, w, h in faces:
          # 3.1、在原图上绘制人脸矩形框
          cv.rectangle(pic, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
          # 3.2、提取人脸区域
          face_area = pic[y : y + h, x : x + w]
  
          # 3.3、在人脸区域内使用眼睛检测器检测眼睛
          eyes = eye_detector.detectMultiScale(face_area, 1.3, 10)
          for ex, ey, ew, eh in eyes:
              # 3.3.1、在人脸区域上绘制眼睛矩形框
              cv.rectangle(face_area, (ex, ey), (ex + ew, ey + eh), color=(0, 255, 0), thickness=2)
  
          # 3.4、在人脸区域内使用微笑检测器检测微笑
          smiles = smile_detector.detectMultiScale(face_area, scaleFactor=1.16, minNeighbors=65, minSize=(25, 25), flags=cv.CASCADE_SCALE_IMAGE)
          for sx, sy, sw, sh in smiles:
              # 3.4.1、在人脸区域上绘制微笑矩形框
              cv.rectangle(face_area, (sx, sy), (sx + sw, sy + sh), color=(255, 0, 0), thickness=2)
              # 3.4.2、如果检测到微笑，在原图上绘制文本
              cv.putText(pic, "smile", (sx, sy - 7), cv.FONT_HERSHEY_SIMPLEX, 2, (0, 0, 255), 2, cv.LINE_AA)
      # 4、显示处理后的图像
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
  ```

###### 识别案例

> 检测：判断图片中是否有某个目标
>
> 识别：判断图片中是否有某个目标，并指出目标是什么。识别需要目标和名称的对应关系库

###### 人脸识别模型

> OpenCV 默认提供的一些训练好的人脸识别模型，用于检测图片中的正面人脸，如脸部、眼睛、微笑
>
> 模型所在位置
>
> ```bash
> python -c 'import cv2; import os; print(os.path.join(cv2.data.__file__).replace("__init__.py", ""))'
> 
> /Users/jiangsai/anaconda3/envs/py3_pyautogui2/lib/python3.8/site-packages/cv2/data/
> ```
>
> 模型说明
>
> | 文件名                                | 用途                                        |
> | ------------------------------------- | ------------------------------------------- |
> | `haarcascade_frontalface_default.xml` | 检测正面人脸（快，不太准）                  |
> | `haarcascade_frontalface_alt.xml`     | 检测正面人脸（升级算法1.0，耗时，准确）     |
> | `haarcascade_frontalface_alt2.xml`    | 检测正面人脸（升级算法2.0，更耗时，更准确） |
> | `haarcascade_profileface.xml`         | 检测侧面人脸                                |
> | `haarcascade_eye.xml`                 | 检测眼睛                                    |
> | `haarcascade_eye_tree_eyeglasses.xml` | 检测佩戴眼镜的眼睛                          |
> | `haarcascade_smile.xml`               | 检测微笑                                    |
> | `haarcascade_upperbody.xml`           | 检测上半身                                  |
> | `haarcascade_fullbody.xml`            | 检测全身                                    |


