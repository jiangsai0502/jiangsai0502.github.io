##### 安装

````
> pip install pandas
> pip install pandas sqlalchemy
````

**核心数据类型：DataFrame类**

> 列表和字典都可以转为DataFrame类
>
> ```python
> MoiveList = [
>     {"影片名": "教父", "评分": 7.7, "评价人数": "2938225人"},
>     {"影片名": "冰与火", "评分": 9.6, "评价人数": "2170430人"},
>     {"影片名": "暗战", "评分": 5.9, "评价人数": "430人"},
> ]
> Sai_df = pd.DataFrame(MoiveList)
> MoiveDict = {
>     "影片名": ["教父", "冰与火"],
>     "评分": ["9.7", "9.6"],
>     "评价人数": ["2938225人", "2170430人"],
> }
> Sai_df = pd.DataFrame(MoiveDict)
> ```
>
> ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310302027704.png)
>
> * 行提取
>
>   * 单行提取：`loc[行索引]`，从 `0` 到 `行数-1`
>
>     ```
>     # 第1行
>     FilterData = result_df.loc[[0]]
>     print(FilterData)
>     ```
>
>     ```
>       影片名   评分      评价人数
>     0  教父  7.7  2938225人
>     ```
>
>   * 多行提取：`loc[[行索引, 行索引]]`
>
>     ```
>     # 第1和第3行
>     FilterData = result_df.loc[[0,2]]
>     print(FilterData)
>     ```
>
>     ```
>      影片名   评分      评价人数
>     0  教父  7.7  2938225人
>     2  暗战  5.9      430人
>     ```
>
>   * 多行切片提取：`loc[行索引:行索引]`
>
>     ```
>     # 第1行 到 第3行
>     FilterData = result_df.loc[0:2]
>     print(FilterData)
>     ```
>
>     ```
>        影片名   评分      评价人数
>     0   教父  7.7  2938225人
>     1  冰与火  9.6  2170430人
>     2   暗战  5.9      430人
>     ```
>
>   * 多行切片提取：`loc[start:stop:step]` 即起始索引:终止索引:步长
>
>     ```
>     # 从第1行开始，到最后，步长为2
>     > FilterData = result_df.loc[0::2]
>     > print(FilterData)
>     ```
>
>     ```
>        影片名   评分      评价人数
>     0   教父  7.7  2938225人
>     2   暗战  5.9      430人
>     ```
>
> * 列提取
>
>   * 单列提取
>
>     ```
>     # "影片名"列
>     FilterData = Sai_df[["影片名"]]
>     print(FilterData)
>     ```
>
>     ```
>     # "影片名"列
>     FilterData = Sai_df.loc[::, ["影片名"]]
>     print(FilterData)
>     ```
>
>     > 上述方式效果相同
>
>     ```
>        影片名
>     0   教父
>     1  冰与火
>     2   暗战
>     ```
>
>   * 多列提取
>
>     ```
>     # 第1和第3行
>     FilterData = Sai_df[["影片名", "评价人数"]]
>     print(FilterData)
>     ```
>
>     ```
>     # 第1和第3行
>     FilterData = Sai_df.loc[::, ["影片名", "评价人数"]]
>     print(FilterData)
>     ```
>
>     ```
>       影片名   评分      评价人数
>     0  教父  7.7  2938225人
>     2  暗战  5.9      430人
>     ```
>
>   * 多列切片提取
>
>     ```
>     # 第1行 到 第3行，"影片名"和"评价人数"列的值
>     FilterData = Sai_df.loc[[0, 2], ["影片名", "评价人数"]]
>     print(FilterData)"影片名", "评价人数"列的值
>     ```
>
>     ```
>       影片名      评价人数
>     0  教父  2938225人
>     2  暗战      430人
>     ```
>
> * 区域提取
>
> * 重要属性
>
>   * `result_df.values` ：查看所有元素的值
>
>     ```
>     [['教父', 7.7, '2938225人'],
>      ['冰与火', 9.6, '2170430人'],
>      ['暗战', 5.9, '430人']]
>     ```
>
>   * `result_df.dtypes` ：查看所有元素的类型
>
>     ```
>     影片名      object
>     评分      float64
>     评价人数     object
>     dtype: object
>     ```
>
>   * `result_df.index` ：查看所有行名、重命名行名
>
>     ```
>     RangeIndex(start=0, stop=3, step=1)
>     ```
>
>   * `result_df.columns` ：查看所有列名,重命名列名
>
>     ```
>     Index(['影片名', '评分', '评价人数'], dtype='object')
>     ```
>
>   * `result_df.T` ：行列数据转换
>
>     ![](https://raw.githubusercontent.com/jiangsai0502/PicBedRepo/master/img/202310302032141.png)
>
>   * `result_df.head` ：查看前N条数据，默认5条；`result_df.head(2)`：查看前2条
>
>     ```
>     <bound method NDFrame.head of    影片名   评分      评价人数
>     0   教父  7.7  2938225人
>     1  冰与火  9.6  2170430人
>     2   暗战  5.9      430人>
>     ```
>
>   * `result_df.tail` ：查看后N条数据，默认5条；`result_df.tail(2)` ：查看后2条
>
>     ```
>     <bound method NDFrame.tail of    影片名   评分      评价人数
>     0   教父  7.7  2938225人
>     1  冰与火  9.6  2170430人
>     2   暗战  5.9      430人>
>     ```
>
>   * `result_df.shape` ：查看行数和列数；shape[0]表示行，shape[1]表示列
>
>     ```
>     (3, 3)
>     ```
>
>   * `result_df.info` ：查看索引、数据类型和内存信息
>
>     ```
>     <bound method DataFrame.info of    影片名   评分      评价人数
>     0   教父  7.7  2938225人
>     1  冰与火  9.6  2170430人
>     2   暗战  5.9      430人>
>     ```
>

**使用SQL代替pandas自身的查询**

```python
import pandas as pd
from sqlalchemy import create_engine, text

MoiveList = [
    {"影片名": "教父", "评分": 7.7, "评价人数": "2938225人"},
    {"影片名": "冰与火", "评分": 9.6, "评价人数": "2170430人"},
    {"影片名": "暗战", "评分": 5.9, "评价人数": "430人"},
]
File = "/Users/jiangsai/Desktop/temp.csv"


# 爬取网站数据，存入csv
def Get_Data_From_Web(website):
    pass


# 加载web数据，增删改查，存入csv
def Processing_Data_From_Web(MoiveList, SavedFile):
    # 1. 数据列表转换为DataFrame
    Sai_df = pd.DataFrame(MoiveList)
    # 2. 连接到内存数据库SQLite
    engine = create_engine("sqlite:///:memory:")
    # 3. 将DataFrame写入数据库表中
    Sai_df.to_sql("my_table", engine, index=False)
    # 4. 执行SQL查询
    sql_query = "SELECT * FROM my_table WHERE 评分 >= 5"
    result_df = pd.read_sql_query(sql_query, engine)
    # 5. 打印并保存查询结果
    print(result_df)
    result_df.to_csv(SavedFile, mode="w+", index=False)
    # 6. 关闭数据库连接
    engine.dispose()


# 加载csv，增删改查，存回csv
def Processing_Data_From_CSV(ProcessFile, ProcessingSQL):
    # 1. 读取csv文件并转换为DataFrame
    Sai_df = pd.read_csv(ProcessFile)
    # 2. 连接到内存数据库SQLite
    engine = create_engine("sqlite:///:memory:")
    # 3. 将DataFrame写入数据库表中
    Sai_df.to_sql("my_table", engine, index=False)
    # 4. 执行SQL增、删、改、查
    Insert_Delete_Update = False
    for item in ["insert", "delete", "update"]:
        if ProcessingSQL.text.lower().startswith(item):
            Insert_Delete_Update = True
    if Insert_Delete_Update:
        conn = engine.connect()
        conn.execute(ProcessingSQL)
        # 从内存数据库中读取更新后的数据并写回csv文件
        updated_df = pd.read_sql("SELECT * FROM my_table", engine)
        updated_df.to_csv(ProcessFile, mode="w+", index=False)
        conn.close()
    else:
        result_df = pd.read_sql(ProcessingSQL, engine)
        print(result_df)
    # 5. 关闭内存数据库连接
    engine.dispose()


# 加载csv，数据分析
def Analyse_Data(AnalyseFile):
    # 1. 读取csv文件并转换为DataFrame
    Sai_df = pd.read_csv(AnalyseFile)
    print(Sai_df)

    # 2. 单行提取：loc[行索引]，从 0 到 行数-1
    FilterData = Sai_df.loc[2]  # 第3行
    print(FilterData)
    #    多行提取：loc[[行索引, 行索引]]
    FilterData = Sai_df.loc[[0, 2]]  # 第1、3行
    print(FilterData)
    #    多行切片提取：loc[行索引:行索引]
    FilterData = Sai_df.loc[0:2]  # 第1行 - 第3行
    print(FilterData)

    # 3. 单列提取：loc[::, [列名]]
    FilterData = Sai_df.loc[::, ["影片名"]]  # "影片名"列的值
    print(FilterData)
    #            DataFrame[[列名]]
    FilterData = Sai_df[["影片名"]]
    print(FilterData)
    #    多列提取：loc[::, [列名, 列名]]
    FilterData = Sai_df.loc[::, ["影片名", "评价人数"]]  # "影片名", "评价人数"列的值
    print(FilterData)
    #            DataFrame[[列名, 列名]]
    FilterData = Sai_df[["影片名", "评价人数"]]
    print(FilterData)

    # 4. 指定行指定列提取
    FilterData = Sai_df.loc[[0, 2], ["影片名", "评价人数"]]  # 第1、3行，"影片名", "评价人数"列的值
    print(FilterData)


if __name__ == "__main__":
    # Processing_Data_From_Web(MoiveList, File)
    # sql_query = text("UPDATE my_table SET 评分 = 9.9 WHERE 影片名 = '暗战'")
    # sql_query = text("INSERT into my_table values ('霸王别姬1',7.8,'943858人')")
    # sql_query = text("DELETE FROM my_table WHERE 影片名 = '霸王别姬1'")
    # sql_query = text("SELECT * FROM my_table WHERE 评分 >= 7")
    # Processing_Data_From_CSV(File, sql_query)
    Analyse_Data(File)
```

> `DataFrame.to_csv(TargetFile, mode="w+", index=False)`
>
> * `mode='a+'`：追加，不存在文件，则新建并写入
> * `mode='w+'`：覆盖，不存在文件，则新建并写入
> * `header=True`：写入dataframe的列名（表头）
> * `index=False`：不添加索引