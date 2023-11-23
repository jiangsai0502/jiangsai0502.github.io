###### 环境搭建



###### 检测案例

* 图片人脸检测：认出图像中哪些区域是人脸，并框选出来

  > [人脸识别模型获取方式](#人脸识别模型)

  ```python
  import cv2 as cv
  
  # 待检测图片
  pic = "/Users/jiangsai/Desktop/test/demo1.png"
  
  # 1、读取图片
  original_pic = cv.imread(pic)
  
  # 2、修改图片尺寸
  resize_pic = cv.resize(original_pic, dsize=(1500, 1500))
  
  # 3、显示图片，名称用英文名，中文可能无法展示
  cv.imshow(f"resize {resize_pic.shape}", resize_pic)
  
  # 4、灰度转换
  gray_pic = cv.cvtColor(resize_pic, cv.COLOR_BGR2GRAY)
  
  # 5、分类器
  detect_face = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_alt2.xml")
  detected_coord = detect_face.detectMultiScale(gray_pic)
  
  for x, y, w, h in detected_coord:
      # 6、绘制矩形
      cv.rectangle(resize_pic, (x, y), (x + w, y + h), color=(0, 0, 255), thickness=2)
      # 7、绘制圆形
      # cv.circle(resize_pic, center=(x, y), radius=150, color=(255, 0, 0), thickness=2)
  
  cv.imshow("detected", resize_pic)
  
  # 7、保存图片
  cv.imwrite("/Users/jiangsai/Desktop/test/aaa.png", resize_pic)
  
  # 8、焦点落在图片窗口上时，点击q键退出
  while True:
      if cv.waitKey(1) & 0xFF == ord("q"):
          break
  
  # 9、释放内存
  cv.destroyAllWindows()
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

>模板匹配：`cv2.matchTemplate`  低级识别，适合于目标图像与模板非常相似，图像一旦旋转、运动便无法匹配
>
>特征匹配：

* 模板匹配

  * 图片识别物品（搜索图片与模板图片同尺寸）

    ```python
    import cv2
    import numpy as np
    import os
    
    def load_templates(folder):
        """加载模板图片"""
        templates = {}
        for item in os.listdir(folder):
            # 获取文件的名称和扩展名，并转换为小写
            file_name = item.lower().split(".")[0]
            file_extension = item.lower().split(".")[-1]
            # 检查扩展名是否为图片格式
            if file_extension not in ["jpg", "jpeg", "png", "bmp"]:
                continue
            img_path = os.path.join(folder, item)
    
            img = cv2.imread(img_path, 0)
            if img is not None:
                templates[file_name] = img  # 添加到列表中
        return templates
    
    
    def match_and_label(frame, templates):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        for name, template in templates.items():
            if template is None or len(template.shape) < 2:
                continue
            res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(res)
            if max_val > 0.2:  # 设定阈值
                top_left = max_loc
                bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
                cv2.rectangle(frame, top_left, bottom_right, 255, 2)
                cv2.putText(frame, name, top_left, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
        return frame
    
    
    # 使用函数
    templates = load_templates("/Users/jiangsai/Desktop/test/yellow")
    image_path = "/Users/jiangsai/Desktop/test/7.jpeg"
    image = cv2.imread(image_path)  # 读取单张图片
    
    labeled_image = match_and_label(image, templates)
    cv2.imshow("Labeled Image", labeled_image)  # 显示标注后的图片
    
    cv2.waitKey(0)  # 等待用户输入
    cv2.destroyAllWindows()  # 关闭所有窗口
    ```

  * 图片识别物品（搜索图片与模板图片不同尺寸）

    * 1个模板1张图

      ```python
      import cv2, os
      import numpy as np
      
      
      # 定义多尺度模板匹配函数
      def multi_scale_template_matching(template, search_image, scales=np.linspace(0.2, 1.0, 20)):
          # 1、将模板图像转换为灰度图，因为模板匹配不需要颜色信息，而且灰度图处理速度更快
          template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
          # 2、将待搜索的图像也转换为灰度图
          search_image_gray = cv2.cvtColor(search_image, cv2.COLOR_BGR2GRAY)
          # 初始化最佳匹配结果为None
          best_match = None
      
          # 3、遍历不同的缩放尺度，np.linspace生成一个等差数列，这里是0.2到1.0之间的20个数
          for scale in scales:
              # 3.1、根据当前尺度缩放模板图像
              resized_template = cv2.resize(template_gray, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
              # 3.2、检查缩放后的模板是否比搜索图像大，如果是，则跳过此尺度
              if (
                  resized_template.shape[0] > search_image_gray.shape[0]
                  or resized_template.shape[1] > search_image_gray.shape[1]
              ):
                  continue
      
              # 3.3、对缩放后的模板和搜索图像进行模板匹配
              match_result = cv2.matchTemplate(search_image_gray, resized_template, cv2.TM_CCOEFF_NORMED)
              # 3.4、从匹配结果中找到最大匹配值和其位置
              _, max_val, _, max_loc = cv2.minMaxLoc(match_result)
      
              # 3.5、如果这是第一个匹配结果或者当前匹配更好，则更新最佳匹配
              if best_match is None or max_val > best_match[0]:
                  best_match = (max_val, max_loc, scale, resized_template.shape[1], resized_template.shape[0])
      
          # 4、返回最佳匹配结果
          return best_match
      
      
      # 定义在模板文件夹中匹配所有模板的函数
      def match_templates_in_folder(templates_folder, search_image_path):
          # 1、读取搜索图像
          search_image = cv2.imread(search_image_path)
          # 如果搜索图像未能成功加载，则打印错误信息并返回
          if search_image is None:
              print("搜索图像未能成功加载")
              return
      
          # 2、遍历模板文件夹中的每个文件
          for template_name in os.listdir(templates_folder):
              # 2.1、获取模板文件的完整路径
              template_path = os.path.join(templates_folder, template_name)
              # 2.2、确保当前路径是文件，不是目录
              if os.path.isfile(template_path):
                  # 2.3、读取模板图像
                  template = cv2.imread(template_path)
                  # 如果模板图像未能成功加载，则打印错误信息并继续下一个文件
                  if template is None:
                      print(f"模板图像 {template_name} 未能成功加载")
                      continue
      
                  # 2.4、对当前模板图像执行多尺度模板匹配
                  best_match = multi_scale_template_matching(template, search_image)
                  # 2.5、如果找到了匹配结果
                  if best_match is not None:
                      # 2.5.1、获取匹配结果的详细信息
                      max_val, max_loc, scale, t_width, t_height = best_match
                      # 2.5.2、计算匹配区域的左上角和右下角坐标
                      top_left = (int(max_loc[0]), int(max_loc[1]))
                      # t_width：匹配宽度；t_height：匹配高度
                      bottom_right = (int(max_loc[0] + t_width), int(max_loc[1] + t_height))
      
                      # 2.5.3、在搜索图像上画出矩形框，并在矩形框上方标注模板文件名
                      # cv2.rectangle参数：绘制矩形框的底图，矩形框的左上角和右下角坐标、矩形框的颜色和线宽
                      # cv2.putText参数：放置文字的底图，文本，文本的左上角坐标、字体、字体大小、文本的颜色、线宽
                      cv2.rectangle(search_image, top_left, bottom_right, (0, 0, 255), 4)
                      cv2.putText(
                          search_image,
                          template_name,
                          (top_left[0], top_left[1] - 10),
                          cv2.FONT_HERSHEY_SIMPLEX,
                          0.7,
                          (0, 0, 255),
                          2,
                      )
      
          # 显示所有匹配结果的搜索图像
          cv2.imshow("Template Matches", search_image)
          cv2.waitKey(0)  # 等待用户按键后关闭窗口
          cv2.destroyAllWindows()  # 销毁所有创建的窗口
      
      
      # 设置模板文件夹路径和搜索图像路径
      templates_folder = "/Users/jiangsai/Desktop/test/recognition"  # 模板文件夹
      search_image_path = "/Users/jiangsai/Desktop/test/demo.jpeg"  # 搜索图像
      
      # 调用函数，执行匹配并在找到的矩形框上标注模板文件名
      match_templates_in_folder(templates_folder, search_image_path)
      ```

    * 1个模板多张图

      ```python
      import cv2
      import numpy as np
      import os
      
      def multi_scale_template_matching(template, search_image, scales=np.linspace(0.2, 1.0, 20)):
          # 1、将模板图像转换为灰度图，因为模板匹配不需要颜色信息，而且灰度图处理速度更快
          template_gray = cv2.cvtColor(template, cv2.COLOR_BGR2GRAY)
          # 2、将待搜索的图像也转换为灰度图
          search_image_gray = cv2.cvtColor(search_image, cv2.COLOR_BGR2GRAY)
          # 初始化最佳匹配结果为None
          best_match = None
      
          # 3、遍历不同的缩放尺度，np.linspace生成一个等差数列，这里是0.2到1.0之间的20个数
          for scale in scales:
              # 3.1、根据当前尺度缩放模板图像
              resized_template = cv2.resize(template_gray, None, fx=scale, fy=scale, interpolation=cv2.INTER_AREA)
              # 3.2、检查缩放后的模板是否比搜索图像大，如果是，则跳过此尺度
              if (
                  resized_template.shape[0] > search_image_gray.shape[0]
                  or resized_template.shape[1] > search_image_gray.shape[1]
              ):
                  continue
      
              # 3.3、对缩放后的模板和搜索图像进行模板匹配
              match_result = cv2.matchTemplate(search_image_gray, resized_template, cv2.TM_CCOEFF_NORMED)
              # 3.4、从匹配结果中找到最大匹配值和其位置
              _, max_val, _, max_loc = cv2.minMaxLoc(match_result)
      
              # 3.5、如果这是第一个匹配结果或者当前匹配更好，则更新最佳匹配
              if best_match is None or max_val > best_match[0]:
                  best_match = (max_val, max_loc, scale, resized_template.shape[1], resized_template.shape[0])
      
          # 4、返回最佳匹配结果
          return best_match
      
      
      def match_template_in_folder(template_folder, search_image):
          matches = []
          # 遍历模板文件夹中的每个文件
          for template_name in os.listdir(template_folder):
              template_path = os.path.join(template_folder, template_name)
              if os.path.isfile(template_path):
                  template = cv2.imread(template_path)
                  if template is None:
                      print(f"Error: Unable to load template image: {template_name}")
                      continue
      
                  best_match = multi_scale_template_matching(template, search_image)
                  if best_match:
                      matches.append((best_match, template_name))
          return matches
      
      
      def match_templates_in_folders(templates_root_folder, search_image_path):
          search_image = cv2.imread(search_image_path)
          if search_image is None:
              print("Error: Unable to load the search image.")
              return
      
          # 遍历根模板文件夹中的每个二级文件夹
          for folder_name in os.listdir(templates_root_folder):
              folder_path = os.path.join(templates_root_folder, folder_name)
              if os.path.isdir(folder_path):
                  # 对当前二级文件夹中的模板进行匹配
                  matches = match_template_in_folder(folder_path, search_image)
                  for best_match, matched_template_name in matches:
                      max_val, max_loc, scale, t_width, t_height = best_match
                      top_left = (int(max_loc[0]), int(max_loc[1]))
                      bottom_right = (int(max_loc[0] + t_width), int(max_loc[1] + t_height))
      
                      # 在搜索图像上画出矩形框，并在矩形框上方标注二级文件夹名称
                      cv2.rectangle(search_image, top_left, bottom_right, (0, 0, 255), 4)
                      cv2.putText(
                          search_image,
                          folder_name,
                          (top_left[0], top_left[1] - 10),
                          cv2.FONT_HERSHEY_SIMPLEX,
                          0.7,
                          (0, 0, 255),
                          2,
                      )
      
          # 显示所有匹配结果的搜索图像
          cv2.imshow("Template Matches", search_image)
          cv2.waitKey(0)
          cv2.destroyAllWindows()
      
      
      # 设置根模板文件夹路径和搜索图像路径
      templates_root_folder = "/Users/jiangsai/Desktop/test/recognition"  # 根模板文件夹
      search_image_path = "/Users/jiangsai/Desktop/test/demo.jpeg"  # 搜索图像
      
      
      # 调用函数，执行匹配并在找到的矩形框上标注模板文件名
      match_templates_in_folders(templates_root_folder, search_image_path)
      ```

  * 图片识别人脸

    >1. 从文件夹读取已知人像的图片和名称
    >2. 使用人脸检测在待检测图片中找到所有人脸
    >3. 对于每个检测到的人脸，使用模板匹配方法确定它是否匹配已知人像之一
    >4. 在图片上标注已知人像的名称，对于未匹配的人脸标注“未知”

    ```python
    import cv2 as cv
    import os
    
    # 加载已知人像
    def load_known_faces(folder_path):
        known_faces = {}
        for filename in os.listdir(folder_path):
            if filename.lower().endswith((".png", ".jpg", ".jpeg")):
                name = os.path.splitext(filename)[0]
                img_path = os.path.join(folder_path, filename)
                img = cv.imread(img_path, 0)
                known_faces[name] = img
        return known_faces
    
    
    # 人脸匹配和标注
    def match_and_label(image, known_faces, face_cascade):
        gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)
        faces = face_cascade.detectMultiScale(gray, 1.1, 4)
        for x, y, w, h in faces:
            face_roi = gray[y : y + h, x : x + w]
            matched_name = "未知"
            for name, face_img in known_faces.items():
                resized_face_img = cv.resize(face_img, (w, h))  # 调整模板大小
                res = cv.matchTemplate(face_roi, resized_face_img, cv.TM_CCOEFF_NORMED)
                _, max_val, _, _ = cv.minMaxLoc(res)
                if max_val > 0.7:  # 阈值可调
                    matched_name = name
                    break
            cv.rectangle(image, (x, y), (x + w, y + h), (255, 0, 0), 2)
            cv.putText(image, matched_name, (x, y - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (255, 0, 0), 2)
        return image
    
    
    # 主程序
    def process_image(image_path, known_faces_folder):
        known_faces = load_known_faces(known_faces_folder)
        face_cascade = cv.CascadeClassifier(cv.data.haarcascades + "haarcascade_frontalface_default.xml")
        image = cv.imread(image_path)
        labeled_image = match_and_label(image, known_faces, face_cascade)
        cv.imshow("Labeled Image", labeled_image)
        cv.waitKey(0)
        cv.destroyAllWindows()
    
    
    # 执行
    image_path = "/Users/jiangsai/Desktop/test/7.jpeg"
    known_faces_folder = "/Users/jiangsai/Desktop/test/yellow"
    process_image(image_path, known_faces_folder)
    ```

  * 视频识别物品（非常不实用）

    ```python
    import cv2
    import numpy as np
    import os
    
    
    def load_templates(folder):
        """加载模板图片"""
        templates = {}
        for item in os.listdir(folder):
            # 获取文件的名称和扩展名，并转换为小写
            file_name = item.lower().split(".")[0]
            file_extension = item.lower().split(".")[-1]
            # 检查扩展名是否为图片格式
            if file_extension not in ["jpg", "jpeg", "png", "bmp"]:
                continue
            img_path = os.path.join(folder, item)
    
            img = cv2.imread(img_path, 0)
            if img is not None:
                templates[file_name] = img  # 添加到列表中
        return templates
    
    
    def match_and_label(frame, templates):
        gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        for name, template in templates.items():
            if template is None or len(template.shape) < 2:
                continue
            res = cv2.matchTemplate(gray_frame, template, cv2.TM_CCOEFF_NORMED)
            _, max_val, _, max_loc = cv2.minMaxLoc(res)
            if max_val > 0.8:  # 设定阈值
                top_left = max_loc
                bottom_right = (top_left[0] + template.shape[1], top_left[1] + template.shape[0])
                cv2.rectangle(frame, top_left, bottom_right, 255, 2)
                cv2.putText(frame, name, top_left, cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 255, 255), 2)
                break
        return frame
    
    
    def recognize_items_in_video(video_path, templates):
        """在视频中识别物品"""
        cap = cv2.VideoCapture(video_path)
        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break
    
            labeled_frame = match_and_label(frame, templates)
            cv2.imshow("Video", labeled_frame)
    
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    
        cap.release()
        cv2.destroyAllWindows()
    
    
    # 使用函数
    templates = load_templates("/Users/jiangsai/Desktop/test/yellow")
    recognize_items_in_video("/Users/jiangsai/Desktop/test/7.jpeg", templates)
    ```

* 特征识别

  ```python
  import cv2
  import numpy as np
  import os
  
  
  def load_sift_templates(folder):
      sift = cv2.SIFT_create()
      templates = {}
      for item in os.listdir(folder):
          file_extension = item.lower().split(".")[-1]
          if file_extension not in ["jpg", "jpeg", "png", "bmp"]:
              continue
          img_path = os.path.join(folder, item)
          img = cv2.imread(img_path, 0)
          if img is not None:
              key_points, descriptors = sift.detectAndCompute(img, None)
              templates[item.split(".")[0]] = (key_points, descriptors)
      return templates
  
  
  def match_and_label_sift(frame, templates):
      sift = cv2.SIFT_create()
      gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
      frame_key_points, frame_descriptors = sift.detectAndCompute(gray_frame, None)
      flann_index_kdtree = 1
      index_params = {"algorithm": flann_index_kdtree, "trees": 5}
      search_params = {"checks": 50}
      flann = cv2.FlannBasedMatcher(index_params, search_params)
  
      for name, (tpl_key_points, tpl_descriptors) in templates.items():
          matches = flann.knnMatch(tpl_descriptors, frame_descriptors, k=2)
          good_matches = []
          for m, n in matches:
              if m.distance < 0.7 * n.distance:  # Lowe's ratio test
                  good_matches.append(m)
          if len(good_matches) > 10:  # 设置匹配点的最小数量
              src_pts = np.float32([tpl_key_points[m.queryIdx].pt for m in good_matches]).reshape(-1, 1, 2)
              dst_pts = np.float32([frame_key_points[m.trainIdx].pt for m in good_matches]).reshape(-1, 1, 2)
              M, _ = cv2.findHomography(src_pts, dst_pts, cv2.RANSAC, 5.0)
              h, w = tpl_descriptors.shape[:2]
              pts = np.float32([[0, 0], [0, h - 1], [w - 1, h - 1], [w - 1, 0]]).reshape(-1, 1, 2)
              dst = cv2.perspectiveTransform(pts, M)
              frame = cv2.polylines(frame, [np.int32(dst)], True, (0, 255, 0), 3, cv2.LINE_AA)
              cv2.putText(
                  frame,
                  name,
                  (int(dst[0][0][0]), int(dst[0][0][1])),
                  cv2.FONT_HERSHEY_SIMPLEX,
                  1,
                  (255, 255, 255),
                  2,
              )
      return frame
  
  
  # 使用函数
  templates = load_sift_templates("/Users/jiangsai/Desktop/test/recognition/")
  image_path = "/Users/jiangsai/Desktop/test/demo.jpeg"
  image = cv2.imread(image_path)
  
  labeled_image = match_and_label_sift(image, templates)
  cv2.imshow("Labeled Image", labeled_image)
  
  cv2.waitKey(0)
  cv2.destroyAllWindows()
  ```

  

###### 原理窥探



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






