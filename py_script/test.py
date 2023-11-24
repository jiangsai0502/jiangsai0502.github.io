import cv2
import numpy as np
import mss
import torch
from models.experimental import attempt_load
from utils.torch_utils import select_device
from utils.general import non_max_suppression, scale_coords
from utils.datasets import letterbox


# 初始化YOLO模型
def load_model(weights_path, device="cpu"):
    model = attempt_load(weights_path, map_location=device)  # 加载YOLO模型
    return model.to(device).eval()


# 处理屏幕截图以用于模型推理
def process_frame(frame, img_size=640):
    frame = letterbox(frame, new_shape=img_size)[0]
    frame = frame[:, :, ::-1].transpose(2, 0, 1)  # BGR to RGB
    frame = np.ascontiguousarray(frame)
    frame = torch.from_numpy(frame).to(device)
    frame = frame.float()
    frame /= 255.0  # 归一化
    if frame.ndimension() == 3:
        frame = frame.unsqueeze(0)
    return frame


# YOLO检测
def detect(model, frame):
    pred = model(frame, augment=False)[0]
    pred = non_max_suppression(pred, 0.25, 0.45)
    return pred


# 主函数
def main():
    device = select_device("")
    model = load_model("yolov5s.pt", device=device)
    sct = mss.mss()

    # 初始化视频录制
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")
    out = cv2.VideoWriter("/Users/jiangsai/Desktop/output.mp4", fourcc, 20.0, (640, 480))

    while True:
        screenshot = sct.grab(sct.monitors[1])
        frame = np.array(screenshot)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGRA2BGR)

        # 处理屏幕截图并进行YOLO检测
        frame_processed = process_frame(frame)
        pred = detect(model, frame_processed)

        # 在原始帧上绘制检测结果
        # (这部分需要根据您的需要进行调整，例如，绘制边界框和标签)

        # 保存帧到视频
        out.write(frame)

        # 显示结果
        cv2.imshow("Screen Capture", frame)
        if cv2.waitKey(1) == 27:  # 按下ESC键退出
            break

    # 清理
    sct.close()
    out.release()
    cv2.destroyAllWindows()


if __name__ == "__main__":
    main()
