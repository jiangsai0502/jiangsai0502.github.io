import cv2
import torch

# 加载官方预训练的模型
model = torch.hub.load("ultralytics/yolov5", "yolov5s", pretrained=True)

# 打开视频文件或相机
video_path = "/Users/jiangsai/Desktop/test/jump boy.mp4"  # 修改为你的视频路径或使用 0 用于摄像头输入
cap = cv2.VideoCapture(video_path)

# 循环读取视频帧
while cap.isOpened():
    ret, frame = cap.read()
    if not ret:
        break

    # 进行目标检测
    results = model(frame)

    # 对结果进行解析，并在帧上画出检测框和标签
    for *xyxy, conf, cls in results.xyxy[0].cpu().numpy():
        label = model.names[int(cls)]  # 获取类别名称
        x1, y1, x2, y2 = [int(i) for i in xyxy]
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
        cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)

    # 显示帧
    cv2.imshow("YOLOv5 Detection", frame)

    # 按 'q' 退出循环
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# 释放资源
cap.release()
cv2.destroyAllWindows()
