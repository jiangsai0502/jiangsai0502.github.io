###### 安装

```bash
pip install gradio
```

###### 基础组件

|          | 组件            | 用途                                   |
| -------- | --------------- | -------------------------------------- |
| 字符串   | `gr.Text()`     | 输入、输出字符串                       |
| 字符串   | `gr.Markdown()` | 输出 Markdown                          |
| 数字     | `gr.Number()`   | 输入、输出数字                         |
| 图片     | `gr.Image()`    | 输入（上传）、输出图片                 |
| 按钮     | `gr.Button()`   | 按钮                                   |
| 文件     | `gr.Files()`    | 输入（上传）文件                       |
| 单选框   | `gr.Radio()`    | 输入（选择）单选框                     |
| 复选框   | `gr.Checkbox()` | 输入（选择）复选框                     |
| 下拉菜单 | `gr.Dropdown()` | 输入（选择）下拉选项                   |
| tab页    | `gr.Tab()`      | 创建tab页                              |
| 水平排列 | `gr.Row()`      | `with gr.Row()` 内的多个组件排成1行    |
| 垂直排列 | `gr.Column()`   | `with gr.Column()` 内的多个组件排成1列 |

###### 组件属性

| 属性名         | 说明                                   | 应用于的组件类型                     |
| -------------- | -------------------------------------- | ------------------------------------ |
| `label`        | 界面上显示的组件名称                   | 所有组件                             |
| `value`        | 组件默认值                             | 大多数组件（如 `Text`、`Slider` 等） |
| `placeholder`  | 文本框的占位符                         | `Text`、`Textarea`                   |
| `step`         | `Slider`  步长                         |                                      |
| `min` 和 `max` | `Slider`、`Number` 最小, 最大值。      |                                      |
| `rows`         | 文本框行数(设置文本框高度)             |                                      |
| `checked`      | `Checkbox`初始状态，True 为选中        |                                      |
| `disabled`     | 禁用组件，True 为禁用                  | 所有组件                             |
| `live`         | `Slider`、`Text` 实时更新，True 为启用 | 等支持实时更新的组件                 |

###### 范例

```python
import gradio as gr

def greet(name, drink, liter):
    salu = "喝一杯" if drink else "不喝算了"
    greeting = f"Hi {name}， {salu}"
    liter = float(liter)
    return greeting, liter

args = [gr.Textbox(lines=2, placeholder="随意写点啥"), gr.Checkbox(), gr.Slider(0, 1)]
outputs = [gr.Textbox(), gr.Number()]
demo = gr.Interface(greet, args, outputs)
demo.launch()
```

`gr.Interface(greet, args, outputs)` ：创建一个 `gradio` 页面

> * 参数1：`greet`，即 Gradio 页面要运行的函数
> * 参数2：`args`，即 Gradio 页面上接受用户输入的区域
>   * 区域1：2行高度的文本框，默认文案为"随意写点啥"；作为参数1 `name` 传入 `WebFunc`
>   * 区域2：单选框，默认不勾选；作为参数2 `drink` 传入 `WebFunc`
>   * 区域3：滑动条，默认为0；作为参数3 `liter` 传入 `WebFunc`
> * 参数3：`outputs`，即 Gradio页面上展示 `WebFunc` 函数的返回值
>   * 区域1：单行高度的文本框，默认文案为空
>   * 区域2：单行高度的数字框，默认数字为空

```python
import gradio as gr


# 定义各个组件的回调函数
def show_image(image):
    return image

def echo_text(text):
    return text

def show_selection(choice):
    return f"你选择了：{choice}"

def show_number(num):
    return f"输入的数字是：{num}"

def show_checkbox(check):
    return f"你选择了：{check}"

def show_filenames(files):
    # 假设 files 是一个文件列表
    filenames = [file.name for file in files]
    return f"上传的文件：{', '.join(filenames)}"

def show_slider_value(value):
    return f"滑块的值是：{value}"

# 创建 Gradio Blocks 接口
with gr.Blocks() as demo:
    tab = gr.Tab()
    with tab:
        with gr.TabItem("输入"):
            # ------------------------ 字符串 ------------------------
            with gr.Row():
                with gr.Column():
                    # 使用 change 方法实现根据实时变化执行函数
                    text_input1 = gr.Text()
                    text_output1 = gr.Text()
                    text_input1.change(echo_text, inputs=text_input1, outputs=text_output1)
                with gr.Column():
                    # 使用 Button 实现点击按钮执行函数
                    text_input2 = gr.Text(placeholder="微柚酱", label="输入字符串", info="这是个注释")
                    text_output2 = gr.Text(label="展示函数处理后的字符串")
                    gr.Button("点击执行函数").click(echo_text, inputs=text_input2, outputs=text_output2)
            gr.Markdown("---")  # 添加分割线
            # ------------------------ 数字 ------------------------
            with gr.Row():
                with gr.Column():
                    # 使用 change 方法实现根据实时变化执行函数
                    number_input1 = gr.Number()
                    number_output1 = gr.Text()
                    number_input1.change(show_number, inputs=number_input1, outputs=number_output1)
                with gr.Column():
                    # 使用 Button 实现点击按钮执行函数
                    number_input2 = gr.Number(label="输入数字")
                    number_output2 = gr.Text(label="展示函数处理后的数字")
                    gr.Button("点击执行函数").click(show_number, inputs=number_input2, outputs=number_output2)
            gr.Markdown("---")  # 添加分割线

        with gr.TabItem("选择"):
            # ------------------------ 滑块 ------------------------
            with gr.Row():
                with gr.Column():
                    # 使用 change 方法实现根据实时变化执行函数
                    slider1 = gr.Slider(minimum=0, maximum=100, label="滑动选值")
                    slider_output1 = gr.Label()
                    slider1.change(show_slider_value, inputs=slider1, outputs=slider_output1)
                with gr.Column():
                    # 使用 Button 实现点击按钮执行函数
                    slider2 = gr.Slider(minimum=0, maximum=100, label="回显当前值")
                    slider_output2 = gr.Label()
                    gr.Button("点击执行函数").click(show_slider_value, inputs=slider2, outputs=slider_output2)
            gr.Markdown("---")
            # ------------------------ 单选框 ------------------------
            with gr.Row():
                with gr.Column():
                    # 使用 change 方法实现根据实时变化执行函数
                    radio1 = gr.Radio(["选项1", "选项2"])
                    radio_output1 = gr.Text()
                    radio1.change(show_checkbox, inputs=radio1, outputs=radio_output1)
                with gr.Column():
                    # 使用 Button 实现点击按钮执行函数
                    radio2 = gr.Radio(["选项1", "选项2"], value="选项2", label="挑个选项")
                    radio_output2 = gr.Text(label="回显选项")
                    gr.Button("点击执行函数").click(show_checkbox, inputs=radio2, outputs=radio_output2)
            gr.Markdown("---")
            # ------------------------ 复选框 ------------------------
            with gr.Row():
                with gr.Column():
                    # 使用 change 方法实现根据实时变化执行函数
                    check1 = gr.Checkbox(["选项1", "选项2"])
                    check_output1 = gr.Text()
                    check1.change(show_checkbox, inputs=check1, outputs=check_output1)
                with gr.Column():
                    # 使用 Button 实现点击按钮执行函数
                    check2 = gr.Checkbox(["选项1", "选项2"], value=["选项1"], label="挑个选项")
                    check_output2 = gr.Text(label="回显选项")
                    gr.Button("点击执行函数").click(show_checkbox, inputs=check2, outputs=check_output2)
            gr.Markdown("---")
            # ------------------------ 下拉菜单 ------------------------
            with gr.Row():
                with gr.Column():
                    # 使用 change 方法实现根据实时变化执行函数
                    dropdown1 = gr.Dropdown(choices=["选项1", "选项2"])
                    dropdown_output1 = gr.Text()
                    dropdown1.change(show_selection, inputs=dropdown1, outputs=dropdown_output1)
                with gr.Column():
                    # 使用 Button 实现点击按钮执行函数
                    dropdown2 = gr.Dropdown(choices=["选项1", "选项2"], label="挑个选项")
                    dropdown_output2 = gr.Text(label="回显选项")
                    gr.Button("点击执行函数").click(show_selection, inputs=dropdown2, outputs=dropdown_output2)

        with gr.TabItem("上传"):
            # ------------------------ 图片上传和显示 ------------------------
            with gr.Row():
                with gr.Column():
                    # 使用 change 方法实现根据实时变化执行函数
                    img1 = gr.Image()
                    output_img1 = gr.Image()
                    img1.change(show_image, inputs=img1, outputs=output_img1)
                with gr.Column():
                    # 使用 Button 实现点击按钮执行函数
                    img2 = gr.Image(label="上传图片")
                    output_img2 = gr.Image(label="展示函数处理后的图片")
                    gr.Button("点击执行函数").click(show_image, inputs=img2, outputs=output_img2)
            gr.Markdown("---")
            # ------------------------ 文件上传 ------------------------
            with gr.Row():
                with gr.Column():
                    # 使用 change 方法实现根据实时变化执行函数
                    files_input1 = gr.Files()
                    files_output1 = gr.Text()
                    files_input1.change(show_filenames, inputs=files_input1, outputs=files_output1)
                with gr.Column():
                    # 使用 Button 实现点击按钮执行函数
                    files_input2 = gr.Files(label="上传文件")
                    files_output2 = gr.Text(label="回显文件名")
                    gr.Button("点击执行函数").click(show_filenames, inputs=files_input2, outputs=files_output2)

# 启动应用
demo.launch()
```