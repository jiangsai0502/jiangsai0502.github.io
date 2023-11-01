a = "I Love Crystal!And I Hate Tom!"
name_list = ["Jessie", "Tom", "Crystal"]
print(any(name in a for name in name_list))
name_list = ["Jessie", "Tomi", "Rose"]
print(any(name in a for name in name_list))

x = "This is a hello message."
z = "Ths is a message."

# 列表包含的关键词
keywords = ["hi", "hello"]

# 使用 any() 函数检查是否有任意一个关键词出现在字符串 x 中，并且只在条件为真时执行命令
if any(keyword in x for keyword in keywords):
    # 如果条件为真，则执行某个命令，这里用 print 作为示例
    print(any(keyword in x for keyword in keywords))
    print("x")

if any(keyword in z for keyword in keywords):
    # 如果条件为真，则执行某个命令，这里用 print 作为示例
    print(any(keyword in z for keyword in keywords))
    print("z")
