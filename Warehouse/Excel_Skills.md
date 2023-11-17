### Excel技巧

| 查找行内/列内重复数据                                        | 删除行内/列内重复数据                                        |
| ------------------------------------------------------------ | ------------------------------------------------------------ |
| ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210730223545.png) | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210730224151.png) |
| **数字0补齐5位**                                             | **防止重复录入**                                             |
| ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210730224940.png) | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210730231118.png) |
| **设置下拉菜单**                                             | **删除空白行**                                               |
| ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210730233103.png) | ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210730234210.png) |
| **快速调整列宽**                                             |                                                              |
| ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20210730234809.png) |                                                              |
| 快速移动：Command+方向键                                     | 快速多选：Command+Shift+方向键                               |
|                                                              |                                                              |

**vlookup用法**

> * [参考1](https://zhuanlan.zhihu.com/p/29161495)，[参考2](https://zhidao.baidu.com/question/1734379668253114707.html)
>
> * **坑**：公式：VLOOKUP(D1,A$1:B$9,2,0)，要加上绝对引用符号 $，否则会匹配出问题

**正态分布画图**

> [参考](https://www.bilibili.com/video/BV1Hi4y1L7Eg)
>
> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202309201525146.png)

**数值判断大小并添加颜色**

> 1. 选中待判断的单元格
> 2. 开始-条件格式-突出显示单元格规则

**单元格下拉格式部分不变**

> 增加$
>
> 1. A1= $C$1+D1
> 2. 下拉得到A2、A3
> 3. A2 = $C$1+D2
> 4. A3 = $C$1+D3
