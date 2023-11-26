import Quartz
from AppKit import NSWorkspace
import cv2
import numpy as np
import Quartz.CoreGraphics as CG
import pyautogui


def get_window_info(app_name):
    workspace = NSWorkspace.sharedWorkspace()
    active_apps = workspace.runningApplications()
    for app in active_apps:
        # 模糊查找运行中的应用名称
        if "sub" in app.localizedName().lower():
            print(app.localizedName())
        if app.localizedName() == app_name:
            app_pid = app.processIdentifier()
            window_info_list = Quartz.CGWindowListCopyWindowInfo(Quartz.kCGWindowListOptionOnScreenOnly, Quartz.kCGNullWindowID)
            for window_info in window_info_list:
                if window_info["kCGWindowOwnerPID"] == app_pid:
                    window_bounds = window_info["kCGWindowBounds"]
                    return (window_bounds["X"], window_bounds["Y"], window_bounds["Width"], window_bounds["Height"])


def capture_screen(x, y, width, height):
    # 创建一个 CGRect 结构体来表示捕获区域
    region = CG.CGRectMake(x, y, width, height)
    # 捕获指定区域的屏幕内容
    image_ref = CG.CGWindowListCreateImage(region, CG.kCGWindowListOptionOnScreenOnly, CG.kCGNullWindowID, CG.kCGWindowImageDefault)
    # 将捕获的内容转换为 numpy 数组
    width = CG.CGImageGetWidth(image_ref)
    height = CG.CGImageGetHeight(image_ref)
    bytes_per_row = CG.CGImageGetBytesPerRow(image_ref)
    pixel_data = CG.CGDataProviderCopyData(CG.CGImageGetDataProvider(image_ref))
    image = np.frombuffer(pixel_data, dtype=np.uint8).reshape((height, bytes_per_row // 4, 4))
    image = image[:, :width, :3]  # 去掉 alpha 通道
    return image


if __name__ == "__main__":
    app_name = "Google Chrome"
    bounds = get_window_info(app_name)
    print(f"{app_name} 的位置是: {bounds}")
    search_image_path = "/Users/jiangsai/Desktop/test/1.png"
    search_image = cv2.imread(search_image_path)

    if bounds:
        while True:
            x, y, width, height = bounds
            screenshot = capture_screen(x, y, width, height)
            cv2.imshow("Screenshot", screenshot)
            # 1、将模板图像转换为灰度图，因为模板匹配不需要颜色信息，而且灰度图处理速度更快
            ss_gray = cv2.cvtColor(screenshot, cv2.COLOR_BGR2GRAY)
            # 2、将待搜索的图像也转换为灰度图
            si_gray = cv2.cvtColor(search_image, cv2.COLOR_BGR2GRAY)
            # 3.3、对缩放后的模板和搜索图像进行模板匹配
            match_result = cv2.matchTemplate(si_gray, ss_gray, cv2.TM_CCOEFF_NORMED)
            # 3.4、从匹配结果中找到最大匹配值和其位置的中心点，并点击该位置

            # 找到最大匹配值和其位置
            _, max_val, _, max_loc = cv2.minMaxLoc(match_result)
            print(f"最大匹配值: {max_val}")

            # 0.8作为匹配阈值，可以根据实际情况调整
            if max_val > 0.8:
                # 计算模板图像的中心点
                si_gray_w, si_gray_h = si_gray.shape[::-1]
                center_x = max_loc[0] + si_gray_w // 2
                center_y = max_loc[1] + si_gray_h // 2

                # 转换为全屏幕坐标
                screen_x = x + center_x
                screen_y = y + center_y

                # 使用 pyautogui 点击该位置
                pyautogui.click(screen_x, screen_y)

            # 如果用户按下 'q' 键，则跳出循环。
            if cv2.waitKey(1) & 0xFF == ord("q"):
                break
    else:
        print(f"{app_name} not found or no accessible window.")
    cv2.destroyAllWindows()
