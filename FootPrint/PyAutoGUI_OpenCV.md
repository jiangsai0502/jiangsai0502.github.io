##### 每5秒检查一次屏幕，有目标就双击

```python
import pyautogui
import time
import cv2
import numpy as np

# 目标图像文件路径
target_image_path = "/Users/jiangsai/Desktop/Snipaste_2024-07-27_09-27-48.png"

# 加载目标图像
target_image = cv2.imread(target_image_path)

while True:
    # 截取当前屏幕
    screenshot = pyautogui.screenshot()

    # 将截图转换为OpenCV格式
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # 使用OpenCV的模板匹配功能查找目标图像
    result = cv2.matchTemplate(screenshot, target_image, cv2.TM_CCOEFF_NORMED)
    min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)

    # 设置匹配的阈值
    threshold = 0.8

    # 如果匹配度大于阈值，说明找到了目标图像
    if max_val >= threshold:
        # 获取目标图像中心点的位置
        target_center_x = max_loc[0] + target_image.shape[1] // 2
        target_center_y = max_loc[1] + target_image.shape[0] // 2

        # 移动鼠标到目标图像的中心点并点击，Mac的分辨率是屏幕的2倍，解法是坐标/2
        pyautogui.moveTo(target_center_x // 2, target_center_y // 2)
        pyautogui.doubleClick()
        print(f"点击了图像，位置：({target_center_x}, {target_center_y})")
        # break

    # 每5秒检查一次
    time.sleep(5)
    print(("继续检查..."))
```

