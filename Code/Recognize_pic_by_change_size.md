> 金字塔算法：缩放物品图片的尺寸进行匹配

> 在给定的搜索图像中，使用多尺度模板匹配方法，对一个文件夹中的多个模板图像进行匹配，并将匹配结果在搜索图像上标注出来
>
> 1. `multi_scale_template_matching` 函数：并在一个搜索图像中查找一个模板图像的最佳匹配
>    - 将模板图像和搜索图像转换为灰度图像，以便进行模板匹配
>    - 遍历一系列不同的缩放尺度，对模板图像进行缩放
>    - 对每个缩放后的模板图像在搜索图像上进行模板匹配
>    - 找到每个尺度下的最大匹配值和其位置，并记录最佳匹配
>    - 返回最佳匹配的相关信息，包括最大匹配值、位置、缩放尺度以及模板图像的宽度和高度
> 2. `match_templates_in_folder` 函数：在给定的文件夹中遍历多个模板图像，并在搜索图像上查找它们的匹配
>    - 加载搜索图像
>    - 遍历模板文件夹中的每个模板图像
>    - 加载每个模板图像，并查找最佳匹配
>      - 若找到最佳匹配，则在搜索图像上绘制匹配的矩形框，并标注模板名和最大匹配值
>    - 显示带有匹配结果的搜索图像，并等待用户按下任意键后关闭

```python
import cv2, os
import numpy as np


# 多尺度模板匹配函数
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
        if resized_template.shape[0] > search_image_gray.shape[0] or resized_template.shape[1] > search_image_gray.shape[1]:
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


# 在给定文件夹中的模板图像与搜索图像进行匹配
def match_templates_in_folder(templates_folder, search_image_path):
    # 从文件加载搜索图像
    search_image = cv2.imread(search_image_path)
    if search_image is None:
        print("搜索图像未能成功加载")
        return
    # 遍历模板文件夹中的每个模板图像
    for template_name in os.listdir(templates_folder):
        # 构建模板图像的完整路径
        template_path = os.path.join(templates_folder, template_name)
        # 检查路径是否指向文件（而不是子文件夹等）
        if os.path.isfile(template_path):
            # 从文件加载模板图像
            template = cv2.imread(template_path)
            if template is None:
                print(f"模板图像 {template_name} 未能成功加载")
                continue
            # 使用多尺度模板匹配函数查找最佳匹配
            best_match = multi_scale_template_matching(template, search_image)
            # 如果找到了最佳匹配
            if best_match is not None:
                # 获取匹配的相关信息
                max_val, max_loc, scale, t_width, t_height = best_match
                # 计算匹配矩形的左上角和右下角坐标
                top_left = (int(max_loc[0]), int(max_loc[1]))
                bottom_right = (int(max_loc[0] + t_width), int(max_loc[1] + t_height))
                # 在搜索图像上绘制匹配矩形
                cv2.rectangle(search_image, top_left, bottom_right, (0, 0, 255), 4)
                # 获取模板名称并添加到匹配框上
                template_name = template_name.split(".")[0]  # 去掉文件扩展名
                text = f"{template_name} ({max_val:.2f})"
                cv2.putText(search_image, text, (top_left[0], top_left[1] - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 255), 2)

    cv2.imshow("Template Matches", search_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    templates_folder = "/Users/jiangsai/Desktop/test/a"  # 模板文件夹
    search_image_path = "/Users/jiangsai/Desktop/test/2.jpeg"  # 搜索图像

    # 调用函数，执行匹配并在找到的矩形框上标注模板文件名
    match_templates_in_folder(templates_folder, search_image_path)
```