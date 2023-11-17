### pyecharts

#### 1. 安装

```bash
# 查看当前系统下的虚拟环境
conda info --envs
# 切换虚拟环境
source activate py3_428
# 查看当前虚拟环境下用conda安装的包
conda list
# 查看当前虚拟环境下用pip安装的包
pip list
# 安装pyecharts版本1.0以上，0.5已被废弃
conda install pyecharts
# 查看pyecharts版本
conda list
# 

# 

# 

# 

# 

# 


```



#### 饼状图

1. **数字**

   <img src="https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200204103234.png" style="zoom:40%;" />

   ```python
   from pyecharts.faker import Faker
   from pyecharts import options as opts
   from pyecharts.charts import Pie
   
   listData = [('配置项', 60),('插件', 15),('用户文档', 9)]
   
   def pie_base() -> Pie:
       c = (
           Pie()
           .add("", listData,)
           .set_global_opts(title_opts=opts.TitleOpts(title=""))
           .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))
       )
       return c
   
   pie_base().render('Chart_Pie.html')
   ```

   > 1. Pie 类只接受一种类型的数据 
   >
   >    [(TupleKey1, TupleValue1),(TupleKey2, TupleValue2)]
   >
   >    > TupleKey 是 string
   >    >
   >    > TupleValue 是 int，float
   >
   > 2. 数据标签的格式：*用户文档：9*
   >
   >    `.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {c}"))`
   >
   >    > b 代表 TupleKey 字符串
   >    >
   >    > c 代表 TupleValue 数值
   >    >
   >    > d 代表 TupleValue 数值所占百分比

2. **百分比**

   <img src="https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/20200204102250.png" style="zoom:40%;" />

   ```python
   from pyecharts.faker import Faker
   from pyecharts import options as opts
   from pyecharts.charts import Pie
   
   listData = [('满意',60), ('不满',6), ('建议',50)]
   # listData = [('文档',8), ('流水线',21), ('插件',14), ('shell',2)]
   listData = [('Q1计划解决',26), ('Q1暂不解决',9)]
   def pie_base() -> Pie:
       c = (
           Pie()
           .add("", listData,)
           .set_global_opts(title_opts=opts.TitleOpts(title=""))
           .set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))
       )
       return c
   
   pie_base().render('Chart_Pie.html')
   ```

   > 数据标签的格式：*用户文档：9*
   >
   > `.set_series_opts(label_opts=opts.LabelOpts(formatter="{b}: {d}%"))`
   >
   > > b 是 TupleKey 字符串
   > >
   > > c 是TupleValue 数值
   > >
   > > d 是 TupleValue 数值所占百分比

3. 百分比



### Matplotlib

1. 安装

   ```bash
   # 切换到虚拟环境
   source activate py3.8
   # 安装 numpy
   conda install numpy
   # 安装 matplotlib
   conda install matplotlib
   # 验证安装版本
   conda list
   ```

2. 基本用法

   ```
   
   ```

   