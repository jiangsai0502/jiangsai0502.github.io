#### 安装

1. 安装

   ```bash
   # 切换虚拟环境
   conda info --envs
   source activate py3.8
   # 安装 PyQt5
   pip install PyQt5 -i https://pypi.tuna.tsinghua.edu.cn/simple
   # 安装Qt Designer
   https://build-system.fman.io/qt-designer-download
   # 
   ```

   



#### 基础用法

```python
import sys
from PyQt5.QtWidgets import QApplication, QWidget,QLabel
from PyQt5 import QtGui, QtWidgets, QtCore
from PyQt5.QtGui import QPainter, QColor

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = QWidget()
    # 窗口大小：宽250px，高150px
    w.resize(300, 300)
    # 窗口位置：距离左上角，x轴300px，y轴500px
    w.move(500, 300)
    # 窗口标题为：Simple
    w.setWindowTitle('Simple')
    # 窗口背景色
    palette = QtGui.QPalette()
    palette.setColor(w.backgroundRole(), QColor(192,253,123))
    w.setPalette(palette)
    # 显示图片，在窗口w中新建一个label_img
    label_img = QLabel(w)
    label_img.setPixmap(QtGui.QPixmap('/Users/sai/Desktop/1.jpg'))
    label_img.setAlignment(QtCore.Qt.AlignCenter())
    # 显示文字，在窗口w中新建一个label_word
    label_word = QLabel(w)
    label_word.setText('这是个啥')
    label_word.move(100,20)

    # 显示窗口
    w.show()
    sys.exit(app.exec_())
```

