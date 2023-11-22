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


def match_templates_in_video(templates_root_folder, video_path):
    # 打开视频文件
    video = cv2.VideoCapture(video_path)

    if not video.isOpened():
        print("Error: Unable to open video.")
        return

    # 读取视频的每一帧
    while True:
        ret, frame = video.read()
        if not ret:
            break  # 如果没有帧了，就退出循环

        # 遍历根模板文件夹中的每个二级文件夹
        for folder_name in os.listdir(templates_root_folder):
            folder_path = os.path.join(templates_root_folder, folder_name)
            if os.path.isdir(folder_path):
                # 对当前二级文件夹中的模板进行匹配
                matches = match_template_in_folder(folder_path, frame)
                for best_match, matched_template_name in matches:
                    max_val, max_loc, scale, t_width, t_height = best_match
                    top_left = (int(max_loc[0]), int(max_loc[1]))
                    bottom_right = (int(max_loc[0] + t_width), int(max_loc[1] + t_height))
                    # 在当前帧上画出矩形框，并在矩形框上方标注二级文件夹名称
                    cv2.rectangle(frame, top_left, bottom_right, (0, 0, 255), 2)
                    cv2.putText(
                        frame,
                        folder_name,  # 标注文件夹名称
                        (top_left[0], top_left[1] - 10),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        0.5,
                        (0, 0, 255),
                        1,
                    )

        # 显示带有匹配结果的视频帧
        cv2.imshow("Template Matches", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):  # 如果按下'q'键，则退出
            break

    # 释放视频和关闭所有窗口
    video.release()
    cv2.destroyAllWindows()


# 设置根模板文件夹路径和视频路径
templates_root_folder = "/Users/jiangsai/Desktop/test/aa"  # 根模板文件夹
video_path = "/Users/jiangsai/Desktop/test/恐龙快打1.mp4"  # 视频文件路径

# 调用函数，在视频中执行匹配并在找到的矩形框上标注模板文件名
match_templates_in_video(templates_root_folder, video_path)
