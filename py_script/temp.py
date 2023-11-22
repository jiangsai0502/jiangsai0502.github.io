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
                print(f"模板图像未能成功加载: {template_name}")
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
