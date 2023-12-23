##### 安装&设置

* 安装

  >教程[PySide6 QtDesigner教程](https://www.bilibili.com/video/BV1Wa41127fk) , [15分钟入门PySide6](https://www.bilibili.com/video/BV18F411W7y2)

  ```bash
  # 创建新环境 PySide6
  conda create -n PySide6 python=3.8
  conda activate PySide6
  # 安装
  pip install pyside6
  ```

* 设置VSCode

  ```python
  import os, subprocess
  
  # 获取当前虚拟环境的 Python 目录
  result = subprocess.run(["which", "python"], capture_output=True, text=True)
  python_path = result.stdout.strip()
  parts = python_path.split("/")  # 分割路径
  python_folder_path = "/".join(parts[:-2])  # 移除最后两个部分
  
  # 在目录中查找文件
  def find_file(root_folder, file_name):
      for root, dirs, files in os.walk(root_folder):
          if file_name in files:
              full_path = os.path.join(root, file_name)
              print(f"文件路径: {full_path}")
              return  # 如果只想找到第一个匹配的文件，就在这里返回
      print(f"{file_name} 文件没找到.")
  
  Designer = "Designer"
  pyside6_rcc = "pyside6-rcc"
  pyside6_uic = "pyside6-uic"
  find_file(python_folder_path, Designer)
  find_file(python_folder_path, pyside6_rcc)
  find_file(python_folder_path, pyside6_uic)
  # /Users/jiangsai/anaconda3/envs/PySide6/lib/python3.8/site-packages/PySide6/Designer.app/Contents/MacOS/Designer
  # /Users/jiangsai/anaconda3/envs/PySide6/bin/pyside6-rcc
  # /Users/jiangsai/anaconda3/envs/PySide6/bin/pyside6-uic
  ```

  * 安装插件 `Qt for Python`
  * 插件 右键扩展配置
    * `Qt For Python > Designer: Path`：粘贴上述程序输出的路径1
    * `Qt For Python > Rcc: Path`：粘贴上述程序输出的路径2
    * `Qt For Python > Uic: Path`：粘贴上述程序输出的路径3
  
* Qt designer设置

  > 修改视图模式：`Preferences-Appearance-User Interface Mode-Docked Window`

##### 常见控件

1. `QLabel `、`QLineEdit`、`QPushButton`

   > 登陆框：输入账号、密码，点击登陆，展示”登陆成功“

   * 使用Qt Designer 画界面

     > 资源管理器栏：右键 > Create Qt UI File (designer)
     >
     > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202312161413708.png)
     >
     > 1. 新建 `QWidget` > 拖入4个 `框架Frame` + 顶底2个 `纵向弹簧Horizontal Spacer` > `QWidget` 设为垂直布局
     >
     > 2. 每个`Frame` 中 放置对应功能的控件，如下
     >
     >    * 账号栏：拖入左右2个 `横向弹簧Vertical Spacer` + `标签label` + `单行文本框LineEdit` > `Frame` 设置为水平布局
     >
     >    * 密码栏：同上
     >    * 登录栏：`shortcut` 设为option + 5
     >    * 密码状态栏：同账号栏
     >
     > 3. 需要交互的控件全部语义化命名：`计算按钮` 、 `待输入数字框`、`结果标签`
     >
     > 4. 文件保存为 `first.ui`，自动编译生成 `frist_ui.py`

     * ###### 界面分离设计

       > `xxx.ui` 
       >
       > * Qt Designer创建的用户界面(UI)文件，控制窗口和元素的布局
       >
       > `xxx_ui.py`
       >
       > * 是 `xxx.ui` 编译成的Python文件，与之功能一样，是用Python代码控制窗口和元素的布局
       > * 每次保存 `xxx.ui` 时会自动重新编译并覆盖旧文件
       >
       > `xxx_main.py` 
       >
       > * 自行创建的主程序代码，是编写自定义代码、处理信号和槽、以及扩展UI功能的地方

   * 主程序代码

     ```python
     import sys
     from PySide6.QtWidgets import QApplication, QWidget
     from frist_ui import Ui_Form
     
     
     # 主窗口类
     class mainWindow(QWidget):
         def __init__(self):
             super(mainWindow, self).__init__()
             self.ui = Ui_Form()  # 创建UI对象
             self.ui.setupUi(self)  # 加载UI布局
             self.bind_event()  # 绑定事件
     
         # 绑定事件
         def bind_event(self):
             self.ui.account_lineEdit.textChanged.connect(lambda: print(self.ui.account_lineEdit.text()))
             self.ui.login_btn.clicked.connect(self.login)
     
         # 待绑定函数
         def login(self):
             account = self.ui.account_lineEdit.text()
             password = self.ui.password_lineEdit.text()
             if account == "admin" and password == "123456":
                 self.ui.login_status_label.setText("登录成功")
             else:
                 self.ui.login_status_label.setText("账号/密码错误，登录失败")
     
     
     if __name__ == "__main__":
         app = QApplication(sys.argv)  # 创建应用对象
         window = mainWindow()  # 创建主窗口对象
         window.show()  # 显示主窗口
         sys.exit(app.exec())  # 运行应用
     ```

     > * `标签 QLabel`
     >   * `setText(text)`：设置标签的文本
     >   * `text()`：获取标签当前显示的文本
     >   * `setPixmap(QPixmap('path_to_image.jpg'))`：设置标签以显示一个图片
     > * `单行文本框 QLineEdit`
     >   * `setText(text)`：设置文本框的文本
     >   * `text()`：获取文本框中的文本
     >   * 信号
     >     * `lineEdit_Name.textChanged.connect(your_function)`：文本框内容改变时触发
     > * `按钮 QPushButton`
     >   * `setText(text)`：设置按钮的文本
     >   * `setDisabled(True)`：禁用按钮
     >   * 信号
     >     * `button_Name.clicked.connect(your_function)` ：点击按钮时触发

2. `QRadioButton`、`QCheckBox`、`QComBoBox `

   * 使用Qt Designer 画界面

     > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202312161546666.png)
     >
     > 1. 新建 `QWidget`
     > 2. 主题：3个 `标签label` + 2个 `单选按钮radioButton`，全选5个控件设为栅格布局
     > 3. 通知：3个 `标签label` + 1个 `复选框checkBox`，全选4个控件设为栅格布局
     > 4. 语言：3个 `标签label` + 1个 `下拉框comboBox`，全选4个控件设置为栅格布局
     > 5. 需要交互的控件全部语义化命名
     > 6. 文件保存为 `second.ui`，自动编译生成 `second_ui.py`

   * 主程序代码

     ```python
     import sys
     from PySide6.QtWidgets import QApplication, QWidget
     from second_ui import Ui_Form
     
     
     # 主窗口类
     class mainWindow(QWidget):
         def __init__(self):
             super(mainWindow, self).__init__()
             self.ui = Ui_Form()  # 创建UI对象
             self.ui.setupUi(self)  # 加载UI布局
             self.bind_event()  # 绑定事件
     
         # 绑定事件
         def bind_event(self):
             self.ui.Theme_dark_radioButton.toggled.connect(self.on_radio_button_toggled)
             self.ui.Theme_light_radioButton.toggled.connect(self.on_radio_button_toggled)
             self.ui.Notify_checkBox.stateChanged.connect(self.Notify_on_changed)
             self.ui.Language_comboBox.currentIndexChanged.connect(self.Language_on_changed)
     
         # 待绑定函数
         def on_radio_button_toggled(self):
             if self.ui.Theme_dark_radioButton.isChecked():
                 self.setStyleSheet("background-color: rgb(79, 86, 107);color: rgb(255, 255, 255);")
                 self.ui.Theme_Status_label.setText("暗色系")
             else:
                 self.setStyleSheet("background-color: rgb(199, 206, 234);color: rgb(0, 0, 0);")
                 self.ui.Theme_Status_label.setText("亮色系")
     
         def Notify_on_changed(self):
             self.ui.Notify_Status_label.setText("启用" if self.ui.Notify_checkBox.isChecked() else "禁用")
     
         def Language_on_changed(self):
             self.ui.Language_Status_label.setText(self.ui.Language_comboBox.currentText())
     
     
     if __name__ == "__main__":
         app = QApplication(sys.argv)  # 创建应用对象
         window = mainWindow()  # 创建主窗口对象
         window.show()  # 显示主窗口
         sys.exit(app.exec())  # 运行应用
     ```

     > *  `单选按钮radioButton`
     >   *  `isChecked()`：返回 `True` 按钮选中，返回 `False` 按钮未选中
     >   *  `setChecked(state)`：设置按钮选中状态，`True` 为选中，`False`为未选中
     >   *  `text()`：获取单选按钮旁边显示的文本
     >   *  信号
     >      *  `radioButton_Name.toggled.connect(your_function)`：选中项时触发
     > *  `复选框checkBox`
     >   * `isChecked()`：返回 `True` 复选框选中，返回 `False` 复选框未选中
     >   * `setChecked(state)`：设置复选框选中状态，`True` 为选中，`False`为未选中
     >   * 信号
     >     * `checkBox_Name.stateChanged.connect(your_function)`：选中状态改变时触发
     > *  `下拉框comboBox`
     >   * `currentText()`：返回当前选中项的文本
     >   * `currentIndex()`：返回当前选中项的索引
     >   * `addItem(text)`：向下拉列表中添加一个选项
     >   * `addItems([item_list])`: 向下拉列表中添加多个选项
     >   * 信号
     >     * `comboBox_Name.currentIndexChanged.connect(your_function)` ：选中项时触发

3. `QSlider`、`QFileDialog`、`QPlainTextEdit`

   * 使用Qt Designer 画界面

     > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202312172257237.png)
     >
     > 1. 新建 `QWidget`
     >
     > 2. 图片展示区：1个 `框架frame` ，向 `frame` 拖入顶底2个 `纵向弹簧Horizontal Spacer` + 1个 `标签label` ，`frame`设置为垂直布局
     >
     > 3. 导入图片区：1个 `按钮pushButton` + 1个 `纯文本框plainTextEdit`，全选2个控件设置为横向布局
     >
     > 4. 模糊度调整区：1个 `标签label` + 1个 `滑动条slider`，全选2个控件设置为横向布局
     >
     >    > **`slider`**设置：`maximum`：10；`tickPosition`：`TicksBelow`；`tickInterval`：10
     >
     > 5. 需要交互的控件全部语义化命名
     >
     > 6. 文件保存为 `third.ui`，自动编译生成 `third_ui.py`

   * 主程序代码

     ```python
     import sys
     from PySide6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QSlider, QLabel, QFileDialog, QPlainTextEdit
     from PySide6.QtGui import QPixmap, QGuiApplication
     from PySide6.QtCore import Qt
     from PIL import Image, ImageFilter
     from io import BytesIO
     from third_ui import Ui_Form
     
     
     class mainWindow(QWidget):
         def __init__(self):
             """主窗口类"""
             super(mainWindow, self).__init__()
             self.ui = Ui_Form()  # 创建UI对象
             self.ui.setupUi(self)  # 加载UI布局
             self.bind_event()  # 绑定事件
     
         def bind_event(self):
             """绑定事件"""
             self.ui.UpLoadButton.clicked.connect(self.loadImage)  # 图片上传按钮点击事件
             self.ui.Image_Slider.valueChanged.connect(self.adjustBlur)  # 滑动条值改变事件
     
         def loadImage(self):
             """加载图片"""
             imagePath, _ = QFileDialog.getOpenFileName(self, "打开图片", "", "图片文件 (*.png *.jpg *.bmp *.webp)")  # 打开图片文件对话框
             if imagePath:  # 判断是否选择了图片
                 self.originalImage = Image.open(imagePath)  # 打开图片
                 self.updateImageDisplay()  # 更新图片显示
                 self.displayImageInfo(imagePath)  # 显示图片信息
     
         def displayImageInfo(self, imagePath):
             """显示图片信息"""
             infoText = f"文件名：{imagePath.split('/')[-1]}\n"  # 获取图片文件名
             infoText += f"尺寸：{self.originalImage.width} x {self.originalImage.height} pixels\n"  # 获取图片尺寸
             self.ui.image_info_textEdit.setPlainText(infoText)  # 设置文本框显示图片信息
     
         def adjustBlur(self, value):
             """调整模糊度"""
             if self.originalImage:
                 blurredImage = self.originalImage.filter(ImageFilter.GaussianBlur(value))  # 模糊图片
                 self.updateImageDisplay(blurredImage)  # 更新图片显示
     
         def updateImageDisplay(self, image=None):
             """更新图片显示"""
             if image is None:
                 image = self.originalImage  # 如果没有传入图片，默认使用原始图片
             if image:
                 byteArr = BytesIO()  # 创建字节流
                 image.save(byteArr, format="PNG")  # 保存图片为字节流
                 byteArr = byteArr.getvalue()  # 获取字节流的值
                 pixmap = QPixmap()  # 创建图片像素光标
                 pixmap.loadFromData(byteArr)  # 从字节流中加载图片
                 scaled_pixmap = self.scaleImageToLabel(pixmap.toImage(), self.ui.image_frame)
                 self.ui.image_label.setPixmap(scaled_pixmap)  # 设置显示标签的图片
     
         def scaleImageToLabel(self, image, area):
             """调整图片尺寸"""
             label_width = area.width()  # 获取显示区域的宽度
             label_height = area.height()  # 获取显示区域的高度
             pixmap = QPixmap.fromImage(image)  # 将图片转化为QPixmap
             scaled_pixmap = pixmap.scaled(label_width, label_height, Qt.AspectRatioMode.KeepAspectRatio)  # 缩放图片
             return scaled_pixmap
     
     
     if __name__ == "__main__":
         app = QApplication(sys.argv)  # 创建应用对象
         window = mainWindow()  # 创建主窗口对象
         window.show()  # 显示主窗口
         sys.exit(app.exec())  # 运行应用
     ```

     > *  `纯文本框plainTextEdit`
     >    *  `setPlainText(text)`：设置控件的文本
     >    *  `toPlainText()`：获取控件的文本
     >    *  `appendPlainText(text)`：在文本框的文本末尾追加文本，不添加新行
     >    *  `clear()`：清除文本框
     > *  `文件上传弹窗fileDialog`
     >    *  `getOpenFileName(parent, title, dir, filter)`：打开文件选择对话框，返回选定的文件名
     >    *  `getOpenFileNames(parent, title, dir, filter)`：类似于 `getOpenFileName`，可选多个文件
     >    *  `getExistingDirectory(parent, title, dir)`：打开目录选择对话框
     > *  `滑块slider`
     >    *  `setValue(value)`：设置滑块当前值
     >    *  `value()`：获取滑块当前值
     >    *  `setRange(int min, int max)`：设置滑块的最小值和最大值
     >    *  信号
     >       *  `slider_Name.valueChanged.connect(your_function)` ：滑块的值变化时触发

4. `QTableWidget`、`QTableWidgetItem`、`QDialog`、`QSpinBox`

   * 使用Qt Designer 画界面

     > ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202312192221639.png)
     >
     > 1. 数据展示窗口：新建 `QWidget`
     >
     >    1. 搜索区：1个`单行文本框lineEdit` + 1个`按钮pushButton`，全选6个控件设为水平布局
     >    2. 数据展示区：1个 `表格tableWidget`
     >    3. 插入区：1个`按钮pushButton`
     >
     >    > `QWidget` 设置：`QWidget` 为垂直布局；双击`QWidget` ，设置列名；`sortingEnabled`：开启排序；
     >
     > 2. 用户录入窗口：新建 `QWidget`
     >
     >    1. 用户输入区：3个 `label` +  `单行文本框lineEdit` + `数字下拉框spinBox` + `文本下拉框comboBox`，全选6个控件设置为栅格布局
     >
     >       > `spinBox`设置：`value`：默认值设为18；`minimum`：设为0；`maximum`：设为60；`singleStep`：设为0.5
     >       >
     >       > `comboBox`设置：双击控件，设置选项
     >
     >    2. 确认区：1个`按钮pushButton`
     >
     >    > `QWidget` 设置：`QWidget` 为垂直布局；
     >
     > 3. 需要交互的控件全部语义化命名
     >
     > 4. 文件保存为 `forth.ui`、`forth_son.ui`，自动编译生成 `forth_ui.py`、`forth_son_ui.py`
   
   * 主程序代码
   
     ```python
     import sys
     from PySide6.QtWidgets import QApplication, QWidget, QTableWidgetItem, QDialog
     from PySide6.QtCore import Qt
     from tableWidget_ui import Ui_Form
     from tableWidge_sonWindow_ui import Ui_Form as Ui_Form_sonWindow
     
     
     class mainWindow(QWidget):
         def __init__(self):
             """主窗口类"""
             super(mainWindow, self).__init__()
             self.ui = Ui_Form()  # 创建UI对象
             self.ui.setupUi(self)  # 加载UI布局
             self.bind_event()  # 绑定事件
     
         def bind_event(self):
             """绑定事件"""
             self.ui.insert_btn.clicked.connect(self.showEntryDialog)  # 插入按钮被点击时，调用showEntryDialog
             self.ui.search_btn.clicked.connect(self.current_cell_on_selected)  # 搜索按钮被点击时，调用current_cell_on_selected
             self.ui.tableWidget.cellClicked.connect(self.current_cell_row_col)  # 任何单元格被点击时，调用current_cell_row_col
             self.ui.tableWidget.cellChanged.connect(self.current_cell_on_changed)  # 任何单元格内容改变时，调用current_cell_on_changed
     
         def showEntryDialog(self):
             """显示子窗口，若点击“确定”，则将子窗口数据添加到主窗口"""
             dialog = EntryDialog(self)  # 创建 EntryDialog 子窗口
             dialog.show()  # 显示 dialog
             if dialog.exec():  # 显示 dialog 并等待用户点击“确定”（即 accept() 被调用）
                 data = dialog.get_data()  # 获取用户在 dialog 中输入的数据
                 row_position = self.ui.tableWidget.rowCount()  # 获取表格中当前行数
                 self.ui.tableWidget.insertRow(row_position)  # 在最后一行插入一行
                 self.ui.tableWidget.setItem(row_position, 0, QTableWidgetItem(data["name"]))  # 该行的第一列设为“name”
                 self.ui.tableWidget.setItem(row_position, 1, QTableWidgetItem(str(data["age"])))  # 该行的第二列设为“age”
                 self.ui.tableWidget.setItem(row_position, 2, QTableWidgetItem(data["sex"]))  # 该行的第三列设为“sex”
     
         def current_cell_row_col(self):
             """显示当前选中行的行号、列号、内容"""
             row = self.ui.tableWidget.currentRow()  # 获取当前选中行的行号
             col = self.ui.tableWidget.currentColumn()  # 获取当前选中列的列号
             content = self.ui.tableWidget.item(row, col).text()  # 获取表格中指定行和列的文本内容
             print(f"行数：{row}；列数：{col}；内容：{content}")
     
         def current_cell_on_changed(self):
             """显示当前选中行的行号、列号"""
             row = self.ui.tableWidget.currentRow()  # 获取当前选中行的行号
             col = self.ui.tableWidget.currentColumn()  # 获取当前选中列的列号
             print(f"行数：{row}；列数：{col} 单元格发生改变")
     
         def current_cell_on_selected(self):
             """当前选定的单元格坐标和内容"""
             search_text = self.ui.search_input_lineEdit.text()  # 获取搜索文本
             result = self.ui.tableWidget.findItems(search_text, Qt.MatchExactly)  # 在表格中搜索匹配的项
             for item in result:
                 print(f"行数：{item.row()}；列数：{item.column()}；内容：{item.text()}")
     
     
     class EntryDialog(QDialog):
         def __init__(self, parent=None):
             """子窗口类"""
             super(EntryDialog, self).__init__()
             self.son_ui = Ui_Form_sonWindow()  # 创建UI对象
             self.son_ui.setupUi(self)  # 加载UI布局
             self.bind_event()  # 绑定事件
     
         def bind_event(self):
             """为子窗口的确认按钮绑定事件"""
             self.son_ui.confirm_insert_btn.clicked.connect(self.accept)
     
         def get_data(self):
             """获取用户在 dialog 中输入的数据"""
             data = {
                 "name": self.son_ui.name_lineEdit.text(),
                 "age": self.son_ui.age_spinBox.value(),
                 "sex": self.son_ui.sex_comboBox.currentText(),
             }
             return data
     
     
     if __name__ == "__main__":
         app = QApplication(sys.argv)  # 创建应用对象
         window = mainWindow()  # 创建主窗口对象
         window.show()  # 显示主窗口
         sys.exit(app.exec())  # 运行应用
     ```
     
     > *  `表格QTableWidget`
     >    *  `insertRow(row_position)`：在 `row_position` 插入一行
     >    *  `removeRow(row_position)`：删除第 `row_position` 行
     >    *  `setItem(int row, int column, QTableWidgetItem item)`：设置单元格(行、列)的值
     >    *  `item(int row, int column)`：返回单元格的值
     >    *  `findItems(search_text, Qt.MatchFlag)`：搜索文本
     >       *  `Qt.MatchFlag.MatchContains`：包含匹配
     >       *  `Qt.MatchFlag.MatchExactly`：完全匹配
     >       *  `Qt.MatchFlag.MatchStartsWith`：开头匹配
     >       *  `Qt.MatchFlag.MatchEndsWith`：结尾匹配
     >    *  `scrollToItem(text, QTableWidget.ScrollHints)`：滚动到文本处
     >       *  `QTableWidget.ScrollHints.PositionAtTop`：表格顶部
     >       *  `QTableWidget.ScrollHints.PositionAtCenter`：表格中间
     >       *  `QTableWidget.ScrollHints.PositionAtBottom`：表格底部
     >    *  信号
     >       *  `table_Name.cellClicked.connect(your_function)`：任何单元格被点击时触发
     >       *  `table_Name.cellChanged.connect(your_function)`：任何单元格内容改变时触发
     > *  `表格的单元格QTableWidgetItem`
     >    *  `setText(str)`：设置该单元格的值
     >    *  `text()`：返回该单元格的值
     >    *  `setBackground(Qt.GlobalColors)`：设置该单元格的背景色
     >    *  `setForeground(Qt.GlobalColors)`：设置该单元格的前景色
     > *  `QDialog`
     >    * `exec()`：执行对话框并阻塞其余程序，直到对话框关闭。
     >    * `accept()`：接受对话框，关闭并发送 Accepted 信号。
     >    * `reject()`：拒绝对话框，关闭并发送 Rejected 信号。
     >    * `show()`：显示对话框（非模态）。
     > *  `QSpinBox`
     >    * `value()`：返回当前值。
     >    * `setRange(int min, int max)`：设置滑块的最小值和最大值
     >    * 信号
     >      * `spinBox_Name.valueChanged.connect(your_function)` ：数字框的值变化时触发



![image-20231221235621082](/Users/jiangsai/Library/Application Support/typora-user-images/image-20231221235621082.png)



创建一个命令快捷输入窗口，分为三个区域

1. 命令新增区：用来新增命令。新增命令后，实时展示在「待执行命令集」
2. 待执行命令集：用来展示已经新增的命令
3. 待执行命令-编辑区：用来展示所有已新增命令的文本形式，文本可编辑，编辑保存后，实时更新「待执行命令集」





fake库用法



* `标签 Label`

  > 
  >
  > * `styleSheet`：标签的CSS样式，如背景色、字体颜色
  >
  >   > 标签增加边框和内边距：`border: 1px solid black; padding: 4px;`
  >
  > * `scaledContents`：标签内的图片缩放以适应标签的大小
  
* `单行文本 LineEdit`

  > * `validator`：验证器，用于限制输入的内容类型（如数字、字母）
  >
  >   > `mylineEdit.setValidator(QtGui.QRegularExpressionValidator(QtCore.QRegularExpression("[0-9]*")))`：只能输入0-9的数字
  >  >
  >   > `mylineEdit.setValidator(QtGui.QRegularExpressionValidator(QtCore.QRegularExpression("[a-zA-Z]*")))`：只能输入字母

  

* `下拉列表 ListWidget`

  > 方法
  >
  > list =["钢之炼金术", "地狱少女", "进击的巨人"]
  >
  > myListWidget.addItems (list)



