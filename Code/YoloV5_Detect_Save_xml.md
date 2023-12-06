> 用自定义yoloV5模型检测图片，并导出Pascal VOC格式的xml文件

```py
import torch
import cv2 as cv
import os
import glob
import xml.etree.ElementTree as ET


def save_detection_to_xml(image_path, detections, output_folder_xml, classes):
    """将模型的检测结果保存为Pascal VOC格式的xml文件"""
    image_height, image_width, image_depth = cv.imread(image_path).shape

    # 创建XML文件的基本结构
    annotation = ET.Element("annotation")
    ET.SubElement(annotation, "folder").text = os.path.basename(os.path.dirname(image_path))
    ET.SubElement(annotation, "filename").text = os.path.basename(image_path)
    ET.SubElement(annotation, "path").text = image_path
    source = ET.SubElement(annotation, "source")
    ET.SubElement(source, "database").text = "Unknown"

    # 图像大小部分
    size = ET.SubElement(annotation, "size")
    ET.SubElement(size, "width").text = str(image_width)
    ET.SubElement(size, "height").text = str(image_height)
    ET.SubElement(size, "depth").text = str(image_depth)

    # 遍历检测结果并添加到XML
    for detection in detections:
        x1, y1, x2, y2, conf, cls_id = detection
        object_ = ET.SubElement(annotation, "object")
        ET.SubElement(object_, "name").text = classes[int(cls_id)]
        ET.SubElement(object_, "pose").text = "Unspecified"
        ET.SubElement(object_, "truncated").text = "0"
        ET.SubElement(object_, "difficult").text = "0"
        bndbox = ET.SubElement(object_, "bndbox")
        ET.SubElement(bndbox, "xmin").text = str(int(x1))
        ET.SubElement(bndbox, "ymin").text = str(int(y1))
        ET.SubElement(bndbox, "xmax").text = str(int(x2))
        ET.SubElement(bndbox, "ymax").text = str(int(y2))

    # 将创建的XML结构写入文件
    xml_file_path = os.path.join(output_folder_xml, os.path.basename(image_path).replace(".png", ".xml"))
    tree = ET.ElementTree(annotation)
    tree.write(xml_file_path)


def detect_and_draw(image_path, output_folder_img, output_folder_txt):
    """将模型的检测结果绘制到图像中"""
    # 读取图像
    img = cv.imread(image_path)
    # 进行检测
    results = model(img)
    detections = results.xyxy[0].cpu().numpy()
    # 绘制边界框和标签
    for detection in detections:
        x1, y1, x2, y2, conf, cls_id = detection
        label = model.names[int(cls_id)]
        conf_text = f"{conf:.2f}"
        cv.rectangle(img, (int(x1), int(y1)), (int(x2), int(y2)), (0, 255, 0), 2)
        cv.putText(img, f"{label} {conf_text}", (int(x1), int(y1) - 10), cv.FONT_HERSHEY_SIMPLEX, 0.9, (0, 255, 0), 2)
    # 保存图像
    cv.imwrite(os.path.join(output_folder_img, os.path.basename(image_path)), img)
    # 保存检测结果为 Pascalvoc的xml格式
    save_detection_to_xml(image_path, detections, output_folder_xml, classes)


if __name__ == "__main__":
    ######### 设置项 #########
    Model_path = "./runs/train/Day1206_01/weights/best.pt"  # 模型文件
    Project_dir = "/Users/jiangsai/Desktop/labels"  # 项目目录
    ######### 设置项 #########

    # 固定不变项
    input_folder_img = os.path.join(Project_dir, "1_original_pic/")  # 待检测图片目录
    output_folder_xml = os.path.join(Project_dir, "2_yolo_xml/")  # xml文件目录
    output_folder_img = os.path.join(Project_dir, "3_draw_pic/")  # 已检测绘制图片目录

    # 确保输出目录存在
    os.makedirs(input_folder_img, exist_ok=True)
    os.makedirs(output_folder_xml, exist_ok=True)
    os.makedirs(output_folder_img, exist_ok=True)

    # 加载模型
    model = torch.hub.load("./", "custom", path=Model_path, source="local")
    # 模型有两个类别：顺序非常重要，`"red"`是 0，`"black"` 是1
    classes = ["red", "black"]

    # 处理目录 A 中的所有图片
    image_formats = ["*.png", "*.jpg", "*.jpeg"]

    # 处理目录中的所有图片
    for img_format in image_formats:
        for image_path in glob.glob(input_folder_img + img_format):
            detect_and_draw(image_path, output_folder_img, output_folder_xml)
```

