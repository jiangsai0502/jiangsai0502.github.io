> 打地鼠

```python
import Quartz
from AppKit import NSWorkspace, NSScreen
import cv2
import numpy as np
import Quartz.CoreGraphics as CG
import pyautogui

def get_scaling_factor():
    """获取主屏幕的缩放因子，Retina屏幕通常为2"""
    scaling_factor = NSScreen.mainScreen().backingScaleFactor()
    return scaling_factor

def find_app_window(app_name):
    """获取目标程序窗口的信息"""
    workspace = NSWorkspace.sharedWorkspace()
    active_apps = workspace.runningApplications()
    for app in active_apps:
        # 模糊查找运行中的所有应用名称，用于调试
        if "sub" in app.localizedName().lower():
            print(app.localizedName())
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

def perform_template_matching(screenshot, template):
    """执行模板匹配并返回最大匹配值和位置"""
    # 1、将目标程序的实时截图转换为灰度图，因为模板匹配不需要颜色信息，而且灰度图处理速度更快
    ss_gray = cv2.cvtColor(app_screenshot, cv2.COLOR_BGR2GRAY)
    # 2、将待搜索的模板图像也转换为灰度图
    si_gray = cv2.cvtColor(search_image, cv2.COLOR_BGR2GRAY)
    # 3、对模板和目标程序的实时截图进行模板匹配
    match_result = cv2.matchTemplate(si_gray, ss_gray, cv2.TM_CCOEFF_NORMED)
    # 4、找到最大匹配值和其位置
    _, max_val, _, max_loc = cv2.minMaxLoc(match_result)
    si_w, si_h = si_gray.shape[::-1]  # 模板图像的宽、高
    print(f"最大匹配值: {max_val}")
    return max_val, max_loc, si_w, si_h  # 返回匹配值、位置和模板宽高

def highlight_and_click_match(screenshot, max_val, max_loc, t_w, t_h, scaling_factor, window_position):
    """在匹配成功的区域绘制边框和中心点，并执行点击操作"""
    # 1. 绘制边框：在目标程序的实时截图中，画出模板匹配成功的区域的边框
    top_left = max_loc  # 左上角坐标（模板相对于目标程序窗口）
    bottom_right = (top_left[0] + t_w, top_left[1] + t_h)  # 右下角坐标（模板相对于目标程序窗口）
    cv2.rectangle(app_screenshot, top_left, bottom_right, (0, 255, 0), 2)
    # 2、绘制边框：在目标程序的实时截图中，画出模板匹配成功的区域的中心点坐标
    center_x = top_left[0] + t_w // 2  # 左上角坐标（中心点相对于目标程序窗口）
    center_y = top_left[1] + t_h // 2  # 右下角坐标（中心点相对于目标程序窗口）
    #   画出中心点四周的小框
    cv2.rectangle(app_screenshot, (center_x - 10, center_y - 10), (center_x + 10, center_y + 10), (0, 0, 255), 2)
    # 3、点击中心点：中心点坐标转换为全屏幕坐标后，点击
    screen_x = x + center_x // scaling_factor
    screen_y = y + center_y // scaling_factor
    pyautogui.click(screen_x, screen_y)

if __name__ == "__main__":
    # 待识别程序
    app_name = "Google Chrome"
    # 程序所在当前屏幕位置
    window_info = find_app_window(app_name)
    print(f"{app_name} 的左上角坐标和宽高是: {window_info}")
    # 当前屏幕坐标和分辨率的缩放比例
    scaling_factor = get_scaling_factor()
    # 待匹配到的图片
    search_image_path = "/Users/jiangsai/Desktop/test/1.png"
    search_image = cv2.imread(search_image_path)

    if window_info and search_image is not None:
        while True:
            x, y, w, h = window_info
            # 1、获取目标程序的实时截图
            app_screenshot = capture_screen(x, y, w, h)
            # 2、对实时截图进行模板匹配
            max_val, max_loc, si_w, si_h = perform_template_matching(app_screenshot, search_image)
            if max_val > 0.8:  # 匹配成功
                # 3、框住匹配结果并点击
                highlight_and_click_match(app_screenshot, max_val, max_loc, si_w, si_h, scaling_factor, window_info)
            # 4、显示处理后的实时截图
            cv2.imshow("Screenshot", app_screenshot)
            # 按下 'q' 键跳出循环。
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    else:
        print(f"{app_name} not found or no accessible window.")
    cv2.destroyAllWindows()
```

* 获取所有运行的桌面程序名称

  ```py
  from AppKit import NSWorkspace, NSApplicationActivationPolicyRegular
  
  workspace = NSWorkspace.sharedWorkspace()
  active_apps = workspace.runningApplications()
  for app in active_apps:
      # 只列出前台运行的应用程序
      if app.activationPolicy() == NSApplicationActivationPolicyRegular:
          app_name = app.localizedName()
          print(app_name)

* 获取所有屏幕缩放因子

  ```python
  from AppKit import NSScreen
  
  def get_screens_info():
      screens_info = []
      screens = NSScreen.screens()
      for screen in screens:
          info = screen.deviceDescription()
          display_id = info.get("NSScreenNumber", "Unknown")
          scaling_factor = screen.backingScaleFactor()
          screen_info = {"Display ID": display_id, "Scaling Factor": scaling_factor, "Device Description": info}
          screens_info.append(screen_info)
      return screens_info
  
  # 打印所有屏幕的信息
  all_screens_info = get_screens_info()
  for index, screen_info in enumerate(all_screens_info):
      print(f"屏幕 {index+1}:")
      for key, value in screen_info.items():
          print(f"{key}: {value}")
  ```

  >* Mac的Retina屏幕像素密度较高，在屏幕坐标和实际像素坐标之间存在一个缩放因子，通常这个因子是2。如，屏幕坐标(100, 100)对应Retina屏幕的实际像素坐标是(200, 200)
  >
  >* Quartz API获取屏幕截图时，返回的坐标基于实际像素点，无需缩放，而pyautogui获取屏幕截图时，返回的坐标基于屏幕坐标的，需要缩放2倍
