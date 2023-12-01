###### 教程

> * [YOLOv5 40分钟训练自定义模型](https://www.bilibili.com/video/BV13G4y1W75c)
> * [手把手带你实战 YOLOv5](https://github.com/zyds/yolov5-code)

##### 环境搭建

1. 下载源码、安装依赖、安装看板

   ```bash
   cd /Users/jiangsai/Desktop
   
   git clone https://github.com/ultralytics/yolov5.git
   
   cd /Users/jiangsai/Desktop/yolov5
   
   conda create -n yolov5 python=3.8
   
   conda activate yolov5
   
   pip install -r requirements.txt
   
   mkdir /Users/jiangsai/Desktop/yolov5/weights
   
   pip install tensorboard
   ```

2. 预制模型说明

   >`yolov5/models` 目录有4个模型：s > m > l > x，精度越来越高，速度越来越慢
   >
   >`https://github.com/ultralytics/yolov5/releases/download/v7.0/yolov5s.pt`
   >
   >将 `yolov5s.pt` 模型放入 `/Users/jiangsai/Desktop/yolov5/weights`

##### 预制模型检测

1. VSCode加载 `yolov5` 项目：`/Users/jiangsai/Desktop/yolov5`

2. VSCode终端切换到 `/Users/jiangsai/Desktop/yolov5` 目录

3. 使用 **`./detect.py`** 检测

   ```python
   def parse_opt():
       parser.add_argument("--weights", nargs="+", type=str, default="./weights/yolov5s.pt")
       parser.add_argument("--source", type=str, default="./data/images")
       parser.add_argument("--conf-thres", type=float, default=0.25)
       parser.add_argument("--classes", nargs="+", type=int)
       parser.add_argument("--project", default="./runs/detect")
       parser.add_argument("--name", default="exp")
       parser.add_argument("--view-img", action="store_true")
   ```

   * `"--weights"` ：执行检测的模型文件路径

   * `"--source"` ：待识别的素材文件路径

     * `default=0` ：识别摄像头
     * `default="screen"` ：识别屏幕
     * `default="/Users/jiangsai/Desktop/yolov5/Sai"` ：识别本地文件夹内的视频和图片
     * `default="/Users/jiangsai/Desktop/yolov5/Sai/jump.mp4"` ：识别本地视频
     * `default="/Users/jiangsai/Desktop/yolov5/Sai/people.jpg"` ：识别本地图片，网络图片也可

   * `"--conf-thres"` ：置信度阈值，`default=0.25` 即置信度>0.25的结果都识别出来

     * yolo 有两个阈值参数：`--conf-thres` 越小越宽松，识别结果越多；`--iou-thres` 越大越宽松，识别结果越多

   * `"--classes"` ：识别的类别

     * 类别文件：`data/coco128.yaml`

       ```yaml
       # Classes
       names:
         0: person
         1: bicycle
         2: car
         3: motorcycle
         4: airplane
         5: bus
       ```

     * 指定识别类别：`default=[0, 5]` 只识别第0和第5个类别，即 person 和 bus

       ```python
       parser.add_argument("--classes", nargs="+", type=int, default=[0, 5])
       ```

     * 不指定识别类别，凡是 `data/coco128.yaml` 文件中的类别全都识别

       ```python
       parser.add_argument("--classes", nargs="+", type=int)
       ```

   * `"--project"` ：所有检测结果的保存目录

   * `"--name"` ：每次检测结果的保存目录

   * `"--view-img"` ：

     * 若 `action="store_false"` 默认实时显示检测结果；但若在命令行加上 `--view-img` 则不实时显示检测结果
     * 若 `action="store_true"` 默认不实时显示检测结果；但若在命令行加上 `--view-img` 则实时显示检测结果

4. 识别结果保存在`yolov5/runs/detect` 目录

5. 使用 **自制脚本** 检测

   ```python
   import torch
   
   # 加载模型
   model = torch.hub.load("./", "custom", path="./weights/yolov5s", source="local")
   # 待识别数据
   recog_data = "./data/images/bus.jpg"
   # 开始识别
   recog_results = model(recog_data)
   # 展示识别结果
   recog_results.show()
   ```

   1. `torch.hub.load("./", "custom", path="./weights/yolov5s", source="local")`
      1. `"./"` ：「固定写法」`yolo V5` 源码目录（目录里的 `hubconf.py` 定义了如何加载模型）
      2. `"custom"` ：「固定写法」声明使用自定义模型
      3. `path="./weights/yolov5s"` ：「固定写法」模型文件的路径
      4. `source="local"` ：「固定写法」从本地加载模型

##### 自制模型检测

1. 图片准备

   > [自动化截帧 - 摄像头/本地视频](Code/ScreenShot_Camera_Video.md)
   >
   > [自动化截帧 - 桌面程序](Code/ScreenShot_DesktopApp.md)

   > 目录准备
   >
   > 1. `/Users/jiangsai/Desktop/material/images`： 存放待训练图片（必须叫 `images`）
   > 2. `/Users/jiangsai/Desktop/material/labels`： 存放标注文件（必须叫 `labels`）

2. 标注软件

   ```bash
   // 安装标注软件
   pip install labelImg
   // 启动标注软件
   labelImg
   ```

   ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202312011745248.png)

   > 1. 软件设置：自动保存、显示类别、专家模式
   > 2. `打开目录`：打开 `/Users/jiangsai/Desktop/material/images`
   > 3. `改变存放目录`：打开 `/Users/jiangsai/Desktop/material/labels`
   > 4. `yolo`：标注为 txt 文件
   > 5. `创建区块`：框选目标区域

   > 标注完成后  `/Users/jiangsai/Desktop/material/labels` 目录会生成与图片等量的 txt 文件，外加1个 classes.txt，里面是标注的类别 Red，Black
   >
   > ```
   > Red
   > Black
   > ```

3. 数据集拆分

   1. 当前目录

      ```
      material/
      ├── images/
      │     ├── screenshot_1.png
      │     └── screenshot_2.png
      └── labels/
          ├── classes.txt
          ├── screenshot_1.txt
          └── screenshot_2.txt
      ```

   2. 新建目录，并转移文件

      > `images` 目录新建 `train` 和 `val` 目录，将 80%的图片转移到 `train` ，剩余20% 到 `val`
      >
      > *  `train` ：训练集图片
      > *  `val` ：验证集图片
      >
      > `labels` 目录新建 `train` 和 `val` 目录，将 80%的 `同名txt` 转移到 `train` ，剩余20% 到 `val`
      >
      > *  `train` ：训练集标注文件，必须与训练集图片名称一一对应
      > *  `val` ：验证集标注文件，必须与验证集图片名称一一对应
      >
      > `labels` 目录的 `classes.txt` 转移到 `material` 目录

      ```
      material/
      ├── images/
      │    ├── train/
      │    │     ├── screenshot_1.png
      │    │     └── screenshot_2.png
      │    └── val/
      │         └── screenshot_3.png
      └── labels/
      │    ├── train/
      │    │     ├── screenshot_1.txt
      │    │     └── screenshot_2.txt
      │    └── val/
      │         └── screenshot_3.txt
      └── classes.txt
      ```

4. 使用 **`./train.py`** 训练

   ```python
   def parse_opt(known=False):
       parser = argparse.ArgumentParser()
       parser.add_argument('--weights', type=str, default='./weights/yolov5s.pt')
       parser.add_argument('--data', type=str, default='./data/data1201.yaml')
       parser.add_argument('--epochs', type=int, default=100)
   ```

   * `'--weights'` ：执行训练的模型文件路径

   * `'--data'` ：训练数据集的配置文件路径（存放训练数据集目录和训练类别）

     > 1. 将 `./data/coco128.yaml` 原地复制一份，改名为 `data1201.yaml`
     >
     >    ```bash
     >    path: /Users/jiangsai/Desktop/material/  # material的绝对路径
     >    train: images/train/  # 训练集图片的相对path的路径
     >    val: images/val/  # 验证集图片的相对path的路径
     >    test: 留空
     >    
     >    # Classes 必须与标注时生成 classes.txt 里的类别顺序一致
     >    names:
     >      0: Red
     >      1: Black
     >    ```

   * `--epochs` ：模型的训练轮次，`default=100` 即训练100 轮

5. 训练结果

   > 识别结果保存在`./runs/train` 目录，一般使用训练出的最优模型 `best.pt`

6. 查看训练过程

   > 切换到 `/Users/jiangsai/Desktop/yolov5` 源码目录
   >
   > `tensorboard --logdir=runs/train` 可在浏览器查看训练过程

7. 使用训练结果模型进行识别

   切换到`/Users/jiangsai/Desktop/yolov5/` 目录

   ```bash
   // 调用训练结果模型检测视频
   python detect.py --source "/Users/jiangsai/Desktop/box.mp4" --weights runs/train/exp2/weights/best.pt --view-img
   ```

   



##### 另一种训练标注方式

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
> 2. > 1. 标注软件
>    >
>    >    ```bash
>    >    // 安装标注软件
>    >    pip install labelImg
>    >    // 启动标注软件
>    >    labelImg
>    >    ```
>    >
>    >    ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202311240027760.png)
>    >
>    >    > 1. `打开目录`：打开`/XML_to_TXT_Project/Original_XML_Images/Images/` 目录
>    >    > 2. `改变存放目录`：打开`/XML_to_TXT_Project/Original_XML_Images/xml_of_Images/` 目录
>    >    > 3. `PascalVOC`：标注为xml文件
>    >    > 4. `创建区块`：框选目标区域
>    >    > 5. `保存`：保存xml文件到 `改变存放目录`
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

