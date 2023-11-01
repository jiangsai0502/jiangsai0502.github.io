a = "I Love Crystal!And I Hate Tom!"
name_list = ["Jessie", "Tom", "Crystal"]

for fun in dir(a):
    if "__" not in fun:
        print(fun)
