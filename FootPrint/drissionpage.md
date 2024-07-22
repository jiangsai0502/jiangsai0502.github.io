### 使用教程

* 安装

  ```js
  pip install DrissionPage

* 浏览器创建

  ```python
  baseUrl = "https://gitee.com/explore"
  
  # 创建配置对象
  CO = ChromiumOptions()
  # 设置本地浏览器调试端口
  CO.auto_port()
  # 创建页面对象，并启动或接管浏览器
  page = ChromiumPage(CO)
  # 创建标签页
  tab = page.new_tab()
  # 在当前标签页打开网址
  tab.get(baseUrl)
  ```

* 元素定位（DrissionPage 结合Xpath、css selector自创的）

  > 所有查找方法都是基于3种素属性
  >
  > |   写法    |      说明      | 示例                                                 |
  > | :-------: | :------------: | ---------------------------------------------------- |
  > | `@tag()`  |     标签名     | 即 `<div id="one">` 中的 `div`                       |
  > |  `@xxxx`  | 标签体中的属性 | 如 `<div id="one">` 中的 `id`，写作 `'@id'`          |
  > | `@text()` |    元素文本    | 即 `<p class="p_cls">可视文字</p>` 中的 `'可视文字'` |
  >
  > `tab.ele('@id=one')`  ：获取第一个 `id` 为 `one` 的元素
  > `tab.ele('@tag()=div')`  ：获取第一个 `div` 元素
  > `tab.ele('@text()=可视文字')`  ：获取第一个文本为 `"可视文字"` 的元素

  * 单属性匹配符 `@`

    > `tab.ele('@id=one')`  ：获取第一个 `id` 为 `one` 的元素

  * 多属性匹配符 **与**  `@@`

    > `name = tab.ele('@@class=p_cls@@text()=可视文字') ` ：查找 `class` 为 `p_cls` 且文本为`"可视文字"`的元素

  * 多属性匹配符 **或**  `@| `

    >`scores = tab.eles('@|id=row1@|id=row2') ` ：查找所有 `id` 为 `row1` 或 `id` 为 `row2` 的元素

  * 否定匹配符 `@!`

    >

  * 

* 

