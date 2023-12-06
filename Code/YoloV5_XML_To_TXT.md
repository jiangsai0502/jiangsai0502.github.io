###### Yolo V5 PascalVOC xml 转 txt

> 将 `labelImg` 标注软件标注的XML标注文件转换成YOLO可识别的txt格式，并将图片和txt分配到训练集和验证集目录中

```py
import xml.etree.ElementTree as ET
import os
import random
from shutil import copyfile


def convert(size, box):
    """将边界框的坐标从VOC格式转换为YOLO格式。VOC格式使用左上角和右下角的坐标，而YOLO格式使用边界框的中心点和宽高"""
    # 计算宽高的归一化因子
    dw = 1.0 / size[0]
    dh = 1.0 / size[1]
    # 计算中心点坐标
    x = (box[0] + box[1]) / 2.0
    y = (box[2] + box[3]) / 2.0
    # 计算宽度和高度
    w = box[1] - box[0]
    h = box[3] - box[2]
    # 将中心点坐标和尺寸归一化到(0, 1)范围内
    x = x * dw
    w = w * dw
    y = y * dh
    h = h * dh
    return (x, y, w, h)


def convert_annotation(image_path, output_dir):
    """读取VOC格式的XML标注文件，将其中的边界框坐标转换为YOLO格式，并将转换后的标注保存到文本文件中"""
    # 从图片路径获取文件名，并构造XML和TXT文件的路径
    file_name, _ = os.path.splitext(os.path.basename(image_path))
    xml_file = os.path.join(xml_dir, f"{file_name}.xml")
    txt_file = os.path.join(output_dir, f"{file_name}.txt")

    try:
        # 打开XML文件并读取内容
        with open(xml_file) as in_file, open(txt_file, "w") as out_file:
            tree = ET.parse(in_file)
            root = tree.getroot()
            size = root.find("size")
            w = int(size.find("width").text)
            h = int(size.find("height").text)

            # 遍历XML中的每个对象
            for obj in root.iter("object"):
                difficult = obj.find("difficult").text
                cls = obj.find("name").text
                # 过滤掉不在目标类别中或标记为难以识别的对象
                if cls not in classes or int(difficult) == 1:
                    continue
                cls_id = classes.index(cls)
                # 读取边界框坐标并转换为YOLO格式
                xmlbox = obj.find("bndbox")
                b = (
                    float(xmlbox.find("xmin").text),
                    float(xmlbox.find("xmax").text),
                    float(xmlbox.find("ymin").text),
                    float(xmlbox.find("ymax").text),
                )
                bb = convert((w, h), b)
                # 将转换后的坐标写入TXT文件
                out_file.write(f"{cls_id} {' '.join(map(str, bb))}\n")
    except Exception as e:
        print(f"Could not convert annotation for {file_name}: {e}")


def make_directory(path):
    """创建目录，如果目录不存在"""
    if not os.path.exists(path):
        os.makedirs(path)


def prepare_directories(base_dir):
    """准备必要的文件夹结构"""
    directories = {
        "yolov5_images_train_dir": os.path.join(base_dir, "YOLO_Data/images/train/"),
        "yolov5_images_test_dir": os.path.join(base_dir, "YOLO_Data/images/val/"),
        "yolov5_labels_train_dir": os.path.join(base_dir, "YOLO_Data/labels/train/"),
        "yolov5_labels_test_dir": os.path.join(base_dir, "YOLO_Data/labels/val/"),
    }
    for directory in directories.values():
        make_directory(directory)
    return directories


def is_image_file(filename):
    """检查文件是否是图片"""
    # 添加支持的图片扩展名
    supported_extensions = [".jpg", ".jpeg", ".png", ".bmp"]
    return any(filename.lower().endswith(ext) for ext in supported_extensions)


def split_datasets(image_dir, XML_dir, directories, train_ratio=80):
    """将图片分配到训练集和验证集"""
    images = [img for img in os.listdir(image_dir) if is_image_file(img)]
    for img in images:
        image_path = os.path.join(image_dir, img)
        file_name, _ = os.path.splitext(img)
        xml_path = os.path.join(XML_dir, file_name + ".xml")
        label_path = os.path.join(directories["yolov5_labels_train_dir"], file_name + ".txt")
        prob = random.randint(1, 100)
        if prob <= train_ratio:
            # 训练集
            if os.path.exists(xml_path):
                convert_annotation(xml_path, directories["yolov5_labels_train_dir"])
                copyfile(image_path, os.path.join(directories["yolov5_images_train_dir"], img))
        else:
            # 验证集
            if os.path.exists(xml_path):
                convert_annotation(xml_path, directories["yolov5_labels_test_dir"])
                copyfile(image_path, os.path.join(directories["yolov5_images_test_dir"], img))


# 主逻辑
if __name__ == "__main__":
    ######### 设置项 #########
    classes = ["red", "black"]  # 所要识别的类
    TRAIN_RATIO = 80  # 表示训练集和验证集比例为：8:2
    Project_dir = "/Users/jiangsai/Desktop/aaa/"  # 项目目录
    ######### 设置项 #########

    # 固定不变项
    Workspace_dir = os.path.join(Project_dir, "Original_Data/")
    xml_dir = os.path.join(Workspace_dir, "Xmls/")
    image_dir = os.path.join(Workspace_dir, "Images/")
    directories = prepare_directories(Project_dir)
    split_datasets(image_dir, xml_dir, directories, TRAIN_RATIO)
```



