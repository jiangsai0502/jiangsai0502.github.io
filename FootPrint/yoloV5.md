###### 教程

> * [YOLOv5 40分钟训练自定义模型](https://www.bilibili.com/video/BV13G4y1W75c)
> * [手把手带你实战 YOLOv5](https://github.com/zyds/yolov5-code)

##### 环境搭建

1. 源码

   ```bash
   cd /Users/jiangsai/Desktop
   
   git clone https://github.com/ultralytics/yolov5.git
   
   cd /Users/jiangsai/Desktop/yolov5
   
   conda create -n yolov5 python=3.10
   
   conda activate yolov5
   
   pip install -r requirements.txt
   
   mkdir /Users/jiangsai/Desktop/yolov5/weights
   ```

2. 预制模型

   >`yolov5/models` 目录有4个模型：s > m > l > x，精度越来越高，速度越来越慢
   >
   >`https://github.com/ultralytics/yolov5/releases/download/v7.0/yolov5s.pt`
   >
   >将 `yolov5s.pt` 模型放入 `/Users/jiangsai/Desktop/yolov5/weights`

3. 

##### yoloV5训练 & 识别

###### 下载模型

> ```bash
> 
> ```
>
> >

###### 使用训练好的预制模型

> 1. 安装依赖包
>
>    ```bash
>    // 进入模型目录
>    cd yolov5
>    // 安装依赖包
>    pip install -r requirements.txt
>    ```
>
> 2. 设置 `detect.py`
>
>    ```python
>    def parse_opt():
>        # 执行识别的模型文件的路径
>        parser.add_argument("--weights", nargs="+", type=str, default="weights/yolov5s.pt", help="model path or triton URL")
>        # 识别素材文件的路径
>        # 识别图片：default="./data/images"
>        # 识别视频：default="/Users/jiangsai/Desktop/test/jump boy.mp4"
>        # 识别摄像头：default=0
>        parser.add_argument("--source", type=str, default="./data/images", help="file/dir/URL/glob/screen/0(webcam)")
>        # 置信度阈值：即 >default=0.25的结果都识别出来
>        parser.add_argument("--conf-thres", type=float, default=0.25, help="confidence threshold")
>    ```
>
>    > #yolo 检测中有两个阈值参数，一般使用--conf-thres 比较好理解，--iou-thres 太大时容易出现一个目标多个检测框，太小时容易出现检测不到
>
> 3. vscode终端切换到`/Users/jiangsai/Desktop/test/yolov5/` 目录后， 执行 `detect.py`
>
> 4. 识别结果保存在`yolov5/runs/detect` 目录
>
> | `view_img` | 显示结果。如果启用，将在检测时显示窗口。 | `--view-img`                       |
> | ---------- | ---------------------------------------- | ---------------------------------- |
> | `classes`  | 过滤类别。按类别ID过滤检测结果。         | `--classes 0` 或 `--classes 0 2 3` |
> | `project`  | 保存结果的项目目录。                     | `--project runs/detect`            |
> | `name`     | 保存结果的子目录名。                     | `--name exp`                       |

###### 自己训练模型

> 教程：[文字](https://blog.csdn.net/weixin_46046179/article/details/129639551)    [视频](https://www.bilibili.com/video/BV1f44y187Xg)   [yolo桌面软件](https://gitee.com/song-laogou/yolov5-mask-42)
>
> 1. 预备训练图片
>
>    ```bash
>    ├── XML_to_TXT.py
>    └── XML_to_TXT_Project/
>        └── Original_XML_Images/
>            ├── Images/
>            │    ├── 1.png
>            │    └── 2.png
>            └── xml_of_Images/
>    ```
>
>    > 目录必须是这个结构
>    >
>    > 1. `XML_to_TXT.py` 是[脚本](#`XML_to_TXT.py`)，后面会用到
>    > 2. `/XML_to_TXT_Project/Original_XML_Images/Images/` 目录里放的是要训练的图片
>    > 3. `/XML_to_TXT_Project/Original_XML_Images/xml_of_Images/` 目录是空的，用于后续标注时放的xml文件
>
> 2. 标注软件
>
>    ```bash
>    // 安装标注软件
>    pip install labelImg
>    // 启动标注软件
>    labelImg
>    ```
>
>    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311240027760.png)
>
>    > 1. `打开目录`：打开`/XML_to_TXT_Project/Original_XML_Images/Images/` 目录
>    > 2. `改变存放目录`：打开`/XML_to_TXT_Project/Original_XML_Images/xml_of_Images/` 目录
>    > 3. `PascalVOC`：标注为xml文件
>    > 4. `创建区块`：框选目标区域
>    > 5. `保存`：保存xml文件到 `改变存放目录`
>
> 3. 跑`XML_to_TXT.py` [脚本](#`XML_to_TXT.py`)
>
>    > `classes = ["Yellow", "Red"]`：改为框选的目标名称
>    >
>    > 跑完脚本后的目录
>    >
>    > ```bash
>    > ├── XML_to_TXT.py
>    > └── XML_to_TXT_Project/
>    >  ├── Original_XML_Images/
>    >  │    ├── Images/
>    >  │    │    ├── 1.png
>    >  │    │    └── 2.png
>    >  │    └── xml_of_Images/
>    >  │         ├── 1.xml
>    >  │         └── 2.xml
>    >  └── YOLO_Data/
>    >      ├── images/
>    >      │    ├── train/
>    >      │    │    └── 1.png
>    >      │    └── val/
>    >      │         └── 2.png
>    >      └── labels/
>    >          ├── train/
>    >          │    └── 1.txt
>    >          └── val/
>    >               └── 2.txt
>    > ```
>
> 4. 新增本项目的YOLO配置文件
>
>    > 1. 将 `YOLO_Data` 目录copy到 `yolov5` 目录下，即与 `train.py` 和 `detect.py` 同级目录
>    >
>    > 2. 将 `/data/VOC.yaml` 复制一份，改名为 `will.yaml`
>    >
>    >    ```yaml
>    >    # 相对路径：vscode左侧资源管理器 - 右键「复制相对路径」
>    >    path: /Users/jiangsai/Desktop/test/yolov5/
>    >    train: YOLO_Data/images/train/  # 相对于path的训练集路径
>    >    val: YOLO_Data/images/val/  # 相对于path的验证集路径
>    >    test: # 如果没有测试集可以留空
>    >    ```
>    >
>    >    ```yaml
>    >    # Classes
>    >    names:
>    >      0: Yellow
>    >      1: Red
>    >    ```
>    >
>    >    > `["Yellow", "Red"]`：框选的目标名称
>    >
>    > 3. 将 `/models/yolov5s.yaml` 复制一份，改名为 `yolov5s_will.yaml`
>    >
>    >    > 本项目使用的是 yolov5s.pt 这个训练模型，若用别的模型，则复制改名别的yaml文件
>    >
>    >    ```yaml
>    >    nc: 2  # number of classes
>    >    ```
>    >
>    >    > 2 是框选的目标名称数量
>
> 5. 开始训练
>
>    1. 设置 `train.py`
>
>       ```python
>       def parse_opt(known=False):
>           # 执行训练的模型文件的路径
>           parser.add_argument('--weights', type=str, default='weights/yolov5s.pt', help='initial weights path')
>           # 执行训练的模型配置文件的路径
>           parser.add_argument('--cfg', type=str, default='models/yolov5s_will.yaml', help='model.yaml path')
>           # 训练素材配置文件的路径
>           parser.add_argument('--data', type=str, default='data/will.yaml', help='dataset.yaml path')
>           # 模型的训练轮次 300 轮
>           parser.add_argument('--epochs', type=int, default=100, help='total training epochs')
>           # 单次图片处理数量
>           parser.add_argument('--batch-size', type=int, default=16, help='total batch size for all GPUs, -1 for autobatch')
>       ```
>
>    2. vscode终端切换到`/Users/jiangsai/Desktop/test/yolov5/` 目录后， 执行 `train.py`
>
>    3. 另开一个终端切换到`/Users/jiangsai/Desktop/test/yolov5/` 目录后，执行 `tensorboard --logdir=runs/train` 可在浏览器查看训练过程
>
>    4. 训练结束后会在 `yolov5/runs/train/exp5/weights` 产生两个模型文件，最后一轮的模型和效果最好的模型，一般用效果最好的
>
> 6. 使用训练结果模型进行识别
>
>    切换到`/Users/jiangsai/Desktop/test/yolov5/` 目录
>
>    ```bash
>    // 调用训练结果模型检测视频
>    python detect.py --source "/Users/jiangsai/Desktop/test/aaaaa.mp4" --weights runs/train/exp5/weights/best.pt 
>    ```
>

###### `XML_to_TXT.py`

> 将 `labelImg` 标注软件标注的XML标注文件转换成YOLO可识别的txt格式，并将图片和txt分配到训练集和验证集目录中

```python
import xml.etree.ElementTree as ET
import os
import random
from shutil import copyfile

classes = ["hat", "arm"]  # 所要识别的类
TRAIN_RATIO = 80  # 表示训练集和验证集比例为：8:2


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
    Project_dir = "/Users/jiangsai/Desktop/test/data/XML_to_TXT_Project/"
    Workspace_dir = os.path.join(Project_dir, "Original_XML_Images/")
    xml_dir = os.path.join(Workspace_dir, "xml_of_Images/")
    image_dir = os.path.join(Workspace_dir, "Images/")

    directories = prepare_directories(Project_dir)
    split_datasets(image_dir, xml_dir, directories, TRAIN_RATIO)
```

