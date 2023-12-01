###### OpenCV+yolov5：识别摄像头/本地视频

> 1. 将摄像头/本地视频作为视频源
> 2. 读取视频源的每一帧
> 3. 使用YOLOv5「官方模型 / 自制模型」进行目标检测
> 4. 在每一帧上绘制检测到的物体边界框、类别标签
> 5. 按 'q' 键退出程序

```python
import cv2
import torch
import numpy as np
from AppKit import NSScreen


def get_scaling_factor():
    """获取主屏幕的缩放因子，Retina屏幕通常为2"""
    scaling_factor = NSScreen.mainScreen().backingScaleFactor()
    return scaling_factor


def load_model(model_path, conf_thres):
    """加载 YOLOv5 模型"""
    yolo_model = torch.hub.load("/Users/jiangsai/Desktop/test/yolov5", "custom", path=model_path, source="local")
    yolo_model.conf = conf_thres  # 更新模型的置信度阈值，大于阈值才识别
    return yolo_model


def detect_objects(yolo_model, screenshot, scaling_factor):
    """对象检测与可视化"""
    # 使用 YOLOv5 模型对当前帧进行目标检测
    results = yolo_model(screenshot)
    # 遍历所有检测结果，并在每个检测结果上画边框和标签
    # 每个检测结果包括边界框坐标（xyxy）、置信度 (conf) 和类别索引 (cls)
    for *xyxy, conf, cls in results.xyxy[0].cpu().numpy():
        # 获取类别名称。model.names 是一个列表，包含了所有可能的类别名称
        # int(cls) 将类别索引 (cls) 转换为整数，然后用它来从 model.names 中获取相应的类别名称
        label = yolo_model.names[int(cls)]
        # 解析边界框坐标 xyxy，并将它们转换为整数
        # xyxy 是一个列表，包含了四个元素：x1, y1, x2, y2（边界框的左上角和右下角坐标）
        x1, y1, x2, y2 = [int(i) for i in xyxy]
        # (x1, y1) ：边界框的左上角坐标；(x2, y2) 是边界框的右下角坐标
        # (0, 255, 0) 是矩形颜色（绿色）的 RGB 值，2 是矩形边框的厚度
        cv2.rectangle(screenshot, (x1, y1), (x2, y2), (0, 255, 0), 2)
        # label_with_conf：类别名+置信度；(x1, y1-10)：类别展示位置（稍微在边界框上方）
        # cv2.FONT_HERSHEY_SIMPLEX：字体，0.9：字号，(0, 255, 0)：字色，2：字体粗细
        label_with_conf = f"{label} {conf:.2f}"
        cv2.putText(screenshot, label_with_conf, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        # 计算检测框的中心位置
        center_x = int((x1 + x2) / scaling_factor)
        center_y = int((y1 + y2) / scaling_factor)
        cv2.rectangle(screenshot, (center_x - 10, center_y - 10), (center_x + 10, center_y + 10), (0, 0, 255), 2)
    # 显示处理后的帧
    cv2.imshow("YOLOv5 Detection", screenshot)


if __name__ == "__main__":
    # 模型文件路径
    model_path = "/Users/jiangsai/Desktop/test/yolov5/weights/yolov5s.pt"
    # 设置置信度阈值
    conf_thres = 0.5
    # 加载yolo模型
    yolo_model = load_model(model_path, conf_thres)

    # 识别的视频源
    video_source = 0  # 摄像头：0，本地视频："/Users/jiangsai/Desktop/jump.mp4"
    # 加载视频
    cap = cv2.VideoCapture(video_source)
    # 当前屏幕坐标和分辨率的缩放比例
    scaling_factor = get_scaling_factor()

    # 检查是否打开视频
    if not cap.isOpened():
        print(f"无法打开视频源: {video_source}")
        exit()
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        frame = cv2.flip(frame, 1)  # 镜像反转：前置摄像头为左右反转的镜像模式
        detect_objects(yolo_model, frame, scaling_factor)
        # 按'q'键跳出循环
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    # 释放 VideoCapture 对象和销毁所有 OpenCV 窗口
    cap.release()
    cv2.destroyAllWindows()
```

> `torch.hub.load("ultralytics/yolov5", "custom", path=model_path, force_reload=True)`
>
> * `"ultralytics/yolov5"`：即使用Github的Yolo V5代码库
>   * `/Users/jiangsai/Desktop/test/yolov5`：即使用本地Yolo V5代码库
> * `custom`：即使用自定义模型
> * `path`：即自定义模型的文件路径
> * `source="local"`：即使用本地Yolo V5代码库加载模型
> * `force_reload=True`：即强制重新加载模型，更换模型时确保本次使用的是新更换的模型版本