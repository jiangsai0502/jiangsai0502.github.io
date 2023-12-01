###### OpenCV+yolov5+PyautoGUI：识别本地程序+自动操作

> 1. 查找目标程序窗口信息
> 2. 将目标程序窗口作为视频源
> 3. 读取视频源的每一帧
> 4. 使用YOLOv5「官方模型 / 自制模型」进行目标检测
> 5. 在每一帧上绘制检测到的物体边界框、类别标签
> 6. 按 'q' 键退出程序

```python
import Quartz, time, pyautogui, torch
from AppKit import NSWorkspace, NSScreen, NSApplicationActivationPolicyRegular
import numpy as np
import Quartz.CoreGraphics as CG
import cv2 as cv

def get_scaling_factor():
    """获取主屏幕的缩放因子，Retina屏幕通常为2"""
    scaling_factor = NSScreen.mainScreen().backingScaleFactor()
    return scaling_factor

def find_app_window(app_name):
    """查找目标程序窗口的信息"""
    workspace = NSWorkspace.sharedWorkspace()
    active_apps = workspace.runningApplications()
    for app in active_apps:
        # 只列出前台运行的应用程序
        if app.activationPolicy() == NSApplicationActivationPolicyRegular:
            if app.localizedName() == app_name:
                # 获取目标程序的进程ID
                app_pid = app.processIdentifier()
                # 获取所有窗口的信息
                window_info_list = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID)
                for window_info in window_info_list:
                    # 如果窗口属于目标程序
                    if window_info["kCGWindowOwnerPID"] == app_pid:
                        # 获取窗口的位置和大小
                        window = window_info["kCGWindowBounds"]
                        return (window["X"], window["Y"], window["Width"], window["Height"])

def capture_screen(x, y, width, height):
    """「固定用法」捕获屏幕上指定区域的图像"""
    # 根据指定的位置和大小创建CGRect结构体
    region = CG.CGRectMake(x, y, width, height)
    # 捕获指定区域的屏幕内容
    image_ref = CG.CGWindowListCreateImage(region, CG.kCGWindowListOptionOnScreenOnly, CG.kCGNullWindowID, CG.kCGWindowImageDefault)
    # 将捕获的内容转换为 numpy 数组
    width = CG.CGImageGetWidth(image_ref)
    height = CG.CGImageGetHeight(image_ref)
    bytes_per_row = CG.CGImageGetBytesPerRow(image_ref)
    pixel_data = CG.CGDataProviderCopyData(CG.CGImageGetDataProvider(image_ref))
    image = np.frombuffer(pixel_data, dtype=np.uint8).reshape((height, bytes_per_row // 4, 4))
    image = image[:, :width, :3]
    image = np.ascontiguousarray(image, dtype=np.uint8)
    return image

def load_model(model_path, conf_thres):
    """加载 YOLOv5 模型"""
    yolo_model = torch.hub.load("/Users/jiangsai/Desktop/test/yolov5", "custom", path=model_path, source="local")
    yolo_model.conf = conf_thres  # 更新模型的置信度阈值，大于阈值才识别
    return yolo_model

def detect_and_display(yolo_model, screenshot, scaling_factor):
    """使用YOLOv5模型对图像进行目标检测并显示结果"""
    results = yolo_model(screenshot)
    for *xyxy, conf, cls in results.xyxy[0].cpu().numpy():
        label = yolo_model.names[int(cls)]
        x1, y1, x2, y2 = [int(i) for i in xyxy]
        cv.rectangle(screenshot, (x1, y1), (x2, y2), (0, 255, 0), 2)
        label_with_conf = f"{label} {conf:.2f}"
        cv.putText(screenshot, label_with_conf, (x1, y1 - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
        center_x = int((x1 + x2) / scaling_factor)
        center_y = int((y1 + y2) / scaling_factor)
        cv.rectangle(screenshot, (center_x - 10, center_y - 10), (center_x + 10, center_y + 10), (0, 0, 255), 2)
        # 将鼠标移动到检测框的中心
        # pyautogui.moveTo(center_x, center_y)
    cv.imshow("YOLOv5 Detection", screenshot)

if __name__ == "__main__":
    # 识别的视频源
    app_name = "Google Chrome"  # 待识别程序
    # 程序所在当前屏幕位置
    window_info = find_app_window(app_name)
    print(f"{app_name} 的左上角坐标和宽高是: {window_info}")

    # 检查是否有目标程序
    if window_info:
        # 模型文件路径
        model_path = "/Users/jiangsai/Desktop/test/yolov5/weights/yolov5s.pt"
        # 设置置信度阈值
        conf_thres = 0.5
        # 加载yolo模型
        yolo_model = load_model(model_path, conf_thres)
        # 当前屏幕坐标和分辨率的缩放比例
        scaling_factor = get_scaling_factor()
        while True:
            x, y, w, h = window_info
            # 获取目标程序的实时截图
            app_screenshot = capture_screen(x, y, w, h)
            detect_and_display(yolo_model, app_screenshot, scaling_factor)
            # 按'q'键跳出循环
            if cv.waitKey(1) & 0xFF == ord("q"):
                break
    else:
        print(f"{app_name} 没找着呢")
    cv.destroyAllWindows()
```

