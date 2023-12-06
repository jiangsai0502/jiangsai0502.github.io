###### 教程

> * [YOLOv5 40分钟训练自定义模型](https://www.bilibili.com/video/BV13G4y1W75c)
> * [手把手带你实战 YOLOv5](https://github.com/zyds/yolov5-code)

#### 环境搭建

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

#### 预制模型检测

1. 终端切换到 `yolov5` 源码目录

   ```bash
   python detect.py --weights "./weights/yolov5s.pt" --source 0 --conf 0.25 --view-img
   ```

   * 必须参数

     > 1. `--weights` ：执行检测的模型文件
     > 2. `--source` ：待识别的素材文件
     >    * `default=0` ：识别摄像头
     >    * `default="screen"` ：识别屏幕
     >    * `default="/Users/jiangsai/Desktop/Sai"` ：识别本地文件夹内的视频和图片
     >    * `default="/Users/jiangsai/Desktop/Sai/jump.mp4"` ：识别本地视频
     >    * `default="/Users/jiangsai/Desktop/Sai/people.jpg"` ：识别本地图片
     >    * `default="https://baidu.rudon.cn/img/bd.png"` ：识别网络图片

   * 非必须参数

     > 1. `--conf-thres` ：置信度阈值，默认为 0.25，即置信度>0.25的结果都识别出来
     >
     >    ````bash
     >    python detect.py --weights "./weights/yolov5s.pt" --source "data/images/people_car.jpg" --conf 0.25
     >    ````
     >
     >    * yolo 有两个阈值参数：`--conf-thres` 越小越宽松，识别结果越多；`--iou-thres` 越大越宽松，识别结果越多
     >
     > 2. `--classes` ：要识别的类别 （必须来自 `data/coco128.yaml`的 `names` 中）
     >
     >    ```bash
     >    # Classes 即要检测的类名
     >    names:
     >      0: person
     >      1: bicycle
     >      2: car
     >      ……
     >    ```
     >
     >    * 指定识别类别：只识别第0和第2个类别，即 person 和 bus
     >
     >      ```bash
     >      python detect.py --weights "./weights/yolov5s.pt" --source "data/images/people_car.jpg" --classes 0 2
     >      ```
     >
     >    * 不指定识别类别：不填写该参数，凡是 `data/coco128.yaml` 文件中的类别全都识别
     >
     > 3. `--view-img` ：实时显示检测结果
     >
     >    ```bash
     >    python detect.py --weights "./weights/yolov5s.pt" --source "data/images/people_car.jpg" --view-img
     >    ```

2. 结果保存在`./runs/detect` 目录

#### 模型训练

1. 终端切换到 `yolov5` 源码目录

   ```bash
   python train.py --weights "./weights/yolov5s.pt" --source 0 --conf 0.25 --view-img
   python train.py --weights "./weights/yolov5s.pt" --data "./data/data1201.yaml"
   ```

   * 必须参数

     > 1. `--weights` ：执行训练的模型文件
     >
     > 2. `--data` ：数据集配置文件，包含训练集和验证集的路径、类别
     >
     >    > 将 `./data/coco128.yaml` 原地复制一份，改名为 `data1201.yaml`
     >
     >    ```yaml
     >    path: /Users/jiangsai/Desktop/try/Yolo_Label/YOLO_Data/  # （每次都变）YOLO_Data的绝对路径
     >    train: images/train/  # （不变）训练集图片的相对path的路径
     >    val: images/val/  # （不变）验证集图片的相对path的路径
     >    test: # （不变）留空
     >    
     >    # Classes 必须 「xml 转 txt」的类名顺序一致
     >    names:
     >    0: red
     >    1: black
     >    ```

   * 非必须参数

     > 1. `--name`：本次训练的名字，用于保存训练过程中生成的模型文件、日志文件
     >
     >    ```bash
     >    python train.py --weights "./weights/yolov5s.pt" --data "./data/data1201.yaml" --name "result1206"
     >    ```
     >
     >    > 训练结果保存在`./runs/train/result1206/weights` 目录，一般使用训练出的最优模型 `best.pt`
     >
     > 2. `--batch`：（一般不修改）默认每次训练16张图像。增大数量可能提高训练速度和准确性，但会增加内存/显存压力
     >
     >    ```bash
     >    python train.py --weights "./weights/yolov5s.pt" --data "./data/data1201.yaml" --name "result1206" --batch 32
     >
     > 3. `--epochs 50`：（一般不修改）默认训练100轮数。一般可改为100-300，但当待训练图片不足以支撑过多轮训练时，强行提高数量，会有过拟合的风险
     >
     >    ```bash
     >    python train.py --weights "./weights/yolov5s.pt" --data "./data/data1201.yaml" --name "result1206" --epochs 200

2. 结果保存在`./runs/train` 目录

----

#### python脚本检测图片

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

>`torch.hub.load("./", "custom", path="./weights/yolov5s", source="local")`
>
>1. `"./"` ：「固定写法」`yolo V5` 源码目录（目录里的 `hubconf.py` 定义了如何加载模型）
>2. `"custom"` ：「固定写法」声明使用自定义模型
>3. `path="./weights/yolov5s"` ：「固定写法」模型文件的路径
>4. `source="local"` ：「固定写法」从本地加载模型

#### python脚本检测视频

```python
import cv2
import torch

def process_and_save_video(cap, model, out):
    ret, frame = cap.read()
    if not ret:
        return  # 视频结束或出错

    # 对帧进行预测
    results = model(frame)

    # 打印预测结果
    print(results.pred)

    # 获取预测后的帧
    frame_pred = results.render()[0]

    # 写入处理后的帧
    out.write(frame_pred)


if __name__ == "__main__":
    # 加载模型
    model = torch.hub.load("./", "custom", path="./runs/train/exp2/weights/best.pt", source="local")

    # 打开视频
    video_path = "/Users/jiangsai/Desktop/box.mp4"
    cap = cv2.VideoCapture(video_path)

    # 获取视频的基本参数
    frame_width = int(cap.get(3))
    frame_height = int(cap.get(4))
    fps = cap.get(cv2.CAP_PROP_FPS)

    # 定义 VideoWriter 对象
    save_path = "/Users/jiangsai/Desktop/box1.mp4"
    fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # 或者使用 'XVID'
    out = cv2.VideoWriter(save_path, fourcc, fps, (frame_width, frame_height))

    # 检查是否成功打开视频文件
    if not cap.isOpened():
        print("Error: Could not open video.")
        exit()

    # 处理视频的每一帧
    while True:
        process_and_save_video(cap, model, out)

    # 释放资源
    cap.release()
    out.release()
```

