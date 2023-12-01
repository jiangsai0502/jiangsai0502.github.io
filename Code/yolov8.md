https://www.bilibili.com/video/BV14h4y1v7Qw/?spm_id_from=333.788.recommend_more_video.0&vd_source=052b07ad0190d9dabdf1d78fda0168a7





###### 命令行检测

```bash
pip uninstall ultralytics
python
import ultralytics
# 检查Ultralytics YOLOv8版本号
ultralytics.checks()
```

###### python脚本检测

教程：https://www.bilibili.com/video/BV13V4y1S7MK

```bash
mkdir /Users/jiangsai/Desktop/SaiYolov8 && cd /Users/jiangsai/Desktop/SaiYolov8

conda create -n py310_yolov8 python=3.10

conda activate py310_yolov8

git clone https://github.com/ultralytics/ultralytics

cd ultralytics

mkdir /Users/jiangsai/Desktop/SaiYolov8/ultralytics/weights

# 下载 YOLOv8n：https://github.com/ultralytics/assets/releases/download/v0.0.0/yolov8n.pt
# 将 yolov8n.pt 放入 weights 目录

# 命令行用 yolo 命令测试一下检测图片，默认输出到 ./runs/detect/predict(.指当前目录 ultralytics)
yolo task=detect mode=predict model='./weights/yolov8n.pt' source='ultralytics/assets/bus.jpg'

pip install -e .  # 执行当前目录的 setup.py，1、为当前虚拟环境安装yolov8的依赖 2、yolo命令会使用本地修改的项目代码
```

```python
from ultralytics import YOLO
import cv2

model = YOLO("model.pt")
# 检测
# 摄像头
results = model.predict(source="0", show=True)
# 检测文件夹
results = model.predict(source="folder", show=True) # Display preds. Accepts all YOLO predict arguments
# 检测图片
im2 = cv2.imread("https://www.quickanddirtytips.com/wp-content/uploads/2022/05/ezgif.com-gif-maker-3.jpg")
results = model.predict(source=im2, save=True, save_txt=True)  # save predictions as labels
# 检测
```



```python
# python脚本训练
from ultralytics import YOLO

# Load a model
model = YOLO("yolov8n.yaml")  # build a new model from scratch
model = YOLO("yolov8n.pt")  # load a pretrained model (recommended for training)

# Use the model
model.train(data="coco128.yaml", epochs=3)  # train the model
metrics = model.val()  # evaluate model performance on the validation set
results = model("https://www.quickanddirtytips.com/wp-content/uploads/2022/05/ezgif.com-gif-maker-3.jpg")  # predict on an image
path = model.export(format="onnx")  # export the model to ONNX format
```

重要文件

1. `./engine/model.py`

   >命令行的 yolo 命令，无论检测、训练都是调用这个文件

   ```python
   # 找到 predict 函数，在函数中增加一句 print("Sai的代码注入了")
   def predict(self, source=None, stream=False, predictor=None, **kwargs):
       print("Sai的代码注入了")
   ```

   > 命令行用 yolo 命令测试一下检测图片，输出 「Sai的代码注入了」

   ```bash
   yolo task=detect mode=predict model='./weights/yolov8n.pt' source='ultralytics/assets/bus.jpg'
   ```

2. `./ultralytics/cfg/default.yaml`

   >  YOLOv8 模型训练和使用的默认配置文件，用于控制模型的训练、验证、预测









