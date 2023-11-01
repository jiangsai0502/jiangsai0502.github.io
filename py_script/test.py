import pandas as pd
from sqlalchemy import create_engine, text


MoiveList = [
    {"影片名": "教父", "评分": 7.7, "评价人数": "2938225人"},
    {"影片名": "冰与火", "评分": 9.6, "评价人数": "2170430人"},
    {"影片名": "暗战", "评分": 5.9, "评价人数": "430人"},
]
Sai_df = pd.DataFrame(MoiveList)

# 单行提取：loc[行索引]，从 0 到 行数-1
FilterData = Sai_df.loc[2]  # 第3行
print(FilterData)
# 多行提取：loc[[行索引, 行索引]]
FilterData = Sai_df.loc[[0, 2]]  # 第1、3行
print(FilterData)
# 多行切片提取：loc[行索引:行索引]
FilterData = Sai_df.loc[0:2]  # 第1行 - 第3行
print(FilterData)

FilterData = result_df.loc[0::2]
print(FilterData)

# 单列提取："影片名"列的值
FilterData = Sai_df[["影片名"]]
print(FilterData)
FilterData = Sai_df.loc[::, ["影片名"]]
print(FilterData)
# 查看"影片名", "评价人数"列的值
FilterData = Sai_df[["影片名", "评价人数"]]
print(FilterData)
FilterData = Sai_df.loc[::, ["影片名", "评价人数"]]
print(FilterData)
# 查看第1、3行，"影片名", "评价人数"列的值
FilterData = Sai_df.loc[[0, 2], ["影片名", "评价人数"]]
print(FilterData)

# def Data_to_CSV(MoiveList, SavedFile):
#     # 1. 数据列表转换为DataFrame
#     Sai_df = pd.DataFrame(MoiveList)
#     # 2. 连接到内存数据库SQLite
#     engine = create_engine("sqlite:///:memory:")
#     # 3. 将DataFrame写入数据库表中
#     Sai_df.to_sql("my_table", engine, index=False)
#     # 4. 执行SQL查询
#     sql_query = "SELECT * FROM my_table WHERE 评分 >= 5"
#     result_df = pd.read_sql_query(sql_query, engine)
#     # 5. 保存查询结果
#     result_df.to_csv(SavedFile, mode="w+", index=False)
#     # 6. 关闭数据库连接
#     engine.dispose()


# def CSV_Processing(ProcessFile, sql_query):
#     # 1. 数据列表转换为DataFrame
#     Sai_df = pd.read_csv(ProcessFile)
#     # 2. 连接到内存数据库SQLite
#     engine = create_engine("sqlite:///:memory:")
#     # 3. 将DataFrame写入数据库表中
#     Sai_df.to_sql("my_table", engine, index=False)

#     # 4. 执行SQL增、删、改、查
#     Insert_Delete_Update = False
#     for item in ["insert", "delete", "update"]:
#         if sql_query.text.lower().startswith(item):
#             Insert_Delete_Update = True
#     if Insert_Delete_Update:
#         conn = engine.connect()
#         conn.execute(sql_query)
#         # 从内存数据库中读取更新后的数据并写回csv文件
#         updated_df = pd.read_sql("SELECT * FROM my_table", engine)
#         updated_df.to_csv(ProcessFile, mode="w+", index=False)
#         conn.close()
#     else:
#         result_df = pd.read_sql(sql_query, engine)
#         print(result_df)
#     # 5. 关闭内存数据库连接
#     engine.dispose()


# def Data_Perpare():
#     MoiveList = [
#         {"影片名": "教父", "评分": 7.7, "评价人数": "2938225人"},
#         {"影片名": "冰与火", "评分": 9.6, "评价人数": "2170430人"},
#         {"影片名": "暗战", "评分": 5.9, "评价人数": "430人"},
#     ]
#     SavedFile = "/Users/jiangsai/Desktop/temp.csv"
#     return MoiveList, SavedFile


# if __name__ == "__main__":
#     MoiveList, SavedFile = Data_Perpare()
#     Data_to_CSV(MoiveList, SavedFile)
#     # sql_query = text("UPDATE my_table SET 评分 = 9.9 WHERE 影片名 = '暗战'")
#     # sql_query = text("INSERT into my_table values ('霸王别姬1',7.8,'943858人')")
#     # sql_query = text("DELETE FROM my_table WHERE 影片名 = '霸王别姬1'")
#     sql_query = text("SELECT * FROM my_table WHERE 评分 >= 7")
#     CSV_Processing(SavedFile, sql_query)


# # 查看MoiveList在pandas中的数据样式
# print(Dict_Data)
# # 查看MoiveList在pandas中的行数和列数
# print(Dict_Data.shape)


# Panda_Data = pd.DataFrame(MoiveList, columns=["影片名", "评分", "评价人数"])
# print(Panda_Data)

# CsvFile = "/Users/jiangsai/Desktop/test.csv"
# OpenCsv = pd.read_csv(CsvFile, encoding="utf-8-sig")
# print(OpenCsv)


##########################################
# CsvFile = "/Users/jiangsai/Desktop/test.csv"
# # 加载csv文件
# CSVwriter = pd.read_csv(CsvFile)


# # 存储
# def save_data():
#     CSVwriter.to_csv(CsvFile, encoding="utf-8", index=False)


# # 查询
# def filter(type, key):
#     result = CSVwriter.query('题目.str.contains("{}", na=False)'.format(key))
#     format_print(result)


# # 新增
# def add(title, dynasty, author, content):
#     CSVwriter.loc[last_index] = [title, dynasty, author, content]
#     save_data()


# # 删除
# def delete(index):
#     CSVwriter.drop(CSVwriter.index[index], inplace=True)
#     save_data()


# # 修改
# def update(old_index, new_index):
#     old_values = CSVwriter.loc[old_index].values
#     delete(old_index)
#     CSVwriter.reset_index(inplace=True, drop=True)

#     df1 = CSVwriter.iloc[:new_index]
#     df1.loc[new_index] = old_values

#     df2 = CSVwriter.iloc[new_index:]
#     CSVwriter = df1.append(df2)
#     CSVwriter.reset_index(inplace=True, drop=True)


# content = "教父"
# filter(content)

# title = ""
# score = 7
# comments = "43人"
# add(title, dynasty, author, content)
# format_print(CSVwriter)

# index = 2
# delete(index)

# old_index = 3
# new_index = 13
# update(int(old_index), int(new_index))
