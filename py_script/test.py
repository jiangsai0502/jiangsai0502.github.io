import pandas as pd

ExcelFile = "/Users/jiangsai/Desktop/test.xlsx"
MoiveList = [
    {"影片名": "教父", "评分": "9.7", "评价人数": "2938225人"},
    {"影片名": "冰与火", "评分": "9.6", "评价人数": "2170430人"},
]

# 追加写入
new_data = [
    {"影片名": "肖申克的救赎", "评分": 9.3, "评价人数": 2513246},
    {"影片名": "盗梦空间", "评分": 8.8, "评价人数": 2092510},
]

# 转换新数据
data_to_append = pd.DataFrame(new_data)
# 读取旧数据
original_data = pd.read_excel(ExcelFile)
# 合并新旧数据
combined_data = pd.concat([original_data, data_to_append], ignore_index=True)
# 将合并后的数据写回 Excel
with pd.ExcelWriter(ExcelFile, mode="w", engine="openpyxl") as writer:
    combined_data.to_excel(writer, sheet_name="Sheet1", index=False)
