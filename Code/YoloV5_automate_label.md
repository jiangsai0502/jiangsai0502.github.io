##### 半自动标注

> 思路
>
> * 步骤1：打标签：使用labelImg对 [0, 10%] 的图片，手工打 XML 标签
>
> * 步骤2：训练：使用预制模型 yolo5s.pt 训练 [0, 10%] 的图片，得到本项目模型 （best.pt）v_1
>
> * 步骤3：打标签：使用本项目模型 （best.pt）v_1 检测[10%, 20%] 的图片，生成标签文件
>
> * 步骤4：矫正标签：使用labelImg对 [10%, 20%] 的图片，手工矫正标签
>
> * 步骤5：训练：使用 **本项目模型 （best.pt）v_1**  训练[0, 20%] 的图片，得到本项目模型 （best.pt）v_2
>
>   > - **使用预制模型（yolov5s.pt）训练[0, 20%]的图片**：这相当于从头开始训练，忽略了之前训练的best.pt v_1模型。这种方法在v_1模型的性能不够好或者有显著偏差时比较合适。
>   > - **使用本项目模型（best.pt v_1）训练[0, 20%]的图片**：这是在已有模型的基础上进一步训练，也称为模型的迭代或微调。v_1模型已经有了不错的性能，这种方法更合适。
>
> * 重复步骤3-5

* ###### 步骤0：预备图片 / 标注软件

  1. 图片预备

     > [视频中抽帧](Code/ScreenShot_Camera_Video.md) 
     >
     > [自动化截帧 - 摄像头/本地视频](Code/ScreenShot_Camera_Video.md) 
     >
     > [自动化截帧 - 桌面程序](Code/ScreenShot_DesktopApp.md)

  2. 标注软件

     ```bash
     // 安装标注软件
     pip install labelImg
     // 启动标注软件
     labelImg
     ```

* ###### 步骤1：打标签

  1. LabelImg 手工打 XML 标签

     > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202312061036617.png)
     >
     > 1. `LabelImg设置`：自动保存、专家模式
     > 2. `打开目录`：存放 `待训练 [0, 10%] 的图片` 的目录
     > 3. `改变存放目录`：准备存放 `xml标签文件` 的目录
     > 4. `PascalVOC`：标注为 `xml文件`

  2. XML 标签 转 TXT 标签

     >1. 目录搭建
     >
     >   ```bash
     >   Any_Name/
     >       ├── XML_to_TXT.py
     >       └── Original_Data/
     >              ├── Images/
     >              │    ├── 1.png
     >              │    └── 2.png
     >              └── Xmls/
     >                   ├── 1.xml
     >                   └── 2.xml
     >   ```
     >
     >   > 目录 **必须** 是这个结构
     >   >
     >   > * `XML_to_TXT.py` 是[xml转txt脚本](Code/YoloV5_XML_To_TXT.md)
     >   > * 将要训练的图片，移至 `Any_Name/Original_Data/Images/`
     >   > * 将打标签生成的 `xml` 文件，移至 `Any_Name/Original_Data/Xmls/`
     >
     >2. xml 转 txt
     >
     >   > 教程：[文字](https://blog.csdn.net/weixin_46046179/article/details/129639551)    [视频](https://www.bilibili.com/video/BV1f44y187Xg)   [yolo桌面软件](https://gitee.com/song-laogou/yolov5-mask-42)
     >   >
     >   > [xml转txt脚本](Code/YoloV5_XML_To_TXT.md) 
     >   >
     >   > * `classes=["red", "black"]` ：`class` 为 `LabelImg` 标注的类名，顺序非常重要，`"red"`是 0，`"black"` 是1
     >   >
     >   > * 跑完脚本后的目录如下，其中 `YOLO_Data` 目录在步骤2可用
     >   >
     >   > ```bash
     >   > Any_Name/
     >   >     ├── XML_to_TXT.py
     >   >     ├── Original_Data/
     >   >     │    ├── Images/
     >   >     │    │    ├── 1.png
     >   >     │    │    └── 2.png
     >   >     │    └── Xmls/
     >   >     │         ├── 1.xml
     >   >     │         └── 2.xml
     >   >     └── YOLO_Data/
     >   >       ├── images/
     >   >       │    ├── train/
     >   >       │    │    └── 1.png
     >   >       │    └── val/
     >   >       │         └── 2.png
     >   >       └── labels/
     >   >           ├── train/
     >   >           │    └── 1.txt
     >   >           └── val/
     >   >                └── 2.txt
     >   > ```

* ###### 步骤2：训练

  ```bash
  # 切换到 yoloV5 源码根目录
  cd /Users/jiangsai/Desktop/yolov5
  # 训练
  python train.py --weights "./weights/yolov5s.pt" --data "./data/data1201.yaml"
  ```

  > 1. `--weights`：（必须修改）要使用的训练模型。第一轮用`yolov5s.pt` ，之后每轮都用上一轮训练出的 `best.pt`
  >
  > 2. `--data`：（必须新建）数据集配置文件，包含训练集和验证集的路径、类别
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
  >   1: black
  >    ```

* ###### 步骤3：打标签

  1. 目录搭建

     ```bash
     Any_Name/
         └── 1_original_pic/
                ├── 1.png
                └── 2.png
     ```

     > 目录 **必须** 是这个结构
     >
     > * `Any_Name/1_original_pic/` ：存放将要训练的[10%, 20%] 的图片

  2. 模型自动打 XML 标签

     1. VSCode新建终端，`cd 命令` 切换到 yoloV5 源码根目录

     2. 在  yoloV5 源码根目录，创建 `Detect_Save_xml.py`  

        > [检测图片并生成 xml 的脚本](Code/YoloV5_XML_To_TXT.md) 
        >
        > 1. `classes=["red", "black"]` ：`class` 顺序非常重要，`"red"`是 0，`"black"` 是1
        > 2. `Model_path="/xxx/xxx/best.pt"` ：模型文件
        > 3. `Project_dir="/xxx/xxx/labels"` ：项目目录

     3. 跑完脚本后的目录如下

        ```bash
        Any_Name/
        ├── 1_original_pic/
        │    ├── 1.png
        │    └── 2.png
        ├── 2_yolo_xml/
        │    ├── 1.xml
        │    └── 2.xml
        └── 3_draw_pic/
            ├── 1.png
            └── 2.png
        ```

        > * `Any_Name/2_yolo_xml/` ：存放检测生成的 xml 文件
        > * `Any_Name/3_draw_pic/` ：存放检测后画了标注框的图片

* ###### 步骤4：矫正标签

  1. LabelImg 手工矫正 XML 标签

     > 1. `打开目录`：`Any_Name/1_original_pic/`
     > 2. `改变存放目录`：`Any_Name/2_yolo_xml/`
     > 3. `PascalVOC`：标注为 `xml文件`

  2. XML 标签 转 TXT 标签（见步骤1）

* ###### 步骤5：训练

  * （见步骤2）

* ###### 步骤6：重复3-5