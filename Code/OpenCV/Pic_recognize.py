import cv2
import torch
import pyautogui

# 加载官方预训练的模型
# model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)

# 使用自定义模型权重加载模型
model_path = "/Users/jiangsai/Desktop/test/yolov5/weights/yolov5s.pt"
# "custom" 即自定义模型，"path" 指定模型文件的路径。
yolo_model = torch.hub.load("ultralytics/yolov5", "custom", path=model_path, force_reload=True)

# 打开视频文件或相机
# video_path = "/Users/jiangsai/Desktop/test/jump boy.mp4"
# 打开摄像头
video_path = 0
cap = cv2.VideoCapture(video_path)

# 循环读取视频帧
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 使用 YOLOv5 模型对当前帧进行目标检测
    results = yolo_model(frame)

    # 遍历所有检测结果results.xyxy[0]，并在每个检测结果上画边框和标签
    # 每个检测结果包括边界框坐标（xyxy）、置信度 (conf) 和类别索引 (cls)。
    for *xyxy, conf, cls in results.xyxy[0].cpu().numpy():
        # 获取类别名称。model.names 是一个列表，包含了所有可能的类别名称。
        # int(cls) 将类别索引 (cls) 转换为整数，然后用它来从 model.names 中获取相应的类别名称。
        label = yolo_model.names[int(cls)]
        # 解析边界框坐标 xyxy，并将它们转换为整数。
        # xyxy 是一个列表，包含了四个元素：x1, y1, x2, y2（边界框的左上角和右下角坐标）。
        x1, y1, x2, y2 = [int(i) for i in xyxy]
        # (x1, y1) 是边界框的左上角坐标，(x2, y2) 是边界框的右下角坐标。
        # (0, 255, 0) 是矩形颜色（绿色）的 RGB 值，2 是矩形边框的厚度。
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # putText 函数在边界框的展示文字 (x1, y1 - 10) 指定了文本开始的位置（稍微在边界框上方）。
        # cv2.FONT_HERSHEY_SIMPLEX 是字体样式，0.9 是字体大小，(0, 255, 0) 是字体颜色，2 是字体厚度。
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

        # 计算检测框的中心位置
        center_x = int((x1 + x2) / 2)
        center_y = int((y1 + y2) / 2)
        cv2.rectangle(frame, (center_x - 10, center_y - 10), (center_x + 10, center_y + 10), (0, 0, 255), 2)
        # 将鼠标移动到检测框的中心
        # pyautogui.moveTo(center_x, center_y)

    # 显示处理后的帧。
    cv2.imshow("YOLOv5 Detection", frame)

    # 如果用户按下 'q' 键，则跳出循环。
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 释放 VideoCapture 对象和销毁所有 OpenCV 窗口。
cap.release()
cv2.destroyAllWindows()
